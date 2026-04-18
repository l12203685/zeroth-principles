## Volume Profile, Market Profile, Order Flow Next Generation of Daytrading by Johannes Forthmann (z-lib.org) — 未標示
**來源**: E:/投資交易/交易學習資料庫/@交易/@VolumeProfile/Volume Profile, Market Profile, Order Flow Next Generation of Daytrading by Johannes Forthmann (z-lib.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1.Introduction**
- **2. The Advantages of Futures**
- **3. The Market Participants**
- **4. Market Profile - A Brief Overview**
- **5. What is a Volume Profile?**
- **6. Value Area**
- **7. Forms and Shapes of Profiles**
- **8. How to display the Profiles?**
  - 8.1 Fixed profiles
  - 8.2 Flexible profiles
- **9. Bounce Backs**
- **10. General Set ups**
  - 10.1 Accumulation and Follow-up
  - 10.2 Reversals
- **11. Hardware, Software and Data Feed**
- **12. Order Flow Analysis**
  - 12.1 Order book - DOM
  - 12.2 Footprints - Inside the Chart
  - 12.3 Delta
- **13. The Preparation**
- **14. Liquidity and Volatility - An Important Pair**
- **15. Characteristics of Individual Trading Instruments**
- **16. More on Market Profile**
- **17. Filtering the Ledge**
- **18. Broadening Tops - a Warning Signal**
- **19. Complete Examples**
  - 19.1 Yen
  - 19.2 E-Mini S&P
  - 19.3 Fdax
  - 19.4 Bund Future
  - 19.5 A Day with Crude Oil
  - 19.6 Gold
  - 19.7 Broadening Top and Ledge Filter
  - 19.8 EURUSD
  - 19.9 Weekly Profiles
- **20. Summary**
- **21. Questions that could be asked**
- **22. Fake Moves**
  - 22.1 Backfire Pattern
  - 22.2 SHS Fakes
  - 22.3 Bottom- and Top squeeze
  - 22.4 Natural Support and Resistance Fakes
  - 22.5 Trend line Fakes
  - 22.6. Fake Breakouts
- **23. What is a Trend?**
- **24. Trade- and Risk Management**
- **25. Short Term Trading - A Trade Example**

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

- 呼應零式原則 *derivative_over_level* — 關注變化率/拐點而非單期水準
- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
