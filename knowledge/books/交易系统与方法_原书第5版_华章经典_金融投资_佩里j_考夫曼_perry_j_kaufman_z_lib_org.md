## 交易系统与方法 (Trading Systems and Methods, 5th Ed) — Perry J. Kaufman
**來源**: E:/書籍/交易系统与方法（原书第5版） (华章经典·金融投资) (佩里J.考夫曼（Perry J.Kaufman）) (z-lib.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **第1章 概述** (技術分析擴張、股票期貨收斂、隨機遊走、全球化)
- **第2章 基本概念和計算方法** (均值、分布、方差/偏度/峰度、標準化風險收益、指數、系統性能度量)
- **第3章 圖表分析** (道氏理論、趨勢線、蠟燭圖)
- **第4章 圖表系統及相關應用技術** (鄧尼根、諾弗里、威科夫)
- **第5章 由事件驅動的行情趨勢** (波段、點數圖、N日突破)
- **第6章 回歸分析** (線性/非線性、ARIMA)
- **第7章 基於時間因子的趨勢運算** (移動平均、指數平滑)
- **第8章 順勢交易系統** (價格通道、多重趨勢、綜合研究)
- **第9章 動量指標和震盪指標**
- **第10章 季節性因素**
- **第11章 循環模式分析** (最大熵)
- **第12章 交易量、未平倉合約、行情寬幅**
- **第13章 利差和套利** (持有成本、股票利差)
- **第14章 行為金融視角下的交易技巧** (COT 報告、事件交易)
- **第15章 行情模式判定方法**
- **第16章 日內交易模式**
- **第17章 自適應技術應用** (AMA、KAMA)
- **第18章 價格分布系統**
- **第19章 多重時間架構** (Elder 三重濾網)
- **第20章 領先性的技術指標** (波動率度量與應用)
- **第21章 交易系統測試** (預期、參數識別、過擬合)
- **第22章 實證分析模式** (極端情境、輪盤賭理論)
- **第23章 風險控制模式** (流動性、金字塔加倉、Kelly)
- **第24章 多元化投資組合的資產配置**
- **附錄** (統計表格、馬可夫鏈、三角回歸)

### TL;DR (≤120字)
系統化交易的百科全書:從技術指標(MA、RSI、布林)到行為金融、從回測到風控,全系統工程覆蓋。核心訊息:任何單一指標無 edge;邊際 edge 在「多指標組合 + 自適應 + 嚴格回測 + 紀律風控」。Kaufman 的 KAMA (Adaptive Moving Average) 與參數穩定性檢驗是書中精華。

### 核心本質 (3-5 條, 每條 50-120字)
1. **系統化交易 = 半自動化+紀律,不是無人化** — 全書隱含主軸:系統的意義在消除情緒介入,而非把賺錢機械化。系統是在「人理解市場 + 機器執行規則」中間找最佳分工;純 black-box 最終都會遇到 regime change 毀滅。
2. **任何指標都有其「適配 regime」,穿越 regime 必失效** — MA 在趨勢市有效,在震盪市反被磨;RSI 在震盪市有效,在強勢突破市反成陷阱。第 17 章 Adaptive 技術的核心是讓參數隨 regime 變(以 volatility / 雜訊 / 趨勢強度為判斷)。
3. **參數優化的敵人是過擬合,解藥是 walk-forward + 參數穩定度檢驗** — 第 21 章系統測試強調:optimise 出的參數若在鄰近參數點表現懸殊,屬於過擬合;穩定參數表現區應是參數空間裡的「高原」而非「尖峰」。這是所有策略工程師必學。
4. **風險控制分層:倉位 → 停損 → 資本曲線 → 資金分配** — 第 23-24 章把風控建為多層級工程:單筆停損 (技術面) → 倉位上限 (Kelly-based) → 策略 equity drawdown 暫停 → 多策略資金配置 (risk-parity 思路)。每層各管一個時間尺度。
5. **利差與套利 = 低相關 alpha 來源** — 第 13 章提醒:純方向策略在多策略組合中容易共振崩潰,spread 與套利策略提供 orthogonal 收益曲線,是 portfolio diversification 真正的非相關 α。

### 可用戰術/策略
- **KAMA (Kaufman Adaptive MA) 直接作為 B1 訊號 building block** — 噪聲比率 = Σ|daily changes| / |cumulative change|;噪聲高時 MA 慢,噪聲低時 MA 快;Python 幾行實現,可替代 EMA 作為趨勢過濾器。
- **N 日突破系統 (第 5 章) 作為 event-driven baseline** — 20 日高/低破位進場的「海龜交易法」變體,簡單到可作 benchmark;任何自研策略須 outperform 此 baseline 才有 edge 意義。
- **季節性 (第 10 章) 作為時序事件因子** — 商品期貨在特定月份歷史平均報酬顯著,結合 COT report (第 14 章) 的持倉極端值,形成「季節 + 持倉」二階段 filter。
- **walk-forward optimisation 模板** — 將回測資料切為 in-sample (訓練) + out-of-sample (驗證) 滾動窗口,每期重新優化;out-of-sample Sharpe 降幅 > in-sample 50% 即判定過擬合,此流程可做為 B1 回測模組強制標準。
- **Adaptive trade sizing = volatility-scaled positions** — 第 20 章波動率交易思路:position size ∝ 1/ATR;目標波動率固定(如 15% 年化),市場 vol 升倉位縮,反之放大,使整體 portfolio vol 穩定。

### 盲點 / 反例 / 適用邊界
- **絕大多數指標均基於「歷史模式會重複」假設,未給嚴謹統計檢驗** — Aronson 的 Evidence-Based Technical Analysis 指出,多數 Kaufman 類指標在嚴格的多重比較校正下無顯著 edge。這本書需搭配 Aronson + López de Prado 看。
- **HFT / 微秒級結構未涵蓋** — 第 16 章日內交易仍以 1-分鐘 K 為主;對 tick-level、order book 動態、market making 不涉及;要做 HFT 需轉向 Harris《Trading and Exchanges》或 Aldridge《High-Frequency Trading》。
- **書中例題以美股/商品為主,直接搬到台股/A 股須考慮漲跌停限制、手續費、稅制差異** — 尤其日內交易成本台股偏高,第 16 章策略直接套用利潤消散。
- **過度倚賴 backtest 結果** — 第 21-22 章雖強調過擬合警告,但仍以 backtest 作為主要 validation。更嚴謹做法需加入 Monte Carlo 擾動測試、bootstrap 抽樣、Deflated Sharpe Ratio (López de Prado)。

### 與 Edward 既有知識的連結
- 直接支撐 B1 自營交易系統:此書提供 40+ 具體指標公式,每個都可作為 signal building block;建議建 `indicators/` 模組庫,將 KAMA、ATR、突破、動量等封裝為 Python functions。
- 對應零式第 3 條 `meta_strategy_over_strategy`:第 21-24 章的回測、風控、資產配置屬於 meta-strategy 層;策略(第 3-20 章) 是基層。做好 meta 層比單純加更多策略更有效。
- 連結 `bias_toward_inaction`:Adaptive 思維本質是「無 edge 時系統自動減配/退場」,符合零式「no edge → no move」。
- 對應 `backtest_methodology`:第 21-22 章給出了 walk-forward、參數穩定度、資料分割等 best practice,可作為 B1 回測工程規範的起草基礎。
