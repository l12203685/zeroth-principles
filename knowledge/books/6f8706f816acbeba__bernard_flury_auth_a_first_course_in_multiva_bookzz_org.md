## Bernard_Flury__(auth.)]_A_First_Course_in_Multiva(BookZZ.org) — 未標示
**來源**: E:/書籍/Bernard_Flury__(auth.)]_A_First_Course_in_Multiva(BookZZ.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Chapter 1: Why Multivariate Statistics? Table 1.1. Midge Data**
  - Chapter 1: Why Multivariate Statistics? What if three variables (or more) were to be analyzed? Obviously, things will get somewhat more tricky, because three-dimensional scatterplots are difficult to
  - Chapter 1: Why Multivariate Statistics? Let us briefly discuss yet another aspect of the midge example. Although the data of the two groups appear well-separated in the graph ofantenna length vs. wing
  - Chapter 1: Why Multivariate Statistics? Table 1.2 Head Dimension Data in Millimeters
  - Chapter 1: Why Multivariate Statistics? onto a straight line, one would want to choose the representatives along this line. For p = 6 variables (or even p = 25 as in the original data set), it would be helpful if
  - Chapter 1: Why MultivariateStatistics? the uncertainty inherent in the allocation of any given specimen to the male or the female group, particularly for birds near the dip at wing length 89 to 90 millimeters.
  - Chapter 1: Why Multivariate Statistics? Hours slept under old drug

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
