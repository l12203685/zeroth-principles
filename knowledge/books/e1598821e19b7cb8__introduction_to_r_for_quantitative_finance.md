## Introduction to R for Quantitative Finance — 未標示
**來源**: E:/書籍/Introduction to R for Quantitative Finance.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Credits**
- **About the Reviewers**
- **www.PacktPub.com**
- **Chapter 1: Time Series Analysis**
  - Working with time series data
  - Linear time series modeling and forecasting
  - Cointegration
  - Modeling volatility
  - Summary
- **Chapter 2: Portfolio Optimization**
  - Mean-Variance model
  - Solution concepts
  - Working with real data
  - Tangency portfolio and Capital Market Line
  - Noise in the covariance matrix
  - When variance is not enough
  - Summary
- **Chapter 3: Asset Pricing Models**
  - Capital Asset Pricing Model
  - Arbitrage Pricing Theory
  - Beta estimation
  - Model testing
  - Summary
- **Chapter 4: Fixed Income Securities**
  - Measuring market risk of fixed income securities
  - Immunization of fixed income portfolios
  - Pricing a convertible bond
  - Summary
- **Chapter 5: Estimating the Term Structure of Interest Rates**
  - The term structure of interest rates and related functions
  - The estimation problem
  - Estimation of the term structure by linear regression
  - Cubic spline regression
  - Applied R functions
  - Summary
- **Chapter 6: Derivatives Pricing**
  - The Black-Scholes model
  - The Cox-Ross-Rubinstein model
  - Connection between the two models
  - Greeks
  - Implied volatility
  - Summary
- **Chapter 7: Credit Risk Management**
  - Credit default models
  - Correlated defaults - the portfolio approach
  - Migration matrices
  - Getting started with credit scoring in R
  - Summary
- **Chapter 8: Extreme Value Theory**
  - Theoretical overview
  - Application - modeling insurance claims
  - Summary
- **Chapter 9: Financial Networks**
  - Representation, simulation, and visualization of financial networks
  - Analysis of networks' structure and detection of topology changes
  - Contribution to systemic risk - identification of SIFIs
  - Summary
- **Appendix: References**
  - Time series analysis
  - Portfolio optimization
  - Asset pricing
  - Fixed income securities
  - Estimating the term structure of interest rates
  - Derivatives Pricing
  - Credit risk management
  - Extreme value theory
  - Financial networks

### TL;DR (≤120字)
本書屬於 statistics evidence based 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **多次檢驗問題會偽造 alpha** — data mining 若不做 Bonferroni/BH 校正,幾乎任何「策略」都能在歷史上跑贏
2. **統計顯著 ≠ 經濟顯著** — t-stat 3.0 但年化超額 0.3% 在扣手續費後無法存活
3. **前瞻偏誤 (look-ahead bias) 在學術論文與商業回測都普遍** — 特別留意財報日、指數調整日的訊號重建

### 可用戰術/策略

- 採用 white's reality check / stepwise superior predictive ability 做多重檢驗修正
- 所有 backtest 引入交易成本、滑價、融資成本,再看 net Sharpe

### 盲點 / 反例 / 適用邊界

- 統計檢驗預設資料獨立,金融時序高度相關,block bootstrap / stationary bootstrap 才能貼近實際分布

### 與 Edward 既有知識的連結

- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
- 呼應零式原則 *derivative_over_level* — 關注變化率/拐點而非單期水準
