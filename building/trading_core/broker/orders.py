"""Order management module for trading system.

Provides an abstract broker interface for order lifecycle management:
place, query, cancel, and list orders. Concrete implementations
(e.g. ShioajiOrderManager) extend AbstractOrderManager.
"""

from __future__ import annotations

import logging
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------


class OrderType(str, Enum):
    """Supported order types."""

    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"


class OrderSide(str, Enum):
    """Order side (direction)."""

    BUY = "BUY"
    SELL = "SELL"


class OrderStatus(str, Enum):
    """Lifecycle status of an order."""

    PENDING = "PENDING"       # submitted, not yet acknowledged / filled
    FILLED = "FILLED"         # fully executed
    PARTIAL = "PARTIAL"       # partially executed, still open
    CANCELLED = "CANCELLED"   # cancelled by user or system
    REJECTED = "REJECTED"     # rejected by broker


# ---------------------------------------------------------------------------
# Data transfer objects
# ---------------------------------------------------------------------------


@dataclass
class Order:
    """Immutable representation of a submitted order.

    Attributes:
        order_id:        Unique order identifier (broker-assigned or generated).
        symbol:          Instrument symbol (e.g. "TXF", "BTC-USDT").
        side:            BUY or SELL.
        quantity:        Total order quantity (must be > 0).
        order_type:      MARKET, LIMIT, or STOP.
        price:           Limit / stop price (required for LIMIT/STOP orders).
        status:          Current lifecycle status.
        filled_quantity: Quantity executed so far.
        avg_fill_price:  Volume-weighted average fill price.
        created_at:      Timestamp when the order was created.
        updated_at:      Timestamp of the last status update.
        broker_ref:      Broker-specific reference / metadata (optional).
    """

    symbol: str
    side: OrderSide
    quantity: float
    order_type: OrderType
    price: Optional[float] = None
    status: OrderStatus = OrderStatus.PENDING
    filled_quantity: float = 0.0
    avg_fill_price: Optional[float] = None
    order_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    broker_ref: Optional[str] = None

    def __post_init__(self) -> None:
        """Validate order fields."""
        if self.quantity <= 0:
            raise ValueError(f"quantity must be positive, got {self.quantity}")
        if self.order_type in (OrderType.LIMIT, OrderType.STOP) and self.price is None:
            raise ValueError(
                f"{self.order_type} orders require a price"
            )
        if self.price is not None and self.price <= 0:
            raise ValueError(f"price must be positive, got {self.price}")

    @property
    def is_active(self) -> bool:
        """True when the order can still receive fills or be cancelled."""
        return self.status in (OrderStatus.PENDING, OrderStatus.PARTIAL)

    @property
    def remaining_quantity(self) -> float:
        """Unfilled quantity."""
        return max(0.0, self.quantity - self.filled_quantity)

    def with_update(
        self,
        *,
        status: Optional[OrderStatus] = None,
        filled_quantity: Optional[float] = None,
        avg_fill_price: Optional[float] = None,
        broker_ref: Optional[str] = None,
    ) -> "Order":
        """Return a new Order with updated fields (immutable update).

        Args:
            status:          New status (if changing).
            filled_quantity: New filled quantity (if changing).
            avg_fill_price:  New average fill price (if changing).
            broker_ref:      New broker reference (if changing).

        Returns:
            New Order instance with requested fields updated.
        """
        return Order(
            order_id=self.order_id,
            symbol=self.symbol,
            side=self.side,
            quantity=self.quantity,
            order_type=self.order_type,
            price=self.price,
            status=status if status is not None else self.status,
            filled_quantity=filled_quantity if filled_quantity is not None else self.filled_quantity,
            avg_fill_price=avg_fill_price if avg_fill_price is not None else self.avg_fill_price,
            created_at=self.created_at,
            updated_at=datetime.now(),
            broker_ref=broker_ref if broker_ref is not None else self.broker_ref,
        )


# ---------------------------------------------------------------------------
# Abstract broker interface
# ---------------------------------------------------------------------------


