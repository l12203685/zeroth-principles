## Option Trading Tactics with Oliver Velez — Oliver L. Velez
**來源**: E:/投資交易/交易學習資料庫/@交易/@選擇權/Option Trading Tactics with Oliver Velez ( PDFDrive ).pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Introduction: Welcome to Options Trading the Pristine Way
- Chapter 1 The Four Styles of Trading
  - A Look at Available Timeframes
  - The Four Styles (scalper/micro-trader, day trader, swing trader, core trader)
- Chapter 2 The Tools for Options Trading
  - Charting Tools / Technical Tools / Options Tools
- Chapter 3 The Pristine Method
  - Who Won the Battle? / Count Your Way to Profits / When to be a Bull / When to be a Bear
  - Pristine Combinations / Time to Strike / Summary
- Chapter 4 Pristine Options
  - Options Defined / The Advantages / Disadvantages / Types of Options / How the Numbers Work
- Chapter 5 Putting it All Together
- Appendix: Option Pricing / Trading Resource Guide / Recommended Reading

### TL;DR (≤120字)
Velez (Pristine Capital 創辦人、Velez Capital Management CEO) 的獨門 "Pristine Method"：把 candlestick + price action 結構化為可教學框架，再把 option 當槓桿工具放大 directional trade。核心訊息：85% 短線交易者虧損的根源不是知識不夠而是紀律不足；"知 + 行" 結合才是 edge。

### 核心本質 (3-5 條)
1. **Four Trading Styles 的時間尺度區分**（本質，Ch1） — Scalper / Micro（分鐘-小時）、Day Trader（intraday，收盤不留倉）、Swing Trader（2-5 天）、Core Trader（週-月）。每個 style 需要不同 chart timeframe、risk tolerance、capital allocation。混合使用最易失敗——早上 scalp、下午 swing 會讓決策框架互相污染。
2. **Pristine Method = Price Action 結構化**（本質，Ch3） — Velez 把 candlestick pattern 拆解成 "Who Won the Battle?"（多空誰勝）；"Count Your Way to Profits"（計數 bullish/bearish pattern）；"Time to Strike"（多個 pattern 同向 alignment 時進場）。結構化程度比傳統 candlestick 教學高，降低主觀判斷。
3. **Knowledge + Discipline 的 multiplicative 關係**（本質，Intro） — Velez 反覆強調：「knowledge without discipline is dangerous」。高知識低紀律的交易者會用複雜策略自欺欺人；低知識高紀律的交易者至少能堅持簡單策略。最危險是「過度知識」——懂太多反而每單都試不同方法。
4. **Options as Leverage, Not Strategy**（本質，Ch4） — Velez 把 option 當「正確 directional trade 的槓桿放大器」，不當獨立策略。先判斷 stock 方向（Pristine Method），再選 option（ITM call for bullish、OTM put for bearish）；論述「option 策略本身就有 edge」是錯誤認知。
5. **Micro Trading 的社會學意義**（特殊觀點，Intro） — Velez 的願景：把 trading 當 "micro banking" 的平權工具——讓發展中國家（北京、越南、莫斯科、墨西哥）的人透過小資金 trading 脫貧。他的 VCM 模型是自己出資本、trader 承擔訓練與執行、盈虧分成，類似 micro-finance 結構。

### 可用戰術/策略
- **Pristine ABC Pattern**：bullish ABC = higher low → lower high → 突破 higher high；bearish ABC 反向。此為 trend continuation 信號，進場勝率約 60-65%（書中宣稱）。
- **Three Bar Reversal Pattern**：3 根 bearish candle 後 1 根大陽線 engulf 前者 high → bullish reversal；反之 bearish。適合 swing trade 進場。
- **Option Selection Rule**：directional trade 確認後，若 volatility 低買 ATM call / put；若 volatility 高買 ITM（delta 0.7+）降低 theta 影響；避免 OTM（delta <0.3）cheapo lottery。
- **Risk Management 2%**：每單虧損 ≤ 帳戶 2%；跟 Elder 的 Triple Screen 同數字。option 上計算方式 = option loss × contracts / equity。
- **Timeframe Alignment**：daily 趨勢 + 60-min entry + 15-min fine-tune；三 timeframe 都同向才進場。

### 盲點 / 反例 / 適用邊界
- **Pristine Method 缺乏 statistical validation** — 書中以 anecdote 為主，未提供 large-sample backtest；candlestick pattern 的預測力在學術文獻（Bulkowski, Aronson）中多為 marginal。
- **過度依賴 retail trader 視角** — Velez 的方法適合 $5,000-$50,000 帳戶的 retail day trader；大資金（>$1M）無法用 market order 進場，slippage 會吃掉 edge。
- **VCM 商業模式可疑** — 一人 backing 260-1000 traders 的模型，實際是 proprietary firm 用大量 trader 分散風險；對個別 trader 的長期致富幫助有限——多數 payout 被公司抽成。
- **缺 options 數學嚴謹性** — 書中對 Greeks、IV、skew 討論淺嘗輒止；想做 volatility trading 或 spread strategies 需補 Natenberg / Augen / Sinclair。
- **2010 出版，未涵蓋 0DTE / retail option boom** — 2020 Robinhood 熱潮、0DTE SPX 期權普及改變了散戶 option landscape；Velez 的日線 swing 策略在 0DTE 世界需要整體重構。

### 與 Edward 既有知識的連結
- **延伸 Elder《New Trading for a Living》**：Elder 的 Triple Screen + Velez 的 Pristine Method + Augen 的 option adjustment 構成散戶 option trader 三合一技能組。
- **衝突 Bennett Trading Volatility**：Velez 的 directional option 視角 vs Bennett 的 vol / variance 視角；Edward 應按 market regime 切換——trending market 用 Velez，高 IV vol-selling 用 Bennett。
- **DNA §8 決策分工類比**：Velez 的 knowledge + discipline = 規則 + 執行；呼應 Edward-Koko 的 substance-lead + form-defer 分工結構。
- **可挖金礦**：Pristine Method 的 ABC pattern + Three Bar Reversal 可編程自動 scan；用於 `ZP/technical/pattern_scanner/` 模組，每日掃描 S&P 500 成分股給出 bullish/bearish signal list。
- **Poker 類比**：Velez 強調 "knowledge without discipline is dangerous" = poker 的 "tilt management > 技巧"；兩者最大敵人都是情緒化偏離策略。
- **延伸應用**：Velez 的 VCM 模型（公司出資本、trader 出技能）類似自營基金募資 model；Edward 未來若想擴張，可參考但對實際 long-term payout 保持懷疑。
