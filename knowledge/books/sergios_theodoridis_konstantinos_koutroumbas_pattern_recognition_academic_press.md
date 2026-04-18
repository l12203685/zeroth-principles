## Pattern Recognition (4th Ed) — Sergios Theodoridis, Konstantinos Koutroumbas
**來源**: E:/書籍/Sergios Theodoridis_Konstantinos Koutroumbas-Pattern recognition-Academic Press (2009).pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Ch 1** Introduction (pattern recognition overview)
- **Ch 2** Classifiers Based on Bayes Decision Theory
- **Ch 3** Linear Classifiers (perceptron, SVM linear)
- **Ch 4** Nonlinear Classifiers (MLP, RBF, kernel methods)
- **Ch 5** Feature Selection
- **Ch 6** Feature Generation I (orthogonal transforms: DFT, DCT, wavelets, KL transform)
- **Ch 7** Feature Generation II (PCA, ICA, NMF, Non-linear dim reduction / kernel PCA)
- **Ch 8** Template Matching (dynamic time warping, HMM)
- **Ch 9** Context-Dependent Classification (HMM Viterbi)
- **Ch 10** System Evaluation (ROC, confusion matrix, cross-validation)
- **Ch 11** Clustering Basics
- **Ch 12** Clustering Algorithms I (sequential)
- **Ch 13** Clustering Algorithms II (hierarchical)
- **Ch 14** Clustering Algorithms III (cost function, k-means, fuzzy c-means, spectral clustering)
- **Ch 15** Clustering Algorithms IV (density-based, DBSCAN, SOM, ART)
- **Ch 16** Cluster Validity (relative + external + internal indices)
- **Appendix A-D** (Probability basics, linear algebra, optimization, Hausdorff distance)

### TL;DR (≤120字)
工程學院派寫的 pattern recognition 綜合教材:強在分類器數學(Bayes、SVM、MLP、kernel)與 feature engineering (PCA、wavelets、ICA),是 1990-2010 代 ML 學科骨幹教材。2014 後由 deep learning 主導,但 feature/kernel/clustering 基本功仍有效;適合金融 quant 補 ML 底層知識。

### 核心本質 (3-5 條, 每條 50-120字)
1. **Bayes 最優決策 = 所有分類器的理論下限** — Ch2 明確:若知真分佈,Bayes rule (posterior max) 是最小錯誤率分類器。所有 ML 方法本質在「近似 Bayes rule」;理解此點才懂為何朴素 Bayes、SVM、MLP 都指向同一目標,差別在近似方式。
2. **Feature engineering > algorithm choice (in most 非深度學習場景)** — Ch5-7 的 feature selection + generation 主張:好的特徵讓簡單 linear classifier 夠用,壞的特徵讓 deep net 也難救。金融 ML 多屬此類 — stationarity / low signal-to-noise 使特徵工程比模型選擇更關鍵。
3. **SVM 的 kernel trick 是「把非線性藏進內積」的典範** — Ch3-4 詳解:用 kernel 把資料映射到高維 feature space,但只需計算 kernel K(x,y)=⟨ϕ(x),ϕ(y)⟩;計算量不隨維度爆炸。這是 kernel methods 之所以 tractable 的關鍵,也是 Gaussian process、kernel PCA 等的基礎。
4. **PCA/ICA 分別對應不同的「主成份」概念** — PCA 找 variance 最大方向(適合連續/相關訊號);ICA 找統計獨立的 source(適合 blind source separation,如 cocktail party problem)。金融因子分析若想找「獨立 alpha source」,ICA 比 PCA 更適合。
5. **Clustering 無 ground truth,評估是主觀判斷** — Ch16 cluster validity 列舉 Dunn、Davies-Bouldin、silhouette 等 indices,但不同 index 選出不同 "optimal K"。重要體認:clustering 結果品質必須結合 domain knowledge,純數學指標不夠。

### 可用戰術/策略
- **DBSCAN 作為市場 regime detection** — Ch15 DBSCAN 對任意形狀 cluster 有效且自動決定 K;以 (volatility, autocorrelation, volume) 三維 representation,DBSCAN 可識別 "trending" / "mean-reverting" / "crash" 三種 regime,驅動策略切換。
- **PCA 降維 for factor exposure 分析** — 對 N 個股票回報矩陣做 PCA,前幾個成份對應 market factor / sector factor;用於 "市場 neutral" 組合建構 — 去除前 K 主成份後的 residual 是純 idiosyncratic 部分。
- **SVM 分類策略方向** — 以歷史數據 (technical indicators 為 features, 未來 N 日報酬正負為 label) 訓練 SVM;Ch3-4 的 C parameter + kernel 選擇流程可 templated 為 B1 策略開發工具。
- **HMM (Ch8-9) 用於 regime-switching model** — 隱藏狀態 = market regime,觀察變量 = 報酬/波動;用 Viterbi 解碼當前最可能 regime,用 forward-backward 算 regime 轉移機率。這是 Hamilton (1989) regime-switching 模型的 ML 實作路徑。

### 盲點 / 反例 / 適用邊界
- **2009 版,完全不涵蓋 deep learning (CNN/RNN/transformer)** — 2012 後 DL 橫掃 CV/NLP;金融時序用 LSTM/transformer 架構需另讀 Goodfellow《Deep Learning》、Chollet《Deep Learning with Python》。
- **偏靜態 classification,時序資料處理有限** — HMM 有提但不深;現代金融時序 ML 需讀 López de Prado《Advances in Financial ML》(含 meta-labeling、triple-barrier、fractional differentiation)。
- **工程視角偏多,統計推斷層嚴謹度一般** — 給 MATLAB code 但缺 generalization bound、VC dimension、PAC learning 完整討論;配 Mohri《Foundations of Machine Learning》補。
- **金融領域範例稀少** — 主要以圖像/語音為範例;金融特殊挑戰(non-stationarity、low SNR、regime shift、label leakage) 需另補金融 ML 專書。

### 與 Edward 既有知識的連結
- 連結 Wasserman《All of Statistics》:兩書互補 — Wasserman 強統計推斷,Theodoridis 強工程實作;合讀可覆蓋金融 ML 研究的理論+實作兩側。
- 對應 `derivative_over_level`:Feature engineering (Ch5-7) 本質是「在 raw data 之上導出有訊號的變化量」,正是 derivative > level 的實踐。
- 連結 `meta_strategy_over_strategy`:Ch10 System Evaluation 的 cross-validation 與 confusion matrix 是 meta-strategy 層面的策略品質評估工具,不是 "策略之內" 的指標。
- 對 B1 自營交易系統的貢獻:若要加入 ML 選股/擇時模組,建議作為 engineer 培訓書 + API 參考;結合 sklearn/PyTorch 實作後,直接以 Ch3 SVM 或 Ch14 k-means 為 baseline。
