## Numerical Optimization, 2nd Edition — Jorge Nocedal & Stephen J. Wright
**來源**: E:/課程/[10] 最佳化/Numerical Optimization, 2ed, 2006, Nocedal J. and S.J. Wright.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Introduction
- Ch2 Fundamentals of Unconstrained Optimization（convergence analysis）
- Ch3 Line Search Methods（Wolfe conditions, step-length selection）
- Ch4 Trust-Region Methods（Cauchy point, dogleg, Steihaug-CG）
- Ch5 Conjugate Gradient Methods（linear/nonlinear CG, Fletcher-Reeves, Polak-Ribière）
- Ch6 Quasi-Newton Methods（BFGS, L-BFGS, DFP, SR1）
- Ch7 Large-Scale Unconstrained Optimization
- Ch8 Calculating Derivatives（auto-differentiation, adjoint）
- Ch9 Derivative-Free Methods（Nelder-Mead, model-based）
- Ch10 Least-Squares Problems（Gauss-Newton, Levenberg-Marquardt）
- Ch11 Nonlinear Equations（Newton, Broyden, continuation methods）
- Ch12 Theory of Constrained Optimization（KKT, second-order conditions）
- Ch13 Linear Programming: The Simplex Method
- Ch14 Linear Programming: Interior-Point Methods
- Ch15 Fundamentals of Algorithms for Nonlinear Constrained Optimization
- Ch16 Quadratic Programming
- Ch17 Penalty and Augmented Lagrangian Methods
- Ch18 Sequential Quadratic Programming
- Ch19 Interior-Point Methods for Nonlinear Programming

### TL;DR (≤120字)
Nocedal-Wright 是 numerical optimization 的 operational bible——所有主流 solver（IPOPT、SNOPT、KNITRO）背後算法皆在此書。與 Boyd 的 theory-first 不同，Nocedal-Wright 專注「如何實際求解」：line search/trust region/quasi-Newton 細節、收斂證明、算法變體選擇。對 quant：calibration (local vol, Heston)、MPC (optimal execution)、robust hedging 的數值引擎全部來自此書。

### 核心本質 (3-5 條)
1. **Newton's Method 的超線性收斂**（Ch2, Ch3） — 對光滑凸函數 f，Newton step p = -H⁻¹g (H=Hessian, g=gradient) 在 x* 附近二次收斂：‖x_{k+1}-x*‖ ≤ C·‖x_k-x*‖²。代價：需計算 H 並求解 Hp=-g；對大問題不實際，需替代。
2. **BFGS / L-BFGS 是 Quasi-Newton 的黃金標準**（Ch6） — 用 rank-1 或 rank-2 update 維持 Hessian 逆近似 H_k；無需真實 Hessian 計算。L-BFGS 儲存最近 m 個 (s_k, y_k) pair，O(nm) 記憶與計算，適合 n~10^5+ 問題。優化 optimizer 首選。
3. **Trust Region vs Line Search**（Ch3, Ch4） — Line search 沿給定方向找最佳步長；Trust region 限定「信任區域」內求二次模型最優。Trust region 對 indefinite Hessian 更穩健；是 Levenberg-Marquardt、Powell dogleg 的基礎。
4. **SQP (Sequential Quadratic Programming)**（Ch18） — 對非線性約束問題 min f(x) s.t. g(x)=0，每步解 QP subproblem（linearized constraints）；Lagrangian Hessian 替代 Hessian。收斂快，是中小規模 NLP 的標準。
5. **Interior-Point Methods for NLP**（Ch19） — 以 barrier - μ Σ log(sᵢ) 加入目標（sᵢ 為 slack），primal-dual iterate；比 SQP 在大規模（n>10^4）更高效。IPOPT 是其開源實現，廣泛用於金融 optimization。

### 可用戰術/策略
- **Levenberg-Marquardt for Calibration**：對 option price calibration，objective = Σ(market - model)²；用 LM 結合 Gauss-Newton 與 steepest descent，穩健、快速。
- **L-BFGS-B for Box-Constrained Portfolio**：QP solver 之外，對大 portfolio (n>1000) 且 box constraint 0≤wᵢ≤1，L-BFGS-B 比 active-set QP 快 10 倍。
- **Adjoint Methods for Greeks**（Ch8） — 對 MC pricing，gradient 計算需 O(n) (finite diff) 或 O(1) (adjoint)；adjoint differentiation 是大維度 sensitivity 的唯一實用選擇。
- **Trust Region for Non-convex Calibration**：local vol calibration 可能 non-convex，trust region 比 line search 更穩健；避免跳到假最優。
- **Wolfe Conditions for Line Search**：Armijo（sufficient decrease）+ curvature condition；保證 step size 既足夠 descend 又不過長；L-BFGS 收斂依賴此。

### 盲點 / 反例 / 適用邊界
- **Stochastic optimization 不深入** — Sample average approximation、scenario decomposition 只輕觸；需 Shapiro 專書補。
- **Deep learning 優化缺席** — SGD、Adam、RMSprop 等 first-order methods 為現代 DL 標配，此書 2006 版只速寫；需 Goodfellow《Deep Learning》Ch8 補。
- **Black-box derivative-free 章節（Ch9）過簡** — Nelder-Mead + model-based 只 30 頁；當前 Bayesian optimization、genetic algorithms 需其他書。
- **二階導數假設** — 多數算法假設 Hessian 存在；對非光滑問題（L¹ regularization, ReLU network）需 subgradient / proximal methods。
- **缺少 GPU / parallel** — 當代大規模 training 依賴 GPU parallel，書中無著墨。

### 與 Edward 既有知識的連結
- **ZP calibration / tuning 核心**：`ZP/quant/calibration/` 與 `ZP/execution/mpc/` 的主要參考；所有 optimization 實作走此書。
- **對應 Boyd-Vandenberghe**：Boyd 教 convex theory，Nocedal-Wright 教 numerical method；Edward 兩書並讀最有效。
- **延伸 Bertsekas**：Bertsekas 在 dynamic programming / stochastic control 上更深，Nocedal-Wright 偏 deterministic optimization。
- **衝突：實作重於理論** — 對 pure math 讀者覺得不夠嚴格；但對工程師是完美 reference。
- **可挖金礦**：Ch8 adjoint differentiation 可整合進 ZP 的 Greeks pipeline——對大 portfolio 的 gradient 計算從 O(n) 降到 O(1)，顯著加速 dynamic hedging。
