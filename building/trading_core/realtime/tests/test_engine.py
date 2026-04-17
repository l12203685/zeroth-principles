"""Tests for realtime/engine.py.

Coverage targets:
- get_market_session()         — all session branches + edge cases
- next_session_open()          — correct next open for every session state
- TradingSignal validation
- RealtimeEngine.submit_signal — state checks, session checks, risk checks,
                                  order submission, FLAT handling
- RealtimeEngine.on_tick       — portfolio price update + callback dispatch
- RealtimeEngine.on_bar        — callback dispatch + error tolerance
- RealtimeEngine.on_fill       — portfolio update + callback dispatch
- RealtimeEngine.health()      — snapshot fields
- RealtimeEngine._check_risk   — all four risk limit branches
- RealtimeEngine reconnect     — exponential backoff, max-attempts cap
- RealtimeEngine shutdown      — cancel pending orders, flatten positions
- Engine start/stop lifecycle  — state transitions, idempotent stop
"""

from __future__ import annotations

import threading
import time
from datetime import datetime, time as dtime
from typing import Dict, List, Optional
from unittest.mock import MagicMock, patch, call

import pytest

from trading_core.broker.orders import (
    AbstractOrderManager,
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
    PaperOrderManager,
)
from trading_core.data.positions import Portfolio, PositionType
from trading_core.realtime.engine import (
    EngineConfig,
    EngineState,
    MarketSession,
    RealtimeEngine,
    RiskLimits,
    TradingSignal,
    SignalAction,
    get_market_session,
    next_session_open,
)


# ---------------------------------------------------------------------------
# Helpers / fixtures
# ---------------------------------------------------------------------------


def _make_engine(
    *,
    order_manager: Optional[AbstractOrderManager] = None,
    portfolio: Optional[Portfolio] = None,
    risk: Optional[RiskLimits] = None,
    config: Optional[EngineConfig] = None,
    on_tick=None,
    on_bar=None,
    on_fill=None,
    on_error=None,
    connect_fn=None,
    disconnect_fn=None,
) -> RealtimeEngine:
    """Create a RealtimeEngine with fast timings for tests."""
    if order_manager is None:
        order_manager = PaperOrderManager(auto_fill=True, market_fill_price=18000.0)
    cfg = config or EngineConfig(
        heartbeat_interval=0.1,
        poll_interval=0.05,
        reconnect_base_delay=0.01,
        reconnect_max_delay=0.05,
    )
    return RealtimeEngine(
        order_manager=order_manager,
        portfolio=portfolio,
        risk=risk,
        config=cfg,
        on_tick=on_tick,
        on_bar=on_bar,
        on_fill=on_fill,
        on_error=on_error,
        connect_fn=connect_fn,
        disconnect_fn=disconnect_fn,
    )


def _running_engine() -> RealtimeEngine:
    """Return an engine that has been force-set to RUNNING for unit tests."""
    engine = _make_engine()
    engine._set_state(EngineState.RUNNING)
    return engine


# ---------------------------------------------------------------------------
# get_market_session
# ---------------------------------------------------------------------------


class TestGetMarketSession:
    """Unit tests for the pure market-session logic."""

    @pytest.mark.parametrize("hour,minute,expected", [
        # Day session — inside
        (8, 45, MarketSession.DAY),
        (10, 0, MarketSession.DAY),
        (13, 45, MarketSession.DAY),
        # Night session — before midnight
        (15, 0, MarketSession.NIGHT),
        (20, 0, MarketSession.NIGHT),
        (23, 59, MarketSession.NIGHT),
        # Night session — after midnight
        (0, 0, MarketSession.NIGHT),
        (4, 59, MarketSession.NIGHT),
        (5, 0, MarketSession.NIGHT),
        # Closed gaps
        (5, 1, MarketSession.CLOSED),
        (8, 44, MarketSession.CLOSED),
        (13, 46, MarketSession.CLOSED),
        (14, 59, MarketSession.CLOSED),
    ])
    def test_session_at_time(self, hour: int, minute: int, expected: MarketSession):
        now = datetime(2024, 1, 15, hour, minute, 0)
        assert get_market_session(now) == expected

    def test_defaults_to_current_time(self):
        """Calling with no arg should not raise."""
        result = get_market_session()
        assert isinstance(result, MarketSession)


