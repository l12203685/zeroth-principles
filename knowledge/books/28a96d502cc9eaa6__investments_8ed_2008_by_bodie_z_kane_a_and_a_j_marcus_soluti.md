## Investments, 8ed, 2008, by Bodie Z., Kane A. and  A. J. Marcus — Solutions
**來源**: E:/書籍/Investments, 8ed, 2008, by Bodie Z., Kane A. and  A. J. Marcus - Solutions.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1. 
Ultimately, it is true that real assets determine the materia**
- **2. 
Securitization requires access to a large number of potential**
- **3. 
Securitization leads to disintermediation; that is, securitiz**
- **4. 
Financial assets make it easy for large firms to raise the ca**
- **5. 
Even if the firm does not need to issue stock in any particul**
- **9. 
For commercial banks, the ratio is: $107.5/$10,410.9 = 0.010**

### TL;DR (≤120字)
本書屬於 statistics evidence based 範疇,作者 Solutions 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

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
