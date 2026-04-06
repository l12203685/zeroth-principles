"""Configuration settings for trading system.

This module provides centralized configuration management using environment variables.
All sensitive information (API keys, passwords, paths) should be stored in .env file,
not hardcoded in the source.
"""

import os
from dataclasses import dataclass, asdict
from typing import Optional
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(dotenv_path=None):
        """Fallback if python-dotenv not installed."""
        pass


@dataclass
class Settings:
    """Settings for trading system.

    Attributes:
        # Broker credentials
        broker_api_key: Sinopac API key
        broker_secret: Sinopac API secret
        broker_person_id: Person ID for CA certification
        broker_ca_path: Path to .pfx certificate file

        # Market data
        market_data_dir: Directory to store market data
        txf_data_file: Path to TXF tick data file

        # Trading
        contract_default: Default contract code (e.g., 'TXF')
        commission_rate: Commission rate as percentage (default 0.025%)
        commission_tick: Minimum commission in ticks (default 2.5)
        big_point_value: Point value for futures (default 200 for TXF)

        # Logging
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_dir: Directory for log files
    """

    # Broker settings
    broker_api_key: str = ""
    broker_secret: str = ""
    broker_person_id: str = ""
    broker_ca_path: str = ""

    # Market data paths
    market_data_dir: str = "./data"
    txf_data_file: str = "./data/txf_trades"

    # Trading parameters
    contract_default: str = "TXF"
    commission_rate: float = 0.025  # percentage
    commission_tick: float = 2.5    # tick amount
    big_point_value: float = 200.0  # for TXF

    # Logging
    log_level: str = "INFO"
    log_dir: str = "./logs"

    def __post_init__(self):
        """Create required directories."""
        Path(self.market_data_dir).mkdir(parents=True, exist_ok=True)
        Path(self.log_dir).mkdir(parents=True, exist_ok=True)

    def to_dict(self) -> dict:
        """Convert settings to dictionary."""
        return asdict(self)

    @classmethod
    def from_env(cls, env_file: Optional[str] = None) -> "Settings":
        """Load settings from environment variables.

        Args:
            env_file: Path to .env file. If None, looks for .env in current directory.

        Returns:
            Settings instance with values from environment variables.
        """
        if env_file is None:
            env_file = ".env"

        if os.path.exists(env_file):
            load_dotenv(env_file)
        else:
            load_dotenv()

        return cls(
            broker_api_key=os.getenv("BROKER_API_KEY", ""),
            broker_secret=os.getenv("BROKER_SECRET", ""),
            broker_person_id=os.getenv("BROKER_PERSON_ID", ""),
            broker_ca_path=os.getenv("BROKER_CA_PATH", ""),
            market_data_dir=os.getenv("MARKET_DATA_DIR", "./data"),
            txf_data_file=os.getenv("TXF_DATA_FILE", "./data/txf_trades"),
            contract_default=os.getenv("CONTRACT_DEFAULT", "TXF"),
            commission_rate=float(os.getenv("COMMISSION_RATE", "0.025")),
            commission_tick=float(os.getenv("COMMISSION_TICK", "2.5")),
            big_point_value=float(os.getenv("BIG_POINT_VALUE", "200.0")),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
            log_dir=os.getenv("LOG_DIR", "./logs"),
        )


# Global settings instance
_settings: Optional[Settings] = None


def get_settings() -> Settings:
    """Get global settings instance.

    Returns:
        Global Settings instance. Loads from .env on first call.
    """
    global _settings
    if _settings is None:
        _settings = Settings.from_env()
    return _settings


def set_settings(settings: Settings) -> None:
    """Set global settings instance.

    Args:
        settings: Settings instance to use globally.
    """
    global _settings
    _settings = settings