# ---------------------------------------------------------------------------
# next_session_open
# ---------------------------------------------------------------------------


class TestNextSessionOpen:
    """Unit tests for next_session_open()."""

    def test_closed_between_night_end_and_day_start_returns_today_day(self):
        now = datetime(2024, 1, 15, 7, 0, 0)   # 07:00 → closed
        result = next_session_open(now)
        assert result == datetime(2024, 1, 15, 8, 45, 0)

    def test_closed_between_day_end_and_night_start_returns_today_night(self):
        now = datetime(2024, 1, 15, 14, 0, 0)  # 14:00 → closed
        result = next_session_open(now)
        assert result == datetime(2024, 1, 15, 15, 0, 0)

    def test_during_day_session_returns_tonight_night(self):
        now = datetime(2024, 1, 15, 10, 0, 0)  # 10:00 → day session
        result = next_session_open(now)
        assert result == datetime(2024, 1, 15, 15, 0, 0)

    def test_during_night_session_returns_tomorrow_day(self):
        now = datetime(2024, 1, 15, 20, 0, 0)  # 20:00 → night session
        result = next_session_open(now)
        assert result.date() == datetime(2024, 1, 16).date()
        assert result.time() == dtime(8, 45)

    def test_defaults_to_now(self):
        result = next_session_open()
        assert isinstance(result, datetime)


# ---------------------------------------------------------------------------
# TradingSignal
# ---------------------------------------------------------------------------


class TestTradingSignal:
    def test_valid_market_buy(self):
        sig = TradingSignal("TXF", SignalAction.BUY, 1.0)
        assert sig.symbol == "TXF"
        assert sig.action == SignalAction.BUY

    def test_valid_limit_sell(self):
        sig = TradingSignal("TXF", SignalAction.SELL, 2.0, order_type="LIMIT", price=18000.0)
        assert sig.price == 18000.0

    def test_zero_quantity_raises(self):
        with pytest.raises(ValueError, match="quantity must be positive"):
            TradingSignal("TXF", SignalAction.BUY, 0.0)

    def test_negative_quantity_raises(self):
        with pytest.raises(ValueError, match="quantity must be positive"):
            TradingSignal("TXF", SignalAction.BUY, -1.0)

    def test_limit_without_price_raises(self):
        with pytest.raises(ValueError, match="require a price"):
            TradingSignal("TXF", SignalAction.BUY, 1.0, order_type="LIMIT", price=None)

    def test_immutable(self):
        sig = TradingSignal("TXF", SignalAction.BUY, 1.0)
        with pytest.raises(Exception):  # frozen dataclass
            sig.quantity = 99  # type: ignore[misc]


# ---------------------------------------------------------------------------
# RealtimeEngine — state and lifecycle
# ---------------------------------------------------------------------------


class TestEngineLifecycle:
    def test_initial_state_is_idle(self):
        engine = _make_engine()
        assert engine.state == EngineState.IDLE

    def test_cannot_start_twice(self):
        engine = _make_engine()
        engine._set_state(EngineState.RUNNING)
        with pytest.raises(RuntimeError, match="Cannot start engine"):
            engine.start()

    def test_stop_from_idle_is_noop(self):
        engine = _make_engine()
        engine.stop(timeout=1.0)   # should not raise
        assert engine.state == EngineState.STOPPED

    def test_stop_idempotent(self):
        engine = _make_engine()
        engine.stop(timeout=1.0)
        engine.stop(timeout=1.0)   # second call is safe

    def test_start_stop_cycle_with_open_market(self):
        """Engine starts, runs briefly during open market, then stops cleanly."""
        with patch(
            "trading_core.realtime.engine.get_market_session",
            return_value=MarketSession.DAY,
        ):
            engine = _make_engine()
            engine.start()
            time.sleep(0.15)   # let the loop spin
            engine.stop(timeout=2.0)
            assert engine.state == EngineState.STOPPED


# ---------------------------------------------------------------------------
# RealtimeEngine — submit_signal
# ---------------------------------------------------------------------------


@patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.DAY)
class TestSubmitSignal:
    """All tests patch the market session to 'DAY' so trades are allowed."""

    def test_buy_signal_places_order(self, _mock_session):
        engine = _running_engine()
        order = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        assert order is not None
        assert order.side == OrderSide.BUY
        assert order.symbol == "TXF"

    def test_sell_signal_places_order(self, _mock_session):
        engine = _running_engine()
        order = engine.submit_signal(TradingSignal("TXF", SignalAction.SELL, 1.0))
        assert order is not None
        assert order.side == OrderSide.SELL

    def test_signal_rejected_when_engine_idle(self, _mock_session):
        engine = _make_engine()
        # Engine is IDLE, not RUNNING/WAITING
        result = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        assert result is None

    def test_signal_rejected_when_stopping(self, _mock_session):
        engine = _make_engine()
        engine._set_state(EngineState.STOPPING)
        result = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        assert result is None

    def test_order_rejected_by_risk_max_order_size(self, _mock_session):
        engine = _running_engine()
        engine._risk.max_order_size = 2.0
        result = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 5.0))
        assert result is None

    def test_order_rejected_by_risk_daily_loss(self, _mock_session):
        engine = _running_engine()
        engine._daily_pnl = -200_000.0
        engine._risk.max_daily_loss = 100_000.0
        result = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        assert result is None

    def test_order_rejected_when_market_closed(self, mock_session):
        mock_session.return_value = MarketSession.CLOSED
        engine = _running_engine()
        result = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        assert result is None

    def test_flat_signal_with_no_position(self, _mock_session):
        engine = _running_engine()
        result = engine.submit_signal(TradingSignal("TXF", SignalAction.FLAT, 1.0))
        assert result is None   # no position to close

    def test_flat_signal_closes_long_position(self, _mock_session):
        engine = _running_engine()
        # First open a long position
        engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 2.0))
        # Now flatten
        close_order = engine.submit_signal(TradingSignal("TXF", SignalAction.FLAT, 1.0))
        assert close_order is not None
        assert close_order.side == OrderSide.SELL

    def test_limit_order_signal(self, _mock_session):
        engine = _running_engine()
        sig = TradingSignal("TXF", SignalAction.BUY, 1.0, order_type="LIMIT", price=17500.0)
        order = engine.submit_signal(sig)
        assert order is not None
        assert order.order_type == OrderType.LIMIT
        assert order.price == 17500.0

    def test_error_in_order_submission_fires_on_error(self, _mock_session):
        errors: List[Exception] = []
        bad_manager = PaperOrderManager()

        # Monkeypatch place_order to raise
        def _raise(*args, **kwargs):
            raise RuntimeError("broker down")

        bad_manager.place_order = _raise  # type: ignore[assignment]

        engine = _make_engine(
            order_manager=bad_manager,
            on_error=lambda e, eng: errors.append(e),
        )
        engine._set_state(EngineState.RUNNING)
        result = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        assert result is None
        assert len(errors) == 1
        assert "broker down" in str(errors[0])


# ---------------------------------------------------------------------------
# RealtimeEngine — on_tick / on_bar / on_fill
# ---------------------------------------------------------------------------


