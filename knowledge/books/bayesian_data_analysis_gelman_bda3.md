## Bayesian Data Analysis 3e (BDA3) — Andrew Gelman, John B. Carlin et al.
**來源**: E:/書籍/[Andrew_Gelman.pdf, Andrew_Gelman,_John_B.pdf  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- **Part I Fundamentals (1-5)**：probability、single-parameter、multiparameter、asymptotics
- **Part II Models (6-10)**：model checking、posterior predictive、hierarchical、comparison
- **Part III Computation (11-13)**：MCMC basics、Gibbs、Metropolis-Hastings、HMC/Stan、VI
- **Part IV Regression (14-18)**：linear regression、GLM、hierarchical linear models、missing data
- **Part V Multivariate (19-22)**：mixture models、Dirichlet process、survival analysis、ordinal
- **Part VI Advanced (23-25)**：Gaussian processes、decision analysis、nonparametric Bayesian

### TL;DR (≤120字)
BDA3 是 applied Bayesian 的聖經。Gelman 團隊強調「計算實用主義 + 模型診斷」，不只數學推導。對交易者最寶貴是第 6-7（posterior predictive check）、第 9（hierarchical model）、第 11-13（MCMC/HMC/VI/Stan）。Hierarchical model 對「多資產 / 多策略共享參數」完美適配——每個資產有自己 β，又部分 shrink 向 global mean，避免過擬合稀少數據。

### 核心本質 (3-5 條)
1. **Bayesian = prior × likelihood ∝ posterior（本質，第 1-2 章）** — 一切 Bayesian 就是 p(θ|y) ∝ p(y|θ) p(θ)；prior 不是主觀偏見而是正則化。對交易者，prior 就是「先驗知識：Sharpe > 2 的策略極少見」。
2. **Hierarchical model = 部分 pooling（本質，第 5、9 章）** — 多組數據分享超參數；每組參數既有自己 estimate 又被 global mean 拉近。金融：30 檔股票共同分享「動能因子 β 均值」，個股 β 部分 shrink。
3. **Posterior predictive check 是模型診斷核心（本質，第 6 章）** — 從 posterior 抽 θ，再抽 y_rep；比較 y_rep 與 y 的 test statistic（min、max、skew）。判斷模型是否錯估 fat-tail。
4. **MCMC 診斷必不可少（本質，第 11-12 章）** — R-hat < 1.01、effective sample size > 1000、trace plot 無 trend。Stan 的 HMC + NUTS 比 Metropolis 快 10-100 倍且自動調步長。
5. **Weakly informative prior > flat prior（本質，第 2.8、5.7 節）** — Gelman 強烈建議對 log-scale 參數用 N(0, 1)（weakly informative）而非 flat；flat prior 在高維會把質量推到邊界（curse of dimensionality）。

### 可用戰術/策略
- **Hierarchical Sharpe**：對 30 個策略的 Sharpe 用 N(μ_global, τ²) 先驗；shrink 後的 post_mean 是下一期 allocation weight（James-Stein estimator）。
- **Dynamic linear model (DLM)**：β_t ~ β_{t-1} + ε；用 Kalman + MCMC 估計 β_t 分布，作 rolling beta 取代 rolling OLS。
- **Prior from literature**：對 momentum 因子 Sharpe 用 N(0.3, 0.1²)（Asness 等實證）；對新策略 Sharpe 用 N(0, 0.3²)。
- **Model comparison via LOO-CV**：用 `loo` R 套件計 expected log predictive density；ΔELPD > 4 視為顯著勝出。
- **PP check 驗 fat-tail**：比 y_rep 與 y 的 P99 tail quantile；若 y 的 tail 大於 y_rep 95% → 模型低估 tail → 加 Student-t likelihood。

### 盲點 / 反例 / 適用邊界
- **計算仍重**：full Bayesian 比 MLE 慢 100-1000 倍；秒級高頻不適用，日頻以下可用。
- **模型誤設仍會 garbage-in-garbage-out**：Bayesian 不救錯模型，只讓錯誤更確定化；PP check 是唯一防線。
- **金融非平穩性**：BDA3 大多 iid 假設，時間序列章節簡短；Edward 需搭 Harvey / West-Harrison 狀態空間。
- **高維會悶 MCMC**：變量 > 1000 MCMC 可能不收斂；需退 VI 或 normalizing flows。
- **中文資源少**：原書英文，中譯本繁中罕見；Stan 手冊是額外必讀。

### 與 Edward 既有知識的連結
- **對齊 ZP multi-strategy risk budget**：hierarchical model 直接應用於多策略 sharpe 估計；Edward 可在 `ZP/portfolio/bayesian_allocator.py` 實作。
- **延伸 Bayesian Methods in Finance (Rachev)**：Rachev 偏推導、Gelman 偏實作；Rachev + Stan 例子 = Edward 的黃金組合。
- **衝突點**：Gelman 反對 Jeffreys prior（他認為是「uninformative but wrong」）；Rachev 書多用 Jeffreys。Edward 實戰用 weakly informative。
- **可挖金礦**：第 6.3 graphical posterior predictive check 是「策略回測的下一代診斷」——不只看 Sharpe，看整個分布是否 realistic。
- **對接 McElreath Statistical Rethinking**：McElreath 入門、Gelman 進階；新手先 McElreath → 再 BDA3。
