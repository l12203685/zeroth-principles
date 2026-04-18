## Continuous Martingales and Brownian Motion, 3rd Edition — Daniel Revuz & Marc Yor
**來源**: E:/課程/[7] 隨機過程/Continuous Martingales and Brownian Motion, 3ed, 1999, Revuz D. and M. Yor.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch0 Preliminaries
- Ch1 Introduction (Wiener measure, construction of Brownian motion)
- Ch2 Martingales
- Ch3 Markov Processes
- Ch4 Stochastic Integration
- Ch5 Representation of Martingales
- Ch6 Local Times
- Ch7 Generators and Time Reversal
- Ch8 Girsanov's Theorem and First Applications
- Ch9 Stochastic Differential Equations
- Ch10 Additive Functionals of Brownian Motion
- Ch11 Bessel Processes and Ray-Knight Theorems
- Ch12 Limit Theorems in Distribution
- Ch13 An Introduction to Malliavin Calculus（附錄）

### TL;DR (≤120字)
Revuz-Yor 是連續 martingale 與 Brownian motion 的 French encyclopedia——專注連續 case 但深度無出其右。Marc Yor 是 Paris School 的核心，Bessel processes、Ray-Knight theorems、path decompositions 皆為其獨特貢獻。對 quant finance：Ch11 Bessel process 直接對應 Heston CIR vol，Ch10 additive functionals 對 Asian option 密度計算有絕對優勢。

### 核心本質 (3-5 條)
1. **Dambis-Dubins-Schwarz Theorem**（Ch5） — 任何連續 local martingale M 可表示為 M_t = B_{[M]_t}（B 為 BM）。這是「Brownian motion 是所有連續 martingale 的模板」的嚴格表述；提供了時間變化技巧，將複雜的 local martingale 化為 BM 問題。
2. **Local Time L_t^a**（Ch6） — BM 在位準 a 停留時間的極限密度；滿足 Tanaka's formula：|B_t - a| = |B_0-a| + ∫sign(Bₛ-a)dBₛ + L_t^a。用於 barrier option 的 high-touch 計算、reflected BM 刻畫。
3. **Girsanov 在 BM 上的完整處理**（Ch8） — Novikov / Kazamaki 條件保證 Doléans-Dade exponential 是 martingale；當條件失敗時 exp 只是 local martingale。實務：Heston / SABR calibration 中 measure change 可能違反 Novikov，需特殊處理。
4. **Bessel Processes BES(δ)**（Ch11） — 多維 BM 的 radius ||B_t|| 滿足 Bessel SDE：dR = ((δ-1)/2R)dt + dW；其中 δ 為 dim。δ=2 對應 2D BM，δ=0 對應 critical Bessel。CIR model dV = κ(θ-V)dt + σ√V dW 經時間變換等價於 squared Bessel——是 Heston 模型為何 tractable 的數學原因。
5. **Ray-Knight Theorems for Local Times**（Ch11） — BM 在 unit 時間的 local time field (a → L_1^a) 的分布可由 Bessel process 表示。非直觀應用：雙向 occupation density 計算，Asian option 密度推導。

### 可用戰術/策略
- **Time-Change Representation**：對任何連續 martingale，計算 [M]_t 並用 DDS 轉成 BM 問題；常大幅簡化複雜計算。
- **Tanaka's Formula for Running Min/Max**：對 lookback option，running max M_t = max_{s≤t} Bₛ 與 Ba 之差可用 local time 表示；提供 lookback pricing 封閉解。
- **Bessel Process for CIR Vol**：Heston vol V_t 時間變換 V_{t(u)} = W²_u/4 (W 為 BM)；用此將 Heston density 計算化為 Bessel density。
- **Ornstein-Uhlenbeck via Time-Change**：OU process dX = -κX dt + σdW 等價於 σ·e^{-κt}·B_{(e^{2κt}-1)/(2κ)}（scaled time-changed BM）。用於 mean-reverting spread pricing。
- **Malliavin Calculus for Greeks**（Ch13） — 將 ∂E[f(X_T)]/∂X₀ 表為 E[f(X_T)·π] 形式（π 為 weight），避免 path-by-path finite difference；對 discontinuous payoff 的 delta 計算尤其有效。

### 盲點 / 反例 / 適用邊界
- **只做連續** — 跳躍過程需 Protter、Jacod-Shiryaev 補。
- **法派風格抽象** — 相比美國風格（Karatzas-Shreve）更抽象、更數學；需讀者有較強數學素養。
- **缺少金融案例** — 雖含 option pricing 的理論工具，但沒有具體金融建模；需與 Shreve Vol II 同步讀。
- **部分章節（Ch10-12）冷門** — additive functionals、Bessel processes 對一般 quant 非必要；只對 exotic pricing 研究者重要。
- **1999 年版** — 缺乏 rough path、BSDE 等現代 topic。

### 與 Edward 既有知識的連結
- **ZP 進階 reference**：建議作為「深度 quant research」時查閱；非循序通讀教材。
- **對應 Karatzas-Shreve**：KS 是英美主流、Revuz-Yor 是法派；並行讀可獲得不同視角。
- **延伸 Protter**：Protter 延伸到 jumps，Revuz-Yor 深入 continuous path 細節。
- **衝突：學習成本巨大**：686 頁法派風格；Edward 除非做 pure math PhD 否則不必全讀。
- **可挖金礦**：Ch11 Bessel process 與 Heston 的對應可作為 `ZP/quant/stochastic_vol/heston/` 模組的理論文件，解釋為何 Heston 可 calibrate 且 tractable——Bessel 結構提供封閉解工具。
