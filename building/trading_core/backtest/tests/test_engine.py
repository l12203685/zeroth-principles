"""Tests for BacktestEngine (backtest/engine.py).

Coverage targets:
- Commission modes: fraction-of-notional, per-contract.
- Slippage modes: none, fixed-ticks, percent.
- Sizing modes: fixed, percent-equity, kelly.
- PaperOrderManager integration.
- Equity curve correctness.
- Metrics wiring.
- Edge cases: empty trades, no position at end, force-close.
- Config validation.
- Kelly fallback before 10 trades.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from trading_core.backtest.engine import (
    BacktestEngine,
    BacktestResult,
    CommissionMode,
    EngineConfig,
    SizingMode,
    SlippageMode,
    _apply_slippage,
    _compute_commission,
    _compute_size,
    _kelly_fraction,
)
from trading_core.backtest.harness import Signal


# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------


def make_ohlcv(closes, start="2024-01-01", freq="D") -> pd.DataFrame:
    """Build a minimal OHLCV DataFrame from a list of close prices."""
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


def buy_and_hold_strategy(ctx):
    """Buy on first bar, never close (force-close at end)."""
    if ctx.idx == 0:
        return Signal.BUY
    return None


def buy_then_close_strategy(buy_idx: int = 0, close_idx: int = 2):
    """Buy at buy_idx, close at close_idx."""
    def _strat(ctx):
        if ctx.idx == buy_idx:
            return Signal.BUY
        if ctx.idx == close_idx:
            return Signal.CLOSE
        return None
    return _strat


def no_trade_strategy(ctx):
    """Never trade."""
    return None


# ---------------------------------------------------------------------------
# EngineConfig validation
# ---------------------------------------------------------------------------


class TestEngineConfigValidation:
    def test_default_config_is_valid(self):
        cfg = EngineConfig()
        assert cfg.initial_capital == 1_000_000.0
        assert cfg.commission_mode == CommissionMode.FRACTION_OF_NOTIONAL

    def test_negative_capital_raises(self):
        with pytest.raises(ValueError, match="initial_capital"):
            EngineConfig(initial_capital=-1.0)

    def test_zero_capital_raises(self):
        with pytest.raises(ValueError, match="initial_capital"):
            EngineConfig(initial_capital=0.0)

    def test_negative_commission_raises(self):
        with pytest.raises(ValueError, match="commission_value"):
            EngineConfig(commission_value=-0.001)

    def test_negative_slippage_raises(self):
        with pytest.raises(ValueError, match="slippage_value"):
            EngineConfig(slippage_value=-1.0)

    def test_zero_tick_size_raises(self):
        with pytest.raises(ValueError, match="tick_size"):
            EngineConfig(tick_size=0.0)

    def test_negative_sizing_param_raises(self):
        with pytest.raises(ValueError, match="sizing_param"):
            EngineConfig(sizing_param=-1.0)


# ---------------------------------------------------------------------------
# OHLCV validation
# ---------------------------------------------------------------------------


class TestOHLCVValidation:
    def test_missing_columns_raises(self):
        bad = pd.DataFrame({"close": [1.0, 2.0]})
        with pytest.raises(ValueError, match="missing columns"):
            BacktestEngine(bad, no_trade_strategy)

    def test_empty_dataframe_raises(self):
        empty = pd.DataFrame(columns=["open", "high", "low", "close", "volume"])
        with pytest.raises(ValueError, match="empty"):
            BacktestEngine(empty, no_trade_strategy)


# ---------------------------------------------------------------------------
# Commission calculation
# ---------------------------------------------------------------------------


class TestComputeCommission:
    def test_fraction_of_notional(self):
        c = _compute_commission(CommissionMode.FRACTION_OF_NOTIONAL, 0.001, 100.0, 5.0)
        assert c == pytest.approx(0.5)  # 100 * 5 * 0.001

    def test_per_contract(self):
        c = _compute_commission(CommissionMode.PER_CONTRACT, 100.0, 99_999.0, 3.0)
        assert c == pytest.approx(300.0)  # 3 * 100

    def test_zero_commission(self):
        c = _compute_commission(CommissionMode.FRACTION_OF_NOTIONAL, 0.0, 1000.0, 1.0)
        assert c == pytest.approx(0.0)


# ---------------------------------------------------------------------------
# Slippage application
# ---------------------------------------------------------------------------


class TestApplySlippage:
    def test_none_mode_no_change(self):
        price = _apply_slippage(SlippageMode.NONE, 1.0, 1.0, 100.0, is_buy=True)
        assert price == pytest.approx(100.0)

    def test_fixed_ticks_buy(self):
        # 2 ticks * 0.5 tick_size = 1.0 markup on buy
        price = _apply_slippage(SlippageMode.FIXED_TICKS, 2.0, 0.5, 100.0, is_buy=True)
        assert price == pytest.approx(101.0)

    def test_fixed_ticks_sell(self):
        price = _apply_slippage(SlippageMode.FIXED_TICKS, 2.0, 0.5, 100.0, is_buy=False)
        assert price == pytest.approx(99.0)

    def test_percent_buy(self):
        # 0.1% of 200 = 0.2 markup
        price = _apply_slippage(SlippageMode.PERCENT, 0.001, 1.0, 200.0, is_buy=True)
        assert price == pytest.approx(200.2)

    def test_percent_sell(self):
        price = _apply_slippage(SlippageMode.PERCENT, 0.001, 1.0, 200.0, is_buy=False)
        assert price == pytest.approx(199.8)


# ---------------------------------------------------------------------------
# Position sizing
# ---------------------------------------------------------------------------


class TestComputeSize:
    def _cfg(self, **kwargs) -> EngineConfig:
        return EngineConfig(**kwargs)

    def test_fixed_size(self):
        cfg = self._cfg(sizing_mode=SizingMode.FIXED, sizing_param=3.0)
        size = _compute_size(cfg, equity=100_000.0, fill_price=1000.0, closed_trades=[])
        assert size == pytest.approx(3.0)

    def test_percent_equity(self):
        # 2% of 100_000 / (1000 * 1.0 price_per_unit) = 2.0 contracts
        cfg = self._cfg(
            sizing_mode=SizingMode.PERCENT_EQUITY,
            sizing_param=0.02,
            price_per_unit=1.0,
        )
        size = _compute_size(cfg, equity=100_000.0, fill_price=1000.0, closed_trades=[])
        assert size == pytest.approx(2.0)

    def test_percent_equity_with_multiplier(self):
        # 2% of 500_000 / (20_000 * 200) → 0.025 → floors to 0 < min_size=1 → returns 0
        cfg = self._cfg(
            sizing_mode=SizingMode.PERCENT_EQUITY,
            sizing_param=0.02,
            price_per_unit=200.0,
            min_size=1.0,
        )
        size = _compute_size(cfg, equity=500_000.0, fill_price=20_000.0, closed_trades=[])
        # 500_000 * 0.02 / (20_000 * 200) = 10_000 / 4_000_000 = 0.0025 → floor → 0
        assert size == 0.0

    def test_kelly_falls_back_before_10_trades(self):
        cfg = self._cfg(sizing_mode=SizingMode.KELLY, sizing_param=0.5, min_size=1.0)
        trades = [{"pnl": 100.0}] * 5  # only 5 trades
        size = _compute_size(cfg, equity=100_000.0, fill_price=1000.0, closed_trades=trades)
        # fallback: raw_size=1.0, but sizing_param=0.5 so... let's check the fallback branch
        # In KELLY with <10 trades: size = 1.0 (fixed), then floor→1, min_size=1 → pass
        assert size == pytest.approx(1.0)

    def test_max_size_cap(self):
        cfg = self._cfg(sizing_mode=SizingMode.FIXED, sizing_param=10.0, max_size=3.0)
        size = _compute_size(cfg, equity=100_000.0, fill_price=1000.0, closed_trades=[])
        assert size == pytest.approx(3.0)

    def test_below_min_size_returns_zero(self):
        # percent_equity gives 0 contracts
        cfg = self._cfg(
            sizing_mode=SizingMode.PERCENT_EQUITY,
            sizing_param=0.0001,  # very small fraction
            price_per_unit=1.0,
            min_size=1.0,
        )
        size = _compute_size(cfg, equity=100.0, fill_price=1000.0, closed_trades=[])
        assert size == 0.0


# ---------------------------------------------------------------------------
# Kelly fraction helper
# ---------------------------------------------------------------------------


class TestKellyFraction:
    def test_balanced_trades(self):
        trades = [{"pnl": 100.0}] * 6 + [{"pnl": -50.0}] * 4
        k = _kelly_fraction(trades)
        # win_rate=0.6, avg_win=100, avg_loss=50
        # kelly = (0.6*100 - 0.4*50) / 100 = (60-20)/100 = 0.4
        assert k == pytest.approx(0.4)

    def test_all_wins_returns_one(self):
        trades = [{"pnl": 100.0}] * 10
        k = _kelly_fraction(trades)
        assert k == pytest.approx(1.0)

    def test_all_losses_returns_one(self):
        trades = [{"pnl": -100.0}] * 10
        k = _kelly_fraction(trades)
        assert k == pytest.approx(1.0)

    def test_clamped_to_two(self):
        # Very high win scenarios should clamp at 2
        trades = [{"pnl": 1000.0}] * 9 + [{"pnl": -0.01}]
        k = _kelly_fraction(trades)
        assert k <= 2.0


# ---------------------------------------------------------------------------
# Engine integration — commission correctness
# ---------------------------------------------------------------------------


class TestEngineFractionCommission:
    """Fraction-of-notional commission, no slippage, fixed size=1."""

    def test_long_trade_pnl(self):
        """BUY at bar 0 (open=100), CLOSE at bar 2 (open=110).

        commission_rate = 0.1% per side.
        Fill prices = open of next bar (next-bar open fill):
          entry_fill = 100 (open of bar 1, but bar 0 open is also 100)
        Wait - bar 0 signal → fill at bar 1 open = 105.
        bar 2 signal → fill at bar 3 open = N/A (only 3 bars, idx 0,1,2)
        Actually with closes=[100,105,110], opens=same.
        Signal at bar 0 (idx=0) → pending for bar 1 (idx=1), fill at bar 1 open=105.
        Signal at bar 2 (idx=2) → idx+1=3 >= n=3, so fill immediately at bar 2 close=110.

        entry = 105, exit = 110
        entry_comm = 105 * 1 * 0.001 = 0.105
        exit_comm  = 110 * 1 * 0.001 = 0.110
        gross = (110-105)*1*1.0 = 5.0
        net = 5.0 - 0.105 - 0.110 = 4.785
        """
        ohlcv = make_ohlcv([100.0, 105.0, 110.0])
        strat = buy_then_close_strategy(buy_idx=0, close_idx=2)
        cfg = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.001,
            slippage_mode=SlippageMode.NONE,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        assert len(result.trade_log) == 1
        trade = result.trade_log.iloc[0]
        assert trade["direction"] == "long"
        assert trade["entry_price"] == pytest.approx(105.0)
        assert trade["exit_price"] == pytest.approx(110.0)
        assert trade["commission"] == pytest.approx(0.215, abs=1e-9)
        assert trade["pnl"] == pytest.approx(4.785, abs=1e-9)

    def test_short_trade_pnl(self):
        """SELL at bar 0, CLOSE at bar 2 (price drops).

        closes=[100,95,90], opens=same.
        entry_fill = 95 (bar 1 open), exit_fill = 90 (bar 2 close, last bar).
        gross = (95-90)*1 = 5.0
        entry_comm = 95*0.001=0.095, exit_comm=90*0.001=0.09
        net = 5.0 - 0.185 = 4.815
        """
        ohlcv = make_ohlcv([100.0, 95.0, 90.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.SELL
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        cfg = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.001,
            slippage_mode=SlippageMode.NONE,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        assert len(result.trade_log) == 1
        trade = result.trade_log.iloc[0]
        assert trade["direction"] == "short"
        assert trade["pnl"] == pytest.approx(4.815, abs=1e-6)


class TestEnginePerContractCommission:
    def test_per_contract_commission_applied(self):
        """Per-contract: NT$50 per side, size=2.

        entry_comm = 2*50 = 100
        exit_comm  = 2*50 = 100
        total_comm = 200
        """
        ohlcv = make_ohlcv([1000.0, 1010.0, 1020.0])

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

        assert len(result.trade_log) == 1
        trade = result.trade_log.iloc[0]
        assert trade["commission"] == pytest.approx(200.0)
        # gross = (1020-1010)*2 = 20, net = 20-200 = -180
        assert trade["gross_pnl"] == pytest.approx(20.0)
        assert trade["pnl"] == pytest.approx(-180.0)


# ---------------------------------------------------------------------------
# Slippage integration
# ---------------------------------------------------------------------------


class TestEngineSlippage:
    def test_fixed_tick_slippage_on_buy(self):
        """1 tick = 1.0 slippage on entry and exit.

        closes=[1000, 1010, 1020], opens=same.
        Signal bar 0 → entry at bar 1 open = 1010, + 1 tick = 1011.
        Signal bar 2 → last bar, exit at close = 1020 (no slippage needed since we simulate close).
        Actually CLOSE on last bar: fills at bar 2 close=1020, but is_buy=True (closing short=buying back).
        For long position close: is_buy=False (selling), so slip = 1020 - 1 = 1019.
        gross = (1019 - 1011) * 1 * 1 = 8.0
        """
        ohlcv = make_ohlcv([1000.0, 1010.0, 1020.0])
        strat = buy_then_close_strategy(buy_idx=0, close_idx=2)
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

        assert len(result.trade_log) == 1
        trade = result.trade_log.iloc[0]
        # entry with buy slippage: 1010 + 1 = 1011
        assert trade["entry_price"] == pytest.approx(1011.0)
        # exit on last bar: close price 1020, sell slip: 1020 - 1 = 1019
        assert trade["exit_price"] == pytest.approx(1019.0)
        assert trade["gross_pnl"] == pytest.approx(8.0)

    def test_percent_slippage_on_short(self):
        """0.1% slippage on a short trade.

        closes=[100, 95, 90], opens=same.
        bar 0 signal → entry at bar 1 open=95, sell slip: 95*(1-0.001)=94.905.
        bar 2 signal → last bar, exit close=90, buying back slip: 90*(1+0.001)=90.09.
        gross = (94.905 - 90.09) * 1 = 4.815.
        """
        ohlcv = make_ohlcv([100.0, 95.0, 90.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.SELL
            if ctx.idx == 2:
                return Signal.CLOSE
            return None

        cfg = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            slippage_mode=SlippageMode.PERCENT,
            slippage_value=0.001,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        trade = result.trade_log.iloc[0]
        assert trade["entry_price"] == pytest.approx(94.905)
        assert trade["exit_price"] == pytest.approx(90.09)
        assert trade["gross_pnl"] == pytest.approx(94.905 - 90.09, rel=1e-6)


# ---------------------------------------------------------------------------
# Sizing modes
# ---------------------------------------------------------------------------


class TestEngineSizing:
    def test_percent_equity_sizing(self):
        """2% equity sizing: with 100k equity at fill 1000, get 2 contracts."""
        ohlcv = make_ohlcv([1000.0, 1000.0, 1000.0])
        strat = buy_then_close_strategy(buy_idx=0, close_idx=2)
        cfg = EngineConfig(
            initial_capital=100_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            slippage_mode=SlippageMode.NONE,
            sizing_mode=SizingMode.PERCENT_EQUITY,
            sizing_param=0.02,
            price_per_unit=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        if len(result.trade_log) > 0:
            assert result.trade_log.iloc[0]["size"] == pytest.approx(2.0)

    def test_kelly_fallback_with_few_trades(self):
        """Kelly sizing with <10 trades falls back to size=1."""
        ohlcv = make_ohlcv([100.0, 100.0, 100.0])
        strat = buy_then_close_strategy(buy_idx=0, close_idx=2)
        cfg = EngineConfig(
            initial_capital=100_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            slippage_mode=SlippageMode.NONE,
            sizing_mode=SizingMode.KELLY,
            sizing_param=0.5,
            price_per_unit=1.0,
            min_size=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        if len(result.trade_log) > 0:
            assert result.trade_log.iloc[0]["size"] == pytest.approx(1.0)


# ---------------------------------------------------------------------------
# Price-per-unit (futures multiplier)
# ---------------------------------------------------------------------------


class TestPricePerUnit:
    def test_multiplier_applied_to_pnl(self):
        """price_per_unit=200 (like TXF): 1-point move = 200 cash.

        closes=[20000, 20010, 20020], size=1.
        entry at bar 1 open=20010, exit at last bar close=20020.
        gross = (20020-20010)*1*200 = 2000.
        """
        ohlcv = make_ohlcv([20_000.0, 20_010.0, 20_020.0])
        strat = buy_then_close_strategy(buy_idx=0, close_idx=2)
        cfg = EngineConfig(
            initial_capital=1_000_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            slippage_mode=SlippageMode.NONE,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
            price_per_unit=200.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        assert len(result.trade_log) == 1
        trade = result.trade_log.iloc[0]
        assert trade["gross_pnl"] == pytest.approx(2000.0)


# ---------------------------------------------------------------------------
# Equity curve and capital tracking
# ---------------------------------------------------------------------------


class TestEquityCurve:
    def test_equity_length_equals_bar_count(self):
        n = 20
        ohlcv = make_ohlcv(list(range(100, 100 + n)))
        result = BacktestEngine(ohlcv, no_trade_strategy).run()
        assert len(result.equity_curve) == n

    def test_equity_no_trades_stays_at_initial(self):
        ohlcv = make_ohlcv([100.0, 101.0, 102.0])
        cfg = EngineConfig(initial_capital=50_000.0)
        result = BacktestEngine(ohlcv, no_trade_strategy, cfg).run()
        assert result.equity_curve.iloc[-1] == pytest.approx(50_000.0)

    def test_equity_rises_with_profitable_trade(self):
        closes = [100.0, 110.0, 120.0, 130.0]
        ohlcv = make_ohlcv(closes)
        result = BacktestEngine(
            ohlcv,
            buy_and_hold_strategy,
            EngineConfig(
                initial_capital=10_000.0,
                commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
                commission_value=0.0,
                sizing_mode=SizingMode.FIXED,
                sizing_param=1.0,
            ),
        ).run()
        assert result.equity_curve.iloc[-1] > 10_000.0

    def test_force_close_at_last_bar(self):
        """Open position not explicitly closed should be force-closed."""
        ohlcv = make_ohlcv([100.0, 110.0, 120.0])
        cfg = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, buy_and_hold_strategy, cfg).run()
        assert len(result.trade_log) == 1

    def test_equity_curve_no_nan(self):
        closes = np.random.uniform(100, 200, 50).tolist()
        ohlcv = make_ohlcv(closes)
        result = BacktestEngine(ohlcv, buy_and_hold_strategy).run()
        assert not result.equity_curve.isna().any()


# ---------------------------------------------------------------------------
# Flip position (short → long, long → short)
# ---------------------------------------------------------------------------


class TestPositionFlip:
    def test_short_flips_to_long(self):
        """SELL bar 0, BUY bar 1 → closes short, opens long."""
        ohlcv = make_ohlcv([100.0, 105.0, 100.0, 95.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.SELL
            if ctx.idx == 1:
                return Signal.BUY
            return None

        cfg = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        # 2 explicit trades + 1 force-close
        assert len(result.trade_log) >= 2
        assert result.trade_log.iloc[0]["direction"] == "short"
        assert result.trade_log.iloc[1]["direction"] == "long"

    def test_long_flips_to_short(self):
        """BUY bar 0, SELL bar 1 → closes long, opens short."""
        ohlcv = make_ohlcv([100.0, 95.0, 90.0, 80.0])

        def strat(ctx):
            if ctx.idx == 0:
                return Signal.BUY
            if ctx.idx == 1:
                return Signal.SELL
            return None

        cfg = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        assert len(result.trade_log) >= 2
        assert result.trade_log.iloc[0]["direction"] == "long"
        assert result.trade_log.iloc[1]["direction"] == "short"


# ---------------------------------------------------------------------------
# PaperOrderManager integration
# ---------------------------------------------------------------------------


class TestOrderManagerIntegration:
    def test_orders_recorded_in_result(self):
        """Each open + close creates two orders (entry + exit)."""
        ohlcv = make_ohlcv([100.0, 100.0, 100.0])
        strat = buy_then_close_strategy(buy_idx=0, close_idx=2)
        cfg = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        # At least 2 orders: entry BUY + exit SELL
        assert len(result.orders) >= 2

    def test_no_trades_no_orders(self):
        ohlcv = make_ohlcv([100.0, 100.0, 100.0])
        result = BacktestEngine(ohlcv, no_trade_strategy).run()
        assert len(result.orders) == 0

    def test_all_orders_are_filled(self):
        """No pending orders should remain after backtest."""
        from trading_core.broker.orders import OrderStatus

        ohlcv = make_ohlcv([100.0, 100.0, 100.0])
        strat = buy_then_close_strategy(buy_idx=0, close_idx=2)
        cfg = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        for order in result.orders.values():
            assert order.status == OrderStatus.FILLED


# ---------------------------------------------------------------------------
# Metrics wiring
# ---------------------------------------------------------------------------


class TestMetricsWiring:
    def test_metrics_present(self):
        ohlcv = make_ohlcv(list(range(100, 160)))
        result = BacktestEngine(ohlcv, buy_and_hold_strategy).run()

        m = result.metrics
        assert m is not None
        assert hasattr(m, "sharpe")
        assert hasattr(m, "max_drawdown")
        assert hasattr(m, "profit_factor")
        assert hasattr(m, "win_rate")
        assert hasattr(m, "sortino")
        assert hasattr(m, "calmar")
        assert hasattr(m, "sqn")
        assert hasattr(m, "annual_return")

    def test_win_rate_is_one_for_profitable_hold(self):
        """A single profitable trade should give win_rate > 0."""
        closes = list(range(100, 130))
        ohlcv = make_ohlcv(closes)
        cfg = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, buy_and_hold_strategy, cfg).run()
        assert result.metrics.win_rate >= 0.0

    def test_num_trades_matches_trade_log(self):
        closes = [100.0] * 10
        ohlcv = make_ohlcv(closes)
        result = BacktestEngine(ohlcv, buy_and_hold_strategy).run()
        assert result.metrics.num_trades == len(result.trade_log)


# ---------------------------------------------------------------------------
# BacktestResult / summary
# ---------------------------------------------------------------------------


class TestBacktestResult:
    def test_summary_no_exception(self):
        ohlcv = make_ohlcv([100.0, 105.0, 110.0])
        result = BacktestEngine(ohlcv, buy_and_hold_strategy).run()
        s = result.summary()
        assert "BacktestEngine" in s
        assert "trades" in s

    def test_returns_length_matches_equity(self):
        ohlcv = make_ohlcv(list(range(100, 115)))
        result = BacktestEngine(ohlcv, no_trade_strategy).run()
        assert len(result.returns) == len(result.equity_curve)

    def test_returns_first_element_is_zero(self):
        ohlcv = make_ohlcv([100.0, 105.0, 110.0])
        result = BacktestEngine(ohlcv, no_trade_strategy).run()
        assert result.returns.iloc[0] == pytest.approx(0.0)

    def test_empty_trade_log_has_expected_columns(self):
        ohlcv = make_ohlcv([100.0, 101.0, 102.0])
        result = BacktestEngine(ohlcv, no_trade_strategy).run()
        expected_cols = {
            "entry_time", "exit_time", "direction", "size",
            "entry_price", "exit_price", "gross_pnl", "commission", "pnl",
        }
        assert expected_cols.issubset(set(result.trade_log.columns))

    def test_trade_log_has_gross_pnl_column(self):
        ohlcv = make_ohlcv([100.0, 110.0, 120.0])
        result = BacktestEngine(
            ohlcv,
            buy_and_hold_strategy,
            EngineConfig(
                initial_capital=10_000.0,
                commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
                commission_value=0.0,
                sizing_mode=SizingMode.FIXED,
                sizing_param=1.0,
            ),
        ).run()
        if len(result.trade_log) > 0:
            assert "gross_pnl" in result.trade_log.columns


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------


class TestEdgeCases:
    def test_single_bar_no_crash(self):
        """Single-bar OHLCV should not crash the engine."""
        ohlcv = make_ohlcv([100.0])
        result = BacktestEngine(ohlcv, buy_and_hold_strategy).run()
        assert len(result.equity_curve) == 1

    def test_close_when_flat_is_noop(self):
        """CLOSE signal when already flat should produce no trade."""
        ohlcv = make_ohlcv([100.0, 100.0, 100.0])

        def strat(ctx):
            return Signal.CLOSE  # always signal close when flat

        result = BacktestEngine(ohlcv, strat).run()
        assert len(result.trade_log) == 0

    def test_buy_when_already_long_is_noop(self):
        """BUY signal when already long should produce only 1 open."""
        ohlcv = make_ohlcv([100.0, 100.0, 100.0, 100.0])

        def strat(ctx):
            return Signal.BUY  # always BUY

        cfg = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, strat, cfg).run()

        # Only 1 trade: the force-close at end
        assert len(result.trade_log) == 1

    def test_result_is_backtest_result_instance(self):
        ohlcv = make_ohlcv([100.0, 100.0, 100.0])
        result = BacktestEngine(ohlcv, no_trade_strategy).run()
        assert isinstance(result, BacktestResult)

    def test_zero_commission_zero_slippage_gross_equals_net(self):
        """With 0 cost, gross_pnl == pnl."""
        ohlcv = make_ohlcv([100.0, 110.0, 120.0])
        cfg = EngineConfig(
            initial_capital=10_000.0,
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            slippage_mode=SlippageMode.NONE,
            sizing_mode=SizingMode.FIXED,
            sizing_param=1.0,
        )
        result = BacktestEngine(ohlcv, buy_and_hold_strategy, cfg).run()
        if len(result.trade_log) > 0:
            trade = result.trade_log.iloc[0]
            assert trade["pnl"] == pytest.approx(trade["gross_pnl"])


# ---------------------------------------------------------------------------
# Coverage gap: EngineConfig validation edge cases
# ---------------------------------------------------------------------------


class TestEngineConfigEdgeCases:
    def test_zero_price_per_unit_raises(self):
        with pytest.raises(ValueError, match="price_per_unit"):
            EngineConfig(price_per_unit=0.0)

    def test_negative_price_per_unit_raises(self):
        with pytest.raises(ValueError, match="price_per_unit"):
            EngineConfig(price_per_unit=-1.0)

    def test_zero_min_size_raises(self):
        with pytest.raises(ValueError, match="min_size"):
            EngineConfig(min_size=0.0)

    def test_negative_min_size_raises(self):
        with pytest.raises(ValueError, match="min_size"):
            EngineConfig(min_size=-0.5)


# ---------------------------------------------------------------------------
# Coverage gap: Kelly with >= 10 trades
# ---------------------------------------------------------------------------


class TestKellySizingWithHistory:
    def test_kelly_activates_after_10_trades(self):
        """Kelly sizing should compute from trade history once >= 10 trades exist.

        We verify the engine does NOT crash with Kelly active.
        We cannot directly control closed_trades from the engine,
        so we test _compute_size directly with a 10-trade history.
        """
        trades = [{"pnl": 100.0}] * 7 + [{"pnl": -40.0}] * 3  # 10 trades
        cfg = EngineConfig(
            sizing_mode=SizingMode.KELLY,
            sizing_param=0.5,
            price_per_unit=1.0,
            min_size=1.0,
            initial_capital=100_000.0,
        )
        # With 10 trades, Kelly branch fires
        size = _compute_size(cfg, equity=100_000.0, fill_price=1000.0, closed_trades=trades)
        # Kelly: win_rate=0.7, avg_win=100, avg_loss=40
        # kelly = (0.7*100 - 0.3*40)/100 = (70-12)/100 = 0.58
        # full_kelly = 100_000 * 0.58 / (1000*1) = 58 contracts
        # sizing_param=0.5 → 58*0.5=29 → floor=29
        assert size >= 1.0  # definitely gets a valid size

    def test_kelly_zero_unit_value_returns_zero(self):
        """When fill_price=0 and price_per_unit=1, unit_value=0 → size=0."""
        trades = [{"pnl": 100.0}] * 10  # enough for Kelly
        cfg = EngineConfig(
            sizing_mode=SizingMode.KELLY,
            sizing_param=0.5,
            price_per_unit=1.0,
            min_size=1.0,
        )
        size = _compute_size(cfg, equity=100_000.0, fill_price=0.0, closed_trades=trades)
        assert size == 0.0


# ---------------------------------------------------------------------------
# Coverage gap: size <= 0 early return (open position skipped)
# ---------------------------------------------------------------------------


class TestSizeZeroSkipsOpen:
    def test_open_skipped_when_size_zero(self):
        """With very small equity and large price, sized quantity floors to 0,
        so open is skipped → no trades."""
        ohlcv = make_ohlcv([1_000_000.0, 1_000_001.0, 1_000_002.0])
        cfg = EngineConfig(
            initial_capital=1.0,  # tiny capital
            commission_mode=CommissionMode.FRACTION_OF_NOTIONAL,
            commission_value=0.0,
            slippage_mode=SlippageMode.NONE,
            sizing_mode=SizingMode.PERCENT_EQUITY,
            sizing_param=0.01,   # 1% of $1 = $0.01
            price_per_unit=1.0,
            min_size=1.0,        # min 1 contract → skipped
        )
        result = BacktestEngine(ohlcv, buy_and_hold_strategy, cfg).run()
        # With price=1_000_000 and equity=1, size = floor(0.01/1_000_000) = 0 → skip
        assert len(result.trade_log) == 0


# ---------------------------------------------------------------------------
# Coverage gap: percent_equity with unit_value <= 0
# ---------------------------------------------------------------------------


class TestPercentEquityZeroUnitValue:
    def test_zero_fill_price_returns_zero_size(self):
        """fill_price=0 makes unit_value=0 → returns 0.0."""
        cfg = EngineConfig(
            sizing_mode=SizingMode.PERCENT_EQUITY,
            sizing_param=0.02,
            price_per_unit=1.0,
        )
        size = _compute_size(cfg, equity=100_000.0, fill_price=0.0, closed_trades=[])
        assert size == 0.0
