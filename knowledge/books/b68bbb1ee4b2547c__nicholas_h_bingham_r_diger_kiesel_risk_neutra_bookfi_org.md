## [Nicholas_H._Bingham,_Rüdiger_Kiesel]_Risk — Neutra(BookFi.org)
**來源**: E:/書籍/[Nicholas_H._Bingham,_Rüdiger_Kiesel]_Risk-Neutra(BookFi.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **RISK-NEUTRAL VALUATION: PRICING AND HEDGING OF FINANCIAL DERIVATIVES, 2ND ED.**
- **Springer Finance**
- **Preface to the Second Edition**
- **Preface to the First Edition**
- **Chapter 1. Derivative Background**
  - 1.1 Financial Markets and Instruments
  - 1.2 Arbitrage
  - 1.3 Arbitrage Relationships
  - ... (2 more sections)
- **Chapter 2. Probability Background**
  - 2.1 Measure
  - 2.2 Integral
  - 2.3 Probability
  - ... (10 more sections)
- **Chapter 3. Stochastic Processes in Discrete Time**
  - 3.1 Information and Filtrations
  - 3.2 Discrete-parameter Stochastic Processes
  - 3.3 Definition and Basic Properties of Martingales
  - ... (6 more sections)
- **Chapter 4. Mathematical Finance in Discrete Time**
  - 4.1 The Model
  - 4.2 Existence of Equivalent Martingale Measures
  - 4.3 Complete Markets: Uniqueness of Equivalent Martingale Measures
  - ... (7 more sections)
- **Chapter 5. Stochastic Processes in Continuous Time**
  - 5.1 Filtrations; Finite-dimensional Distributions
  - 5.2 Classes of Processes
  - 5.3 Brownian Motion
  - ... (9 more sections)
- **Chapter 6. Mathematical Finance in Continuous Time**
  - 6.1 Continuous-time Financial Market Models
  - 6.2 The Generalized Black-Scholes Model
  - 6.3 Further Contingent Claim Valuation
  - ... (3 more sections)
- **Chapter 7. Incomplete Markets**
  - 7.1 Pricing in Incomplete Markets
  - 7.2 Hedging in Incomplete Markets
  - 7.3 Stochastic Volatility Models
  - ... (1 more sections)
- **Chapter 8. Interest Rate Theory**
  - 8.1 The Bond Market
  - 8.2 Short-rate Models
  - 8.3 Heath-Jarrow-Morton Methodology
  - ... (4 more sections)
- **Chapter 9. Credit Risk**
  - 9.1 Aspects of Credit Risk
  - 9.2 Basic Credit Risk Modeling
  - 9.3 Structural Models
  - ... (4 more sections)
- **Appendix A. Hilbert Space**
- **Appendix B. Projections and Conditional Expectations**
- **Appendix C. The Separating Hyperplane Theorem**

### TL;DR (≤120字)
本書屬於 options volatility 範疇,作者 Neutra(BookFi.org) 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

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
