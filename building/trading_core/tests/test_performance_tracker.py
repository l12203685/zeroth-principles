"""Unit tests for performance_tracker: rolling Sharpe, edge ratio, correlation."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from trading_core.strategy.performance_tracker import (
    PerformanceTracker,
    correlation_matrix,
    edge_ratio,
    rolling_sharpe,
)


# ---------------------------------------------------------------------------
# rolling_sharpe
# ---------------------------------------------------------------------------


def test_rolling_sharpe_output_length_matches_input() -> None:
    rng = np.random.default_rng(0)
    r = pd.Series(rng.normal(0.001, 0.02, 300))
    rs = rolling_sharpe(r, window=30)
    assert len(rs) == len(r)
    # First window-1 entries should be NaN -> replaced with 0
    assert rs.iloc[:29].eq(0.0).all()


def test_rolling_sharpe_constant_returns_yields_zero() -> None:
    r = pd.Series([0.01] * 100)
    rs = rolling_sharpe(r, window=30)
    # constant series has std=0 → ratio defined as 0
    assert rs.iloc[30:].eq(0.0).all()


def test_rolling_sharpe_window_gt_1_enforced() -> None:
    with pytest.raises(ValueError):
        rolling_sharpe(pd.Series([0.0, 0.1]), window=1)


def test_rolling_sharpe_annualization() -> None:
    rng = np.random.default_rng(1)
    r = pd.Series(rng.normal(0.001, 0.01, 200))
    rs_raw = rolling_sharpe(r, window=30, annualization_factor=1.0)
    rs_252 = rolling_sharpe(r, window=30, annualization_factor=252.0)
    non_zero = rs_raw != 0
    assert np.allclose(rs_252[non_zero], rs_raw[non_zero] * np.sqrt(252.0))


# ---------------------------------------------------------------------------
# edge_ratio
# ---------------------------------------------------------------------------


def test_edge_ratio_empty_trades_returns_zero() -> None:
    assert edge_ratio(pd.DataFrame()) == 0.0


def test_edge_ratio_realized_excursion_longs() -> None:
    trades = pd.DataFrame(
        [
            {"direction": "LONG", "entry_price": 100.0, "exit_price": 110.0},  # mfe=10, mae=0
            {"direction": "LONG", "entry_price": 100.0, "exit_price": 95.0},   # mfe=0,  mae=5
            {"direction": "LONG", "entry_price": 100.0, "exit_price": 105.0},  # mfe=5,  mae=0
        ]
    )
    # mean mfe = (10+0+5)/3 = 5, mean mae = (0+5+0)/3 = 1.667 → ratio = 3.0
    er = edge_ratio(trades)
    assert er == pytest.approx(3.0, rel=1e-3)


def test_edge_ratio_mixed_long_short() -> None:
    trades = pd.DataFrame(
        [
            {"direction": "LONG", "entry_price": 100.0, "exit_price": 110.0},
            {"direction": "SHORT", "entry_price": 110.0, "exit_price": 100.0},
            {"direction": "SHORT", "entry_price": 100.0, "exit_price": 110.0},  # mae for short
        ]
    )
    # LONG  : mfe 10 mae 0
    # SHORT : mfe 10 mae 0
    # SHORT : mfe 0  mae 10
    # mean mfe = 20/3, mean mae = 10/3, ratio = 2.0
    er = edge_ratio(trades)
    assert er == pytest.approx(2.0, rel=1e-3)


def test_edge_ratio_infinite_when_all_winners() -> None:
    trades = pd.DataFrame(
        [
            {"direction": "LONG", "entry_price": 100.0, "exit_price": 110.0},
            {"direction": "LONG", "entry_price": 100.0, "exit_price": 105.0},
        ]
    )
    assert edge_ratio(trades) == float("inf")


def test_edge_ratio_mfe_mae_columns_preferred() -> None:
    trades = pd.DataFrame([{"mfe": 20.0, "mae": 5.0}, {"mfe": 10.0, "mae": 5.0}])
    assert edge_ratio(trades) == pytest.approx((20 + 10) / 2 / ((5 + 5) / 2), rel=1e-6)


# ---------------------------------------------------------------------------
# correlation_matrix
# ---------------------------------------------------------------------------


def test_correlation_identical_series_is_one() -> None:
    rng = np.random.default_rng(2)
    s1 = pd.Series(rng.normal(0, 1, 100))
    s2 = s1.copy()
    corr = correlation_matrix({"a": s1, "b": s2})
    assert corr.loc["a", "b"] == pytest.approx(1.0)
    assert corr.loc["a", "a"] == pytest.approx(1.0)


def test_correlation_anti_correlated_series_is_negative_one() -> None:
    rng = np.random.default_rng(3)
    s1 = pd.Series(rng.normal(0, 1, 100))
    s2 = -s1
    corr = correlation_matrix({"pos": s1, "neg": s2})
    assert corr.loc["pos", "neg"] == pytest.approx(-1.0)


def test_correlation_empty_mapping_returns_empty_frame() -> None:
    corr = correlation_matrix({})
    assert corr.empty


def test_correlation_zero_variance_column_handled() -> None:
    s1 = pd.Series([0.01] * 50)  # zero variance
    rng = np.random.default_rng(4)
    s2 = pd.Series(rng.normal(0, 1, 50))
    corr = correlation_matrix({"flat": s1, "rand": s2})
    assert not corr.isna().any().any()
    assert corr.loc["flat", "flat"] == 1.0
    assert corr.loc["flat", "rand"] == 0.0


# ---------------------------------------------------------------------------
# PerformanceTracker stateful registry
# ---------------------------------------------------------------------------


def test_tracker_register_and_unregister() -> None:
    tracker = PerformanceTracker()
    r = pd.Series(np.arange(50) * 0.001)
    tracker.register("s1", r)
    assert tracker.names() == ["s1"]
    tracker.unregister("s1")
    assert tracker.names() == []


def test_tracker_snapshot_shape() -> None:
    rng = np.random.default_rng(5)
    tracker = PerformanceTracker()
    tracker.register("a", rng.normal(0.001, 0.01, 200))
    tracker.register("b", rng.normal(-0.001, 0.015, 200))
    snap = tracker.snapshot(rolling_window=30)

    assert set(snap.keys()) == {"rolling_sharpe", "edge_ratio", "correlation", "summary"}

    rs = snap["rolling_sharpe"]
    assert isinstance(rs, pd.DataFrame)
    assert list(rs.columns) == ["a", "b"]

    corr = snap["correlation"]
    assert corr.shape == (2, 2)

    summary = snap["summary"]
    assert set(summary.index) == {"a", "b"}
    assert "n_trades" in summary.columns
    assert "edge_ratio" in summary.columns


def test_tracker_with_trades() -> None:
    tracker = PerformanceTracker()
    tracker.register(
        "cci",
        returns=pd.Series(np.zeros(30)),
        trades=pd.DataFrame(
            [
                {"direction": "LONG", "entry_price": 100.0, "exit_price": 110.0},
                {"direction": "LONG", "entry_price": 100.0, "exit_price": 95.0},
            ]
        ),
    )
    er = tracker.edge_ratios()
    assert "cci" in er.index
    # mfe mean = 5, mae mean = 2.5, ratio = 2.0
    assert er["cci"] == pytest.approx(2.0, rel=1e-3)


def test_tracker_empty_returns_frame() -> None:
    tracker = PerformanceTracker()
    assert tracker.returns_frame().empty
    assert tracker.summary().empty