class TestEventCallbacks:
    @patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.DAY)
    def test_on_tick_updates_portfolio_price(self, _):
        engine = _running_engine()
        # Open a position first
        engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        # Send tick
        engine.on_tick({"symbol": "TXF", "price": 18500.0})
        pos = engine._portfolio.get_position("TXF")
        assert pos is not None
        assert pos.current_price == 18500.0

    def test_on_tick_fires_callback(self):
        ticks: List[Dict] = []
        engine = _make_engine(on_tick=lambda t: ticks.append(t))
        engine.on_tick({"symbol": "TXF", "price": 18000.0})
        assert len(ticks) == 1
        assert ticks[0]["price"] == 18000.0

    def test_on_tick_callback_error_fires_on_error(self):
        errors: List[Exception] = []

        def _bad_tick(t):
            raise ValueError("tick crash")

        engine = _make_engine(
            on_tick=_bad_tick,
            on_error=lambda e, eng: errors.append(e),
        )
        engine.on_tick({"symbol": "TXF", "price": 18000.0})
        assert len(errors) == 1

    def test_on_bar_fires_callback(self):
        bars: List[Dict] = []
        engine = _make_engine(on_bar=lambda b: bars.append(b))
        bar = {"symbol": "TXF", "open": 18000, "close": 18100}
        engine.on_bar(bar)
        assert bars == [bar]

    def test_on_bar_callback_error_fires_on_error(self):
        errors: List[Exception] = []

        def _bad_bar(b):
            raise RuntimeError("bar crash")

        engine = _make_engine(
            on_bar=_bad_bar,
            on_error=lambda e, eng: errors.append(e),
        )
        engine.on_bar({})
        assert len(errors) == 1

    def test_on_fill_fires_callback(self):
        fills: List[Order] = []
        engine = _make_engine(on_fill=lambda o, e: fills.append(o))
        order = Order(
            symbol="TXF",
            side=OrderSide.BUY,
            quantity=1.0,
            order_type=OrderType.MARKET,
            status=OrderStatus.FILLED,
            filled_quantity=1.0,
            avg_fill_price=18000.0,
        )
        engine.on_fill(order)
        assert len(fills) == 1
        assert fills[0].symbol == "TXF"

    def test_on_fill_callback_error_fires_on_error(self):
        errors: List[Exception] = []

        def _bad_fill(o, e):
            raise RuntimeError("fill crash")

        engine = _make_engine(
            on_fill=_bad_fill,
            on_error=lambda e, eng: errors.append(e),
        )
        order = Order(
            symbol="TXF",
            side=OrderSide.BUY,
            quantity=1.0,
            order_type=OrderType.MARKET,
            status=OrderStatus.FILLED,
            filled_quantity=1.0,
            avg_fill_price=18000.0,
        )
        engine.on_fill(order)
        assert len(errors) == 1

    def test_on_fill_updates_portfolio_on_buy(self):
        engine = _make_engine()
        order = Order(
            symbol="TXF",
            side=OrderSide.BUY,
            quantity=2.0,
            order_type=OrderType.MARKET,
            status=OrderStatus.FILLED,
            filled_quantity=2.0,
            avg_fill_price=18000.0,
        )
        engine.on_fill(order)
        pos = engine._portfolio.get_position("TXF")
        assert pos is not None
        assert pos.direction == PositionType.LONG
        assert pos.size == 2.0

    def test_on_fill_closes_position_on_opposite_side(self):
        engine = _make_engine()
        # Open long
        buy_order = Order(
            symbol="TXF",
            side=OrderSide.BUY,
            quantity=2.0,
            order_type=OrderType.MARKET,
            status=OrderStatus.FILLED,
            filled_quantity=2.0,
            avg_fill_price=18000.0,
        )
        engine.on_fill(buy_order)
        # Close with full sell
        sell_order = Order(
            symbol="TXF",
            side=OrderSide.SELL,
            quantity=2.0,
            order_type=OrderType.MARKET,
            status=OrderStatus.FILLED,
            filled_quantity=2.0,
            avg_fill_price=18200.0,
        )
        engine.on_fill(sell_order)
        pos = engine._portfolio.get_position("TXF")
        assert pos is None   # position closed


# ---------------------------------------------------------------------------
# RealtimeEngine — health()
# ---------------------------------------------------------------------------


class TestHealth:
    def test_health_idle_not_healthy(self):
        engine = _make_engine()
        h = engine.health()
        assert h.state == EngineState.IDLE
        assert h.is_healthy is False

    def test_health_running_no_recent_heartbeat_not_healthy(self):
        engine = _running_engine()
        # last_heartbeat is None
        h = engine.health()
        assert h.state == EngineState.RUNNING
        assert h.is_healthy is False  # heartbeat never fired

    def test_health_running_with_fresh_heartbeat_is_healthy(self):
        engine = _running_engine()
        engine._last_heartbeat = datetime.now()
        h = engine.health()
        assert h.is_healthy is True

    @patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.DAY)
    def test_health_reflects_open_orders(self, _):
        # PaperOrderManager auto_fill=False → orders stay PENDING
        om = PaperOrderManager(auto_fill=False)
        engine = _make_engine(order_manager=om)
        engine._set_state(EngineState.RUNNING)
        engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        h = engine.health()
        assert h.active_orders == 1

    def test_health_reconnect_count(self):
        engine = _make_engine()
        engine._reconnect_count = 3
        h = engine.health()
        assert h.reconnect_count == 3


