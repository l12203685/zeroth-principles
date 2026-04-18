"""Tests for ShioajiOrderManager (broker/shioaji_broker.py).

All Shioaji API calls are mocked via a fake BrokerConnector so these tests
run without a live SinoPac account or the shioaji package installed.

Coverage targets:
  - _submit_order (MARKET, LIMIT, STOP→NotImplementedError)
  - _fetch_order_status (all status mappings, missing trade, update_status failure)
  - _request_cancel (happy-path, missing trade, cancel exception)
  - _on_order_event (FOrder path, FDeal path, unknown broker_ref, exception safety)
  - _resolve_contract (futures, stocks, unknown symbol)
  - create_order_manager("shioaji") factory
  - Error cases: shioaji not installed, connection failure, invalid contract
"""

from __future__ import annotations

import threading
from types import SimpleNamespace
from typing import Any, Optional
from unittest.mock import MagicMock, patch, PropertyMock

import pytest

from trading_core.broker.orders import (
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
    create_order_manager,
)
from trading_core.broker.shioaji_broker import (
    ShioajiOrderManager,
    _map_shioaji_status,
)
from trading_core.config import Settings


# ---------------------------------------------------------------------------
# Module-level autouse fixture: patch sj to non-None so the guard passes
# ---------------------------------------------------------------------------

# A minimal fake shioaji module sentinel — just needs to be truthy.
_FAKE_SJ = MagicMock(name="shioaji_module")


@pytest.fixture(autouse=True)
def _patch_sj():
    """Patch the module-level `sj` reference to a sentinel so the
    ``if sj is None`` guard in _submit_order never fires (unless a specific
    test overrides it with None to test that branch)."""
    with patch("trading_core.broker.shioaji_broker.sj", _FAKE_SJ):
        yield


# ---------------------------------------------------------------------------
# Helpers / Fixtures
# ---------------------------------------------------------------------------


def _make_settings() -> Settings:
    """Return a minimal Settings with fake credentials (no I/O)."""
    return Settings(
        broker_api_key="TEST_KEY",
        broker_secret="TEST_SECRET",
        broker_person_id="A123456789",
        broker_ca_path="",
        market_data_dir="/tmp/tc_test_data",
        log_dir="/tmp/tc_test_logs",
    )


def _make_trade(
    order_id: str = "SJ-001",
    status_str: str = "Submitted",
    deal_quantity: float = 0.0,
    average_price: Optional[float] = None,
) -> SimpleNamespace:
    """Build a fake Shioaji Trade object mirroring the attrs ShioajiOrderManager reads."""
    trade_status = SimpleNamespace(
        status=status_str,
        deal_quantity=deal_quantity,
        average_price=average_price,
    )
    trade_order = SimpleNamespace(id=order_id)
    return SimpleNamespace(order=trade_order, status=trade_status)


def _make_api(
    trade: Optional[SimpleNamespace] = None,
    place_order_side_effect=None,
    cancel_order_side_effect=None,
    update_status_side_effect=None,
) -> MagicMock:
    """Build a fake shioaji API object."""
    api = MagicMock()
    api.futopt_account = MagicMock()

    # place_order returns a trade
    _trade = trade or _make_trade()
    if place_order_side_effect:
        api.place_order.side_effect = place_order_side_effect
    else:
        api.place_order.return_value = _trade

    if cancel_order_side_effect:
        api.cancel_order.side_effect = cancel_order_side_effect

    if update_status_side_effect:
        api.update_status.side_effect = update_status_side_effect

    # api.Order builds a plain object; we don't inspect its fields
    api.Order.return_value = MagicMock()

    # Default: Futures.get returns None (no futures contracts)
    api.Contracts.Futures.get.return_value = None

    return api


def _make_connector(api: MagicMock) -> MagicMock:
    """Return a mock BrokerConnector whose .api property returns the given api."""
    connector = MagicMock()
    type(connector).api = PropertyMock(return_value=api)
    return connector


