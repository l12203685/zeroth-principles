## Introduction to Linear Algebra, 5th Edition — Gilbert Strang
**來源**: E:/課程/[2] 線性代數/Introduction to Linear Algebra, 5ed, 2016, Gilbert Strang.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Introduction to Vectors
- Ch2 Solving Linear Equations（Gaussian elimination, LU decomposition）
- Ch3 Vector Spaces and Subspaces（column space, null space, rank）
- Ch4 Orthogonality（projections, least squares, Gram-Schmidt, Fourier）
- Ch5 Determinants
- Ch6 Eigenvalues and Eigenvectors（similarity, diagonalization, systems of differential equations）
- Ch7 Singular Value Decomposition (SVD)
- Ch8 Linear Transformations
- Ch9 Complex Vectors and Matrices
- Ch10 Applications（graphs/networks, Markov matrices, Fourier series, linear programming, computer graphics）
- Ch11 Numerical Linear Algebra（Gaussian elimination, iterative methods, eigenvalue algorithms）
- Ch12 Linear Algebra in Probability & Statistics

### TL;DR (≤120字)
Strang 的《Introduction to Linear Algebra》是全球最流行的線性代數教材——MIT OpenCourseWare Strang 教學 video 累積 10M+ 觀看次數。特色：幾何直觀 + 四大基本子空間的統一視角 (column / row / null / left-null)。相對 Axler 的抽象取向更實用，對 quant（PCA、regression、eigen-analysis、Kalman）全適用。

### 核心本質 (3-5 條)
1. **四大基本子空間 (The Big Picture)**（Ch3） — 對 m×n 矩陣 A：Column space C(A) ⊂ ℝᵐ, Null space N(A) ⊂ ℝⁿ, Row space C(Aᵀ) ⊂ ℝⁿ, Left-null N(Aᵀ) ⊂ ℝᵐ；關係：C(Aᵀ)⊥N(A)，C(A)⊥N(Aᵀ)；rank(A)+nullity(A)=n。Strang 的核心教學框架，一張圖總結整個線性代數。
2. **Projection = Closest Point = Least Squares**（Ch4） — 投影 p = A(AᵀA)⁻¹Aᵀb；即 argmin_x ||Ax-b||² 的解 x̂ = (AᵀA)⁻¹Aᵀb。金融：CAPM beta estimation、multi-factor regression、Kalman filter 更新步驟全是 projection。
3. **Eigenvalue Decomposition A = SΛS⁻¹**（Ch6） — 如 A 有 n 個獨立 eigenvector，A = SΛS⁻¹（S 由 eigenvector 組成）。計算 Aᵏ = SΛᵏS⁻¹ 變容易；Markov chain stationary 即 eigenvalue=1 的 eigenvector；portfolio Principal Component 正是 covariance matrix 的 eigenvector。
4. **SVD A = UΣVᵀ 是線性代數最一般的工具**（Ch7） — 任何矩陣（不必方陣、不必可對角化）都有 SVD；U, V 為 orthogonal，Σ 為對角（singular values）。應用廣泛：low-rank approximation (truncate σᵢ)、pseudo-inverse、compressed sensing、PCA、recommendation system。
5. **Positive Definite & Positive Semi-Definite**（Ch6） — A PSD ⟺ xᵀAx ≥ 0 ∀x ⟺ eigenvalues ≥ 0 ⟺ A = BᵀB；PD 嚴格大於 0。Covariance matrix 必為 PSD；portfolio variance wᵀΣw ≥ 0；optimization convex 條件常由 PSD 刻畫。

### 可用戰術/策略
- **Normal Equations for Regression**：β̂ = (XᵀX)⁻¹Xᵀy；若 XᵀX 奇異，加 ridge：β̂ = (XᵀX+λI)⁻¹Xᵀy；直接解 multi-factor regression。
- **Cholesky for Correlated Sampling**：Σ = LLᵀ (lower triangular L)；由 z~N(0,I) 生成 correlated x = Lz ~ N(0,Σ)；Monte Carlo simulation 標配。
- **SVD for Dimensionality Reduction**：對 m×n data matrix X = UΣVᵀ，truncate 到前 k 個 singular values 得 X_k = U_k·Σ_k·Vᵀ_k；rank-k 最佳近似 (Eckart-Young)；用於 factor model 與 noise filtering。
- **Power Iteration for Dominant Eigenvalue**：x_{k+1} = Ax_k / ‖Ax_k‖ 收斂到最大 eigenvalue 的 eigenvector；PageRank 算法的核心；portfolio 的 "first principal factor" 估計。
- **LU for Linear System**：A=LU，解 Ax=b 變解 Ly=b (forward sub) + Ux=y (back sub)；O(n²) 一次分解後可解多個 b；在 backtest / pricing 多個 scenarios 適用。

### 盲點 / 反例 / 適用邊界
- **抽象較淺** — Axler 的「無 determinant」路線更嚴格；Strang 偏計算。
- **Infinite-dim 輕觸** — Hilbert space 只 briefly；操作性 Fourier / spectral 需其他書。
- **缺少 tensor** — Tensor network, multilinear algebra 無涵蓋；對 deep learning 需 Hackbusch《Tensor Spaces》補。
- **Numerical stability 基礎** — Ch11 numerical 只 35 頁；深度需 Golub-Van Loan《Matrix Computations》。
- **習題偏計算** — 對證明訓練不夠；純數路線建議 Axler。

### 與 Edward 既有知識的連結
- **ZP 線性代數基礎**：`ZP/math/linear_algebra/` 首選教材；Edward 所有 quant 工作的基礎工具。
- **對應 Axler**：Axler 偏抽象數學，Strang 偏計算與應用；Edward 以 Strang 為主、Axler 作深化選項。
- **延伸 Horn-Johnson《Matrix Analysis》**：Strang 後進階；尤其 matrix inequality、perturbation theory 深化。
- **衝突：幾何直觀 vs 嚴格證明**：Strang 直觀優先，純數學家偏好 Axler；選擇依需求。
- **可挖金礦**：Ch7 SVD 的 low-rank 近似可直接整合進 ZP 的 covariance matrix shrinkage——對 500 股票的 sample covariance 做 truncated SVD (保留前 10 principal components) 對抗 noise 污染，顯著改善 out-of-sample portfolio performance。
