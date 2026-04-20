"""Extended strategy library — 5 new strategy classes extracted from 950 PLA logic.

Contents:
    - CCIStrategy         Commodity Channel Index mean-reversion / breakout (PLA: 16 files)
    - DMIStrategy         Directional Movement / ADX trend follower (PLA: 16 files)
    - MACDStrategy        MACD zero-line + histogram trend (PLA: 13 files)
    - ORBStrategy         Opening Range Breakout — intraday (PLA: 15 files)
    - KeltnerStrategy     Keltner channel breakout (PLA: 8 files)

All strategies inherit from :class:`trading_core.strategy.base.BaseStrategy` and
implement :meth:`on_bar`. Indicators are computed lazily on the first ``on_bar``
call to avoid repeated work, then cached on the ``ohlcv`` DataFrame via
:meth:`BaseStrategy.add_indicator`.

Design invariants:
    * Immutable per-strategy configuration via ``frozen=True`` dataclasses.
    * No print statements — use :mod:`logging`.
    * No hidden state mutation of input data outside indicator columns.
    * All numeric outputs are ``float`` to avoid mixed-type surprises downstream.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
import pandas as pd

from trading_core.strategy.base import BaseStrategy

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Indicator helpers (pure pandas / numpy — no talib dependency)
# ---------------------------------------------------------------------------


def _true_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Compute True Range component used by ATR / DMI / Keltner."""
    prev_close = close.shift(1)
    tr1 = high - low
    tr2 = (high - prev_close).abs()
    tr3 = (low - prev_close).abs()
    return pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, length: int) -> pd.Series:
    """Average True Range via Wilder smoothing approximation (EMA)."""
    tr = _true_range(high, low, close)
    return tr.ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean()


def _ema(series: pd.Series, length: int) -> pd.Series:
    """Exponential moving average."""
    return series.ewm(span=length, adjust=False, min_periods=length).mean()


def _sma(series: pd.Series, length: int) -> pd.Series:
    """Simple moving average."""
    return series.rolling(window=length, min_periods=length).mean()


def _cci(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    length: int,
    constant: float = 0.015,
) -> pd.Series:
    """Commodity Channel Index.

    CCI = (Typical Price - SMA_TP) / (constant * mean absolute deviation)
    """
    tp = (high + low + close) / 3.0
    sma_tp = tp.rolling(window=length, min_periods=length).mean()
    mad = tp.rolling(window=length, min_periods=length).apply(
        lambda x: np.mean(np.abs(x - np.mean(x))), raw=True
    )
    # Avoid divide-by-zero warnings; where mad==0 return 0.
    denom = (constant * mad).replace(0, np.nan)
    return ((tp - sma_tp) / denom).fillna(0.0)


def _dmi(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    length: int,
) -> pd.DataFrame:
    """Directional Movement Index / ADX (Wilder).

    Returns a DataFrame with columns ``+DI``, ``-DI``, ``ADX``.
    """
    up_move = high.diff()
    down_move = -low.diff()

    plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0.0)
    minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0.0)

    plus_dm_s = pd.Series(plus_dm, index=high.index)
    minus_dm_s = pd.Series(minus_dm, index=high.index)

    tr = _true_range(high, low, close)
    atr = tr.ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean()

    plus_di = 100.0 * plus_dm_s.ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean() / atr
    minus_di = 100.0 * minus_dm_s.ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean() / atr

    dx = 100.0 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    adx = dx.ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean()

    return pd.DataFrame({"+DI": plus_di, "-DI": minus_di, "ADX": adx}).fillna(0.0)


def _macd(
    close: pd.Series, fast: int, slow: int, signal: int
) -> pd.DataFrame:
    """Classic MACD returning ``MACD``, ``SIGNAL``, ``HIST``."""
    macd_line = _ema(close, fast) - _ema(close, slow)
    signal_line = macd_line.ewm(span=signal, adjust=False, min_periods=signal).mean()
    hist = macd_line - signal_line
    return pd.DataFrame({"MACD": macd_line, "SIGNAL": signal_line, "HIST": hist})


def _keltner(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    length: int,
    mult: float,
) -> pd.DataFrame:
    """Keltner Channel = EMA(close) +/- mult * ATR."""
    mid = _ema(close, length)
    atr = _atr(high, low, close, length)
    upper = mid + mult * atr
    lower = mid - mult * atr
    return pd.DataFrame({"KC_MID": mid, "KC_UP": upper, "KC_LO": lower, "ATR": atr})