def _make_manager(
    api: Optional[MagicMock] = None,
    trade: Optional[SimpleNamespace] = None,
    place_order_side_effect=None,
    cancel_order_side_effect=None,
    update_status_side_effect=None,
) -> ShioajiOrderManager:
    """Convenience: build a fully-mocked ShioajiOrderManager."""
    _api = api or _make_api(
        trade=trade,
        place_order_side_effect=place_order_side_effect,
        cancel_order_side_effect=cancel_order_side_effect,
        update_status_side_effect=update_status_side_effect,
    )
    connector = _make_connector(_api)
    # Patch BrokerConnector so __init__ never hits real settings validation
    with patch(
        "trading_core.broker.shioaji_broker.BrokerConnector",
        return_value=connector,
    ):
        mgr = ShioajiOrderManager(settings=_make_settings())
    # Expose the api for post-call assertions
    mgr._test_api = _api
    return mgr


# ---------------------------------------------------------------------------
# _map_shioaji_status unit tests
# ---------------------------------------------------------------------------


class TestMapShioajiStatus:
    @pytest.mark.parametrize(
        "sj_status, expected",
        [
            ("PendingSubmit", OrderStatus.PENDING),
            ("PreSubmitted", OrderStatus.PENDING),
            ("Submitted", OrderStatus.PENDING),
            ("Filled", OrderStatus.FILLED),
            ("PartFilled", OrderStatus.PARTIAL),
            ("Cancelled", OrderStatus.CANCELLED),
            ("Failed", OrderStatus.REJECTED),
        ],
    )
    def test_known_statuses(self, sj_status: str, expected: OrderStatus) -> None:
        assert _map_shioaji_status(sj_status) == expected

    def test_unknown_status_defaults_to_pending(self) -> None:
        result = _map_shioaji_status("SomeUnknownStatus")
        assert result == OrderStatus.PENDING

    def test_unknown_status_logs_warning(self, caplog) -> None:
        import logging
        with caplog.at_level(logging.WARNING, logger="trading_core.broker.shioaji_broker"):
            _map_shioaji_status("WeirdStatus")
        assert "WeirdStatus" in caplog.text


# ---------------------------------------------------------------------------
# ShioajiOrderManager — place_order (MARKET)
# ---------------------------------------------------------------------------


class TestPlaceMarketOrder:
    def test_market_order_returns_pending_with_broker_ref(self) -> None:
        trade = _make_trade(order_id="SJ-MARKET-01", status_str="Submitted")
        mgr = _make_manager(trade=trade)

        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        assert order.broker_ref == "SJ-MARKET-01"
        assert order.status == OrderStatus.PENDING
        assert order.symbol == "TXF"
        assert order.side == OrderSide.BUY
        assert order.quantity == 1.0

    def test_market_order_calls_api_place_order(self) -> None:
        trade = _make_trade(order_id="SJ-CALL-CHECK")
        mgr = _make_manager(trade=trade)

        mgr.place_order("MXF", "SELL", 2, "MARKET")

        assert mgr._test_api.place_order.call_count == 1

    def test_market_order_trade_stored_in_registry(self) -> None:
        trade = _make_trade(order_id="REG-TEST-01")
        mgr = _make_manager(trade=trade)

        mgr.place_order("TXF", "BUY", 1, "MARKET")

        assert "REG-TEST-01" in mgr._trade_registry

    def test_market_order_symbol_normalised(self) -> None:
        trade = _make_trade(order_id="NORM-01")
        mgr = _make_manager(trade=trade)

        order = mgr.place_order("txf", "buy", 1, "market")

        assert order.symbol == "TXF"
        assert order.side == OrderSide.BUY

    def test_sell_market_order(self) -> None:
        trade = _make_trade(order_id="SELL-01")
        mgr = _make_manager(trade=trade)

        order = mgr.place_order("TXF", "SELL", 3, "MARKET")

        assert order.side == OrderSide.SELL
        assert order.quantity == 3.0


# ---------------------------------------------------------------------------
# ShioajiOrderManager — place_order (LIMIT)
# ---------------------------------------------------------------------------


