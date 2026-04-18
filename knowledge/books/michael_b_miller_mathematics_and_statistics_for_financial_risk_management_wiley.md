## Mathematics and Statistics for Financial Risk Management (2nd Ed) — Michael B. Miller
**來源**: E:/書籍/Michael B. Miller-Mathematics and Statistics for Financial Risk Management-Wiley (2013).pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Ch 1** Some Basic Math (logarithms, log returns, compounding, Taylor series)
- **Ch 2** Probabilities (discrete/continuous RVs, mutually exclusive, independent, conditional)
- **Ch 3** Basic Statistics (averages, expectations, variance, skew/kurtosis, coskewness)
- **Ch 4** Distributions (uniform, Bernoulli, binomial, Poisson, normal, lognormal, student-t, chi-square, F, triangular, mixture)
- **Ch 5** Multivariate Distributions and Copulas
- **Ch 6** Bayesian Analysis (Bayes' theorem, Bayes vs Frequentists, priors, MCMC basics)
- **Ch 7** Hypothesis Testing & Confidence Intervals
- **Ch 8** Matrix Algebra (notation, operations, transition matrices, eigen)
- **Ch 9** Vector Spaces (orthogonality, rotation, basis, projection)
- **Ch 10** Linear Regression (single + multi regressor, factor analysis)
- **Ch 11** Time Series Models (random walks, drift-diffusion, AR/MA/ARMA, unit root, seasonality)
- **Ch 12** Decay Factors (EWMA, weighted least squares, realized vol)
- **Appendices**: Binary numbers, Taylor expansions, Vector spaces, Greek alphabet, Abbreviations, Copulas
- **Answers** (sample problems 12 chapters)

### TL;DR (≤120字)
Michael Miller(前 Goldman Sachs、現 Northstar Risk)寫的實務導向 risk management 數學書。特色是「短、聚焦、直接可用」— 每個章節以實際 risk manager 日常工具為導向,避免學院派長篇證明。比 Wasserman《All of Statistics》更實務,比 Jorion FRM 更嚴謹,是 buy-side risk manager 的首選 self-study 書。

### 核心本質 (3-5 條, 每條 50-120字)
1. **Log returns ≠ simple returns,在多期複合時兩者可加性不同** — Ch1 重申 pedestrian but crucial:log returns (連續複利) 跨期可加;simple returns 不可加。Risk 建模全部用 log returns,交易績效報告則偏 simple returns — 混用會產出錯誤 vol 估計。
2. **Skewness 與 kurtosis 是 "beyond normal" 的最基本二階 extension** — Ch3 強調:純 μ 和 σ² 不足以描述金融報酬分布;skew (不對稱) + kurtosis (厚尾) 提供更完整描述。Jarque-Bera test 是最常用的正態性拒絕檢驗。
3. **Copulas 是 multivariate dependence 結構的唯一嚴謹工具** — Ch5 核心:Gaussian copula、t-copula、Archimedean copula (Clayton、Gumbel、Frank) 提供不同 tail dependence 結構。2008 年 CDO 危機 = 信錯 Gaussian copula 的教訓。實務上金融危機情境優先用 t-copula。
4. **EWMA (Exponentially Weighted Moving Average) vol 是實務 GARCH 的簡化版** — Ch12:σ²_t = λ σ²_{t-1} + (1-λ) r²_{t-1};λ = 0.94 (RiskMetrics 標準)。實作單行程式碼,捕捉 vol clustering 大部分效果。GARCH 是 strict 升級但多數場景 EWMA 夠用。
5. **Factor analysis 是多資產 risk decomposition 的核心技法** — Ch10.3:將多資產報酬分解為 systematic factors (market, size, value, momentum) + residual;此分解讓 risk manager 能知道「組合到底在什麼 factor 上暴露」,而非只看個股。

### 可用戰術/策略
- **EWMA volatility estimator 作為 daily risk monitor** — λ=0.94 單行式計算每個策略/資產的 daily volatility;超過歷史中位 2 倍 = 啟動倉位減半警示。B1 系統此模組 20 行 Python 完成。
- **Jarque-Bera + QQ plot 作為 "返回是否正態" 健康檢查** — 每週對策略 daily PnL 做 JB test;若 p < 0.01 拒絕正態,Gaussian VaR 不可信,須切換到 historical 或 EVT VaR。
- **Bayesian update of strategy parameters (Ch6)** — 策略的 expected α 以歷史績效為 prior;最近 X 日實績為 likelihood;posterior α 作為 live strategy 的 confidence level,驅動 scale-up / scale-down。
- **Copula-based portfolio tail risk simulation** — 用 t-copula (df=5-10) 搭配 EVT-fit marginals,Monte Carlo 生成多資產 joint extreme scenarios;用於 stress test + tail hedge design。
- **PCA / factor decomposition for B1 multi-asset system** — Ch10 方法:對策略/資產回報矩陣做 PCA,主成份對應 latent factors;用於 "真正獨立 alpha sources" 識別(去除前 2-3 主成份後的 residual)。

### 盲點 / 反例 / 適用邊界
- **實務偏向 sell-side / risk manager 視角** — alpha generation 討論少;若主要是買方策略研發,需補 López de Prado《Advances in Financial ML》。
- **Bayesian 章節 (Ch6) 入門級** — MCMC、hierarchical model、variational inference 等 modern Bayesian 工具需另讀 Gelman BDA、Kruschke《Doing Bayesian Data Analysis》。
- **時序章節 (Ch11) 偏簡** — 實務 AR(p) 選擇、stationarity 檢測 (ADF、KPSS)、structural breaks 等需補 Hamilton《Time Series Analysis》。
- **無 Python/R code implementation** — 理論清晰但 code 要自寫;與 Benninga Excel 版互補(概念相同但實作不同)。

### 與 Edward 既有知識的連結
- 補充 Wasserman (純統計)、Jorion FRM (風控業務流程)、Benninga (Excel 實作) 三者;Miller 剛好填 "嚴謹但實務導向" 的 niche。
- 對應 `risk_control_four_layers`:Ch5 Copula + Ch12 EWMA + Ch6 Bayesian 可作為四層架構的具體數學組件。
- 連結 `backtest_methodology`:Ch7 hypothesis testing + Ch11 time series 檢驗是回測結果信度的理論基礎。
- 對 B1 自營交易系統的貢獻:此書是 risk module 設計的 practical reference;建議新 risk engineer 首讀書籍之一。
