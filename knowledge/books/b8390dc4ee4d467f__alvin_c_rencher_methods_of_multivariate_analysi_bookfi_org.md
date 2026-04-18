## [Alvin_C._Rencher]_Methods_of_Multivariate_Analysi(BookFi.org) — 未標示
**來源**: E:/書籍/[Alvin_C._Rencher]_Methods_of_Multivariate_Analysi(BookFi.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Contents v**
- **Preface xv**
- **1 Introduction 1**
  - 1.1 Why Multivariate Analysis? 1
  - 1.2 Prerequisites 3
  - ... (2 more sections)
- **2 Matrix Algebra 5**
  - 2.1 Introduction 5
  - 2.2 Notation and Basic Definitions 5
  - ... (9 more sections)
- **3 Characterizing and Displaying Multivariate Data 43**
  - 3.1 Mean and Variance of a Univariate Random Variable 43
  - 3.2 Covariance and Correlation of Bivariate Random Variables 45
  - ... (10 more sections)
- **4 The Multivariate Normal Distribution 82**
  - 4.1 Multivariate Normal Density Function 82
  - 4.2 Properties of Multivariate Normal Random Variables 85
  - ... (3 more sections)
- **5 Tests on One or Two Mean Vectors 112**
  - 5.1 Multivariate versus Univariate Tests 112
  - 5.2 Tests on mu with Sigma Known 113
  - ... (7 more sections)
- **6 Multivariate Analysis of Variance 156**
  - 6.1 One-Way Models 156
  - 6.2 Comparison of the Four Manova Test Statistics 176
  - ... (9 more sections)
- **7 Tests on Covariance Matrices 248**
  - 7.1 Introduction 248
  - 7.2 Testing a Specified Pattern for Sigma 248
  - ... (2 more sections)
- **8 Discriminant Analysis: Description of Group Separation 270**
  - 8.1 Introduction 270
  - 8.2 The Discriminant Function for Two Groups 271
  - ... (7 more sections)
- **9 Classification Analysis: Allocation of Observations to Groups 299**
  - 9.1 Introduction 299
  - 9.2 Classification into Two Groups 300
  - ... (5 more sections)
- **10 Multivariate Regression 322**
  - 10.1 Introduction 322
  - 10.2 Multiple Regression: Fixed x's 323
  - ... (6 more sections)
- **11 Canonical Correlation 361**
  - 11.1 Introduction 361
  - 11.2 Canonical Correlations and Canonical Variates 361
  - ... (4 more sections)
- **12 Principal Component Analysis 380**
  - 12.1 Introduction 380
  - 12.2 Geometric and Algebraic Bases of Principal Components 381
  - ... (7 more sections)
- **13 Factor Analysis 408**
  - 13.1 Introduction 408
  - 13.2 Orthogonal Factor Model 409
  - ... (6 more sections)
- **14 Cluster Analysis 451**
  - 14.1 Introduction 451
  - 14.2 Measures of Similarity or Dissimilarity 452
  - ... (5 more sections)
- **15 Graphical Procedures 504**
  - 15.1 Multidimensional Scaling 504
  - 15.2 Correspondence Analysis 514
  - ... (1 more sections)
- **A Tables 549**
  - Table A.1 Upper Percentiles for √b1
  - Table A.2 Coefficients for Transforming √b1 to a Standard Normal
  - ... (13 more sections)
- **B Answers and Hints to Problems 591**
  - CHAPTER 2
  - CHAPTER 3
  - ... (12 more sections)
- **C Data Sets and SAS Files 679**
- **References 681**
- **Index 695**

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
