## Lectures on Stochastic Processes(Ito) — 未標示
**來源**: E:/書籍/Lectures on Stochastic Processes(Ito).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Preliminaries**
  - Measurable space
  - Probability space
  - Independence
  - Conditional expectation
  - Wiener and Poisson processes
- **Markov Processes**
  - Introduction
  - Transition Probability
  - Semi-groups
  - Green operator
  - The Generator
  - Examples
  - Dual notions
  - A Theorem of Kac
- **Srong Markov Processes**
  - Markov time
  - Examples of Markov time
  - Definition of strong Markov process
  - A condition for a Markov process...
  - Example of a Markov process....
  - Dynkin's formula and generalized ...
  - Blumenthal's 0-1 law
  - Markov process with discrete state space
  - Generator in the restricted sence
- **Multi-dimensional Brownian Motion**
  - Definition
  - Generator of the k-dimensional Brownian motion
  - Stochastic solution of the Dirichlet problem
  - Recurrence
  - Green function
  - Hitting probability
  - Regular points (k 3)
  - Plane measure of a two dimensional...
- **Additive Processes**
  - Definitions
  - Gaussian additive processes and ...
  - Levy's canonical form
  - Temporally homogeneouos Lévy processes
  - Stable processes
  - Lévy process as a Markov process
  - Multidimensional Levy processes
- **Stochastic Differential Equations**
  - Introduction
  - Stochastic integral (1) Function spaces E, L2, Es
  - Stochastic Integral (II) Definitions and properties
  - Definition of stochastic integral (III) Continuous version
  - Stochstic differentials
  - Stochastic differential equations
  - Construction of diffusion
- **Linear Diffusion**
  - Generalities
  - Generator in the restricted sense
  - Local generator
  - Feller's form of generators (1) Scale
  - Feller's form of generator (2) Speed measure
  - Feller's form of generators (3)
  - Feller's form of generators...

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
- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
