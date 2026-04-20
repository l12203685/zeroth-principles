"""Unit tests for PLA pattern catalog + StrategyGenerator."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from trading_core.strategy import BaseStrategy
from trading_core.strategy.pla_catalog import (
    PLA_CATALOG,
    PLAPattern,
    StrategyGenerator,
)


def test_catalog_non_empty_and_five_patterns() -> None:
    assert len(PLA_CATALOG) == 5
    names = {p.name for p in PLA_CATALOG}
    assert {"cci_reversion", "dmi_trend", "macd_trend", "orb_intraday", "keltner_channel"} <= names


def test_pattern_param_space_size_correct() -> None:
    gen = StrategyGenerator()
    for pat in PLA_CATALOG:
        combos = list(pat.iter_params())
        assert len(combos) == pat.space_size()
        assert pat.space_size() >= 1


def test_families_and_filter() -> None:
    gen = StrategyGenerator()
    fams = set(gen.families())
    assert {"trend", "mean_reversion", "breakout"} <= fams
    trend_pats = gen.filter(family="trend")
    assert {p.name for p in trend_pats} == {"dmi_trend", "macd_trend"}
    atr_pats = gen.filter(indicator="ATR")
    # all five patterns reference ATR
    assert len(atr_pats) == 5


def test_by_name_raises_on_missing() -> None:
    gen = StrategyGenerator()
    with pytest.raises(KeyError):
        gen.by_name("does_not_exist")


def test_expand_all_yields_base_strategy_instances() -> None:
    gen = StrategyGenerator()
    strats = gen.expand_all(sample_per_pattern=2)
    assert strats
    for s in strats:
        assert isinstance(s, BaseStrategy)
        assert s.name  # non-empty


def test_expand_single_with_sample_respected() -> None:
    gen = StrategyGenerator()
    # cci_reversion has 3*3*3*3=81 combos, cap at 4
    strats = gen.expand("cci_reversion", sample=4)
    assert 1 <= len(strats) <= 4


def test_generated_strategy_runs_on_synthetic_data() -> None:
    rng = np.random.default_rng(3)
    closes = 1000 + np.cumsum(rng.normal(0, 2, 260))
    idx = pd.date_range("2024-01-01", periods=260, freq="D")
    df = pd.DataFrame(
        {
            "open": closes,
            "high": closes + np.abs(rng.normal(0, 1.5, 260)) + 1,
            "low": closes - np.abs(rng.normal(0, 1.5, 260)) - 1,
            "close": closes,
            "volume": np.full(260, 10_000.0),
        },
        index=idx,
    )

    gen = StrategyGenerator()
    for pattern_name in ("cci_reversion", "dmi_trend", "macd_trend", "keltner_channel"):
        strats = gen.expand(pattern_name, sample=1)
        assert strats
        s = strats[0]
        s.set_data(df)
        res = s.run()
        assert "trades" in res
        assert "metrics" in res


def test_summary_returns_expected_shape() -> None:
    gen = StrategyGenerator()
    summary = gen.summary()
    assert len(summary) == 5
    for row in summary:
        assert set(row.keys()) >= {
            "name",
            "family",
            "indicators",
            "param_space_size",
            "pla_file_count",
            "description",
        }
        assert row["param_space_size"] >= 1
        assert row["pla_file_count"] >= 0


def test_catalog_is_frozen_dataclass() -> None:
    p = PLA_CATALOG[0]
    assert isinstance(p, PLAPattern)
    with pytest.raises(Exception):
        # frozen dataclass — assignment should raise
        p.name = "mutated"  # type: ignore[misc]
