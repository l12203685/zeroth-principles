## Allen's Book (美國老師合作研究) — 未標示
**來源**: E:/書籍/Allen's Book (美國老師合作研究).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **List of Acronyms**
- **1. Introduction**
  - 1.1 Purpose of this Book
  - 1.2 Systems and Key Input Variables
  - 1.3 Problem-solving Methods
  - 1.4 History of "Quality" and Six Sigma
  - 1.5 The Culture of Discipline
  - 1.6 Real Success Stories
  - 1.7 Overview of this Book
  - Problems
- **Part I: Statistical Quality Control**
  - 2. Statistical Quality Control and Six Sigma
  - 3. Define Phase and Strategy
  - 4. Measure Phase and Statistical Charting
  - 5. Analyze Phase
  - 6. Improve or Design Phase
  - 7. Control or Verify Phase
  - 8. Advanced SQC Methods
  - 9. SQC Case Studies
  - 10. SQC Theory
- **Part II: Design of Experiments (DOE) and Regression**
  - 11. DOE: The Jewel of Quality Engineering
  - 12. DOE: Screening Using Fractional Factorials
  - 13. DOE: Response Surface Methods
  - 14. DOE: Robust Design
  - 15. Regression
  - 16. Advanced Regression and Alternatives
  - 17. DOE and Regression Case Studies
  - 18. DOE and Regression Theory
- **Part III: Optimization and Strategy**
  - 19. Optimization and Strategy
  - 20. Tolerance Design
  - 21. Design for Six Sigma
  - 22. Lean Sigma Project Design
- **Problem Solutions**
  - Chapter 1
  - Chapter 2
  - Chapter 3
  - Chapter 4
  - Chapter 5
  - Chapter 6
  - Chapter 7
  - Chapter 8
  - Chapter 9
  - Chapter 10
  - Chapter 11
  - Chapter 12
  - Chapter 13
  - Chapter 14
  - Chapter 15
  - Chapter 16
  - Chapter 17
  - Chapter 18
  - Chapter 19
  - Chapter 20
  - Chapter 21
  - Chapter 22

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
