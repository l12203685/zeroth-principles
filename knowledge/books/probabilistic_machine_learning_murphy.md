## Probabilistic Machine Learning: An Introduction — Kevin P. Murphy (2022)
**來源**: MIT Press canonical edition  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- **Part I Foundations (1-7)**：intro、probability、statistics、decision theory、information theory
- **Part II Linear Models (8-11)**：linear/logistic regression、GLM、regularization、feature selection
- **Part III Deep Neural Networks (12-16)**：MLP、CNN、RNN、Transformers、graph neural networks
- **Part IV Nonparametric Models (17-19)**：kernels、Gaussian processes、Dirichlet processes
- **Part V Beyond Supervised (20-23)**：clustering、dimensionality reduction、recommender systems
- **Part VI Other (24)**：generative models (VAE/GAN/normalizing flows/diffusion)

### TL;DR (≤120字)
Murphy 2022 是 2020s 的 ML 教科書新王，統合頻率派 + Bayesian + Deep Learning 全景。對交易者的價值：不用再讀 Bishop+Goodfellow 兩本湊，一本覆蓋所有現代 ML。特別是第 15-16 章 Transformer + graph NN、第 24 章 diffusion，是 2020s 新技術的教科書級解說。缺點是 1000+ 頁太厚，適合當索引書不是從頭讀。

### 核心本質 (3-5 條)
1. **機率框架統合一切 ML（本質，第 1-4 章）** — 所有模型視為 p(y|x, θ) 的假設空間；MLE/MAP/Bayesian 是三種參數學習策略。Murphy 強調這統一視角讓學習演算法不再是黑盒。
2. **Transformers = attention + positional encoding + FFN（本質，第 15.5 節）** — Self-attention 讓任兩 token 直接互動（不像 RNN 順序傳遞）；O(n²) memory 是瓶頸，Flash Attention/Linformer 緩解。金融 TS 用 Informer/Autoformer。
3. **Diffusion model 是新 generative SOTA（本質，第 24 章）** — 從 noise 逐步 denoising 學 p(x)；比 GAN 穩定、比 VAE 樣本品質高。金融：合成極端情境用 diffusion 比 GAN 更 reliable。
4. **Graph NN 處理非 Euclidean 數據（本質，第 16 章）** — 股票關聯網路、公司子母公司、交易對手圖都是 graph；GCN/GAT 學節點表示，可作 cross-sectional alpha。
5. **PAC-Bayes 連接頻率與 Bayesian（本質，第 4.7 節）** — Generalization bound 用 KL(posterior || prior)；解釋為什麼 Bayesian 正則化有理論保證。

### 可用戰術/策略
- **Transformer 日內預測**：用 Informer 架構（稀疏 attention）處理 1-min bar 過去 200 根；輸出下 10 min return 分布。
- **GNN 產業關聯因子**：用股票相關矩陣建 graph，GAT 2 層學節點 embedding；embedding 做 cross-sectional 因子。
- **Diffusion 增強 tail event**：用 diffusion 學正常市場日分布；從訓練分布抽樣合成「擴充尾部」訓練集。
- **Gaussian process regression**：對小樣本（< 1000）參數校準（如 implied vol surface）用 GP 比 NN 穩定、自動給 uncertainty。
- **Conformal prediction**：用 quantile regression + 驗證集建預測區間，無分布假設；金融 downside risk 預測的 robust 方法。

### 盲點 / 反例 / 適用邊界
- **1000+ 頁**：不可能從頭讀；適合按章節查。
- **金融例子零**：全 vision/NLP/recommendation；金融特化需自己 porting。
- **Python 碼分散**：書不附碼，配 pmls-book.github.io 的 Jupyter notebook。
- **進階需第 2 本**：Murphy 另有 *Advanced Topics* (2023) 才覆蓋 RL、causal inference、inference-time compute；合二書 2000+ 頁。
- **Transformer 章節精簡**：15.5 節僅 30 頁，深入需讀 Vaswani 原論文 + Annotated Transformer。

### 與 Edward 既有知識的連結
- **對齊 ZP next-gen alpha 引擎**：Transformer + GNN 是 2024+ 標配；Murphy 提供教科書級入門，Edward 可直接 porting。
- **延伸 Bishop + Goodfellow**：Bishop 深、Goodfellow 舊、Murphy 新而廣；用 Murphy 作索引，深入時回 Bishop/Goodfellow。
- **衝突點**：Murphy 對 Bayesian vs Frequentist 兩派平衡（比 Bishop 更中性）；Edward 可依任務彈性選派。
- **可挖金礦**：第 15.5.5 的 Informer 稀疏 attention + 第 16.2 的 GAT 直接可跑金融；書有作者官方 code。
- **對接 Hernán-Robins Causal Inference**：Murphy 第 4-5 章略提 causality；深入需讀 Hernán 或 Pearl。
