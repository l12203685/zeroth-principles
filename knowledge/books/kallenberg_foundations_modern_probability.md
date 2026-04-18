## Foundations of Modern Probability, 2nd Edition — Olav Kallenberg
**來源**: E:/課程/[6] 機率論/Foundations of Modern Probability, 2ed, 2002, Olav Kallenberg.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Measure Theory—Basic Notions
- Ch2 Measure Theory—Key Results
- Ch3 Processes, Distributions, and Independence
- Ch4 Random Sequences, Series, and Averages
- Ch5 Characteristic Functions and Classical Limit Theorems
- Ch6 Conditioning and Disintegration
- Ch7 Martingales and Optional Times
- Ch8 Markov Processes and Discrete-Time Chains
- Ch9 Random Walks and Renewal Theory
- Ch10 Stationary Processes and Ergodic Theory
- Ch11 Special Notions of Symmetry and Invariance
- Ch12 Poisson and Pure Jump-Type Markov Processes
- Ch13 Gaussian Processes and Brownian Motion
- Ch14 Skorohod Embedding and Invariance Principles
- Ch15 Independent Increments and Infinite Divisibility
- Ch16 Convergence of Random Processes, Measures, and Sets
- Ch17 Stochastic Integrals and Quadratic Variation
- Ch18 Continuous Martingales and Brownian Motion
- Ch19 Feller Processes and Semigroups
- Ch20 Ergodic Properties of Markov Processes
- Ch21 Stochastic Differential Equations and Martingale Problems
- Ch22 Local Time, Excursions, and Additive Functionals
- Ch23 One-Dimensional SDEs and Diffusions
- Ch24 Connections with PDEs and Potential Theory
- Ch25 Predictability, Compensation, and Excessive Functions
- Ch26 Semimartingales and General Stochastic Integration

### TL;DR (≤120字)
Kallenberg 是當代機率論聖經 (650+ 頁)——將現代機率論從測度基礎到 semi-martingale 完全覆蓋，以極度壓縮的命題-證明格式呈現。被視為博士 qualifying 最難等級。對金融：Ch17-26 幾乎所有 quant finance 隨機基礎都能在此找到嚴格定義與證明；是 Protter、Karatzas-Shreve、Revuz-Yor 的百科式參考。

### 核心本質 (3-5 條)
1. **Disintegration Theorem 是條件測度的終極工具**（Ch6） — 對 joint distribution P(X,Y)，存在 regular conditional distribution P(dy|X=x) 使 P(X∈A, Y∈B) = ∫_A P(Y∈B|X=x) P_X(dx)。這是 Bayesian pricing、Filtering 理論、disintegration-based MC 的數學基石。
2. **Skorohod Embedding**（Ch14） — 任何 martingale (mean 0, variance σ²) 都可嵌入 Brownian motion 在某個 stopping time 的值。這提供了 discrete → continuous 對應的精確結構，CLT 的過程版本（Donsker's theorem）之基礎。
3. **Infinitely Divisible Distributions = Lévy Processes**（Ch15） — 分布 F 無窮可分 ⟺ 存在 Lévy process X_t 使 X_1 ~ F。Lévy-Khintchine 公式將所有 Lévy process 刻畫為 drift + diffusion + jumps (compensated Poisson)。所有 asset return 的 jump-diffusion 建模都建立於此。
4. **Semi-martingale 是最一般的可做隨機積分的過程**（Ch26） — Bichteler-Dellacherie theorem 將 semi-martingale 刻畫為「可對 bounded predictable 過程積分並得到合理結果」的最大類。所有 ITO 理論的自然活動空間。
5. **Connections between SDE and PDE**（Ch24） — 對應 Kolmogorov forward/backward 方程、Feynman-Kac 公式；SDE dX = b(X)dt + σ(X)dW 的解的密度滿足 PDE ∂ₜp = L*p (L* 為 generator 的 adjoint)。金融：Black-Scholes PDE 正是此關係的 backward 版本。

### 可用戰術/策略
- **Regular Conditional Distribution for Bayesian Update**：在 filtering 問題，後驗分布 p(θ|Y) 由 disintegration 構造，保證在 Polish 空間上存在。
- **Lévy-Khintchine Parametrization for Model Selection**：asset return 的 Lévy process 模型需設定 (b, σ², ν)（drift、擴散、jump measure），三個參數完整刻畫；用於擬合 option smile。
- **Donsker's Invariance Principle for Rescaled Price Paths**：將離散價格序列標準化為 n^(-1/2) Σ x_i，當 n→∞ 弱收斂到 Brownian motion；這是高頻 → 中頻 scaling 的理論基礎。
- **Martingale Problem Formulation of SDE**：用 Stroock-Varadhan 框架——指定 generator L，「martingale problem solution」等同 SDE weak solution。對非 Lipschitz coefficient SDE 提供 existence。
- **Feller Process for Markov Approximation**：Feller 條件（連續 + decay）保證 Markov process 有良好 semi-group；用此檢驗 discrete Markov chain 在 scaling limit 下是否收斂到 Feller process（= 連續 Markov 過程）。

### 盲點 / 反例 / 適用邊界
- **密度極高極不友善** — 沒有例子，幾乎只有定理；博士候選人也常被勸退。讀者必須具備測度論+泛函分析深度，否則讀不下去。
- **非教學優化** — 對初學者無指引，更像 reference。學習建議配合 Protter (應用) / Williams (直觀) 同步讀。
- **缺少金融 motivation** — 全純數，讀者需自己把定理連到 Black-Scholes、Heston、Lévy model。
- **2002 年 2nd ed 略舊** — 新結果（rough path theory、backward SDE）未涵蓋；需期刊論文補。
- **習題極少** — 只有提示性練習，沒有 computational 題。

### 與 Edward 既有知識的連結
- **ZP reference book**：保留為 `ZP/math/reference/` 的 encyclopedia，查閱用；不適合 Edward 循序通讀。
- **對應 Protter Stochastic Integration**：Protter 有更多 semi-martingale 應用與例子，Kallenberg 提供嚴格證明；二者互補。
- **延伸 Revuz-Yor Continuous Martingales**：Revuz-Yor 專注連續 martingale 與 Brownian motion 細節，Kallenberg 更廣泛。
- **衝突：學習效率低** — 對 Edward 的「階段性交付」原則不友善；建議只用作 reference 而非教材。
- **可挖金礦**：Ch24 SDE-PDE 連接可直接作為 ZP 自營系統的 pricing 模組理論基礎——用 PDE 解 (finite difference) 與 SDE 解 (Monte Carlo) 互為 cross-check。
