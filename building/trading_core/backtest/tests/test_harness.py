"""Tests for Backtester MVP.

Core invariant under test: a single simulated trade produces the exact
expected net P&L given commission rate and price path.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from trading_core.backtest import (
    Backtester,
    BacktestConfig,
    Signal,
    sma_cross_strategy,
)


def _make_ohlcv(closes, start="2024-01-01", freq="D") -> pd.DataFrame:
    idx = pd.date_range(start=start, periods=len(closes), freq=freq)
    return pd.DataFrame(
        {
            "open": closes,
            "high": [c * 1.01 for c in closes],
            "low": [c * 0.99 for c in closes],
            "close": closes,
            "volume": [1000.0] * len(closes),
        },
        index=idx,
    )


# ---------------------------------------------------------------------------
# Single-trade PnL correctness
# ---------------------------------------------------------------------------


def test_single_long_trade_pnl():
    """BUY at 100, CLOSE at 110, size 1, commission 0.1% per side.

    Expected:
      entry_commission = 100 * 1 * 0.001 = 0.10
      exit_commission  = 110 * 1 * 0.001 = 0.11
      gross            = (110 - 100) * 1 = 10.00
      net pnl          = 10.00 - 0.21     = 9.79
    """
    ohlcv = _make_ohlcv([100.0, 105.0, 110.0])

    calls = {"n": 0}

    def strat(ctx):
        calls["n"] += 1
        if ctx.idx == 0:
            return Signal.BUY
        if ctx.idx == 2:
            return Signal.CLOSE
        return None

    config = BacktestConfig(
        initial_capital=10_000.0,
        commission_rate=0.001,
        size=1.0,
    )
    result = Backtester(ohlcv, strat, config).run()

    assert len(result.trade_log) == 1
    trade = result.trade_log.iloc[0]

    assert trade["direction"] == "long"
    assert trade["entry_price"] == pytest.approx(100.0)
    assert trade["exit_price"] == pytest.approx(110.0)
    assert trade["commission"] == pytest.approx(0.21, abs=1e-9)
    assert trade["pnl"] == pytest.approx(9.79, abs=1e-9)

    # Final equity = initial + net pnl
    assert result.equity_curve.iloc[-1] == pytest.approx(
        10_000.0 + 9.79, abs=1e-6
    )


def test_single_short_trade_pnl():
    """SELL at 100, CLOSE at 90 -> profit on short."""
    ohlcv = _make_ohlcv([100.0, 95.0, 90.0])

    def strat(ctx):
        if ctx.idx == 0:
            return Signal.SELL
        if ctx.idx == 2:
            return Signal.CLOSE
        return None

    config = BacktestConfig(
        initial_capital=10_000.0, commission_rate=0.001, size=1.0
    )
    result = Backtester(ohlcv, strat, config).run()

    assert len(result.trade_log) == 1
    trade = result.trade_log.iloc[0]
    # gross = (100-90)*1 = 10; commission = 0.1 + 0.09 = 0.19
    assert trade["direction"] == "short"
    assert trade["commission"] == pytest.approx(0.19, abs=1e-9)
    assert trade["pnl"] == pytest.approx(9.81, abs=1e-9)


def test_open_position_force_closed_at_end():
    """Open BUY never explicitly closed -> force-closed at last bar."""
    ohlcv = _make_ohlcv([100.0, 105.0, 108.0])

    def strat(ctx):
        return Signal.BUY if ctx.idx == 0 else None

    result = Backtester(
        ohlcv, strat, BacktestConfig(commission_rate=0.0, size=1.0)
    ).run()

    assert len(result.trade_log) == 1
    assert result.trade_log.iloc[0]["exit_price"] == pytest.approx(108.0)
    assert result.trade_log.iloc[0]["pnl"] == pytest.approx(8.0)


def test_buy_flips_short_to_long():
    """BUY while short should close short, then open long."""
    ohlcv = _make_ohlcv([100.0, 110.0, 105.0])

    def strat(ctx):
        if ctx.idx == 0:
            return Signal.SELL
        if ctx.idx == 1:
            return Signal.BUY
        return None

    result = Backtester(
        ohlcv, strat, BacktestConfig(commission_rate=0.0, size=1.0)
    ).run()

    # Expect 2 trades: short 100->110 (loss -10), long 110->105 force-close (-5)
    assert len(result.trade_log) == 2
    assert result.trade_log.iloc[0]["direction"] == "short"
    assert result.trade_log.iloc[0]["pnl"] == pytest.approx(-10.0)
    assert result.trade_log.iloc[1]["direction"] == "long"
    assert result.trade_log.iloc[1]["pnl"] == pytest.approx(-5.0)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def test_missing_columns_raises():
    bad = pd.DataFrame({"close": [1.0, 2.0]})
    with pytest.raises(ValueError, match="missing columns"):
        Backtester(bad, lambda ctx: None)


def test_empty_dataframe_raises():
    empty = pd.DataFrame(
        columns=["open", "high", "low", "close", "volume"]
    )
    with pytest.raises(ValueError, match="empty"):
        Backtester(empty, lambda ctx: None)


# ---------------------------------------------------------------------------
# SMA cross sanity
# ---------------------------------------------------------------------------


def test_sma_cross_runs_and_produces_trades():
    # Downtrend then uptrend -> at least one crossover.
    n = 80
    closes = list(np.linspace(100, 80, n // 2)) + list(
        np.linspace(80, 120, n - n // 2)
    )
    ohlcv = _make_ohlcv(closes)

    strat = sma_cross_strategy(fast=5, slow=20)
    result = Backtester(ohlcv, strat, BacktestConfig()).run()

    assert len(result.equity_curve) == len(ohlcv)
    assert len(result.trade_log) >= 1
    # equity curve length equals bar count
    assert not result.equity_curve.isna().any()


def test_sma_cross_invalid_params():
    with pytest.raises(ValueError):
        sma_cross_strategy(fast=30, slow=10)


# ---------------------------------------------------------------------------
# Result wiring
# ---------------------------------------------------------------------------


def test_result_has_metrics_and_returns():
    ohlcv = _make_ohlcv([100.0, 101.0, 102.0, 103.0])

    def strat(ctx):
        if ctx.idx == 0:
            return Signal.BUY
        return None

    result = Backtester(
        ohlcv, strat, BacktestConfig(commission_rate=0.0)
    ).run()

    assert result.metrics is not None
    assert len(result.returns) == len(ohlcv)
    assert result.returns.iloc[0] == pytest.approx(0.0)  # first bar zero
    # summary() should not raise
    assert "Backtest:" in result.summary()
