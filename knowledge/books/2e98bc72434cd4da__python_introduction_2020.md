## python_introduction_2020 — 未標示
**來源**: E:/書籍/python_introduction_2020.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Introduction**
  - Background
  - ... (6 more sections)
- **Built-in Data Types**
  - Variable Names
  - ... (4 more sections)
- **Arrays**
  - Array
  - ... (9 more sections)
- **Basic Math**
  - Operators
  - ... (10 more sections)
- **Basic Functions and Numerical Indexing**
  - Generating Arrays
  - ... (8 more sections)
- **Special Arrays**
  - Exercises
- **Array Functions**
  - Shape Information and Transformation
  - ... (3 more sections)
- **Importing and Exporting Data**
  - Importing Data using pandas
  - ... (4 more sections)
- **Inf, NaN and Numeric Limits**
  - inf and NaN
  - ... (2 more sections)
- **Logical Operators and Find**
  - >, >=, <, <=, ==, !=
  - ... (4 more sections)
- **Advanced Selection and Assignment**
  - Numerical Indexing
  - ... (4 more sections)
- **Flow Control, Loops and Exception Handling**
  - Whitespace and Flow Control
  - ... (7 more sections)
- **Dates and Times**
  - Creating Dates and Times
  - ... (2 more sections)
- **Graphics**
  - seaborn
  - ... (6 more sections)
- **pandas**
  - Data Structures
  - ... (5 more sections)
- **Structured Arrays**
  - Mixed Arrays with Column Names
  - ... (1 more sections)
- **Custom Function and Modules**
  - Functions
  - ... (9 more sections)
- **Probability and Statistics Functions**
  - Simulating Random Variables
  - ... (6 more sections)
- **Statistical Analysis with statsmodels**
  - Regression
  - ... (4 more sections)
- **Non-linear Function Optimization**
  - Unconstrained Optimization
  - ... (5 more sections)
- **String Manipulation**
  - String Building
  - ... (4 more sections)
- **File System Operations**
  - Changing the Working Directory
  - ... (7 more sections)
- **Performance and Code Optimization**
  - Getting Started
  - ... (10 more sections)
- **Improving Performance using Numba**
  - Quick Start
  - ... (6 more sections)
- **Improving Performance using Cython**
  - Diagnosing Performance Issues
  - ... (2 more sections)
- **Executing Code in Parallel**
  - map and related functions
  - ... (5 more sections)
- **Object-Oriented Programming (OOP)**
  - Introduction
  - ... (3 more sections)
- **Other Interesting Python Packages**
  - Statistics and Statistical Modeling
  - ... (3 more sections)
- **Examples**
  - Estimating the Parameters of a GARCH Model
  - ... (3 more sections)
- **Quick Reference**
  - Built-ins
  - ... (5 more sections)

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
