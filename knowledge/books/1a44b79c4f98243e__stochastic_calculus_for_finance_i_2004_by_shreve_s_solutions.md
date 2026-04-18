## Stochastic Calculus for Finance I, 2004 — Shreve S. - Solutions_2
**來源**: E:/書籍/Stochastic Calculus for Finance I, 2004, by Shreve S. - Solutions_2.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Chapter 1: −→1.1: Since S1(H) = uS0, S1(T) = dS0, X1(H) = ∆0S0(u −(1 + r)) and X1(T) = ∆0S0(d −(1 + r)). Therefore, X1(H) positive implies X1(T) negative and vice-versa.**
  - Chapter 2: −→2.1: (i) A and A∁are disjoint and their union is the whole space. Therefore
  - Chapter 3: −→3.1 (i) Since eP > 0, Z > 0. Therefore
  - Chapter 4: −→4.1 (ii) V C
  - Chapter 5: −→5.1 (i) We need the following property: If X and Y are independent r.v. then E(XY ) = E(X)E(Y ).

### TL;DR (≤120字)
本書屬於 statistics evidence based 範疇,作者 Shreve S. - Solutions_2 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

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
