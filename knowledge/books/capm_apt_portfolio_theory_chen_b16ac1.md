## Investments Lecture 4: Portfolio Theory, CAPM and APT — Chyi-Mei Chen (國立臺灣大學財務金融系)
**來源**: NTU Finance lecture notes 2018 (65 pages)  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **Introduction to fund separation theorems**
- **Distribution-based two-fund separation**
- **Preference-based two-fund separation (Cass-Stiglitz)**
- **CAPM derivation from two-fund separation**
- **Equilibrium properties: β, market risk premium, SML**
- **APT: Ross 1976 arbitrage-free factor model**
- **CAPM vs APT: empirical comparison**
- **Extensions: Conditional CAPM, multi-beta CAPM**

### TL;DR
臺大財金系投資學第四堂課深度講義,嚴格從 fund separation theorems 推導 CAPM,再對比 APT 的 factor arbitrage 邏輯。核心訊息:CAPM 成立的前提條件極強(二基金分離),現實市場常違反,APT 是更 robust 的替代。

### 核心本質
1. **Fund separation = CAPM 的數學基石** — 當所有投資者的最佳組合都是少數「基金」(fixed portfolios) 的線性組合,其他市場可以關閉而不損失效率。Two-fund 分離 + 無風險資產 → 單一 market portfolio → β-定價 → CAPM。這是 CAPM 的前提而非結論。
2. **分離定理的兩條路徑:分佈 vs 偏好** — Distribution-based (Ross 1978):當報酬分佈屬特定族(橢圓分佈、常態);Preference-based (Cass-Stiglitz 1970):當效用函數屬 HARA (Hyperbolic Absolute Risk Aversion) 族。兩種限制都很強,現實常被違反。
3. **CAPM ≠ diversification argument** — 初階教科書把 CAPM 描述為「分散化去特有風險,系統性風險用 β 定價」,這是結果而非推導;嚴格推導需從 equilibrium + two-fund separation,跳過此步會遮蔽 CAPM 的前提強度。
4. **APT 放寬了 CAPM 的強前提** — APT 只要求「factor structure + no-arbitrage」,不需要均衡、不需要市場組合、不需要效用函數形式;代價是 factor 需外生給定,無「正確 factor」的理論指引,實務常 data-mining factors。
5. **Empirical anomalies 證 CAPM 結構性缺陷** — size effect (Banz 1981), value effect (Fama-French 1992), momentum (Jegadeesh-Titman 1993) 長期違反 CAPM;multi-factor model (FF3, FF5, Q-factor) 是對 CAPM 的實證替代方案。

### 可用戰術/策略
- **CAPM 校準 β 的穩健化**:rolling 60m regression + Dimson correction (adjacent lag beta) + shrinkage 到產業 β,避免個股 β 的雜訊。
- **APT factor 選擇**:優先使用已驗證的 factor (Fama-French 3/5, Carhart momentum, Q-factor, betting-against-beta),避免從零開始 data-mine factors。
- **CAPM breakdown 的戰術**:當 empirical anomalies 穩定 (size/value/momentum),可建 long-short factor portfolio 收 risk premium;本文邏輯支持這種 multi-factor approach。
- **市場組合的 proxy 挑選**:用全球 total market ETF (VT) 而非純美股 (SPY),更貼近 CAPM 理論的「全市場」概念;台股應用用 MSCI Taiwan 或 Taiex Total Return。

### 盲點 / 反例 / 適用邊界
- **CAPM 實證失敗的意義**:β 對 return 的解釋力在 US 股市長期 R² < 0.05;嚴格講 CAPM empirical 已死,但仍被當成 benchmark 使用是因教學傳統,非因準確性。
- **APT factor 數量與解釋力的 trade-off**:因子太少漏掉系統性風險,太多變 data-mining (Harvey 2016 的 factor zoo 批判);5-7 個 factor 是當前共識上限。
- **市場組合的不可觀察性 (Roll 1977 critique)**:真正的 market portfolio 包含人力資本、房地產、私募股權、債券,無法觀察;任何 proxy 都有 mis-specification 風險。
- **適用邊界**:大型流動股票市場;小型股、EM、crypto、illiquid 資產的 risk pricing 需用 consumption-based CAPM 或 Arbitrage Pricing 的延伸,非純 CAPM。

### 與 Edward 既有知識的連結
- 呼應 **derivative_over_level**:CAPM β 本身是 return 的 sensitivity 量度 = derivative of asset return w.r.t. market return;框架本身對齊第一公理。
- 銜接 **population_exploit**:CAPM empirical anomalies (size/value/momentum) 正是 population mispricing 的結構性證據,multi-factor portfolio 就是對 population 誤判的收割工具。
- 補強 **meta_strategy_over_strategy**:multi-factor portfolio 作為 meta-strategy = 「分散到多個 systematic risk premium」 > 單一策略;對應 Edward 的策略組合哲學。
- 對照 **Aronson evidence_based**:CAPM 廣泛採用但 empirically fail → 典型的「理論便利 vs 實證嚴謹」衝突;本講義批判性呈現 CAPM 限制,符合 evidence-based 原則。
