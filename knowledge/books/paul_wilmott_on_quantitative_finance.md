# Paul Wilmott on Quantitative Finance (2ed) — Paul Wilmott

### 目錄
1. 核心本質 — 英國系派 Quant 教科書：PDE 先於 Martingale
2. 可用戰術 — Delta hedging、American options、Interest rate models
3. 盲點/反例 — 2008 後的新數學工具未涵蓋
4. 與 Edward 既有知識的連結

### TL;DR
Paul Wilmott (Wiley 2006, 2ed, 三卷套書約 1500 頁 75+ 章) 是英國派 quant finance 教科書的代表，作者是 Oxford Mathematical Institute 教授 + Wilmott Magazine 創辦人，以嚴格數學 + 實作 code（含 VB code for Excel）並重著稱。**三卷結構**：Vol 1 (Ch 1-27) Mathematical & Financial Foundations + BSM + PDE + American Options + Fixed Income；Vol 2 (Ch 28-52) 進階 Equity / FX / Commodity Models + Stochastic Volatility + Jump Diffusion + Copulas；Vol 3 (Ch 53-76) Credit Risk + Exotics + Monte Carlo + Finite Difference + Risk Management。Wilmott 的**獨特風格**：PDE 派思維為主（相較 Shreve 的 martingale measure 派），強調 physical intuition + empirical calibration + implementation detail，附 VB code 讓讀者直接跑。書中幽默諷刺（「prove it yourself if you have a few months free」）與嚴肅數學並列。**核心哲學**：金融工程不只是定價，還要（1）hedge 要 robust、（2）model 要能 calibrate 到 market、（3）risk management 要能應對 model misspecification。

### 核心本質
1. **BSM PDE 是金融物理學的中心等式（Vol 1 Ch 5-6）**：∂V/∂t + ½σ²S²∂²V/∂S² + rS∂V/∂S - rV = 0。Wilmott 強調這是 parabolic PDE 與熱方程 ∂u/∂t = α∂²u/∂x² 同構——這就是為何 quant 可以借用物理 heat equation 的解法（Fourier transform、Green's function）。PDE 方法的優勢：exotic payoff 直接當 boundary condition 塞進去求解，比 martingale-based Monte Carlo 快且 deterministic。
2. **Delta Hedging 的 Implementation Detail（Vol 1 Ch 12）**：理論上 continuous hedging 讓 option 無風險，實務上 discrete hedging 產生 tracking error。Wilmott 推導 E[hedging error²] = ½σ²(ΔS)² · Γ²·T/n，n 是 hedge 頻率。意義：hedge 越頻繁誤差越小但 transaction cost 越高；optimal n 在兩者 trade-off。實務 desk 每日 2-4 次 delta hedge 是經驗平衡。
3. **American Options 的 Free Boundary Problem（Vol 1 Ch 9）**：American put 的早期行使 (early exercise) 產生一條 free boundary S*(t)——在此邊界以下應該 exercise 獲得 intrinsic value。Wilmott 用 PSOR (Projected Successive Over-Relaxation) 算法數值求解 LCP (linear complementary problem)，比 Monte Carlo 快 10-100x 且更精準。
4. **Multi-asset Options 的 Correlation Challenge（Vol 1 Ch 11）**：basket option、best-of、worst-of 等 multi-asset payoff 需要 correlation structure。PDE 方法在 2+ dim 記憶體爆炸，常用 Finite Difference + ADI (Alternating Direction Implicit) 或 Monte Carlo + Cholesky decomposition。書中給 sample code。
5. **Calibration 的 Inverse Problem（Vol 2 Ch 29-30）**：market 給 option price，如何反推 risk-neutral parameters (σ, r, dividend yield)？Wilmott 討論 local volatility (Dupire) 與 stochastic volatility (Heston) 兩派 calibration——LV 給 perfect fit 到 market 但 dynamics 不穩定；SV 動力學合理但 fit 誤差較大。

