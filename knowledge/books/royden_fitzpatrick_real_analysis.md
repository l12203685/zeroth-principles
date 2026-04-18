## Real Analysis, 4th Edition — H. L. Royden & P. M. Fitzpatrick
**來源**: E:/課程/[1] 數學分析/Real Analysis, 4ed, 2010, Royden H. L. and P. M. Fitzpatrick.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Part I Lebesgue Integration for Functions of a Single Variable
  - Ch1 The Real Numbers: Sets, Sequences, and Functions
  - Ch2 Lebesgue Measure
  - Ch3 Lebesgue Measurable Functions
  - Ch4 Lebesgue Integration
  - Ch5 Lebesgue Integration: Further Topics
  - Ch6 Differentiation and Integration
  - Ch7 The Lᵖ Spaces
- Part II Abstract Spaces: Metric, Topological, Banach, and Hilbert
  - Ch8-10 Metric Spaces, Topological Spaces
  - Ch11-12 Normed / Banach Spaces / Hilbert Spaces
- Part III Measure and Integration: General Theory
  - Ch17-20 General measure, Lebesgue-Stieltjes, Hausdorff, Fubini
- Part IV Topics in Measure Theory and Modern Analysis
  - Ch22 Invariant Measures
  - Ch23 Measures on Locally Compact Topological Groups
  - Ch24 Mappings Between Measure Spaces

### TL;DR (≤120字)
Royden-Fitzpatrick 是美國最流行的 qualifier 教材之一，風格介於 Rudin 與 Folland 之間：嚴謹但有充足例子。第 4 版由 Fitzpatrick 大幅改寫，教學更清晰。Part I 從 ℝ 上 Lebesgue 入門，Part II 抽象化到泛函分析，Part III 回歸一般測度論。對 quant：提供所有 Shreve 前置知識。

### 核心本質 (3-5 條)
1. **Lebesgue 測度的完整構造**（Ch2） — 從 outer measure → 可測集 → 測度 的標準 4 步建構，清晰展示為何 Lebesgue 測度推廣 Jordan 測度、並包含所有 Borel 集。此構造是 P(Ω)（機率測度）的 prototype。
2. **Lebesgue 可積 ⟺ |f| 可積**（Ch4） — 與 Riemann 的重要差別：Lebesgue 只需「絕對可積」。對條件收斂的 Riemann 積分（如 ∫sin(x)/x dx），Lebesgue 版本需要特殊處理。金融中，當 payoff 無上界時必須注意此點。
3. **Vitali Covering & Lebesgue Differentiation**（Ch6） — F(x) = ∫₀^x f(t)dt 的可微性 + F'(x)=f(x) a.e.——當且僅當 f 可積時成立。這是 FTOC 的 Lebesgue 版，對 American option 的 free boundary 分析至關重要。
4. **Lᵖ 空間的完整性與可分性**（Ch7） — Lᵖ (1≤p<∞) 對 Lᵖ-norm 完備且可分（有可數稠密集）；Lᵖ 對偶 (Lᵖ)* = Lᑫ (q=p/(p-1))；對偶作用於 quant 的 hedging duality、robust pricing。
5. **Riesz Representation Theorem for C(K)** (Ch21) — 緊 Hausdorff 空間上的正線性泛函必由測度表示。這是金融中「no-arbitrage 等價於 pricing 線性泛函」的嚴謹來源——第一 FTAP 背後的數學。

### 可用戰術/策略
- **Lebesgue 可積性測試**：驗證 payoff X 在 (Ω, F, P) 下 E|X|<∞；若 X=max(S_T-K, 0) 且 S_T=S₀exp((r-½σ²)T+σ√T·Z) (Z~N(0,1))，E|X|<∞ ⟺ E|S_T|<∞ ⟺ σ² < ∞。
- **Vitali + Lebesgue Differentiation Applied**：對 call option value C(S,t)，C_S = ∂C/∂S 幾乎處處存在；實務中用於構造 delta-hedge portfolio 的嚴格基礎。
- **Lᵖ 空間的應用選擇**：pricing 常用 L²（Hilbert 結構好）；robust hedging 用 L¹（對偶 L^∞ 對應 essential supremum）。依問題選空間。
- **Fubini for Path Integral Decomposition**：對 ∫₀ᵀ E[f(S_t)]dt = E[∫₀ᵀ f(S_t)dt]，需驗證 Fubini 條件再交換；否則會得到錯誤結果。
- **Lusin + Egorov for Approximation**：可測函數可被連續函數 L¹-approximate（Lusin）；a.s. 收斂可近似為均勻收斂（Egorov）。實用於證明 MC 估計之 regularity。

### 盲點 / 反例 / 適用邊界
- **缺少複分析** — 不含 Cauchy theorem / residues / Hardy spaces；若需 quant 複分析需配 Ahlfors。
- **機率論章節極少** — 只有 Lebesgue 理論無 CLT / martingale / Markov chain；需 Durrett / Williams 補足。
- **Ch22-24 少人讀** — Haar measure / group representation 對金融無直接用途；多數讀者可跳過。
- **習題量大** — 約 1000+ 題，全解完不可能；需選擇性（每章至少 10 題核心題）。
- **抽象化慢** — Part I 用 500 頁才把 Lebesgue 理論講完，讀者若趕時間可考慮 Folland 或直接 Royden 簡化版。

### 與 Edward 既有知識的連結
- **ZP 測度論 qualifier 教材**：美國 PhD 常用；若 Edward 考慮申請 PhD 路線可選此。否則 Folland 更簡潔。
- **對應 Durrett PTE**：Royden 提供測度基礎，Durrett 提供機率論核心；二者結合是 Shreve 的完整前置。
- **延伸 Protter Stochastic Integration**：Protter 假設讀者有完整測度論背景，Royden 第 7 章 Lᵖ 空間剛好銜接。
- **衝突：教材過厚** — 683 頁，在時間有限的 Edward 學習節奏下非最優；可選 Folland 的 450 頁替代。
- **可挖金礦**：Ch6 Lebesgue differentiation 可用來分析 path-dependent option (如 Asian, barrier) 的價格函數 regularity；對數值穩定性分析有直接價值。
