## Nonlinear Programming, 3rd Edition — Dimitri P. Bertsekas
**來源**: E:/課程/[10] 最佳化/Nonlinear Programming, 3ed, 2016, Dimitri P. Bertsekas.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Unconstrained Optimization: Basic Methods
- Ch2 Unconstrained Optimization: Additional Methods
- Ch3 Optimization over a Convex Set
- Ch4 Lagrange Multiplier Theory
- Ch5 Duality
- Ch6 Dual Computational Methods（proximal, augmented Lagrangian, ADMM）
- Ch7 Nondifferentiable Optimization（subgradient, cutting plane, ε-subgradient, bundle methods）
- Ch8 Approximate and Incremental Methods（stochastic gradient, online learning）

### TL;DR (≤120字)
Bertsekas 的《Nonlinear Programming》是進階最佳化理論的權威——比 Nocedal-Wright 更深入 duality theory、subgradient methods、proximal algorithms。Bertsekas 是 dynamic programming 與 decentralized optimization 的祖師爺；此書 Ch6 ADMM、Ch7 bundle methods、Ch8 stochastic gradient 直接銜接當代 ML / distributed optimization 生態。對 quant：為複雜 non-convex、non-smooth 問題（如 robust optimization、stochastic programming）提供正式工具。

### 核心本質 (3-5 條)
1. **Subgradient for Nondifferentiable Optimization**（Ch7） — 對凸函數 f 在 x₀ 的 subgradient ∂f(x₀) = {g : f(x)≥f(x₀)+gᵀ(x-x₀) ∀x}；若 f 可微，∂f(x)={∇f(x)}；不可微時 ∂f 為集合。Subgradient method：x_{k+1} = x_k - α_k·g_k (g_k ∈ ∂f(x_k))。對 L¹-regularized problem 直接適用。
2. **Proximal Operator & Proximal Gradient**（Ch6） — prox_{α·h}(x) = argmin_y (h(y) + (1/2α)‖y-x‖²)；對很多「簡單」h 有封閉形式 (soft thresholding for L¹, projection for indicator of convex set)。Proximal gradient method：x_{k+1} = prox_{α·h}(x_k - α·∇g(x_k))；適合 composite problem g+h (smooth + simple non-smooth)。
3. **ADMM (Alternating Direction Method of Multipliers)**（Ch6） — 求解 min f(x)+g(z) s.t. Ax+Bz=c；拆解為 x-update (fixed z,λ)、z-update (fixed x,λ)、λ-update；在凸問題下線性收斂。適合大規模分散式 ML、sparse regression、consensus optimization。
4. **Duality Gap & Strong Duality in Non-convex**（Ch5） — 對非凸問題，weak duality p* ≥ d* 仍成立；strong duality p*=d* 通常不成立；但某些 special cases（如 QCQP, trust region subproblem）有 zero duality gap。實務：放鬆 non-convex 為 convex dual 給下界；branch-and-bound 利用此下界剪枝。
5. **Stochastic Gradient & Incremental Methods**（Ch8） — 對 f(x)=ΣN fᵢ(x)，每步用單一 ∇fᵢ 而非全梯度；變異數大但計算便宜。SAG、SVRG、SAGA 等 variance reduction 方法將 SGD 收斂率提升到 vs full-batch 相似。

### 可用戰術/策略
- **Proximal for Lasso**：對 min ½‖y-Xw‖² + λ‖w‖₁，proximal gradient 的 w-update = soft_threshold(w-α·Xᵀ(Xw-y), α·λ)；O(np) per iteration，大規模 LASSO 標配。
- **ADMM for Distributed Portfolio Optimization**：多個 agent 各自持有子問題，via consensus constraint wᵢ=w（global portfolio）；ADMM 迭代 agent 本地 update + global averaging；平行化自然。
- **Bundle Method for Non-smooth Optimization**：對 max over scenarios 類 robust problem，bundle method 用 past subgradients 構造 piecewise linear model + regularization；比單純 subgradient 收斂快。
- **Cutting Plane for Integer Programming Relaxation**：對 mixed-integer problem，LP relaxation + cutting plane 逐步加入 Gomory cut 或 lift-and-project cut，逼近 integer hull。
- **Mirror Descent for Probability Simplex**：portfolio weights 在 simplex 上，使用 mirror descent with entropy regularizer: w_{t+1} ∝ w_t · exp(-η·∇f(w_t))；自動保持 simplex constraint，比 projection 高效。

### 盲點 / 反例 / 適用邊界
- **比 Nocedal-Wright 更 mathematical** — 對純實作者偏理論；需搭 Nocedal-Wright 的具體算法細節。
- **Machine learning 應用輕觸** — DL 常見 optimizer (Adam, RMSprop) 只 briefly discuss；需 Bubeck《Convex Optimization: Algorithms and Complexity》補。
- **Global optimization 不處理** — 全局最優（如 simulated annealing, GA）不在範圍；需 Floudas 專書。
- **Numerical recipes 較少** — 偏 algorithm design 而非 programming detail；實作時需參考 solver 官方文件。
- **篇幅過大** — 800+ 頁，非 Edward「階段性交付」友善教材。

### 與 Edward 既有知識的連結
- **ZP 進階 optimization**：`ZP/optimization/advanced/` 參考；在 Boyd + Nocedal-Wright 之後深化。
- **對應 Boyd**：Boyd 教基礎 convex theory，Bertsekas 教 non-smooth / proximal / ADMM；二書完美互補。
- **延伸 Dynamic Programming**：Bertsekas 另著《Dynamic Programming and Optimal Control》二卷本是 Merton problem 深化。
- **衝突：抽象度高** — 對時間緊張的 Edward，建議選讀 Ch6 (proximal/ADMM) 與 Ch8 (SGD) 即可；其他章節作 reference。
- **可挖金礦**：Ch6 ADMM 可整合進 ZP 的「多策略 portfolio」優化——每個策略獨立解自己的子問題 + consensus on global budget；天然支援分散式計算。
