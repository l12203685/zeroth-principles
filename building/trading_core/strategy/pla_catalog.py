"""PLA pattern catalog + strategy generator.

This module catalogs the **recurring entry/exit/filter/risk patterns** extracted
from the 950 PLA logic files (see ``LYH/systems/pla_knowledge_synthesis.md``)
and exposes a parameter-space driven ``StrategyGenerator`` that produces
concrete :class:`BaseStrategy` instances.

Design:
    * ``PLAPattern`` — frozen dataclass capturing one logical pattern:
      ``family`` (breakout / trend / mean_reversion / filter / risk),
      ``indicators`` used, ``param_space`` (grid of parameter variants), and
      ``builder`` (callable ``(params) -> BaseStrategy``).
    * ``PLA_CATALOG`` — curated list of patterns that map directly to the
      strategies in :mod:`strategies_extended`.
    * ``StrategyGenerator.expand()`` — cartesian-product expansion of a
      pattern's ``param_space`` into concrete strategy instances (with an
      optional ``sample`` cap for deterministic sub-sampling).

The catalog is intentionally **open for extension**: adding a new pattern only
requires appending to ``PLA_CATALOG``.
"""

from __future__ import annotations

import itertools
import logging
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple

from trading_core.strategy.base import BaseStrategy
from trading_core.strategy.strategies_extended import (
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

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Core data classes
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PLAPattern:
    """A single PLA-derived pattern descriptor.

    Attributes:
        name: Human-readable pattern identifier (unique within the catalog).
        family: One of ``breakout | trend | mean_reversion | filter | risk``.
        indicators: Tuple of indicator tags used by the pattern
            (e.g. ``("CCI", "ATR")``).
        param_space: Mapping of parameter-name -> iterable of allowed values.
        builder: Callable that takes a ``dict`` of params and returns a
            ready-to-run :class:`BaseStrategy`.
        pla_file_count: Number of PLA source files from which this pattern was
            observed (reference only; used for ranking).
        description: Prose description.
    """

    name: str
    family: str
    indicators: Tuple[str, ...]
    param_space: Dict[str, Tuple[Any, ...]]
    builder: Callable[[Dict[str, Any]], BaseStrategy]
    pla_file_count: int = 0
    description: str = ""

    def space_size(self) -> int:
        """Return total cartesian size of the parameter grid."""
        if not self.param_space:
            return 1
        sizes = [len(v) for v in self.param_space.values()]
        n = 1
        for s in sizes:
            n *= s
        return n

    def iter_params(self) -> Iterable[Dict[str, Any]]:
        """Iterate all param combinations."""
        keys = list(self.param_space.keys())
        if not keys:
            yield {}
            return
        values_lists = [self.param_space[k] for k in keys]
        for combo in itertools.product(*values_lists):
            yield dict(zip(keys, combo))


# ---------------------------------------------------------------------------
# Builder helpers (keep top-level + importable — lambdas are not picklable)
# ---------------------------------------------------------------------------


def _build_cci(params: Dict[str, Any]) -> BaseStrategy:
    return CCIStrategy(
        name=f"CCI_{params.get('length', 20)}_{int(params.get('overbought', 100))}",
        config=CCIConfig(
            length=params.get("length", 20),
            overbought=params.get("overbought", 100.0),
            oversold=params.get("oversold", -100.0),
            atr_stop_mult=params.get("atr_stop_mult", 2.0),
            allow_short=params.get("allow_short", True),
        ),
    )


def _build_dmi(params: Dict[str, Any]) -> BaseStrategy:
    return DMIStrategy(
        name=f"DMI_{params.get('length', 14)}_{int(params.get('adx_threshold', 20))}",
        config=DMIConfig(
            length=params.get("length", 14),
            adx_threshold=params.get("adx_threshold", 20.0),
            atr_stop_mult=params.get("atr_stop_mult", 2.0),
            allow_short=params.get("allow_short", True),
        ),
    )


def _build_macd(params: Dict[str, Any]) -> BaseStrategy:
    return MACDStrategy(
        name=f"MACD_{params.get('fast', 12)}_{params.get('slow', 26)}_{params.get('signal', 9)}",
        config=MACDConfig(
            fast=params.get("fast", 12),
            slow=params.get("slow", 26),
            signal=params.get("signal", 9),
            hist_min=params.get("hist_min", 0.0),
            atr_stop_mult=params.get("atr_stop_mult", 2.5),
            allow_short=params.get("allow_short", True),
        ),
    )


def _build_orb(params: Dict[str, Any]) -> BaseStrategy:
    return ORBStrategy(
        name=f"ORB_{params.get('opening_bars', 6)}",
        config=ORBConfig(
            opening_bars=params.get("opening_bars", 6),
            session_close_hour=params.get("session_close_hour", 13),
            breakout_buffer_pct=params.get("breakout_buffer_pct", 0.0),
            atr_stop_mult=params.get("atr_stop_mult", 1.5),
            allow_short=params.get("allow_short", True),
        ),
    )


def _build_keltner(params: Dict[str, Any]) -> BaseStrategy:
    return KeltnerStrategy(
        name=f"Keltner_{params.get('length', 20)}_{params.get('mult', 2.0)}_{params.get('mode', 'breakout')}",
        config=KeltnerConfig(
            length=params.get("length", 20),
            mult=params.get("mult", 2.0),
            mode=params.get("mode", "breakout"),
            atr_stop_mult=params.get("atr_stop_mult", 1.5),
            allow_short=params.get("allow_short", True),
        ),
    )


# ---------------------------------------------------------------------------
# Canonical catalog — maps PLA synthesis (Top-30 ranked table) to code.
# ---------------------------------------------------------------------------

PLA_CATALOG: Tuple[PLAPattern, ...] = (
    PLAPattern(
        name="cci_reversion",
        family="mean_reversion",
        indicators=("CCI", "ATR"),
        param_space={
            "length": (14, 20, 28),
            "overbought": (100.0, 150.0, 200.0),
            "oversold": (-100.0, -150.0, -200.0),
            "atr_stop_mult": (1.5, 2.0, 2.5),
        },
        builder=_build_cci,
        pla_file_count=16,
        description="CCI overbought/oversold rebound with ATR stop (PLA: 16 files).",
    ),
    PLAPattern(
        name="dmi_trend",
        family="trend",
        indicators=("DMI", "ADX", "ATR"),
        param_space={
            "length": (10, 14, 20),
            "adx_threshold": (15.0, 20.0, 25.0),
            "atr_stop_mult": (1.5, 2.0, 3.0),
        },
        builder=_build_dmi,
        pla_file_count=16,
        description="DMI/ADX trend follower with DI-flip exit (PLA: 16 files).",
    ),
    PLAPattern(
        name="macd_trend",
        family="trend",
        indicators=("MACD", "ATR"),
        param_space={
            "fast": (8, 12),
            "slow": (21, 26),
            "signal": (7, 9),
            "atr_stop_mult": (2.0, 2.5, 3.0),
        },
        builder=_build_macd,
        pla_file_count=13,
        description="MACD signal/zero-line crossover trend (PLA: 13 files).",
    ),
    PLAPattern(
        name="orb_intraday",
        family="breakout",
        indicators=("Highest", "Lowest", "ATR"),
        param_space={
            "opening_bars": (3, 6, 10),
            "session_close_hour": (12, 13, 14),
            "breakout_buffer_pct": (0.0, 0.001),
            "atr_stop_mult": (1.0, 1.5, 2.0),
        },
        builder=_build_orb,
        pla_file_count=15,
        description="Opening range breakout, intraday (PLA: 15 files).",
    ),
    PLAPattern(
        name="keltner_channel",
        family="breakout",
        indicators=("Keltner", "ATR"),
        param_space={
            "length": (14, 20, 30),
            "mult": (1.5, 2.0, 2.5),
            "mode": ("breakout", "mean_reversion"),
            "atr_stop_mult": (1.0, 1.5, 2.0),
        },
        builder=_build_keltner,
        pla_file_count=8,
        description="Keltner channel breakout / mean-reversion (PLA: 8 files).",
    ),
)


# ---------------------------------------------------------------------------
# StrategyGenerator — expand catalog to concrete strategies
# ---------------------------------------------------------------------------


@dataclass
class StrategyGenerator:
    """Expand :data:`PLA_CATALOG` entries into concrete strategies.

    Attributes:
        catalog: Iterable of :class:`PLAPattern` (defaults to :data:`PLA_CATALOG`).
    """

    catalog: Tuple[PLAPattern, ...] = field(default_factory=lambda: PLA_CATALOG)

    def by_name(self, name: str) -> PLAPattern:
        """Return pattern by name or raise ``KeyError``."""
        for p in self.catalog:
            if p.name == name:
                return p
        raise KeyError(f"No PLA pattern named {name!r}")

    def families(self) -> List[str]:
        """Return sorted unique families in the catalog."""
        return sorted({p.family for p in self.catalog})

    def filter(
        self,
        family: Optional[str] = None,
        indicator: Optional[str] = None,
    ) -> List[PLAPattern]:
        """Return catalog subset filtered by family and/or indicator tag."""
        out: List[PLAPattern] = []
        for p in self.catalog:
            if family is not None and p.family != family:
                continue
            if indicator is not None and indicator not in p.indicators:
                continue
            out.append(p)
        return out

    def expand(
        self,
        pattern_name: str,
        sample: Optional[int] = None,
    ) -> List[BaseStrategy]:
        """Expand one pattern to concrete strategies.

        Args:
            pattern_name: Name of pattern in catalog.
            sample: If not ``None``, deterministically down-sample by taking
                every ``ceil(N / sample)``-th combination.  Useful for keeping
                Phase-1 gates cheap while covering the space.
        """
        pat = self.by_name(pattern_name)
        combos = list(pat.iter_params())
        if sample is not None and sample > 0 and sample < len(combos):
            step = max(1, len(combos) // sample)
            combos = combos[::step][:sample]
        out: List[BaseStrategy] = []
        for c in combos:
            try:
                out.append(pat.builder(c))
            except Exception as e:  # noqa: BLE001
                logger.warning("Builder failed for pattern=%s params=%s: %s", pattern_name, c, e)
        return out

    def expand_all(
        self,
        sample_per_pattern: Optional[int] = None,
    ) -> List[BaseStrategy]:
        """Expand the whole catalog to a flat list of strategies."""
        out: List[BaseStrategy] = []
        for p in self.catalog:
            out.extend(self.expand(p.name, sample=sample_per_pattern))
        return out

    def summary(self) -> List[Dict[str, Any]]:
        """Return catalog summary as list of dicts (for dashboards)."""
        return [
            {
                "name": p.name,
                "family": p.family,
                "indicators": list(p.indicators),
                "param_space_size": p.space_size(),
                "pla_file_count": p.pla_file_count,
                "description": p.description,
            }
            for p in self.catalog
        ]


__all__ = [
    "PLAPattern",
    "PLA_CATALOG",
    "StrategyGenerator",
]
