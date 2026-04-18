## Probability and Measure, 3rd Edition — Patrick Billingsley
**來源**: E:/課程/[6] 機率論/Probability and Measure, 3ed, 1995, Patrick Billingsley.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Probability
- Ch2 Measure
- Ch3 Integration
- Ch4 Random Variables and Expected Values
- Ch5 Convergence of Distributions
- Ch6 Derivatives and Conditional Probability
- Ch7 Stochastic Processes（Kolmogorov existence, Wiener measure）
- Appendix Borel sets, Integration, Hilbert space, etc.

### TL;DR (≤120字)
Billingsley 是美國機率論的經典教材（自 1979 首版）——與 Durrett 並列博士入學必讀。特色：強調「機率+測度」兩條線並進，Ch3 積分章節極為扎實；Ch5 弱收斂章節（含 Prokhorov、Helly、tightness）是此書標誌性貢獻。Billingsley 另著《Convergence of Probability Measures》為此書 Ch5 的專著擴展，對 functional CLT（Donsker）處理最權威。

### 核心本質 (3-5 條)
1. **π-λ Theorem for Measure Uniqueness**（Ch2） — 若兩個機率測度在 π-system 上一致，且 λ-system 包含此 π-system，則二測度全等。實際意義：僅需在一部分事件上指定機率（如離散點），即可唯一擴展到整個 Borel σ-field。用於建構新機率空間時的 consistency check。
2. **Weak Convergence (vague convergence of distributions)**（Ch5） — μₙ ⇒ μ ⟺ ∫f dμₙ → ∫f dμ 對所有 bounded continuous f。非僅 pointwise CDF convergence！這是 CLT 的正確陳述——需要驗證所有 bounded continuous 測試函數；Portmanteau theorem 給出等價刻畫。
3. **Prokhorov Theorem: Tightness ⇔ Relative Compactness**（Ch5 擴展） — 機率測度族 {μₙ} 在弱收斂意義下相對緊 ⟺ tight（對任意 ε，存在緊集 K 使 μₙ(K^c)<ε）。這是證明 invariance principle (Donsker) 的關鍵——從 finite-dim convergence + tightness 得到過程收斂。
4. **Radon-Nikodym 機率版本**（Ch6） — 對機率測度 Q≪P，dQ/dP 是 likelihood ratio。Girsanov theorem、Bayes formula、importance sampling 皆為此定理特例。
5. **Kolmogorov Consistency Theorem**（Ch7） — 給定一致的 finite-dim distributions，存在唯一機率測度在 path space 上實現它們。這是 Brownian motion、Gaussian process、Markov chain 在無限維空間的合法性證明。

### 可用戰術/策略
- **Portmanteau Equivalence Check**：驗證弱收斂可從五個等價條件選擇最易驗證者——CDF pointwise (at continuity)、open sets liminf、bounded continuous、bounded uniformly continuous、closed sets limsup。
- **Tightness + Finite-Dim Convergence = Process Convergence**：證明離散 random walk 收斂到 BM 的方法——驗證 finite-dim marginal 收斂到 Gaussian + tightness (Kolmogorov moment criterion)。
- **Helly's Selection Theorem**：任何 distribution function 序列都有弱收斂子列到一個 sub-probability measure；用於量化 extreme value theory 中的極限分布存在性。
- **Etemadi's Inequality**：對獨立 Xᵢ 與 partial sum Sₙ，P(max_k |Sₖ| ≥ 3λ) ≤ 3 max_k P(|Sₖ|≥λ)。弱於 Doob 但不需 martingale 結構。
- **Skorohod Representation**：若 μₙ⇒μ 在可分度量空間，存在 random variables Xₙ→X a.s. with distribution μₙ→μ；將弱收斂 "lift" 為 a.s. 收斂，簡化證明。

### 盲點 / 反例 / 適用邊界
- **偏向歐美 probabilistic tradition** — 風格以 Kolmogorov-Doob 傳統為主；缺少法派（Meyer-Dellacherie）semimartingale 傳統。
- **Martingale 處理不深入**（Ch6 後半段 only） — 不如 Williams 或 Protter；若追求 martingale 深度需其他書。
- **缺少現代 topic** — rough paths, malliavin calculus, BSDE 皆未涵蓋。
- **1995 年版較舊** — 當代 machine learning / stochastic optimization 的機率應用無著墨。
- **符號傳統** — 用 Greek σ-field、Fraktur 寫法，部分讀者需要適應。

### 與 Edward 既有知識的連結
- **ZP 機率論完整參考**：與 Durrett 並列主推；兩書互補，Billingsley 偏 functional CLT，Durrett 偏 Markov / ergodic。
- **對應 Convergence of Probability Measures**：Billingsley 另著專書是本書 Ch5 的深化，二書配合即可完整掌握 Donsker invariance principle。
- **延伸 Karatzas-Shreve**：Ch7 Wiener measure 建構是 Karatzas-Shreve 的前置。
- **衝突：學習曲線 steep** — 比 Williams 更硬，比 Durrett 更古典；對初學者可能偏難。
- **可挖金礦**：Ch5 tightness 技巧可直接應用於 ZP 的 invariance principle 實證——測試歷史日頻數據標準化後是否收斂到 BM，作為 diffusion model 的 empirical validation。
