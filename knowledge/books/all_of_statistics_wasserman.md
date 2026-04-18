## All of Statistics — Larry Wasserman
**來源**: E:/書籍/All of Statistics A Concise Course in Statistical Inference, Larry Wasserman.pdf  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- **Part I Probability (1-5)**：probability spaces、random variables、expectation、inequalities、convergence
- **Part II Statistical Inference (6-12)**：models、estimating CDF、parametric inference、hypothesis testing、Bayesian、statistical decision theory、simulation
- **Part III Statistical Models & Methods (13-24)**：linear/logistic regression、multivariate、inference about independence、CI for functions of parameters、directed graphs、undirected graphs、log-linear models、nonparametric curve estimation、smoothing、classification、stochastic processes、stimulation
- 附錄 Brief Review of Calculus, Analysis, Linear Algebra

### TL;DR (≤120字)
Wasserman 這本 *All of Statistics* 是 CMU 為 CS/ML 學生寫的「壓縮版」研究生統計，一本書覆蓋從機率到非參估計。比 Casella-Berger 快、比 Wooldridge 深、比 Bishop 簡略。對 ML 背景想補統計/Bayesian/因果的人最理想。對交易者：CS 出身想學 finance 前先把統計打底，Wasserman 400 頁 vs Casella-Berger 700 頁效率高。附帶圖形模型章是其他統計書罕見。

### 核心本質 (3-5 條)
1. **Sampling distribution 是 frequentist 核心（本質，第 8 章）** — θ̂ 是隨機變量（因為樣本隨機），其分布就是 sampling distribution。Confidence interval、hypothesis test 都從此出。
2. **Bootstrap 是分布未知時的救命稻草（本質，第 8.3 節）** — Empirical CDF 替代真實 CDF，re-sample with replacement 估計 θ̂ 的分布。比 asymptotic approximation 對小樣本更準。
3. **Hypothesis test 是 decision theory 的特例（本質，第 10、12 章）** — Type I/II error trade-off；Neyman-Pearson lemma 給最優 test。金融 Sharpe 顯著性 = 單尾 test for H0: μ=0。
4. **Bayesian ≠ subjective，僅是 prior/posterior 數學（本質，第 11 章）** — Wasserman 對 Bayesian 中立介紹，指出「objective Bayes」（Jeffreys, reference prior）與 frequentist 結論在 iid 時漸近一致。
5. **Nonparametric curve estimation（本質，第 20-21 章）** — 當不假設 parametric family，用 kernel/local polynomial/spline 估計 f(x)；bandwidth 選擇是關鍵 trade-off（bias-variance）。

### 可用戰術/策略
- **Bootstrap Sharpe CI**：對策略 5000 個 daily return bootstrap 10000 次，取 Sharpe 的 2.5/97.5 分位；若下界 > 0.5 視為顯著。
- **Permutation test for strategy overlap**：H0: 策略 A 與 B 收益無關；隨機置換 B 的 return，重算 correlation，計算 p-value。
- **Kernel density for return distribution**：直方圖對 tail 粗糙；用 Epanechnikov kernel, bandwidth via Silverman rule，得平滑 density 估計。
- **Chi-square for regime change**：把 return 分 Q1-Q5，檢驗 regime A vs B 的分位分布是否獨立；拒絕 → regime 有結構差異。
- **Jackknife bias correction**：對偏倚估計量（如樣本自相關）用 jackknife：θ̂_JK = n×θ̂ - (n-1)×θ̂_(-i) 平均。

### 盲點 / 反例 / 適用邊界
- **壓縮版**：每題薄薄一頁；深入需配 Casella-Berger 或 Ferguson。
- **時序僅第 23 章略提**：不是時序教材；金融 TS 需 Tsay/Hamilton。
- **ML 章輕**：classification/clustering 各一章，不深；需配 ESL/Bishop。
- **計算細節少**：書中公式為主，R/Python 實作需自行。
- **沒 causality**：因果推論完全不在；需 Pearl/Hernán 補。

### 與 Edward 既有知識的連結
- **對齊 ZP 統計基礎**：補足 CS/ML 出身的統計 gap；特別第 8 章 bootstrap、第 10 章 test 直接用於回測。
- **延伸 Bishop PRML**：Wasserman 先，Bishop 再；前者建立 frequentist 基礎，後者展開 Bayesian ML。
- **衝突點**：Wasserman 中立客觀；Gelman/McElreath 堅定 Bayesian。Edward 可中立派，任務導向選派。
- **可挖金礦**：第 8.3 節 bootstrap 的各種 variant（non-parametric、parametric、smooth）可直接成 ZP 策略檢定工具包。
- **對接 Efron-Tibshirani Bootstrap**：Efron 1993 原典更深；Wasserman 是教材級入門。
