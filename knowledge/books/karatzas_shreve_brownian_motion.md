## Brownian Motion and Stochastic Calculus, 2nd Edition — Ioannis Karatzas & Steven E. Shreve
**來源**: E:/課程/[7] 隨機過程/Brownian Motion and Stochastic Calculus, 2ed, 1991, Karatzas I. and S.E. Shreve.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Martingales, Stopping Times, and Filtrations
- Ch2 Brownian Motion（construction, Lévy's characterization, strong Markov property, reflection principle）
- Ch3 Stochastic Integration（Itô integral, Itô's formula, local times, martingale representation）
- Ch4 Brownian Motion and Partial Differential Equations（Kolmogorov equations, Feynman-Kac, Dirichlet problem）
- Ch5 Stochastic Differential Equations（existence, uniqueness via Lipschitz, weak vs strong solutions）
- Ch6 P. Lévy's Theorem, Girsanov's Theorem, and Related Topics
- Ch7 Applications to Control（optimal stopping, Merton's problem）
- Addendum: Absolute Continuity of Measures, Uniqueness in Law, Itô's Rule in Its Most General Form

### TL;DR (≤120字)
Karatzas-Shreve 的《Brownian Motion and Stochastic Calculus》是 stochastic calculus 的 gold standard——專業 quant 都必讀。相對 Shreve《for Finance》更數學，涵蓋 BM 嚴格建構、Itô integral theory、SDE 存在唯一性、PDE 連接、optimal control，任何進階 quant finance 研究都要用到。1991 年第 2 版後 30 年仍未有更完整替代教材。

### 核心本質 (3-5 條)
1. **Brownian Motion 四種等價刻畫**（Ch2） — (a) independent Gaussian increments；(b) continuous path martingale with [W]_t = t（Lévy's characterization）；(c) Wiener measure on C([0,T])；(d) functional CLT limit。Lévy's characterization 尤其強大——任何 continuous martingale with quadratic variation t 就是 BM！
2. **Itô's Formula 的多維版本**（Ch3） — 對 f(t, X_t) 其中 dXⁱ = μⁱdt + σⁱdW，df = ∂ₜf dt + Σᵢ ∂ᵢf dXⁱ + ½Σᵢⱼ ∂ᵢⱼf d[Xⁱ,Xⱼ]。關鍵：dW² = dt 的「額外 drift」源自 quadratic variation。這是所有 derivative pricing、hedging、Greeks 計算的基礎。
3. **Martingale Representation Theorem**（Ch3） — 在 BM filtration 下，任何 L² martingale 可表示為 Itô integral Xₜ = X₀ + ∫₀ᵗ ψₛ dWₛ。這是金融市場「完整性」的數學本質——任何 contingent claim 可以 dynamic hedging 複製。
4. **Girsanov Theorem**（Ch6） — 等價測度變換 dQ/dP = exp(-∫θ·dW - ½∫θ²dt) (Novikov condition 下 martingale)；在 Q 下 W̃ₜ = Wₜ + ∫θds 是 BM。金融：Black-Scholes pricing 的 measure change 核心。
5. **Feynman-Kac Formula**（Ch4） — 對 PDE ∂ₜu + Lu - ru + f = 0 with terminal condition u(T,x)=g(x)，解為 u(t,x) = E[e^{-r(T-t)}g(X_T) + ∫ₜᵀ e^{-r(s-t)}f(s,X_s)ds | X_t=x]。直接連接 PDE ↔ SDE，對 Black-Scholes PDE 與 discrete 模型對比關鍵。

### 可用戰術/策略
- **Itô's Formula in Practice**：對 S_t = S₀ exp((μ-½σ²)t + σW_t)，應用 Itô 於 f(S)=log(S) 得 dlog(S) = (μ-½σ²)dt + σdW；常數化後可直接積分。
- **Girsanov for Risk-Neutral Transformation**：欲從 dS = μSdt + σSdW_P 轉為 dS = rSdt + σSdW_Q，設 θ=(μ-r)/σ；則 dW_Q = dW_P + θdt；dQ/dP = exp(-θW_T - ½θ²T)。
- **Feynman-Kac for Option Pricing**：將 C(t,S) 滿足 BS PDE 的解寫為 E_Q[e^{-r(T-t)}g(S_T)|S_t=S]；直接用 MC 估計當 PDE 難解。
- **Quadratic Variation as Realized Variance**：對高頻觀察，[X]_T ≈ Σ(X_{t_{i+1}} - X_{t_i})²；直接得到 realized variance 估計，是 volatility 交易的核心。
- **Strong vs Weak Solution**（Ch5） — 強解要求在固定 BM 下 path-wise 存在；弱解允許 BM 與 SDE 同時構造；對 non-Lipschitz coefficient (如 CIR √X)，通常只有 weak solution 存在。

### 盲點 / 反例 / 適用邊界
- **1991 年版本** — 不含 fractional Brownian motion、rough paths、BSDE 等現代 topic。
- **Lévy process / jump 沒 covered** — Karatzas-Shreve 只做連續 diffusion；需 Protter 補跳躍過程。
- **符號極其密集** — 新手需要至少 3 個月集中研讀才能消化；不適合自學者。
- **Ch7 optimal control 偏理論** — Merton problem 解釋清楚，但 policy iteration / viscosity solution 需更現代教材（Fleming-Soner）。
- **缺少 numerical** — 全是存在唯一性，沒 Monte Carlo / PDE solver；需配合 Glasserman / Seydel。

### 與 Edward 既有知識的連結
- **ZP 進階必備**：`ZP/math/stochastic_calculus/` 主力教材；Edward 若打算深入 quant research 必讀。
- **對應 Shreve Vol II**：Shreve Vol II 是 Karatzas-Shreve 的 金融應用版 + 簡化；二書配合效果最佳——先 Shreve Vol II 建立直觀，再 Karatzas-Shreve 嚴格化。
- **延伸 Protter**：Karatzas-Shreve 專注 continuous case，Protter 延伸到 semimartingale with jumps。
- **衝突：純理論無實作**：閱讀完畢需 Glasserman 或 Seydel 才能實際寫程式。
- **可挖金礦**：Ch6 Girsanov 可整合為 `ZP/quant/measure_change/` 工具模組；所有 pricing 轉換統一框架處理。