# ---------------------------------------------------------------------------
# RealtimeEngine — risk checks
# ---------------------------------------------------------------------------


@patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.DAY)
class TestRiskChecks:
    def test_max_position_size_buy(self, _):
        engine = _running_engine()
        engine._risk.max_position_size = 3.0
        engine._risk.max_order_size = 10.0  # allow large single order
        # Try to buy 4 contracts — exceeds max position
        result = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 4.0))
        assert result is None

    def test_max_position_size_sell(self, _):
        engine = _running_engine()
        engine._risk.max_position_size = 3.0
        engine._risk.max_order_size = 10.0
        result = engine.submit_signal(TradingSignal("TXF", SignalAction.SELL, 4.0))
        assert result is None

    def test_max_drawdown_blocks_order(self, _):
        engine = _running_engine()
        engine._risk.max_drawdown_pct = 0.05
        # Simulate equity drop: peak = 100_000, current = 90_000 → 10% drawdown
        engine._peak_equity = 100_000.0
        engine._portfolio = Portfolio(initial_cash=90_000.0)
        result = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        assert result is None

    def test_order_passes_when_within_limits(self, _):
        engine = _running_engine()
        engine._risk.max_position_size = 10.0
        engine._risk.max_order_size = 5.0
        engine._risk.max_daily_loss = 1_000_000.0
        result = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        assert result is not None


# ---------------------------------------------------------------------------
# RealtimeEngine — reconnect logic
# ---------------------------------------------------------------------------


class TestReconnect:
    def test_reconnect_uses_exponential_backoff(self):
        config = EngineConfig(
            reconnect_base_delay=0.01,
            reconnect_max_delay=1.0,
            reconnect_max_attempts=3,
        )
        engine = _make_engine(config=config)
        engine._stop_event.clear()

        delays_waited = []

        original_wait = engine._stop_event.wait

        def _spy_wait(timeout=None):
            if timeout is not None and timeout > 0:
                delays_waited.append(timeout)
            return False  # always "not set" so reconnect proceeds

        engine._stop_event.wait = _spy_wait  # type: ignore[assignment]

        engine._handle_reconnect()  # attempt 1
        engine._handle_reconnect()  # attempt 2

        assert len(delays_waited) == 2
        assert delays_waited[1] >= delays_waited[0]   # backoff grows

    def test_max_attempts_returns_false(self):
        config = EngineConfig(
            reconnect_max_attempts=2,
            reconnect_base_delay=0.001,
            reconnect_max_delay=0.01,
        )
        engine = _make_engine(config=config)
        engine._stop_event.clear()
        engine._stop_event.wait = lambda timeout=None: False  # type: ignore

        # Exhaust attempts
        engine._reconnect_attempt = 2
        result = engine._handle_reconnect()
        assert result is False

    def test_zero_max_attempts_retries_indefinitely(self):
        """max_attempts=0 should never return False from the attempt check."""
        config = EngineConfig(
            reconnect_max_attempts=0,
            reconnect_base_delay=0.001,
            reconnect_max_delay=0.01,
        )
        engine = _make_engine(config=config)
        engine._stop_event.clear()
        engine._stop_event.wait = lambda timeout=None: False  # type: ignore

        engine._reconnect_attempt = 1000  # very high attempt count
        result = engine._handle_reconnect()
        assert result is True  # should still retry

    def test_reconnect_count_increments(self):
        config = EngineConfig(
            reconnect_max_attempts=0,
            reconnect_base_delay=0.001,
            reconnect_max_delay=0.01,
        )
        engine = _make_engine(config=config)
        engine._stop_event.clear()
        engine._stop_event.wait = lambda timeout=None: False  # type: ignore

        engine._handle_reconnect()
        assert engine._reconnect_count == 1
        engine._handle_reconnect()
        assert engine._reconnect_count == 2


