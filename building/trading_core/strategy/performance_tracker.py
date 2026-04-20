"""Live performance tracker — rolling Sharpe, edge ratio, correlation matrix.

Extends :mod:`trading_core.analytics.metrics` with **rolling** and **cross-strategy**
analytics required by Phase 1 pass criteria (plan_system_restructure_v2, line 116).

Core APIs
---------
* :func:`rolling_sharpe` — rolling-window Sharpe ratio series.
* :func:`edge_ratio` — ratio of mean favourable excursion (MFE) over mean
  adverse excursion (MAE) across closed trades.
* :func:`correlation_matrix` — pairwise correlation of strategy return series
  (aligns on the union of timestamps and fills missing with zeros).
* :class:`PerformanceTracker` — stateful registry for *multiple* strategies
  that exposes snapshot dashboards combining the three primitives.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Union

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

ArrayLike = Union[pd.Series, np.ndarray, Sequence[float]]


# ---------------------------------------------------------------------------
# Functional primitives
# ---------------------------------------------------------------------------


def _as_series(returns: ArrayLike, name: str = "ret") -> pd.Series:
    """Coerce to a clean ``pd.Series`` with NaNs replaced by 0."""
    if isinstance(returns, pd.Series):
        s = returns.copy()
    else:
        s = pd.Series(np.asarray(returns, dtype=float), name=name)
    return s.fillna(0.0)


def rolling_sharpe(
    returns: ArrayLike,
    window: int = 60,
    risk_free_rate: float = 0.0,
    annualization_factor: float = 1.0,
    min_periods: Optional[int] = None,
) -> pd.Series:
    """Compute rolling Sharpe ratio.

    Sharpe in a rolling window = (mean(r) - rf) / std(r) * sqrt(annualization_factor)

    Args:
        returns: Per-period return series.
        window: Rolling window length.
        risk_free_rate: Per-period risk-free rate to subtract.
        annualization_factor: e.g. 252 for daily -> annualized; 1 to keep raw.
        min_periods: Minimum observations (default = ``window``).

    Returns:
        ``pd.Series`` (same index as input) of rolling Sharpe values.
        Zero where the rolling std == 0 to avoid infinities.
    """
    if window <= 1:
        raise ValueError("window must be > 1")
    s = _as_series(returns)
    if min_periods is None:
        min_periods = window

    roll = s.rolling(window=window, min_periods=min_periods)
    mean = roll.mean() - risk_free_rate
    std = roll.std(ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = mean / std
    ratio = ratio.replace([np.inf, -np.inf], 0.0).fillna(0.0)
    if annualization_factor and annualization_factor != 1.0:
        ratio = ratio * np.sqrt(float(annualization_factor))
    ratio.name = "rolling_sharpe"
    return ratio


def edge_ratio(trades: pd.DataFrame) -> float:
    """Compute **Edge Ratio** = mean MFE / mean MAE across closed trades.

    A trade is expected to carry ``direction`` and either:

    * ``mfe``/``mae`` columns (absolute favourable / adverse excursions), OR
    * ``entry_price`` + ``high_since_entry`` + ``low_since_entry`` columns.

    For compatibility with :class:`BaseStrategy` trade_history (which stores
    ``entry_price`` / ``exit_price`` / ``direction`` / ``pnl_pct``), this
    function falls back to a **realized** edge ratio using the traded excursion
    between entry and exit:

        * long  : MFE ~ max(0, exit - entry) ; MAE ~ max(0, entry - exit)
        * short : MFE ~ max(0, entry - exit) ; MAE ~ max(0, exit - entry)

    In pure-realized mode, this degenerates to the ``profit_factor`` over
    winning / losing magnitudes — intentional, since intra-trade MFE/MAE are
    not stored by the default portfolio.  Strategies that *do* record MFE/MAE
    (via a richer trade_history schema) will pick up the higher-fidelity path.

    Args:
        trades: Trade-history DataFrame.

    Returns:
        Float edge ratio.  Returns 0.0 on empty input, and ``inf`` if there
        are only favourable trades.
    """
    if trades is None or len(trades) == 0:
        return 0.0

    df = trades.copy()

    if "mfe" in df.columns and "mae" in df.columns:
        mfe = df["mfe"].astype(float).abs()
        mae = df["mae"].astype(float).abs()
    else:
        # Realized-excursion fallback
        if "entry_price" not in df.columns or "exit_price" not in df.columns:
            return 0.0
        entry = df["entry_price"].astype(float)
        exit_ = df["exit_price"].astype(float)
        direction = df.get("direction", pd.Series(["LONG"] * len(df))).astype(str).str.upper()
        long_mask = direction == "LONG"
        mfe = pd.Series(0.0, index=df.index)
        mae = pd.Series(0.0, index=df.index)
        # long
        mfe[long_mask] = (exit_[long_mask] - entry[long_mask]).clip(lower=0.0)
        mae[long_mask] = (entry[long_mask] - exit_[long_mask]).clip(lower=0.0)
        # short
        short_mask = ~long_mask
        mfe[short_mask] = (entry[short_mask] - exit_[short_mask]).clip(lower=0.0)
        mae[short_mask] = (exit_[short_mask] - entry[short_mask]).clip(lower=0.0)

    mean_mfe = float(mfe.mean()) if len(mfe) else 0.0
    mean_mae = float(mae.mean()) if len(mae) else 0.0
    if mean_mae <= 0.0:
        if mean_mfe <= 0.0:
            return 0.0
        return float("inf")
    return mean_mfe / mean_mae


def correlation_matrix(
    returns_by_strategy: Mapping[str, ArrayLike],
    method: str = "pearson",
    min_periods: int = 2,
) -> pd.DataFrame:
    """Pairwise correlation of per-strategy return series.

    Args:
        returns_by_strategy: Mapping ``{name: returns_series}``.
        method: ``"pearson"`` | ``"spearman"`` | ``"kendall"``.
        min_periods: Minimum overlapping non-NaN pairs.

    Returns:
        Square correlation DataFrame with NaN replaced by 0.0 on the diagonal
        (a strategy with zero variance still reports correlation 1 with itself
        and 0 with others for downstream stability).
    """
    if not returns_by_strategy:
        return pd.DataFrame()

    # Align all series on union of indices, fill missing with 0.
    normalized: Dict[str, pd.Series] = {}
    for name, arr in returns_by_strategy.items():
        s = _as_series(arr, name=name)
        normalized[name] = s

    # Build a DataFrame.  If an input has no DatetimeIndex, reset to RangeIndex.
    try:
        frame = pd.concat(normalized.values(), axis=1, keys=normalized.keys()).fillna(0.0)
    except Exception:  # noqa: BLE001
        frame = pd.DataFrame(
            {k: pd.Series(v.values if isinstance(v, pd.Series) else v) for k, v in normalized.items()}
        ).fillna(0.0)

    corr = frame.corr(method=method, min_periods=min_periods)
    # Replace NaN from zero-variance columns: diag = 1, off-diag = 0.
    if corr.isna().any().any():
        corr = corr.fillna(0.0)
        for col in corr.columns:
            corr.loc[col, col] = 1.0
    return corr


# ---------------------------------------------------------------------------
# Stateful registry
# ---------------------------------------------------------------------------


@dataclass
class StrategyPerf:
    """Per-strategy performance record."""

    name: str
    returns: pd.Series = field(default_factory=lambda: pd.Series(dtype=float))
    trades: pd.DataFrame = field(default_factory=pd.DataFrame)


@dataclass
class PerformanceTracker:
    """Registry for multiple strategies.

    Usage::

        tracker = PerformanceTracker()
        tracker.register("cci_20", returns=res["returns"], trades=res["trades"])
        tracker.register("macd_12_26_9", returns=..., trades=...)
        snap = tracker.snapshot(rolling_window=60)
        # snap["rolling_sharpe"]    -> DataFrame[index=time, cols=strategies]
        # snap["edge_ratio"]        -> Series[strategy] -> float
        # snap["correlation"]       -> DataFrame (corr matrix)
        # snap["summary"]           -> DataFrame[strategy -> {sharpe, edge, trades, ...}]
    """

    strategies: Dict[str, StrategyPerf] = field(default_factory=dict)

    # ---- mutation
    def register(
        self,
        name: str,
        returns: ArrayLike,
        trades: Optional[pd.DataFrame] = None,
    ) -> None:
        """Register or overwrite a strategy's returns + trades."""
        self.strategies[name] = StrategyPerf(
            name=name,
            returns=_as_series(returns, name=name),
            trades=trades.copy() if trades is not None else pd.DataFrame(),
        )

    def unregister(self, name: str) -> None:
        self.strategies.pop(name, None)

    # ---- views
    def names(self) -> List[str]:
        return sorted(self.strategies.keys())

    def returns_frame(self) -> pd.DataFrame:
        """Wide DataFrame (index=time, columns=strategies)."""
        if not self.strategies:
            return pd.DataFrame()
        return pd.concat(
            {n: s.returns for n, s in self.strategies.items()},
            axis=1,
        ).fillna(0.0)

    # ---- analytics
    def rolling_sharpe(
        self,
        window: int = 60,
        risk_free_rate: float = 0.0,
        annualization_factor: float = 1.0,
    ) -> pd.DataFrame:
        frame = self.returns_frame()
        if frame.empty:
            return frame
        return pd.DataFrame(
            {
                col: rolling_sharpe(
                    frame[col],
                    window=window,
                    risk_free_rate=risk_free_rate,
                    annualization_factor=annualization_factor,
                )
                for col in frame.columns
            },
            index=frame.index,
        )

    def edge_ratios(self) -> pd.Series:
        return pd.Series(
            {n: edge_ratio(s.trades) for n, s in self.strategies.items()},
            name="edge_ratio",
            dtype=float,
        )

    def correlation_matrix(self, method: str = "pearson") -> pd.DataFrame:
        return correlation_matrix({n: s.returns for n, s in self.strategies.items()}, method=method)

    def summary(self, rolling_window: int = 60) -> pd.DataFrame:
        """Per-strategy snapshot: trades, latest rolling Sharpe, edge ratio."""
        if not self.strategies:
            return pd.DataFrame()
        rs = self.rolling_sharpe(window=rolling_window)
        er = self.edge_ratios()
        rows: List[Dict[str, float]] = []
        for n, s in self.strategies.items():
            latest_sharpe = float(rs[n].iloc[-1]) if (n in rs.columns and len(rs)) else 0.0
            mean_sharpe = float(rs[n].mean()) if (n in rs.columns and len(rs)) else 0.0
            rows.append(
                {
                    "strategy": n,
                    "n_bars": int(len(s.returns)),
                    "n_trades": int(len(s.trades)),
                    "total_return": float(s.returns.sum()),
                    "mean_rolling_sharpe": mean_sharpe,
                    "latest_rolling_sharpe": latest_sharpe,
                    "edge_ratio": float(er.get(n, 0.0)),
                }
            )
        return pd.DataFrame(rows).set_index("strategy")

    def snapshot(
        self,
        rolling_window: int = 60,
        annualization_factor: float = 1.0,
    ) -> Dict[str, object]:
        """Compose the three primitives into a single dashboard payload."""
        return {
            "rolling_sharpe": self.rolling_sharpe(
                window=rolling_window, annualization_factor=annualization_factor
            ),
            "edge_ratio": self.edge_ratios(),
            "correlation": self.correlation_matrix(),
            "summary": self.summary(rolling_window=rolling_window),
        }


__all__ = [
    "rolling_sharpe",
    "edge_ratio",
    "correlation_matrix",
    "StrategyPerf",
    "PerformanceTracker",
]
