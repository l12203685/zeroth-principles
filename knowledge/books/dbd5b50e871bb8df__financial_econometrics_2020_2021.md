## financial-econometrics-2020-2021 — 未標示
**來源**: E:/書籍/financial-econometrics-2020-2021.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Probability, Random Variables and Expectations**
  - Axiomatic Probability
  - Univariate Random Variables
  - Multivariate Random Variables
  - Expectations and Moments
- **Estimation, Inference, and Hypothesis Testing**
  - Estimation
  - Convergence and Limits for Random Variables
  - Properties of Estimators
  - Distribution Theory
  - Hypothesis Testing
  - The Bootstrap and Monte Carlo
  - Inference on Financial Data
- **Analysis of Cross-Sectional Data**
  - Model Description
  - Functional Form
  - Estimation
  - Assessing Fit
  - Assumptions
  - Small-Sample Properties of OLS estimators
  - Maximum Likelihood
  - Small-Sample Hypothesis Testing
  - Large-Sample Assumption
  - Large-Sample Properties
  - Large-Sample Hypothesis Testing
  - Violations of the Large-Sample Assumptions
  - Model Selection and Specification Checking
  - Machine Learning
  - Projection
  - Selected Proofs
- **Analysis of a Single Time Series**
  - Stochastic Processes
  - Stationarity, Ergodicity, and the Information Set
  - ARMA Models
  - Difference Equations
  - Data and Initial Estimates
  - Autocorrelations and Partial Autocorrelations
  - Estimation
  - Inference
  - Forecasting
  - Nonstationary Time Series
  - SARIMA Models
  - Filters
  - Nonlinear Models for Time-Series Analysis
  - Computing Autocovariance and Autocorrelations
- **Analysis of Multiple Time Series**
  - Vector Autoregressions
  - Companion Form
  - Empirical Examples
  - VAR forecasting
  - Estimation and Identification
  - Granger causality
  - Impulse Response Functions
  - Cointegration
  - Cross-sectional Regression with Time-series Data
  - Cointegration in a trivariate VAR
- **Generalized Method Of Moments (GMM)**
  - Classical Method of Moments
  - Examples
  - General Specification
  - Estimation
  - Asymptotic Properties
  - Covariance Estimation
  - Special Cases of GMM
  - Diagnostics
  - Parameter Inference
  - Two-Stage Estimation
  - Weak Identification
  - Considerations for using GMM
- **Univariate Volatility Modeling**
  - Why does volatility change?
  - ARCH Models
  - Estimation and Inference
  - GARCH-in-Mean
  - Alternative Distributional Assumptions
  - Model Building
  - Forecasting Volatility
  - Realized Variance
  - Implied Volatility and VIX
  - Kurtosis of an ARCH(1)
  - Kurtosis of a GARCH(1,1)
- **Value-at-Risk, Expected Shortfall and Density Forecasting**
  - Defining Risk
  - Value-at-Risk (VaR)
  - Conditional Value-at-Risk
  - Unconditional Value at Risk
  - Evaluating VaR models
  - Expected Shortfall
  - Density Forecasting
  - Coherent Risk Measures
- **Multivariate Volatility, Dependence and Copulas**
  - Introduction
  - Preliminaries
  - Simple Models of Multivariate Volatility
  - Multivariate ARCH Models
  - Realized Covariance
  - Measuring Dependence
  - Copulas
  - Bootstrap Standard Errors

### TL;DR (≤120字)
本書屬於 ml for finance 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **金融時序資料是非平穩的** — 機器學習的 i.i.d. 假設在市場失效,這是所有金融 ML 失靈的本質原因
2. **樣本外績效下降是常態不是異常** — 模型週期性重訓、特徵漂移監測應視為系統常規模組,而非意外處理
3. **訊號強度 vs. 成本** — ML 模型發現的 alpha 往往小於 bid-ask 與手續費,backtest 必須內含實務成本

### 可用戰術/策略

- 使用 walk-forward validation + purged k-fold 防止時序洩漏
- ensemble 多個弱訊號而非單一強訊號,降低 overfitting 風險

### 盲點 / 反例 / 適用邊界

- ML 模型在結構性變化 (央行政策轉向、市場微結構改變) 下失效,必須有 regime detection 做護欄

### 與 Edward 既有知識的連結

- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
- 呼應零式原則 *information_asymmetry_action* — 有邊際資訊優勢才進場
