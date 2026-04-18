## Rice_數理統計與資料分析_3ed — 未標示
**來源**: E:/投資交易/參考書籍/Rice_數理統計與資料分析_3ed.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Front Cover**
- **1. Probability**
  - 1.1 Introduction
  - 1.2 Sample Spaces
  - 1.3 Probability Measures
  - ... (5 more sections)
- **2. Random Variables**
  - 2.1 Discrete Random Variables
  - 2.2 Continuous Random Variables
  - 2.3 Functions of a Random Variable
  - ... (2 more sections)
- **3. Joint Distributions**
  - 3.1 Introduction
  - 3.2 Discrete Random Variables
  - 3.3 Continuous Random Variables
  - ... (5 more sections)
- **4. Expected Values**
  - 4.1 The Expected Value of a Random Variable
  - 4.2 Variance and Standard Deviation
  - 4.3 Covariance and Correlation
  - ... (4 more sections)
- **5. Limit Theorems**
  - 5.1 Introduction
  - 5.2 The Law of Large Numbers
  - 5.3 Convergence in Distribution and the Central Limit Theorem
  - ... (1 more sections)
- **6. Distributions Derived from the Normal Distribution**
  - 6.1 Introduction
  - 6.2 χ[sup(2)], t, and F Distributions
  - 6.3 The Sample Mean and the Sample Variance
  - ... (1 more sections)
- **7. Survey Sampling**
  - 7.1 Introduction
  - 7.2 Population Parameters
  - 7.3 Simple Random Sampling
  - ... (4 more sections)
- **8. Estimation of Parameters and Fitting of Probability Distributions**
  - 8.1 Introduction
  - 8.2 Fitting the Poisson Distribution to Emissions of Alpha Particles
  - 8.3 Parameter Estimation
  - ... (7 more sections)
- **9. Testing Hypotheses and Assessing Goodness of Fit**
  - 9.1 Introduction
  - 9.2 The Neyman-Pearson Paradigm
  - 9.3 The Duality of Confidence Intervals and Hypothesis Tests
  - ... (8 more sections)
- **10. Summarizing Data**
  - 10.1 Introduction
  - 10.2 Methods Based on the Cumulative Distribution Function
  - 10.3 Histograms, Density Curves, and Stem-and-Leaf Plots
  - ... (6 more sections)
- **11. Comparing Two Samples**
  - 11.1 Introduction
  - 11.2 Comparing Two Independent Samples
  - 11.3 Comparing Paired Samples
  - ... (3 more sections)
- **12. The Analysis of Variance**
  - 12.1 Introduction
  - 12.2 The One-Way Layout
  - 12.3 The Two-Way Layout
  - ... (2 more sections)
- **13. The Analysis of Categorical Data**
  - 13.1 Introduction
  - 13.2 Fisher's Exact Test
  - 13.3 The Chi-Square Test of Homogeneity
  - ... (5 more sections)
- **14. Linear Least Squares**
  - 14.1 Introduction
  - 14.2 Simple Linear Regression
  - 14.3 The Matrix Approach to Linear Least Squares
  - ... (6 more sections)
- **APPENDIX A: Common Distributions**
- **APPENDIX B: Tables**
- **Answers to Selected Problems**
- **Author Index**
- **Applications Index**
- **Subject Index**
- **Credits**

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
