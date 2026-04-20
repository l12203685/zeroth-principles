## Probability and Measure_Patrick Billingsley — 未標示
**來源**: E:/書籍/Probability and Measure_Patrick Billingsley.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **PROBABILITY AND MEASURE, 3RD ED.**
- **Chapter 1. Probability**
  - 1. Borel's Normal Number Theorem
  - 2. Probability Measures
  - 3. Existence and Extension
  - 4. Denumerable Probabilities
  - 5. Simple Random Variables
  - 6. The Law of Large Numbers
  - 7. Gambling Systems
  - 8. Markov Chains
  - 9. Large Deviations and the Law of the Iterated Logarithm*
- **Chapter 2. Measure**
  - 10. General Measures
  - 11. Outer Measure
  - 12. Measures in Euclidean Space
  - 13. Measurable Functions and Mappings
  - 14. Distribution Functions
- **Chapter 3. Integration**
  - 15. The Integral
  - 16. Properties of the Integral
  - 17. The Integral with Respect to Lebesgue Measure
  - 18. Product Measure and Fubini's Theorem
  - 19. The L^p Spaces*
- **Chapter 4. Random Variables and Expected Values**
  - 20. Random Variables and Distributions
  - 21. Expected Values
  - 22. Sums of Independent Random Variables
  - 23. The Poisson Process
  - 24. The Ergodic Theorem*
- **Chapter 5. Convergence of Distributions**
  - 25. Weak Convergence
  - 26. Characteristic Functions
  - 27. The Central Limit Theorem
  - 28. Infinitely Divisible Distributions*
  - 29. Limit Theorems in R^k
  - 30. The Method of Moments*
- **Chapter 6. Derivatives and Conditional Probability**
  - 31. Derivatives on the Line*
  - 32. The Radon-Nikodym Theorem
  - 33. Conditional Probability
  - 34. Conditional Expectation
  - 35. Martingales
- **Chapter 7. Stochastic Processes**
  - 36. Kolmogorov's Existence Theorem
  - 37. Brownian Motion
  - 38. Nondenumerable Probabilities*
  - Set Theory
  - The Real Line
  - Euclidean k-Space
  - Analysis
  - Infinite Series
  - Convex Functions
  - Some Multivariable Calculus
  - Continued Fractions
- **Notes on the Problems**
  - Section 1
  - Section 2
  - Section 3
  - Section 4
  - Section 5
  - Section 6
  - Section 7
  - Section 8
  - Section 9
  - Section 10
  - Section 11
  - Section 12
  - Section 13
  - Section 14
  - Section 15
  - Section 16
  - Section 17
  - Section 18
  - Section 19
  - Section 20
  - Section 21
  - Section 22
  - Section 23
  - Section 25
  - Section 26
  - Section 27
  - Section 28
  - Section 29
  - Section 30
  - Section 31
  - Section 32
  - Section 33
  - Section 34
  - Section 35
  - Section 36
  - Section 37
- **List of Symbols**
- **Back Cover**

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
