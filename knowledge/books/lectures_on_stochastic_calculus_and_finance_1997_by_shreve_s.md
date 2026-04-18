## Lectures on Stochastic Calculus and Finance — Steven E. Shreve
**來源**: E:/書籍/Lectures on Stochastic Calculus and Finance, 1997, by Shreve S..pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Ch 1** Introduction to Probability Theory
  - Binomial Asset Pricing Model
  - Finite Probability Spaces
  - Lebesgue Measure and Integral
  - General Probability Spaces
  - Independence (sets, σ-algebras, RVs, LLN, CLT)
- **Ch 2** Conditional Expectation (信息 σ-algebra、martingale)
- **Ch 3** Arbitrage Pricing (Binomial, General one-step APT, risk-neutral measure, self-financing)
- **Ch 4** American Options & Optimal Stopping
- **Ch 5** Random Walks & Brownian Motion
- **Ch 6** Stochastic Integrals & Itô's Formula
- **Ch 7** Black-Scholes PDE derivation
- **Ch 8** Girsanov's Theorem & Martingale Representation
- **Ch 9** Term Structure of Interest Rates (HJM framework)
- **Ch 10** Risk-Neutral Measure for Multi-factor Models
- **Ch 11** American Derivatives in Continuous Time
- **Ch 12** Topics in Asian, Barrier, Lookback Options

### TL;DR (≤120字)
CMU Shreve 教授 1996-97 年在 MMA 程式的 lecture notes 匯編(後擴為 Shreve 2004 書);從 binomial tree + Lebesgue integral 入門,一路通到 Girsanov + HJM。比 Shreve 2004 兩卷本更精簡但嚴謹,是 quant finance 入門與複習的最佳折衷。對有 probability 基礎的學生可以在 3-4 週內讀完。

### 核心本質 (3-5 條, 每條 50-120字)
1. **Binomial model = 連續模型的數學訓練輪** — Ch 1-4:Shreve 堅持從 binomial 出發教 martingale、risk-neutral、replication,因為離散模型直觀可視,所有概念先建立紮實直覺再推廣到 continuous。這順序是理解 derivatives pricing 的最佳路徑。
2. **Martingale 是理解 "無套利 = 無方向性 edge" 的數學語言** — Ch2-3:在適當 filtration 下,折現後的資產價格在 risk-neutral measure 下是 martingale (條件期望不變)。這是 FTAP 的核心陳述:定價問題 ↔ martingale measure 存在性問題。
3. **Itô's Formula 是 stochastic calculus 的 chain rule** — Ch6:df(X) = f'(X) dX + (1/2) f''(X) d⟨X⟩;連續版的 "second-order taylor expansion"。此公式是 BS derivation 的骨架,也是所有 stochastic control 的起點。
4. **Girsanov 定理 = P-measure 與 Q-measure 之間的橋樑** — Ch8:在 equivalent measure 下,drift 可被 shifted 而 quadratic variation 不變;這讓 "pricing 在 Q 下" 與 "risk management 在 P 下" 能在同一模型空間處理。實務意義:實世界預期報酬 μ 與無風險利率 r 的區別就是 market price of risk (σ × Sharpe ratio)。
5. **HJM 框架統一處理 interest rate 模型** — Ch9:用 forward rate curve 而非 short rate 建模,因 forward rate 是可觀察 + 可交易;drift 在 risk-neutral measure 下被 volatility structure 完全決定 (no arbitrage condition)。這使不同 short-rate 模型 (Vasicek、CIR、Hull-White) 統一為 HJM 的特殊 volatility structure。

### 可用戰術/策略
- **作為 quant 工程師的 "每季複習" 參考** — 比 Hull 深但比 Karatzas-Shreve 精簡;實務 quant 每 3-6 月瀏覽一次 Ch6-8 保持對 Itô、Girsanov 的熟悉度,防止概念遺忘。
- **Binomial tree 作為新模型的 sanity check** — 任何新定價公式先用 binomial tree 驗證;若分析解在 N → ∞ 時與 binomial tree 收斂,才相信分析解正確。這是 Shreve 書教學順序給的 professional habit。
- **HJM framework 實作為 interest rate models 的 meta-class** — B1 系統若擴充到固定收益,以 HJM 抽象為 forward curve + volatility structure,具體 Vasicek/Hull-White 作為 instance;代碼設計上更 modular 且易擴展。
- **Self-financing portfolio 作為回測 PnL 計算規範** — Ch3 明確定義:portfolio value = position × price - financing cost;B1 回測模組須嚴格遵守 self-financing 約束,否則 simulated PnL 會虛高(missing funding cost)。

### 盲點 / 反例 / 適用邊界
- **1997 年 lecture notes,仍然是 draft 形式** — 有 typos、notation 偶有不一致;更 polished 版本是 Shreve 2004《Stochastic Calculus for Finance I & II》兩卷。若是初讀,建議用 2004 版。
- **需 real analysis + measure theory 預備** — Lebesgue integral (Ch1.3)、σ-algebra (Ch1.5.2) 對沒修過 real analysis 的讀者難度大;先讀 Billingsley、Folland 或 Reitano (for quant) 補底子。
- **缺 numerical implementation (code)** — 純理論 + 證明;沒有 Python/Matlab code 範例。實作需配合 Modeling Derivatives in C++ 或 Jäckel《Monte Carlo Methods in Finance》。
- **未涵蓋 Lévy process / jump diffusion** — 僅處理連續樣本路徑模型;實證金融對 jump 的重要性在 2000 後才大幅被認識,需補 Cont-Tankov《Financial Modelling with Jump Processes》。

### 與 Edward 既有知識的連結
- 補足從 Reitano (math prereq) → Shreve (stochastic calc) → Shiryaev / Karatzas-Shreve (rigorous treatment) 的學習鏈;三書形成 quant finance 理論基礎三階梯。
- 對應零式第 1 條 `derivative_over_level`:全書主題即「變化率的數學」(Itô calculus);stock price 在變、volatility 在變、利率在變,分析這些 "變" 的結構是 pricing 的核心。
- 連結 `information_asymmetry_action`:Ch2 filtration (information σ-algebra) 數學化「信息的時間演化」;實務上每個交易員都有自己的 filtration,alpha 來自 "你的 filtration 比市場共識 filtration 多了某 bit"。
- 對 B1 自營交易系統的貢獻:若要自研定價引擎或複雜策略,Shreve 是 reference;Ch9 HJM 是 fixed-income strategy 擴展的必讀。
