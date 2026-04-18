## Machine Learning with R — Brett Lantz (Packt Publishing, 2013)
**來源**: E:/書籍/Brett Lantz-Machine Learning with R-Packt Publishing (2013).pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Chapter 1 Introducing Machine Learning (origins, uses/abuses, how machines learn, steps, choosing algorithm, R for ML)
- Chapter 2 Managing and Understanding Data (R data structures, vectors, factors, managing, exploring)
- Chapter 3 Lazy Learning - Classification using Nearest Neighbors (breast cancer kNN example)
- Chapter 4 Probabilistic Learning - Naive Bayes (mobile phone spam filtering example)
- Chapter 5 Decision Trees and Rules (C5.0 decision trees for risky loans, rule learners for poisonous mushrooms)
- Chapter 6 Forecasting Numeric Data - Regression Methods (linear regression for medical expenses, regression trees for wine quality)
- Chapter 7 Black Box Methods - Neural Networks and SVM (ANN for concrete strength, SVM for OCR)
- Chapter 8 Finding Patterns - Market Basket Analysis using Association Rules (grocery purchases)
- Chapter 9 Finding Groups of Data - Clustering with k-means
- Chapter 10 Evaluating Model Performance (classification metrics, cross-validation, hold-out)
- Chapter 11 Improving Model Performance (hyperparameter tuning, bagging/boosting meta-learning)
- Chapter 12 Specialized Machine Learning Topics (special data, R performance)

### TL;DR (≤120字)
Lantz 的 ML 入門教材最大價值：每個演算法搭配一個真實數據集（breast cancer、spam、mushrooms、wine、concrete、groceries），從 load data 到 evaluation 的完整 R 流程 end-to-end。讀者跑完 10 個範例就能理解 ML workflow，不需學術嚴謹的數學推導。適合金融 quant 用 ML 的第一本。

### 核心本質 (3-5 條)
1. **ML Workflow 標準化**（本質，Ch1） — Lantz 把 ML 流程拆成 6 步：資料收集 → 探索清洗 → 模型訓練 → 評估 → 改進 → 部署。這個框架在任何 ML 工具（R, Python, Scala）都通用；跳過任一步都是災難（尤其是 Ch10 evaluation，新手常忽略）。
2. **Algorithm Selection by Problem Type**（本質，Ch1 末） — 分類選 kNN/Naive Bayes/Tree/NN/SVM；回歸選 linear/tree/NN；pattern 選 association rules；grouping 選 k-means。Lantz 用 decision flowchart 幫讀者快速選擇，避免「有錘子看什麼都是釘子」。
3. **Evaluation ≠ Training Accuracy**（本質，Ch10） — 訓練集準確率高不代表實戰好；必須用 holdout / k-fold cross-validation 評估 out-of-sample。混淆矩陣、ROC curve、kappa 統計等都是必須技能。此章節在金融應用尤其重要（過擬合致命）。
4. **Meta-Learning 是效能 +5-20% 的銀彈**（本質，Ch11） — 單一模型 tuning 不夠；bagging（減 variance）、boosting（減 bias）、stacking（不同模型組合）幾乎必定 outperform 單一模型。Random Forest 就是 decision tree + bagging + random feature selection 的成功案例。
5. **R Data Structures 的 factor 陷阱**（本質，Ch2） — R 的 factor type（類別變數）與 character string 不同；新手常誤用導致 silent bug。Lantz 在第 2 章清晰示範 factor 的 level、ordering、ordered factor 區別，這是所有 R user 必過的陷阱。

### 可用戰術/策略
- **Confusion Matrix + Cost-Sensitive**：金融違約預測中，false negative（該違約沒抓到）成本遠高於 false positive；用 `caret::confusionMatrix` 設定 cost 調整 threshold，優化商業價值而非 accuracy。
- **ROC + AUC 為主要 metric**：對 imbalanced dataset（95% 正常、5% 違約），accuracy meaningless；用 AUC 評估，> 0.75 是可接受，> 0.85 是優秀。
- **Feature Engineering before Algorithm**：Lantz 示範：先用 domain knowledge 做 log-transform、ratio、lag features；通常比換演算法提升大得多。
- **Random Forest as Default Baseline**：對大多數 tabular data 問題，Random Forest (500 trees) 是最佳 single-model baseline；若做不贏 RF，複雜模型多半也做不贏。
- **k-Fold Cross Validation (k=10)**：用 `caret::train(method="cv", number=10)` 做 robust evaluation；避免 single train-test split 的高 variance 結論。

### 盲點 / 反例 / 適用邊界
- **2013 年出版，已過時** — 當年 deep learning 才剛興起，書中完全沒有 Keras/TensorFlow/PyTorch；當前 ML 場景（CNN、RNN、Transformer、LLM）需另尋教材。
- **R vs Python 生態差距** — 2013 R 優於 Python；2026 Python 已成主流，R 剩統計科學小圈；金融 quant 實務用 Python 更吃香。
- **時序資料處理薄弱** — 書中例子多為 iid 資料（cancer、groceries），金融時序有 autocorrelation、regime change 等特殊挑戰，Lantz 幾乎沒提；需配合 Tsay 或時序專書。
- **無 hyperparameter tuning 最佳實務** — 第 11 章提了 grid search，但未涵蓋 Bayesian optimization（Hyperopt, Optuna）、Population-based training 等當代技術。
- **Imbalanced Class 處理僅淺嘗輒止** — SMOTE、weighted loss、focal loss 等當代處理方法未討論；金融詐欺偵測會遇到此痛點。

### 與 Edward 既有知識的連結
- **ZP ML 入門教材**：比 Tsay 的計量經濟學更貼近 data scientist 工作流程；適合作為 `ZP/ml_for_finance/fundamentals/` 的 reference。
- **延伸 Financial ML**：Kelly-Xiu 的理論論述搭配 Lantz 的實作範例，一理論一實務；Edward 可先讀 Lantz 熟悉 workflow，再讀 Kelly-Xiu 理解金融專屬考量。
- **對應 Bayesian Methods**：Lantz 的 Naive Bayes 章節（Ch4）是 Rachev Bayesian book 的簡化版入門；兩本搭配讀完整。
- **衝突 Tsay 的 interpretability**：Lantz 的 black-box 風格與 Tsay 的 interpretable 派相反；Edward 應明確區分用途——監管報表用 Tsay，alpha 生成用 Lantz/Kelly-Xiu。
- **可挖金礦**：書中 R 範例全部 port 到 Python + scikit-learn + pandas，作為 `ZP/ml_for_finance/exercises/` 的學習模組；每週跑 1-2 個 example 維持 ML 肌肉。
- **Poker 應用**：Chapter 8 Market Basket Analysis（association rules）可用於分析對手 betting pattern 的 co-occurrence；Chapter 4 Naive Bayes 可做 opponent 類型分類。
