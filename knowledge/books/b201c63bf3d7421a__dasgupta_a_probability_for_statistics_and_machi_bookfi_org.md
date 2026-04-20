## [DasGupta_A.]_Probability_for_statistics_and_machi(BookFi.org) — 未標示
**來源**: E:/書籍/[DasGupta_A.]_Probability_for_statistics_and_machi(BookFi.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Springer Texts in Statistics**
- **Probability for Statistics and Machine Learning**
- **ISBN 9781441996336**
  - Suggested Courses with Different Themes
- **Chapter 1 Review of Univariate Probability**
  - 1.1 Experiments and Sample Spaces
  - ... (18 more sections)
- **Chapter 2 Multivariate Discrete Distributions**
  - 2.1 Bivariate Joint Distributions and Expectations of Functions
  - ... (5 more sections)
- **Chapter 3 Multidimensional Densities**
  - 3.1 Joint Density Function and Its Role
  - ... (8 more sections)
- **Chapter 4 Advanced Distribution Theory**
  - 4.1 Convolutions and Examples
  - ... (7 more sections)
- **Chapter 5 Multivariate Normal and Related Distributions**
  - 5.1 Definition and Some Basic Properties
  - ... (5 more sections)
- **Chapter 6 Finite Sample Theory of Order Statistics and Extremes**
  - 6.1 Basic Distribution Theory
  - ... (6 more sections)
- **Chapter 7 Essential Asymptotics and Applications**
  - 7.1 Some Basic Notation and Convergence Concepts
  - ... (6 more sections)
- **Chapter 8 Characteristic Functions and Applications**
  - 8.1 Characteristic Functions of Standard Distributions
  - ... (9 more sections)
- **Chapter 9 Asymptotics of Extremes and Order Statistics**
  - 9.1 Central-Order Statistics
  - ... (2 more sections)
- **Chapter 10 Markov Chains and Applications**
  - 10.1 Notation and Basic Definitions
  - ... (6 more sections)
- **Chapter 11 Random Walks**
  - 11.1 Random Walk on the Cubic Lattice
  - ... (7 more sections)
- **Chapter 12 Brownian Motion and Gaussian Processes**
  - 12.1 Preview of Connections to the Random Walk
  - ... (7 more sections)
- **Chapter 13 Poisson Processes and Applications**
  - 13.1 Notation
  - ... (6 more sections)
- **Chapter 14 Discrete Time Martingales and Concentration Inequalities**
  - 14.1 Illustrative Examples and Applications in Statistics
  - ... (5 more sections)
- **Chapter 15 Probability Metrics**
  - 15.1 Standard Probability Metrics Useful in Statistics
  - ... (3 more sections)
- **Chapter 16 Empirical Processes and VC Theory**
  - 16.1 Basic Notation and Definitions
  - ... (5 more sections)
- **Chapter 17 Large Deviations**
  - 17.1 Large Deviations for Sample Means
  - ... (4 more sections)
- **Chapter 18 The Exponential Family and Statistical Applications**
  - 18.1 One-Parameter Exponential Family
  - ... (4 more sections)
- **Chapter 19 Simulation and Markov Chain Monte Carlo**
  - 19.1 The Ordinary Monte Carlo
  - ... (6 more sections)
- **Chapter 20 Useful Tools for Statistics and Machine Learning**
  - 20.1 The Bootstrap
  - ... (2 more sections)
- **Appendix A Symbols, Useful Formulas, and Normal Table**
  - A.1 Glossary of Symbols
  - ... (2 more sections)
- **Author Index**
- **Subject Index**

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
