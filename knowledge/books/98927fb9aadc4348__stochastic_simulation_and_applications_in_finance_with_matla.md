## Stochastic Simulation and Applications in Finance with MATLAB Programs — 未標示
**來源**: E:/書籍/Stochastic Simulation and Applications in Finance with MATLAB Programs.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Stochastic Simulation and Applications in Finance with MATLAB® Programs**
  - 1 Introduction to Probability
  - 2 Introduction to Random Variables
  - 3 Random Sequences
  - 4 Introduction to Computer Simulation of Random Variables
  - 5 Foundations of Monte Carlo Simulations
  - 6 Fundamentals of Quasi Monte Carlo (QMC) Simulations
  - 7 Introduction to Random Processes
  - 8 Solution of Stochastic Differential Equations
  - 9 General Approach to the Valuation of Contingent Claims
  - 10 Pricing Options using Monte Carlo Simulations
  - 11 Term Structure of Interest Rates and Interest Rate Derivatives
  - 12 Credit Risk and the Valuation of Corporate Securities
  - 13 Valuation of Portfolios of Financial Guarantees
  - 14 Risk Management and Value at Risk (VaR)
  - 15 Value at Risk (VaR) and Principal Components Analysis (PCA)
  - Appendix A: Review of Mathematics
  - Appendix B: MATLAB® Functions
  - References and Bibliography

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
