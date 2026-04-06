"""Position and portfolio management module.

Tracks open positions and portfolio state.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class PositionType(Enum):
    """Position direction type."""

    LONG = 1
    SHORT = -1
    FLAT = 0


@dataclass
class Position:
    """Single position record.

    Attributes:
        symbol: Contract symbol
        direction: PositionType (LONG, SHORT, or FLAT)
        size: Number of contracts
        entry_price: Average entry price
        entry_time: Entry timestamp
        current_price: Current market price
        current_value: Current position value (size * current_price)
    """

    symbol: str
    direction: PositionType
    size: float
    entry_price: float
    entry_time: datetime
    current_price: float = 0.0
    pnl: float = field(default=0.0, init=False)
    pnl_pct: float = field(default=0.0, init=False)

    def __post_init__(self):
        """Calculate P&L fields."""
        self._update_pnl()

    def _update_pnl(self):
        """Update P&L calculations."""
        if self.direction == PositionType.LONG:
            self.pnl = (self.current_price - self.entry_price) * self.size
            if self.entry_price != 0:
                self.pnl_pct = (self.current_price - self.entry_price) / self.entry_price
        elif self.direction == PositionType.SHORT:
            self.pnl = (self.entry_price - self.current_price) * self.size
            if self.entry_price != 0:
                self.pnl_pct = (self.entry_price - self.current_price) / self.entry_price
        else:
            self.pnl = 0.0
            self.pnl_pct = 0.0

    @property
    def is_open(self) -> bool:
        """Check if position is open."""
        return self.direction != PositionType.FLAT and self.size > 0

    def update_price(self, new_price: float) -> None:
        """Update current market price and recalculate P&L.

        Args:
            new_price: New market price
        """
        self.current_price = new_price
        self._update_pnl()

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "symbol": self.symbol,
            "direction": self.direction.name,
            "size": self.size,
            "entry_price": self.entry_price,
            "entry_time": self.entry_time,
            "current_price": self.current_price,
            "pnl": self.pnl,
            "pnl_pct": self.pnl_pct,
        }


class Portfolio:
    """Portfolio tracking multiple positions.

    Tracks all open positions, calculates portfolio-level metrics.

    Attributes:
        positions: Dict[symbol, Position] of open positions
        cash: Available cash
        initial_cash: Starting cash amount
    """

    def __init__(self, initial_cash: float = 0.0):
        """Initialize portfolio.

        Args:
            initial_cash: Starting cash amount
        """
        self.positions: Dict[str, Position] = {}
        self.cash = initial_cash
        self.initial_cash = initial_cash
        self.trade_history: List[Dict] = []

    def add_position(
        self,
        symbol: str,
        direction: str,
        size: float,
        entry_price: float,
        entry_time: datetime = None,
        cash_impact: float = None,
    ) -> None:
        """Add or update a position.

        Args:
            symbol: Contract symbol
            direction: 'long' or 'short'
            size: Position size
            entry_price: Entry price
            entry_time: Entry time (default: now)
            cash_impact: Impact on cash (default: size * entry_price)
        """
        if entry_time is None:
            entry_time = datetime.now()

        if cash_impact is None:
            cash_impact = size * entry_price

        pos_dir = PositionType.LONG if direction.lower() == "long" else PositionType.SHORT

        if symbol in self.positions:
            # Update existing position
            old_pos = self.positions[symbol]
            self.positions[symbol] = Position(
                symbol=symbol,
                direction=pos_dir,
                size=size,
                entry_price=entry_price,
                entry_time=entry_time,
                current_price=old_pos.current_price,
            )
        else:
            # Create new position
            self.positions[symbol] = Position(
                symbol=symbol,
                direction=pos_dir,
                size=size,
                entry_price=entry_price,
                entry_time=entry_time,
            )

        self.cash -= cash_impact

    def close_position(
        self,
        symbol: str,
        exit_price: float,
        exit_time: datetime = None,
    ) -> Optional[Dict]:
        """Close a position and record trade.

        Args:
            symbol: Contract symbol
            exit_price: Exit price
            exit_time: Exit time (default: now)

        Returns:
            Trade record dictionary or None if position didn't exist
        """
        if symbol not in self.positions:
            return None

        if exit_time is None:
            exit_time = datetime.now()

        pos = self.positions[symbol]
        trade_record = {
            "symbol": symbol,
            "direction": pos.direction.name,
            "size": pos.size,
            "entry_price": pos.entry_price,
            "entry_time": pos.entry_time,
            "exit_price": exit_price,
            "exit_time": exit_time,
            "pnl": pos.pnl,
            "pnl_pct": pos.pnl_pct,
        }

        self.trade_history.append(trade_record)
        cash_return = pos.size * exit_price
        self.cash += cash_return

        del self.positions[symbol]
        return trade_record

    def update_prices(self, price_data: Dict[str, float]) -> None:
        """Update current prices for positions.

        Args:
            price_data: Dict of {symbol: price}
        """
        for symbol, price in price_data.items():
            if symbol in self.positions:
                self.positions[symbol].update_price(price)

    @property
    def total_value(self) -> float:
        """Get total portfolio value (cash + positions).

        Returns:
            Total value
        """
        position_value = sum(
            p.size * p.current_price * p.direction.value for p in self.positions.values()
        )
        return self.cash + position_value

    @property
    def portfolio_pnl(self) -> float:
        """Get total unrealized P&L.

        Returns:
            Total P&L
        """
        return sum(p.pnl for p in self.positions.values())

    @property
    def portfolio_pnl_pct(self) -> float:
        """Get total P&L percentage.

        Returns:
            P&L as percentage of initial cash
        """
        if self.initial_cash == 0:
            return 0.0
        return self.portfolio_pnl / self.initial_cash

    @property
    def net_position(self) -> float:
        """Get net position (long - short).

        Returns:
            Net position size
        """
        return sum(
            p.size * p.direction.value for p in self.positions.values()
        )

    def get_position(self, symbol: str) -> Optional[Position]:
        """Get position by symbol.

        Args:
            symbol: Contract symbol

        Returns:
            Position or None
        """
        return self.positions.get(symbol)

    def to_dataframe(self) -> pd.DataFrame:
        """Convert positions to DataFrame.

        Returns:
            DataFrame with position details
        """
        if not self.positions:
            return pd.DataFrame()

        return pd.DataFrame([p.to_dict() for p in self.positions.values()])

    def summary(self) -> Dict:
        """Get portfolio summary.

        Returns:
            Summary dictionary with key metrics
        """
        return {
            "cash": self.cash,
            "initial_cash": self.initial_cash,
            "total_value": self.total_value,
            "unrealized_pnl": self.portfolio_pnl,
            "unrealized_pnl_pct": self.portfolio_pnl_pct,
            "net_position": self.net_position,
            "num_open_positions": len([p for p in self.positions.values() if p.is_open]),
            "total_trades": len(self.trade_history),
        }
