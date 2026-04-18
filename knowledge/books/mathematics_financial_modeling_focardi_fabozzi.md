# The Mathematics of Financial Modeling and Investment Management — Focardi & Fabozzi

### 目錄
1. 核心本質 — 金融建模所需的數學基礎全圖
2. 可用戰術 — Calculus / Matrix / Optimization / Stochastic 各層工具
3. 盲點/反例 — 2004 前的數學工具未覆蓋現代 ML
4. 與 Edward 既有知識的連結

### TL;DR
Focardi-Fabozzi (Wiley 2004, 約 800 頁 17+ 章) 是寫給 practitioner 的 "financial math textbook"——把金融建模需要的**全部數學基礎**在一本書內完整呈現：set theory、calculus、matrix algebra、linear algebra、probability、random variables、stochastic processes、differential equations、Itô calculus、optimization、dynamic programming、Monte Carlo、regression、factor models、portfolio optimization。**結構**：Ch 1-2 金融市場與 investment management 過程（起引）、Ch 3 Milestones in Financial Modeling（歷史脈絡 Pareto→Bachelier→Markowitz→MM→EMH→CAPM→APT→BSM）、Ch 4-6 數學基礎（calculus, matrix, probability）、Ch 7-9 stochastic process（Markov, martingale, Itô）、Ch 10-12 PDE + numerical methods、Ch 13-15 optimization + dynamic programming、Ch 16-17 regression + factor model 在金融的應用。**定位**：這本是比 Neftci 更「數學基礎」、比 Shreve 更「廣」的教材——給無 PhD 數學背景但要做 quant 的投資專業人士一條 catch-up 路徑。**特色章節**：Ch 3 Milestones 的歷史敘事、Ch 4 "Application to Bond Analysis"（duration & convexity 的 Taylor 展開推導）、Ch 11 Stochastic Calculus Application（BSM 從 Itô lemma 兩頁推出）。

### 核心本質
1. **金融工程的歷史脈絡（Ch 3）**：Focardi 從 Pareto (19 世紀經濟統計)、Walras (general equilibrium)、Bachelier 1900 (Brownian motion 在 option pricing 首先應用，比 Einstein 1905 物理應用早 5 年)、Lundberg 1903 (保險業的 ruin theory)、Markowitz 1952 (portfolio selection)、Modigliani-Miller 1958 (capital structure)、Fama 1965/Samuelson 1965 (EMH)、Sharpe 1964/Lintner 1965/Mossin 1966 (CAPM)、Merton 1973 (multifactor CAPM)、Ross 1976 (APT)、Black-Scholes-Merton 1973 (option pricing) 連起完整敘事。讀這章知道每個「公式」背後的歷史動機。
2. **Taylor 展開是定價的通用工具（Ch 4）**：Bond 定價用 Taylor: ΔP/P ≈ -D·Δy + (1/2)C·(Δy)²，其中 D = duration、C = convexity。Option 定價：Δ價 ≈ Delta·ΔS + (1/2)Γ·(ΔS)² + Theta·Δt + Vega·Δσ。所有衍生品 P&L attribution 本質都是 Taylor 展開——一階是 Delta/Duration 管理，二階是 Gamma/Convexity 管理，時間項是 Theta/carry。
3. **Itô Lemma 是隨機微積分的核心（Ch 9-11）**：d[f(X_t, t)] = ∂f/∂t dt + ∂f/∂x dX_t + (1/2)·∂²f/∂x² (dX_t)²。關鍵：dB_t·dB_t = dt（不像普通微積分 ≈ 0）。這讓 BSM 推導成立——option price V(S,t) 對 S (Brownian) 的 Itô expansion 產生無風險 hedging 組合。
4. **Matrix Decomposition 是 factor model 的根基（Ch 5）**：covariance matrix Σ = V·Λ·V^T (eigenvalue decomposition)，principal component = eigenvector of Σ。Cholesky decomposition Σ = L·L^T 用於 Monte Carlo 生成 correlated normal。SVD = U·Σ·V^T 是 dimension reduction 的最通用工具。所有 factor risk model、PCA、statistical arbitrage 都依賴這些分解。
5. **Optimization 分類與 KKT 條件（Ch 13）**：convex vs. non-convex、equality vs. inequality constraint、linear vs. quadratic objective。KKT (Karush-Kuhn-Tucker) 條件：∇f + Σλ_i∇g_i + Σμ_j∇h_j = 0 + complementary slackness。Markowitz mean-variance 是 QP problem 有 closed-form；Black-Litterman 是 Bayesian QP；CVaR optimization 是 LP。

