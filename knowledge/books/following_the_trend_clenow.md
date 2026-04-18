# Following the Trend: Diversified Managed Futures Trading — Andreas F. Clenow

### 目錄
1. 核心本質 — Diversified Trend Following 是 CTA 主流策略的 demystification
2. 可用戰術 — 雙 MA crossover、ATR position sizing、year-by-year post-mortem
3. 盲點/反例 — 2010s 後 trend following 長期 drawdown
4. 與 Edward 既有知識的連結

### TL;DR
Clenow (Wiley 2013, 10 章 + 索引，約 240 頁) 是前 Man Investments CIO 寫給零售交易員的 managed futures trend-following 教科書，Curtis Faith（Turtle 學員，Round 1 已讀他的 Way of the Turtle）作序認證。結構：Ch 1 Cross-Asset Trend Following、Ch 2 Futures Data & Tools、Ch 3 Constructing Diversified Futures Strategy、Ch 4 Two Basic Trend-Following Strategies、Ch 5 In-Depth Performance Analysis、Ch 6 Year-by-Year Review（1990-2012，106 頁）、Ch 7 Reverse Engineering the Competition（拆解 Winton、Man AHL、JWM 等 CTA 績效）、Ch 8 Tweaks and Improvements、Ch 9 Practicalities、Ch 10 Final Words of Caution。**Clenow 最大貢獻**：他把 billion-dollar CTA 們守了幾十年的秘密——**「diversified trend following 其實是一套簡單規則」**——完整公開，包含 position sizing、risk parity、跨 20-30 市場的 signal generation。Ch 6 逐年分析讓讀者看到策略在 2001 tech bust、2008、2011 能賺，但在 2012-2017（後文獻 prolonged drawdown）無情被拖入深坑。

### 核心本質
1. **Diversification Across Asset Classes 是主動勝因（Ch 3）**：單一市場 trend following 勝率約 35-40%（低勝率 long tail），跨 20-40 市場（equity index、rates、FX、agricultures、energy、metals）可把 P&L 變平滑——一個市場 drawdown 時另一個上漲。Clenow 實證 5-asset portfolio Sharpe 0.5，30-asset portfolio Sharpe 1.0。Diversification 本質是「找更多獨立 bet」（Fundamental Law of Active Management）。
2. **ATR-Based Position Sizing（Ch 3）**：每個 futures contract 的 $risk per trade = entry_price - stop_loss；要 risk 帳戶 0.5-1% per trade；則 contract_size = (0.5% × account) / ($risk per trade)。這讓不同 vol 市場（原油 vs. 十年期國債）的 dollar exposure 自動 normalize 到等 risk。
3. **Two Core Signals（Ch 4）**：(a) Exponential Moving Average Crossover（50 day vs. 100 day），向上 crossover = long，向下 = short；(b) Donchian Channel Breakout（20 day high/low），突破新高 long、突破新低 short。兩個訊號都是經典 Turtle-era 技術，但關鍵不在 signal 多精巧，而在「diversify enough + size correctly + 堅持 execute」。
4. **Profits Come in Clumps（Ch 5）**：trend following 的 P&L 分布極非正態——長期小虧 (whipsaw) + 偶發大賺 (trends)。1990-2012 期間 15% 的月份貢獻 80% 的 return，其他 85% 的月份淨損。這解釋為何 behavioral discipline 是生存線——大部分時間在虧，心理承受不了就提早出場失去 fat tail upside。
5. **Reverse Engineering CTA（Ch 7）**：Clenow 用 multiple regression 回歸 Winton, Man AHL, Chesapeake 等 CTA monthly return 對「公開可複製的 standard trend following strategy」，R² 普遍 >0.7——意指 "expensive CTA" 的 alpha 多半是 commodity trend exposure，不是真技能。投資人可用 passive 系統以 1/10 成本複製 95% return。

