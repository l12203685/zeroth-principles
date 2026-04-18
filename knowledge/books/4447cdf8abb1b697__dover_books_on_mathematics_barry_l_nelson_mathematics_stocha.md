## (Dover Books on Mathematics) Barry L. Nelson, Mathematics-Stochastic Modeling_ Analysis and Simulation — Dover Publications (2010)
**來源**: E:/書籍/(Dover Books on Mathematics) Barry L. Nelson, Mathematics-Stochastic Modeling_ Analysis and Simulation-Dover Publications (2010).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1. Why Are We Here**
- **2. Sample Paths?**
  - 2.1 The Case of the Copy Enlargement
  - 2.2 Notation and Review
  - 2.3 Sample-Path Decomposition
  - 2.4 Exercises
- **3. Basics**
  - 3.1 Probability
  - 3.2 Statistics
  - 3.3 Random-Variate Generation
  - 3.4 The Case of the Copy Enlargement, Revisited
  - 3.5 Fine Points
  - 3.6 Exercises
- **4. Simulation**
  - 4.1 The Case of the Leaky Bit Bucket
  - 4.2 Notation and Review
  - 4.3 Stochastic Processes
  - 4.4 Simulating the Leaky Bit Bucket
  - 4.5 A Generic Stochastic-Process Model
  - 4.6 Simulating the Copy Enlargement
  - 4.7 Simulation Programming
  - 4.8 Fine Points
  - 4.9 Exercises
- **5. Arrival-Counting Processes**
  - 5.1 The Case of the Reckless Beehunter
  - 5.2 Notation and Review
  - 5.3 A Generic Arrival-Counting-Process Model
  - 5.4 Simulating the Reckless Beehunter
  - 5.5 The Poisson Arrival Process
  - 5.6 More about Poisson Arrival Processes
  - 5.7 The Case of the Meandering Message
  - 5.8 Derivations
  - 5.9 Results for the Renewal Arrival-Counting Process
  - 5.10 Fine Points
  - 5.11 Exercises
- **6. Discrete-Time Processes**
  - 6.1 The Case of the Random Behavior
  - 6.2 Notation and Review
  - 6.3 Simulating the Random Behavior
  - 6.4 Markov Chains
  - 6.5 The Case of the Defective Detective
  - 6.6 Time-Dependent Performance Measures
  - 6.7 Time-Independent ⠀䰀漀渀最ⴀ刀甀渀) Performance Measures
  - 6.8 The Markov and Stationarity Properties Revisited
  - 6.9 Fine Points
  - 6.10 Exercises
- **7. Continuous-Time Processes**
  - 7.1 The Case of the Software Sellout
  - 7.2 Notation and Review
  - 7.3 Simulating the Software Sellout
  - 7.4 Sample Paths of the Software Sellout
  - 7.5 Markov Processes
  - 7.6 Analysis of Markov Process Sample Paths
  - 7.7 The Case of the Stressed-Out Student
  - 7.8 The Markov and Stationarity Properties Revisited
  - 7.9 Semi-Markov Processes
  - 7.10 Fine Points
  - 7.11 Exercises
- **8. Queueing Processes**
  - 8.1 The Case of the Last Parking Space on Earth
  - 8.2 Notation and Review
  - 8.3 A Queueing Model for the Last Parking Space on Earth
  - 8.4 Markovian Queueing Processes
  - 8.5 Standard Formulations
  - 8.6 Parameterizing Queueing Processes
  - 8.7 Shorthand Notation and Examples
  - 8.8 The Case of the Tardy Ticket
  - 8.9 Networks of Markovian Queues
  - 8.10 Non-Markovian Queues and Networks
  - 8.11 Exercises
- **9. Topics in Simulation of Stochastic Processes**
  - 9.1 Statistical Issues in Simulation
  - 9.2 Rough-Cut Modeling
  - 9.3 Exercises
- **A Simulation Programming Examples**
  - A.l Fortran
  - A.2 SLAM II
  - A.3 SIMAN IV
  - A.4 GPSS/H

### TL;DR (≤120字)
本書屬於 statistics evidence based 範疇,作者 Dover Publications (2010) 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

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
