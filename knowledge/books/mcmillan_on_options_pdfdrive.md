## McMillan on Options (2nd Ed) — Lawrence G. McMillan
**來源**: E:/投資交易/交易學習資料庫/@交易/@選擇權/McMillan on options ( PDFDrive ).pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Ch 1 Option Basics** (futures vs stock options, option pricing)
- **Ch 2 An Overview of Option Strategies** (long/short call-put, spreads, ratios, straddles)
- **Ch 3 Using Options to Construct Equivalent Positions** (synthetic, locked-limit escape, expiration effects, protective puts)
- **Ch 4 The Predictive Power of Options** (volume, open interest, put/call ratio, IV 預測)
- **Ch 5 Trading Volatility as a Speculative Strategy** (long vol vs short vol, straddle/backspread)
- **Ch 6 Mathematical Applications** (delta hedging, Greeks, VIX, volatility skew)
- **Ch 7 The Rest of the Story** (trading mistakes, margin, stop orders, psychology)

### TL;DR (≤120字)
實務派的選擇權交易實戰手冊(非理論書):以真實案例 + 錯誤故事教學,涵蓋 synthetic 等價、選擇權量能預測、波動率交易、Greeks 實務。與 Hull 理論教科書互補 — McMillan 解釋「為什麼市場這樣動 + 如何據此下單」,適合把理論轉為實操的 trader。

### 核心本質 (3-5 條, 每條 50-120字)
1. **選擇權交易的真正 edge 在 volatility 而非 direction** — McMillan 反覆強調:猜方向是 50/50 遊戲,預測波動率(implied vs realized 差距)才有可能長期 edge。賣高隱含 vol、買低隱含 vol,是多數 option pro trader 的核心。
2. **Put/Call ratio 與 option volume 是領先指標,不是落後指標** — Ch4 核心主張:不尋常的 call volume 暴增(尤其 OTM)預示多頭訊號;put/call ratio 反向極值 = 情緒反轉點。此不是機械指標,需配合流動性與事件上下文判斷。
3. **Synthetic equivalence 是風控而非套利工具** — synthetic long = long call + short put (同 strike 同 expiry);若真實 stock locked-limit(跌停)但選擇權仍流動,可透過 synthetic 出場。理解 put-call parity 的每一種重排列 = 每一種「改道出場」路徑。
4. **Long straddle 不是看不懂方向的懶人工具,是精準的 volatility 押注** — 須滿足:(a) 當前 IV 低於 realized vol 預期;(b) 有具體事件催化 (earnings、FOMC);(c) 部位大小容許雙向時間衰減吞噬。McMillan 提供失敗案例警示 naive straddle 會被 theta 磨死。
5. **保護性 put (portfolio insurance) 是「買保險,不是省錢」** — Ch3 後段明確:保護性 put 成本 5-10% 年化;歷史上 90% 時間像「浪費錢」,但 10% 時間救命。心理上須接受「保費」屬性,不然多數人會在 bull market 中途停保,正好在 crash 前裸奔。

### 可用戰術/策略
- **IV rank / IV percentile 作為策略 router 的決策基準** — 當 IV rank > 70% → 賣 option 策略(iron condor、credit spread);IV rank < 30% → 買 option 策略(long straddle、calendar)。可直接實作為 B1 選擇權模組主流程。
- **Option volume 爆量 + price unchanged 作為「knowledgeable money」訊號** — Ch4 的 "flipping the ratio" 技巧:OTM call 大量買入卻 stock price 未動 = insider 或 informed money 預期短期跳漲。跟隨此訊號設定 momentum entry。
- **Covered call / cash-secured put 作為收益策略 baseline** — 持股族寫近月 OTM call 收權利金 (年化 8-15%),現金族寫 OTM put 吸引低點接股。McMillan 書中給具體 strike 選擇與 roll-over 規則。
- **Expiration effects (Ch3) 作為日曆策略** — 月選擇權 expiry week(週五前 1-2 天)有可預測的 pinning effect;可建立「expiry week long gamma」策略捕捉 gamma scalp 機會。
- **Stop-loss 在 option 上不等於 stop-loss 在 stock 上** — Ch7 警告:option 的 stop-loss 可能遭 intraday liquidity 造成 whipsaw;用 delta-based risk limit(當部位 delta 超過 X 才調整)比固定 stop 更適合。

### 盲點 / 反例 / 適用邊界
- **2004 年版本,未涵蓋 0DTE options(日內到期選擇權)爆發** — 2020 後 0DTE 占 SPX 選擇權成交量 >40%,gamma squeeze / weekly pin 動態大幅變化,書中框架需加入 intraday dynamic。
- **強美股/期貨市場範例** — 台股/亞洲選擇權流動性、稅制、交易時段差異大;台指選擇權 (TXO) 的專屬規則(如結算日、價差商品)需另讀在地書籍(如張林忠《選擇權實戰操作》)。
- **偏經驗敘述,統計嚴謹度弱** — 書中 put/call ratio、volume 訊號都有「歷史上看起來 work」陳述但缺 rigorous backtest;需搭配 Aronson、López de Prado 做多重比較校正與 Deflated Sharpe。
- **忽略加密選擇權結構差異** — Deribit、Binance Options 的永續 funding、結算機制、24/7 交易時段使 expiration pinning、theta 計算需另建模型。

### 與 Edward 既有知識的連結
- 補完 Hull 教科書:Hull = 理論定價;McMillan = 實戰執行;Natenberg = 中間的交易者理論。三書組合形成選擇權策略的完整知識棧。
- 對應零式第 2 條 `information_asymmetry_action`:option volume 訊號是「市場參與者的資訊從選擇權 order flow 洩漏出來」;自己若無 fundamental edge,跟隨 informed flow 是次佳選項。
- 連結 `derivative_over_level`:McMillan 的 Ch4 "predictive power" 本質是對選擇權的 二階 derivative (IV change rate、volume change rate) 的利用,而非 stock price level 本身。
- 對 B1 自營交易系統的貢獻:若擴充選擇權模組,McMillan 的 IV rank-based strategy router 與 put/call ratio event-driven entry 可直接 port 為 Python 策略 class;保護性 put 是 portfolio 風險管理的 building block。
