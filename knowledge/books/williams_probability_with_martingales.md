## Probability with Martingales — David Williams
**來源**: E:/課程/[6] 機率論/Probability with Martingales, 1991, David Williams.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1-5 基礎（測度空間, π-λ theorem, σ-field, probability measure）
- Ch6 Expectation, Integration
- Ch7 An Easy Strong Law
- Ch8 Product Measure & Fubini
- Ch9 Independence
- Ch10 Conditional Expectation（基本性質、regular, tower law）
- Ch11 Martingales
- Ch12 Supermartingales & submartingales
- Ch13 Convergence theorem
- Ch14 Doob's L^p inequality, Doob's upcrossing
- Ch15 Optional stopping, optional sampling
- Ch16 UI martingales & Martingale convergence in L^1
- Ch17 Strong law of large numbers via martingale approach
- Ch18 Doob decomposition
- Ch19-A 附錄（Kolmogorov extension theorem, projection）

### TL;DR (≤120字)
Williams 的《Probability with Martingales》是劍橋大學本科/研究所入門教材——薄（251 頁）、直觀、清晰，但涵蓋所有必要工具：測度論基礎 + CLT + Strong LLN + Martingale theory。以 martingale 為主線貫穿機率論是此書最大特色。對 quant：比 Durrett 更聚焦 martingale 核心工具，讀完可直接接 Shreve。

### 核心本質 (3-5 條)
1. **Tower Law (Iterated Conditioning)**（Ch10） — 若 H ⊂ G ⊂ F，E[E[X|G]|H] = E[X|H]。這是 martingale 預測可摺疊性的核心——多步預測等價於單步預測。金融中，動態 hedging 的連續修正合理性來自於此。
2. **Martingale = Fair Game**（Ch11） — Xₙ 是 martingale ⟺ E[Xₙ₊₁|Fₙ]=Xₙ。條件期望等於當前值，意味對未來的最佳預測就是現在的值——這是風險中性定價「discounted price = martingale」的直接定義。
3. **Optional Stopping Theorem (OST)**（Ch15） — 對 martingale X 與 bounded stopping time τ，E[X_τ]=E[X₀]。關鍵條件：stopping time bounded 或 X uniformly integrable。實務：若無 UI 條件，「馬丁格爾停損策略」會失敗（Wald's identity 失敗）。
4. **Doob's Maximal Inequality**（Ch14） — 對非負 submartingale X，P(max_{k≤n} Xₖ ≥ λ) ≤ E[Xₙ]/λ。強化 Chebyshev，提供 running maximum 的尾機率上界。金融應用：pricing 與 hedge of barrier option、控制最大回撤。
5. **Martingale Convergence in L¹ needs UI**（Ch16） — L¹-bounded 不足保證 L¹-convergence，需要 uniform integrability。UI = 「尾部積分一致變小」；是 Ch 13 的弱收斂強化為 Ch16 的強收斂的橋樑。

### 可用戰術/策略
- **馬丁格爾構造 via Doob Decomposition**：任何 adapted Xₙ 可分解為 Mₙ（martingale 部分）+ Aₙ（predictable 部分）。量化 strategy 的 PnL 若 Aₙ=0 則為公平遊戲，否則 Aₙ 即系統性 alpha/slippage。
- **UI for Hedging Completeness**：在完整市場，hedging portfolio 的 discounted value 是 UI martingale；不完整市場中此性質失敗。
- **Doob's L^p Inequality**：對 non-negative submartingale，||max_{k≤n} Xₖ||_p ≤ (p/(p-1))·||Xₙ||_p (p>1)。用於控制 running maximum 的 L^p 範數。
- **Strong Law via Martingale**：Ch17 用 martingale 證明 Kolmogorov SLN，是比 Durrett 更簡潔的途徑；副產品：MC 估計一致性證明自動取得。
- **Kolmogorov Extension Theorem**（App） — 給定 consistent finite-dim distributions，存在 path space probability measure。這是 Wiener measure / 其他連續時間過程的建構基礎。

### 盲點 / 反例 / 適用邊界
- **只做離散時間** — 連續時間 martingale / BM / SDE 完全沒有；讀完需接 Karatzas-Shreve 或 Revuz-Yor。
- **1991 年出版略舊** — 當代 martingale theory 新發展（rough path, BSDE）未涵蓋。
- **薄而快** — 251 頁對於進階讀者是優點，但初學者可能不適應 Williams 的 dense 風格；習題不多但極 clever（如 "paradox of the bookmaker"）。
- **缺少金融案例** — Williams 用 Monty Hall, coupon collector, Polya urn 等經典問題，沒直接 option pricing 應用。
- **不討論 Markov process / Feller semigroup** — 需 Kallenberg 或 Ethier-Kurtz 補。

### 與 Edward 既有知識的連結
- **ZP 機率論入門推薦**：是 Baby Rudin + 測度論基礎後的首選機率教材；比 Durrett/Billingsley 更短更直觀。
- **對應 Shreve Vol II**：Williams 提供離散 martingale 直覺，Shreve Ch2-4 提供離散→連續橋接；二書配對完美。
- **延伸 Protter Stochastic Integration**：Williams 的 optional stopping 與 Doob decomposition 是 Protter 連續版的 prototype。
- **衝突：過度數學化**：對純策略執行者略嫌繁瑣；但對模型建構/回測分析是基本功。
- **可挖金礦**：Ch15 OST 可直接應用於「停損時機」的數學分析——若 PnL 是 martingale，任何 bounded stopping time 期望值=0，意味「機械規則停損不能改變期望值」——只能改變風險形狀。
