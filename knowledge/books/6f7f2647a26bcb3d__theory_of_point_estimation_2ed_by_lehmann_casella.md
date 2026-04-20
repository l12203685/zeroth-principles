## Theory of Point Estimation,2ed — Lehmann&Casella
**來源**: E:/書籍/Theory of Point Estimation,2ed, by Lehmann&Casella.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Preface to the Second Edition**
- **Preface to the First Edition**
- **List of Tables**
- **List of Figures**
- **List of Examples**
- **Table of Notation**
- **1 Preparations**
  - 1 The Problem
  - 2 Measure Theory and Integration
  - 3 Probability Theory
  - 4 Group Families
  - 5 Exponential Families
  - 6 Sufficient Statistics
  - 7 Convex Loss Functions
  - 8 Convergence in Probability and in Law
  - 9 Problems
  - 10 Notes
- **2 Unbiasedness**
  - 1 UMVU Estimators
  - 2 Continuous One- and Two-Sample Problems
  - 3 Discrete Distributions
  - 4 Nonparametric Families
  - 5 The Information Inequality
  - 6 The Multiparameter Case and Other Extensions
  - 7 Problems
  - 8 Notes
- **3 Equivariance**
  - 1 First Examples
  - 2 The Principle of Equivariance
  - 3 Location-Scale Families
  - 4 Normal Linear Models
  - 5 Random and Mixed Effects Models
  - 6 Exponential Linear Models
  - 7 Finite Population Models
  - 8 Problems
  - 9 Notes
- **4 Average Risk Optimality**
  - 1 Introduction
  - 2 First Examples
  - 3 Single-Prior Bayes
  - 4 Equivariant Bayes
  - 5 Hierarchical Bayes
  - 6 Empirical Bayes
  - 7 Risk Comparisons
  - 8 Problems
  - 9 Notes
- **5 Minimaxity and Admissibility**
  - 1 Minimax Estimation
  - 2 Admissibility and Minimaxity in Exponential Families
  - 3 Admissibility and Minimaxity in Group Families
  - 4 Simultaneous Estimation
  - 5 Shrinkage Estimators in the Normal Case
  - 6 Extensions
  - 7 Admissibility and Complete Classes
  - 8 Problems
  - 9 Notes
- **6 Asymptotic Optimality**
  - 1 Performance Evaluations in Large Samples
  - 2 Asymptotic Efficiency
  - 3 Efficient Likelihood Estimation
  - 4 Likelihood Estimation: Multiple Roots
  - 5 The Multiparameter Case
  - 6 Applications
  - 7 Extensions
  - 8 Asymptotic Efficiency of Bayes Estimators
  - 9 Problems
  - 10 Notes
- **Author Index**
  - A
  - B
  - C
  - D
  - E
  - F
  - G
  - H
  - I
  - J
  - K
  - L
  - M
  - N
  - O
  - P
  - Q
  - R
  - S
  - T
  - U
  - V
  - W
  - Y
  - Z
- **Subject Index**
  - A
  - B
  - C
  - D
  - E
  - F
  - G
  - H
  - I
  - J
  - K
  - L
  - M
  - N
  - O
  - P
  - Q
  - R
  - S
  - T
  - U
  - V
  - W

### TL;DR (≤120字)
本書屬於 statistics evidence based 範疇,作者 Lehmann&Casella 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

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
