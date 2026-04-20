## Arbitrage Theory in Continuous Time, 3ed, 2004, by Bjork, T. — 未標示
**來源**: E:/書籍/Arbitrage Theory in Continuous Time, 3ed, 2004, by Bjork, T..pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1 Introduction**
  - 1.1 Problem Formulation
- **2 The Binomial Model**
  - 2.1 The One Period Model
  - ... (3 more sections)
- **3 A More General One Period Model**
  - 3.1 The Model
  - ... (6 more sections)
- **4 Stochastic Integrals**
  - 4.1 Introduction
  - ... (9 more sections)
- **5 Differential Equations**
  - 5.1 Stochastic Differential Equations
  - ... (7 more sections)
- **6 Portfolio Dynamics**
  - 6.1 Introduction
  - ... (3 more sections)
- **7 Arbitrage Pricing**
  - 7.1 Introduction
  - ... (9 more sections)
- **8 Completeness and Hedging**
  - 8.1 Introduction
  - ... (4 more sections)
- **9 Parity Relations and Delta Hedging**
  - 9.1 Parity Relations
  - ... (3 more sections)
- **10 The Martingale Approach to Arbitrage Theory***
  - 10.1 The Case with Zero Interest Rate
  - ... (7 more sections)
- **11 The Mathematics of the Martingale Approach***
  - 11.1 Stochastic Integral Representations
  - ... (7 more sections)
- **12 Black-Scholes from a Martingale Point of View***
  - 12.1 Absence of Arbitrage
  - ... (2 more sections)
- **13 Multidimensional Models: Classical Approach**
  - 13.1 Introduction
  - ... (5 more sections)
- **14 Multidimensional Models: Martingale Approach***
  - 14.1 Absence of Arbitrage
  - ... (9 more sections)
- **15 Incomplete Markets**
  - 15.1 Introduction
  - ... (7 more sections)
- **16 Dividends**
  - 16.1 Discrete Dividends
  - ... (3 more sections)
- **17 Currency Derivatives**
  - 17.1 Pure Currency Contracts
  - ... (5 more sections)
- **18 Barrier Options**
  - 18.1 Mathematical Background
  - ... (6 more sections)
- **19 Stochastic Optimal Control**
  - 19.1 An Example
  - ... (8 more sections)
- **20 The Martingale Approach to Optimal Investment***
  - 20.1 Generalities
  - ... (9 more sections)
- **21 Optimal Stopping Theory and American Options***
  - 21.1 Introduction
  - ... (7 more sections)
- **22 Bonds and Interest Rates**
  - 22.1 Zero Coupon Bonds
  - ... (4 more sections)
- **23 Short Rate Models**
  - 23.1 Generalities
  - ... (3 more sections)
- **24 Martingale Models for the Short Rate**
  - 24.1 Q-dynamics
  - ... (5 more sections)
- **25 Forward Rate Models**
  - 25.1 The Heath-Jarrow-Morton Framework
  - ... (4 more sections)
- **26 Change of Numeraire***
  - 26.1 Introduction
  - ... (10 more sections)
- **27 LIBOR and Swap Market Models**
  - 27.1 Caps: Definition and Market Practice
  - ... (13 more sections)
- **28 Potentials and Positive Interest**
  - 28.1 Generalities
  - ... (6 more sections)
- **29 Forwards and Futures**
  - 29.1 Forward Contracts
  - ... (3 more sections)
- **A Measure and Integration***
  - A.1 Sets and Mappings
  - ... (12 more sections)
- **B Probability Theory***
  - B.1 Random Variables and Processes
  - ... (7 more sections)
- **C Martingales and Stopping Times***
  - C.1 Martingales
  - ... (26 more sections)

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
