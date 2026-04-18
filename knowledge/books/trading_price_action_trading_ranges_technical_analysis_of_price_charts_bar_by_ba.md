## Trading Price Action: Trading Ranges — Al Brooks
**來源**: E:/書籍/Price Action/Trading Price Action Trading Ranges Technical Analysis of Price Charts Bar by Bar for the Serious Trader by Al Brooks.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Part I: Breakouts — Transitioning into a New Trend**
  - Ch 1-6 Breakout 進場、初始突破、突破拉回測試、Gap
- **Part II: Magnets — Support and Resistance**
  - Ch 7-10 Measured Moves (Spike-based & Gap-based)、Signal bars 返回、其他 magnets
- **Part III: Pullbacks — Trends Converting to Trading Ranges**
  - Ch 11-20 First Pullback Sequence、Double Top/Bottom Flags、Twenty Gap Bars、Key Inflection Times、ABC Corrections、Wedge、Head & Shoulders
- **Part IV: Trading Ranges**
  - Ch 21-23 如何交易 Trading Range、Tight Trading Ranges、Triangles
- **Part V: Orders and Trade Management**
  - Ch 24 Scalping/Swinging/Trading/Investing
  - Ch 25 Trader's Equation + Directional Probability
  - Ch 26 Need Two Reasons
  - Ch 27-28 Entering on Stops / Limits
  - Ch 29 Protective & Trailing Stops
  - Ch 30 Profit Taking & Targets
  - Ch 31 Scaling In/Out
  - Ch 32 Money Management

### TL;DR (≤120字)
Al Brooks 的 Price Action 三部曲之一,專注震盪市 (Trading Range) 的交易法則。以 5-min SPX/ES 期貨 bar-by-bar 解讀為核心,建立 "signal bar → entry bar → follow-through" 三步決策框架。配合 Trader's Equation (EV = P(win) × profit - P(loss) × stop) 作為每一筆交易前的數學檢驗。

### 核心本質 (3-5 條, 每條 50-120字)
1. **任何交易 = Trader's Equation 正 EV 檢驗** — Ch25 核心:E[trade] = P(win) × Reward - P(loss) × Risk。進場前必須算得出 P(win) (直接經驗估計)、Risk (到 stop 的 ticks)、Reward (到 target 的 ticks)。任何 "感覺好" 但算出負 EV 的交易直接放棄;"感覺差" 但正 EV 的反而要做。
2. **Price Action 本質是「同類 bar 行為的統計歸納」** — 書中 Signal Bars 分類(如 inside bar、outside bar、trend bar、doji bar)不是玄學,是對歷年 5-min bar 反應的經驗性分類。每個分類對應統計上的後續機率 — 這是「把 discretionary trading 量化為概率遊戲」的嘗試。
3. **市場 80% 時間是 Trading Range,只有 20% 是 Trend** — 統計事實:多數時候價格在 channel 內震盪。Breakout 策略 (Part I) 勝率低但賠率高,Trading Range 策略 (Part IV) 勝率高但賠率低 — 兩者長期 EV 可能接近。個性決定選擇。
4. **Magnet (Measured Move) 是可預測的心理靶點** — Ch7-10:市場從突破點往前邁一步後,常會往「等距離的下一步」移動(1:1、1.5:1、2:1 measured move)。這源於 cognitive bias + algo programming — "預期的自我實現" 在短期時間框架下真實有效。
5. **Two reasons rule = 紀律過濾濾波器** — Ch26 「需要兩個理由才進場」:例如同時有 trendline break + signal bar,或 double bottom + higher-low。單一訊號就進場是散戶賠錢主因。這條 rule 把 confirm bias 轉為 strength — 理由必須獨立。

### 可用戰術/策略
- **20-period MA + trendline 作為 trend/range 判斷** — 與 MA 距離、MA 角度、與 trendline 相對位置組合成 regime classifier。B1 系統實作 10 行 Python 即可用,驅動策略開關(range 時用 mean reversion,trend 時用 breakout)。
- **Measured Move target 作為 systematic profit target** — 進場後以「起始 spike 的高度」為單位,第一 target = 1:1 projection;若持倉管理需要多層,1.5:1 和 2:1 作為 trailing target。省去 arbitrary 設 profit target。
- **Scalping vs Swinging 的 trade sizing 分離** — Ch24 主張 scalp 與 swing 分開倉位池;一筆 trade 入場後,拆 1/3 scalp (快速取小利)、1/3 swing (等大波)、1/3 runner (追最終 target)。減低 "全出還是全留" 的心理壓力。
- **Brooks-style Entry 模擬** — 在 B1 回測系統加入 "signal bar + entry bar" 的 structural filter,比純 indicator crossing 多一層噪音過濾;測試 EV 改善是否顯著。

### 盲點 / 反例 / 適用邊界
- **Price action reading 是主觀判斷,標準化困難** — 書中 1147 頁的 bar-by-bar 分析極度經驗性,不同人看同一 chart 可能 classify 成不同 signal bar;回測自動化時必須先寫嚴格的 rule-based classifier,否則 backtest 結果不穩。
- **強 reliance on 5-min chart,其他時間框架需重新驗證** — Brooks 的 "number rules" (如 twenty gap bars) 是在 5-min ES 期貨上得出;移植到日線股票或 tick 資料時,參數與概率分布可能大幅不同。
- **假設市場流動性充足、spread 窄** — 個股 thinly-traded 或 Asian market session 流動性差時,signal bar 可能是 false signal;需另做 liquidity 過濾。
- **缺乏嚴謹統計驗證** — 書中很少給 backtest 結果或統計顯著性;讀者需自行驗證 "Brooks 說這個 pattern 70% 成功" 類陳述。配合 Aronson《Evidence-Based Technical Analysis》校正。

### 與 Edward 既有知識的連結
- 對應零式第 5 條 `bias_toward_inaction`:Ch26 "two reasons" 的紀律 = "沒有雙重 edge 就不動手",符合 no-edge-no-move 原則。
- 連結 `information_asymmetry_action`:Price action 本質是從 order flow 遺留的 bar shape 推斷市場參與者意圖 — 這是對 public data 的另一種資訊萃取,在無 fundamental edge 時的可能 alpha 來源。
- 對應 `backtest_methodology`:Ch25 Trader's Equation 是「個別交易的 pre-mortem 檢驗」,可在 B1 系統實作為每筆 trade 執行前的 gatekeeper。
- 對 B1 自營交易系統的貢獻:Brooks 的 signal bar classifier 可整合入 execution module,作為進場時機精調;Part V 的 order management 策略(stop、trailing、scaling)可作為 exit rules 起草基礎。
