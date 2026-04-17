"""Tests for broker/orders.py — order management module.

Coverage targets: OrderType, OrderSide, OrderStatus enums; Order dataclass;
AbstractOrderManager public API; PaperOrderManager; create_order_manager factory.
"""

from __future__ import annotations

import uuid
from datetime import datetime

import pytest

from trading_core.broker.orders import (
    AbstractOrderManager,
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
    PaperOrderManager,
    create_order_manager,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _paper(auto_fill: bool = True, market_fill_price: float = 0.0) -> PaperOrderManager:
    return PaperOrderManager(auto_fill=auto_fill, market_fill_price=market_fill_price)


def _place(
    mgr: AbstractOrderManager,
    symbol: str = "TXF",
    side: str = "BUY",
    quantity: float = 1.0,
    order_type: str = "MARKET",
    price: float | None = None,
) -> Order:
    return mgr.place_order(symbol, side, quantity, order_type, price)


# ===========================================================================
# Enum tests
# ===========================================================================


class TestEnums:
    def test_order_type_values(self) -> None:
        assert OrderType.MARKET == "MARKET"
        assert OrderType.LIMIT == "LIMIT"
        assert OrderType.STOP == "STOP"

    def test_order_side_values(self) -> None:
        assert OrderSide.BUY == "BUY"
        assert OrderSide.SELL == "SELL"

    def test_order_status_values(self) -> None:
        expected = {"PENDING", "FILLED", "PARTIAL", "CANCELLED", "REJECTED"}
        assert {s.value for s in OrderStatus} == expected

    def test_enum_case_insensitive_via_manager(self) -> None:
        """place_order normalises side/order_type strings."""
        mgr = _paper()
        order = _place(mgr, side="buy", order_type="market")
        assert order.side == OrderSide.BUY
        assert order.order_type == OrderType.MARKET


# ===========================================================================
# Order dataclass tests
# ===========================================================================


class TestOrderDataclass:
    def test_defaults(self) -> None:
        o = Order(
            symbol="TXF",
            side=OrderSide.BUY,
            quantity=2.0,
            order_type=OrderType.MARKET,
        )
        assert o.status == OrderStatus.PENDING
        assert o.filled_quantity == 0.0
        assert o.avg_fill_price is None
        assert o.price is None
        assert o.broker_ref is None
        assert isinstance(o.order_id, str) and len(o.order_id) == 36  # UUID4

    def test_unique_order_ids(self) -> None:
        ids = {
            Order(
                symbol="X", side=OrderSide.BUY, quantity=1.0, order_type=OrderType.MARKET
            ).order_id
            for _ in range(100)
        }
        assert len(ids) == 100

    def test_validation_zero_quantity(self) -> None:
        with pytest.raises(ValueError, match="quantity must be positive"):
            Order(symbol="X", side=OrderSide.BUY, quantity=0, order_type=OrderType.MARKET)

    def test_validation_negative_quantity(self) -> None:
        with pytest.raises(ValueError, match="quantity must be positive"):
            Order(symbol="X", side=OrderSide.BUY, quantity=-1, order_type=OrderType.MARKET)

    def test_limit_order_requires_price(self) -> None:
        with pytest.raises(ValueError, match="require a price"):
            Order(
                symbol="X", side=OrderSide.BUY, quantity=1, order_type=OrderType.LIMIT
            )

    def test_stop_order_requires_price(self) -> None:
        with pytest.raises(ValueError, match="require a price"):
            Order(
                symbol="X", side=OrderSide.SELL, quantity=1, order_type=OrderType.STOP
            )

    def test_non_positive_price_rejected(self) -> None:
        with pytest.raises(ValueError, match="price must be positive"):
            Order(
                symbol="X",
                side=OrderSide.BUY,
                quantity=1,
                order_type=OrderType.LIMIT,
                price=0.0,
            )

    def test_valid_limit_order(self) -> None:
        o = Order(
            symbol="TXF",
            side=OrderSide.SELL,
            quantity=5.0,
            order_type=OrderType.LIMIT,
            price=18000.0,
        )
        assert o.price == 18000.0

    def test_is_active_pending(self) -> None:
        o = Order(symbol="X", side=OrderSide.BUY, quantity=1, order_type=OrderType.MARKET)
        assert o.is_active is True

    def test_is_active_partial(self) -> None:
        o = Order(
            symbol="X",
            side=OrderSide.BUY,
            quantity=2,
            order_type=OrderType.MARKET,
            status=OrderStatus.PARTIAL,
            filled_quantity=1,
        )
        assert o.is_active is True

    @pytest.mark.parametrize(
        "status",
        [OrderStatus.FILLED, OrderStatus.CANCELLED, OrderStatus.REJECTED],
    )
    def test_is_active_terminal(self, status: OrderStatus) -> None:
        o = Order(
            symbol="X",
            side=OrderSide.BUY,
            quantity=1,
            order_type=OrderType.MARKET,
            status=status,
        )
        assert o.is_active is False

    def test_remaining_quantity_full(self) -> None:
        o = Order(symbol="X", side=OrderSide.BUY, quantity=3, order_type=OrderType.MARKET)
        assert o.remaining_quantity == 3.0

    def test_remaining_quantity_partial(self) -> None:
        o = Order(
            symbol="X",
            side=OrderSide.BUY,
            quantity=10,
            order_type=OrderType.MARKET,
            status=OrderStatus.PARTIAL,
            filled_quantity=3,
        )
        assert o.remaining_quantity == 7.0

    def test_with_update_immutability(self) -> None:
        original = Order(
            symbol="TXF", side=OrderSide.BUY, quantity=1, order_type=OrderType.MARKET
        )
        updated = original.with_update(status=OrderStatus.FILLED)
        assert original.status == OrderStatus.PENDING  # unchanged
        assert updated.status == OrderStatus.FILLED
        assert updated.order_id == original.order_id

    def test_with_update_preserves_fields(self) -> None:
        original = Order(
            symbol="TXF",
            side=OrderSide.BUY,
            quantity=2,
            order_type=OrderType.LIMIT,
            price=18000.0,
        )
        updated = original.with_update(filled_quantity=1.0, avg_fill_price=17999.0)
        assert updated.symbol == "TXF"
        assert updated.price == 18000.0
        assert updated.filled_quantity == 1.0
        assert updated.avg_fill_price == 17999.0

    def test_with_update_updated_at_changes(self) -> None:
        original = Order(
            symbol="X", side=OrderSide.BUY, quantity=1, order_type=OrderType.MARKET
        )
        updated = original.with_update(status=OrderStatus.FILLED)
        # updated_at must be >= created_at
        assert updated.updated_at >= original.created_at


# ===========================================================================
# PaperOrderManager — place_order
# ===========================================================================


class TestPaperPlaceOrder:
    def test_market_order_auto_fill(self) -> None:
        mgr = _paper(auto_fill=True, market_fill_price=18500.0)
        order = _place(mgr, order_type="MARKET")
        assert order.status == OrderStatus.FILLED
        assert order.filled_quantity == 1.0
        assert order.avg_fill_price == 18500.0

    def test_market_order_no_auto_fill(self) -> None:
        mgr = _paper(auto_fill=False)
        order = _place(mgr)
        assert order.status == OrderStatus.PENDING
        assert order.filled_quantity == 0.0

    def test_limit_order_stays_pending(self) -> None:
        mgr = _paper(auto_fill=True)
        order = _place(mgr, order_type="LIMIT", price=18000.0)
        assert order.status == OrderStatus.PENDING

    def test_stop_order_stays_pending(self) -> None:
        mgr = _paper(auto_fill=True)
        order = _place(mgr, order_type="STOP", price=17500.0)
        assert order.status == OrderStatus.PENDING

    def test_sell_market_order(self) -> None:
        mgr = _paper(auto_fill=True, market_fill_price=18000.0)
        order = _place(mgr, side="SELL")
        assert order.side == OrderSide.SELL
        assert order.status == OrderStatus.FILLED

    def test_symbol_normalised_to_uppercase(self) -> None:
        mgr = _paper()
        order = _place(mgr, symbol="txf")
        assert order.symbol == "TXF"

    def test_broker_ref_assigned(self) -> None:
        mgr = _paper()
        order = _place(mgr)
        assert order.broker_ref is not None
        assert order.broker_ref.startswith("PAPER-")

    def test_invalid_side_raises(self) -> None:
        mgr = _paper()
        with pytest.raises(ValueError):
            mgr.place_order("TXF", "HOLD", 1, "MARKET")

    def test_invalid_order_type_raises(self) -> None:
        mgr = _paper()
        with pytest.raises(ValueError):
            mgr.place_order("TXF", "BUY", 1, "TWAP")

    def test_zero_quantity_raises(self) -> None:
        mgr = _paper()
        with pytest.raises(ValueError):
            mgr.place_order("TXF", "BUY", 0, "MARKET")


# ===========================================================================
# PaperOrderManager — query_order
# ===========================================================================


class TestPaperQueryOrder:
    def test_query_filled(self) -> None:
        mgr = _paper(market_fill_price=1000.0)
        order = _place(mgr)
        status = mgr.query_order(order.order_id)
        assert status == OrderStatus.FILLED

    def test_query_pending(self) -> None:
        mgr = _paper(auto_fill=False)
        order = _place(mgr)
        assert mgr.query_order(order.order_id) == OrderStatus.PENDING

    def test_query_unknown_raises(self) -> None:
        mgr = _paper()
        with pytest.raises(KeyError):
            mgr.query_order("nonexistent-id")


# ===========================================================================
# PaperOrderManager — cancel_order
# ===========================================================================


class TestPaperCancelOrder:
    def test_cancel_pending_order(self) -> None:
        mgr = _paper(auto_fill=False)
        order = _place(mgr)
        result = mgr.cancel_order(order.order_id)
        assert result is True
        assert mgr.query_order(order.order_id) == OrderStatus.CANCELLED

    def test_cancel_filled_order_returns_false(self) -> None:
        mgr = _paper(market_fill_price=100.0)
        order = _place(mgr)
        assert order.status == OrderStatus.FILLED
        result = mgr.cancel_order(order.order_id)
        assert result is False

    def test_cancel_already_cancelled_returns_false(self) -> None:
        mgr = _paper(auto_fill=False)
        order = _place(mgr)
        mgr.cancel_order(order.order_id)
        result = mgr.cancel_order(order.order_id)
        assert result is False

    def test_cancel_unknown_raises(self) -> None:
        mgr = _paper()
        with pytest.raises(KeyError):
            mgr.cancel_order("no-such-id")


# ===========================================================================
# PaperOrderManager — list_active_orders
# ===========================================================================


class TestPaperListActiveOrders:
    def test_empty_at_start(self) -> None:
        mgr = _paper()
        assert mgr.list_active_orders() == []

    def test_filled_orders_not_listed(self) -> None:
        mgr = _paper(market_fill_price=500.0)
        _place(mgr)
        assert mgr.list_active_orders() == []

    def test_pending_orders_listed(self) -> None:
        mgr = _paper(auto_fill=False)
        o1 = _place(mgr, symbol="TXF")
        o2 = _place(mgr, symbol="MXF")
        active_ids = {o.order_id for o in mgr.list_active_orders()}
        assert {o1.order_id, o2.order_id} == active_ids

    def test_cancelled_orders_excluded(self) -> None:
        mgr = _paper(auto_fill=False)
        o1 = _place(mgr, symbol="TXF")
        o2 = _place(mgr, symbol="MXF")
        mgr.cancel_order(o1.order_id)
        active = mgr.list_active_orders()
        assert len(active) == 1
        assert active[0].order_id == o2.order_id

    def test_list_sorted_by_created_at(self) -> None:
        mgr = _paper(auto_fill=False)
        orders = [_place(mgr, symbol=f"SYM{i}") for i in range(5)]
        active = mgr.list_active_orders()
        assert [o.order_id for o in active] == [o.order_id for o in orders]


# ===========================================================================
# PaperOrderManager — simulate_fill
# ===========================================================================


class TestPaperSimulateFill:
    def test_full_fill(self) -> None:
        mgr = _paper(auto_fill=False)
        order = _place(mgr, quantity=3)
        updated = mgr.simulate_fill(order.order_id, fill_price=18000.0)
        assert updated.status == OrderStatus.FILLED
        assert updated.filled_quantity == 3.0
        assert updated.avg_fill_price == pytest.approx(18000.0)

    def test_partial_fill(self) -> None:
        mgr = _paper(auto_fill=False)
        order = _place(mgr, quantity=4)
        updated = mgr.simulate_fill(order.order_id, fill_price=18000.0, fill_quantity=1)
        assert updated.status == OrderStatus.PARTIAL
        assert updated.filled_quantity == 1.0
        assert updated.remaining_quantity == 3.0

    def test_two_partial_fills_avg_price(self) -> None:
        mgr = _paper(auto_fill=False)
        order = _place(mgr, quantity=4)
        mgr.simulate_fill(order.order_id, fill_price=18000.0, fill_quantity=2)
        updated = mgr.simulate_fill(order.order_id, fill_price=18100.0, fill_quantity=2)
        assert updated.status == OrderStatus.FILLED
        expected_avg = (18000.0 * 2 + 18100.0 * 2) / 4
        assert updated.avg_fill_price == pytest.approx(expected_avg)

    def test_fill_unknown_order_raises(self) -> None:
        mgr = _paper()
        with pytest.raises(KeyError):
            mgr.simulate_fill("bad-id", 100.0)

    def test_fill_non_active_raises(self) -> None:
        mgr = _paper(auto_fill=False)
        order = _place(mgr)
        mgr.cancel_order(order.order_id)
        with pytest.raises(ValueError, match="not active"):
            mgr.simulate_fill(order.order_id, 100.0)

    def test_overfill_raises(self) -> None:
        mgr = _paper(auto_fill=False)
        order = _place(mgr, quantity=2)
        with pytest.raises(ValueError, match="fill_quantity"):
            mgr.simulate_fill(order.order_id, 100.0, fill_quantity=3)

    def test_zero_fill_quantity_raises(self) -> None:
        mgr = _paper(auto_fill=False)
        order = _place(mgr, quantity=2)
        with pytest.raises(ValueError, match="fill_quantity"):
            mgr.simulate_fill(order.order_id, 100.0, fill_quantity=0)

    def test_query_reflects_simulate_fill(self) -> None:
        mgr = _paper(auto_fill=False)
        order = _place(mgr)
        mgr.simulate_fill(order.order_id, 99.0)
        assert mgr.query_order(order.order_id) == OrderStatus.FILLED


# ===========================================================================
# PaperOrderManager — get_order
# ===========================================================================


class TestGetOrder:
    def test_get_order_returns_order(self) -> None:
        mgr = _paper()
        order = _place(mgr)
        fetched = mgr.get_order(order.order_id)
        assert fetched.order_id == order.order_id

    def test_get_unknown_raises(self) -> None:
        mgr = _paper()
        with pytest.raises(KeyError):
            mgr.get_order("nonexistent")


# ===========================================================================
# AbstractOrderManager — must be abstract
# ===========================================================================


class TestAbstractness:
    def test_cannot_instantiate_abstract(self) -> None:
        with pytest.raises(TypeError):
            AbstractOrderManager()  # type: ignore[abstract]

    def test_custom_concrete_implementation(self) -> None:
        """A minimal concrete subclass must implement all abstract methods."""

        class MinimalManager(AbstractOrderManager):
            def _submit_order(self, order: Order) -> Order:
                return order.with_update(broker_ref="MINIMAL")

            def _fetch_order_status(self, order: Order) -> Order:
                return order

            def _request_cancel(self, order: Order) -> Order:
                return order.with_update(status=OrderStatus.CANCELLED)

        mgr = MinimalManager()
        o = mgr.place_order("TXF", "BUY", 1, "MARKET")
        assert o.broker_ref == "MINIMAL"
        assert mgr.cancel_order(o.order_id) is True


# ===========================================================================
# create_order_manager factory
# ===========================================================================


class TestFactory:
    def test_paper_broker_default(self) -> None:
        mgr = create_order_manager()
        assert isinstance(mgr, PaperOrderManager)

    def test_paper_broker_explicit(self) -> None:
        mgr = create_order_manager("paper")
        assert isinstance(mgr, PaperOrderManager)

    def test_paper_broker_case_insensitive(self) -> None:
        mgr = create_order_manager("PAPER")
        assert isinstance(mgr, PaperOrderManager)

    def test_unknown_broker_raises(self) -> None:
        with pytest.raises(ValueError, match="Unknown broker"):
            create_order_manager("binance")

    def test_kwargs_forwarded(self) -> None:
        mgr = create_order_manager("paper", auto_fill=False)
        assert isinstance(mgr, PaperOrderManager)
        # auto_fill=False means MARKET order stays PENDING
        o = mgr.place_order("TXF", "BUY", 1, "MARKET")
        assert o.status == OrderStatus.PENDING
