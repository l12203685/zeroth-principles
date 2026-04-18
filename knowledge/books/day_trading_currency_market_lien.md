## Day Trading and Swing Trading the Currency Market — Kathy Lien
**來源**: E:/書籍/Day Trading and Swing Trading the Currency Market Technical and Fundamental Strategies to Profit from Market Moves.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Chapter 1 Foreign Exchange - The Fastest-Growing Market of Our Time
- Chapter 2 Historical Events in the FX Market
- Chapter 3 What Moves the Currency Market in the Long Term?
- Chapter 4 What Moves the Market in the Short Term?
- Chapter 5 What Are the Best Times to Trade for Individual Currency Pairs?
- Chapter 6 What Are Currency Correlations and How Do Traders Use Them?
- Chapter 7 Seasonality - How It Applies to the FX Market
- Chapter 8 Trade Parameters for Different Market Conditions
- Chapter 9 Technical Trading Strategies
- Chapter 10 Fundamental Trading Strategies
- Chapter 11 How to Trade Like a Hedge Fund Manager
- Chapter 12 Profiles and Unique Characteristics of Major Currency Pairs

### TL;DR (≤120字)
Kathy Lien (DailyFX 首席分析師) 把 FX 交易拆成三個時間尺度——長期由 capital flow + 央行政策決定，短期由 news + technical 驅動，intraday 由 session overlap + 流動性決定。是專業 FX trader 最完整的散戶入門書：涵蓋 major pair 特質、交易時段、correlation、季節性、central bank 反應。

### 核心本質 (3-5 條)
1. **FX 是最大 + 最分散的市場**（本質，Ch1） — 日均交易量 $7+ trillion，24 小時交易，無單一主導機構，相對股票市場極難 manipulated。這決定了 FX 策略必須依賴 edge in speed, information, or discipline，不能依賴 insider info。
2. **三時間尺度驅動力**（本質，Ch3-5） — 長期：利率差 + GDP + 經常帳（數月到數年）。短期：央行 statement + NFP + CPI（數日到數週）。Intraday：London-NY overlap + liquidity gaps（數分鐘到數小時）。散戶最常見錯誤是用 intraday 策略做 swing trade 或反之。
3. **Currency Correlations 非穩態但 exploitable**（本質，Ch6） — EUR/USD 和 USD/CHF 長期 -0.9 correlation；AUD/USD 和 oil/gold 有 +0.6 correlation；但 regime change 時 correlation 可瞬間反轉。實務上用 rolling 20-day correlation 監測，突破 1σ 外進場 mean-reversion。
4. **Session Overlap = 流動性黃金期**（本質，Ch5） — 倫敦（03:00-12:00 EST）與紐約（08:00-17:00 EST）overlap 的 08:00-12:00 是主要 FX 行情時段，占日成交量 40%+。亞洲時段（19:00-04:00 EST）僅 JPY crosses 有明顯波動。選擇交易時段的 alpha 大於選策略。
5. **Central Bank Reaction Function**（本質，Ch4, Ch10） — 每家央行對 inflation、employment、currency strength 的反應不同：Fed = 雙目標（物價+就業）；ECB = 純通膨（2%）；BOJ = 低利率維持；BOC = 匯率容忍高。讀懂每家央行的 policy rule 後，data release 的方向比 level 更易預測。

### 可用戰術/策略
- **Carry Trade with Momentum Filter**：long 高利率 currency + short 低利率 currency，但加入 3-month momentum 過濾；只在 trend 順 carry 方向時建倉，危機來臨前 momentum 先翻，自然 close carry。
- **News Release Fade**：NFP/CPI/FOMC 數據發布後 15-30 分鐘的 overreaction，常有 retrace；進場條件：數據與 consensus 相差 >1σ 且價格移動 >50 pip；目標 30-50% retracement。
- **Session Breakout Strategy**：倫敦開盤前 2 小時的 high-low range，記錄後突破 + 1 ATR 進場；stop = range midpoint；target = range × 1.5。
- **Correlation Arb**：當 EUR/USD 和 USD/CHF correlation breaks below -0.8（正常值 -0.95），建 long EUR/USD + long USD/CHF；等 correlation 修復。
- **Hedge Fund Style Positioning**：用 CFTC COT (Commitment of Traders) report 監測 speculator 淨部位；extreme positioning（>90% percentile）是 contrarian 信號。

### 盲點 / 反例 / 適用邊界
- **2008 前出版，未涵蓋 post-GFC 環境** — QE、NIRP、central bank 干預頻率上升後，傳統 interest rate parity 常失效；2014-2020 USD strengthening 與利率差脫鉤是例外常態。
- **Retail broker spread 吞噬 alpha** — 書中範例假設 0.5-2 pip spread；實際 retail broker spread + commission 常 3-5 pip，把短線策略 edge 吃掉。
- **無 DMA / ECN 區分** — 當前 retail 應用 ECN broker（Interactive Brokers, OANDA），與 MT4 retail broker（有 dealing desk，可能 stop hunting）的 execution 差異書中不討論。
- **Cryptocurrency 興起未涵蓋** — BTC、ETH、USDT 的跨市場 FX 交易模式（spot vs perp, 8-hour funding rate）書中完全沒有。
- **情緒指標現代化** — 書中提 COT 但沒提社交媒體情緒指標（Twitter sentiment、Google Trends）、retail broker positioning data（OANDA positions），2020 後這些成為重要 alpha。

### 與 Edward 既有知識的連結
- **對齊 ZP B1 經濟自給**：FX 是 Edward 可能 diversify 的 alpha 來源之一，流動性比股票高、交易成本低；但需注意 retail broker 陷阱。
- **對應 Trading Strategies in Futures**：FX carry 是該論文集的三大 alpha 之一；Lien 提供實務操作細節，論文提供 statistical validation。
- **衝突 Natenberg / Augen**：Lien 偏 directional / macro，Natenberg/Augen 偏 volatility；Edward 應根據自身優勢選擇——有 macro research 資源用 FX，有 option 定價能力用 vol。
- **可挖金礦**：Ch12 Major Currency Pair 特質可作為 Edward 的 currency notebook——每對 pair 的 driver、典型波動、best session、central bank 反應；整理成 `ZP/fx/currency_profiles/`。
- **DNA §2 Work Model 延伸**：FX 24 小時市場與 Edward 數位永生樹的「持續運行」特質對應；可設計自動化 FX 策略配合 dashboard 監控。
- **香港/台北時區優勢**：Lien 提 Asia session 流動性差，但 Tokyo 開盤有特定 JPY 機會；Edward 在台北時間適合做 Asia-London 轉換期（14:00-16:00 台北時間）。