class AbstractOrderManager(ABC):
    """Abstract base class for order management.

    Concrete implementations (e.g. ShioajiOrderManager, PaperOrderManager)
    override the four abstract methods to communicate with a real or simulated
    broker. The in-memory order registry is maintained here.
    """

    def __init__(self) -> None:
        self._orders: Dict[str, Order] = {}
        logger.info("%s initialised", self.__class__.__name__)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def place_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        order_type: str,
        price: Optional[float] = None,
    ) -> Order:
        """Submit a new order to the broker.

        Args:
            symbol:     Instrument symbol (e.g. "TXF").
            side:       "BUY" or "SELL".
            quantity:   Number of contracts / shares / units (> 0).
            order_type: "MARKET", "LIMIT", or "STOP".
            price:      Limit / stop price (required for LIMIT and STOP).

        Returns:
            Order object with assigned order_id and PENDING status.

        Raises:
            ValueError:  On invalid arguments.
            RuntimeError: On broker submission failure.
        """
        order = Order(
            symbol=symbol.upper(),
            side=OrderSide(side.upper()),
            quantity=quantity,
            order_type=OrderType(order_type.upper()),
            price=price,
        )

        logger.info(
            "Placing %s %s %s x%s @ %s",
            order.order_type,
            order.side,
            order.symbol,
            order.quantity,
            order.price if order.price is not None else "MKT",
        )

        submitted = self._submit_order(order)
        self._orders[submitted.order_id] = submitted
        logger.info("Order placed: %s [%s]", submitted.order_id, submitted.status)
        return submitted

    def query_order(self, order_id: str) -> OrderStatus:
        """Query the current status of an order.

        First refreshes the cached order from the broker, then returns status.

        Args:
            order_id: Order identifier returned by place_order().

        Returns:
            Current OrderStatus.

        Raises:
            KeyError: If order_id is not found.
        """
        if order_id not in self._orders:
            raise KeyError(f"Unknown order_id: {order_id!r}")

        refreshed = self._fetch_order_status(self._orders[order_id])
        self._orders[order_id] = refreshed
        return refreshed.status

    def cancel_order(self, order_id: str) -> bool:
        """Request cancellation of an active order.

        Args:
            order_id: Order identifier returned by place_order().

        Returns:
            True if the cancellation was accepted by the broker,
            False if the order is no longer active (already filled/cancelled/rejected).

        Raises:
            KeyError: If order_id is not found.
        """
        if order_id not in self._orders:
            raise KeyError(f"Unknown order_id: {order_id!r}")

        order = self._orders[order_id]
        if not order.is_active:
            logger.warning(
                "cancel_order called on non-active order %s [%s]",
                order_id,
                order.status,
            )
            return False

        cancelled = self._request_cancel(order)
        self._orders[order_id] = cancelled
        accepted = cancelled.status == OrderStatus.CANCELLED
        logger.info("Cancel %s: %s", order_id, "accepted" if accepted else "rejected")
        return accepted

    def list_active_orders(self) -> List[Order]:
        """Return all orders that are currently active (PENDING or PARTIAL).

        Returns:
            List of active Order objects, sorted by creation time (oldest first).
        """
        active = [o for o in self._orders.values() if o.is_active]
        return sorted(active, key=lambda o: o.created_at)

    def get_order(self, order_id: str) -> Order:
        """Retrieve an order by ID (from local cache).

        Args:
            order_id: Order identifier.

        Returns:
            Order object.

        Raises:
            KeyError: If order_id is not found.
        """
        if order_id not in self._orders:
            raise KeyError(f"Unknown order_id: {order_id!r}")
        return self._orders[order_id]

    # ------------------------------------------------------------------
    # Abstract broker hooks (override in concrete implementations)
    # ------------------------------------------------------------------

    @abstractmethod
    def _submit_order(self, order: Order) -> Order:
        """Send the order to the broker and return the broker-acknowledged copy.

        Implementations should:
        1. Call the broker API.
        2. Return a new Order (via order.with_update()) with any broker-assigned
           fields (broker_ref, possibly an updated status).

        Args:
            order: Validated Order ready for submission.

        Returns:
            Updated Order (must retain the same order_id).

        Raises:
            RuntimeError: On unrecoverable submission errors.
        """

    @abstractmethod
    def _fetch_order_status(self, order: Order) -> Order:
        """Fetch fresh order status from the broker.

        Args:
            order: Locally cached Order.

        Returns:
            Updated Order with current broker status.
        """

    @abstractmethod
    def _request_cancel(self, order: Order) -> Order:
        """Ask the broker to cancel the order.

        Args:
            order: Active Order to cancel.

        Returns:
            Updated Order reflecting the broker response
            (status should be CANCELLED on success).
        """


