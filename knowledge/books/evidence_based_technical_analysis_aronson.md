## Evidence-Based Technical Analysis — David R. Aronson
**來源**: E:/書籍/Evidence-Based Technical Analysis, David R. Aronson.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **Part I: Methodological, Psychological, Philosophical, and Statistical Foundations**
  - Chapter 1: Objective Rules and Their Evaluation
  - Chapter 2: The Illusory Validity of Subjective Technical Analysis
  - Chapter 3: The Scientific Method and Technical Analysis
  - Chapter 4: Statistical Analysis
  - Chapter 5: Hypothesis Tests and Confidence Intervals
  - Chapter 6: Data-Mining Bias: The Fool's Gold of Objective TA
  - Chapter 7: Theories of Nonrandom Price Motion
- **Part II: Case Study: Signal Rules for the S&P 500 Index**
  - Chapter 8: Case Study of Rule Data Mining for the S&P 500
  - Chapter 9: Case Study Results and the Future of TA

### TL;DR
Aronson 對主觀技術分析的 528 頁統計清算書。核心主張:傳統 TA 是「前科學」敘事信仰,必須用 scientific method + 假說檢定 + Monte Carlo permutation 檢驗 6400+ 條規則,才能區分真 edge 與資料挖掘偏誤。書末對 S&P 500 完整案例:在校正 data-mining bias 後絕大多數 TA 規則無統計顯著性。

### 核心本質
1. **主觀 TA = 認知偏誤產生器** — Ch.1-2 證明:人類在隨機走勢會「看見」模式 (pareidolia),加上後見之明 + 確認偏誤,必然產出「有效」的圖表派說法。這是心理學結構限制,只能用「客觀、可編碼、可回測」規則取代。
2. **Data-Mining Bias 是 TA 的 fool's gold** — 測 1000 條規則,即使全無效,純機率也讓最佳那條達 95% 信心水準。Aronson 用 White 的 Reality Check + Masters 的 Monte Carlo permutation 把 p-value 校正到整個搜尋空間,揭露大部分「發現」的規則是抽樣垃圾。
3. **科學方法是唯一可累積的知識生產流程** — 假說 → 可證偽 → 實驗 → 統計推論 → 保留/拒絕。TA 界長期缺此紀律,因此兩百年無法累積 domain knowledge;本書把 philosophy of science 植入交易技術。
4. **TA 規則必須客觀、可編碼、可參數化** — 只有機械化規則能被統計檢定,需要「交易員判斷」的訊號 (頭肩頂像不像) 本質無法驗證,無法累積知識。是對主觀派結構性否定,不是風格差異。
5. **非隨機價格運動需明確理論支撐** — Ch.7 整理動量、均值回歸、風險溢酬、行為偏誤、microstructure 等可能源;策略若無法對應其中之一,大概率只是 data mining 幻覺。Edge 需 theory + evidence 雙柱。

### 可用戰術/策略
- **Monte Carlo permutation test**:把每日報酬打亂 1000 次重套規則,原始報酬需超 95th percentile 才算 edge。
- **White Reality Check / Hansen SPA**:批量檢驗多規則時校正 family-wise error rate,避免 multiple testing fallacy。
- **Trend-follow 與 mean-reversion 分離檢驗**:拆單維度驗證,不混用指標。
- **Detrending benchmarking**:策略報酬需扣 position bias (long-bias 時 bull market 自帶報酬) 才是真 TA edge。

### 盲點 / 反例 / 適用邊界
- **全書偏嚴厲,可能矯枉過正**:Aronson 判幾乎所有 TA 死,但現實中有些規則 (52-week high breakout, Jegadeesh-Titman momentum) 確有邊際顯著性。過度套用會把真實微弱 edge 也排除。
- **統計顯著 ≠ 經濟顯著**:通過 permutation 的規則可能 edge 太小 (年 alpha 0.5%),交易成本就吃掉。
- **適用邊界:流動性深、歷史長的主流市場** (SPX, 主要期貨)。小型股、低頻資料無法做 1000 次 permutation。

### 與 Edward 既有知識的連結
- 核心銜接 **bias_toward_inaction**:整套方法論就是「缺乏證據就不下注」的操作化,與零式第 5 公理同構——未通過 Reality Check = no edge = no action。
- 呼應 **population_exploit**:Ch.7「非隨機源」理論框架正是「群體系統性誤判」的命名,可補充 ZP population_exploit.md 的機制清單。
- 強化 **backtest_methodology**:Monte Carlo permutation + White Reality Check 應列為 ZP 回測 SOP 必經門檻,與 Davey 流程漏斗 + Halls-Moore walk-forward 形成三層防線。