class TestPlaceLimitOrder:
    def test_limit_order_sets_broker_ref(self) -> None:
        trade = _make_trade(order_id="SJ-LIMIT-01", status_str="Submitted")
        mgr = _make_manager(trade=trade)

        order = mgr.place_order("TXF", "BUY", 1, "LIMIT", price=20000.0)

        assert order.broker_ref == "SJ-LIMIT-01"
        assert order.order_type == OrderType.LIMIT
        assert order.price == 20000.0

    def test_limit_order_requires_price(self) -> None:
        mgr = _make_manager()
        with pytest.raises(ValueError, match="require a price"):
            mgr.place_order("TXF", "BUY", 1, "LIMIT")

    def test_limit_order_api_order_built_with_price(self) -> None:
        trade = _make_trade(order_id="PRICE-CHECK")
        mgr = _make_manager(trade=trade)

        mgr.place_order("TXF", "BUY", 2, "LIMIT", price=19500.0)

        call_kwargs = mgr._test_api.Order.call_args
        # price kwarg must be 19500.0
        assert call_kwargs.kwargs.get("price") == 19500.0 or (
            call_kwargs.args and call_kwargs.args[0] == 19500.0
        )


# ---------------------------------------------------------------------------
# ShioajiOrderManager — STOP order raises NotImplementedError
# ---------------------------------------------------------------------------


class TestStopOrderNotSupported:
    def test_stop_order_raises_not_implemented(self) -> None:
        mgr = _make_manager()
        with pytest.raises(NotImplementedError, match="STOP"):
            mgr.place_order("TXF", "BUY", 1, "STOP", price=19000.0)


# ---------------------------------------------------------------------------
# ShioajiOrderManager — place_order error cases
# ---------------------------------------------------------------------------


class TestPlaceOrderErrors:
    def test_api_exception_wrapped_as_runtime_error(self) -> None:
        mgr = _make_manager(
            place_order_side_effect=Exception("Network timeout")
        )
        with pytest.raises(RuntimeError, match="Shioaji place_order failed"):
            mgr.place_order("TXF", "BUY", 1, "MARKET")

    def test_invalid_side_raises_value_error(self) -> None:
        mgr = _make_manager()
        with pytest.raises(ValueError):
            mgr.place_order("TXF", "HOLD", 1, "MARKET")

    def test_invalid_order_type_raises_value_error(self) -> None:
        mgr = _make_manager()
        with pytest.raises(ValueError):
            mgr.place_order("TXF", "BUY", 1, "TWAP")

    def test_zero_quantity_raises_value_error(self) -> None:
        mgr = _make_manager()
        with pytest.raises(ValueError, match="quantity must be positive"):
            mgr.place_order("TXF", "BUY", 0, "MARKET")

    def test_shioaji_not_installed_raises_import_error(self) -> None:
        """When sj is None (package missing), _submit_order raises ImportError."""
        mgr = _make_manager()
        # Override the autouse patch to inject None for this one test
        with patch("trading_core.broker.shioaji_broker.sj", None):
            with pytest.raises(ImportError, match="shioaji package"):
                mgr.place_order("TXF", "BUY", 1, "MARKET")


# ---------------------------------------------------------------------------
# ShioajiOrderManager — query_order / _fetch_order_status
# ---------------------------------------------------------------------------


