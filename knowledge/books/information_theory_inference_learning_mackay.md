## Information Theory, Inference, and Learning Algorithms — David J.C. MacKay
**來源**: E:/書籍/MacKay D.J.C.-Information theory, inference and learning algorithms-CUP (2005).pdf  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- **Part I Data Compression (1-6)**：entropy、source coding theorem、symbol codes、stream codes、arithmetic coding
- **Part II Noisy-Channel Coding (7-13)**：dependent random variables、communication over noisy channels、channel capacity、channel coding theorem、linear codes、Hamming codes
- **Part III Further Topics in Information Theory (14-19)**：very good linear codes exist、hash codes、binary symmetric channel、Gaussian channel、cluster expansion
- **Part IV Probabilities and Inference (20-30)**：exact inference、model comparison、Monte Carlo methods、Gibbs sampling、slice sampling、Hamiltonian Monte Carlo、ising model、exact marginalization、importance sampling
- **Part V Neural Networks (31-39)**：single/multilayer perceptrons、Hopfield nets、Boltzmann machines、supervised learning in MLP、Bayesian learning、Gaussian processes、SVM 雛形
- **Part VI Sparse Graph Codes (40-48)**：low-density parity check codes、convolutional codes、turbo codes、belief propagation

### TL;DR (≤120字)
MacKay 這本書是 *Information Theory + Bayesian ML* 雙聖經合體，630 頁 + 免費線上（書作者堅持免費）。寫作風格獨特：每章有圖解、例題、練習 + 哲學討論。對交易者的價值：**Shannon entropy 量化交易訊號的 information content**、第 IV 部分 MCMC 引導 Bayesian 後驗、第 V 部分 Gaussian process 對小樣本參數校準完美。跨 CS-Physics-Stats 三界少見好書。

### 核心本質 (3-5 條)
1. **Entropy = 資訊量 = 編碼下界（本質，第 2 章）** — H(X) = -Σp(x)log p(x)；Shannon 定理說任何無失真編碼平均長度 ≥ H。金融：alpha signal 的 entropy 量化其 predictive information。
2. **Mutual information I(X;Y) = 相關性的資訊版（本質，第 8 章）** — I(X;Y) = H(X) + H(Y) - H(X,Y)；非線性相關（相關系數 = 0 但 I > 0）。對 copula/tail dependence 檢測。
3. **Bayesian inference = 機率更新演算法（本質，第 20 章）** — p(θ|D) = p(D|θ)p(θ)/p(D)；evidence p(D) 是 model comparison 核心（Bayes factor）。
4. **MCMC 為無窮維積分的 Monte Carlo 工具（本質，第 29-30 章）** — Metropolis、Gibbs、Hamiltonian MC；HMC 利用梯度資訊在高維更高效（比 vanilla Metropolis 快 10-100x）。
5. **Neural Network = 非線性 basis function expansion（本質，第 38 章）** — MacKay 的 Bayesian 視角把 NN 視為 regression over function space；Bayesian NN 給 predictive uncertainty（頻率派 NN 只給 point estimate）。

### 可用戰術/策略
- **Mutual information feature selection**：用 MI(X_i, Y) 代替 Pearson correlation 選特徵；適用非線性依賴（e.g., volatility → absolute return 的關係）。
- **Bayesian model selection via evidence**：比較 2 competing 策略的 log evidence log p(D|M)；差 > 5 視為顯著勝出。
- **HMC for hierarchical model**：用 Stan/PyMC 的 NUTS（無調步 HMC）做高維 posterior sampling；比 Gibbs 快。
- **Gaussian process for IV surface**：GP 對小樣本擬合 implied volatility surface；自動給出 posterior uncertainty 在 maturity × strike 空間。
- **Entropy-based regime detector**：滾動窗口計算 return 分布 entropy；entropy 突變 = regime change alarm。

### 盲點 / 反例 / 適用邊界
- **寫作獨特 = 非標準**：書有大量哲學、幽默、插圖；喜歡就愛，不合胃口讀不下。
- **時序淺**：本書 iid 假設為主；時序需 Hamilton/Tsay 補。
- **2003 出版**：Deep Learning 爆發前；現代 CNN/Transformer 不在。
- **Channel coding 章對金融者無用**：第 II-III 部分純通訊理論；金融可跳。
- **Stan/TensorFlow 碼無**：只虛擬碼；實作自行 porting。

### 與 Edward 既有知識的連結
- **對齊 ZP information-theoretic alpha**：用 MI 代替 Pearson；用 entropy 量化 alpha signal strength；用 HMC 做參數後驗。
- **延伸 Bishop PRML**：Bishop 更結構化 Bayesian ML；MacKay 更 cross-domain（info theory + Bayesian + NN）。讀完 Bishop 再 MacKay 有新洞見。
- **衝突點**：MacKay 偏 Bayesian + info theory；Wasserman 偏 frequentist + nonparametric；兩書視角互補。
- **可挖金礦**：第 IV 部分 MCMC 章有大量可視化，幫 Edward 理解為何 HMC 在高維優於 Gibbs；實作到 ZP 參數校準。
- **對接 Cover-Thomas Information Theory**：Cover-Thomas 是純 info theory 聖經；MacKay 是 cross-domain。兩書各取所需。
