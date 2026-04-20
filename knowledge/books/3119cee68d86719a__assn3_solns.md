## assn3-solns — 未標示
**來源**: E:/課程/[3] 數理統計/數統一練習題/assn3-solns.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1. (1.4.21) Suppose a fair 6-sided die is rolled 6 independent t**
- **6.
Since the rolls are independent, the probability that there a**
- **2. (1.4.32) Hunters A and B shoot at a target; their probabiliti**
- **3. Then**
- **4. Therefore there are no solutions to this equation, and no suc**
- **3. (1.5.1) Let a card be selected from an ordinary deck of playi**
- **4. (1.5.9) Consider an urn which contains slips of aper each wit**
- **25. Suppose one slip is drawn at random, let X be the number of t**
- **5. (1.5.10) Let X be a random variable with space D. For a seque**
- **6. (1.6.2) Let a bowl contain 10 chips of the same shape and siz**

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
- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層

<!-- QA_FAIL: extract_below_10k_chars, OCR re-extraction queued -->
