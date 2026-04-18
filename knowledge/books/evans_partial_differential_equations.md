## Partial Differential Equations, 2nd Edition — Lawrence C. Evans
**來源**: E:/課程/[8] PDE/Partial Differential Equations, 2ed, 2010, Lawrence C. Evans.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Part I: Representation Formulas for Solutions
  - Ch1 Introduction
  - Ch2 Four Important Linear PDE（transport, Laplace, heat, wave）
  - Ch3 Nonlinear First-Order PDE（characteristics, Hamilton-Jacobi）
  - Ch4 Other Ways to Represent Solutions（separation of variables, Fourier, Laplace transforms）
- Part II: Theory for Linear Partial Differential Equations
  - Ch5 Sobolev Spaces
  - Ch6 Second-Order Elliptic Equations（weak solutions, existence, regularity）
  - Ch7 Linear Evolution Equations（parabolic, hyperbolic, semigroup theory）
- Part III: Theory for Nonlinear Partial Differential Equations
  - Ch8 The Calculus of Variations
  - Ch9 Nonvariational Techniques
  - Ch10 Hamilton-Jacobi Equations（viscosity solutions）
  - Ch11 Systems of Conservation Laws

### TL;DR (≤120字)
Evans 是 PDE 的 modern standard——美國應用數學 PhD qualifier 指定教材。特色：從古典 (heat, Laplace, wave) 到 modern (Sobolev, weak solution, viscosity solution) 完整覆蓋。對 quant finance：Ch2 heat equation = Black-Scholes 核心；Ch10 Hamilton-Jacobi = Merton 最佳消費-投資；Ch8 變分法 = 最優停止/控制問題的嚴格框架。

### 核心本質 (3-5 條)
1. **Heat Equation Green's Function**（Ch2） — ∂ₜu = Δu 在 ℝⁿ 上的 fundamental solution Φ(x,t)=(4πt)^{-n/2}·exp(-|x|²/4t)；任意初值問題解為 u(x,t)=∫Φ(x-y,t)g(y)dy（convolution with initial data）。Black-Scholes 公式正是此 Green's function 的變形。
2. **Maximum Principle**（Ch2, Ch6） — 對橢圓/拋物 PDE，解在 boundary 或 initial 達極值；内部沒有 spurious extrema。應用於金融：option pricing function 被 intrinsic value 與 replication bound 夾緊；no-arbitrage 條件與此等價。
3. **Sobolev Space Embedding**（Ch5） — W^{k,p}(Ω) ↪ L^q(Ω) 當 1/q ≥ 1/p - k/n；解的 regularity 可提升：如果 PDE 滿足某些條件，弱解自動具有更高光滑性。Quant：option price 的 regularity 分析（是否 C²、∂² 是否存在）由此確定。
4. **Viscosity Solution for Hamilton-Jacobi**（Ch10） — Crandall-Lions 提出：HJ 方程的連續函數 u 是 viscosity solution ⟺ u 滿足 sub/super-solution 的 test function 比較條件。Merton's problem、optimal stopping 通常產生有 kink 的 value function，經典解不存在，只有 viscosity solution。
5. **Lax-Milgram Theorem for Elliptic PDE**（Ch6） — 對 bilinear form B(u,v) 與線性 functional f，若 B 連續且 coercive，則存在唯一 u 使 B(u,v)=f(v) 對所有 v。這是 finite element method 的理論基礎，也是 variational form of PDE 的 cornerstone。

### 可用戰術/策略
- **Heat Equation Solution in Black-Scholes**：對 BS 標準化為 heat eq，初值 g(x) = payoff(e^x)；直接 convolution 得 European option price 的解析式。
- **Weak Formulation for PDE Solver**：對 domain Ω, PDE L u = f，weak form ∫_Ω ∇u·∇v = ∫_Ω f v (對所有 test v)；離散化為 FEM：u ≈ Σ cᵢφᵢ, 解 stiffness matrix 方程。
- **HJB for Merton's Problem**：value function V(t,w)=sup E[u(W_T)]，HJB：∂ₜV + sup_{π,c}{(r+π(μ-r))w ∂_wV + ½π²σ²w²∂²_{ww}V - c∂_wV + u(c)}=0。對 CRRA utility 有封閉解。
- **Comparison Principle for Viscosity Solution**：兩個 viscosity solution 在 boundary 一致 ⇒ 全 domain 一致；提供唯一性與穩健性保證。
- **Energy Methods for Estimates**：對解乘以 u 或 u' 並積分，得到 ‖u‖_H¹ ≤ C·‖f‖_L²（對 elliptic）或 ‖u(T)‖_L² ≤ C·‖u(0)‖_L² (對 parabolic)；控制解的 size。

### 盲點 / 反例 / 適用邊界
- **純數傾向強** — 抽象度高，應用型讀者可能覺得過度嚴格；Wilmott-Howison-Dewynne 對金融應用更直接。
- **缺少 numerical detail** — finite difference/volume 方法細節少；需 Thomas《Numerical PDE》補。
- **高維 curse of dimensionality** — Evans 多數討論 2D-3D；金融多資產 PDE (10+ 資產) 在此 framework 失效。
- **Stochastic PDE 未涵蓋** — 需 Da Prato-Zabczyk 或 Walsh；SPDE 是當代 interest rate model (HJM) 的語言。
- **缺少 Python 實作** — FEM code 需 FEniCS 或 FreeFem++ 學習。

### 與 Edward 既有知識的連結
- **ZP PDE 嚴格參考**：`ZP/math/pde/` 主力教材；當 Wilmott-Howison-Dewynne 的直觀處理不夠時查閱。
- **對應 Wilmott-Howison-Dewynne**：WHD 是工程師視角、Evans 是數學家視角；Edward 應以 WHD 為主、Evans 為深化。
- **延伸 Fleming-Soner《Controlled Markov Processes and Viscosity Solutions》**：Evans Ch10 viscosity 的金融應用專書。
- **衝突：學習時間成本高**：Evans 789 頁對 Edward「階段性交付」原則不友善；建議選章節讀。
- **可挖金礦**：Ch8 calculus of variations 可用於 Edward 的 portfolio optimization with 軌跡約束（如 VWAP、TWAP execution）——將 execution 最適化公式化為變分問題。
