## Algorithmic Trading Winning Strategies and Their Rationale, 2013, Ernest P. Chan — 未標示
**來源**: E:/書籍/Ernest P. Chan/Algorithmic Trading Winning Strategies and Their Rationale, 2013, Ernest P. Chan.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **ALGORITHMIC TRADING**
- **CHAPTER 1 Backtesting and Automated Execution**
  - The Importance of Backtesting
  - Common Pitfalls of Backtesting
  - Statistical Significance of Backtesting: Hypothesis Testing
  - When Not to Backtest a Strategy
  - Will a Backtest Be Predictive of Future Returns?
  - Choosing a Backtesting and Automated Execution Platform
- **CHAPTER 2 The Basics of Mean Reversion**
  - Mean Reversion and Stationarity
  - Cointegration
  - Pros and Cons of Mean-Reverting Strategies
- **CHAPTER 3 Implementing Mean Reversion Strategies**
  - Trading Pairs Using Price Spreads, Log Price Spreads, or Ratios
  - Bollinger Bands
  - Does Scaling-in Work?
  - Kalman Filter as Dynamic Linear Regression
  - Kalman Filter as Market-Making Model
  - The Danger of Data Errors
- **CHAPTER 4 Mean Reversion of Stocks and ETFs**
  - The Difficulties of Trading Stock Pairs
  - Trading ETF Pairs (and Triplets)
  - Intraday Mean Reversion: Buy-on-Gap Model
  - Arbitrage between an ETF and Its Component Stocks
  - Cross-Sectional Mean Reversion: A Linear Long-Short Model
- **CHAPTER 5 Mean Reversion of Currencies and Futures**
  - Trading Currency Cross-Rates
  - Rollover Interests in Currency Trading
  - Trading Futures Calendar Spread
  - Futures Intermarket Spreads
- **CHAPTER 6 Interday Momentum Strategies**
  - Tests for Time Series Momentum
  - Time Series Strategies
  - Extracting Roll Returns through Future versus ETF Arbitrage
  - Cross-Sectional Strategies
  - Pros and Cons of Momentum Strategies
- **CHAPTER 7 Intraday Momentum Strategies**
  - Opening Gap Strategy
  - News-Driven Momentum Strategy
  - Leveraged ETF Strategy
  - High-Frequency Strategies
- **CHAPTER 8 Risk Management**
  - Optimal Leverage
  - Constant Proportion Portfolio Insurance
  - Stop Loss
  - Risk Indicators
- **CONCLUSION**
- **ABOUT THE WEBSITE**

### TL;DR (≤120字)
本書屬於 algorithmic trading 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **演算法交易的邊際利潤來自執行細節** — 進出場時點、冰山單、VWAP/POV 切片,而非主策略
2. **策略衰退 (alpha decay) 是必然,持續研發管線是本質不是選項** — 單一策略 life cycle 常低於 2-3 年
3. **Latency 不是唯一賽道,穩定性與再現性才是散戶與機構都可 scale 的護城河**

### 可用戰術/策略

- 建立策略標準化介面與回測基建,把每個新策略的研發時間壓到 1-2 週
- 為每個 live 策略設定監控 (PnL/ drawdown/ trade frequency) 觸發自動下線閾值

### 盲點 / 反例 / 適用邊界

- 過度依賴歷史 backtest 而忽略線上資料源穩定性、訊號延遲、交易所規則變更

### 與 Edward 既有知識的連結

- 呼應零式原則 *meta_strategy_over_strategy* — 關注資金曲線與長期夏普、勝過單筆交易或單期回報
- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