# ---------------------------------------------------------------------------
# 1. CCI — mean reversion + threshold breakout (PLA family: 16 files)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CCIConfig:
    length: int = 20
    overbought: float = 100.0
    oversold: float = -100.0
    exit_zero_cross: bool = True
    atr_stop_mult: float = 2.0
    atr_length: int = 14
    allow_short: bool = True


class CCIStrategy(BaseStrategy):
    """Commodity Channel Index strategy.

    Entry:
        long  when CCI crosses **above** ``oversold`` (rebound).
        short when CCI crosses **below** ``overbought`` (fade).
    Exit:
        * CCI zero cross (if ``exit_zero_cross`` enabled), OR
        * ATR-based stop at ``atr_stop_mult * ATR`` from entry.
    """

    def __init__(
        self,
        name: str = "CCI",
        initial_capital: float = 100_000.0,
        contract: str = "TXF",
        config: Optional[CCIConfig] = None,
    ) -> None:
        super().__init__(name=name, initial_capital=initial_capital, contract=contract)
        self.config: CCIConfig = config or CCIConfig()
        self._entry_price: Optional[float] = None
        self._indicators_ready = False

    # --------------------------------------------------------------
    def _ensure_indicators(self) -> None:
        if self._indicators_ready or self.ohlcv is None:
            return
        cfg = self.config
        self.add_indicator("CCI", _cci(self.ohlcv["high"], self.ohlcv["low"], self.ohlcv["close"], cfg.length))
        self.add_indicator("ATR", _atr(self.ohlcv["high"], self.ohlcv["low"], self.ohlcv["close"], cfg.atr_length))
        self._indicators_ready = True

    # --------------------------------------------------------------
    def on_bar(self) -> None:
        self._ensure_indicators()
        if self.current_bar_idx < max(self.config.length, self.config.atr_length) + 1:
            return

        prev = self.ohlcv.iloc[self.current_bar_idx - 1]
        cur = self.current_bar
        cci_prev = float(prev["CCI"])
        cci_cur = float(cur["CCI"])
        atr_cur = float(cur["ATR"]) if not np.isnan(cur["ATR"]) else 0.0
        price = float(cur["close"])

        pos_size = self.get_position_size()

        # ---- Exit logic first
        if pos_size != 0 and self._entry_price is not None:
            if self.config.exit_zero_cross:
                if pos_size > 0 and cci_cur <= 0 < cci_prev:
                    self.close_position()
                    self._entry_price = None
                    return
                if pos_size < 0 and cci_cur >= 0 > cci_prev:
                    self.close_position()
                    self._entry_price = None
                    return
            # ATR stop
            if atr_cur > 0:
                if pos_size > 0 and price <= self._entry_price - self.config.atr_stop_mult * atr_cur:
                    self.close_position()
                    self._entry_price = None
                    return
                if pos_size < 0 and price >= self._entry_price + self.config.atr_stop_mult * atr_cur:
                    self.close_position()
                    self._entry_price = None
                    return

        # ---- Entry logic
        if pos_size == 0:
            if cci_prev <= self.config.oversold < cci_cur:
                self.buy()
                self._entry_price = price
            elif self.config.allow_short and cci_prev >= self.config.overbought > cci_cur:
                self.sell()
                self._entry_price = price


# ---------------------------------------------------------------------------
# 2. DMI / ADX trend follower (PLA family: 16 files)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class DMIConfig:
    length: int = 14
    adx_threshold: float = 20.0
    atr_stop_mult: float = 2.0
    atr_length: int = 14
    allow_short: bool = True


