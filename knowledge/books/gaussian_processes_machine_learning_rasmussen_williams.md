## Gaussian Processes for Machine Learning — Carl Edward Rasmussen & Christopher K.I. Williams
**來源**: E:/書籍/Gaussian Processes for Machine Learning.pdf  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- 第 1 章 Introduction（weight-space view、function-space view）
- 第 2 章 Regression（predictive distribution、smoothing、noise-free）
- 第 3 章 Classification（Laplace approx、EP、MCMC）
- 第 4 章 Covariance Functions（squared exp、Matern、periodic、neural network kernel）
- 第 5 章 Model Selection & Adaptation of Hyperparameters（marginal likelihood、CV、Bayesian CV）
- 第 6 章 Relationships Between GPs and Other Models（spline、SVM、neural network、RKHS）
- 第 7 章 Theoretical Perspectives（asymptotic analysis、consistency、PAC-Bayes）
- 第 8 章 Approximation Methods for Large Datasets（subset of data、projected process、FITC）
- 第 9 章 Further Issues and Conclusions（learning curves、applications）
- 附錄 Mathematical background、Kernel details

### TL;DR (≤120字)
Rasmussen-Williams 是 Gaussian Process (GP) 的標準教材，MIT 出版 + 作者提供免費 PDF。GP 本質：對任何有限點集，output 是 multivariate Gaussian，以 kernel（covariance function）描述平滑性假設。對金融的價值：小樣本（< 1000）+ 需要 uncertainty（implied volatility surface、rare event probability）時，GP 勝過 NN。缺點 O(N³) 運算，N > 10000 需 approximation（第 8 章）。

### 核心本質 (3-5 條)
1. **GP = 函數空間上的 prior（本質，第 1-2 章）** — f(x) 服從 GP 代表任何有限點集 (f(x_1),..., f(x_n)) ~ MVN；mean function + covariance function (kernel) 完整定義 GP。
2. **預測 = 條件 MVN 的 analytic formula（本質，第 2.2 節）** — 對新點 x*，predictive mean + variance 皆有 closed form；variance 反映「離訓練點有多遠」——外推時 variance 自動增大。
3. **Kernel 編碼問題結構（本質，第 4 章）** — Squared exp → smooth；Matern-5/2 → 中等平滑；Periodic → 週期；Linear → 線性趨勢。金融數據常組合 kernel（e.g., trend + seasonality + noise）。
4. **Marginal likelihood 自動 model selection（本質，第 5 章）** — log p(y|X) 對超參數（length-scale, signal variance, noise）對數可微；gradient ascent 找最優超參。自動平衡 fit vs complexity。
5. **O(N³) 計算限制（本質，第 8 章）** — 精確 GP 需 Cholesky (KN×N)⁻¹ 耗 O(N³)；N > 10000 需 sparse GP（FITC、VFE、stochastic variational GP）。

### 可用戰術/策略
- **GP for IV surface interpolation**：implied volatility as f(strike, maturity)；用 Matern-5/2 kernel + marginal likelihood 優化 length-scales；預測時給出 mean + std 雙輸出。
- **GP for Bayesian optimization of hyperparams**：策略參數調優用 GP-BO（Snoek 2012）；比 grid search 少 10-100 倍樣本。
- **Temporal GP for noisy vol**：realized vol 為 GP 觀察 + Gaussian noise；kernel 用 periodic × squared exp 捕日/週期。
- **GP state-space for filter**：連續時間 state-space 用 Matern kernel → equivalent to SDE；Kalman-like recursive inference。
- **Sparse GP for large data**：inducing points M=100-500 代替全部 N 樣本；FITC 或 VFE 近似，O(NM²) 而非 O(N³)。

### 盲點 / 反例 / 適用邊界
- **假設 Gaussian likelihood**：分類或 Poisson count 需 Laplace approx 或 EP；精度降低。
- **不能 handle 明確 non-stationary**：固定 kernel 意味平穩；金融 regime 需 deep GP 或 locally adaptive kernel。
- **Kernel 選擇仍需 expertise**：錯 kernel → 錯結果；需領域知識或 kernel search。
- **O(N³) 嚴重限制**：實務金融常百萬以上樣本；sparse 方法損失精度。
- **ML 未統合**：2006 出版，GP + deep（NPs, DKL）皆 2015+ 發展；深度 GP 需 Damianou 論文。

### 與 Edward 既有知識的連結
- **對齊 ZP option pricing surface**：GP 對 IV surface 優於 polynomial fit；給 pricer uncertainty 輸入。
- **延伸 Bishop PRML**：Bishop 第 6 章也談 GP，但較簡；Rasmussen 深度 + 完整覆蓋。
- **衝突點**：GP 小樣本強、deep 大樣本強；金融 regime 變時 GP 更快適應；Edward 在 N < 10000 場景優先 GP。
- **可挖金礦**：第 5 章 marginal likelihood 自動調 kernel 可替代 Edward 目前手動調策略參數的 grid search。
- **對接 Rasmussen-Williams（本書）+ Bishop PRML + Murphy PML**：GP 是 Bayesian 非參方法家族；讀完 GP 書再看 Bishop/Murphy 更懂結構。
