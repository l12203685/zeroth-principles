"""Performance metrics module.

Merged from:
- AlgoTrading/functions/func_performance.py: get_mdd, get_rf, get_sqn, get_sharpe, get_wr, get_plr_*
- AlgoTrading/algo.py: get_MDD, get_RF, get_SQN
- detail_backtest.py: performance calculation functions
"""

import numpy as np
import pandas as pd
from typing import Union, Tuple
from dataclasses import dataclass


def sharpe_ratio(
    returns: Union[pd.Series, np.ndarray], risk_free_rate: float = 0.0
) -> float:
    """Calculate Sharpe Ratio.

    Sharpe Ratio = (Mean Return - Risk Free Rate) / Std Dev of Returns
    Measures excess return per unit of volatility.

    Args:
        returns: Series or array of returns (should be same frequency)
        risk_free_rate: Annual risk-free rate (default 0.0)

    Returns:
        Sharpe ratio value
    """
    if isinstance(returns, pd.Series):
        returns = returns.fillna(0)
    else:
        returns = np.asarray(returns)
        returns = np.where(np.isnan(returns), 0, returns)

    mean_return = np.mean(returns)
    std_return = np.std(returns)

    if std_return == 0:
        return 0.0

    return (mean_return - risk_free_rate) / std_return


def sortino_ratio(
    returns: Union[pd.Series, np.ndarray], risk_free_rate: float = 0.0
) -> float:
    """Calculate Sortino Ratio.

    Sortino Ratio = (Mean Return - Risk Free Rate) / Downside Deviation
    Similar to Sharpe but only penalizes downside volatility.

    Args:
        returns: Series or array of returns
        risk_free_rate: Annual risk-free rate (default 0.0)

    Returns:
        Sortino ratio value
    """
    if isinstance(returns, pd.Series):
        returns = returns.fillna(0)
    else:
        returns = np.asarray(returns)
        returns = np.where(np.isnan(returns), 0, returns)

    mean_return = np.mean(returns)
    downside = returns[returns < 0]

    if len(downside) == 0:
        downside_std = 0.0
    else:
        downside_std = np.sqrt(np.mean(downside ** 2))

    if downside_std == 0:
        return 0.0

    return (mean_return - risk_free_rate) / downside_std


def drawdown_series(returns: Union[pd.Series, np.ndarray]) -> pd.Series:
    """Calculate drawdown at each point.

    Args:
        returns: Series or array of returns

    Returns:
        Series of drawdown values
    """
    if isinstance(returns, np.ndarray):
        returns = pd.Series(returns)

    cumulative = returns.fillna(0).cumsum()
    running_max = cumulative.expanding().max()
    drawdown = running_max - cumulative

    return drawdown


def max_drawdown(returns: Union[pd.Series, np.ndarray]) -> float:
    """Calculate Maximum Drawdown.

    Maximum Drawdown = (Peak - Trough) / Peak
    Measures the largest peak-to-trough decline.

    Args:
        returns: Series or array of returns

    Returns:
        Maximum drawdown value
    """
    dd = drawdown_series(returns)
    return dd.max()


def calmar_ratio(returns: Union[pd.Series, np.ndarray]) -> float:
    """Calculate Calmar Ratio.

    Calmar Ratio = Annual Return / Max Drawdown
    Measures risk-adjusted return based on drawdown.

    Args:
        returns: Series or array of returns

    Returns:
        Calmar ratio value
    """
    mdd = max_drawdown(returns)
    if mdd == 0:
        return 0.0

    # Annualize return (assuming daily returns)
    ann_ret = annual_return(returns)
    return ann_ret / mdd


def annual_return(returns: Union[pd.Series, np.ndarray]) -> float:
    """Calculate annualized return.

    Args:
        returns: Series or array of returns (assumed daily)

    Returns:
        Annualized return
    """
    if isinstance(returns, pd.Series):
        total_return = (1 + returns).prod() - 1
        n_days = len(returns)
    else:
        returns = np.asarray(returns)
        returns = np.where(np.isnan(returns), 0, returns)
        total_return = np.prod(1 + returns) - 1
        n_days = len(returns)

    if n_days == 0:
        return 0.0

    # Assume 252 trading days per year
    years = n_days / 252
    if years == 0:
        return 0.0

    return (1 + total_return) ** (1 / years) - 1


def win_rate(returns: Union[pd.Series, np.ndarray]) -> float:
    """Calculate Win Rate (percentage of winning periods).

    Win Rate = Number of Positive Returns / Total Non-Zero Returns

    Args:
        returns: Series or array of returns

    Returns:
        Win rate between 0 and 1
    """
    if isinstance(returns, pd.Series):
        returns = returns.fillna(0)
    else:
        returns = np.asarray(returns)
        returns = np.where(np.isnan(returns), 0, returns)

    non_zero = returns != 0
    if non_zero.sum() == 0:
        return 0.0

    wins = (returns > 0).sum()
    return wins / non_zero.sum()


