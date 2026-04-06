"""Base strategy class for all trading strategies."""

import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import logging

from trading_core.data import Portfolio
from trading_core.analytics import PerformanceMetrics

logger = logging.getLogger(__name__)


class BaseStrategy(ABC):
    """Abstract base class for trading strategies.

    All strategies should inherit from this class and implement:
    - on_bar(): Called on each new bar
    - on_tick(): Called on each tick (optional)
    """

    def __init__(
        self,
        name: str,
        initial_capital: float = 100000.0,
        contract: str = "TXF",
    ):
        """Initialize strategy.

        Args:
            name: Strategy name
            initial_capital: Starting capital
            contract: Contract to trade
        """
        self.name = name
        self.initial_capital = initial_capital
        self.contract = contract

        # Portfolio and tracking
        self.portfolio = Portfolio(initial_capital)
        self.ohlcv: Optional[pd.DataFrame] = None
        self.current_bar_idx: int = 0
        self.current_bar: Optional[pd.Series] = None

        # Performance tracking
        self.returns: List[float] = []
        self.equity_curve: List[float] = [initial_capital]

        logger.info(f"Initialized {self.name} with capital: {initial_capital}")

    def set_data(self, ohlcv: pd.DataFrame) -> None:
        """Set OHLCV data for backtesting.

        Args:
            ohlcv: DataFrame with datetime index and columns [open, high, low, close, volume]
        """
        if not all(c in ohlcv.columns for c in ["open", "high", "low", "close", "volume"]):
            raise ValueError("OHLCV data missing required columns")

        self.ohlcv = ohlcv.sort_index()
        logger.info(f"Data set: {len(self.ohlcv)} bars from {self.ohlcv.index[0]} to {self.ohlcv.index[-1]}")

    def run(self) -> Dict:
        """Run backtest on loaded data.

        Returns:
            Results dictionary with metrics and performance
        """
        if self.ohlcv is None:
            raise ValueError("No data set. Call set_data() first.")

        logger.info(f"Running {self.name}...")

        for idx in range(len(self.ohlcv)):
            self.current_bar_idx = idx
            self.current_bar = self.ohlcv.iloc[idx]

            # Calculate equity
            self.portfolio.update_prices({self.contract: self.current_bar["close"]})
            current_equity = self.portfolio.total_value
            self.equity_curve.append(current_equity)

            # Calculate return for this bar
            if len(self.equity_curve) > 1:
                bar_return = (current_equity - self.equity_curve[-2]) / self.equity_curve[-2]
                self.returns.append(bar_return)

            # Call strategy logic
            try:
                self.on_bar()
            except Exception as e:
                logger.error(f"Error in on_bar at bar {idx}: {e}")
                raise

        logger.info(f"Backtest complete. Total bars: {len(self.ohlcv)}")

        return self.get_results()

    def get_results(self) -> Dict:
        """Get backtest results and metrics.

        Returns:
            Dictionary with results
        """
        returns_series = pd.Series(self.returns)
        metrics = PerformanceMetrics.calculate(returns_series, len(self.portfolio.trade_history))

        return {
            "strategy_name": self.name,
            "initial_capital": self.initial_capital,
            "final_value": self.equity_curve[-1] if self.equity_curve else self.initial_capital,
            "total_return": (self.equity_curve[-1] / self.initial_capital - 1) if self.equity_curve else 0,
            "equity_curve": pd.Series(self.equity_curve, name="Equity"),
            "returns": returns_series,
            "trades": pd.DataFrame(self.portfolio.trade_history) if self.portfolio.trade_history else pd.DataFrame(),
            "metrics": metrics,
            "portfolio_summary": self.portfolio.summary(),
        }

    @abstractmethod
    def on_bar(self) -> None:
        """Called on each new bar. Implement trading logic here.

        Access current bar via:
        - self.current_bar: Current OHLCV
        - self.current_bar_idx: Bar index
        - self.portfolio: Current portfolio state

        Methods to trade:
        - self.buy()
        - self.sell()
        - self.close_position()
        """
        pass

    def on_tick(self, tick: Dict) -> None:
        """Called on each tick (optional override).

        Args:
            tick: Tick data dictionary
        """
        pass

    def buy(
        self,
        size: float = 1.0,
        entry_price: Optional[float] = None,
    ) -> None:
        """Buy (go long).

        Args:
            size: Number of contracts
            entry_price: Entry price (default: current close)
        """
        if entry_price is None:
            entry_price = self.current_bar["close"]

        self.portfolio.add_position(
            symbol=self.contract,
            direction="long",
            size=size,
            entry_price=entry_price,
            entry_time=self.current_bar.name,  # datetime from index
            cash_impact=size * entry_price,
        )

        logger.debug(f"BUY {size} at {entry_price}")

    def sell(
        self,
        size: float = 1.0,
        entry_price: Optional[float] = None,
    ) -> None:
        """Sell (go short).

        Args:
            size: Number of contracts
            entry_price: Entry price (default: current close)
        """
        if entry_price is None:
            entry_price = self.current_bar["close"]

        self.portfolio.add_position(
            symbol=self.contract,
            direction="short",
            size=size,
            entry_price=entry_price,
            entry_time=self.current_bar.name,
            cash_impact=size * entry_price,
        )

        logger.debug(f"SELL {size} at {entry_price}")

    def close_position(
        self,
        exit_price: Optional[float] = None,
    ) -> None:
        """Close current position.

        Args:
            exit_price: Exit price (default: current close)
        """
        if exit_price is None:
            exit_price = self.current_bar["close"]

        trade = self.portfolio.close_position(
            symbol=self.contract,
            exit_price=exit_price,
            exit_time=self.current_bar.name,
        )

        if trade:
            logger.debug(f"CLOSE at {exit_price}, PnL: {trade['pnl']}")

    def has_position(self) -> bool:
        """Check if there is an open position.

        Returns:
            True if position is open
        """
        return self.contract in self.portfolio.positions

    def get_position_size(self) -> float:
        """Get current position size.

        Returns:
            Current position size (positive for long, negative for short)
        """
        pos = self.portfolio.get_position(self.contract)
        if pos is None:
            return 0.0
        return pos.size * pos.direction.value

    def add_indicator(self, name: str, values: pd.Series) -> None:
        """Add custom indicator to OHLCV.

        Args:
            name: Indicator name
            values: Indicator values (Series with same index as OHLCV)
        """
        if self.ohlcv is None:
            raise ValueError("No data set")
        self.ohlcv[name] = values