class DMIStrategy(BaseStrategy):
    """DMI / ADX trend-following strategy.

    Entry:
        long  when +DI > -DI **and** ADX >= threshold (trend in motion).
        short when -DI > +DI **and** ADX >= threshold.
    Exit:
        * DI reversal (direction flip), OR
        * ATR stop from entry.
    """

    def __init__(
        self,
        name: str = "DMI",
        initial_capital: float = 100_000.0,
        contract: str = "TXF",
        config: Optional[DMIConfig] = None,
    ) -> None:
        super().__init__(name=name, initial_capital=initial_capital, contract=contract)
        self.config: DMIConfig = config or DMIConfig()
        self._entry_price: Optional[float] = None
        self._indicators_ready = False

    def _ensure_indicators(self) -> None:
        if self._indicators_ready or self.ohlcv is None:
            return
        cfg = self.config
        dmi = _dmi(self.ohlcv["high"], self.ohlcv["low"], self.ohlcv["close"], cfg.length)
        self.add_indicator("+DI", dmi["+DI"])
        self.add_indicator("-DI", dmi["-DI"])
        self.add_indicator("ADX", dmi["ADX"])
        self.add_indicator("ATR", _atr(self.ohlcv["high"], self.ohlcv["low"], self.ohlcv["close"], cfg.atr_length))
        self._indicators_ready = True

    def on_bar(self) -> None:
        self._ensure_indicators()
        if self.current_bar_idx < self.config.length * 2 + 1:
            return

        cur = self.current_bar
        plus_di = float(cur["+DI"])
        minus_di = float(cur["-DI"])
        adx = float(cur["ADX"])
        atr = float(cur["ATR"]) if not np.isnan(cur["ATR"]) else 0.0
        price = float(cur["close"])
        pos_size = self.get_position_size()

        # Exit on DI flip or ATR stop
        if pos_size != 0 and self._entry_price is not None:
            if pos_size > 0 and minus_di > plus_di:
                self.close_position()
                self._entry_price = None
                return
            if pos_size < 0 and plus_di > minus_di:
                self.close_position()
                self._entry_price = None
                return
            if atr > 0:
                if pos_size > 0 and price <= self._entry_price - self.config.atr_stop_mult * atr:
                    self.close_position()
                    self._entry_price = None
                    return
                if pos_size < 0 and price >= self._entry_price + self.config.atr_stop_mult * atr:
                    self.close_position()
                    self._entry_price = None
                    return

        # Entry
        if pos_size == 0 and adx >= self.config.adx_threshold:
            if plus_di > minus_di:
                self.buy()
                self._entry_price = price
            elif self.config.allow_short and minus_di > plus_di:
                self.sell()
                self._entry_price = price


# ---------------------------------------------------------------------------
# 3. MACD trend / zero-line crossover (PLA family: 13 files)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class MACDConfig:
    fast: int = 12
    slow: int = 26
    signal: int = 9
    hist_min: float = 0.0
    use_signal_cross: bool = True
    atr_stop_mult: float = 2.5
    atr_length: int = 14
    allow_short: bool = True


class MACDStrategy(BaseStrategy):
    """MACD strategy — signal-line cross OR zero-line cross.

    Entry:
        long  when MACD crosses above SIGNAL (or above 0 if ``use_signal_cross`` False)
              **and** histogram magnitude ``HIST > hist_min``.
        short mirror conditions.
    Exit:
        * Opposite MACD/SIGNAL cross, OR
        * ATR stop.
    """

    def __init__(
        self,
        name: str = "MACD",
        initial_capital: float = 100_000.0,
        contract: str = "TXF",
        config: Optional[MACDConfig] = None,
    ) -> None:
        super().__init__(name=name, initial_capital=initial_capital, contract=contract)
        self.config: MACDConfig = config or MACDConfig()
        self._entry_price: Optional[float] = None
        self._indicators_ready = False

    def _ensure_indicators(self) -> None:
        if self._indicators_ready or self.ohlcv is None:
            return
        cfg = self.config
        macd = _macd(self.ohlcv["close"], cfg.fast, cfg.slow, cfg.signal)
        self.add_indicator("MACD", macd["MACD"])
        self.add_indicator("SIGNAL", macd["SIGNAL"])
        self.add_indicator("HIST", macd["HIST"])
        self.add_indicator("ATR", _atr(self.ohlcv["high"], self.ohlcv["low"], self.ohlcv["close"], cfg.atr_length))
        self._indicators_ready = True

    def on_bar(self) -> None:
        self._ensure_indicators()
        warmup = self.config.slow + self.config.signal + 1
        if self.current_bar_idx < warmup:
            return

        prev = self.ohlcv.iloc[self.current_bar_idx - 1]
        cur = self.current_bar
        macd_prev, macd_cur = float(prev["MACD"]), float(cur["MACD"])
        sig_prev, sig_cur = float(prev["SIGNAL"]), float(cur["SIGNAL"])
        hist = float(cur["HIST"])
        atr = float(cur["ATR"]) if not np.isnan(cur["ATR"]) else 0.0
        price = float(cur["close"])
        pos_size = self.get_position_size()

        # Cross detection
        if self.config.use_signal_cross:
            long_cross = macd_prev <= sig_prev and macd_cur > sig_cur
            short_cross = macd_prev >= sig_prev and macd_cur < sig_cur
        else:
            long_cross = macd_prev <= 0 < macd_cur
            short_cross = macd_prev >= 0 > macd_cur

        # Exit
        if pos_size != 0 and self._entry_price is not None:
            if pos_size > 0 and short_cross:
                self.close_position()
                self._entry_price = None
                return
            if pos_size < 0 and long_cross:
                self.close_position()
                self._entry_price = None
                return
            if atr > 0:
                if pos_size > 0 and price <= self._entry_price - self.config.atr_stop_mult * atr:
                    self.close_position()
                    self._entry_price = None
                    return
                if pos_size < 0 and price >= self._entry_price + self.config.atr_stop_mult * atr:
                    self.close_position()
                    self._entry_price = None
                    return

        # Entry
        if pos_size == 0 and abs(hist) >= self.config.hist_min:
            if long_cross:
                self.buy()
                self._entry_price = price
            elif self.config.allow_short and short_cross:
                self.sell()
                self._entry_price = price


