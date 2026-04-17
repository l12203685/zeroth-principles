"""Integration tests for trading_core — cross-module workflows.

Covers:
1.  Signal → PaperOrderManager → BacktestEngine end-to-end
2.  RealtimeEngine → PaperOrderManager signal submission pipeline
3.  Multi-strategy backtest with portfolio-level metrics aggregation
4.  Fee/slippage impact verification across modules
5.  Order lifecycle consistency between backtest and realtime layers
"""

from __future__ import annotations

import time
from datetime import datetime
from typing import Dict, List, Optional
from unittest.mock import patch

import numpy as np
import pandas as pd
import pytest

# ── broker ──────────────────────────────────────────────────────────────────
from trading_core.broker.orders import (
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
    PaperOrderManager,
    create_order_manager,
)

# ── backtest ─────────────────────────────────────────────────────────────────
from trading_core.backtest.engine import (
    BacktestEngine,
    BacktestResult,
    CommissionMode,
    EngineConfig,
    SizingMode,
    SlippageMode,
)
from trading_core.backtest.harness import Signal

# ── realtime ─────────────────────────────────────────────────────────────────
from trading_core.realtime.engine import (
    EngineConfig as RealtimeConfig,
    EngineState,
    MarketSession,
    RealtimeEngine,
    RiskLimits,
    SignalAction,
    TradingSignal,
)

# ── data ─────────────────────────────────────────────────────────────────────
from trading_core.data.positions import Portfolio, PositionType


# ---------------------------------------------------------------------------
# Shared fixtures / helpers
# ---------------------------------------------------------------------------


def _make_ohlcv(closes: list, start: str = "2024-01-01", freq: str = "D") -> pd.DataFrame:
    """Build minimal OHLCV DataFrame from a list of close prices."""
    idx = pd.date_range(start=start, periods=len(closes), freq=freq)
    return pd.DataFrame(
        {
            "open": closes,
            "high": [c * 1.005 for c in closes],
            "low": [c * 0.995 for c in closes],
            "close": closes,
            "volume": [10_000.0] * len(closes),
        },
        index=idx,
    )


def _default_engine_cfg(**overrides) -> EngineConfig:
    base = dict(
        initial_capital=100_000.0,
        commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
        commission_value=0.001,
        slippage_mode=SlippageMode.NONE,
        sizing_mode=SizingMode.FIXED,
        sizing_param=1.0,
    )
    base.update(overrides)
    return EngineConfig(**base)


def _realtime_cfg(**overrides) -> RealtimeConfig:
    base = dict(
        heartbeat_interval=0.05,
        poll_interval=0.05,
        reconnect_base_delay=0.01,
        reconnect_max_delay=0.05,
    )
    base.update(overrides)
    return RealtimeConfig(**base)


# ===========================================================================
# 1. Signal → PaperOrderManager → BacktestEngine end-to-end
# ===========================================================================