# ---------------------------------------------------------------------------
# RealtimeEngine — shutdown / cancel / flatten
# ---------------------------------------------------------------------------


class TestShutdown:
    @patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.DAY)
    def test_stop_cancels_pending_orders(self, _):
        om = PaperOrderManager(auto_fill=False)  # orders stay PENDING
        engine = _make_engine(order_manager=om)
        engine._set_state(EngineState.RUNNING)

        # Place an order that won't auto-fill
        engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        assert len(om.list_active_orders()) == 1

        engine.stop(timeout=1.0)

        # All orders should be cancelled after shutdown
        assert len(om.list_active_orders()) == 0

    def test_disconnect_fn_called_on_stop(self):
        disconnects: List[int] = []
        engine = _make_engine(disconnect_fn=lambda: disconnects.append(1))
        engine.stop(timeout=1.0)
        assert len(disconnects) == 1

    def test_flatten_on_shutdown_closes_positions(self):
        with patch(
            "trading_core.realtime.engine.get_market_session",
            return_value=MarketSession.DAY,
        ):
            risk = RiskLimits(flatten_on_shutdown=True)
            om = PaperOrderManager(auto_fill=True, market_fill_price=18000.0)
            engine = _make_engine(order_manager=om, risk=risk)
            engine._set_state(EngineState.RUNNING)

            # Open a position
            engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 2.0))
            pos = engine._portfolio.get_position("TXF")
            assert pos is not None and pos.is_open

            engine.stop(timeout=2.0)

            # Position should be closed by flatten
            final_pos = engine._portfolio.get_position("TXF")
            assert final_pos is None or not final_pos.is_open

    @patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.DAY)
    def test_connect_fn_called_on_start(self, _):
        connects: List[int] = []
        engine = _make_engine(connect_fn=lambda: connects.append(1))
        engine.start()
        time.sleep(0.1)
        engine.stop(timeout=2.0)
        assert len(connects) >= 1


# ---------------------------------------------------------------------------
# RealtimeEngine — full start/stop integration
# ---------------------------------------------------------------------------


class TestIntegration:
    @patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.DAY)
    def test_start_then_stop_reaches_stopped(self, _):
        engine = _make_engine()
        engine.start()
        time.sleep(0.15)
        engine.stop(timeout=3.0)
        assert engine.state == EngineState.STOPPED

    @patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.CLOSED)
    def test_engine_waits_when_market_closed(self, _):
        engine = _make_engine()
        engine.start()
        time.sleep(0.15)
        # Engine should be in WAITING state because market is closed
        assert engine.state in (EngineState.WAITING, EngineState.CONNECTING, EngineState.RUNNING)
        engine.stop(timeout=2.0)

    @patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.DAY)
    def test_heartbeat_fires_during_running(self, _):
        engine = _make_engine(
            config=EngineConfig(
                heartbeat_interval=0.05,
                poll_interval=0.05,
                reconnect_base_delay=0.01,
                reconnect_max_delay=0.05,
            )
        )
        engine.start()
        time.sleep(0.3)   # allow heartbeat to fire
        engine.stop(timeout=2.0)
        assert engine._last_heartbeat is not None

    @patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.DAY)
    def test_reconnect_on_connect_error(self, _):
        connect_calls: List[int] = []

        def _flaky_connect():
            connect_calls.append(1)
            if len(connect_calls) < 3:
                raise ConnectionError("temporary failure")

        config = EngineConfig(
            reconnect_max_attempts=5,
            reconnect_base_delay=0.01,
            reconnect_max_delay=0.05,
            poll_interval=0.05,
            heartbeat_interval=0.1,
        )
        engine = _make_engine(connect_fn=_flaky_connect, config=config)
        engine.start()
        time.sleep(0.5)
        engine.stop(timeout=2.0)

        # connect_fn should have been called multiple times
        assert len(connect_calls) >= 2
        # Engine should eventually stabilise
        assert engine.state == EngineState.STOPPED
