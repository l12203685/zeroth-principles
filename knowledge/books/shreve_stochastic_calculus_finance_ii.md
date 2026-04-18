## Stochastic Calculus for Finance II: Continuous-Time Models — Steven E. Shreve
**來源**: E:/課程/[9] 金融數學/Stochastic Calculus for Finance II - Continuous-Time Models, 2004, Shreve S.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 General Probability Theory（σ-algebras, probability spaces, conditional expectation）
- Ch2 Information and Conditioning
- Ch3 Brownian Motion
- Ch4 Stochastic Calculus（Itô integral, Itô-Doeblin formula, Black-Scholes-Merton PDE）
- Ch5 Risk-Neutral Pricing（Girsanov, martingale representation, completeness）
- Ch6 Connections with Partial Differential Equations（Feynman-Kac, stochastic representation）
- Ch7 Exotic Options（Asian, barrier, lookback）
- Ch8 American Derivatives（optimal stopping, Snell envelope, free-boundary PDE）
- Ch9 Change of Numéraire
- Ch10 Term Structure Models（HJM framework, short rate models）
- Ch11 Introduction to Jump Processes（Poisson, compound Poisson, jump-diffusion, Merton's model）

### TL;DR (≤120字)
Shreve Vol II 是金融工程的 gold standard—— CMU 計算金融碩士的核心教材，涵蓋連續時間金融數學完整體系。特色：理論嚴格度比 Hull 高、比 Karatzas-Shreve 低；每章都用具體金融問題驅動數學工具導出。讀完本書即可獨立處理 vanilla + exotic + American + term structure 全部主流衍生品定價。

### 核心本質 (3-5 條)
1. **Black-Scholes PDE via Hedging Argument**（Ch4） — 設 portfolio Π = V(t,S) - Δ·S，選 Δ=∂V/∂S 消除 dW 項，則 dΠ = r·Π·dt（risk-free）；推導出 BS PDE：∂ₜV + rS∂_SV + ½σ²S²∂_{SS}V - rV = 0。這是金融工程最重要的推導，直接展示「no-arb」如何生出 PDE。
2. **Risk-Neutral Measure Q 的存在與唯一**（Ch5） — Q 存在 ⟺ no-arbitrage (FTAP I)；Q 唯一 ⟺ market complete (FTAP II)。BS model 同時滿足；Heston SV model 中 Q 不唯一，需選擇 vol risk premium。
3. **Change of Numéraire**（Ch9） — 選不同 numeraire (money market, stock, bond, forward) 對應不同 pricing measure；合適選擇可大幅簡化計算。例：options on stock，選擇 stock 為 numeraire 則 S̃ = S/S = 1 恆定，pricing 變成 expectation under "stock measure"。
4. **Snell Envelope for American Options**（Ch8） — American option value V_t = sup_{τ≥t} E^Q[e^{-r(τ-t)}·g(S_τ)|F_t]；最優 stopping 問題。離散版為 backward induction max(payoff, continuation)；連續版產生 free-boundary PDE。
5. **HJM Framework**（Ch10） — 直接 model forward rate f(t,T) 的 SDE；no-arbitrage 給出 drift restriction：α(t,T) = σ(t,T)·∫ₜᵀ σ(t,s)ds。所有 short-rate 模型皆為 HJM 特例；LIBOR market model 從此衍生。

### 可用戰術/策略
- **Black-Scholes Delta-Gamma Hedging**：Δ = ∂V/∂S 消除 S 風險，Γ = ∂²V/∂S² 需 re-hedging；動態避險頻率越高，hedge error 越小（由 Itô's formula 表示為 ½Γσ²S²dt 的累積誤差）。
- **Monte Carlo Pricing under Q**：sample S_T ~ S₀·exp((r-½σ²)T + σ√T·Z)，payoff average × e^{-rT} 得 pricing；variance reduction 用 control variate (geometric average) 對 arithmetic Asian。
- **Fokker-Planck for Density**：若 dX = μ(X)dt + σ(X)dW，X_t 的密度 p(t,x) 滿足 ∂ₜp = -∂ₓ(μp) + ½∂_{xx}(σ²p)。用於計算 first passage time、barrier pricing 的密度。
- **Girsanov for Stochastic Volatility**：Heston 的 vol V_t 也需 Q 測度，但 vol 風險溢酬 λ 可選；option calibration 可視為選 λ 的最佳化。
- **PDE for Barrier / Lookback**：Ch7 的 barrier option 用 2D PDE（S, running min/max）；Ch8 American 的 free boundary 用 linear complementarity problem (LCP)。

### 盲點 / 反例 / 適用邊界
- **缺少 SABR / Vol Smile**（Ch11 只輕觸 Heston） — 當代選擇權市場用 SABR 是標準；需 Brigo-Mercurio 補足。
- **Credit risk 只簡述** — 結構模型 (Merton) 提及但 reduced-form、CDO、CVA 未深入；需 Bielecki-Rutkowski。
- **最佳化（portfolio selection）只到 Merton**（沒 continuous time 深入） — 需 Karatzas-Shreve《Methods of Mathematical Finance》。
- **HFT / market microstructure 未涵蓋** — Shreve 2004 出版時 HFT 未興起；需其他書（Hasbrouck 或 Cont）。
- **模型校正（calibration）沒實作細節** — 理論完美但數值技巧較少；需 Gatheral 或 Cont 補。

### 與 Edward 既有知識的連結
- **ZP 金融數學核心**：`ZP/quant/finance_math/` 主推教材；Shreve 對 Edward 的「從理論到自營系統」路徑最關鍵。
- **對應 Hull Options**：Hull 是 MBA 視角，Shreve 是理工科視角；二書互補——Hull 看寬度，Shreve 看深度。
- **延伸 Karatzas-Shreve**：Shreve Vol II 是 KS 的 applied 版；二書配合先讀 Shreve 再 KS 為最佳節奏。
- **衝突：缺少 Python code**：全是數學，需配 Hilpisch《Derivatives Analytics with Python》實作。
- **可挖金礦**：Ch9 change of numeraire 可作為 ZP 自營系統 pricing engine 的標準化介面——所有 derivatives 計算統一用「選 numeraire + expectation」格式。
