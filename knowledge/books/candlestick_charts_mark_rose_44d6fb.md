## Everything you wanted to know about candlestick charts — Mark Rose
**來源**: Candlestick Charts.pdf (入門電子書, 22 pages)  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **Chapter 1. What is a candlestick chart?**
- **Chapter 2. Candlestick shapes**
  - Anatomy of a candle
  - Doji
  - Marubozo
- **Chapter 3. Candlestick Patterns**
  - Harami (bullish / bearish)
  - Hammer / Hanging Man
  - Inverted Hammer / Shooting Star
  - Engulfing (bullish / bearish)
  - Morning Star / Evening Star
  - Three White Soldiers / Three Black Crows
  - Piercing Line / Dark Cloud Cover
- **Chapter 4. The history of candlestick charts**
- **Conclusion**
- **Candlestick Cheat Sheet**

### TL;DR
22 頁入門小冊,系統整理 K 棒單根形態(Doji、Marubozu)+ 兩根以上組合形態(Harami、Hammer、Engulfing、Morning/Evening Star、Three Soldiers/Crows 等)+ 每個形態的「可靠 vs 不可靠」判讀。價值在於「K 棒是情緒 snapshot,不是預測工具」的心法建立。

### 核心本質
1. **K 棒是情緒視覺化,非預測工具** — 作者反覆強調 candlestick 的資訊來自 open/close/high/low 四點的「多空博弈痕跡」,不是未來走勢的因果預測;一根 Doji 只告訴你「多空今日打平」,不保證明日反轉。這與技術分析「訊號 = 預測」的常見誤解相反。
2. **單根形態需要「位置 context」才有意義** — Hammer 在上升中段出現無意義,在 downtrend 底部出現才是潛在反轉訊號;Doji 在橫盤無訊號,在趨勢極端才是 indecision。作者區分「形態本身 vs 形態+位置」,避免初階交易者機械看圖。
3. **兩根以上組合形態優於單根** — Engulfing、Morning Star、Three Black Crows 等多根形態提供「確認機制」——第二根/第三根驗證第一根的訊號,過濾隨機噪音。單根形態勝率低,組合形態勝率顯著提升。
4. **「可靠形態」vs「不可靠形態」分層** — 作者明確指出部分形態(如 Three Soldiers/Crows、Engulfing)歷史勝率較高,另一些(如 Inverted Hammer)實務上常失效,不應等權對待。這是經驗沉澱的分層,避免把教科書訊號一視同仁。
5. **Candlestick ≠ 完整交易系統** — 結論強調 K 棒是 confirmation tool,必須搭配 indicator (RSI, MACD)、price channel、volume 才能進場;單靠 K 棒交易是誤用,正確角色是「臨門一腳的確認」而非「獨立訊號源」。

### 可用戰術/策略
- **Doji + channel 邊界**:Doji 出現在 price channel 上沿 → 熊背離候選 entry;下沿 → 多頭背離候選。避免中段 Doji 亂操作。
- **Engulfing 確認規則**:bullish engulfing 需滿足「第二根開於第一根收盤下、收於第一根開盤上」且成交量放大,才是可靠訊號;形似但量縮的 engulfing 直接忽略。
- **Morning Star 三根濾網**:星線小實體 + 位置在下降末端 + 第三根收於第一根實體中點以上,三條件全符才進場,任何一條不符就等下個訊號。
- **Three Soldiers/Crows 入場門檻**:連續三根同向強實體、逐根高點/低點遞進、相對前段成交量放大 → 趨勢延續訊號,非反轉。

### 盲點 / 反例 / 適用邊界
- **缺乏勝率的實證數據**:書中未提供回測統計(各形態歷史勝率、樣本數、market regime 分層),讀者只能靠作者經驗判讀,違反 Aronson 的「evidence-based」原則。
- **適用市場未明示**:形態在不同市場(主要股指 vs 小型股 vs crypto vs FX)的可靠性差異顯著,作者以籠統的「price chart」為背景,讀者需自行回測驗證。
- **時間框架隱含假設**:多數 pattern 案例用日 K 為例,但在 1 分、5 分 K 的雜訊下,同樣形態的可靠性大幅下降;短線交易者套用本書會 overfit 到噪音。
- **易成「confirmation bias 機器」**:K 棒形態可事後找,幾乎每個趨勢都能挑出 5-10 種「訊號」;無嚴格的訊號定義+量化回測時,容易變成敘事工具。

### 與 Edward 既有知識的連結
- 對照 **Aronson evidence_based_technical_analysis**:本書屬於 Aronson 所批判的「主觀 TA」典型,K 棒形態無嚴格定義、無統計顯著性檢驗;可作為入門視覺語彙,但不應作為可回測策略基礎。
- 補強 **information_asymmetry_action**:K 棒是所有交易者同樣看得見的公開資訊,edge 不在「看得到形態」而在「如何與其他 edge (量能、order flow、fundamental) 疊加」;純 K 棒策略幾乎無 edge。
- 呼應 **bias_toward_inaction**:作者反覆要求「多個條件疊加才進場」與零式第 5 公理同構 — 單一訊號不足以行動,需多重 confirmation 才動;單根 K 棒 = no edge。
- 補充 **backtest_methodology**:要把本書形態轉為可操作策略,需先用 Masters Monte Carlo permutation + White Reality Check 檢驗每個 pattern 的統計顯著性,不能直接 paper-trade。
