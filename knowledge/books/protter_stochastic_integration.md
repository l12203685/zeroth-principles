## Stochastic Integration and Differential Equations, 2nd Edition (v2.1) — Philip E. Protter
**來源**: E:/課程/[7] 隨機過程/Stochastic Integration and Differential Equations, 2ed, 2005, Philip E. Protter.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Preliminaries
- Ch2 Semimartingales and Stochastic Integrals
- Ch3 Semimartingales and Decomposable Processes
- Ch4 General Stochastic Integration and Local Martingales
- Ch5 Stochastic Differential Equations
- Ch6 Expansion of Filtrations

### TL;DR (≤120字)
Protter 是 semi-martingale 理論的權威教材——相比 Karatzas-Shreve 只處理 continuous case，Protter 完整處理 càdlàg semi-martingale（含 jumps）。特色：以 semi-martingale 為主線，從 Bichteler-Dellacherie theorem 出發嚴格構造 stochastic integral；Ch5 對 SDE 存在唯一（含 Lévy noise 版本）是所有跳躍金融模型的理論基石。

### 核心本質 (3-5 條)
1. **Semi-martingale = good integrator**（Ch2） — Bichteler-Dellacherie theorem：X 是 semi-martingale ⟺ integral mapping H → ∫HdX 對 bounded predictable H 有「nice」continuity（in probability）。等價：X = M + A（local martingale + finite variation process）。這是 Itô integral 最廣義的合法活動空間。
2. **General Itô Formula with Jumps**（Ch2） — 對 càdlàg semi-martingale X 與 C² function f：df(X) = f'(X⁻)dX + ½f''(X⁻)d[X,X]^c + Σ_{s≤t}[f(Xₛ)-f(Xₛ⁻) - f'(Xₛ⁻)ΔXₛ]。continuous + jump 兩個部分分開處理；連續部分是 Itô 標準形式，跳躍部分是 pointwise 修正。
3. **Doléans-Dade Exponential**（Ch2） — 對 semi-martingale X，stochastic exponential E(X) = 唯一解 dY = Y⁻dX。在連續 case，E(X) = exp(X - ½[X]_c)；帶跳躍 case，E(X) = exp(X_c - ½[X]_c)·Π_{s≤t}(1+ΔXₛ)exp(-ΔXₛ)。用於構造 change of measure、Girsanov extension。
4. **SDE with Jumps Existence & Uniqueness**（Ch5） — dX = μ(X⁻)dt + σ(X⁻)dW + ∫h(X⁻,z)Ñ(dt,dz)（Ñ 為 compensated Poisson random measure），在 Lipschitz 條件下有 path-wise 唯一強解。這是 Merton jump-diffusion、Kou double-exponential 的嚴格基礎。
5. **Expansion of Filtrations**（Ch6） — 在原 filtration F 上加入新資訊 G 得到 G ⊃ F；semi-martingale 在 F 下未必在 G 下保持 semi-martingale。實務：insider trading 模型，insider 有 future information 後原 semi-martingale 分解改變，drift 項出現。

### 可用戰術/策略
- **Quadratic Variation Decomposition**：[X]_T = [X]^c_T + Σ_{s≤T}(ΔXₛ)²；連續部分+跳躍部分分離；用於 realized variance 的跳躍修正（Barndorff-Nielsen bipower variation）。
- **Girsanov Extension with Jumps**：Q-change 中，除了 Brownian drift，跳躍強度與 mark 分布都可改變；對 pricing under model uncertainty 提供豐富的測度族。
- **Poisson Random Measure for Claims**：insurance / credit event 建模為 N(dt, dz)（時間 × mark 空間）；compensated Ñ 為 martingale，可做 stochastic integral。
- **Doléans-Dade for Credit-Loss Process**：L_t = ∫∫z Ñ(ds,dz)（加總 jump losses），其 Doléans-Dade exponential 可作為 relative density，構造 CDS pricing measure。
- **Jump-Diffusion Model Calibration**：擬合 S_t = S₀ exp((μ-½σ²-λκ)t + σW_t + Σ Y_i) (Y_i 為 jumps)，用 FFT option pricing 快速 calibrate (μ, σ, λ, 跳躍分布)。

### 盲點 / 反例 / 適用邊界
- **抽象度高** — 比 Karatzas-Shreve 還難，少人自學；建議先讀 Applebaum《Lévy Processes and Stochastic Calculus》的入門版。
- **缺少 numerical implementation** — 全是理論，jump-diffusion MC 需 Platen-Bruti-Liberati 或 Glasserman 補充。
- **現代 topic 不足** — rough path, BSDE, Malliavin 只輕觸；需專書。
- **2005 年版稍舊** — fractional / Lévy-driven 等近年發展需期刊論文補。
- **符號高度壓縮** — 對新手不友善；建議與 Jacod-Shiryaev《Limit Theorems for Stochastic Processes》交叉查閱。

### 與 Edward 既有知識的連結
- **ZP reference for jumps**：Edward 若做 crypto / commodity 交易（價格有大跳躍），Protter 是跳躍模型的理論核心。
- **對應 Karatzas-Shreve**：KS 是 continuous only，Protter 是 cadlag；二書互補構成 stochastic calculus 完整圖景。
- **延伸 Cont-Tankov**：Cont-Tankov《Financial Modelling with Jump Processes》是 Protter 的 applied 版。
- **衝突：純理論 vs 實務**：Edward 需要「理論夠用即可」，不必深入 Protter 每個角落；重點讀 Ch2 Itô 與 Ch5 SDE existence。
- **可挖金礦**：Ch6 filtration expansion 可直接對應「insider information / earnings leak」交易策略的數學模型——正式化「內線消息導致 drift 出現」。