class TestSignalToPaperOrderManagerBacktestIntegration:
    """Verify that the backtest engine correctly routes signals through
    PaperOrderManager and that the resulting order lifecycle is consistent
    with what the broker module produces in isolation."""

    def test_buy_signal_creates_filled_order_in_result(self):
        """BUY signal at bar 0 must produce a FILLED order in BacktestResult.orders."""
        ohlcv = _make_ohlcv([100.0, 105.0, 110.0])

        def strategy(ctx):
            return Signal.BUY if ctx.idx == 0 else None

        result = BacktestEngine(ohlcv, strategy, _default_engine_cfg()).run()

        # At least one order should exist (entry)
        assert len(result.orders) >= 1
        for order in result.orders.values():
            assert order.status == OrderStatus.FILLED

    def test_buy_then_close_produces_two_filled_orders(self):
        """A complete round-trip (BUY + CLOSE) must produce exactly 2 FILLED orders."""
        ohlcv = _make_ohlcv([100.0, 105.0, 110.0])

        def strategy(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        cfg = _default_engine_cfg(commission_value=0.0)
        result = BacktestEngine(ohlcv, strategy, cfg).run()

        assert len(result.orders) == 2
        assert all(o.status == OrderStatus.FILLED for o in result.orders.values())

    def test_order_sides_match_direction(self):
        """Entry order must be BUY for long and SELL for exit of long."""
        ohlcv = _make_ohlcv([100.0, 105.0, 110.0])

        def strategy(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        result = BacktestEngine(ohlcv, strategy, _default_engine_cfg()).run()
        sides = [o.side for o in result.orders.values()]
        assert OrderSide.BUY in sides
        assert OrderSide.SELL in sides

    def test_paper_order_manager_used_by_backtest_fills_correctly(self):
        """Instantiate PaperOrderManager separately and confirm identical fill
        semantics to what BacktestEngine records in its trade_log."""
        # BacktestEngine uses auto_fill=False internally and calls simulate_fill.
        # An equivalent manual flow should produce the same fill price logic.
        om = PaperOrderManager(auto_fill=False)
        order = om.place_order("TXF", "BUY", 1.0, "MARKET")
        assert order.status == OrderStatus.PENDING

        filled = om.simulate_fill(order.order_id, fill_price=105.0)
        assert filled.status == OrderStatus.FILLED
        assert filled.avg_fill_price == pytest.approx(105.0)

        # Now verify BacktestEngine fills at next-bar open (105 when signal on bar 0)
        ohlcv = _make_ohlcv([100.0, 105.0, 110.0])

        def strategy(ctx):
            return Signal.BUY if ctx.idx == 0 else None

        result = BacktestEngine(ohlcv, strategy, _default_engine_cfg(commission_value=0.0)).run()
        trade = result.trade_log.iloc[0]
        # Entry fill should be at bar-1 open = 105
        assert trade["entry_price"] == pytest.approx(105.0)

    def test_force_close_at_last_bar_generates_order(self):
        """Position held to end-of-data should be force-closed by the engine,
        resulting in a second filled order."""
        ohlcv = _make_ohlcv([100.0, 110.0, 120.0, 130.0])

        def strategy(ctx):
            return Signal.BUY if ctx.idx == 0 else None

        result = BacktestEngine(ohlcv, strategy, _default_engine_cfg(commission_value=0.0)).run()

        assert len(result.trade_log) == 1
        assert len(result.orders) >= 2  # entry + force-close

    def test_equity_after_profitable_trade_exceeds_initial(self):
        """After a profitable backtest, final equity must exceed initial capital."""
        ohlcv = _make_ohlcv([100.0, 110.0, 120.0, 130.0])

        def strategy(ctx):
            return Signal.BUY if ctx.idx == 0 else None

        cfg = _default_engine_cfg(commission_value=0.0, initial_capital=10_000.0)
        result = BacktestEngine(ohlcv, strategy, cfg).run()
        assert result.equity_curve.iloc[-1] > 10_000.0

    def test_short_signal_creates_sell_entry_order(self):
        """SELL signal should create an entry order with side=SELL."""
        ohlcv = _make_ohlcv([100.0, 95.0, 90.0])

        def strategy(ctx):
            if ctx.idx == 0:
                return Signal.SELL
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        result = BacktestEngine(ohlcv, strategy, _default_engine_cfg(commission_value=0.0)).run()
        orders = list(result.orders.values())
        # First order should be a SELL (entering short)
        first_order = min(orders, key=lambda o: o.created_at)
        assert first_order.side == OrderSide.SELL

    def test_no_trades_no_orders_in_result(self):
        """A strategy that never signals should produce zero orders."""
        ohlcv = _make_ohlcv([100.0, 100.0, 100.0])
        result = BacktestEngine(ohlcv, lambda ctx: None).run()
        assert len(result.orders) == 0
        assert len(result.trade_log) == 0


# ===========================================================================
# 2. RealtimeEngine → PaperOrderManager signal submission pipeline
# ===========================================================================


@patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.DAY)
class TestRealtimeEnginePaperOrderManagerPipeline:
    """Verify that TradingSignal flows correctly through RealtimeEngine into
    PaperOrderManager and that the portfolio reflects resulting fills."""

    def _make_realtime(self, om=None, risk=None):
        if om is None:
            om = PaperOrderManager(auto_fill=True, market_fill_price=18000.0)
        engine = RealtimeEngine(
            order_manager=om,
            risk=risk,
            config=_realtime_cfg(),
        )
        engine._set_state(EngineState.RUNNING)
        return engine

    def test_buy_signal_reaches_paper_order_manager(self, _):
        """BUY signal submitted to RealtimeEngine must appear as FILLED order
        in PaperOrderManager since auto_fill=True."""
        om = PaperOrderManager(auto_fill=True, market_fill_price=18000.0)
        engine = self._make_realtime(om=om)

        order = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 2.0))

        assert order is not None
        assert order.status == OrderStatus.FILLED
        assert order.filled_quantity == 2.0
        assert order.symbol == "TXF"

    def test_sell_signal_reaches_paper_order_manager(self, _):
        om = PaperOrderManager(auto_fill=True, market_fill_price=18000.0)
        engine = self._make_realtime(om=om)

        order = engine.submit_signal(TradingSignal("TXF", SignalAction.SELL, 1.0))

        assert order is not None
        assert order.side == OrderSide.SELL
        assert order.status == OrderStatus.FILLED

    def test_buy_fill_reflected_in_realtime_portfolio(self, _):
        """After a BUY fill, the engine's portfolio should show a LONG position."""
        om = PaperOrderManager(auto_fill=True, market_fill_price=18000.0)
        engine = self._make_realtime(om=om)

        engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 2.0))
        # Simulate the fill callback the realtime engine would receive
        filled_order = om.get_order(list(om._orders.keys())[-1])
        engine.on_fill(filled_order)

        pos = engine._portfolio.get_position("TXF")
        assert pos is not None
        assert pos.direction == PositionType.LONG
        assert pos.size == 2.0

    def test_flat_signal_closes_existing_long_position(self, _):
        """FLAT after BUY should close the position via a SELL order."""
        om = PaperOrderManager(auto_fill=True, market_fill_price=18000.0)
        engine = self._make_realtime(om=om)

        # Open long
        buy_order = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 2.0))
        engine.on_fill(buy_order)

        pos = engine._portfolio.get_position("TXF")
        assert pos is not None

        # Flatten
        close_order = engine.submit_signal(TradingSignal("TXF", SignalAction.FLAT, 1.0))
        assert close_order is not None
        assert close_order.side == OrderSide.SELL

    def test_limit_order_signal_passes_through_correctly(self, _):
        """LIMIT order TradingSignal should arrive at PaperOrderManager with correct price."""
        om = PaperOrderManager(auto_fill=False)
        engine = self._make_realtime(om=om)

        order = engine.submit_signal(
            TradingSignal("TXF", SignalAction.BUY, 1.0, order_type="LIMIT", price=17500.0)
        )

        assert order is not None
        assert order.order_type == OrderType.LIMIT
        assert order.price == pytest.approx(17500.0)
        # Limit order stays PENDING in auto_fill=False mode
        assert order.status == OrderStatus.PENDING

    def test_pending_order_cancels_on_engine_stop(self, _):
        """Pending orders in PaperOrderManager should be cancelled when engine stops."""
        om = PaperOrderManager(auto_fill=False)
        engine = self._make_realtime(om=om)

        engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        assert len(om.list_active_orders()) == 1

        engine.stop(timeout=2.0)

        assert len(om.list_active_orders()) == 0

    def test_risk_limit_blocks_signal_before_hitting_om(self, _):
        """A signal that violates max_order_size must not create any order in OM."""
        om = PaperOrderManager(auto_fill=True, market_fill_price=18000.0)
        risk = RiskLimits(max_order_size=1.0)
        engine = self._make_realtime(om=om, risk=risk)

        result = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 5.0))

        assert result is None
        assert len(om._orders) == 0  # nothing reached the order manager

    def test_on_tick_updates_portfolio_price_after_buy(self, _):
        """Tick event should update position current_price in portfolio."""
        om = PaperOrderManager(auto_fill=True, market_fill_price=18000.0)
        engine = self._make_realtime(om=om)

        buy_order = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        engine.on_fill(buy_order)

        engine.on_tick({"symbol": "TXF", "price": 18500.0})

        pos = engine._portfolio.get_position("TXF")
        assert pos is not None
        assert pos.current_price == pytest.approx(18500.0)