class TestQueryOrder:
    def _setup_with_trade(
        self, status_str: str, deal_qty: float = 0.0, avg_price: Optional[float] = None
    ) -> tuple[ShioajiOrderManager, str]:
        """Place a MARKET order then update the fake trade status for query tests."""
        trade = _make_trade(
            order_id="QRY-001",
            status_str="Submitted",
            deal_quantity=0.0,
            average_price=None,
        )
        mgr = _make_manager(trade=trade)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        # Mutate the in-place fake trade to simulate broker update
        trade.status.status = status_str
        trade.status.deal_quantity = deal_qty
        trade.status.average_price = avg_price

        return mgr, order.order_id

    def test_query_submitted_returns_pending(self) -> None:
        mgr, oid = self._setup_with_trade("Submitted")
        assert mgr.query_order(oid) == OrderStatus.PENDING

    def test_query_filled_returns_filled(self) -> None:
        mgr, oid = self._setup_with_trade("Filled", deal_qty=1.0, avg_price=20100.0)
        assert mgr.query_order(oid) == OrderStatus.FILLED

    def test_query_part_filled_returns_partial(self) -> None:
        mgr, oid = self._setup_with_trade("PartFilled", deal_qty=0.5)
        assert mgr.query_order(oid) == OrderStatus.PARTIAL

    def test_query_cancelled_returns_cancelled(self) -> None:
        mgr, oid = self._setup_with_trade("Cancelled")
        assert mgr.query_order(oid) == OrderStatus.CANCELLED

    def test_query_failed_returns_rejected(self) -> None:
        mgr, oid = self._setup_with_trade("Failed")
        assert mgr.query_order(oid) == OrderStatus.REJECTED

    def test_query_updates_fill_info(self) -> None:
        mgr, oid = self._setup_with_trade("Filled", deal_qty=2.0, avg_price=20050.0)
        mgr.query_order(oid)
        updated = mgr.get_order(oid)
        assert updated.filled_quantity == 2.0
        assert updated.avg_fill_price == pytest.approx(20050.0)

    def test_query_unknown_order_raises_key_error(self) -> None:
        mgr = _make_manager()
        with pytest.raises(KeyError):
            mgr.query_order("no-such-id")

    def test_update_status_failure_returns_cached(self) -> None:
        """If api.update_status raises, query_order returns cached status."""
        trade = _make_trade(order_id="FAIL-001", status_str="Submitted")
        mgr = _make_manager(
            trade=trade,
            update_status_side_effect=RuntimeError("API down"),
        )
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")
        # Status should remain PENDING (cached) despite update_status failing
        status = mgr.query_order(order.order_id)
        assert status == OrderStatus.PENDING

    def test_missing_trade_in_registry_returns_cached(self) -> None:
        """If broker_ref not in _trade_registry, cached status returned."""
        trade = _make_trade(order_id="MISS-001", status_str="Submitted")
        mgr = _make_manager(trade=trade)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        # Manually remove from registry
        mgr._trade_registry.clear()

        status = mgr.query_order(order.order_id)
        assert status == OrderStatus.PENDING  # original cached status


# ---------------------------------------------------------------------------
# ShioajiOrderManager — cancel_order / _request_cancel
# ---------------------------------------------------------------------------


class TestCancelOrder:
    def test_cancel_pending_order_calls_api(self) -> None:
        trade = _make_trade(order_id="CXL-001", status_str="Submitted")
        mgr = _make_manager(trade=trade)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        # Simulate broker accepting cancel: update trade status
        trade.status.status = "Cancelled"
        result = mgr.cancel_order(order.order_id)

        mgr._test_api.cancel_order.assert_called_once()
        assert result is True

    def test_cancel_returns_true_when_status_cancelled(self) -> None:
        trade = _make_trade(order_id="CXL-002", status_str="Submitted")
        mgr = _make_manager(trade=trade)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        trade.status.status = "Cancelled"
        result = mgr.cancel_order(order.order_id)

        assert result is True

    def test_cancel_returns_false_when_broker_did_not_cancel(self) -> None:
        """Broker refuses cancel — trade status stays Submitted → PENDING → not CANCELLED → False."""
        trade = _make_trade(order_id="CXL-003", status_str="Submitted")
        mgr = _make_manager(trade=trade)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        # Trade status stays Submitted after cancel attempt → maps to PENDING
        result = mgr.cancel_order(order.order_id)

        assert result is False

    def test_cancel_unknown_order_raises_key_error(self) -> None:
        mgr = _make_manager()
        with pytest.raises(KeyError):
            mgr.cancel_order("nonexistent")

    def test_cancel_filled_order_returns_false_without_api_call(self) -> None:
        """AbstractOrderManager short-circuits on non-active orders."""
        trade = _make_trade(order_id="FILLED-CXL", status_str="Filled")
        mgr = _make_manager(trade=trade)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        # Force order to FILLED in the registry
        mgr._orders[order.order_id] = order.with_update(status=OrderStatus.FILLED)

        result = mgr.cancel_order(order.order_id)

        assert result is False
        mgr._test_api.cancel_order.assert_not_called()

    def test_cancel_missing_trade_in_registry_no_api_call(self) -> None:
        trade = _make_trade(order_id="MISS-CXL-01", status_str="Submitted")
        mgr = _make_manager(trade=trade)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        mgr._trade_registry.clear()

        result = mgr.cancel_order(order.order_id)

        mgr._test_api.cancel_order.assert_not_called()
        # Original status still PENDING → is_active → but _request_cancel returns unchanged
        assert result is False

    def test_cancel_api_exception_returns_false(self) -> None:
        trade = _make_trade(order_id="EXC-CXL-01", status_str="Submitted")
        mgr = _make_manager(
            trade=trade,
            cancel_order_side_effect=RuntimeError("Broker error"),
        )
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        result = mgr.cancel_order(order.order_id)

        assert result is False