# ---------------------------------------------------------------------------
# Paper / simulation implementation
# ---------------------------------------------------------------------------


class PaperOrderManager(AbstractOrderManager):
    """In-memory paper trading order manager.

    Simulates instant fill at the provided price (or 0.0 for MARKET orders).
    Useful for backtesting, integration tests, and development without a
    live broker connection.

    Args:
        auto_fill:       If True, MARKET orders are immediately filled.
                         LIMIT/STOP orders remain PENDING until explicitly
                         filled via _simulate_fill().
        market_fill_price: Default fill price for MARKET orders.
    """

    def __init__(
        self,
        *,
        auto_fill: bool = True,
        market_fill_price: float = 0.0,
    ) -> None:
        super().__init__()
        self._auto_fill = auto_fill
        self._market_fill_price = market_fill_price

    def _submit_order(self, order: Order) -> Order:
        """Submit order; auto-fill MARKET orders when auto_fill is True."""
        ref = f"PAPER-{order.order_id[:8]}"
        submitted = order.with_update(broker_ref=ref)

        if self._auto_fill and order.order_type == OrderType.MARKET:
            fill_price = self._market_fill_price or (order.price or 0.0)
            submitted = submitted.with_update(
                status=OrderStatus.FILLED,
                filled_quantity=order.quantity,
                avg_fill_price=fill_price,
            )
            logger.debug(
                "Paper auto-fill: %s @ %.4f", order.order_id, fill_price
            )

        return submitted

    def _fetch_order_status(self, order: Order) -> Order:
        """Paper broker: status does not change externally — return as-is."""
        return order

    def _request_cancel(self, order: Order) -> Order:
        """Paper broker: always accepts cancellation of active orders."""
        return order.with_update(status=OrderStatus.CANCELLED)

    def simulate_fill(
        self,
        order_id: str,
        fill_price: float,
        fill_quantity: Optional[float] = None,
    ) -> Order:
        """Manually simulate a (partial) fill for testing purposes.

        Args:
            order_id:      Target order.
            fill_price:    Price of this fill.
            fill_quantity: Quantity filled in this call; defaults to full remaining.

        Returns:
            Updated Order.

        Raises:
            KeyError:   If order_id not found.
            ValueError: If order is not active or fill_quantity is invalid.
        """
        if order_id not in self._orders:
            raise KeyError(f"Unknown order_id: {order_id!r}")

        order = self._orders[order_id]
        if not order.is_active:
            raise ValueError(
                f"Order {order_id} is not active (status={order.status})"
            )

        qty = fill_quantity if fill_quantity is not None else order.remaining_quantity
        if qty <= 0 or qty > order.remaining_quantity:
            raise ValueError(
                f"fill_quantity {qty} invalid "
                f"(remaining={order.remaining_quantity})"
            )

        new_filled = order.filled_quantity + qty
        # Compute running weighted-average fill price
        if order.avg_fill_price is None:
            new_avg = fill_price
        else:
            new_avg = (
                order.avg_fill_price * order.filled_quantity + fill_price * qty
            ) / new_filled

        new_status = (
            OrderStatus.FILLED
            if new_filled >= order.quantity
            else OrderStatus.PARTIAL
        )

        updated = order.with_update(
            status=new_status,
            filled_quantity=new_filled,
            avg_fill_price=new_avg,
        )
        self._orders[order_id] = updated
        return updated


# ---------------------------------------------------------------------------
# Convenience factory
# ---------------------------------------------------------------------------


def create_order_manager(
    broker: str = "paper",
    **kwargs,
) -> AbstractOrderManager:
    """Factory function to create an order manager.

    Args:
        broker: Broker identifier: "paper" (default) or "shioaji".
        **kwargs: Forwarded to the concrete manager constructor.

    Returns:
        AbstractOrderManager instance.

    Raises:
        ValueError: If broker string is not recognised.
    """
    broker = broker.lower()
    if broker == "paper":
        return PaperOrderManager(**kwargs)
    raise ValueError(
        f"Unknown broker {broker!r}. "
        "Available: 'paper'. "
        "For live brokers, import ShioajiOrderManager directly."
    )
