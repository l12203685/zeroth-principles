## edu-2009-fall-exam-fm-ques — 未標示
**來源**: E:/投資交易/研究與模型/SOA/2. FM/edu-2009-fall-exam-fm-ques.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1.  Which statement about zero-cost purchased collars is FALSE?**
- **2.  You are given the following information:**
- **3.   Happy Jalapenos, LLC has an exclusive contract to supply jala**
- **4.   Zero-coupon risk-free bonds are available with the following**
- **5.  You are given the following information:**
- **6.   The current price of one share of XYZ stock is 100.  The forw**
- **7.   A non-dividend paying stock currently sells for 100.  One yea**
- **8.   You believe that the volatility of a stock is higher than ind**
- **9.  You are given the following information:**
- **10. Suppose stock XYZ has a current price of 100.  The forward pr**

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