def profit_factor(returns: Union[pd.Series, np.ndarray]) -> float:
    """Calculate Profit Factor.

    Profit Factor = Sum of Gains / Abs(Sum of Losses)
    Ratio of gross profit to gross loss.

    Args:
        returns: Series or array of returns

    Returns:
        Profit factor (typically > 1 for profitable systems)
    """
    if isinstance(returns, pd.Series):
        returns = returns.fillna(0)
    else:
        returns = np.asarray(returns)
        returns = np.where(np.isnan(returns), 0, returns)

    gains = returns[returns > 0].sum()
    losses = abs(returns[returns < 0].sum())

    if losses == 0:
        return float("inf") if gains > 0 else 0.0

    return gains / losses


def recovery_factor(returns: Union[pd.Series, np.ndarray]) -> float:
    """Calculate Recovery Factor.

    Recovery Factor = Total Return / Max Drawdown
    Measures how many times the strategy recovers from drawdown.

    Args:
        returns: Series or array of returns

    Returns:
        Recovery factor
    """
    if isinstance(returns, pd.Series):
        total = returns.fillna(0).sum()
    else:
        returns = np.asarray(returns)
        returns = np.where(np.isnan(returns), 0, returns)
        total = returns.sum()

    mdd = max_drawdown(returns)
    if mdd == 0:
        return 0.0

    return total / mdd


def mar(returns: Union[pd.Series, np.ndarray]) -> float:
    """Calculate MAR (Monthly/Annualized Return) Ratio.

    MAR = Annual Return / Max Drawdown
    (Alias for Calmar Ratio)

    Args:
        returns: Series or array of returns

    Returns:
        MAR value
    """
    return calmar_ratio(returns)


def sqn(returns: Union[pd.Series, np.ndarray]) -> float:
    """Calculate System Quality Number (SQN).

    SQN = Mean Return / Std Dev * sqrt(Number of Trades)
    Measures system quality adjusted for sample size.

    Args:
        returns: Series or array of returns

    Returns:
        SQN value
    """
    if isinstance(returns, pd.Series):
        returns_arr = returns.fillna(0).values
    else:
        returns_arr = np.asarray(returns)
        returns_arr = np.where(np.isnan(returns_arr), 0, returns_arr)

    mean_ret = np.mean(returns_arr)
    std_ret = np.std(returns_arr)

    if std_ret == 0:
        return 0.0

    return (mean_ret / std_ret) * np.sqrt(len(returns_arr))


@dataclass
class PerformanceMetrics:
    """Comprehensive performance metrics collection.

    Merged metrics from all original performance analysis functions.
    """

    sharpe: float
    sortino: float
    max_drawdown: float
    calmar: float
    win_rate: float
    profit_factor: float
    recovery_factor: float
    sqn: float
    annual_return: float
    total_return: float
    num_trades: int

    @classmethod
    def calculate(
        cls, returns: Union[pd.Series, np.ndarray], trade_count: int = None
    ) -> "PerformanceMetrics":
        """Calculate all metrics at once.

        Args:
            returns: Series or array of returns
            trade_count: Number of trades (if known)

        Returns:
            PerformanceMetrics instance
        """
        if isinstance(returns, pd.Series):
            returns_arr = returns.fillna(0)
            if trade_count is None:
                trade_count = (returns != 0).sum()
        else:
            returns_arr = np.asarray(returns)
            returns_arr = np.where(np.isnan(returns_arr), 0, returns_arr)
            if trade_count is None:
                trade_count = (returns_arr != 0).sum()

        return cls(
            sharpe=sharpe_ratio(returns_arr),
            sortino=sortino_ratio(returns_arr),
            max_drawdown=max_drawdown(returns_arr),
            calmar=calmar_ratio(returns_arr),
            win_rate=win_rate(returns_arr),
            profit_factor=profit_factor(returns_arr),
            recovery_factor=recovery_factor(returns_arr),
            sqn=sqn(returns_arr),
            annual_return=annual_return(returns_arr),
            total_return=returns_arr.sum(),
            num_trades=int(trade_count),
        )

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "Sharpe Ratio": self.sharpe,
            "Sortino Ratio": self.sortino,
            "Max Drawdown": self.max_drawdown,
            "Calmar Ratio": self.calmar,
            "Win Rate": self.win_rate,
            "Profit Factor": self.profit_factor,
            "Recovery Factor": self.recovery_factor,
            "SQN": self.sqn,
            "Annual Return": self.annual_return,
            "Total Return": self.total_return,
            "Num Trades": self.num_trades,
        }

    def __str__(self) -> str:
        """String representation."""
        lines = [
            "=" * 50,
            "PERFORMANCE METRICS",
            "=" * 50,
            f"Annual Return:      {self.annual_return:.4f}",
            f"Total Return:       {self.total_return:.2f}",
            f"Sharpe Ratio:       {self.sharpe:.4f}",
            f"Sortino Ratio:      {self.sortino:.4f}",
            f"Max Drawdown:       {self.max_drawdown:.4f}",
            f"Calmar Ratio:       {self.calmar:.4f}",
            f"Win Rate:           {self.win_rate:.2%}",
            f"Profit Factor:      {self.profit_factor:.4f}",
            f"Recovery Factor:    {self.recovery_factor:.4f}",
            f"SQN:                {self.sqn:.4f}",
            f"Number of Trades:   {self.num_trades}",
            "=" * 50,
        ]
        return "\n".join(lines)
