## Numerical Recipes: The Art of Scientific Computing, 3rd Edition — William H. Press, Saul A. Teukolsky, William T. Vetterling, Brian P. Flannery
**來源**: E:/課程/[11] 數值方法/Numerical Recipes The Art of Scientific Computing, 3ed, 2007, Press W.H. et al.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Preliminaries
- Ch2 Solution of Linear Algebraic Equations（LU, SVD, iterative methods）
- Ch3 Interpolation and Extrapolation
- Ch4 Integration of Functions（Gaussian quadrature, Monte Carlo）
- Ch5 Evaluation of Functions（Chebyshev, Padé, polynomial approximation）
- Ch6 Special Functions（Gamma, Bessel, elliptic, hypergeometric）
- Ch7 Random Numbers
- Ch8 Sorting and Selection
- Ch9 Root Finding and Nonlinear Sets of Equations
- Ch10 Minimization or Maximization of Functions
- Ch11 Eigensystems
- Ch12 Fast Fourier Transform
- Ch13 Fourier and Spectral Applications
- Ch14 Statistical Description of Data
- Ch15 Modeling of Data（Levenberg-Marquardt, Markov chain MC）
- Ch16 Classification and Inference
- Ch17 Integration of Ordinary Differential Equations
- Ch18 Two-Point Boundary Value Problems
- Ch19 Integral Equations and Inverse Theory
- Ch20 Partial Differential Equations
- Ch21 Computational Geometry
- Ch22 Less-Numerical Algorithms

### TL;DR (≤120字)
Numerical Recipes 是 scientific computing 的 cookbook bible——1986 初版至今 35 年，每章都是「概念 + 算法選擇 + C++/Python code」三合一。第 3 版使用 C++，涵蓋線性代數、ODE/PDE、FFT、統計、MC 全譜系。對 quant：實作 option pricer、calibration、backtest、risk engine 的算法參考；一本抵十本專書。

### 核心本質 (3-5 條)
1. **SVD 是最可靠的線性代數 tool**（Ch2） — A = UΣVᵀ 分解任何矩陣；處理 rank deficient、ill-conditioned 問題優於 LU 或 Cholesky。在最小二乘 Ax=b（m>n）中，x = V·Σ⁺·Uᵀ·b 給 minimum-norm 解；條件數 κ(A)=σ_max/σ_min 診斷數值穩定性。
2. **Gauss-Legendre Quadrature**（Ch4） — 對 ∫_{-1}^{1} f(x)dx ≈ Σwᵢf(xᵢ)（n 個節點精確到 2n-1 次多項式）；比 trapezoidal 收斂快 100 倍。金融應用：characteristic function integration (Carr-Madan)、PDE boundary integral。
3. **Mersenne Twister & Sobol Sequences**（Ch7） — 高品質 PRNG：period 2^{19937}-1；Sobol quasi-random 對低維 MC 收斂率 O(N^{-1}logⁿ N) vs 標準 MC 的 O(N^{-1/2})。金融：選擇權定價、portfolio VaR simulation 大幅加速。
4. **Levenberg-Marquardt for Nonlinear Fitting**（Ch15） — 結合 Gauss-Newton（二階）與 steepest descent（一階）；遠離最優時 steepest，接近時 Newton。是所有 option smile calibration（Heston, SABR）的主力算法。
5. **FFT O(N log N)**（Ch12） — Cooley-Tukey 算法將 DFT 從 O(N²) 降到 O(N log N)；直接應用：convolution、correlation、spectral analysis、Carr-Madan option pricing。實作細節：bit-reversal indexing、radix-2 vs radix-4、real-valued FFT 優化。

### 可用戰術/策略
- **Cholesky Decomposition for PD Matrix**：對 PSD covariance matrix Σ = LLᵀ；解 Σx=b 只需 O(n²) 而非 O(n³)。Monte Carlo simulation 中，correlated Gaussian 可由 L·z (z ~ N(0,I)) 生成。
- **Simpson's Rule with Richardson Extrapolation**：對 smooth integrand，Simpson 對 even 步數積分 + Richardson 改進到 4 階精度；比 Gauss-Legendre 簡單但略差。
- **Brent's Method for Root Finding**（Ch9） — 結合 bisection、secant、inverse quadratic；無需導數，保證收斂；在根附近超線性收斂。適合 implied volatility 計算。
- **Explicit Runge-Kutta 4**（Ch17） — 對 ODE dy/dx=f(x,y)，RK4 每步用 4 次 f evaluation 得 O(h⁵) 精度；穩定適中；SDE 的 Euler-Maruyama 是其弱化版。
- **Adaptive Step Size Control**：對 ODE/SDE，用兩個不同精度 RK step 估計 local error，動態調整步長；保持 error ≤ tolerance。

### 盲點 / 反例 / 適用邊界
- **算法選擇偏老** — 2007 年版，缺少當代 ML / deep learning numerical methods；不涵蓋 JAX、autodiff、GPU。
- **C++ code 學習曲線** — 第 3 版全 C++，Python 版需另找（port）；實作時往往改寫更方便。
- **Monte Carlo 章節太簡化** — 只有 basic variance reduction；Glasserman 的《Monte Carlo Methods in Financial Engineering》更全面。
- **PDE 章節老式**（Ch20） — 主要處理 explicit/implicit scheme；當代 finite element, spectral element 未涵蓋。
- **無 symbolic computation** — SymPy / Mathematica 層級不處理。

### 與 Edward 既有知識的連結
- **ZP 數值工具箱**：`ZP/numerical/` reference book；所有算法選擇時先查 Numerical Recipes。
- **對應 Glasserman**：Glasserman 專注金融 MC，Press 是通用 scientific computing；Glasserman 優先用於 quant 專門問題。
- **延伸 Golub-Van Loan《Matrix Computations》**：Press 的矩陣章節輕觸，Golub-Van Loan 是深度參考。
- **衝突：C++ code 不友善** — 當代 Python 生態（numpy, scipy）已封裝大多算法；Press 學習價值在於「背後發生什麼」而非直接用。
- **可挖金礦**：Ch15 Levenberg-Marquardt code 可直接 port 到 ZP 的 option calibrator；提供 explicit control 而非依賴 scipy.optimize.least_squares 黑盒。
