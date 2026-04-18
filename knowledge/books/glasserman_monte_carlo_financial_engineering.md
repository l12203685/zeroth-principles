## Monte Carlo Methods in Financial Engineering — Paul Glasserman
**來源**: E:/課程/[11] 數值方法/Monte Carlo Methods in Financial Engineering, 2003, Paul Glasserman.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Foundations（LLN, CLT, variance, confidence intervals）
- Ch2 Generating Random Numbers and Random Variables
- Ch3 Generating Sample Paths（Brownian motion, geometric BM, square-root diffusion）
- Ch4 Variance Reduction Techniques（antithetic, control variates, stratified, importance sampling, Latin hypercube）
- Ch5 Quasi-Monte Carlo（low-discrepancy sequences: Halton, Sobol, Niederreiter）
- Ch6 Discretization Methods（Euler, Milstein, Richardson extrapolation）
- Ch7 Estimating Sensitivities（finite differences, pathwise, likelihood ratio / score function）
- Ch8 Pricing American Options（longstaff-schwartz regression, dual method）
- Ch9 Applications in Risk Management（VaR, ES, credit risk, large losses）

### TL;DR (≤120字)
Glasserman 的《Monte Carlo Methods in Financial Engineering》是 quant MC 的權威專著——Columbia MBA 計量金融教材，覆蓋 Brownian motion 模擬、variance reduction、Quasi-MC、discretization error、Greeks 計算、American option (LSM)、VaR simulation。Ch8 LSM algorithm 是所有 American option pricer 的基礎；Ch7 pathwise / likelihood ratio method 是 Greeks 計算工業標準。

### 核心本質 (3-5 條)
1. **Variance Reduction 可以把 MC 效能提升 10-1000 倍**（Ch4） — Antithetic (用 (Z, -Z) 對偶) 減少高維噪音；control variate (用已知解 Y 的 residual) 對 Asian option 可降 variance 到 1%；importance sampling 將 rare event (tail risk) 的採樣頻率提升。變異數縮減是 MC 成功的關鍵。
2. **Quasi-MC 的收斂率 O(N^{-1}(logN)^d)**（Ch5） — 對低維度 (d≤20)，Sobol / Niederreiter sequences 收斂率遠優於標準 MC 的 O(N^{-1/2})。但高維 (d>40) 會因 "curse of correlation" 失效；維度降階 (PCA, Brownian bridge) 是關鍵技巧。
3. **Euler vs Milstein Discretization Error**（Ch6） — Euler 有 weak order 1, strong order 0.5；Milstein 加上二階修正項得 strong order 1。對 SABR / CIR 等 non-Lipschitz SDE，Euler 可能 diverge；需 full truncation 或 log-Euler 處理。
4. **Longstaff-Schwartz Method for American Options**（Ch8） — 用 regression 估計 continuation value E[V_{t+1}|S_t]，在每個 exercise date 比較 intrinsic value 與 regressed continuation value；回歸 basis 常用多項式、Laguerre polynomials。是業界標配，但收斂到 true American price 有 bias。
5. **Pathwise vs Likelihood Ratio for Greeks**（Ch7） — Pathwise：對 S_T 可微 payoff (如 call)，∂E[g(S_T)]/∂S₀ = E[g'(S_T)·∂S_T/∂S₀]；適合 continuous payoff。Likelihood ratio：∂E[g(S_T)]/∂S₀ = E[g(S_T)·score]；適合 discontinuous payoff (digital)。兩法互補。

### 可用戰術/策略
- **Antithetic + Control Variate for European Option**：對 vanilla call，用 geometric-mean payoff 作為 CV（封閉解），可將 variance 降至 1% 級。
- **Stratified Sampling for Tail Events**：對 VaR 99%，用 stratified over Z > VaR threshold，保證每個採樣 scenario 都貢獻 tail estimate；variance 降低 5-10 倍。
- **Importance Sampling for Credit Portfolio**：大 portfolio 大損失事件少見，換測度 via exponential tilting 使 rare event 在新測度下成為典型事件；計算出結果後用 likelihood ratio 校正。
- **Brownian Bridge Construction**：對 path-dependent option，先 sample 末端 S_T，再 bridge 中間點；對 Asian option 的 stratification 可以在「均值」維度分層，而非 i.i.d. Z 維度。
- **Adjoint Algorithmic Differentiation (AAD)**：對 batch Greeks (Δ, Γ, ν for 1000 options)，AAD 將成本從 O(N·T) 降到 O(T)；業界 standard。

### 盲點 / 反例 / 適用邊界
- **2003 年版** — 缺少 rough volatility model、deep hedging (neural network MC)、GPU parallel MC；需期刊論文補。
- **Focus on 傳統 option** — exotic 多到 path-dep，不深入 structured product。
- **LSM 的 bias 問題未深究** — 實務中 regression basis 選擇影響 pricing，未有完整指南；Andersen-Broadie duality method 提供 upper bound。
- **Stochastic vol 處理淺** — Heston / SABR 模擬細節只輕觸；Andersen 的 QE scheme 2008 後才標準化。
- **缺少 Python 實作** — 偽碼為主，C++ 參考；當代實作多用 NumPy/JAX/QuantLib。

### 與 Edward 既有知識的連結
- **ZP Monte Carlo 核心**：`ZP/quant/monte_carlo/` 主推教材；所有 simulation-based pricer 的理論 + 實作參考。
- **對應 Press Numerical Recipes**：Press 通用算法，Glasserman 金融專用；Glasserman 優先用於 quant 任務。
- **延伸 Gatheral《Volatility Surface》**：Gatheral 與 Glasserman 同 Columbia，vol model 實務細節在 Gatheral 書中深化。
- **衝突：偏買方視角**：業界 sell-side 模擬技巧（exotic book marking, warehouse management）在此書不多；需 Kiesel-Glasserman 或 Hayes 補。
- **可挖金礦**：Ch7 likelihood ratio for Greeks 可整合進 ZP 的 delta hedging 核心——對任何 discontinuous payoff（digital, barrier）的 Greeks 計算，LR 方法優於 pathwise。