# ---------------------------------------------------------------------------
# 4. Opening Range Breakout — intraday (PLA family: 15 files)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ORBConfig:
    opening_bars: int = 6          # # of bars that define the opening range
    session_start_hour: int = 9    # first valid trading hour (exchange local)
    session_close_hour: int = 13   # force-close before this hour ends
    breakout_buffer_pct: float = 0.0  # optional percentage buffer above range
    atr_stop_mult: float = 1.5
    atr_length: int = 14
    allow_short: bool = True


class ORBStrategy(BaseStrategy):
    """Opening Range Breakout.

    Builds an opening range from the first N bars of each day.  Goes long on
    break above the high (+ buffer), short on break below the low.  Exits on
    opposite break or session-close.

    Assumes OHLCV has a ``DatetimeIndex`` with enough resolution to identify
    day boundaries (intra-day bars).  If data is already daily, the strategy
    treats each bar as its own session — still valid but trivially flat after
    the first bar of each day.
    """

    def __init__(
        self,
        name: str = "ORB",
        initial_capital: float = 100_000.0,
        contract: str = "TXF",
        config: Optional[ORBConfig] = None,
    ) -> None:
        super().__init__(name=name, initial_capital=initial_capital, contract=contract)
        self.config: ORBConfig = config or ORBConfig()
        self._entry_price: Optional[float] = None
        self._current_day: Optional[object] = None
        self._day_bar_count: int = 0
        self._range_high: Optional[float] = None
        self._range_low: Optional[float] = None
        self._indicators_ready: bool = False

    def _ensure_indicators(self) -> None:
        if self._indicators_ready or self.ohlcv is None:
            return
        cfg = self.config
        self.add_indicator(
            "ATR",
            _atr(self.ohlcv["high"], self.ohlcv["low"], self.ohlcv["close"], cfg.atr_length),
        )
        self._indicators_ready = True

    def on_bar(self) -> None:
        self._ensure_indicators()

        cur = self.current_bar
        ts = cur.name  # Timestamp
        price = float(cur["close"])
        high = float(cur["high"])
        low = float(cur["low"])
        atr = float(cur["ATR"]) if ("ATR" in cur.index and not np.isnan(cur["ATR"])) else 0.0

        # Day boundary detection
        day_key = ts.date() if hasattr(ts, "date") else ts
        if day_key != self._current_day:
            # New day — close any lingering overnight position
            if self.get_position_size() != 0:
                self.close_position()
                self._entry_price = None
            self._current_day = day_key
            self._day_bar_count = 0
            self._range_high = None
            self._range_low = None

        # Build opening range
        if self._day_bar_count < self.config.opening_bars:
            self._range_high = high if self._range_high is None else max(self._range_high, high)
            self._range_low = low if self._range_low is None else min(self._range_low, low)
            self._day_bar_count += 1
            return

        pos_size = self.get_position_size()

        # Session close — force flat
        hour = ts.hour if hasattr(ts, "hour") else 0
        if hour >= self.config.session_close_hour and pos_size != 0:
            self.close_position()
            self._entry_price = None
            return

        buffer_abs = self._range_high * self.config.breakout_buffer_pct if self._range_high else 0.0

        # Exit on opposite break OR ATR stop
        if pos_size != 0 and self._entry_price is not None:
            if pos_size > 0 and price < self._range_low:
                self.close_position()
                self._entry_price = None
                return
            if pos_size < 0 and price > self._range_high:
                self.close_position()
                self._entry_price = None
                return
            if atr > 0:
                if pos_size > 0 and price <= self._entry_price - self.config.atr_stop_mult * atr:
                    self.close_position()
                    self._entry_price = None
                    return
                if pos_size < 0 and price >= self._entry_price + self.config.atr_stop_mult * atr:
                    self.close_position()
                    self._entry_price = None
                    return

        # Entry
        if pos_size == 0 and self._range_high is not None and self._range_low is not None:
            if price > self._range_high + buffer_abs:
                self.buy()
                self._entry_price = price
            elif self.config.allow_short and price < self._range_low - buffer_abs:
                self.sell()
                self._entry_price = price


