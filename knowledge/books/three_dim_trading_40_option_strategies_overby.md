## 立体化交易时代：40 种期权投资策略 — [美] 布莱恩·奥弗比 (简中)
**來源**: E:/書籍/立体化交易时代：40种期权投资策略 ([美]布莱恩·奥弗比) (z-lib.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- 第一部 期權基礎
- 第1章 期權是什麼
- 第2章 Greeks 入門（Delta/Gamma/Theta/Vega）
- 第3章 隱含波動率與期權定價
- 第二部 方向性策略
- 第4章 Long Call / Long Put
- 第5章 Covered Call
- 第6章 Protective Put
- 第7章 Collar / Fence
- 第三部 價差策略
- 第8章 Bull Spread (Call/Put)
- 第9章 Bear Spread (Call/Put)
- 第10章 Calendar Spread
- 第11章 Diagonal Spread
- 第四部 中性與波動率策略
- 第12章 Long Straddle / Strangle
- 第13章 Short Straddle / Strangle
- 第14章 Butterfly (Call/Put/Iron)
- 第15章 Iron Condor
- 第16章 Ratio Spread
- 第五部 合成策略
- 第17章 Synthetic Long/Short Stock
- 第18章 Conversion / Reversal
- 第六部 高階策略
- 第19章 Diagonal Calendar
- 第20章 Double Diagonal
- 第21章 事件驅動期權交易（Earnings、FOMC）
- 第七部 40 種策略完整速查表

### TL;DR (≤120字)
奧弗比把期權策略從 4 大類擴展到 40 種具體組合，每個策略配 payoff 圖 + Greeks 特性 + 適用市場觀點 + 風險來源。可視為「期權策略辭典」，不求深度求廣度，適合已經學過基本 Greeks 想系統了解所有組合可能的中階讀者。簡中翻譯完整，適合中國/華語期權交易者。

### 核心本質 (3-5 條)
1. **40 種策略本質是 4 基本單元的排列組合**（本質，第一部） — Long Call、Short Call、Long Put、Short Put 是四個原子；所有複雜策略都是這四個的疊加。理解此本質可推導任何 payoff 圖不需死背。
2. **Payoff 圖只看到輸贏範圍，Greeks 才是動態風險**（本質，第 2 章） — 散戶常只看 payoff 到期圖忽略建倉後每日 delta/theta 變化；專業交易員全程管理 Greeks，過程比結果重要。這區分零售與機構玩家。
3. **隱含波動率環境決定策略選擇**（本質，第 3 章） — 高 IV 環境（VIX > 25）傾向賣方（IronCondor、ShortStraddle）、低 IV 環境（VIX < 15）傾向買方（LongStraddle、Calendar）；不依 IV 選策略 = 盲目下注。
4. **Calendar/Diagonal 是 time decay 與 IV term structure 的複合玩法**（本質，第 10、11 章） — 賣近月買遠月 = 賺近月 theta 衰減更快 + 遠月 vega 保護；這是專業做市商常用結構，零售認識者少但回報穩定。
5. **合成策略揭露期權與現股的等價關係**（本質，第 17、18 章） — 買 Call + 賣 Put = 合成多頭現股；理解這個 put-call parity 可檢查任何策略的套利機會，也能化解「我該買股還是買 Call」的困惑（可能等價）。

### 可用戰術/策略
- **Covered Call 月收租**：持有 ETF/高配息股 + 每月賣 OTM delta 0.2 Call；月收 0.5-1% 權利金，若被 call away 即鎖利出場。
- **Iron Condor 震盪市月收**：賣 delta ±0.15 call/put spread、買 +100bp OTM 保護；月均 0.5-1%，最大虧 8-10%。
- **Calendar Spread 事件前**：事件前賣當月 + 買下月 ATM call/put；賺事件後當月 IV crush，下月 IV 相對穩定。
- **Diagonal Double**：Call/Put 兩側各建 diagonal、組成箱型結構；在 IV 高時建倉、標的窄幅震盪時收 theta + 波動率回歸 vega。
- **事件 Straddle**：財報/FOMC 前買 ATM straddle；若 IV 未過度反映預期則賺事件實際波動；缺點 IV crush 可吃一半利潤。

### 盲點 / 反例 / 適用邊界
- **策略百科全書式排列但缺少情境判斷指南**：書列 40 策略但沒明確說「在什麼市場條件用哪個」，讀者需自行判斷。
- **Greeks 動態管理淺**：第 2 章講了 Greeks 但全書後續策略主要用 payoff 圖分析，缺少 Greek 變化的動態案例。
- **事件驅動章節薄**：Earnings、FOMC 是期權交易 alpha 集中區，書中僅一章略談，遠不如 Augen《Option Trading》深入。
- **美股單市場**：全書以 S&P / 個股期權為例，對指數期權、ETF 期權、中國 50ETF 期權的差異未涵蓋。
- **缺少實盤 PnL 樣本**：每策略展示理論 payoff，但沒統計實盤長期表現；讀者易錯估策略穩定性。

### 與 Edward 既有知識的連結
- **對齊 ZP 期權模組**：本書可作為 ZP 期權策略庫的完整枚舉，40 個策略皆可 formalize 為 Python class；選擇權自營系統必備參考。
- **延伸既有 DNA**：§4 階段性完成——Covered Call、Iron Condor 等收租型策略符合「每月 0.5-1%穩健現金流」的經濟自給路徑。
- **衝突點**：奧弗比偏展示性多數策略，Taleb 警告賣方策略尾部風險；Edward 需在收租（穩健）與 long vol（反脆弱）間平衡。
- **可挖金礦**：附錄 40 種策略速查表可直接轉成 ZP/options/strategy_library/ 的 YAML 目錄，作為策略選擇 UI 的底層資料。
- **對接 Natenberg Option Volatility and Pricing**：Natenberg 是 quantitative 深度派，奧弗比是 practitioner 廣度派；兩書組合可得「數學基礎 + 策略枚舉」完整教材。
