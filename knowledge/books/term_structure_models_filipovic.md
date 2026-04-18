## Term-Structure Models: A Graduate Course — Damir Filipović (2009, Springer Finance)
**來源**: C:/Users/admin/staging/b2_batch_E_extracts/ab9470f60d3bd278__springer_finance_damir_filipovic_term_structure_models_a_gra.md  |  **消化日**: 2026-04-18  |  **模型**: claude-opus-4-7[1m] (main session)

### 目錄
- Ch1 Introduction（利率 term structure 的重要性、何需專門模型）
- Ch2 Interest Rates and Related Contracts（zero-coupon bonds、LIBOR、simple vs continuous compounding、forward/future rates、coupon bonds、swaps、yields、caps/floors、swaptions、market conventions）
- Ch3 Estimating the Yield Curve（Nelson-Siegel、Svensson 函數、bootstrap、spline smoothing）
- Ch4 Statistics of the Yield Curve（Litterman-Scheinkman 3 因子、PCA、term structure shape 分類）
- Ch5 Interest Rate Models Introduction
- Ch6 Short Rate Models（Vasicek、CIR、Hull-White）
- Ch7 HJM Framework（forward rate modeling、drift condition、Markovian HJM）
- Ch8 LIBOR Market Model（BGM/Jamshidian、caplet pricing、swaption pricing）
- Ch9 Affine Diffusion Processes（Filipović 獨有貢獻章節，涵蓋 affine TS models 理論與實作）
- Ch10 附錄：隨機微積分基礎、函數分析

### TL;DR (≤120字)
Filipović 把利率模型論述從 "stock model 的附錄" 升級為一完整 graduate 課程：核心貢獻是 Ch9 的 affine diffusion processes 統一框架，可涵蓋 Vasicek、CIR、Duffie-Kan 等所有熱門 short-rate 與 HJM 模型；對實務界尤其重要的是 curve-fitting 方法（Nelson-Siegel）與 factor model 之間的橋接章節，為 empirical calibration 給出清晰路徑。

### 核心本質 (3-5 條)
1. **Term Structure 本質是 Infinite-Dimensional**（本質） — Ch1 開宗明義：stock model 只需 scalar price process；term structure 是整條曲線 (T → 無窮多期限)，維度無限；此根本性差異使標準 Black-Scholes 框架不適用，需要 HJM 這類處理 stochastic PDE 的工具。這解釋了為何 interest rate 模型比 equity 模型複雜度高出一個量級。
2. **Three Factors 幾乎解釋 90% 曲線變動**（本質） — Ch4 Litterman-Scheinkman 實證：利率曲線動態主要由 level (平行移動)、slope (陡峭/平坦)、curvature (峰值凸性) 三個主成分驅動，各占約 80% / 10% / 5% 變異；意味實務 hedge 只要管 3 個 key rate bucket 即可，不需全曲線逐點對沖。
3. **Short Rate Model vs HJM vs LIBOR Market Model**（本質） — Ch6-8 三大模型家族：short rate 直接對 r(t) 建模（Vasicek 均值回歸 + CIR 非負性 + Hull-White 時間依賴 θ(t)）；HJM 對整條 forward curve f(t,T) 建模（drift 必須滿足 no-arb condition）；LMM 對離散 LIBOR forward rate 建模（bridging 市場慣例，caplet 與 swaption 直接可 price）。三者是「層級越高越貼近市場但計算越重」的 trade-off。
4. **Affine Processes 統一框架**（本質） — Ch9 Filipović 個人貢獻：所有 Vasicek、CIR、Duffie-Kan、Heston 等都是 affine processes 特例；characteristic function 有 closed-form exp(φ(u,τ) + ψ(u,τ)ᵀx)；這使 option pricing、bond pricing 都可透過 Fourier 轉換 O(1) 時間計算，避開 Monte Carlo。這是 2009 後 derivatives desk 的標準技術。
5. **Curve-Fitting 與 Factor Model 的衝突**（本質） — Ch4 提及：實務先用 Nelson-Siegel 把昨日市場 snapshot 擬合成平滑曲線（curve fitting），再在這曲線上跑 factor model 動態；但「perfect fit 今日市場」的模型明日會有較大誤差，而「factor model 保 no-arb」的模型今日市場有誤差；完美 fit 與 no-arb consistency 是不可兼得的 trade-off。

