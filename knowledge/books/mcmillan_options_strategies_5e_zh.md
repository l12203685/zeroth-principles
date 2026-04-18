## 期权投资策略 原书第 5 版 — Lawrence G. McMillan (劳伦斯·麦克米伦) 简中
**來源**: E:/書籍/期权投资策略 原书第5版 劳伦斯 G.麦克米伦著 王琦译 机械工业.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- 第一部 股票期權策略
- 第1章 股票期權基礎
- 第2章 Covered Call Writing
- 第3章 Call Buying
- 第4章 其他 Call Purchasing 策略
- 第5章 Naked Call Writing
- 第6章 Ratio Call Writing
- 第7章 Bull Spread
- 第8章 Bear Spread (Calls/Puts)
- 第9章 Calendar Spread
- 第10章 Butterfly Spread
- 第11章 Ratio/Backspread
- 第12章 Put Buying
- 第13章 Put Writing
- 第14章 組合策略（Straddle/Strangle/Combination）
- 第二部 指數期權與期貨期權
- 第15章 指數期權特性
- 第16章 指數期權套利
- 第17章 期貨期權策略
- 第三部 進階題
- 第18章 動態對沖
- 第19章 事件驅動交易
- 第20章 投資組合保險與波動率交易
- 第21章 稅務考量

### TL;DR (≤120字)
McMillan 被尊為現代期權策略聖經，第 5 版涵蓋 21 章 1000+ 頁。相較 Natenberg 偏數學、奧弗比偏目錄，McMillan 是「深度 + 廣度 + 實戰經驗」三者平衡；每個策略附多情境分析（股價上漲/下跌/橫盤、IV 升降）與調整技巧（roll、adjust、close）。是美國期權專業交易員案頭必備。

### 核心本質 (3-5 條)
1. **所有策略都有「建倉後管理」環節**（本質，全書貫穿） — McMillan 一再強調：期權策略的成敗 50% 在進場、50% 在後續管理（roll、adjust、partial close）；多數散戶書只教進場，McMillan 每章都談如何在不同情境下 adjust。
2. **Covered Call Writing 是期權世界的「入門+永恆」策略**（本質，第 2 章） — 第 2 章佔 60 頁，細致到標的選擇、Strike 選擇、time to expiry、early assignment 風險；這反映 Covered Call 是機構/家族辦公室最廣泛使用的期權策略，值得新手反覆研讀。
3. **Ratio Strategies 是散戶難用但專業愛用**（本質，第 6、11 章） — Ratio Call Writing（賣 2 call 買 1 股）、Backspread（買 2 賣 1）看似複雜但在特定 IV 環境下 ROI 高於普通 spread；McMillan 詳解其 delta/gamma 動態。
4. **指數期權的現金交割改變了所有假設**（本質，第 15-16 章） — 現金交割避免 early assignment 風險、允許歐式定價；指數期權的 IV skew 通常比個股平滑、適合 Iron Condor 類策略。
5. **期貨期權的成本結構與股票期權大不同**（本質，第 17 章） — 期貨期權用 Black-76 而非 Black-Scholes、保證金計算不同、時間衰減對 underlying vs futures 的敏感度有別；套用股票期權直覺會踩坑。

### 可用戰術/策略
- **Covered Call Writing 系統版**：持倉高 beta 股票 + 月度賣 OTM delta 0.30-0.35 call；若股價漲破 strike roll 到更高 strike 更遠月；統計長期 ROI 約 10-15%。
- **Ratio Put Spread**：買 1 當月 ATM put + 賣 2 當月 OTM put（-5%）；低 IV 時建倉，賺溫和下跌的非對稱 payoff。
- **Iron Condor + 動態調整**：初始 delta 中性、若一側被威脅則 roll untested side 近價以收更多權利金；McMillan 提供 IV crush 計算模板。
- **Calendar Spread 季報前**：同 strike 賣當月買下月，事件前建倉賺 IV crush；需注意若股票大幅跳空可能雙邊受傷。
- **事件交易框架**：前 5 日建立 straddle/strangle 賺 IV expansion、事件前 1 日退出（避免 IV crush）；適用 Earnings、FDA 審批、法庭判決等。

### 盲點 / 反例 / 適用邊界
- **書長 1000+ 頁閱讀門檻**：深度廣度俱佳但重量可怕；散戶易讀到第三章就放棄。
- **偏美股與美指**：書中案例幾乎全是美國個股 + SPX/OEX；對中國 50ETF 期權、台指選擇權、德指 DAX 期權需自行適配。
- **稅務章節過時**：第 21 章以美國 IRS 稅法為主，且 2004 年版後美國對期權稅制多次變化；跨國讀者完全不適用。
- **數學基礎偏淺**：Black-Scholes 公式一筆帶過、Greeks 動態推導不深；要進階需補 Natenberg / Hull。
- **早期章節略過時**：1980-1990 年代案例多，近 10 年低 IV 環境下的 Covered Call 回報與書中描述有落差。

### 與 Edward 既有知識的連結
- **對齊 ZP 期權模組**：McMillan 第 2 章 Covered Call 深度論述可直接作為 ZP 第一個 production option strategy 的詳細規格書。
- **延伸既有 DNA**：§4 階段性完成——McMillan 強調「建倉後管理 50%」對應 Edward 永生樹「每個分支需持續照料」的哲學。
- **衝突點**：McMillan 偏傳統規則式策略，Kelly-Xiu / Lopez de Prado 推 ML 動態定價；Edward 可採 McMillan 做結構 baseline、ML 做 alpha overlay。
- **可挖金礦**：第 18 章動態對沖 + 第 20 章投資組合保險的 delta 管理模板可整合進 ZP 所有期權策略的 risk engine。
- **對接 Natenberg / Bennett**：Natenberg 深數學、Bennett 深交易員實戰、McMillan 深策略組合+管理；三本合起來覆蓋 100% 期權領域。