### 可用戰術
1. **Finite Difference Grid for American Options**：Crank-Nicolson scheme 在 S-t grid 做 implicit + explicit 混合，每個 node 檢查 early-exercise condition V ≥ (K-S)+。一個 100×100 grid 一次 pricing < 0.1 sec，batch 幾千個合約即時報價。
2. **Implied Volatility Surface Calibration（Vol 2 Ch 30）**：每個市場 strike/maturity 對應 implied vol，繪 3D surface（moneyness × time to expiry）。Wilmott 給 Nelder-Mead 優化 + weighted least squares 校準 Heston 5 參數。
3. **Jump Diffusion for Fat Tails（Vol 2 Ch 32）**：Merton 1976 的 S_t = S_0·exp((μ-½σ²-λκ)t + σB_t + Σ_{i=1}^{N_t} Y_i)，其中 N_t 是 Poisson(λt)、Y_i 是 jump size。可以 fit smile skew + 更好抓 tail event。pricing 用 Ch 32 的 series expansion 或 Monte Carlo.
4. **Variance Swap Static Replication via Log Contract（Vol 2 Ch 33）**：realized variance = -2·∫(ln(S_T/S_0) dt)，用 infinite OTM strip of vanilla options 複製。Wilmott 推導 replication error 隨 strike granularity 降低——20 個 strike 可達 99% 準確。
5. **Monte Carlo Variance Reduction（Vol 3 Ch 68）**：control variate + antithetic sampling + stratified sampling 可減 20-100x 所需 simulation 次數。對 path-dependent options (Asian, Barrier) 尤其有用——vanilla option price 作 CV 通常可降 10x variance.

### 盲點/反例
1. **PDE 方法對高維災難（Curse of Dimensionality）**：2-asset basket 已需 3-D grid（x1, x2, t），5-asset basket 就超出一般計算機記憶體。實務上 >3 assets 必須改 Monte Carlo。Wilmott 2006 年 QC GPU 還未普及，沒涵蓋 GPU-accelerated PDE solver（2015+ 才成熟）。
2. **Stochastic Volatility 章節停在 2005 年**：Heston, SABR 都有涵蓋，但 rough vol (Gatheral-Jaisson-Rosenbaum 2014+) 完全缺席。Path-dependent volatility、regime-switching SV 也沒。
3. **Machine Learning 幾乎為零**：Wilmott 2006 年 ML 還未進入 quant 主流。2019+ neural network SDE solver、deep hedging (Buehler et al. 2019)、Differentiable ML 是新工具，這本沒。
4. **Excel VBA 實作過時**：書中 code 都是 VBA for Excel 2003/2007；現代 quant 團隊用 Python/C++/Julia。讀者要自己 port，VBA 寫法也不反映現代 vectorized computing.
5. **Credit Derivatives 章節受 2008 之前限制**：Vol 3 Ch 67-68 的 CDO 定價假設 Gaussian copula 主流，沒 post-crisis 的 base correlation smile + local correlation + Bayesian copula 等修正。

### 與 Edward 既有知識的連結
- **對照 Neftci《Principles of Financial Engineering》（本輪）**：Neftci 偏 synthesis (how to build products)，Wilmott 偏 pricing (how to value them)。兩本加起來覆蓋 financial engineer 的兩面技能。
- **對照 Frontiers QF Vol+Credit (本輪)**：Frontiers 是 2009 post-crisis 的 vol/credit 前沿研究，Wilmott 2006 是 pre-crisis baseline。讀 Wilmott 知 classical baseline，讀 Frontiers 知 2008 後修正。
- **對照 Focardi-Fabozzi《Mathematics of Financial Modeling》（本輪）**：Focardi-Fabozzi 偏 math foundation (calculus, linear algebra, prob)，Wilmott 偏 financial engineering application。Focardi 為 Wilmott 提供 math background，Wilmott 把 math 變成 pricing code。
- **對照 Higham《Financial Option Valuation》（Round 1）**：Higham 是 intro 級 mathematical BSM 教材 (200 頁)，Wilmott 是 comprehensive reference (1500 頁)。讀 Higham 快速起步，讀 Wilmott 查細節。
- **對照 ZP/derivatives 模組**：若 ZP 要加台指選擇權 pricing 模組，Wilmott Vol 1 Ch 5-12 是 minimum viable reference——BSM + PDE + Delta hedge + American + multi-asset。Code 雖 VBA 但 logic 可 port Python。
- **對照 Poker 的 Monte Carlo Equity Calculator**：撲克 solver (PioSolver, GTO+) 本質上就是 Monte Carlo simulation — 模擬對手 hand range 下的 EV 分布。Wilmott Vol 3 Ch 68 的 variance reduction 技巧（control variate, antithetic sampling）在 poker solver 裡同樣適用，能把 solver 運算時間從小時降到分鐘。