### 可用戰術
1. **Duration-Convexity 估 Bond Price Change（Ch 4 p.112）**：ΔP/P ≈ -D·Δy + (1/2)·C·(Δy)²。30-year Treasury D≈18, C≈400, 若 yield +1%，ΔP/P ≈ -18% + 2% = -16%；yield -1% 則 +20%。Convexity 提供正凸性 value——duration-matched bond 組合的 convexity 越高越好。
2. **Cholesky Monte Carlo 模擬 Correlated Return（Ch 5）**：給 covariance Σ，做 Cholesky L. 生成 z ~ N(0,I)，return = μ + L·z 自動 follow multivariate normal with covariance Σ。對所有 asset class 模擬同時用一個 L matrix。實務 risk simulation 的基本框架。
3. **Principal Component Analysis for Yield Curve（Ch 5 + Ch 16）**：對 zero rate time series 做 PCA，前 3 個 PC 解釋 95%+ 變異——parallel shift, slope, curvature。這成為利率 risk management 的標準三因子 hedging 框架。
4. **Itô Lemma 應用到 Geometric Brownian Motion（Ch 9）**：若 dS = μS dt + σS dB，則 d(ln S) = (μ-σ²/2) dt + σ dB。意義：log return 是 arithmetic Brownian，但 S 本身是 geometric——解釋為何「報酬率」要取 log、GBM 下股價 lognormal。
5. **Lagrangian Multiplier for Constrained Optimization（Ch 13）**：Markowitz 問題 min w^T Σ w s.t. μ^T w = r, 1^T w = 1，Lagrangian L = w^T Σ w - λ_1(μ^T w - r) - λ_2(1^T w - 1)，∂L/∂w = 0 給 efficient frontier closed-form: w* = Σ^{-1}·(λ_1 μ + λ_2 1)。這是所有 MV optimizer 的 underlying math。

### 盲點/反例
1. **2004 出版，post-2005 ML 工具未涵蓋**：neural net、XGBoost、transformer、kernel method 都缺席。GAN、reinforcement learning、variational inference 等 2015+ 興起的工具完全沒有。現代 financial ML 必須補 Kelly-Xiu（Round 1）或 Géron（本輪）。
2. **PDE 與 finite difference 章節過於基礎**：Ch 11-12 的 numerical PDE 只到 explicit + Crank-Nicolson 基本；沒高階 adaptive FD、sparse grid、adjoint methods 等 current state-of-art。
3. **Stochastic Volatility 與 Jumps 輕描淡寫**：Ch 9 Itô 只講 standard GBM，Heston SV model 與 Merton jump diffusion 只有兩頁介紹。做 exotic options 或 VIX 衍生品要補 Gatheral《Volatility Surface》或 Frontiers QF（本輪）。
4. **Bayesian 章節偏簡**：Ch 17 的 regression + factor model 停在 frequentist；Bayesian regression、MCMC、hierarchical model 只在附錄略提。做 portfolio Bayesian estimation 要補 Rachev（Round 1）。
5. **代碼完全缺席**：800 頁純數學 + 少量 analytic example，沒 Python/R code。讀者要自己 implement。配合 Hastie-Tibshirani《Elements of Statistical Learning》的 code 使用更實用。

### 與 Edward 既有知識的連結
- **對照 Fabozzi-Focardi-Kolm《Financial Modeling of Equity Market》（本輪）**：兩本同一作者群——這本是 math foundation（general），那本是 equity application (specific)。讀這本做背景，讀那本做應用。
- **對照 Casella-Berger《Statistical Inference》（本輪）**：C-B 是 pure stats，這本是 applied math for finance。兩本互補——一個建統計理論，一個建 finance-specific 數學直覺。
- **對照 Neftci《Principles of Financial Engineering》（本輪）**：Neftci 是 engineering approach（synthesize products），FF 是 mathematics approach（tools to model products）。Neftci 教「這個 payoff 怎麼做」，FF 教「這個 formula 怎麼推」。
- **對照 ZP 的 math foundation gap**：我的 ZP 有策略、有 backtest、有 risk 管理，但沒統一的數學語言。FF 提供一個可以 bookmark 的 reference——遇到 duration、Itô、KKT、PCA、Cholesky 不懂時直接翻對應章。
- **對照 Poker 的 combinatorics + EV calc**：撲克 core math = combinatorics (how many ways to make a hand) + probability (odds of hitting draw) + EV calculation (mixed strategy equilibrium)。FF 的 Ch 6-7 probability + Ch 13 optimization 直接對應——poker solver 本質是 LP/QP problem，金融 portfolio optimizer 是同樣問題的 relabeling。
- **對照 DNA §2 axiom 1「Derivative > level」**：金融變化用 Taylor expansion（∂^n f / ∂x^n），最重要是 first + second derivative（Delta + Gamma）。這正是 axiom 1 的數學表達——level 是當前價值，derivative 是變化速率。Focardi Ch 4 Taylor 展開章節為這個哲學公理提供了直接數學語言。
