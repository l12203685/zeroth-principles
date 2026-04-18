## Convex Optimization — Stephen Boyd & Lieven Vandenberghe
**來源**: Cambridge University Press canonical (free PDF on Stanford)  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- **Part I Theory (1-5)**：convex sets、convex functions、convex optimization problems、duality
- **Part II Applications (6-8)**：approximation & fitting、statistical estimation、geometric problems
- **Part III Algorithms (9-11)**：unconstrained minimization、equality-constrained、interior-point methods
- 附錄 Math background、Problems、CVX software

### TL;DR (≤120字)
Boyd-Vandenberghe 是凸優化的標準教科書，MIT/Stanford 課 + CVXPY 軟體。對 ML/金融的價值：大量模型 (OLS、Lasso、Ridge、SVM、Markowitz、CVaR) 都是 convex problem；識別 convex → 保證全域最優 + 有效演算法。金融 portfolio optimization 第一原理就是 convex（mean-variance、CVaR、risk parity）。書厚 (700 頁) 但前 5 章掌握 → CVX 寫下就自動求解。

### 核心本質 (3-5 條)
1. **Convex set + convex function = convex problem（本質，第 1-4 章）** — 任意兩點內任一點仍在集合 ⇒ convex set；f(θx+(1-θ)y) ≤ θf(x)+(1-θ)f(y) ⇒ convex function。兩者結合 → convex optimization problem → 全域最優 = 局部最優。
2. **Lagrangian + KKT conditions（本質，第 5.5 節）** — 約束優化的必要條件：stationarity + primal feasibility + dual feasibility + complementary slackness；convex problem 下也是充分。
3. **Duality gap 可作為 convergence check（本質，第 5.4 節）** — Primal value ≥ Dual value；gap=0 ⇔ strong duality。Interior-point 算法同時跑 primal/dual，gap 為 stopping criterion。
4. **OLS、Lasso、Ridge、SVM 皆 convex（本質，第 7-8 章）** — 都能寫成 min f(x) s.t. constraints 的 convex form；用 CVXPY 可輕鬆實作，不需手寫梯度。
5. **Interior-point method 是 modern solver 核心（本質，第 11 章）** — 對 log-barrier 平滑後 Newton method；MOSEK、Gurobi 皆基於此；比 simplex 在大型問題更有效率。

### 可用戰術/策略
- **Markowitz via CVXPY**：max w'μ - λw'Σw s.t. Σw = 1, w ≥ 0；一行 CVX 解。
- **CVaR optimization**：min CVaR = min (α + 1/(1-β) E[max(loss-α, 0)])；Rockafellar-Uryasev 2000 的 LP 形式，CVXPY 可解。
- **Lasso via CVX**：min ||y - Xβ||² + λ||β||_1；直接 CVX 不需手寫 LARS 或 coordinate descent。
- **Risk parity via iterative**：σ_i × ∂σ_port/∂w_i = constant across i；fixed-point iteration 收斂。
- **Robust portfolio optimization**：uncertainty in μ → min max over μ ∈ ellipsoid；second-order cone program (SOCP)，仍 convex。

### 盲點 / 反例 / 適用邊界
- **非凸世界一片荒**：deep learning loss 全部 non-convex；本書無著墨，需讀 Ruder / Bubeck non-convex 專論。
- **整數變數無解**：mixed-integer programming 需另讀 Wolsey。
- **隨機優化輕**：Part II chap 6.2 僅略；stochastic optimization 需 Shapiro 或 Nemirovski。
- **實作細節少**：第 11 章 interior-point 略過細節；實作用 MOSEK/CVXPY 即可。
- **理論比例高**：證明多、範例少；讀者需邊讀邊實作加深理解。

### 與 Edward 既有知識的連結
- **對齊 ZP portfolio optimization**：所有 allocation 問題先判斷 convex；是 → CVXPY 秒解；否 → 改寫或 approximation。
- **延伸 Vince Portfolio Math (Round 1)**：Vince optimal-f 是非凸；Boyd 告訴你為什麼難、何時可近似 convex。
- **衝突點**：Boyd 偏 engineer / optimizer；實務金融 loss 如 drawdown control 為 non-convex；需混用 genetic algorithm / Bayesian opt。
- **可挖金礦**：第 7.4 robust optimization 範本直接套用「μ 估計不確定」情境；比 naive Markowitz 穩健。
- **對接 Nesterov Introductory Lectures on Convex Optimization**：Nesterov 偏理論、Boyd 偏應用；兩書並讀完整。
