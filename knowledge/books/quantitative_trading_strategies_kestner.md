## Quantitative Trading Strategies: Harnessing the Power of Quantitative Techniques — Lars Kestner
**來源**: E:/書籍/quantitative-trading-strategies-harnessing-the-power-of-quantitative-techniques-to-create-a-winning-trading-program.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- PROLOGUE
- PART ONE Structural Foundations for Improving Technical Trading
  - Chapter 1 Introduction to Quantitative Trading
  - Chapter 2 An Introduction to Statistics
  - Chapter 3 Creating Trading Strategies
  - Chapter 4 Evaluating Trading Strategy Performance
  - Chapter 5 Performance of Portfolios
  - Chapter 6 Optimizing Parameters and Filtering Trading Signals
- PART TWO Harnessing the Power of Quantitative Techniques to Create a Trading Program
  - Chapter 7 Dissecting Strategies Currently Available
  - Chapter 8 New Ideas on Entries, Exits, and Filters
  - Chapter 9 New Ideas of Markets
  - Chapter 10 Investing in the S&P 500
  - Chapter 11 New Techniques in Money Management
  - Chapter 12 Solving the Trading Puzzle

### TL;DR (≤120字)
Kestner 是 Citadel / Salomon 自營交易員出身，書中核心訊息：量化交易的 alpha 不在進出場信號，而在回測流程的統計嚴謹性 + money management 的數學正確性。他引入 K-Ratio（衡量 equity curve 平滑度）取代 Sharpe，並把 pair trading、yield curve spread、volatility 等 relative value 市場帶入量化策略射程。

### 核心本質 (3-5 條)
1. **K-Ratio > Sharpe Ratio**（本質，第 4 章） — Sharpe 忽略 equity curve 的路徑——兩個相同 Sharpe 的策略，一個平穩上升、一個 V 型回撤再創新高，投資人體感風險天差地別。K-Ratio = (slope of regression) / (standard error of slope) 懲罰 drawdown 深度與時長，更反映實際風險承受度。
2. **Optimization 必須跨越參數穩健性檢驗**（本質，第 6 章） — 多數策略的 optimization 只找歷史最佳參數，Kestner 強調：檢查目標函數在參數空間的形狀——若最佳參數周圍 ±20% 範圍內表現急劇下降，此策略是 curve-fitted；穩健策略應呈現寬闊平頂（plateau）。
3. **Relative Value Markets 擴展 alpha 空間**（本質，第 9 章） — Kestner 率先把 yield curve spread、credit spread、stock pair、commodity substitute 納入量化交易範圍。這些合成資產的 time series 多呈 mean-reverting（相對於單一資產的 trend），alpha 來源與純 directional 策略低相關，是 diversification 新維度。
4. **Money Management 決定 survival**（本質，第 11 章） — Kestner 用「最聰明最大型經理人因未遵守資金管理規則而毀滅」（影射 LTCM）警告：再好的策略加上過度槓桿都歸零。書中提供 fixed fractional、Kelly、Volatility-adjusted 等多種 position sizing 方法的優缺點比較。
5. **One Person, Many Markets**（本質，第 1 章） — 量化交易的 scale 優勢是自動化——策略寫好後增量成本近零，一人可同時在 100+ 市場運行同樣邏輯。這改變了 trader 的 job description：從「精通一個市場」變為「建構可跨市場的信號框架」。

### 可用戰術/策略
- **K-Ratio 取代 Sharpe 作為策略篩選**：K-Ratio > 0.5 為可接受，> 1.0 為優秀；計算方法 = slope(log equity) / stderr(slope)，用 linear regression 在完整時間序列上擬合。
- **Parameter Robustness Grid**：每個參數取 5-7 個值，建立 5D grid 跑完整 backtest；篩選 performance 在 top 25% grid points 中的中位數參數，比「最佳值」更穩健。
- **Pair Trading Implementation**（第 9 章）：找 cointegrated stock pairs（同產業、同市值），計算 spread Z-score，|Z| > 2 進場，|Z| < 0.5 出場；hedge ratio 用動態 Kalman filter 更新。
- **Volatility-Adjusted Position Sizing**：position size ∝ 1 / (20-day realized vol)；相同風險單位橫跨市場，避免高波動市場主導 portfolio。
- **Yield Curve Spread 策略**：監測 2s10s 或 5s30s spread 的歷史分布，spread 達歷史 90% 分位做 flattener，達 10% 分位做 steepener；停損用 spread 絕對值偏離。

### 盲點 / 反例 / 適用邊界
- **2003 年出版，資料老舊** — 書中範例停在 2000 年左右；2008 GFC、2020 COVID 的 crisis regime 下許多策略（pair trading、yield curve）表現迥異；讀者需補 post-2008 實證。
- **K-Ratio 對長期策略偏不利** — K-Ratio 的分母是 slope 的標準誤，長時間序列自然 slope std err 越小；同一策略在 10 年資料的 K-Ratio 可能是 5 年的 2 倍，跨策略比較時需同 horizon。
- **Relative Value 假設 cointegration 穩定** — 書中 pair trading 預設 spread 回歸；但產業結構變化（如某家被併購、破產）會 permanently break cointegration，此時停損規則 saves 資金但策略整體 Sharpe 下降。
- **未涵蓋 execution realism** — 書中大多假設理論價格成交，對 market impact、fill ratio、smart order routing 少有討論；小資金（<10 mil USD）可忽略，大資金（>100 mil USD）會使策略 alpha 減半。
- **過度自信 automation** — "One Person Many Markets" 的 hype 忽略了對無人監控狀況下 bug/data error 的 operational risk；真正 production 系統需要 error monitoring + circuit breaker + manual override。

### 與 Edward 既有知識的連結
- **對齊 ZP 零式本質**：Kestner 的 K-Ratio 體現「路徑品質 > 終點位置」的零式觀點——與 Edward 「stability before maximization」的核心交易哲學一致。
- **延伸 Vince Portfolio Math**：第 11 章 money management 與 Vince 書的 Optimal f 互補——Kestner 偏實務 recipe，Vince 偏理論推導；兩本搭配構成完整的 position sizing 知識架構。
- **衝突 Gibson 長期投資**：Kestner 的 active trading 思維與 Gibson 的 asset allocation 立場相反；Edward 在自營交易與家庭理財應清楚分離——自營用 Kestner，家庭用 Gibson。
- **對應實作**：第 9 章 Relative Value Markets 可直接作為 `ZP/trading/strategies/spreads/` 的 reference；pair trading、yield curve spread 都是低相關、高 Sharpe 的潛在 alpha 來源。
- **可挖金礦**：第 4 章 K-Ratio 公式可立即整合進 ZP 回測框架，作為策略篩選的 primary metric；搭配 Sharpe、Sortino、Calmar 組成 multi-metric evaluation。
- **Poker 類比**：Kestner 的「optimization plateau」概念類似 poker 的「mixed strategy robustness」——單一最佳 decision point 易被 exploit，穩健策略在 strategy space 的一個 plateau 內。
