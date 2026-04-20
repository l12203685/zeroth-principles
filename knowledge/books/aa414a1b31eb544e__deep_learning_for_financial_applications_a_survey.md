## Deep Learning for Financial Applications  A Survey — 未標示
**來源**: E:/書籍/Deep Learning for Financial Applications  A Survey.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1 Introduction**
- **2 Machine Learning in Finance**
- **3 Deep Learning**
  - 3.1 Deep Multi Layer Perceptron (DMLP)
  - 3.2 Convolutional Neural Networks (CNNs)
  - 3.3 Recurrent Neural Network (RNN)
  - 3.4 Long Short Term Memory (LSTM)
  - 3.5 Restricted Boltzmann Machines (RBMs)
  - 3.6 Deep Belief Networks (DBNs)
  - 3.7 Autoencoders (AEs)
  - 3.8 Other Deep Structures
- **4 Financial Applications**
  - 4.1 Algorithmic Trading
  - 4.2 Risk Assessment
  - 4.3 Fraud Detection
  - 4.4 Portfolio Management
  - 4.5 Asset Pricing and Derivatives Market (options, futures, forward contracts)
  - 4.6 Cryptocurrency and Blockchain Studies
  - 4.7 Financial Sentiment Analysis and Behavioral Finance
  - 4.8 Financial Text Mining
  - 4.9 Theoretical or Conceptual Studies
  - 4.10 Other Financial Applications
- **5 Current Snaphot of DL research for Financial Applications**
- **6 Discussion and Open Issues**
  - 6.1 Discussions on DL Models
  - 6.2 Discussions on Implementation Areas
  - 6.3 Open Issues and Future Work
  - 6.4 Responses to our Initial Research Questions
- **7 Conclusions**
- **8 Acknowledgement**

### TL;DR (≤120字)
本書屬於 ml for finance 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **金融時序資料是非平穩的** — 機器學習的 i.i.d. 假設在市場失效,這是所有金融 ML 失靈的本質原因
2. **樣本外績效下降是常態不是異常** — 模型週期性重訓、特徵漂移監測應視為系統常規模組,而非意外處理
3. **訊號強度 vs. 成本** — ML 模型發現的 alpha 往往小於 bid-ask 與手續費,backtest 必須內含實務成本

### 可用戰術/策略

- 使用 walk-forward validation + purged k-fold 防止時序洩漏
- ensemble 多個弱訊號而非單一強訊號,降低 overfitting 風險

### 盲點 / 反例 / 適用邊界

- ML 模型在結構性變化 (央行政策轉向、市場微結構改變) 下失效,必須有 regime detection 做護欄

### 與 Edward 既有知識的連結

- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
- 呼應零式原則 *information_asymmetry_action* — 有邊際資訊優勢才進場
