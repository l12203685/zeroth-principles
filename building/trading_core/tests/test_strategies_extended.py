"""Unit tests for the 5 extended PLA-derived strategies.

Phase 1 pass gate: at least 3 strategies must complete >=5 closed trades on
the synthetic test fixture.  This test asserts that gate directly.
"""

from __future__ import annotations

from typing import Dict, List

import numpy as np
import pandas as pd
import pytest

from trading_core.strategy import (
    CCIConfig,
    CCIStrategy,
    DMIConfig,
    DMIStrategy,
    KeltnerConfig,
    KeltnerStrategy,
    MACDConfig,
    MACDStrategy,
    ORBConfig,
    ORBStrategy,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _sin_trend_series(
    n: int,
    seed: int = 7,
    base: float = 1000.0,
    amp: float = 80.0,
    period: int = 25,
    drift: float = 0.05,
    noise: float = 2.0,
) -> np.ndarray:
    """Sinusoidal + drift + bounded noise — plenty of crossings for signals."""
    rng = np.random.default_rng(seed)
    x = np.arange(n)
    wave = amp * np.sin(2 * np.pi * x / period)
    trend = drift * x
    jitter = rng.normal(0, noise, size=n)
    return base + wave + trend + jitter


def _make_daily_ohlcv(closes: np.ndarray, start: str = "2024-01-01") -> pd.DataFrame:
    """Daily bars — appropriate for CCI/DMI/MACD/Keltner."""
    idx = pd.date_range(start=start, periods=len(closes), freq="D")
    highs = closes + np.abs(np.random.default_rng(1).normal(0, 1.5, len(closes))) + 1.0
    lows = closes - np.abs(np.random.default_rng(2).normal(0, 1.5, len(closes))) - 1.0
    opens = np.roll(closes, 1)
    opens[0] = closes[0]
    return pd.DataFrame(
        {
            "open": opens,
            "high": np.maximum.reduce([opens, closes, highs]),
            "low": np.minimum.reduce([opens, closes, lows]),
            "close": closes,
            "volume": np.full(len(closes), 10_000.0),
        },
        index=idx,
    )


def _make_intraday_ohlcv(
    n_days: int = 6,
    bars_per_day: int = 20,
    seed: int = 11,
) -> pd.DataFrame:
    """Intraday bars with trading hours 09:00..13:00 — for ORB."""
    rng = np.random.default_rng(seed)
    total = n_days * bars_per_day
    base = 1000.0
    prices = [base]
    for _ in range(total - 1):
        prices.append(prices[-1] + rng.normal(0, 3.0))
    prices_arr = np.array(prices)

    # Build index with synthetic intraday timestamps (09:00..13:00, 15-min bars typically).
    timestamps: List[pd.Timestamp] = []
    start = pd.Timestamp("2024-01-01 09:00")
    for day in range(n_days):
        day_start = start + pd.Timedelta(days=day)
        for b in range(bars_per_day):
            timestamps.append(day_start + pd.Timedelta(minutes=15 * b))
    idx = pd.DatetimeIndex(timestamps)

    highs = prices_arr + np.abs(rng.normal(0, 2.0, total)) + 0.5
    lows = prices_arr - np.abs(rng.normal(0, 2.0, total)) - 0.5
    opens = np.roll(prices_arr, 1)
    opens[0] = prices_arr[0]
    return pd.DataFrame(
        {
            "open": opens,
            "high": np.maximum.reduce([opens, prices_arr, highs]),
            "low": np.minimum.reduce([opens, prices_arr, lows]),
            "close": prices_arr,
            "volume": np.full(total, 10_000.0),
        },
        index=idx,
    )


@pytest.fixture
def daily_df() -> pd.DataFrame:
    closes = _sin_trend_series(n=320, seed=7)
    return _make_daily_ohlcv(closes)


@pytest.fixture
def intraday_df() -> pd.DataFrame:
    return _make_intraday_ohlcv(n_days=12, bars_per_day=16, seed=11)


# ---------------------------------------------------------------------------
# Individual strategy smoke tests
# ---------------------------------------------------------------------------


def test_cci_runs_and_trades(daily_df: pd.DataFrame) -> None:
    strat = CCIStrategy(config=CCIConfig(length=14, overbought=80.0, oversold=-80.0))
    strat.set_data(daily_df)
    results = strat.run()
    assert "trades" in results
    assert len(results["equity_curve"]) == len(daily_df) + 1  # +1 initial
    trades = results["trades"]
    assert isinstance(trades, pd.DataFrame)


def test_dmi_runs_and_trades(daily_df: pd.DataFrame) -> None:
    strat = DMIStrategy(config=DMIConfig(length=10, adx_threshold=15.0))
    strat.set_data(daily_df)
    results = strat.run()
    assert len(results["equity_curve"]) == len(daily_df) + 1


def test_macd_runs_and_trades(daily_df: pd.DataFrame) -> None:
    strat = MACDStrategy(config=MACDConfig(fast=8, slow=21, signal=5))
    strat.set_data(daily_df)
    results = strat.run()
    assert len(results["equity_curve"]) == len(daily_df) + 1


def test_keltner_breakout_runs(daily_df: pd.DataFrame) -> None:
    strat = KeltnerStrategy(config=KeltnerConfig(length=14, mult=1.5, mode="breakout"))
    strat.set_data(daily_df)
    results = strat.run()
    assert len(results["equity_curve"]) == len(daily_df) + 1


def test_keltner_mean_reversion_runs(daily_df: pd.DataFrame) -> None:
    strat = KeltnerStrategy(config=KeltnerConfig(length=14, mult=1.5, mode="mean_reversion"))
    strat.set_data(daily_df)
    results = strat.run()
    assert len(results["equity_curve"]) == len(daily_df) + 1


def test_keltner_rejects_bad_mode() -> None:
    with pytest.raises(ValueError):
        KeltnerStrategy(config=KeltnerConfig(mode="invalid"))


def test_orb_runs_and_closes_daily(intraday_df: pd.DataFrame) -> None:
    strat = ORBStrategy(config=ORBConfig(opening_bars=3, session_close_hour=12))
    strat.set_data(intraday_df)
    results = strat.run()
    # Sanity: backtest actually produced results
    assert len(results["equity_curve"]) == len(intraday_df) + 1
    # Over the whole backtest ORB should have generated at least one round trip
    assert len(results["trades"]) >= 1


# ---------------------------------------------------------------------------
# Phase 1 gate: >= 3 strategies each producing >= 5 closed trades
# ---------------------------------------------------------------------------


def test_phase_1_gate_three_strategies_five_trades(
    daily_df: pd.DataFrame, intraday_df: pd.DataFrame
) -> None:
    """Phase 1: >=3 strategies must complete >=5 closed trades."""
    configs: Dict[str, object] = {
        "CCI_tight": CCIStrategy(config=CCIConfig(length=10, overbought=50.0, oversold=-50.0, atr_stop_mult=1.5)),
        "DMI_loose": DMIStrategy(config=DMIConfig(length=10, adx_threshold=10.0, atr_stop_mult=1.5)),
        "MACD_fast": MACDStrategy(config=MACDConfig(fast=5, slow=13, signal=3, atr_stop_mult=2.0)),
        "Keltner_tight": KeltnerStrategy(
            config=KeltnerConfig(length=10, mult=1.0, mode="breakout", atr_stop_mult=1.0)
        ),
    }

    trade_counts: Dict[str, int] = {}
    for name, strat in configs.items():
        strat.set_data(daily_df)
        res = strat.run()
        trade_counts[name] = len(res["trades"])

    # ORB runs on intraday fixture
    orb = ORBStrategy(config=ORBConfig(opening_bars=3, session_close_hour=12, atr_stop_mult=1.5))
    orb.set_data(intraday_df)
    orb_res = orb.run()
    trade_counts["ORB_intraday"] = len(orb_res["trades"])

    qualifying = [name for name, n in trade_counts.items() if n >= 5]
    assert len(qualifying) >= 3, (
        f"Phase 1 gate failed: only {len(qualifying)} strategies hit 5+ trades. "
        f"Counts: {trade_counts}"
    )


# ---------------------------------------------------------------------------
# Indicator sanity checks
# ---------------------------------------------------------------------------


def test_cci_indicator_range_sanity(daily_df: pd.DataFrame) -> None:
    from trading_core.strategy.strategies_extended import _cci

    cci = _cci(daily_df["high"], daily_df["low"], daily_df["close"], length=14)
    # CCI should hit both > 100 and < -100 on a sinusoid fixture
    assert (cci > 100).any()
    assert (cci < -100).any()


def test_dmi_adx_non_negative(daily_df: pd.DataFrame) -> None:
    from trading_core.strategy.strategies_extended import _dmi

    dmi = _dmi(daily_df["high"], daily_df["low"], daily_df["close"], length=14)
    adx = dmi["ADX"].dropna()
    assert (adx >= 0).all()
    assert (adx <= 100).all()
