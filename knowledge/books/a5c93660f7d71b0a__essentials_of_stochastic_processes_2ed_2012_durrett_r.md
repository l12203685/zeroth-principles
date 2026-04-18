## Essentials of Stochastic Processes, 2ed, 2012, Durrett R. — 未標示
**來源**: E:/書籍/Essentials of Stochastic Processes, 2ed, 2012, Durrett R..pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Essentials of Stochastic Process**
- **Chapter 1 Markov Chains**
  - 1.1 Definitions and Examples
  - 1.2 Multistep Transition Probabilities
  - 1.3 Classification of States
  - 1.4 Stationary Distributions
  - 1.5 Limit Behavior
  - 1.6 Special Examples
  - 1.7 Proofs of the Main Theorems
  - 1.8 Exit Distributions
  - 1.9 Exit Times
  - 1.10 Infinite State Spaces
  - 1.11 Chapter Summary
  - 1.12 Exercises
- **Chapter 2 Poisson Processes**
  - 2.1 Exponential Distribution
  - 2.2 Defining the Poisson Process
  - 2.3 Compound Poisson Processes
  - 2.4 Transformations
  - 2.5 Chapter Summary
  - 2.6 Exercises
- **Chapter 3 Renewal Processes**
  - 3.1 Laws of Large Numbers
  - 3.2 Applications to Queueing Theory
  - 3.3 Age and Residual Life*
  - 3.4 Chapter Summary
  - 3.5 Exercises
- **Chapter 4 Continuous Time Markov Chains**
  - 4.1 Definitions and Examples
  - 4.2 Computing the Transition Probability
  - 4.3 Limiting Behavior
  - 4.4 Exit Distributions and Hitting Times
  - 4.5 Markovian Queues
  - 4.6 Queueing Networks*
  - 4.7 Chapter Summary
  - 4.8 Exercises
- **Chapter 5 Martingales**
  - 5.1 Conditional Expectation
  - 5.2 Examples, Basic Properties
  - 5.3 Gambling Strategies, Stopping Times
  - 5.4 Applications
  - 5.5 Convergence
  - 5.6 Exercises
- **Chapter 6 Mathematical Finance**
  - 6.1 Two Simple Examples
  - 6.2 Binomial Model
  - 6.3 Concrete Examples
  - 6.4 Capital Asset Pricing Model
  - 6.5 American Options
  - 6.6 Black-Scholes Formula
  - 6.7 Calls and Puts
  - 6.8 Exercises
- **Appendix A Review of Probability**
  - A.1 Probabilities, Independence
  - A.2 Random Variables, Distributions
  - A.3 Expected Value, Moments

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
