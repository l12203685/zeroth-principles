## The Morgan Kaufmann Series in Data Management Systems) Ian H. Witten, Eibe Frank, Mark A. Hall-Data Mining_ Practical Machine Learning Tools and Techniques, Third Edition — Morgan Kaufmann (2011)
**來源**: E:/書籍/The Morgan Kaufmann Series in Data Management Systems) Ian H. Witten, Eibe Frank, Mark A. Hall-Data Mining_ Practical Machine Learning Tools and Techniques, Third Edition-Morgan Kaufmann (2011).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Front cover**
- **Data Mining: Practical Machine Learning Tools and Techniques**
- **List of Figures**
- **List of Tables**
  - Updated and revised content
- **PART I: Introduction to Data Mining**
  - Chapter 1: What's It All About?
  - Chapter 2: Input: Concepts, Instances, and Attributes
  - Chapter 3: Output: Knowledge Representation
  - Chapter 4: Algorithms: The Basic Methods
  - Chapter 5: Credibility: Evaluating What's Been Learned
- **Part 2: Advanced Data Mining**
  - Chapter 6: Implementations: Real Machine Learning Schemes
  - Chapter 7: Data Transformations
  - Chapter 8: Ensemble Learning
  - Chapter 9: Moving on: Applications and Beyond
- **PART III: The Weka Data Mining Workbench**
  - Chapter 10: Introduction to Weka
  - Chapter 11: The Explorer
  - Chapter 12: The Knowledge Flow Interface
  - Chapter 13: The Experimenter
  - Chapter 14: The Command-Line Interface
  - Chapter 15: Embedded Machine Learning
  - Chapter 16: Writing New Learning Schemes
  - Chapter 17: Tutorial Exercises for the Weka Explorer

### TL;DR (≤120字)
本書屬於 ml for finance 範疇,作者 Morgan Kaufmann (2011) 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

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
