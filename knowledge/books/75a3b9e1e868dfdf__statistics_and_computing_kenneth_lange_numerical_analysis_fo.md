## Statistics and Computing) Kenneth Lange-Numerical analysis for statisticians — Springer (2010)
**來源**: E:/書籍/Statistics and Computing) Kenneth Lange-Numerical analysis for statisticians-Springer (2010).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Preface to the Second Edition**
  - 0.1 References
- **Preface to the First Edition**
  - 0.2 References
- **1 Recurrence Relations**
  - 1.1 Introduction
  - ... (11 more sections)
- **2 Power Series Expansions**
  - 2.1 Introduction
  - ... (8 more sections)
- **3 Continued Fraction Expansions**
  - 3.1 Introduction
  - ... (5 more sections)
- **4 Asymptotic Expansions**
  - 4.1 Introduction
  - ... (8 more sections)
- **5 Solution of Nonlinear Equations**
  - 5.1 Introduction
  - ... (8 more sections)
- **6 Vector and Matrix Norms**
  - 6.1 Introduction
  - ... (7 more sections)
- **7 Linear Regression and MatrixInversion**
  - 7.1 Introduction
  - ... (12 more sections)
- **8 Eigenvalues and Eigenvectors**
  - 8.1 Introduction
  - ... (5 more sections)
- **9 Singular Value Decomposition**
  - 9.1 Introduction
  - ... (5 more sections)
- **10 Splines**
  - 10.1 Introduction
  - ... (5 more sections)
- **11 Optimization Theory**
  - 11.1 Introduction
  - ... (7 more sections)
- **12 The MM Algorithm**
  - 12.1 Introduction
  - ... (12 more sections)
- **13 The EM Algorithm**
  - 13.1 Introduction
  - ... (10 more sections)
- **14 Newton's Method and Scoring**
  - 14.1 Introduction
  - ... (11 more sections)
- **15 Local and Global Convergence**
  - 15.1 Introduction
  - ... (7 more sections)
- **16 Advanced Optimization Topics**
  - 16.1 Introduction
  - ... (7 more sections)
- **17 Concrete Hilbert Spaces**
  - 17.1 Introduction
  - ... (7 more sections)
- **18 Quadrature Methods**
  - 18.1 Introduction
  - ... (7 more sections)
- **19 The Fourier Transform**
  - 19.1 Introduction
  - ... (6 more sections)
- **20 The Finite Fourier Transform**
  - 20.1 Introduction
  - ... (7 more sections)
- **21 Wavelets**
  - 21.1 Introduction
  - ... (7 more sections)
- **22 Generating Random Deviates**
  - 22.1 Introduction
  - ... (11 more sections)
- **23 Independent Monte Carlo**
  - 23.1 Introduction
  - ... (8 more sections)
- **24 Permutation Tests and the Bootstrap**
  - 24.1 Introduction
  - ... (5 more sections)
- **25 Finite-State Markov Chains**
  - 25.1 Introduction
  - ... (9 more sections)
- **26 Markov Chain Monte Carlo**
  - 26.1 Introduction
  - ... (7 more sections)
- **27 Advanced Topics in MCMC**
  - 27.1 Introduction
  - ... (10 more sections)
- **Appendix: The Multivariate Normal Distribution**
  - A.1 References

### TL;DR (≤120字)
本書屬於 statistics evidence based 範疇,作者 Springer (2010) 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

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
