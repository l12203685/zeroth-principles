"""MAE/MFE (Maximum Adverse/Favorable Excursion) module.

Merged from:
- PYMAFE/pymafe/mafe.py: MAFE class
- PYMAFE/pymae/mafe.py: mafe class
- AlgoTrading/algo.py: MAE/MFE calculation logic
"""

import pandas as pd
import numpy as np
from typing import Union, Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Trade:
    """Single trade record.

    Attributes:
        entry_time: Entry timestamp
        exit_time: Exit timestamp
        entry_price: Entry price
        exit_price: Exit price
        direction: 'long' or 'short'
        size: Position size (contracts)
    """

    entry_time: pd.Timestamp
    exit_time: pd.Timestamp
    entry_price: float
    exit_price: float
    direction: str
    size: float = 1.0
    high_price: float = 0.0   # Highest price during trade (for MFE long)
    low_price: float = 0.0    # Lowest price during trade (for MAE long)

    @property
    def pnl(self) -> float:
        """Calculate P&L for this trade."""
        if self.direction.lower() == "long":
            return (self.exit_price - self.entry_price) * self.size
        else:  # short
            return (self.entry_price - self.exit_price) * self.size


class MAFE:
    """Maximum Adverse/Favorable Excursion analysis.

    Merged implementation from PYMAFE and AlgoTrading repos.
    Calculates MAE (worst price against position) and MFE (best price for position)
    for each trade.

    Primary interface: pass a list of Trade objects (each carries entry/exit price
    and the intra-trade high/low).  For legacy OHLC-based usage, use the
    ``from_ohlc()`` classmethod instead.
    """

    def __init__(self, trades: List[Trade]):
        """Initialize MAFE calculator from a list of Trade objects.

        Args:
            trades: List of Trade dataclass instances.  Each trade must have
                    ``high_price`` and ``low_price`` set to the intra-trade
                    extreme prices (used for MFE/MAE respectively).

        Raises:
            ValueError: If trades list is empty.
        """
        if not trades:
            raise ValueError("trades list cannot be empty")
        self.trades = trades
        # Keep a per-direction view for convenience
        self._ohlc: Optional[pd.DataFrame] = None   # only set via from_ohlc()

    # ------------------------------------------------------------------
    # Classmethod constructors
    # ------------------------------------------------------------------

    @classmethod
    def from_ohlc(
        cls,
        ohlc: pd.DataFrame,
        entry_times: Union[pd.Series, pd.Index],
        exit_times: Union[pd.Series, pd.Index],
        direction: str = "long",
        entry_prices: Optional[pd.Series] = None,
        exit_prices: Optional[pd.Series] = None,
    ) -> "MAFE":
        """Build a MAFE analyser from raw OHLC data (legacy / PYMAFE-style API).

        Args:
            ohlc: OHLC DataFrame with datetime index and columns open/high/low/close
            entry_times: Series or Index of entry timestamps
            exit_times: Series or Index of exit timestamps
            direction: 'long' or 'short'
            entry_prices: Override entry prices (defaults to ohlc['open'] at entry_times)
            exit_prices: Override exit prices (defaults to ohlc['open'] at exit_times)

        Returns:
            MAFE instance populated with synthesised Trade objects.
        """
        if direction.lower() not in ["long", "short"]:
            raise ValueError("direction must be 'long' or 'short'")

        required_cols = {"open", "high", "low", "close"}
        if not required_cols.issubset(set(ohlc.columns)):
            raise ValueError(f"OHLC must contain columns: {required_cols}")

        if isinstance(entry_times, pd.Index):
            entry_times = pd.Series(entry_times)
        if isinstance(exit_times, pd.Index):
            exit_times = pd.Series(exit_times)

        if len(entry_times) != len(exit_times):
            raise ValueError("entry_times and exit_times must have the same length")

        ep = (
            ohlc.loc[entry_times, "open"].values
            if entry_prices is None
            else entry_prices.values
        )
        xp = (
            ohlc.loc[exit_times, "open"].values
            if exit_prices is None
            else exit_prices.values
        )

        trades: List[Trade] = []
        for i, (et, xt) in enumerate(zip(entry_times, exit_times)):
            mask = (ohlc.index >= et) & (ohlc.index <= xt)
            period = ohlc.loc[mask]
            high = float(period["high"].max()) if len(period) else float(ep[i])
            low = float(period["low"].min()) if len(period) else float(ep[i])
            trades.append(
                Trade(
                    entry_time=pd.Timestamp(et),
                    exit_time=pd.Timestamp(xt),
                    entry_price=float(ep[i]),
                    exit_price=float(xp[i]),
                    direction=direction,
                    high_price=high,
                    low_price=low,
                )
            )

        instance = cls(trades)
        instance._ohlc = ohlc
        return instance

    # ------------------------------------------------------------------
    # Core calculations
    # ------------------------------------------------------------------

    def pnl(self) -> pd.Series:
        """P&L series for each trade."""
        return pd.Series([t.pnl for t in self.trades], name="PnL")

    def mae(self) -> pd.Series:
        """Maximum Adverse Excursion series.

        - Long:  entry_price − intra-trade low  (how far it went against you)
        - Short: intra-trade high − entry_price
        """
        values = []
        for t in self.trades:
            if t.direction.lower() == "long":
                values.append(max(t.entry_price - t.low_price, 0.0))
            else:
                values.append(max(t.high_price - t.entry_price, 0.0))
        return pd.Series(values, name="MAE")

    def mfe(self) -> pd.Series:
        """Maximum Favorable Excursion series.

        - Long:  intra-trade high − entry_price  (how far it went in your favour)
        - Short: entry_price − intra-trade low
        """
        values = []
        for t in self.trades:
            if t.direction.lower() == "long":
                values.append(max(t.high_price - t.entry_price, 0.0))
            else:
                values.append(max(t.entry_price - t.low_price, 0.0))
        return pd.Series(values, name="MFE")

    def mafe_ratio(self) -> pd.Series:
        """MAE / MFE ratio.  Low value → good risk/reward."""
        mae_s = self.mae()
        mfe_s = self.mfe()
        ratio = mae_s / mfe_s.replace(0, np.nan)
        return ratio.fillna(0.0).rename("MAFE_ratio")

    def calculate(self) -> pd.DataFrame:
        """Alias for summary() — returns full per-trade DataFrame."""
        return self.summary()

    def summary(self) -> pd.DataFrame:
        """Full per-trade summary DataFrame.

        Returns:
            DataFrame with columns: entry_time, exit_time, direction,
            entry_price, exit_price, pnl, mae, mfe, mafe_ratio
        """
        df = pd.DataFrame({
            "entry_time": [t.entry_time for t in self.trades],
            "exit_time":  [t.exit_time  for t in self.trades],
            "direction":  [t.direction  for t in self.trades],
            "entry_price":[t.entry_price for t in self.trades],
            "exit_price": [t.exit_price  for t in self.trades],
            "pnl":        self.pnl().values,
            "mae":        self.mae().values,
            "mfe":        self.mfe().values,
        })
        df["mafe_ratio"] = df["mae"] / df["mfe"].replace(0, np.nan)
        df["mafe_ratio"] = df["mafe_ratio"].fillna(0.0)
        return df

    def scatter_plot(
        self, ax=None, figsize: Tuple[int, int] = (12, 8), **kwargs
    ) -> "matplotlib.axes.Axes":
        """Scatter plot of MAE vs MFE with the equal-excursion diagonal."""
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            raise ImportError(
                "matplotlib required for plotting. "
                "Install with: pip install matplotlib"
            )

        mae_vals = self.mae()
        mfe_vals = self.mfe()

        if ax is None:
            _, ax = plt.subplots(figsize=figsize)

        ax.scatter(mae_vals, mfe_vals, alpha=0.6, s=50, **kwargs)
        max_val = max(mae_vals.max(), mfe_vals.max(), 1e-9)
        ax.plot([0, max_val], [0, max_val], "r--", alpha=0.3, label="MAE=MFE")
        ax.set_xlabel("Maximum Adverse Excursion (MAE)")
        ax.set_ylabel("Maximum Favorable Excursion (MFE)")
        directions = set(t.direction for t in self.trades)
        ax.set_title(f"MAE vs MFE ({'/'.join(directions).upper()} trades)")
        ax.legend()
        ax.grid(True, alpha=0.3)
        return ax