# ---------------------------------------------------------------------------
# 5. Keltner Channel Breakout (PLA family: 8 files)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class KeltnerConfig:
    length: int = 20
    mult: float = 2.0
    mode: str = "breakout"   # "breakout" or "mean_reversion"
    atr_stop_mult: float = 1.5
    allow_short: bool = True


class KeltnerStrategy(BaseStrategy):
    """Keltner Channel strategy (breakout or mean-reversion).

    Breakout mode:
        long  on close > upper channel;  short on close < lower channel.
        Exit when price re-enters the mid.
    Mean-reversion mode:
        long  on close < lower channel;  short on close > upper channel.
        Exit on mid crossover.
    """

    def __init__(
        self,
        name: str = "Keltner",
        initial_capital: float = 100_000.0,
        contract: str = "TXF",
        config: Optional[KeltnerConfig] = None,
    ) -> None:
        super().__init__(name=name, initial_capital=initial_capital, contract=contract)
        self.config: KeltnerConfig = config or KeltnerConfig()
        if self.config.mode not in ("breakout", "mean_reversion"):
            raise ValueError(f"Unknown Keltner mode: {self.config.mode!r}")
        self._entry_price: Optional[float] = None
        self._indicators_ready = False

    def _ensure_indicators(self) -> None:
        if self._indicators_ready or self.ohlcv is None:
            return
        cfg = self.config
        kc = _keltner(
            self.ohlcv["high"], self.ohlcv["low"], self.ohlcv["close"], cfg.length, cfg.mult
        )
        self.add_indicator("KC_MID", kc["KC_MID"])
        self.add_indicator("KC_UP", kc["KC_UP"])
        self.add_indicator("KC_LO", kc["KC_LO"])
        self.add_indicator("ATR", kc["ATR"])
        self._indicators_ready = True

    def on_bar(self) -> None:
        self._ensure_indicators()
        if self.current_bar_idx < self.config.length + 2:
            return

        cur = self.current_bar
        price = float(cur["close"])
        mid = float(cur["KC_MID"])
        up = float(cur["KC_UP"])
        lo = float(cur["KC_LO"])
        atr = float(cur["ATR"]) if not np.isnan(cur["ATR"]) else 0.0
        pos_size = self.get_position_size()

        # Exit first
        if pos_size != 0 and self._entry_price is not None:
            # Mid re-cross
            if self.config.mode == "breakout":
                if pos_size > 0 and price < mid:
                    self.close_position()
                    self._entry_price = None
                    return
                if pos_size < 0 and price > mid:
                    self.close_position()
                    self._entry_price = None
                    return
            else:  # mean_reversion
                if pos_size > 0 and price >= mid:
                    self.close_position()
                    self._entry_price = None
                    return
                if pos_size < 0 and price <= mid:
                    self.close_position()
                    self._entry_price = None
                    return
            # ATR stop
            if atr > 0:
                if pos_size > 0 and price <= self._entry_price - self.config.atr_stop_mult * atr:
                    self.close_position()
                    self._entry_price = None
                    return
                if pos_size < 0 and price >= self._entry_price + self.config.atr_stop_mult * atr:
                    self.close_position()
                    self._entry_price = None
                    return

        # Entry
        if pos_size == 0:
            if self.config.mode == "breakout":
                if price > up:
                    self.buy()
                    self._entry_price = price
                elif self.config.allow_short and price < lo:
                    self.sell()
                    self._entry_price = price
            else:  # mean_reversion
                if price < lo:
                    self.buy()
                    self._entry_price = price
                elif self.config.allow_short and price > up:
                    self.sell()
                    self._entry_price = price


__all__ = [
    # indicators (exported for pla_catalog reuse and tests)
    "_atr",
    "_cci",
    "_dmi",
    "_ema",
    "_keltner",
    "_macd",
    "_sma",
    "_true_range",
    # configs
    "CCIConfig",
    "DMIConfig",
    "MACDConfig",
    "ORBConfig",
    "KeltnerConfig",
    # strategies
    "CCIStrategy",
    "DMIStrategy",
    "MACDStrategy",
    "ORBStrategy",
    "KeltnerStrategy",
]