# ---------------------------------------------------------------------------
# ShioajiOrderManager — _on_order_event callback
# ---------------------------------------------------------------------------


class TestOnOrderEvent:
    def test_ford_event_updates_status(self) -> None:
        """FOrder stat (has stat.order.id) triggers status refresh."""
        trade = _make_trade(order_id="EVT-001", status_str="Submitted")
        mgr = _make_manager(trade=trade)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        # Mutate trade to Filled before firing callback
        trade.status.status = "Filled"
        trade.status.deal_quantity = 1.0
        trade.status.average_price = 20000.0

        # Simulate FOrder stat (has .order.id)
        stat = SimpleNamespace(order=SimpleNamespace(id="EVT-001"))
        mgr._on_order_event(stat, {})

        updated = mgr.get_order(order.order_id)
        assert updated.status == OrderStatus.FILLED

    def test_fdeal_event_updates_status(self) -> None:
        """FDeal stat (has stat.trade_id) triggers status refresh."""
        trade = _make_trade(order_id="DEAL-001", status_str="Submitted")
        mgr = _make_manager(trade=trade)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        trade.status.status = "PartFilled"
        trade.status.deal_quantity = 0.5

        # Simulate FDeal stat (no .order.id, has .trade_id)
        stat = SimpleNamespace(trade_id="DEAL-001")
        mgr._on_order_event(stat, {})

        updated = mgr.get_order(order.order_id)
        assert updated.status == OrderStatus.PARTIAL

    def test_unknown_broker_ref_event_is_silently_ignored(self) -> None:
        """Event for unknown broker_ref must not raise."""
        trade = _make_trade(order_id="KNOWN-001")
        mgr = _make_manager(trade=trade)
        mgr.place_order("TXF", "BUY", 1, "MARKET")

        stat = SimpleNamespace(order=SimpleNamespace(id="UNKNOWN-REF"))
        mgr._on_order_event(stat, {})  # must not raise

    def test_stat_without_order_or_trade_id_is_silently_ignored(self) -> None:
        """Stat with neither .order.id nor .trade_id must not raise."""
        mgr = _make_manager()
        stat = SimpleNamespace()  # has neither attribute
        mgr._on_order_event(stat, {})  # must not raise

    def test_callback_exception_does_not_propagate(self) -> None:
        """Internal exception inside callback must be swallowed (never raise)."""
        trade = _make_trade(order_id="SAFE-001")
        mgr = _make_manager(trade=trade)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        # Corrupt the registry to trigger an exception path inside callback
        mgr._orders[order.order_id] = "CORRUPT_NOT_AN_ORDER"  # type: ignore[assignment]

        stat = SimpleNamespace(order=SimpleNamespace(id="SAFE-001"))
        mgr._on_order_event(stat, {})  # must not raise

    def test_callback_is_thread_safe(self) -> None:
        """Fire many events from multiple threads — no deadlock or corruption."""
        trade = _make_trade(order_id="THREAD-001", status_str="Submitted")
        mgr = _make_manager(trade=trade)
        mgr.place_order("TXF", "BUY", 1, "MARKET")

        errors: list[Exception] = []

        def fire_events():
            for _ in range(20):
                stat = SimpleNamespace(order=SimpleNamespace(id="THREAD-001"))
                try:
                    mgr._on_order_event(stat, {})
                except Exception as exc:  # noqa: BLE001
                    errors.append(exc)

        threads = [threading.Thread(target=fire_events) for _ in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=5)

        assert not errors, f"Thread errors: {errors}"


# ---------------------------------------------------------------------------
# ShioajiOrderManager — _resolve_contract
# ---------------------------------------------------------------------------


