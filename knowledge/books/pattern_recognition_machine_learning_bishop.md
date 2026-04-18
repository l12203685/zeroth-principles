## Pattern Recognition and Machine Learning (PRML) — Christopher M. Bishop
**來源**: E:/書籍/[Christopher_M._Bishop]_Pattern_Recognition_and_Ma(BookFi.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- 第 1 章 Introduction（polynomial curve fitting、probability、model selection、decision theory）
- 第 2 章 Probability Distributions（binomial、Gaussian、exponential family、nonparametric）
- 第 3 章 Linear Models for Regression（Bayesian linear regression、evidence approximation）
- 第 4 章 Linear Models for Classification（discriminant、probabilistic generative、Bayesian logistic）
- 第 5 章 Neural Networks（feedforward、backprop、Bayesian NN、mixture density）
- 第 6 章 Kernel Methods（dual representations、Gaussian processes、ARD）
- 第 7 章 Sparse Kernel Machines（SVM、RVM）
- 第 8 章 Graphical Models（Bayesian networks、MRF、message passing）
- 第 9 章 Mixture Models & EM（GMM、K-means、EM convergence）
- 第 10 章 Approximate Inference（variational inference、EP、local VB）
- 第 11 章 Sampling Methods（Gibbs、Metropolis-Hastings、HMC、slice sampling）
- 第 12 章 Continuous Latent Variables（PCA、probabilistic PCA、factor analysis、ICA）
- 第 13 章 Sequential Data（HMM、linear dynamical systems、Kalman filter）
- 第 14 章 Combining Models（Bayesian averaging、mixtures of experts、boosting）

### TL;DR (≤120字)
Bishop PRML 是 Bayesian ML 的聖經。用機率圖模型視角統一 ML：每個演算法（regression、SVM、NN、HMM）都推到最底的 likelihood + prior + posterior 形式。對交易者最關鍵的是第 8、10、11、13 章——Bayesian networks 對因果建模、VI/MCMC 做參數後驗、Kalman filter 做動態系統跟蹤（像 RSI 的 state-space 版）。比 ESL 更數學、更 Bayesian。

### 核心本質 (3-5 條)
1. **一切模型 = 機率圖模型（本質，第 8 章）** — 任何 ML 模型（Regression/SVM/NN/HMM）都能畫成有向/無向圖。變數節點 + 機率邊 → 聯合分布 → 推論 = marginal/MAP 計算。這視角消除「演算法 vs 模型」的混淆。
2. **Bayesian = 用先驗正則化 + 得到不確定性（本質，第 3、5 章）** — Bayesian linear regression 給出 predictive distribution p(y|x, D) 含方差；頻率派只給點估計。交易下單應該看「預測 ± 不確定性」，不是單一 expected return。
3. **EM = 有 latent 變數時的 MLE 替代（本質，第 9 章）** — E-step 計 responsibility、M-step 更新參數；保證似然單調上升但可能卡局部極值。GMM、HMM、factor analysis 全靠 EM。
4. **變分推論 vs MCMC 取捨（本質，第 10-11 章）** — VI 快但偏 mode-seeking（低估 variance）；MCMC 慢但漸近正確。金融實時系統（秒級）用 VI，離線研究（日內/盤後）用 MCMC/HMC。
5. **Sequential data 需 state-space model（本質，第 13 章）** — HMM（離散 latent）和 Kalman filter（連續 Gaussian）是時變系統的標配；regime-switching 交易模型就是 HMM 應用。

### 可用戰術/策略
- **Bayesian linear alpha**：對每個因子用 Bayesian ridge，evidence approximation 自動選 λ；輸出 predictive variance 作為 position sizing 訊號。
- **Kalman filter pairs trade**：spread = β_t × stock_A - stock_B，β_t 用 Kalman 動態估計（比 rolling OLS 對 structural break 更快反應）。
- **HMM regime filter**：用 HMM 2-state 擬合日收益（high-vol / low-vol）；交易策略僅在 low-vol state 啟動。
- **GMM 聚類市場狀態**：用 GMM k=3-5 對 (return, volatility, volume) 聚類，輸出當前市場狀態 posterior。
- **VI 快速後驗**：對高維因子模型用 mean-field VI（比 MCMC 快 100 倍），用於盤中實時更新。

### 盲點 / 反例 / 適用邊界
- **2006 出版，無 deep learning**：第 5 章 NN 以 2 層為主；現代 Transformer/CNN 完全缺席。
- **數學密度高**：幾乎每章都要熟悉變分微積分、測度論基礎；初學者無法啃，需配 Andrew Ng 入門。
- **計算效率未重點**：算法正確性優先，scalability 很少談；大數據需配 Murphy 2022 版。
- **金融案例零**：全書生物/影像範例；交易者需自己把「pixel」類比成「tick」。
- **Bayesian 教條**：對頻率派/PAC-Bayes 只略提；想要理論全景需配 Shalev-Shwartz 或 ESL。

### 與 Edward 既有知識的連結
- **對齊 ZP regime model**：第 13 章 HMM 直接實作成 `ZP/quant/regime/hmm_2state.py`，是宏觀策略的前置過濾器。
- **延伸 Bayesian Methods in Finance (Rachev)**：Rachev 偏應用、Bishop 偏理論；讀完 Bishop 再回 Rachev 能理解 MCMC 公式推導。
- **衝突點**：Bishop 全 Bayesian、ESL 頻率派優先；Edward 應根據任務選——研究/參數學習用 Bayesian、實時模型用頻率 CV。
- **可挖金礦**：第 10.1 VI 的 mean-field approximation 可直接套用 Financial ML 的 SDF 估計，比 MCMC 快數百倍。
- **對接 Goodfellow Deep Learning**：Goodfellow 第 3 章 probability 和 Bishop 第 2 章重疊，Bishop 更嚴謹；兩書合讀補完整 ML 數學基礎。
