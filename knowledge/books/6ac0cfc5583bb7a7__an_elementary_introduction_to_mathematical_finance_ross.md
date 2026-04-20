## An Elementary Introduction To Mathematical Finance(Ross) — 未標示
**來源**: E:/書籍/An Elementary Introduction To Mathematical Finance(Ross).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Half-title**
- **Title**
- **Introduction and Preface**
  - New to This Edition
- **1. Probability**
  - 1.1 Probabilities and Events
  - 1.2 Conditional Probability
  - 1.3 Random Variables and Expected Values
  - ... (4 more sections)
- **2. Normal Random Variables**
  - 2.1 Continuous Random Variables
  - 2.2 Normal Random Variables
  - 2.3 Properties of Normal Random Variables
  - ... (3 more sections)
- **3. Brownian Motion and Geometric Brownian Motion**
  - 3.1 Brownian Motion
  - 3.2 Brownian Motion as a Limit of Simpler Models
  - 3.3 Geometric Brownian Motion
  - ... (3 more sections)
- **4. Interest Rates and Present Value Analysis**
  - 4.1 Interest Rates
  - 4.2 Present Value Analysis
  - 4.3 Rate of Return
  - ... (2 more sections)
- **5. Pricing Contracts via Arbitrage**
  - 5.1 An Example in Options Pricing
  - 5.2 Other Examples of Pricing via Arbitrage
  - 5.3 Exercises
- **6. The Arbitrage Theorem**
  - 6.1 The Arbitrage Theorem
  - 6.2 The Multiperiod Binomial Model
  - 6.3 Proof of the Arbitrage Theorem
  - ... (1 more sections)
- **7. The Black-Scholes Formula**
  - 7.1 Introduction
  - 7.2 The Black-Scholes Formula
  - 7.3 Properties of the Black-Scholes Option Cost
  - ... (4 more sections)
- **8. Additional Results on Options**
  - 8.1 Introduction
  - 8.2 Call Options on Dividend-Paying Securities
  - 8.3 Pricing American Put Options
  - ... (5 more sections)
- **9. Valuing by Expected Utility**
  - 9.1 Limitations of Arbitrage Pricing
  - 9.2 Valuing Investments by Expected Utility
  - 9.3 The Portfolio Selection Problem
  - ... (4 more sections)
- **10. Stochastic Order Relations**
  - 10.1 First-Order Stochastic Dominance
  - 10.2 Using Coupling to Show Stochastic Dominance
  - 10.3 Likelihood Ratio Ordering
  - ... (3 more sections)
- **11. Optimization Models**
  - 11.1 Introduction
  - 11.2 A Deterministic Optimization Model
  - 11.3 Probabilistic Optimization Problems
  - ... (1 more sections)
- **12. Stochastic Dynamic Programming**
  - 12.1 The Stochastic Dynamic Programming Problem
  - 12.2 Infinite Time Models
  - 12.3 Optimal Stopping Problems
  - ... (2 more sections)
- **13. Exotic Options**
  - 13.1 Introduction
  - 13.2 Barrier Options
  - 13.3 Asian and Lookback Options
  - ... (7 more sections)
- **14. Beyond Geometric Brownian Motion Models**
  - 14.1 Introduction
  - 14.2 Crude Oil Data
  - 14.3 Models for the Crude Oil Data
  - ... (1 more sections)
- **15. Autoregressive Models and Mean Reversion**
  - 15.1 The Autoregressive Model
  - 15.2 Valuing Options by Their Expected Return
  - 15.3 Mean Reversion
  - ... (1 more sections)

### TL;DR (≤120字)
本書屬於 options volatility 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **波動率是選擇權定價的核心變量** — 方向性預測失敗時,波動率結構 (ATM/IV skew/term structure) 仍可創造 +EV 機會,這是本質而非戰術
2. **Greeks 是部位面的座標軸** — 任何 payoff 都可以分解為 delta/gamma/vega/theta 的組合,這讓風險管理從「個別部位」升級為「組合相對曝險」
3. **波動率回歸均值是經驗命題,非數學恆等式** — 做 long vol 或 short vol 必須結合結構性事件與資金面,否則長期 short vol 即撿銅板在推土機前

### 可用戰術/策略

- 當 IV rank 高於歷史 80 分位且事件已過,考慮 short iron condor / short strangle,控制 vega 曝險
- 用 calendar spread 捕捉 term structure 扭曲 (近月 IV 高於遠月),對沖市場方向

### 盲點 / 反例 / 適用邊界

- 選擇權策略高度依賴流動性與 bid-ask spread;台指 TXO 週選以外、個股選擇權與期貨選擇權的交易成本可能吞掉理論 edge

### 與 Edward 既有知識的連結

- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
- 呼應零式原則 *meta_strategy_over_strategy* — 關注資金曲線與長期夏普、勝過單筆交易或單期回報
