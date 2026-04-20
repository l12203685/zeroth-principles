## Market Risk Analysis Quantitative Methods in Finance, Carol_Alexander — 未標示
**來源**: E:/書籍/Market Risk Analysis Quantitative Methods in Finance, Carol_Alexander.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Market Risk Analysis Volume I**
  - List of Figures
  - List of Tables
  - List of Examples
  - Preface to Volume I
  - I.1 Basic Calculus for Finance
  - I.2 Essential Linear Algebra for Finance
  - I.3 Probability and Statistics
  - I.4 Introduction to Linear Regression
  - I.5 Numerical Methods in Finance
  - I.6 Introduction to Portfolio Theory
  - Statistical Tables

### TL;DR (≤120字)
本書屬於 risk management 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **風險不是波動率,是永久性虧損的機率** — 資金曲線破底就出局,Sharpe 再高也沒用
2. **相關性是偽穩定變數** — 危機時分散投資效果消失,壓力測試必須用歷史尾端而非平均
3. **倉位管理優於預測** — Kelly 公式、Risk Parity 的核心是限制最大虧損,而非追求最大報酬

### 可用戰術/策略

- 用 VaR/CVaR + 壓力情境設定部位上限,結合 drawdown control 動態調整
- 建立相關性矩陣的時間序列監測,快速察覺 regime shift

### 盲點 / 反例 / 適用邊界

- 歷史資料涵蓋的 tail events 有限,需要模型外的 judgment 補足黑天鵝

### 與 Edward 既有知識的連結

- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
- 呼應零式原則 *bias_toward_inaction* — 無邊際即等待,不動也是決策