def calculate_mae_mfe(
    trades: pd.DataFrame,
    ohlc: pd.DataFrame,
    price_column: str = "open",
) -> Dict[str, Union[pd.Series, float]]:
    """Convenience function to calculate MAE/MFE from trades DataFrame.

    Merged helper function from AlgoTrading scripts.

    Args:
        trades: DataFrame with columns: entry_time, exit_time, entry_price, exit_price, direction, size
        ohlc: OHLC price data
        price_column: Which OHLC column to use for entry/exit ('open', 'close', etc.)

    Returns:
        Dict with keys: 'mae', 'mfe', 'mafe_ratio', 'summary'
    """
    if len(trades) == 0:
        raise ValueError("trades DataFrame is empty")

    # Separate by direction
    results = {}

    for direction in ["long", "short"]:
        direction_trades = trades[trades["direction"] == direction]

        if len(direction_trades) == 0:
            continue

        mafe = MAFE(
            ohlc=ohlc,
            entry_times=direction_trades["entry_time"].values,
            exit_times=direction_trades["exit_time"].values,
            direction=direction,
        )

        results[direction] = {
            "mae": mafe.mae(),
            "mfe": mafe.mfe(),
            "mafe_ratio": mafe.mafe_ratio(),
            "summary": mafe.summary(),
        }

    # Combine results
    all_mae = []
    all_mfe = []
    all_summary = []

    for direction, metrics in results.items():
        all_mae.append(metrics["mae"])
        all_mfe.append(metrics["mfe"])
        all_summary.append(metrics["summary"])

    return {
        "mae": pd.concat(all_mae, ignore_index=True) if all_mae else pd.Series(),
        "mfe": pd.concat(all_mfe, ignore_index=True) if all_mfe else pd.Series(),
        "mafe_ratio": pd.concat(
            [m["mafe_ratio"] for m in results.values()], ignore_index=True
        )
        if results
        else pd.Series(),
        "summary": pd.concat(all_summary, ignore_index=True) if all_summary else pd.DataFrame(),
    }
