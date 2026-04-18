"""Shioaji (SinoPac 永豐金) concrete OrderManager implementation.

Bridges AbstractOrderManager to the Shioaji API for live Taiwan futures trading.
Delegates connection/auth to BrokerConnector — this module is purely order logic.

Usage:
    from trading_core.broker.shioaji_broker import ShioajiOrderManager
    from trading_core.config import Settings

    settings = Settings.from_env()
    mgr = ShioajiOrderManager(settings=settings)
    order = mgr.place_order("TXF", "BUY", 1, "LIMIT", price=20000.0)
"""

from __future__ import annotations

import logging
import threading
from typing import Dict, Optional

try:
    import shioaji as sj
    import shioaji.constant as sjc
except ImportError:  # pragma: no cover
    sj = None  # type: ignore
    sjc = None  # type: ignore

from trading_core.broker.connector import BrokerConnector
from trading_core.broker.orders import (
    AbstractOrderManager,
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
)
from trading_core.config import Settings

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Mapping tables: abstract model → Shioaji constants
# ---------------------------------------------------------------------------

_SIDE_TO_ACTION: Dict[OrderSide, str] = {
    OrderSide.BUY: "Buy",
    OrderSide.SELL: "Sell",
}

# Map abstract OrderType → (price_type, order_type)
# STOP is not natively supported — handled separately via conditional trigger.
_ORDER_TYPE_MAP: Dict[OrderType, tuple[str, str]] = {
    OrderType.MARKET: ("MKT", "ROD"),
    OrderType.LIMIT: ("LMT", "ROD"),
    # STOP: requires application-level monitoring — see _submit_order docstring
}


def _map_shioaji_status(sj_status: str) -> OrderStatus:
    """Convert a Shioaji trade status string to our OrderStatus enum.

    Shioaji trade.status.status values (observed):
        'PendingSubmit', 'PreSubmitted', 'Submitted' → PENDING
        'Filled'                                     → FILLED
        'PartFilled'                                 → PARTIAL
        'Cancelled'                                  → CANCELLED
        'Failed'                                     → REJECTED

    Args:
        sj_status: Raw status string from Shioaji Trade object.

    Returns:
        Mapped OrderStatus.
    """
    mapping = {
        "PendingSubmit": OrderStatus.PENDING,
        "PreSubmitted": OrderStatus.PENDING,
        "Submitted": OrderStatus.PENDING,
        "Filled": OrderStatus.FILLED,
        "PartFilled": OrderStatus.PARTIAL,
        "Cancelled": OrderStatus.CANCELLED,
        "Failed": OrderStatus.REJECTED,
    }
    result = mapping.get(sj_status, OrderStatus.PENDING)
    if sj_status not in mapping:
        logger.warning("Unknown Shioaji status %r — defaulting to PENDING", sj_status)
    return result


# ---------------------------------------------------------------------------
# ShioajiOrderManager
# ---------------------------------------------------------------------------


