## Ruey S. Tsay-An Introduction to Analysis of Financial Data with R — Wiley (2012)
**來源**: E:/書籍/Ruey S. Tsay-An Introduction to Analysis of Financial Data with R-Wiley (2012).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1: Financial Data and Their Properties**
  - 1.1 Asset Returns
  - 1.2 Bond Yields and Prices
  - 1.3 Implied Volatility
  - 1.4 R Packages and Demonstrations
  - 1.5 Examples of Financial Data
  - 1.6 Distributional Properties of Returns
  - 1.7 Visualization of Financial Data
  - 1.8 Some Statistical Distributions
  - Exercises
- **2: Linear Models for Financial Time Series**
  - 2.1 Stationarity
  - 2.2 Correlation and Autocorrelation Function
  - 2.3 White Noise and Linear Time Series
  - 2.4 Simple Autoregressive Models
  - 2.5 Simple Moving Average Models
  - 2.6 Simple Arma Models
  - 2.7 Unit-root Nonstationarity
  - 2.8 Exponential Smoothing
  - 2.9 Seasonal Models
  - 2.10 Regression Models with Time Series Errors
  - 2.11 Long-memory Models
  - 2.12 Model Comparison and Averaging
  - Exercises
- **3: Case Studies of Linear Time Series**
  - 3.1 Weekly Regular Gasoline Price
  - 3.2 Global Temperature Anomalies
  - 3.3 Us Monthly Unemployment Rates
  - Exercises
- **4: Asset Volatility and Volatility Models**
  - 4.1 Characteristics of Volatility
  - 4.2 Structure of a Model
  - 4.3 Model Building
  - 4.4 Testing for ARCH Effect
  - 4.5 The Arch Model
  - 4.6 the Garch Model
  - 4.7 The Integrated Garch Model
  - 4.8 The Garch-M Model
  - 4.9 The Exponential Garch Model
  - 4.10 The Threshold Garch Model
  - 4.11 Asymmetric Power Arch Models
  - 4.12 Nonsymmetric Garch Model
  - 4.13 The Stochastic Volatility Model
  - 4.14 Long-memory Stochastic Volatility Models
  - 4.15 Alternative Approaches
  - Exercises
- **5: Applications of Volatility Models**
  - 5.1 Garch Volatility Term Structure
  - 5.2 Option Pricing and Hedging
  - 5.3 Time-varying Correlations and Betas
  - 5.4 Minimum Variance Portfolios
  - 5.5 Prediction
  - Exercises
- **6: High Frequency Financial Data**
  - 6.1 Nonsynchronous Trading
  - 6.2 Bid-ask Spread of Trading Prices
  - 6.3 Empirical Characteristics of Trading Data
  - 6.4 Models for Price Changes
  - 6.5 Duration Models
  - 6.6 Realized Volatility
  - Appendix A: Some Probability Distributions
  - Appendix B: Hazard Function
  - Exercises
- **7: Value at Risk**
  - 7.1 Risk Measure and Coherence
  - 7.2 Remarks on Calculating Risk Measures
  - 7.3 Riskmetrics
  - 7.4 an Econometric Approach
  - 7.5 Quantile Estimation
  - 7.6 Extreme Value Theory
  - 7.7 an Extreme Value Approach to Var
  - 7.8 Peaks over Thresholds
  - 7.9 The Stationary Loss Processes
  - Exercises

### TL;DR (≤120字)
本書屬於 options volatility 範疇,作者 Wiley (2012) 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **波動率是選擇權定價的核心變量** — 方向性預測失敗時,波動率結構 (ATM/IV skew/term structure) 仍可創造 +EV 機會,這是本質而非戰術
2. **Greeks 是部位面的座標軸** — 任何 payoff 都可以分解為 delta/gamma/vega/theta 的組合,這讓風險管理從「個別部位」升級為「組合相對曝險」
3. **波動率回歸均值是經驗命題,非數學恆等式** — 做 long vol 或 short vol 必須結合結構性事件與資金面,否則長期 short vol 即撿銅板在推土機前

### 可用戰術/策略

- 當 IV rank 高於歷史 80 分位且事件已過,考慮 short iron condor / short strangle,控制 vega 曝險
- 用 calendar spread 捕捉 term structure 扭曲 (近月 IV 高於遠月),對沖市場方向

### 盲點 / 反例 / 適用邊界

- 選擇權策略高度依賴流動性與 bid-ask spread;台指 TXO 週選以外、個股選擇權與期貨選擇權的交易成本可能吞掉理論 edge

### 與 Edward 既有知識的連結

- 呼應零式原則 *derivative_over_level* — 關注變化率/拐點而非單期水準
- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
