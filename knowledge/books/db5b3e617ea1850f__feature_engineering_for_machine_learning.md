## Feature_Engineering_for_Machine_Learning — 未標示
**來源**: E:/書籍/Feature_Engineering_for_Machine_Learning.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Introduction**
  - Conventions Used in This Book
  - Using Code Examples
  - O'Reilly Safari
  - How to Contact Us
- **Chapter 1. The Machine Learning Pipeline**
  - Data
  - Tasks
  - Models
  - Features
  - Model Evaluation
- **Chapter 2. Fancy Tricks with Simple Numbers**
  - Scalars, Vectors, and Spaces
  - Dealing with Counts
  - Log Transformation
  - Feature Scaling or Normalization
  - Interaction Features
  - Feature Selection
  - Summary
- **Chapter 3. Text Data: Flattening, Filtering, and Chunking**
  - Bag-of-X: Turning Natural Text into Flat Vectors
  - Filtering for Cleaner Features
  - Atoms of Meaning: From Words to n-Grams to Phrases
  - Summary
- **Chapter 4. The Effects of Feature Scaling: From Bag-of-Words to Tf-Idf**
  - Tf-Idf : A Simple Twist on Bag-of-Words
  - Putting It to the Test
  - Deep Dive: What Is Happening?
  - Summary
- **Chapter 5. Categorical Variables: Counting Eggs in the Age of Robotic Chickens**
  - Encoding Categorical Variables
  - Dealing with Large Categorical Variables
  - Summary
- **Chapter 6. Dimensionality Reduction: Squashing the Data Pancake with PCA**
  - Intuition
  - Derivation
  - PCA in Action
  - Whitening and ZCA
  - Considerations and Limitations of PCA
  - Use Cases
  - Summary
- **Chapter 7. Nonlinear Featurization via K-Means Model Stacking**
  - k-Means Clustering
  - Clustering as Surface Tiling
  - k-Means Featurization for Classification
  - Pros, Cons, and Gotchas
  - Summary
- **Chapter 8. Automating the Featurizer: Image Feature Extraction and Deep Learning**
  - The Simplest Image Features (and Why They Don't Work)
  - Manual Feature Extraction: SIFT and HOG
  - Learning Image Features with Deep Neural Networks
  - Summary
- **Chapter 9. Back to the Feature: Building an Academic Paper Recommender**
  - Item-Based Collaborative Filtering
  - First Pass: Data Import, Cleaning, and Feature Parsing
  - Second Pass: More Engineering and a Smarter Model
  - Third Pass: More Features = More Information
  - Summary
- **Appendix A. Linear Modeling and Linear Algebra Basics**
  - Overview of Linear Classification
  - The Anatomy of a Matrix
  - Solving a Linear System

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