class ShioajiOrderManager(AbstractOrderManager):
    """Live broker order manager backed by the Shioaji (SinoPac) API.

    Implements AbstractOrderManager's three abstract hooks:
        _submit_order, _fetch_order_status, _request_cancel

    Also registers an order-deal callback for event-driven fill updates,
    keeping the internal order registry in sync without polling.

    Args:
        settings: Optional Settings instance. Defaults to global settings.
        connector: Optional BrokerConnector (for testing / DI).
        default_octype: Shioaji OCType for futures orders.
                        'Auto' lets the exchange decide (safe default).
                        Use 'New'/'Cover' for explicit position control.

    Notes:
        - STOP orders are not natively supported by Shioaji. Passing
          OrderType.STOP raises NotImplementedError. Implement a price-
          monitor thread above this layer to fire MARKET orders conditionally.
        - All mutations to _orders go through _lock for thread safety.
    """

    def __init__(
        self,
        settings: Optional[Settings] = None,
        connector: Optional[BrokerConnector] = None,
        default_octype: str = "Auto",
    ) -> None:
        super().__init__()
        self._connector = connector or BrokerConnector(settings)
        self._default_octype = default_octype
        self._lock = threading.Lock()

        # broker_ref → Shioaji Trade object (for cancel/update)
        self._trade_registry: Dict[str, object] = {}

        # Register event-driven fill callback
        self._connector.api.set_order_callback(self._on_order_event)
        logger.info("ShioajiOrderManager ready (octype=%s)", default_octype)

    # ------------------------------------------------------------------
    # Abstract hook implementations
    # ------------------------------------------------------------------

    def _submit_order(self, order: Order) -> Order:
        """Submit order to Shioaji and return broker-acknowledged Order.

        Maps abstract Order fields to Shioaji-specific parameters, calls
        api.place_order(), and stores the returned Trade for later use.

        Args:
            order: Validated Order ready for submission.

        Returns:
            Updated Order with broker_ref set to the Shioaji order ID.

        Raises:
            NotImplementedError: If order_type is STOP (not natively supported).
            RuntimeError: On Shioaji API error.
            ImportError: If shioaji package is not installed.
        """
        if sj is None:
            raise ImportError(
                "shioaji package is required for live trading. "
                "Install with: pip install shioaji"
            )

        if order.order_type == OrderType.STOP:
            raise NotImplementedError(
                "STOP orders are not natively supported by Shioaji. "
                "Implement a price-monitoring trigger above this layer."
            )

        api = self._connector.api

        # Resolve contract — near-month futures by default
        contract = self._resolve_contract(api, order.symbol)

        # Build Shioaji Order
        price_type_str, order_type_str = _ORDER_TYPE_MAP[order.order_type]
        sj_order = api.Order(
            price=order.price if order.price is not None else 0,
            quantity=int(order.quantity),
            action=_SIDE_TO_ACTION[order.side],
            price_type=price_type_str,
            order_type=order_type_str,
            octype=self._default_octype,
            account=api.futopt_account,
        )

        logger.debug(
            "Submitting to Shioaji: %s %s %s qty=%s price=%s",
            order.symbol, order.side, order.order_type, order.quantity, order.price,
        )

        try:
            trade = api.place_order(contract, sj_order)
        except Exception as exc:
            raise RuntimeError(
                f"Shioaji place_order failed for {order.symbol}: {exc}"
            ) from exc

        broker_ref = trade.order.id
        logger.info("Shioaji trade submitted: broker_ref=%s", broker_ref)

        with self._lock:
            self._trade_registry[broker_ref] = trade

        return order.with_update(broker_ref=broker_ref)

    def _fetch_order_status(self, order: Order) -> Order:
        """Sync order status from Shioaji exchange.

        Calls update_status to pull latest state, then maps the Shioaji
        status string to our OrderStatus enum.

        Args:
            order: Locally cached Order with broker_ref set.

        Returns:
            Updated Order reflecting current exchange status.
        """
        api = self._connector.api

        try:
            api.update_status(api.futopt_account)
        except Exception as exc:
            logger.warning("update_status failed: %s — returning cached status", exc)
            return order

        with self._lock:
            trade = self._trade_registry.get(order.broker_ref)  # type: ignore[arg-type]

        if trade is None:
            logger.warning(
                "No trade found for broker_ref=%s — returning cached status",
                order.broker_ref,
            )
            return order

        sj_status = str(trade.status.status)
        new_status = _map_shioaji_status(sj_status)

        # Extract fill info if available
        filled_qty: Optional[float] = None
        avg_price: Optional[float] = None
        try:
            filled_qty = float(trade.status.deal_quantity)
            avg_price = float(trade.status.average_price) if trade.status.average_price else None
        except (AttributeError, TypeError, ValueError):
            pass  # fill details not yet available — leave as-is

        return order.with_update(
            status=new_status,
            filled_quantity=filled_qty if filled_qty is not None else order.filled_quantity,
            avg_fill_price=avg_price if avg_price is not None else order.avg_fill_price,
        )

    def _request_cancel(self, order: Order) -> Order:
        """Request cancellation of a live order via Shioaji.

        Args:
            order: Active Order to cancel (must have broker_ref set).

        Returns:
            Updated Order. Status will be CANCELLED on success,
            or unchanged if the broker rejects the cancel.
        """
        api = self._connector.api

        with self._lock:
            trade = self._trade_registry.get(order.broker_ref)  # type: ignore[arg-type]

        if trade is None:
            logger.error(
                "Cannot cancel: no trade in registry for broker_ref=%s",
                order.broker_ref,
            )
            return order

        try:
            api.cancel_order(trade)
            api.update_status(api.futopt_account)
        except Exception as exc:
            logger.error("cancel_order failed for %s: %s", order.broker_ref, exc)
            return order

        # Re-read status after cancel attempt
        sj_status = str(trade.status.status)
        new_status = _map_shioaji_status(sj_status)

        logger.info(
            "Cancel result for %s: Shioaji status=%r → %s",
            order.broker_ref, sj_status, new_status,
        )
        return order.with_update(status=new_status)

    # ------------------------------------------------------------------
    # Event-driven fill callback
    # ------------------------------------------------------------------

    def _on_order_event(self, stat, msg) -> None:  # type: ignore[override]
        """Shioaji order/deal event callback.

        Called by the Shioaji API thread on every order state change or fill.
        Updates the internal _orders registry without blocking the caller.

        Args:
            stat: Shioaji OrderState (FOrder or FDeal).
            msg:  Raw message dict from Shioaji.
        """
        try:
            # Determine broker_ref from the event
            broker_ref: Optional[str] = None
            try:
                broker_ref = stat.order.id  # FOrder
            except AttributeError:
                try:
                    broker_ref = stat.trade_id  # FDeal
                except AttributeError:
                    pass

            if broker_ref is None:
                logger.debug("_on_order_event: could not extract broker_ref from %r", stat)
                return

            with self._lock:
                order = next(
                    (o for o in self._orders.values() if o.broker_ref == broker_ref),
                    None,
                )

            if order is None:
                logger.debug(
                    "_on_order_event: no local order for broker_ref=%s", broker_ref
                )
                return

            # Build updated order from event fields
            updated = self._fetch_order_status(order)

            with self._lock:
                self._orders[order.order_id] = updated

            logger.debug(
                "Event update: order_id=%s broker_ref=%s → %s",
                order.order_id, broker_ref, updated.status,
            )

        except Exception as exc:  # noqa: BLE001
            # Never raise from a callback — log and continue
            logger.exception("_on_order_event error: %s", exc)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _resolve_contract(api: "sj.Shioaji", symbol: str) -> object:  # type: ignore[name-defined]
        """Resolve a symbol string to a Shioaji Contract object.

        Tries Futures first, then Stocks. For futures, uses the near-month
        contract. Override this method to support weekly contracts or options.

        Args:
            api: Authenticated Shioaji API instance.
            symbol: Instrument symbol, e.g. "TXF", "MXF", "2330".

        Returns:
            Shioaji Contract object.

        Raises:
            KeyError: If symbol cannot be resolved.
        """
        # Try futures (monthly near-month)
        try:
            contracts_futures = api.Contracts.Futures.get(symbol)
            if contracts_futures:
                # Near-month: first non-expired contract
                for code, contract in sorted(contracts_futures.items()):
                    return contract
        except (AttributeError, TypeError):
            pass

        # Try stocks
        try:
            return api.Contracts.Stocks[symbol]
        except KeyError:
            pass

        raise KeyError(
            f"Cannot resolve symbol {symbol!r} to a Shioaji contract. "
            "Verify symbol and that contracts are loaded (contracts_cb fired)."
        )
