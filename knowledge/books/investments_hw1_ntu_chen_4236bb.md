## Investments Solutions to Homework 1 — Chyi-Mei Chen (NTU 財金)
**來源**: inv2018sh1.pdf NTU Finance HW solutions (15 pages)  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **Problem 1: Mean-Variance Optimization with short-sale constraints**
- **Problem 2: Two-fund separation verification**
- **Problem 3: Efficient frontier parametric solution**
- **Problem 4: CAPM β estimation & expected return**

### TL;DR
NTU 財金系投資學作業解答,含 4 題 mean-variance 最佳化,特別處理 short-sale 限制下的 KKT conditions、兩基金分離的數值驗證。教學價值在於把抽象 portfolio theory 落成具體計算。

### 核心本質
1. **Short-sale 限制使問題變 inequality-constrained QP** — 無限制版本是 closed-form Lagrangian,有限制後需 KKT 條件 + active set 求解;實務上多數機構受監管 short sale 限制,此框架更貼近真實約束。
2. **有效前緣在約束下的 piecewise-hyperbolic 結構** — 約束啟動/解除的 μ 區間不同,產生分段雙曲線;每個 segment 對應不同的 active constraint set。
3. **Tangency portfolio 在 short-sale 禁止時可能不存在** — 傳統 CAPM 有效前緣依賴可無限 leverage,禁 short 後 tangency portfolio 可能退化,需用 Lintner 模型或 capital allocation line 替代。
4. **β 估計的 OLS 標準誤是 underestimate** — 個股 return 的 heteroscedasticity + autocorrelation 使 Newey-West 修正必要;教科書 β 往往 over-precise。
5. **HW 解題方法論 = 先寫 Lagrangian / KKT,後代數值** — 避免看到數字直接算的常見錯誤,先 setup 正確結構再代入。

### 可用戰術/策略
- **KKT 求解習題化**:任何帶約束的投組問題先寫出 Lagrangian、KKT、active set,再求解;避免直接 grid search。
- **Newey-West β 校正**:用 lag=4-6 的 NW 標準誤估 β 的 t-statistic,更 conservative。
- **Active-set algorithm**:禁 short 的 MV optimizer 用 active-set method (CVXPY, scipy.optimize);大規模 portfolio 用 interior-point。
- **sensitivity analysis**:解完最佳組合後測 μ ± 10%、σ ± 10%、ρ ± 0.1 的組合重量變化,識別不穩定的 allocations。

### 盲點 / 反例 / 適用邊界
- **靜態兩期模型,忽略 rebalance 成本**:HW 題設無 transaction cost,實務多期問題需動態規劃 + 交易成本,答案會不同。
- **參數假設為確定 (μ, Σ 已知)**:estimation error 是實務最大問題,Jorion 1986, Michaud 1998 證明 naive MV 由 estimation error 導致極端權重,需用 Bayesian shrinkage / resampling。
- **教學用例,僅兩至三資產**:多資產 (N>50) 的數值性態不同,計算 Σ^(-1) 不穩定,需 Ledoit-Wolf shrinkage。
- **適用邊界**:教學、簡化版 portfolio construction;專業實務用 Black-Litterman、robust optimization、或 ML-driven allocation。

### 與 Edward 既有知識的連結
- 對照 **meta_strategy_over_strategy**:HW 示範的 MV 最佳化是 strategy 層面,真正 meta-strategy 要處理 parameter uncertainty(Bayesian)與 structural breaks。
- 呼應 **risk_control_four_layers**:position sizing 層面,MV 給出一階 framework;需疊加 VaR / ES / drawdown constraint 才完整。
- 補強 **entry_diversity_exit_convergence**:MV 的分散化邏輯是 entry diversity 的數學基礎;exit convergence 是 MV 未處理的領域。
- 連結 **information_asymmetry_action**:μ, Σ estimation 是所有人面對的同樣問題,edge 在於用 non-standard factor / alternative data 優化估計。
