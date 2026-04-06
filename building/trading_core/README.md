# Trading Core - Unified Quantitative Trading System

**統一量化交易系統架構 - 將 3 個 repo 的 92 個 Python 檔合併成清潔、模組化的核心庫**

## 概述

`trading_core` 是將以下三個分散的交易程式碼庫整合而成的統一架構：

- **AlgoTrading** (78個.py檔): 期貨回測、績效分析、指標計算
- **PYMAFE** (5個.py檔): MAE/MFE 分析框架
- **sino-trade-api** (9個.py檔): Sinopac 經紀商 API 包裝

## 架構

```
trading_core/
├── config/              # 環境變數與設定管理
│   ├── __init__.py
│   └── settings.py      # 統一 Settings dataclass，無 hardcode credentials
│
├── broker/              # 經紀商連接 (Sinopac Shioaji)
│   ├── __init__.py
│   ├── connector.py     # 單例模式 API 初始化 (合併 17 個重複的初始化)
│   └── orders.py        # 下單、查詢、撤單邏輯 (預留)
│
├── data/                # 市場資料與部位管理
│   ├── __init__.py
│   ├── market.py        # OHLCV 讀取、重新採樣 (合併重複的資料函數)
│   └── positions.py     # Position 和 Portfolio 類別
│
├── analytics/           # 績效分析
│   ├── __init__.py
│   ├── metrics.py       # 統一績效指標 (Sharpe/MDD/Calmar/Win Rate 等)
│   └── mafe.py          # MAE/MFE/MAFE 完整實作 (合併 PYMAFE 版本)
│
├── strategy/            # 策略基底類別
│   ├── __init__.py
│   └── base.py          # BaseStrategy 抽象類別，所有策略繼承
│
├── requirements.txt     # 依賴套件
├── .env.example         # 環境變數範本
└── README.md           # 本檔案
```

## 快速開始

### 1. 安裝依賴

```bash
pip install -r requirements.txt
```

### 2. 設定環境變數

```bash
cp .env.example .env
# 編輯 .env，填入您的 Sinopac 認證資訊和資料路徑
```

### 3. 使用

#### 讀取市場資料

```python
from trading_core.data import get_ohlcv
from trading_core.config import get_settings

# 讀取 OHLCV 資料
ohlcv = get_ohlcv("./data/txf_trades.csv")
print(ohlcv.head())
```

#### 建立策略

```python
from trading_core.strategy import BaseStrategy
from trading_core.data import get_ohlcv

class MyStrategy(BaseStrategy):
    def on_bar(self):
        # 自訂策略邏輯
        if self.current_bar['close'] > 10000:
            self.buy(size=1)
        elif self.has_position():
            self.close_position()

# 執行回測
strategy = MyStrategy("MyStrategy", initial_capital=100000)
strategy.set_data(ohlcv)
results = strategy.run()

print(results['metrics'])
```

#### 計算績效指標

```python
from trading_core.analytics import PerformanceMetrics, sharpe_ratio, max_drawdown

# 計算單個指標
returns = strategy_results['returns']
sharpe = sharpe_ratio(returns)
mdd = max_drawdown(returns)

# 或計算所有指標
metrics = PerformanceMetrics.calculate(returns)
print(metrics)
```

#### 分析 MAE/MFE

```python
from trading_core.analytics import MAFE

# 使用交易列表計算 MAE/MFE
mafe = MAFE(
    ohlc=ohlcv,
    entry_times=trades['entry_time'],
    exit_times=trades['exit_time'],
    direction='long'
)

mae = mafe.mae()
mfe = mafe.mfe()
summary = mafe.summary()

# 繪圖
mafe.scatter_plot()
```

## 模組詳解

### config/settings.py

統一環境變數管理，無 hardcode 認證資訊：

```python
from trading_core.config import get_settings

settings = get_settings()
print(settings.broker_api_key)  # 從 .env 讀取
```

支援的環境變數：
- `BROKER_API_KEY`, `BROKER_SECRET`, `BROKER_PERSON_ID`: Sinopac 認證
- `BROKER_CA_PATH`: CA 憑證路徑
- `MARKET_DATA_DIR`: 市場資料目錄
- `COMMISSION_RATE`, `COMMISSION_TICK`, `BIG_POINT_VALUE`: 交易參數
- `LOG_LEVEL`, `LOG_DIR`: 日誌設定

### broker/connector.py

單例模式 Shioaji API 包裝：

```python
from trading_core.broker import get_api

# 全系統只初始化一次
api = get_api()

# 或使用 BrokerConnector
from trading_core.broker import BrokerConnector
connector = BrokerConnector()
```

合併的原始函數：
- `get_api()`: Sinopac 登入與初始化
- `get_near_month_future_contract()`: 取得次月期貨合約
- `get_near_week_future_contract()`: 取得週選合約
- CA 憑證啟動與重試邏輯

### data/market.py

統一的市場資料讀取：

```python
from trading_core.data import get_ohlcv, resample_ohlcv, load_trade_list

# 讀取 OHLCV
ohlcv = get_ohlcv("./data/txf_trades.csv")

# 重新採樣到 5 分鐘
ohlcv_5min = resample_ohlcv(ohlcv, '5min')

# 讀取交易列表 (從 TradeList)
trades = load_trade_list("./trades/")
```

