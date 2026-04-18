## ANSWER.FINAL.TERM.EXAM — 未標示
**來源**: E:/課程/[3] 數理統計/數統一考古題/ANSWER.FINAL.TERM.EXAM.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1. Compute p (x) and p (xjy).**
- **2. Compute p (y) and p (yjx).**
- **3. Compute x and 2**
- **4. Compute y and 2**
- **5. Compute , the correlation coe¢ cient of X and Y .**
- **1. Please give the proof in the discrete case.**
- **1. F-distribution with r1 = 4 and r2 = 8. (h)**
- **2. Poisson distribution with parameter m = 3. (b)**
- **3. 2 (4). (d)**
- **4. beta distribution with  = 2 and  = 2. (e)**

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

<!-- QA_FAIL: extract_below_10k_chars, OCR re-extraction queued -->
