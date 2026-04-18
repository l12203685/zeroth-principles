## All of Statistics: A Concise Course in Statistical Inference — Larry Wasserman
**來源**: E:/書籍/All of Statistics A Concise Course in Statistical Inference, Larry Wasserman.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Statistics/Data Mining Dictionary** (術語對照表 for CS vs Statistician)
- **Part I Probability**
  - Ch 1 Probability
  - Ch 2 Random Variables
  - Ch 3 Expectation
  - Ch 4 Inequalities (Markov, Chebyshev, Hoeffding)
  - Ch 5 Convergence of RVs
- **Part II Statistical Inference**
  - Ch 6 Models, Statistical Inference, Learning
  - Ch 7 Estimating the CDF & Statistical Functionals
  - Ch 8 The Bootstrap
  - Ch 9 Parametric Inference (MLE, Delta method)
  - Ch 10 Hypothesis Testing & p-values
  - Ch 11 Bayesian Inference
  - Ch 12 Statistical Decision Theory
- **Part III Statistical Models and Methods**
  - Ch 13 Linear Regression
  - Ch 14 Multivariate Models
  - Ch 15 Inference about Independence
  - Ch 16 Causal Inference
  - Ch 17 Directed Graphical Models (Bayes nets)
  - Ch 18 Undirected Graphs
  - Ch 19 Log-linear Models
  - Ch 20 Nonparametric Curve Estimation (Density + Kernel + Splines)
  - Ch 21 Smoothing using Orthogonal Functions (wavelets)
  - Ch 22 Classification (logistic, LDA, SVM, trees)
  - Ch 23 Probability Redux (Stochastic Processes, Markov chains)
  - Ch 24 Simulation Methods (MC, MCMC, Gibbs)
- **ERRATA** for both printings

### TL;DR (≤120字)
CMU 機率統計的濃縮速成本:從機率論 → 統計推斷 → 現代 data mining 方法一氣呵成。特色是「拋棄教條 counting methods、把 bootstrap / 非參數 / graphical models 放前面」,為 CS / ML 背景讀者設計。是 quant 轉職 ML 或 ML 工程師補統計的 best single book。

### 核心本質 (3-5 條, 每條 50-120字)
1. **機率 vs 推斷是逆問題** — 機率:給定 data-generating process,問 outcome 分布。推斷:給定 outcomes,推 DGP。實務中做 backtest 是機率(已知 strategy,算分布),做 parameter estimation 是推斷(未知真 α,從資料推測)。兩者的混淆是策略工程師最常犯錯誤。
2. **Bootstrap 是「無分布假設的推斷萬靈丹」** — Ch8 明確:當分布未知時,從樣本重抽樣 n 次,計算統計量分布 — 即得近似的標準誤/信心區間。B1 回測的 Sharpe ratio confidence interval 用 bootstrap 比 Normal 假設更穩健,especially 樣本小 或 分布 fat-tailed。
3. **Hypothesis testing 的 p-value 不是「我的發現正確的機率」** — Ch10 反覆澄清:p-value 是「若 H0 為真,觀察到此結果或更極端的機率」。Multiple testing (如 backtest 100 個策略取最好) 會使 p-value 失真;需 Bonferroni / FDR 校正。此與 López de Prado 的 Deflated Sharpe 同源。
4. **MLE 是黃金標準但非總是最優** — Ch9 指出 MLE 有漸進正態、效率 (Cramér-Rao bound) 特性;但小樣本下偏差大、對 model mis-specification 敏感。Bayesian 推斷 (Ch11) 是補充工具,尤其當有 informative prior。
5. **Causal inference 不等於 correlation** — Ch16 強調:A 相關 B 可由 A→B、B→A、共同 confounder C、或 collider 偏誤產生。Granger causality、RCT、instrumental variable、DAG-based do-calculus 是從相關到因果的標準工具。回測中「這個 signal 預測報酬」≠「此 signal 造成報酬」。

### 可用戰術/策略
- **Bootstrap confidence intervals for backtest metrics** — Sharpe ratio / Max DD / Win rate 用 bootstrap 取 95% CI,避免「one-point Sharpe=1.5 就上線」的陷阱;B1 回測 pipeline 必要模組。Python <30 行以 numpy resample 實現。
- **Hoeffding / Chebyshev 尾部上界作為風險 rule-of-thumb** — Ch4 不等式給出「無論真分布如何,X 偏離均值 k 個標準差的機率不超過 1/k²」之類上界;當尾部分布未知時,用不等式保守估風險預算,比假設正態更安全。
- **Nonparametric density estimation (Ch20) 作為 regime detection tool** — KDE 估計 return distribution 的當前形狀,若發現 bimodal / heavy tail 變化 = regime shift signal,觸發策略參數自適應。
- **Graphical models (Ch17-18) 作為多資產相依結構建模** — Bayes net / MRF 比單純 correlation matrix 更能捕捉 conditional independence,在 portfolio 層次用於辨認「真正獨立的 alpha sources」。

### 盲點 / 反例 / 適用邊界
- **偏 IID 假設,對時間序列依賴結構討論不深** — Ch23 只簡略提 Markov chain;時序數據(strategies 回測最重要的資料類型)需另讀 Hamilton《Time Series Analysis》或 Tsay《Analysis of Financial Time Series》。
- **對 high-dimensional stats (p >> n) 覆蓋有限** — 現代 ML 常遇到 thousands of features;需補 Bühlmann-van de Geer《Statistics for High-Dimensional Data》或 Hastie-Tibshirani《Elements of Statistical Learning》。
- **計算統計 (MCMC、Variational Inference) 覆蓋淺** — Ch24 只給 single-chain MH/Gibbs;Bayesian workflow (PyMC、Stan) 需另學 Gelman《Bayesian Data Analysis》。
- **Causal inference (Ch16) 為 introductory 級** — Pearl 的 do-calculus、counterfactual reasoning 需另讀 Pearl《Causality》或 Hernán《Causal Inference》。

### 與 Edward 既有知識的連結
- 直接支撐 `backtest_methodology`:Ch8 Bootstrap 是回測不確定性量化工具;Ch10 multiple testing 校正直接對應「多策略 backtest 的 Type I error inflation」問題。
- 對應零式第 1 條 `derivative_over_level`:Ch13 regression 的殘差分析 = 提取 "excess return over baseline" 的統計過程,本質是 derivative (change over benchmark)。
- 連結 `information_asymmetry_action`:Ch11 Bayesian inference 提供「prior → posterior」框架,當你有 proprietary information 時,Bayes 更新是最佳資訊整合方式。
- 對 B1 自營交易系統的貢獻:所有 signal research、parameter estimation、risk model fitting 都需此書的統計基礎;建議作為工程師培訓的 prerequisite 文本。