class TestResolveContract:
    def test_resolves_futures_contract(self) -> None:
        fake_contract = object()
        api = _make_api()
        # _resolve_contract calls api.Contracts.Futures.get(symbol)
        # which must return a non-empty dict for futures to be resolved
        api.Contracts.Futures.get.return_value = {"202501": fake_contract}

        resolved = ShioajiOrderManager._resolve_contract(api, "TXF")
        assert resolved is fake_contract

    def test_resolves_stock_fallback(self) -> None:
        fake_stock = object()
        api = _make_api()
        # Futures miss
        api.Contracts.Futures.get.return_value = None
        # Stocks hit
        api.Contracts.Stocks.__getitem__ = MagicMock(return_value=fake_stock)

        resolved = ShioajiOrderManager._resolve_contract(api, "2330")
        assert resolved is fake_stock

    def test_stock_fallback_when_futures_empty_dict(self) -> None:
        """An empty futures dict also falls through to stocks."""
        fake_stock = object()
        api = _make_api()
        api.Contracts.Futures.get.return_value = {}  # empty → no near-month
        api.Contracts.Stocks.__getitem__ = MagicMock(return_value=fake_stock)

        resolved = ShioajiOrderManager._resolve_contract(api, "2330")
        assert resolved is fake_stock

    def test_unknown_symbol_raises_key_error(self) -> None:
        api = _make_api()
        api.Contracts.Futures.get.return_value = None
        api.Contracts.Stocks.__getitem__ = MagicMock(side_effect=KeyError("NONEXISTENT"))

        with pytest.raises(KeyError, match="Cannot resolve symbol"):
            ShioajiOrderManager._resolve_contract(api, "NONEXISTENT")


# ---------------------------------------------------------------------------
# create_order_manager factory — shioaji path
# ---------------------------------------------------------------------------


class TestCreateOrderManagerShioaji:
    def test_factory_returns_shioaji_manager(self) -> None:
        connector = _make_connector(_make_api())
        with patch(
            "trading_core.broker.shioaji_broker.BrokerConnector",
            return_value=connector,
        ):
            mgr = create_order_manager(
                "shioaji",
                settings=_make_settings(),
            )
        assert isinstance(mgr, ShioajiOrderManager)

    def test_factory_case_insensitive(self) -> None:
        connector = _make_connector(_make_api())
        with patch(
            "trading_core.broker.shioaji_broker.BrokerConnector",
            return_value=connector,
        ):
            mgr = create_order_manager(
                "SHIOAJI",
                settings=_make_settings(),
            )
        assert isinstance(mgr, ShioajiOrderManager)

    def test_factory_unknown_broker_raises(self) -> None:
        from trading_core.broker.orders import create_order_manager as factory

        with pytest.raises(ValueError, match="Unknown broker"):
            factory("interactive_brokers")


# ---------------------------------------------------------------------------
# Connection / BrokerConnector failure
# ---------------------------------------------------------------------------


class TestConnectionFailure:
    def test_broker_connector_init_failure_propagates(self) -> None:
        """If BrokerConnector raises on construction, ShioajiOrderManager propagates."""
        with patch(
            "trading_core.broker.shioaji_broker.BrokerConnector",
            side_effect=ConnectionError("Login failed"),
        ):
            with pytest.raises(ConnectionError, match="Login failed"):
                ShioajiOrderManager(settings=_make_settings())


# ---------------------------------------------------------------------------
# ShioajiOrderManager — list_active_orders integration
# ---------------------------------------------------------------------------


class TestListActiveOrders:
    def test_placed_orders_appear_in_active_list(self) -> None:
        trade1 = _make_trade(order_id="ACT-001", status_str="Submitted")
        mgr = _make_manager(trade=trade1)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        active = mgr.list_active_orders()
        assert any(o.order_id == order.order_id for o in active)

    def test_filled_orders_not_in_active_list(self) -> None:
        trade = _make_trade(order_id="FILL-ACT-01", status_str="Filled")
        mgr = _make_manager(trade=trade)
        order = mgr.place_order("TXF", "BUY", 1, "MARKET")

        # Force filled status in registry
        mgr._orders[order.order_id] = order.with_update(status=OrderStatus.FILLED)

        active = mgr.list_active_orders()
        assert not any(o.order_id == order.order_id for o in active)
