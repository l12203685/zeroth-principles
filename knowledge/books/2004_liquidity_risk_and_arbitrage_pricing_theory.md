## Liquidity Risk and Arbitrage Pricing Theory — Umut Çetin, Robert A. Jarrow, Philip Protter
**來源**: E:/投資交易/參考書籍/2004 Liquidity risk and arbitrage pricing theory.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **1 Introduction** (frictionless + competitive 假設的缺口、liquidity risk 定位)
- **2 The Model** (stochastic supply curve indexed by trade size)
- **3 Self-Financing Trading Strategies** (在 supply curve 下的新定義)
- **4 First Fundamental Theorem of Asset Pricing (generalised)** (無套利 ↔ 存在等價測度使 zero-net-trade 成為 martingale)
- **5 Second Fundamental Theorem** (失敗;weakening:approximately complete)
- **6 Derivative Pricing in Approximately Complete Markets**
- **7 Extensions & Relation to Transaction Cost / Large-Trader Models**
- **8 Conclusion / Open Problems** (bid-ask spread modelling、portfolio performance 重新定義)

### TL;DR (≤120字)
將 liquidity risk 建為「隨量指數化的 stochastic supply curve」,保留 price-taking 但容許量價彈性。證明第一基本定理推廣成立(無套利 ↔ 零交易點 martingale),第二定理失效但可弱化為「approximately complete」。在近完整市場中,連續且有限變差策略可完全消除 liquidity 成本,使衍生品價格仍等於經典無摩擦價格 — 但避險策略必須改寫。

### 核心本質 (3-5 條, 每條 50-120字)
1. **Supply curve > bid-ask spread 的抽象正義** — 不用「一個 bid 一個 ask」,而用「一個連續函數 S(t,x)=價格取決於時間與交易量」描述市場真實樣貌。bid-ask 只是 x=-ε 與 x=+ε 的特例,此框架自然推廣到任意 size 的滑點結構。
2. **無套利 + 獨特 martingale measure ≠ 完整市場** — 傳統第二基本定理被打破;在 liquidity risk 下市場只能是「近似完整」(L² 意義下任意隨機變數可被近似複製)。這對實務意義重大:定價模型可信,但 perfect replication 不存在。
3. **連續有限變差策略可完全消除 liquidity cost** — 數學上的神奇結果:若把大單切成無限多細小連續交易,因 supply curve 是 C²,總成本在連續極限下消失。這是理論極限,實務受最小交易單位 + 時間延遲 + 自主參與者限制。
4. **Portfolio value 不唯一,至少三種經濟意義解釋** — marked-to-market / 累積成本 / 清算價值三者在 liquidity 下可發散。傳統 "portfolio value" 實為 mark-to-market,清算價值通常更低。策略績效評估需明確選擇哪種 value function。
5. **FTAP 的結構在放鬆 "價格接受者" 假設後會徹底改變** — Cetin-Jarrow-Protter 保留 price-taking,Bank-Baum / Jarrow 1994 放鬆後出現「市場操縱」問題。理論選擇 = 實務自我定位(自己是小散還是大戶)。

### 可用戰術/策略
- **估計自身交易資產的 stochastic supply curve** — 從 tick data (price, size, side) 跑非線性回歸擬合 S(t,x);以此量化每筆交易的 size-dependent 滑點,直接插入策略 PnL 計算。
- **大單切分演算法 = VWAP/TWAP 的理論基礎** — 論文證明連續切分消除成本,實務上 Almgren-Chriss 的執行時程最佳化便是近似實現。B1 自營系統若有大單交易,須 default to splitter 而非 market order。
- **不同 valuation 產生不同決策門檻** — 停損基於 liquidation value (最保守);Risk report 用 mark-to-market;內部績效用 accumulated cost。區分三種 value,避免用錯價格做錯決策。
- **Approximately complete pricing → 實務採 Black-Scholes + liquidity adjustment** — 先以 BS 計算理論價,再以 supply curve 估算 hedging error 的 L² 距離,作為 bid-ask quote 的保守墊。

### 盲點 / 反例 / 適用邊界
- **小交易者假設 (price taker)** — 若你的部位佔市場深度可觀比例,應切到 Bank-Baum 或 Jarrow large-trader 模型。臨界點實務上難界定,但 rule of thumb 是「單筆 > 5% ADV 即非 price taker」。
- **Supply curve C² 假設** — 實務 order book 有離散 tick 與 layer,不是光滑曲線;數學結論(連續切分消成本)是理想化邊界,真實 API latency / minimum order size 產生 lower bound。
- **stochastic supply curve 估計需大量 tick + side 標記資料** — 多數零售市場 data (分鐘 K / 日 K) 無法還原此 curve;要從 futures tick 或加密交易所 level-2 拉資料,並應對資料污染 / partial fills。
- **忽略市場結構性風險(停盤、交易所下線)** — supply curve 在 "normal state" 下成立;黑天鵝事件下 curve 會出現跳點或消失,此時任何光滑近似皆失效。

### 與 Edward 既有知識的連結
- 直接支撐 `risk_control_four_layers` L4 (流動性準備):把流動性風險從「備用現金」抽象為「每筆交易的結構性成本」,風險預算可量化分配。
- 補完 Çetin-Rogers 2005 論文(離散時間版本)— 兩篇組合給了連續+離散時間的 liquidity 處理。B1 自營系統 architecture 可採兩種框架對不同頻率策略。
- 延伸 `backtest_methodology`:回測時 PnL 計算必須區分 marked-to-market / liquidation value,單用 mid-price PnL 會高估策略;可引入 supply-curve-based fill simulator 作為標準回測引擎升級。
- 對應 Wilmott FAQ Q36 & Q47 (complete markets & calibration):FAQ 只提及不完整市場概念,本文給出具體數學建構,供自營系統直接採用。
