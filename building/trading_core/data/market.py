"""Market data handling module.

Merged from:
- AlgoTrading/functions/func_load_data.py: various get_* functions
- AlgoTrading/functions/func_get_daily_data.py: data loading utilities
- sino-trade-api/function_file.py: get_tick() and market data functions
"""

import os
import pandas as pd
import numpy as np
from typing import Union, Optional, Dict, List
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


def get_ohlcv(
    filepath: str, freq: str = "1min", dtype: Optional[Dict] = None
) -> pd.DataFrame:
    """Load OHLCV (Open, High, Low, Close, Volume) data from CSV.

    Merged from multiple func_load_data.py implementations.

    Args:
        filepath: Path to CSV file or directory containing CSV files
        freq: Frequency of data ('1min', '5min', '1h', '1d', etc.)
        dtype: Data type mapping for columns

    Returns:
        DataFrame with columns: [datetime, open, high, low, close, volume]
        Index: datetime

    Raises:
        FileNotFoundError: If filepath doesn't exist
        ValueError: If CSV format is invalid
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File or directory not found: {filepath}")

    if os.path.isdir(filepath):
        # Load all CSV files in directory
        logger.info(f"Loading all CSV files from {filepath}")
        dfs = []
        for filename in os.listdir(filepath):
            if filename.endswith(".csv"):
                df = pd.read_csv(os.path.join(filepath, filename), dtype=dtype)
                dfs.append(df)
        if not dfs:
            raise ValueError(f"No CSV files found in {filepath}")
        data = pd.concat(dfs, ignore_index=True, sort=False)
    else:
        # Load single CSV file
        logger.info(f"Loading CSV file: {filepath}")
        data = pd.read_csv(filepath, dtype=dtype)

    # Standardize column names
    data.columns = data.columns.str.lower().str.strip()

    # Find and rename datetime column
    datetime_cols = [c for c in data.columns if "time" in c or "date" in c]
    if datetime_cols:
        datetime_col = datetime_cols[0]
        if "datetime" not in data.columns:
            data.rename(columns={datetime_col: "datetime"}, inplace=True)

    # Convert datetime
    if "datetime" in data.columns:
        data["datetime"] = pd.to_datetime(data["datetime"])
    else:
        raise ValueError("No datetime column found in data")

    # Ensure required OHLCV columns exist
    required = {"open", "high", "low", "close", "volume"}
    if not required.issubset(set(data.columns)):
        raise ValueError(f"Missing columns: {required - set(data.columns)}")

    # Select and order columns
    data = data[["datetime", "open", "high", "low", "close", "volume"]].copy()
    data = data.sort_values("datetime").reset_index(drop=True)

    # Convert price columns to float
    for col in ["open", "high", "low", "close", "volume"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    # Set datetime index
    data.set_index("datetime", inplace=True)

    # Remove duplicates
    data = data[~data.index.duplicated(keep="first")]

    logger.info(f"Loaded {len(data)} bars from {filepath}")
    return data


def resample_ohlcv(
    ohlcv: pd.DataFrame, target_freq: str = "5min"
) -> pd.DataFrame:
    """Resample OHLCV data to different frequency.

    Merged from AlgoTrading resample logic.

    Args:
        ohlcv: DataFrame with OHLCV columns and datetime index
        target_freq: Target frequency ('5min', '15min', '1h', '1d', etc.)

    Returns:
        Resampled OHLCV DataFrame
    """
    if "datetime" in ohlcv.columns:
        ohlcv = ohlcv.set_index("datetime")

    # Resample using OHLC aggregation
    resampled = pd.DataFrame({
        "open": ohlcv["open"].resample(target_freq).first(),
        "high": ohlcv["high"].resample(target_freq).max(),
        "low": ohlcv["low"].resample(target_freq).min(),
        "close": ohlcv["close"].resample(target_freq).last(),
        "volume": ohlcv["volume"].resample(target_freq).sum(),
    })

    # Remove rows with NaN opens (no data in that period)
    resampled = resampled.dropna(subset=["open"])

    return resampled


def get_tick_data(
    api,
    contract,
    start_date: datetime = None,
    end_date: datetime = None,
) -> pd.DataFrame:
    """Get tick-level data from broker API.

    Merged from sino-trade-api/function_file.py: get_tick()

    Args:
        api: Shioaji API instance
        contract: Contract object from api.Contracts
        start_date: Start datetime (default: yesterday)
        end_date: End datetime (default: now)

    Returns:
        DataFrame with columns: [datetime, price, volume, bid, ask, bid_vol, ask_vol]

    Raises:
        ConnectionError: If API call fails
    """
    if start_date is None:
        start_date = datetime.now() - timedelta(days=1)
    if end_date is None:
        end_date = datetime.now()

    logger.info(f"Fetching tick data for {contract} from {start_date} to {end_date}")

    try:
        ticks = api.ticks(contract, start_date, end_date)
        logger.info(f"Fetched {len(ticks)} ticks")

        # Convert to DataFrame
        tick_list = []
        for tick in ticks:
            tick_list.append({
                "datetime": tick.datetime,
                "price": tick.price,
                "volume": tick.volume,
                "bid": tick.bid_price if hasattr(tick, "bid_price") else np.nan,
                "ask": tick.ask_price if hasattr(tick, "ask_price") else np.nan,
                "bid_vol": tick.bid_volume if hasattr(tick, "bid_volume") else 0,
                "ask_vol": tick.ask_volume if hasattr(tick, "ask_volume") else 0,
            })

        df = pd.DataFrame(tick_list)
        df = df.sort_values("datetime").reset_index(drop=True)

        return df

    except Exception as e:
        logger.error(f"Failed to fetch tick data: {e}")
        raise ConnectionError(f"API error: {e}") from e


def get_daily_summary(
    ohlcv: pd.DataFrame, by: str = "date"
) -> pd.DataFrame:
    """Get daily or period summary from OHLCV data.

    Args:
        ohlcv: OHLCV DataFrame with datetime index
        by: Aggregation level ('date', 'week', 'month', 'year')

    Returns:
        Aggregated summary DataFrame
    """
    if isinstance(ohlcv.index, pd.DatetimeIndex):
        ohlcv = ohlcv.reset_index()

    date_col = "datetime"
    if by == "date":
        group_col = pd.to_datetime(ohlcv[date_col]).dt.date
    elif by == "week":
        group_col = pd.to_datetime(ohlcv[date_col]).dt.isocalendar().week
    elif by == "month":
        group_col = pd.to_datetime(ohlcv[date_col]).dt.to_period("M")
    elif by == "year":
        group_col = pd.to_datetime(ohlcv[date_col]).dt.year
    else:
        raise ValueError("by must be: 'date', 'week', 'month', or 'year'")

    summary = ohlcv.groupby(group_col).agg({
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
        "volume": "sum",
    })

    return summary


def load_trade_list(
    filepath: str, sep: str = ", ", encoding: str = "utf-8"
) -> pd.DataFrame:
    """Load trade list from CSV.

    Merged from AlgoTrading: get_trade_list() function.

    Args:
        filepath: Path to CSV file or directory containing trade files
        sep: Column separator
        encoding: File encoding

    Returns:
        DataFrame with trade data

    Raises:
        FileNotFoundError: If file or directory not found
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    if os.path.isdir(filepath):
        # Load all CSV files in directory and combine
        logger.info(f"Loading trade files from {filepath}")
        dfs = []
        for filename in os.listdir(filepath):
            if filename.endswith(".csv"):
                try:
                    df = pd.read_csv(
                        os.path.join(filepath, filename),
                        sep=sep,
                        dtype=str,
                        encoding=encoding,
                    )
                    df["strategy_name"] = filename[:-4]  # Remove .csv extension
                    dfs.append(df)
                    logger.debug(f"Loaded {filename}")
                except Exception as e:
                    logger.warning(f"Failed to load {filename}: {e}")

        if not dfs:
            raise ValueError(f"No CSV files found in {filepath}")

        data = pd.concat(dfs, ignore_index=True, sort=False)
    else:
        # Load single file
        data = pd.read_csv(filepath, sep=sep, dtype=str, encoding=encoding)

    # Clean column names (remove spaces)
    data.columns = data.columns.str.replace(" ", "")

    # Convert numeric columns
    numeric_columns = [
        "TradeNumber",
        "PosTradeSize",
        "MaxContracts",
        "EntryBar",
        "ExitBar",
        "HoldingBars",
        "HoldingTimes",
        "PnL",
        "MAE",
        "MFE",
        "EntryPrice",
        "ExitPrice",
    ]
    for col in numeric_columns:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")

    # Convert datetime columns
    datetime_columns = ["EntryDatetime", "ExitDatetime"]
    for col in datetime_columns:
        if col in data.columns:
            data[col] = pd.to_datetime(data[col], errors="coerce")

    logger.info(f"Loaded {len(data)} trades")
    return data
