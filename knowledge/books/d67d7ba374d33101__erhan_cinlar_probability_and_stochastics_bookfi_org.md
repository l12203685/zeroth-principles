## [Erhan_Cinlar]_Probability_and_Stochastics(BookFi.org) — 未標示
**來源**: E:/書籍/[Erhan_Cinlar]_Probability_and_Stochastics(BookFi.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Graduate Texts in Mathematics 261**
- **Probability and Stochastics**
- **ISBN 9780387878584**
- **Frequently Used Notation**
- **Chapter I: Measure and Integration**
  - 1 Measurable Spaces
  - 2 Measurable Functions
  - 3 Measures
  - 4 Integration
  - 5 Transforms and Indefinite Integrals
  - 6 Kernels and Product Spaces
- **Chapter II: Probability Spaces**
  - 1 Probability Spaces and Random Variables
  - 2 Expectations
  - 3 Lp-spaces and Uniform Integrability
  - 4 Information and Determinability
  - 5 Independence
- **Chapter III: Convergence**
  - 1 Convergence of Real Sequences
  - 2 Almost Sure Convergence
  - 3 Convergence in Probability
  - 4 Convergence in Lp
  - 5 Weak Convergence
  - 6 Laws of Large Numbers
  - 7 Convergence of Series
  - 8 Central Limits
- **Chapter IV: Conditioning**
  - 1 Conditional Expectations
  - 2 Conditional Probabilities and Distributions
  - 3 Conditional Independence
  - 4 Construction of Probability Spaces
  - 5 Special Constructions
- **Chapter V: Martingales and Stochastics**
  - 1 Filtrations and Stopping Times
  - 2 Martingales
  - 3 Martingale Transformations and Maxima
  - 4 Martingale Convergence
  - 5 Martingales in Continuous Time
  - 6 Martingale Characterizations for Wiener and Poisson
  - 7 Standard Filtrations and Modifications of Martingales
- **Chapter VI: Poisson Random Measures**
  - 1 Random Measures
  - 2 Poisson Random Measures
  - 3 Transformations
  - 4 Additive Random Measures and Lévy Processes
  - 5 Poisson Processes
  - 6 Poisson Integrals and Self-exciting Processes
- **Chapter VII: L´evy Processes**
  - 1 Introduction
  - 2 Stable Processes
  - 3 Lévy Processes on Standard Settings
  - 4 Characterizations for Wiener and Poisson
  - 5 Itô-Lévy Decomposition
  - 6 Subordination
  - 7 Increasing Lévy Processes
- **Chapter VIII: Brownian Motion**
  - 1 Introduction
  - 2 Hitting Times and Recurrence Times
  - 3 Hitting Times and Running Maximum
  - 4 Wiener and its Maximum
  - 5 Zeros, Local Times
  - 6 Excursions
  - 7 Path Properties
  - 8 Existence
- **Chapter IX: Markov Processes**
  - 1 Markov Property
  - 2 Itô Diffusions
  - 3 Jump-Diffusions
  - 4 Markov Systems
  - 5 Hunt Processes
  - 6 Potentials and Excessive Functions
  - 7 Appendix: Stochastic Integration
- **Notes and Comments**

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
- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