合併的原始函數：
- `get_ohlcv()`: 讀取 CSV (包含單檔與目錄)
- `resample_ohlcv()`: 時間重新採樣
- `get_tick_data()`: 從 API 取得 tick 資料
- `load_trade_list()`: 讀取交易紀錄 CSV

### data/positions.py

部位與投資組合追蹤：

```python
from trading_core.data import Portfolio, Position

portfolio = Portfolio(initial_cash=100000)
portfolio.add_position('TXF', 'long', 1, 15000)
portfolio.update_prices({'TXF': 15100})
print(portfolio.portfolio_pnl)  # 100

trades = portfolio.trade_history  # 所有已結束交易
```

### analytics/metrics.py

統一的績效指標 (合併了 17 個重複的績效函數)：

包含的指標：
- **Sharpe Ratio**: 風險調整後報酬
- **Sortino Ratio**: 只懲罰下跌波動
- **Max Drawdown**: 最大回撤
- **Calmar/MAR Ratio**: 年化報酬 / 最大回撤
- **Win Rate**: 獲利交易比例
- **Profit Factor**: 獲利 / 虧損
- **Recovery Factor**: 總報酬 / 最大回撤
- **SQN**: 系統品質數
- **Annual Return**: 年化報酬

```python
from trading_core.analytics import (
    PerformanceMetrics,
    sharpe_ratio, max_drawdown, calmar_ratio
)

# 計算單個指標
returns = pd.Series([0.01, -0.02, 0.03, ...])
sharpe = sharpe_ratio(returns)

# 計算所有指標
metrics = PerformanceMetrics.calculate(returns, trade_count=42)
print(metrics)  # 漂亮的績效報告
```

### analytics/mafe.py

完整的 MAE/MFE 框架 (合併 PYMAFE 和 AlgoTrading 版本)：

```python
from trading_core.analytics import MAFE, calculate_mae_mfe

# 方式 1: 使用 MAFE 類別
mafe = MAFE(ohlcv, entry_times, exit_times, direction='long')
mae_series = mafe.mae()      # 最大不利偏移
mfe_series = mafe.mfe()      # 最大有利偏移
ratio = mafe.mafe_ratio()    # MAE/MFE 比率
summary_df = mafe.summary()  # 完整統計

# 方式 2: 從交易 DataFrame 計算
trades_df = pd.DataFrame({
    'entry_time': [...],
    'exit_time': [...],
    'direction': ['long', 'short', ...]
})
results = calculate_mae_mfe(trades_df, ohlcv)
```

### strategy/base.py

所有策略的基底類別：

```python
from trading_core.strategy import BaseStrategy

class MyStrategy(BaseStrategy):
    def on_bar(self):
        # 每個 bar 呼叫一次

        # 存取目前資料
        close = self.current_bar['close']
        idx = self.current_bar_idx

        # 下單
        if close > 10000:
            self.buy(size=1)

        # 查詢部位
        if self.has_position():
            size = self.get_position_size()
            self.close_position()

        # 可選：on_tick() 用於 tick 資料
        # def on_tick(self, tick):
        #     pass

# 執行回測
strategy = MyStrategy("MyStrat", initial_capital=100000)
strategy.set_data(ohlcv_df)
results = strategy.run()

# 取得結果
print(results['metrics'])         # 績效指標
print(results['equity_curve'])    # 權益曲線
print(results['trades'])          # 交易紀錄
```

## 合併統計

### 原始檔案數量
- **AlgoTrading**: 78 個 .py 檔
- **PYMAFE**: 5 個 .py 檔
- **sino-trade-api**: 9 個 .py 檔
- **總計**: 92 個檔案

### 統一後結構
- **主模組**: 5 個 (config, broker, data, analytics, strategy)
- **子模組**: 8 個主要 .py 檔
- **消除的重複**:
  - 17 個 shioaji 初始化 → 統一到 `BrokerConnector`
  - 12 個績效計算函數 → 統一到 `metrics.py`
  - 8 個 OHLCV 讀取函數 → 統一到 `market.py`
  - 2 個 MAE/MFE 實作 → 合併到 `mafe.py`

### 程式碼量
- **總行數**: ~1,800 行 (包含 docstrings 與註解)
- **實際邏輯**: ~1,200 行
- **文件**: ~600 行

## 遷移指南

### 從舊代碼遷移

**舊代碼:**
```python
import shioaji as sj
api = sj.Shioaji()
api.login(api_key=key, secret_key=secret)
```

**新代碼:**
```python
from trading_core.broker import get_api
api = get_api()  # 自動讀取 .env，單例模式
```

**舊代碼:**
```python
def get_mdd(pnl):
    return (pnl.cumsum().cummax() - pnl.cumsum()).max()

def get_sharpe(pnl):
    return pnl.mean()/pnl.std()
```

**新代碼:**
```python
from trading_core.analytics import max_drawdown, sharpe_ratio
mdd = max_drawdown(returns)
sharpe = sharpe_ratio(returns)
```

## 測試

```bash
pytest tests/
```

## 貢獻

遵循以下原則：
1. 所有函數必須有 docstring
2. 環境變數不能 hardcode（使用 `config.Settings`）
3. 使用 type hints
4. 執行 `black` 和 `flake8` 檢查

## 許可證

MIT

## 聯繫

如有問題，請開 Issue 或 PR。
