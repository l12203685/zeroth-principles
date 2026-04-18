## Probability: Theory and Examples, 4th Edition — Richard Durrett
**來源**: E:/課程/[6] 機率論/Probability Theory and Examples, 4ed, 2013, Rick Durrett.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Measure Theory
- Ch2 Laws of Large Numbers
- Ch3 Central Limit Theorems
- Ch4 Random Walks
- Ch5 Martingales
- Ch6 Markov Chains
- Ch7 Ergodic Theorems
- Ch8 Brownian Motion
- Ch9 Multidimensional Brownian Motion（for those interested in PDE & SDE）

### TL;DR (≤120字)
Durrett 是美國機率論研究所最廣用教材——比 Williams 更完整，比 Kallenberg 更易讀，比 Billingsley 更現代。特色：每個定理配「example」與「exercise」形成三位一體的學習循環；第 4 版加入 Brownian motion（Ch8）變成從機率到隨機過程的完整框架。

### 核心本質 (3-5 條)
1. **Weak Law / Strong Law 的區別與適用**（Ch2） — WLLN 給依機率收斂（弱）；SLLN 給幾乎處處收斂（強）。兩者證明技術與需要條件不同——WLLN 只需有限變異數 (Chebyshev)，SLLN 需 E|X|<∞ (Kolmogorov) 或獨立 (Etemadi 弱化為 pairwise independent)。
2. **Lindeberg-Feller CLT**（Ch3） — 比傳統 Lévy CLT 更強：Xₙ,ₖ 三角陣列，若 Lindeberg condition (tail 貢獻 → 0) 成立，則 Sₙ=Σ Xₙ,ₖ 高斯化。金融 applied：高頻價格返利 (tick-level) 的求和極限分布。
3. **Markov Chain 的 stationary distribution 與 convergence rate**（Ch6） — 不可約 aperiodic MC 收斂到唯一 stationary distribution π；收斂速度由 spectral gap 決定。金融：MCMC 在 Bayesian pricing 的收斂診斷。
4. **Strong Markov Property**（Ch6, Ch8） — 對 BM，在 stopping time τ 後的過程 (Bₜ₊τ - B_τ)_{t≥0} 仍是 BM 且與 F_τ 獨立。這是 American option 透過 stopping problem 分析的核心。
5. **Ergodic Theorem**（Ch7） — 對 measure-preserving dynamical system，time average = space average (invariant measure)。金融回測中，若 price return 是 ergodic，單條路徑的長期均值收斂到 ensemble 均值；若非 ergodic，backtest 外推失敗。

### 可用戰術/策略
- **Lindeberg Test for High-Frequency CLT**：判斷 micro-return 是否高斯化——驗證 Lindeberg condition：max_k Var(Xₙ,ₖ)/Var(Sₙ) → 0；若 dominant jump 存在 (condition 失敗)，則返利分布保有 Lévy flight 性質。
- **Coupling for MC Convergence Rate**：coupling time τ 的 mixing time 提供 TV distance bound：d_TV(Pₙ, π) ≤ P(τ>n)；用於估計 MCMC chain 何時可採樣。
- **Stopped Brownian Motion**：對 τ=first hit of level L，B_τ 的分布有封閉形式（Ch8）；直接提供 barrier option pricing 的解析解。
- **Reflection Principle**：對 BM，P(max_{s≤t} Bₛ ≥ a) = 2P(Bₜ ≥ a)。這是 barrier option 與 running-max 計算的關鍵技巧。
- **SLLN in Backtest Diagnostic**：若回測 T 期的平均收益率 X̄_T 已收斂到穩定值（Cauchy criterion），可作為 SLLN 已生效的證據；若仍震盪，需增加樣本或質疑獨立性。

### 盲點 / 反例 / 適用邊界
- **Martingale 章節相對短**（Ch5） — 不如 Williams 或 Protter 深入；若需 martingale 高階技巧需補書。
- **Markov 處理偏離散** — 連續時間 Markov process 與 semigroup 只速寫；需 Ethier-Kurtz。
- **Brownian motion (Ch8) 基礎** — 不夠深入 stochastic calculus；SDE 走 Karatzas-Shreve 或 Shreve Vol II。
- **缺少 Lévy 過程** — 跳躍過程未涵蓋；需 Applebaum 或 Protter。
- **習題量大** — 超過 600 題，幾乎所有定理都有配套；建議選做每章 10-20 題。

### 與 Edward 既有知識的連結
- **ZP 機率論主推教材**：建議 Edward 選擇此書而非 Billingsley——更現代、例題多、可讀性好。
- **對應 Williams**：Williams 250 頁精簡，Durrett 500+ 頁完整；若時間緊選 Williams，若深度需求選 Durrett。
- **延伸 Shreve Vol II**：Durrett Ch8 BM 是 Shreve 第 3 章 BM 的更嚴格版本；先 Durrett 後 Shreve 無縫接軌。
- **衝突：輕 functional analysis** — 不深入 L^p 對偶、spectral theory；若需泛函分析配合需 Royden / Folland。
- **可挖金礦**：Ch7 ergodic theorem 可用於驗證 ZP 自營策略的回測假設——測試 time average 是否收斂，若不收斂須警惕策略在實盤無法 replicate。
