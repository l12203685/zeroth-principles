## [G._A._Young,_R._L._Smith]_Essentials_of_Statistic(BookFi.org) — 未標示
**來源**: E:/書籍/[G._A._Young,_R._L._Smith]_Essentials_of_Statistic(BookFi.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Binder1.pdf**
  - 00.pdf
  - 01.pdf
  - 02.pdf
  - ... (9 more sections)
- **Binder2.pdf**
  - nlreader.dll@bookid=138968&filename=page_1.pdf
  - nlreader.dll@bookid=138968&filename=page_2.pdf
  - nlreader.dll@bookid=138968&filename=page_3.pdf
  - ... (6 more sections)
- **Binder3.pdf**
  - nlreader.dll@bookid=138968&filename=page_10.pdf
  - nlreader.dll@bookid=138968&filename=page_11.pdf
  - nlreader.dll@bookid=138968&filename=page_12.pdf
  - ... (87 more sections)
- **Binder4.pdf**
  - nlreader.dll@bookid=138968&filename=page_100.pdf
  - nlreader.dll@bookid=138968&filename=page_101.pdf
  - nlreader.dll@bookid=138968&filename=page_102.pdf
  - ... (124 more sections)

### TL;DR (≤120字)
本書屬於 statistics evidence based 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **多次檢驗問題會偽造 alpha** — data mining 若不做 Bonferroni/BH 校正,幾乎任何「策略」都能在歷史上跑贏
2. **統計顯著 ≠ 經濟顯著** — t-stat 3.0 但年化超額 0.3% 在扣手續費後無法存活
3. **前瞻偏誤 (look-ahead bias) 在學術論文與商業回測都普遍** — 特別留意財報日、指數調整日的訊號重建

### 可用戰術/策略

- 採用 white's reality check / stepwise superior predictive ability 做多重檢驗修正
- 所有 backtest 引入交易成本、滑價、融資成本,再看 net Sharpe

### 盲點 / 反例 / 適用邊界

- 統計檢驗預設資料獨立,金融時序高度相關,block bootstrap / stationary bootstrap 才能貼近實際分布

### 與 Edward 既有知識的連結

- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
- 呼應零式原則 *derivative_over_level* — 關注變化率/拐點而非單期水準