### 可用戰術/策略
- **Bootstrap Yield Curve 建構**：從短期 deposit rate + FRA + IRS → 解出 zero-coupon yield curve；每個 instrument 給一個 data point，線性/指數插值填補；這是固定收益 desk 每日 first step。
- **Nelson-Siegel 參數化 Yield Curve**：y(τ) = β₀ + β₁·f₁(τ;λ) + β₂·f₂(τ;λ) + β₃·f₃(τ;λ)；四個參數直觀對應 level/slope/curvature/附加 factor；實務用於 reporting 與 bond index 建構。
- **Vasicek 校正與使用**：dr = κ(θ - r)dt + σ·dW；用 MLE 或 OLS 從歷史 short rate 估 κ, θ, σ；封閉解 P(t,T) = A(t,T)·exp(-B(t,T)·r)；適合教學與初步 intuition，實戰限制：允許負利率 + 單 factor 不夠 flexible。
- **CIR 用於非負利率環境**：dr = κ(θ - r)dt + σ·√r·dW；強制 r ≥ 0（若 2κθ ≥ σ²）；比 Vasicek 更合理，但少了 closed-form swaption；實戰可當 Vasicek 的「非負 patch」。
- **Affine Factor Model Template**：選擇 state variable X 滿足 dX = μ(X)dt + σ(X)dW，其中 μ, σ·σᵀ 都是 X 的 affine 函數；此時 bond price P(t,T) = exp(A(τ) + B(τ)ᵀX)，用 Riccati ODE 解 A, B；封閉解適合 real-time pricing。

### 盲點 / 反例 / 適用邊界
- **過於技術，需先修 stochastic calculus** — Preface 承認讀者需熟 Itô calculus；一般 quant analyst 需先修 Shreve《Stochastic Calculus for Finance》再讀 Filipović。
- **LIBOR 已退場** — 2021-2024 LIBOR 完全退場，改用 SOFR/SONIA/ESTR 等 risk-free rate；雖然模型框架通用，但具體 LMM 章節需重寫 SOFR floating-rate conventions；讀者需搭配 post-2022 SOFR 文獻。
- **Negative Rate 處理不足** — Vasicek 允許負利率被長期批評；現代歐洲 / 日本經歷長期負利率環境，負利率成為常態；需要 shifted lognormal model 等修正。
- **Credit Risk 未深入** — 純 risk-free rate 模型，對 corporate bond、sovereign spread 建模需搭配 credit risk 模型（如 Lando《Credit Risk Modeling》）。
- **Machine Learning 在 rate modeling 的進展未涵蓋** — 2015+ 出現的 neural network yield curve fitting、LSTM forecast 等 ML 方法本書未提。

### 與 Edward 既有知識的連結
- **對齊 ZP 核心**：Term structure 的 3-factor 結構對應零式投資本質 — 表面複雜的多維系統往往由少數因子驅動；Edward 的永生樹管理也可用類似 PCA：找 3-5 個核心因子（時間、能量、context 深度）解釋 90% 的系統行為。
- **延伸既有 DNA**：Affine diffusion 框架可類比 Edward 的模型統一觀 — 不同 subagent / 不同 task 的行為如果都符合 affine structure，就可用一套 calibration 方法；尋找這種 unified structure 是研究的高價值方向。
- **衝突點**：本書偏重理論嚴謹，對實戰 desk 的 day-to-day operation 描述有限；實務 desk 使用的 "quick and dirty" 方法（Bloomberg screen lookups、market convention hacks）本書忽略。
- **可挖金礦**：Ch3 的 Nelson-Siegel 方法 + Ch9 的 affine framework 可組合建立 Edward 的 ZP fixed income 模組基石 — Nelson-Siegel 用於日常 curve fitting / visualization，affine model 用於衍生品 pricing；兩者互補即可應對 90% 利率相關需求。
