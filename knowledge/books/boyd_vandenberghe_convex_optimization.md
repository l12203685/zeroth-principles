## Convex Optimization — Stephen Boyd & Lieven Vandenberghe
**來源**: E:/課程/[10] 最佳化/Convex Optimization, 2004, Boyd S. and L. Vandenberghe.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Part I: Theory
  - Ch1 Introduction
  - Ch2 Convex Sets（hyperplanes, cones, operations preserving convexity）
  - Ch3 Convex Functions（operations, conjugate function, quasiconvex）
  - Ch4 Convex Optimization Problems（LP, QP, SOCP, SDP, standard forms）
  - Ch5 Duality（Lagrangian, KKT, weak/strong duality, Slater's condition）
- Part II: Applications
  - Ch6 Approximation and Fitting（least squares, regularization, robust approximation）
  - Ch7 Statistical Estimation（MLE, experiment design, Chebyshev bounds）
  - Ch8 Geometric Problems（extremal volume, centering, classification, placement）
- Part III: Algorithms
  - Ch9 Unconstrained Minimization（gradient descent, Newton, BFGS）
  - Ch10 Equality Constrained Minimization（Newton's method, sequential quadratic）
  - Ch11 Interior-Point Methods（barrier, primal-dual）
- Appendices: Mathematical background, Linear algebra, Reference

### TL;DR (≤120字)
Boyd-Vandenberghe 的《Convex Optimization》（CVX 書）是當代最佳化的 bible——工程/計量/機器學習/金融全領域必讀。免費 PDF + 斯坦福公開課 + CVX Python solver 生態使其成為全球標配。對 quant：portfolio optimization、risk budgeting、VaR/CVaR 最小化、robust hedging 皆為 LP/QP/SOCP 框架下的直接應用；Ch5 duality 提供經濟直觀的「影子價格」解釋。

### 核心本質 (3-5 條)
1. **Convex = 所有 local min = global min**（Ch3, Ch4） — 這是 convex 問題的終極優勢：不存在 local trap，梯度下降必收斂到最優。金融：portfolio optimization 寫為 convex，保證單一最佳解；非 convex（如 0-1 選股整數問題）則需 branch-and-bound。
2. **KKT Conditions**（Ch5） — 最優點 x* 必滿足：primal feasibility、dual feasibility (λ≥0)、complementary slackness (λᵢgᵢ(x*)=0)、stationarity (∇f + Σλᵢ∇gᵢ + Σνⱼ∇hⱼ=0)。KKT 是檢驗候選解是否最優的通用工具，也是對偶問題構造的基礎。
3. **Lagrange Duality & Slater's Condition**（Ch5） — 原問題 min f(x) s.t. g(x)≤0，對偶 g(λ)=inf_x L(x,λ)；weak duality g(λ) ≤ p*永遠成立；strong duality p*=d* 需 Slater (嚴格 feasibility for convex problem)。對偶變數解釋為「約束的邊際成本」。
4. **Interior-Point Methods**（Ch11） — 以 barrier function φ(x) = -Σlog(-gᵢ(x)) 加入目標，得 min f(x)+tφ(x)；逐步增 t，解序列收斂到 convex problem 最優解。複雜度 O(n^{3.5}·log(1/ε))，多項式時間可解 LP/QP/SDP。
5. **Conjugate Function f*(y) = sup_x (yᵀx - f(x))**（Ch3） — Legendre-Fenchel 變換；將原函數的「梯度」資訊編碼到 conjugate 中。金融應用：risk measure 的 dual representation (ex. CVaR = sup over scenarios)；Robust optimization 的 dual formulation。

### 可用戰術/策略
- **Markowitz QP Formulation**：min wᵀΣw s.t. wᵀμ ≥ μ_target, wᵀ1=1, w≥0；完美 QP 問題，用 CVXPY 幾行 code 解決。
- **L¹-Regularization (LASSO)**：min ½‖y-Xw‖² + λ‖w‖₁；凸，SOCP 可解；效果：稀疏解（許多 wᵢ=0），適合 factor selection、alpha signal selection。
- **CVaR Minimization (Rockafellar-Uryasev)**：min α + 1/(1-β)·E[max(L-α, 0)]；LP 版本 (scenario-based)：min α + 1/(N(1-β))·Σzᵢ s.t. zᵢ≥Lᵢ-α, zᵢ≥0。
- **Robust Optimization**：min max_{u∈U} f(x,u) (U 為不確定集)；若 U 為 ellipsoidal，問題可轉為 SOCP；若 polyhedral，可轉為 LP。
- **Duality for Shadow Price Analysis**：解 primal 得最優 x*，同時得 dual λ*；λᵢ* 即「約束 gᵢ 的邊際成本」。用於解釋為何 portfolio constraint 改變後 Sharpe 下降多少。

### 盲點 / 反例 / 適用邊界
- **Non-convex 不 covered** — 0-1 整數、combinatorial、deep learning 非 convex 都不適用；需 Bertsekas《Nonlinear Programming》補。
- **Stochastic optimization 輕觸** — 只在 Ch7 提及；需 Shapiro-Dentcheva-Ruszczynski 專書。
- **算法章節略舊** — 2004 年版本，缺少 ADMM、proximal methods、Nesterov acceleration 等 2010 後新標準。
- **Symbolic solver 假設** — 假設 solver 能處理問題；大規模問題 (n>10^6) 需 first-order methods 不在此書。
- **缺少 machine learning 連結** — 當代 convex ML（logistic, SVM, Lasso）僅輕觸。

### 與 Edward 既有知識的連結
- **ZP 最佳化核心**：`ZP/optimization/` 主推教材；Edward 所有 portfolio / risk / hedging 問題都走此書 framework。
- **對應 Nocedal-Wright**：Boyd 偏 convex 理論 + application，Nocedal-Wright 偏一般 numerical 算法；二書互補。
- **延伸 Bertsekas**：Bertsekas 處理 non-convex 與 dynamic programming；是 Boyd 的自然延伸。
- **衝突：理論偏向 LP/QP** — 對 deep learning 非 convex 問題需另尋方法。
- **可挖金礦**：Ch7 CVaR 最佳化 + LP formulation 可直接整合進 `ZP/risk/cvar_optimizer/`，作為 ZP 自營系統的風險預算分配核心引擎。
