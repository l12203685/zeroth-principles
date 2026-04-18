## Deep Learning — Goodfellow, Bengio & Courville (MIT Press 2016)
**來源**: Online canonical textbook (deeplearningbook.org)  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- **Part I Applied Math & ML Basics (1-5)**：Linear algebra、Probability、Numerical computation、ML basics（容量、正則化、MLE）、
- **Part II Modern Practical Networks (6-12)**：
  - 第 6 章 Deep Feedforward Networks（XOR、activation、universal approximator）
  - 第 7 章 Regularization（L2、dropout、early stopping、data augmentation、parameter sharing）
  - 第 8 章 Optimization（SGD、momentum、Adam、batch norm、initialization）
  - 第 9 章 CNN（convolution、pooling、equivariance）
  - 第 10 章 RNN/LSTM/GRU（BPTT、vanishing gradient、attention 雛形）
  - 第 11 章 Practical Methodology（baseline、debugging、hyperparameter）
  - 第 12 章 Applications（vision、speech、NLP、structured prediction）
- **Part III Deep Learning Research (13-20)**：
  - 第 13 章 Linear Factor Models（PCA、factor analysis、ICA 從 DL 視角）
  - 第 14 章 Autoencoders（denoising、sparse、contractive）
  - 第 15 章 Representation Learning（transfer、domain adaptation）
  - 第 16-17 章 Structured Probabilistic Models、Monte Carlo Methods
  - 第 18 章 Partition Function（contrastive divergence、NCE）
  - 第 19 章 Approximate Inference
  - 第 20 章 Deep Generative Models（RBM、DBN、DBM、VAE、GAN 雛形）

### TL;DR (≤120字)
Goodfellow-Bengio-Courville 是 2016 年最後一本「pre-Transformer」的 DL 教科書聖經，涵蓋從線性代數到 GAN 的完整數學基礎。對交易者的價值不在賭 AlphaGo/LLM，而在 Part I-II 的機率/最佳化/正則化基本功——LSTM 跑 TS、dropout 防過擬合、batch norm、Adam 這些在任何金融 ML 專案都會用。第 7 章 regularization 是金融 ML 最容易出錯處。

### 核心本質 (3-5 條)
1. **DL = 可學的特徵表示（本質，第 1、15 章）** — 傳統 ML 需人工特徵，DL 讓每層自動學更抽象表示。金融 DL 的價值是「從 tick-level raw data 學出因子」，取代人寫 150 個技術指標。
2. **正則化是 DL 生存關鍵（本質，第 7 章）** — L2、dropout、early stopping、data augmentation、label smoothing、weight tying；金融數據 SNR 極低（噪訊 > 95%），正則強度要比視覺大 10-100 倍。
3. **最佳化 = SGD + momentum + adaptive LR（本質，第 8 章）** — Adam ≈ Adagrad + RMSProp + momentum；batch norm 穩定深度網路。但金融數據非平穩，batch norm 會洩漏未來（常用 layer norm 替代）。
4. **RNN/LSTM 處理序列的核心（本質，第 10 章）** — 普通 RNN 有 vanishing gradient；LSTM/GRU 用 gate 解決。但 2017 後 Transformer + attention 全面取代，本書出版後才爆發——需搭配 Vaswani 2017「Attention is All You Need」補讀。
5. **Generative 模型抓分布而非僅 mapping（本質，第 20 章）** — VAE/GAN 學 p(x)，可以做 anomaly detection（學不像的是異常）、synthetic data（擴充 fat-tail 稀少事件）。對金融風控直接可用。

### 可用戰術/策略
- **LSTM 價量預測**：用 5 層 LSTM + 64 hidden + dropout 0.5，輸入 20 日 OHLCV + 技術指標 → 預測下日收益 z-score。
- **TCN 取代 LSTM**：Temporal ConvNet 用 dilated causal convolution，訓練快 5-10 倍且能處理更長歷史（論文 Bai et al. 2018）。
- **Transformer for prices**：借 BERT 架構，輸入最近 500 個 bar 的 embedding，輸出下一個 bar 分布；注意 positional encoding 用時間戳而非 index。
- **Autoencoder 因子降維**：300 個因子 → encoder → 30 維隱特徵 → decoder 重建；用隱特徵訓 alpha 模型，減過擬合。
- **VAE 異常偵測**：訓 VAE 於正常市場期，高 reconstruction error 時間段標為 regime change 警報（提前平倉）。

### 盲點 / 反例 / 適用邊界
- **2016 出版，Transformer 前時代**：沒有 Attention、BERT、GPT；現代 NLP/TS 架構需補 Vaswani、Dosovitskiy、Rae。
- **金融案例零**：範例全 vision/speech，特徵處理/label 設計與金融差異極大。
- **SNR 假設樂觀**：DL 假設 SNR 高（vision 約 99.9% signal）；金融 SNR ~1-5%，DL 常比線性模型差。
- **數學密度高**：Part I 5 章純數學，非 ML 背景很難啃；建議配 3Blue1Brown 影片。
- **未來向度**：第 20 章 GAN 當時才誕生，細節不完整；StyleGAN/Diffusion 都 2018+。

### 與 Edward 既有知識的連結
- **對齊 ZP deep alpha 專案**：LSTM/TCN/Transformer 三種架構可並行跑，ensemble；第 7 章 regularization 是金融 DL 不爆的關鍵。
- **延伸 Lantz Machine Learning with R**：Lantz 停在隨機森林、神經網路淺層；Goodfellow 補深層架構。
- **衝突點**：Goodfellow DL 假設大數據（ImageNet 百萬級），金融樣本少（日線 ~5000），需特別警惕過擬合；混用 Lopez de Prado 的 meta-labeling 減樣本浪費。
- **可挖金礦**：第 8.7 batch norm 的 internal covariate shift 在金融會造成 lookahead（全域統計量用到未來）；實作要用「causal batch norm」（僅用過去）。
- **對接 Murphy Probabilistic ML**：Murphy 2022 覆蓋 Transformer/diffusion，和 Goodfellow 2016 形成前後期教科書組合。
