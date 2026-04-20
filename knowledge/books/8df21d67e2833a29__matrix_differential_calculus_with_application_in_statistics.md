## Matrix Differential Calculus with Application in Statistics and Econometrics — 未標示
**來源**: E:/書籍/Matrix Differential Calculus with Application in Statistics and Econometrics.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Basic properties of vectors and matrices**
  - Introduction
  - Sets
  - Matrices: addition and multiplication
  - ... (19 more sections)
- **Kronecker products, the vec operator and the Moore-Penrose inverse**
  - Introduction
  - The Kronecker product
  - Eigenvalues of a Kronecker product
  - ... (8 more sections)
- **Miscellaneous matrix results**
  - Introduction
  - The adjoint matrix
  - Proof of Theorem 1
  - ... (13 more sections)
- **Mathematical preliminaries**
  - Introduction
  - Interior points and accumulation points
  - Open and closed sets
  - ... (7 more sections)
- **Differentials and differentiability**
  - Introduction
  - Continuity
  - Differentiability and linear approximation
  - ... (15 more sections)
- **The second differential**
  - Introduction
  - Second-order partial derivatives
  - The Hessian matrix
  - ... (12 more sections)
- **Static optimization**
  - Introduction
  - Unconstrained optimization
  - The existence of absolute extrema
  - ... (15 more sections)
- **Some important differentials**
  - Introduction
  - Fundamental rules of differential calculus
  - The differential of a determinant
  - ... (11 more sections)
- **First-order differentials and Jacobian matrices**
  - Introduction
  - Classification
  - Bad notation
  - ... (13 more sections)
- **Second-order differentials and Hessian matrices**
  - Introduction
  - The Hessian matrix of a matrix function
  - Identification of Hessian matrices
  - ... (6 more sections)
- **Inequalities**
  - Introduction
  - The Cauchy-Schwarz inequality
  - Matrix analogues of the Cauchy-Schwarz inequality
  - ... (31 more sections)
- **Statistical preliminaries**
  - Introduction
  - The cumulative distribution function
  - The joint density function
  - ... (10 more sections)
- **The linear regression model**
  - Introduction
  - Affine minimum-trace unbiased estimation
  - The Gauss-Markov theorem
  - ... (18 more sections)
- **Further topics in the linear model**
  - Introduction
  - Best quadratic unbiased estimation of 2
  - The best quadratic and positive unbiased estimator of 2
  - ... (14 more sections)
- **Maximum likelihood estimation**
  - Introduction
  - The method of maximum likelihood (ML)
  - ML estimation of the multivariate normal distribution
  - ... (11 more sections)
- **Simultaneous equations**
  - Introduction
  - The simultaneous equations model
  - The identification problem
  - ... (9 more sections)
- **Topics in psychometrics**
  - Introduction
  - Population principal components
  - Optimality of principal components
  - ... (16 more sections)

### TL;DR (≤120字)
本書屬於 statistics evidence based 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **多次檢驗問題會偽造 alpha** — data mining 若不做 Bonferroni/BH 校正,幾乎任何「策略」都能在歷史上跑贏
2. **統計顯著 ≠ 經濟顯著** — t-stat 3.0 但年化超額 0.3% 在扣手續費後無法存活
3. **前瞻偏誤 (look-ahead bias) 在學術論文與商業回測都普遍** — 特別留意財報日、指數調整日的訊號重建

### 可用戰術/策略

- 採用 white's reality check / stepwise superior predictive ability 做多重檢驗修正
- 所有 backtest 引入交易成本、滑價、融資成本,再看 net Sharpe

### 盲點 / 反例 / 適用邊界

- 統計檢驗預設資料獨立,金融時序高度相關,block bootstrap / stationary bootstrap 才能貼近實際分布

### 與 Edward 既有知識的連結

- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
- 呼應零式原則 *derivative_over_level* — 關注變化率/拐點而非單期水準
