## How to Make a Digital Currency on a Blockchain Stable — 未標示
**來源**: E:/投資交易/交易學習資料庫/@交易/2. 財務相關知識/papers/How to Make a Digital Currency on a Blockchain Stable.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1 Introduction**
- **2 Blockchain Currency based on Proof of Work**
- **3 Market Price Mechanism of a Blockchain Currency based on Proof of Work**
  - 3.1 Supply and Demand
  - 3.2 Consequences of Proof of Work
- **4 Measures against Positive Demand Shock**
  - 4.1 Limited Target Re-adjustments
  - 4.2 Target Re-adjustments for Positive Shock
- **5 Measures against Negative Demand Shock**
  - 5.1 Two-fold Propositions
  - 5.2 Negative Interests
  - 5.3 Implementation for UTXO Structure
- **6 Simulation**
  - 6.1 Target and Reward Re-adjustments
  - 6.2 Reduction of Supply
- **7 Discussion**
  - 7.1 Responsiveness
  - 7.2 Applicability to Structures other than UTXO
  - 7.3 Deployment
  - 7.4 Sustainability
  - 7.5 Effects of Depreciation
  - 7.6 Effects of Splitting
- **8 Related Work**
  - 8.1 Improvements to Digital Currency Design
  - 8.2 Models of Economics
- **9 Conclusions**

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