### 可用戰術
1. **Risk Parity Weighting Across Markets（Ch 3.4）**：給每個 market 的 weight ∝ 1/volatility，讓每個 market 貢獻等量 portfolio risk。不做 risk parity 的話 S&P 的 5 day ATR $500 vs. corn 的 ATR $100，portfolio 事實上 80% 由 S&P 驅動。
2. **Rolling Futures 避免 expiry roll 損失（Ch 9）**：contango 市場（e.g., VX, natural gas）roll 從 front to next month 每月虧 1-3%；backwardation 市場（e.g., 2003+ oil, 現今黃金某些時段）roll 賺錢。系統必須加 roll cost 進 backtest，否則 paper return 比 live 高 3-5%/year。
3. **Volatility Targeting at Portfolio Level（Ch 8）**：整體 portfolio 目標 annual vol 15-20%，定期 rebalance 讓 each open position size 隨 market vol 變化——market vol up → size down。這在 2020 Mar crash 時 save portfolio 免於爆倉。
4. **Trade Every Signal, No Discretionary Override（Ch 4）**：系統化 trend following 的紀律——每個信號都 trade，即便「看起來不合理」。人類直覺在 whipsaw 期會迴避低勝率信號，但統計上那些被 override 的信號跟其他一樣有 expected value。全自動化比 semi-manual 長期高 2-3%/year。
5. **Year-by-Year Post-Mortem（Ch 6）**：每年結束強制 review：哪些信號、哪些 market 貢獻 P&L。1990s 股多頭 trend following 靠股指 + bond，2001-03 靠 short equity + long bond，2008 靠 short equity + long 黃金，2011-12 開始 underperform。這 23 年的 history 就是策略的 regime robustness 證據。

### 盲點/反例
1. **2012-2017 trend following 大 drawdown**：Clenow 2013 出版正逢「黃金年代結束」分界——2013-2018 SG Trend Index 下跌 20%+、SocGen CTA index 6 年無新高。原因：央行 QE 壓平波動率、FX 無顯著 trend、股指持續緩牛但無大 correction。Clenow 這本沒預示 post-QE 環境的挑戰。
2. **Futures Only 過於狹窄**：只用 futures 意味著沒 single-stock、沒 options、沒 ETF。現代 CTA 已擴張至 equity market neutral + macro 聚合，純 futures trend 的 capacity 有限（~50 億 USD）。
3. **Monthly rebalance 過於 coarse**：Ch 4 的兩個信號都是 daily 但 rebalance 週期不 explicit。實務上 daily rebalance 可降 drawdown 但提高 turnover cost，trade-off 未充分討論。
4. **沒有 Machine Learning / alternative data**：2020+ CTA 的 edge 越來越來自 alt data（satellite images for oil inventory, credit card spending, sentiment scoring），而非純價格。Clenow 的 pure technical approach 面對 quant CTA 的 AI 升級有 obsolescence 風險。
5. **Australia/Europe 市場偏向**：Clenow 本人在瑞士操作，對 US 市場的 nuances（earnings season、Fed meeting）相對輕描淡寫。US 散戶應用時要自行加入 US-specific 過濾。

### 與 Edward 既有知識的連結
- **對照 Faith《Way of the Turtle》（Round 1）**：Faith 是 1984 Turtle 項目當事人角度（story + rules），Clenow 是 2013 專業投資人角度（systematic + institutional）。Curtis Faith 寫序本身就是承認這本是 Turtle 精神的現代延伸。
- **對照 Davey《Building Winning Algo Trading Systems》（本輪）**：Davey 是個別策略的開發 process（walk-forward + MC），Clenow 是 portfolio-level trend following 的 mechanics。兩者互補：Davey 教怎麼驗一個策略，Clenow 教怎麼 combine 多個策略成 portfolio。
- **對照 Kestner《Quantitative Trading Strategies》（Round 1）**：Kestner 涵蓋各種 quant 策略（包括 trend, mean-reversion, arbitrage），Clenow 專注 trend。Kestner 廣度高，Clenow 深度高。
- **對照 Vince《Handbook of Portfolio Mathematics》（Round 1）**：Vince 的 optimal f + geometric mean 為 Clenow 的 ATR-based sizing 提供理論。實務上 Clenow 用 fixed fractional risk（每筆 1%），與 Vince 的 full optimal f 不同但安全。
- **對照 ZP/strategies/trend_following 架構**：若 ZP 加 trend-following branch，Clenow 的 Ch 3-4 是最小可行範本——diverse futures list + EMA crossover + ATR sizing = MVP。但要先跑 2010-2020 的 paper trade 檢驗 regime robustness，因 post-QE 環境挑戰這套經典。
- **對照 Poker 的 tournament ITM variance**：撲克錦標賽 80% 無獎金 + 偶發大獎類似 trend following 的 clumpy profit distribution。長期心理紀律與 bankroll management 在兩個領域同樣重要——虧連續 20 次 tournament 要能扛住才能等到 final table。