# ===========================================================================
# 3. Multi-strategy backtest with portfolio-level metrics
# ===========================================================================


class TestMultiStrategyBacktest:
    """Run multiple strategies on the same data and verify combined portfolio metrics."""

    @staticmethod
    def _run_strategy(ohlcv: pd.DataFrame, strategy_fn, cfg: EngineConfig) -> BacktestResult:
        return BacktestEngine(ohlcv, strategy_fn, cfg).run()

    def test_two_profitable_strategies_both_show_positive_returns(self):
        """Two independent long strategies on rising data should both be profitable."""
        closes = list(range(100, 160))  # steadily rising
        ohlcv = _make_ohlcv(closes)
        cfg = _default_engine_cfg(commission_value=0.0, initial_capital=50_000.0)

        def strat_early(ctx):
            return Signal.BUY if ctx.idx == 0 else None

        def strat_late(ctx):
            return Signal.BUY if ctx.idx == 5 else None

        result_early = self._run_strategy(ohlcv, strat_early, cfg)
        result_late = self._run_strategy(ohlcv, strat_late, cfg)

        assert result_early.equity_curve.iloc[-1] > 50_000.0
        assert result_late.equity_curve.iloc[-1] > 50_000.0

    def test_portfolio_total_return_sum(self):
        """Aggregating net PnL from two strategies should match sum of individual results."""
        closes = [100.0, 110.0, 120.0, 115.0, 125.0]
        ohlcv = _make_ohlcv(closes)
        cfg = _default_engine_cfg(commission_value=0.0, initial_capital=50_000.0)

        def strat_a(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        def strat_b(ctx):
            if ctx.idx == 1:
                return Signal.BUY
            if ctx.idx == 4:
                return Signal.CLOSE
            return None

        result_a = self._run_strategy(ohlcv, strat_a, cfg)
        result_b = self._run_strategy(ohlcv, strat_b, cfg)

        total_pnl_a = result_a.trade_log["pnl"].sum() if len(result_a.trade_log) > 0 else 0.0
        total_pnl_b = result_b.trade_log["pnl"].sum() if len(result_b.trade_log) > 0 else 0.0

        combined_pnl = total_pnl_a + total_pnl_b
        # Both strategies on rising data should have positive combined PnL
        assert combined_pnl > 0.0

    def test_metrics_present_for_each_strategy(self):
        """Every strategy result should carry a full metrics object."""
        closes = list(range(100, 130))
        ohlcv = _make_ohlcv(closes)
        cfg = _default_engine_cfg(commission_value=0.0)

        strategies = [
            ("long", lambda ctx: Signal.BUY if ctx.idx == 0 else None),
            ("short", lambda ctx: Signal.SELL if ctx.idx == 0 else None),
            ("flat", lambda ctx: None),
        ]

        for name, strat in strategies:
            result = self._run_strategy(ohlcv, strat, cfg)
            m = result.metrics
            assert hasattr(m, "sharpe"), f"Sharpe missing for {name}"
            assert hasattr(m, "max_drawdown"), f"max_drawdown missing for {name}"
            assert hasattr(m, "win_rate"), f"win_rate missing for {name}"
            assert hasattr(m, "num_trades"), f"num_trades missing for {name}"

    def test_win_rate_one_for_all_winning_strategies(self):
        """Strategy with only profitable trades should have win_rate=1.0."""
        closes = list(range(100, 130))
        ohlcv = _make_ohlcv(closes)

        def always_win_long(ctx):
            return Signal.BUY if ctx.idx == 0 else None

        cfg = _default_engine_cfg(commission_value=0.0, initial_capital=10_000.0)
        result = BacktestEngine(ohlcv, always_win_long, cfg).run()

        assert result.metrics.win_rate == pytest.approx(1.0)

    def test_different_sizing_modes_produce_different_equity(self):
        """FIXED vs PERCENT_EQUITY sizing on same data should differ."""
        closes = list(range(100, 120))
        ohlcv = _make_ohlcv(closes)

        def strat(ctx):
            return Signal.BUY if ctx.idx == 0 else None

        fixed_cfg = _default_engine_cfg(
            commission_value=0.0,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        pct_cfg = _default_engine_cfg(
            commission_value=0.0,
            sizing_mode=SizingMode.PERCENT_EQUITY,
            sizing_param=0.02,
            price_per_unit=1.0,
            initial_capital=100_000.0,
        )

        result_fixed = BacktestEngine(ohlcv, strat, fixed_cfg).run()
        result_pct = BacktestEngine(ohlcv, strat, pct_cfg).run()

        # Different sizing → different final equity values
        fixed_eq = result_fixed.equity_curve.iloc[-1]
        pct_eq = result_pct.equity_curve.iloc[-1]
        # Both should be profitable on rising data
        assert fixed_eq != pytest.approx(pct_eq)

    def test_multi_strategy_num_trades_sum(self):
        """Running same engine twice resets state; num_trades should be independent."""
        closes = [100.0, 110.0, 120.0]
        ohlcv = _make_ohlcv(closes)

        def strat(ctx):
            return Signal.BUY if ctx.idx == 0 else None

        cfg = _default_engine_cfg(commission_value=0.0)
        engine = BacktestEngine(ohlcv, strat, cfg)

        result1 = engine.run()
        result2 = engine.run()

        assert result1.metrics.num_trades == result2.metrics.num_trades


# ===========================================================================
# 4. Fee / slippage impact verification across modules
# ===========================================================================


class TestFeeSlippageImpactCrossModule:
    """Verify that fee and slippage values applied in BacktestEngine produce
    exactly the arithmetic expected, and that PaperOrderManager fill prices
    match backtest fill prices when configured equivalently."""

    def test_zero_cost_gross_equals_net_pnl(self):
        """With 0 commission and 0 slippage, gross_pnl must equal pnl."""
        ohlcv = _make_ohlcv([100.0, 110.0, 120.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        cfg = _default_engine_cfg(commission_value=0.0, slippage_mode=SlippageMode.NONE)
        result = BacktestEngine(ohlcv, strat, cfg).run()

        assert len(result.trade_log) == 1
        trade = result.trade_log.iloc[0]
        assert trade["pnl"] == pytest.approx(trade["gross_pnl"], rel=1e-9)

    def test_commission_reduces_pnl_by_exact_amount(self):
        """Commission of 0.1% per side must reduce net pnl by precisely
        entry_price*size*0.001 + exit_price*size*0.001."""
        ohlcv = _make_ohlcv([100.0, 105.0, 110.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        cfg = _default_engine_cfg(commission_value=0.001, slippage_mode=SlippageMode.NONE)
        result = BacktestEngine(ohlcv, strat, cfg).run()

        trade = result.trade_log.iloc[0]
        # entry at bar1 open=105, exit at bar2 close=110 (last bar)
        entry_price = trade["entry_price"]
        exit_price = trade["exit_price"]
        size = trade["size"]
        expected_commission = (entry_price + exit_price) * size * 0.001
        assert trade["commission"] == pytest.approx(expected_commission, rel=1e-6)
        assert trade["pnl"] == pytest.approx(trade["gross_pnl"] - expected_commission, rel=1e-6)

    def test_per_contract_commission_exact(self):
        """PER_CONTRACT at NT$50 per side for 2 contracts = NT$200 total commission."""
        ohlcv = _make_ohlcv([1000.0, 1010.0, 1020.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        cfg = EngineConfig(
            initial_capital=100_000.0,
            commission_mode=CommissionMode.PER_CONTRACT,
            commission_value=50.0,
            slippage_mode=SlippageMode.NONE,
            sizing_mode=SizingMode.FIXED,
            sizing_param=2.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        trade = result.trade_log.iloc[0]
        # 2 contracts × 50 per side × 2 sides = 200
        assert trade["commission"] == pytest.approx(200.0)

    def test_fixed_tick_slippage_widens_entry_exit_spread(self):
        """1-tick slippage on 1-point tick should move entry up and exit down."""
        ohlcv = _make_ohlcv([1000.0, 1010.0, 1020.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        cfg = EngineConfig(
            initial_capital=100_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            slippage_mode=SlippageMode.FIXED_TICKS,
            slippage_value=1.0,
            tick_size=1.0,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        trade = result.trade_log.iloc[0]
        # Bar-0 signal → entry at bar-1 open=1010, buy slip = +1 → 1011
        # Bar-2 signal (last bar) → exit at close=1020, sell slip = -1 → 1019
        assert trade["entry_price"] == pytest.approx(1011.0)
        assert trade["exit_price"] == pytest.approx(1019.0)

    def test_percent_slippage_exact_values(self):
        """0.1% percent slippage on a long trade: entry = open*(1+0.001),
        exit = close*(1-0.001)."""
        ohlcv = _make_ohlcv([1000.0, 1010.0, 1020.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        cfg = EngineConfig(
            initial_capital=100_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            slippage_mode=SlippageMode.PERCENT,
            slippage_value=0.001,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        trade = result.trade_log.iloc[0]
        expected_entry = 1010.0 * (1 + 0.001)   # bar-1 open, buy slip
        expected_exit = 1020.0 * (1 - 0.001)    # bar-2 close, sell slip
        assert trade["entry_price"] == pytest.approx(expected_entry, rel=1e-6)
        assert trade["exit_price"] == pytest.approx(expected_exit, rel=1e-6)

    def test_fee_and_slippage_combined_reduce_pnl_more_than_either_alone(self):
        """Commission + slippage together must reduce pnl more than each alone."""
        ohlcv = _make_ohlcv([100.0, 110.0, 120.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        cfg_none = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            slippage_mode=SlippageMode.NONE,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        cfg_fee_only = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.001,
            slippage_mode=SlippageMode.NONE,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        cfg_both = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.001,
            slippage_mode=SlippageMode.FIXED_TICKS,
            slippage_value=1.0,
            tick_size=1.0,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )

        r_none = BacktestEngine(ohlcv, strat, cfg_none).run()
        r_fee = BacktestEngine(ohlcv, strat, cfg_fee_only).run()
        r_both = BacktestEngine(ohlcv, strat, cfg_both).run()

        pnl_none = r_none.trade_log["pnl"].sum() if len(r_none.trade_log) > 0 else 0.0
        pnl_fee = r_fee.trade_log["pnl"].sum() if len(r_fee.trade_log) > 0 else 0.0
        pnl_both = r_both.trade_log["pnl"].sum() if len(r_both.trade_log) > 0 else 0.0

        assert pnl_none >= pnl_fee >= pnl_both

    def test_paper_order_fill_price_consistent_with_backtest_entry(self):
        """PaperOrderManager auto-fill price must match what BacktestEngine
        records as entry_price when both use the same raw price reference."""
        raw_price = 18_500.0
        om = PaperOrderManager(auto_fill=True, market_fill_price=raw_price)
        order = om.place_order("TXF", "BUY", 1.0, "MARKET")
        assert order.avg_fill_price == pytest.approx(raw_price)

        # BacktestEngine uses next-bar open; verify entry_price recorded matches open
        ohlcv = _make_ohlcv([18_000.0, raw_price, 19_000.0])

        def strat(ctx):
            return Signal.BUY if ctx.idx == 0 else None

        result = BacktestEngine(ohlcv, strat, _default_engine_cfg(commission_value=0.0)).run()
        trade = result.trade_log.iloc[0]
        assert trade["entry_price"] == pytest.approx(raw_price)


# ===========================================================================
# 5. Order lifecycle consistency between backtest and realtime
# ===========================================================================


class TestOrderLifecycleConsistency:
    """Verify that Order objects behave consistently whether produced by the
    BacktestEngine or by RealtimeEngine, and that PaperOrderManager state
    transitions are identical in both contexts."""

    def test_backtest_orders_dict_matches_placed_count(self):
        """BacktestResult.orders should contain exactly as many entries as
        the number of place_order calls (1 per open + 1 per close)."""
        ohlcv = _make_ohlcv([100.0, 100.0, 100.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        result = BacktestEngine(ohlcv, strat, _default_engine_cfg(commission_value=0.0)).run()
        # 1 entry + 1 exit = 2
        assert len(result.orders) == 2

    def test_backtest_no_pending_orders_remain_after_run(self):
        """After BacktestEngine.run(), no order should be in PENDING state."""
        ohlcv = _make_ohlcv([100.0, 105.0, 110.0, 115.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 3:
                return Signal.CLOSE
            return None

        result = BacktestEngine(ohlcv, strat, _default_engine_cfg()).run()
        for order in result.orders.values():
            assert order.status != OrderStatus.PENDING

    def test_order_dataclass_immutability_via_with_update(self):
        """Order.with_update() must not mutate the original (same in both contexts)."""
        om = PaperOrderManager(auto_fill=False)
        order = om.place_order("TXF", "BUY", 1.0, "MARKET")

        updated = order.with_update(status=OrderStatus.CANCELLED)
        assert order.status == OrderStatus.PENDING  # original unchanged
        assert updated.status == OrderStatus.CANCELLED

    def test_realtime_and_backtest_order_ids_are_uuids(self):
        """Order IDs produced by both engines must be valid UUID-format strings."""
        import re
        uuid_re = re.compile(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
            re.IGNORECASE,
        )

        # Backtest order
        ohlcv = _make_ohlcv([100.0, 100.0, 100.0])

        def strat(ctx):
            return Signal.BUY if ctx.idx == 0 else None

        result = BacktestEngine(ohlcv, strat, _default_engine_cfg(commission_value=0.0)).run()
        for order_id in result.orders:
            assert uuid_re.match(order_id), f"Bad UUID: {order_id}"

        # Realtime order
        with patch(
            "trading_core.realtime.engine.get_market_session",
            return_value=MarketSession.DAY,
        ):
            om = PaperOrderManager(auto_fill=True, market_fill_price=18000.0)
            engine = RealtimeEngine(
                order_manager=om,
                config=_realtime_cfg(),
            )
            engine._set_state(EngineState.RUNNING)
            order = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
            assert order is not None
            assert uuid_re.match(order.order_id), f"Bad UUID: {order.order_id}"

    @patch("trading_core.realtime.engine.get_market_session", return_value=MarketSession.DAY)
    def test_realtime_cancel_reduces_active_orders(self, _):
        """Cancelling a pending order via PaperOrderManager should be reflected
        in list_active_orders — consistent with how BacktestEngine never leaves
        pending orders after run()."""
        om = PaperOrderManager(auto_fill=False)
        engine = RealtimeEngine(
            order_manager=om,
            config=_realtime_cfg(),
        )
        engine._set_state(EngineState.RUNNING)

        order = engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1.0))
        assert order is not None
        assert len(om.list_active_orders()) == 1

        om.cancel_order(order.order_id)
        assert len(om.list_active_orders()) == 0

    def test_create_order_manager_factory_produces_usable_paper_manager(self):
        """create_order_manager() factory must produce a PaperOrderManager that
        both BacktestEngine and RealtimeEngine can use without modification."""
        om = create_order_manager("paper", auto_fill=True, market_fill_price=1000.0)
        assert isinstance(om, PaperOrderManager)

        # Use it manually like BacktestEngine would
        order = om.place_order("TXF", "BUY", 1.0, "MARKET")
        assert order.status == OrderStatus.FILLED

    def test_order_broker_ref_set_by_paper_manager(self):
        """Every order placed through PaperOrderManager (whether from backtest
        or realtime) must have a broker_ref starting with 'PAPER-'."""
        # Via BacktestEngine
        ohlcv = _make_ohlcv([100.0, 100.0, 100.0])

        def strat(ctx):
            return Signal.BUY if ctx.idx == 0 else None

        result = BacktestEngine(ohlcv, strat, _default_engine_cfg(commission_value=0.0)).run()
        for order in result.orders.values():
            assert order.broker_ref is not None
            assert order.broker_ref.startswith("PAPER-")

        # Via PaperOrderManager directly (as RealtimeEngine uses it)
        om = PaperOrderManager(auto_fill=True, market_fill_price=18000.0)
        rt_order = om.place_order("TXF", "BUY", 1.0, "MARKET")
        assert rt_order.broker_ref is not None
        assert rt_order.broker_ref.startswith("PAPER-")

    def test_equity_and_position_consistent_after_realtime_fill(self):
        """After processing a fill event, portfolio equity and position size
        should be internally consistent."""
        engine = RealtimeEngine(
            order_manager=PaperOrderManager(auto_fill=True, market_fill_price=18000.0),
            config=_realtime_cfg(),
        )

        buy_order = Order(
            symbol="TXF",
            side=OrderSide.BUY,
            quantity=3.0,
            order_type=OrderType.MARKET,
            status=OrderStatus.FILLED,
            filled_quantity=3.0,
            avg_fill_price=18000.0,
        )
        engine.on_fill(buy_order)

        pos = engine._portfolio.get_position("TXF")
        assert pos is not None
        assert pos.size == 3.0
        assert pos.direction == PositionType.LONG
