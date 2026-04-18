## Shalev-Shwartz S., Ben-David S.-Understanding Machine Learning_ From Theory to Algorithms — CUP (2014)
**來源**: E:/書籍/Shalev-Shwartz S., Ben-David S.-Understanding Machine Learning_ From Theory to Algorithms-CUP (2014).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Halftitle**
- **Title**
- **1 Introduction**
  - 1.1 What Is Learning?
  - 1.2 When Do We Need Machine Learning?
  - 1.3 Types of Learning
  - 1.4 Relations to Other Fields
  - 1.5 How to Read This Book
  - 1.6 Notation
- **Part 1 Foundations**
  - 2 A Gentle Start
  - 3 A Formal Learning Model
  - 4 Learning via Uniform Convergence
  - 5 The Bias-Complexity Tradeoff
  - 6 The VC-Dimension
  - 7 Nonuniform Learnability
  - 8 The Runtime of Learning
- **Part 2 From Theory to Algorithms**
  - 9 Linear Predictors
  - 10 Boosting
  - 11 Model Selection and Validation
  - 12 Convex Learning Problems
  - 13 Regularization and Stability
  - 14 Stochastic Gradient Descent
  - 15 Support Vector Machines
  - 16 Kernel Methods
  - 17 Multiclass, Ranking, and Complex Prediction Problems
  - 18 Decision Trees
  - 19 Nearest Neighbor
  - 20 Neural Networks
- **Part 3 Additional Learning Models**
  - 21 Online Learning
  - 22 Clustering
  - 23 Dimensionality Reduction
  - 24 Generative Models
  - 25 Feature Selection and Generation
- **Part 4 Advanced Theory**
  - 26 Rademacher Complexities
  - 27 Covering Numbers
  - 28 Proof of the Fundamental Theorem of Learning Theory
  - 29 Multiclass Learnability
  - 30 Compression Bounds
  - 31 PAC-Bayes
- **A Technical Lemmas**
- **B Measure Concentration**
  - B.1 Markov's Inequality
  - B.2 Chebyshev's Inequality
  - B.3 Chernoff's Bounds
  - B.4 Hoeffding's Inequality
  - B.5 Bennet's and Bernstein's Inequalities
  - B.6 Slud's Inequality
  - B.7 Concentration of χ[sup(2)] Variables
- **C Linear Algebra**
  - C.1 Basic Definitions
  - C.2 Eigenvalues and Eigenvectors
  - C.3 Positive definite matrices
  - C.4 Singular Value Decomposition (SVD)

### TL;DR (≤120字)
本書屬於 ml for finance 範疇,作者 CUP (2014) 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

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
