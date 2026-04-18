## The Mathematics of Financial Derivatives: A Student Introduction — Paul Wilmott, Sam Howison, Jeff Dewynne
**來源**: E:/課程/[9] 金融數學/The Mathematics of Financial Derivatives A Student Introduction, 1995, Wilmott P., Howison S. and J. Dewynne.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Part I: Basic Option Theory
  - Ch1 An Introduction to Options and Markets
  - Ch2 Asset Price Random Walks（binomial, continuous time GBM）
  - Ch3 The Black-Scholes Model（PDE derivation, boundary conditions）
  - Ch4 Partial Differential Equations（diffusion equation, similarity, Fourier methods）
  - Ch5 The Black-Scholes Formula（Green's function, explicit European call formula）
  - Ch6 Variations on the Black-Scholes Model（dividends, time-dependent parameters）
  - Ch7 American Options（free boundary problem, smooth-pasting condition）
- Part II: Numerical Methods
  - Ch8 Binomial Methods
  - Ch9 Finite-Difference Methods（explicit, implicit, Crank-Nicolson, stability）
  - Ch10 Methods for American Options（projected SOR, LCP formulation）
- Part III: Further Option Theory
  - Ch11 Exotic and Path-Dependent Options（Asian, lookback, barrier）
  - Ch12 Bond Models and Interest Rate Derivatives（Vasicek, CIR, HJM）
  - Ch13 Convertible Bonds

### TL;DR (≤120字)
Wilmott-Howison-Dewynne 是 PDE 視角的金融衍生品教材經典——從 diffusion equation 與 Fourier methods 出發嚴格推導 Black-Scholes，而非跳過測度論。對 PDE / numerical methods 背景讀者是最自然入口。Ch9-10 的 finite-difference 方法是業界 PDE-based pricer 的藍本；Ch7 American option 的 free-boundary PDE 是 LCP 方法的經典起點。

### 核心本質 (3-5 條)
1. **Black-Scholes PDE 來自 Delta-Hedging Argument**（Ch3） — 建構無風險組合 Π = V - ΔS (Δ=∂V/∂S)，應用 Itô + no-arbitrage 得 PDE：∂ₜV + ½σ²S²∂²V/∂S² + rS∂V/∂S - rV = 0。這是比測度論導出 BS 更直觀的「工程師」推導路徑。
2. **BS PDE ⟷ Heat Equation (Diffusion)**（Ch4） — 標準變換 S=Ke^x, t=T-2τ/σ², V=K·e^{αx+βτ}·u(x,τ) 化 BS PDE 為 ∂ₜu=∂_{xx}u (heat equation)。Green's function 給封閉解，也是 numerical stability 分析的基礎。
3. **American Option 的 Free Boundary Problem**（Ch7） — American put 滿足：(a) 在 early-exercise region：V=K-S；(b) 在 holding region：BS PDE；(c) 在 boundary S*(t)：value matching V=K-S 與 smooth-pasting ∂V/∂S = -1。自由邊界位置 S*(t) 需一起求解。
4. **Finite-Difference Stability (von Neumann Analysis)**（Ch9） — Explicit scheme 要求 Δt/(Δx)² ≤ 1/(σ²)；Implicit 無條件穩定；Crank-Nicolson 是二階精度折衷。實務中 implicit 或 CN 為標準，避免時間步長限制。
5. **Linear Complementarity Problem (LCP) for American**（Ch10） — LCP 公式：min(L·V, V-payoff)=0，其中 L 為 BS PDE 運算子。projected SOR 或 splitting method 可解 LCP，是 American option 的 canonical numerical 方法。

### 可用戰術/策略
- **Crank-Nicolson Scheme**：時間二階精度 + unconditionally stable；但在 payoff 不連續處（如 digital option）會有 oscillation，需要引入 Rannacher smoothing（前兩步用 implicit）。
- **Similarity Reduction for Exotic**：對 Asian option，定義 similarity variable ζ = I/S（I=running integral），可將 2D PDE 降為 1D，計算成本從 O(N²) 降到 O(N)。
- **Green's Function for Continuous Barrier**：對 barrier option，經由 reflection principle 構造 BS PDE 的 Green's function 並減去 image source；封閉解不需 MC。
- **Explicit Scheme Discretization**：V_n^j = Δt·[½σ²S²∂²V + rS∂V - rV]^j_{n+1} + V_{n+1}^j；central difference for ∂², central for ∂；Δt limited by stability but simple to code.
- **Projected SOR for LCP**：iterate V_n^k = max(V_n^k via Gauss-Seidel, payoff_n)；確保 V ≥ intrinsic value 的 constraint；實作比 policy iteration 更穩健。

### 盲點 / 反例 / 適用邊界
- **1995 年版** — 不含 stochastic vol (Heston)、SABR smile、LIBOR market model 現代模型；Wilmott 後續的《Paul Wilmott on Quantitative Finance》三卷本有補。
- **單一 asset focus** — 多資產選擇權（rainbow、basket）只輕觸；高維 PDE 數值方法需其他書。
- **無 Python/C++ 代碼** — 理論與 pseudocode 為主，實作需自補。
- **偏離 measure-theoretic framework** — 優點是直觀，缺點是不連接到 Shreve / Karatzas-Shreve 正式理論。
- **缺少 calibration** — 假設 σ 已知，沒 implied vol surface 與 local vol / stochastic vol 校正。

### 與 Edward 既有知識的連結
- **ZP 數值方法核心**：`ZP/quant/pde_solver/` 主推教材；Edward 若需實作 PDE-based pricer 必讀。
- **對應 Shreve Vol II**：Shreve 用 stochastic calculus，WHD 用 PDE；二書同主題不同路徑，並讀最佳。
- **延伸 Seydel《Tools for Computational Finance》**：Seydel 對 numerical methods 更深入，WHD 提供理論基礎。
- **衝突：偏老式 PDE 方法**：當代已大量轉向 FFT、Monte Carlo、neural network；PDE 在高維失效。
- **可挖金礦**：Ch9 CN scheme + Ch10 LCP 可作為 ZP 自營系統 American option pricer 的標準實作基礎。
