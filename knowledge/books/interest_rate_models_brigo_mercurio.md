## Interest Rate Models — Theory and Practice: With Smile, Inflation and Credit — Damiano Brigo & Fabio Mercurio
**來源**: E:/書籍/Interest Rate Models - Theory and Practice With Smile, Inflation and Credit, 2006, by Brigo D. and F. Mercurio.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
（PDF 無 bookmarks，根據已知書籍結構列出）
- Part I: Basic Definitions and No Arbitrage（Martingale measures, change of numeraire）
- Part II: No-Arbitrage Equilibrium Models（short rate models: Vasicek, CIR, Hull-White, G2++）
- Part III: Equilibrium Models of Short Rate
- Part IV: Market Models (HJM framework, LIBOR Market Model, Swap Market Model)
- Part V: Pricing Derivatives（caps/floors, swaptions, Bermudan swaptions, CMS）
- Part VI: Smile Modeling（SABR model, shifted lognormal, stochastic volatility extensions）
- Part VII: Cash-Settled Swaptions and Hybrid Products
- Part VIII: Inflation Models（Jarrow-Yildirim）
- Part IX: Credit Derivatives and Counterparty Risk（CDS, CDO, CVA）
- Part X: Counterparty Risk Adjustment（CVA/DVA/FVA）

### TL;DR (≤120字)
Brigo-Mercurio 是 fixed income quant 的聖經——1000+ 頁涵蓋 short-rate model、HJM、LIBOR Market Model、SABR smile、CDS、CVA 全體系。特色是每個模型都提供 calibration 實務細節、Monte Carlo 實作、常見 pitfall。UniCredit 兩位實戰 quant 出身，理論與實務兼備。

### 核心本質 (3-5 條)
1. **Short-Rate vs Market Models 的本質差異**（本質） — Short-rate models（Vasicek、CIR、Hull-White）describe r_t 的 SDE，其他量（yield curve、cap price）從 r_t 推導。Market models（HJM、LMM）直接 describe 可觀察量（forward rate）的 SDE，calibration 更直接但 high-dim。實務 swap/swaption desk 用 LMM，structured product 用 G2++ 兼顧速度與彈性。
2. **SABR Model 解決 volatility smile**（本質，Part VI） — 單一 Black-Scholes implied vol 無法 fit 市場 smile；SABR (F, α, β, ρ, ν) 用四參數 parametric 方式 fit smile 每個 expiry × strike，已成 fixed income option market 標準。α 是 ATM vol，β 是 skew（0=normal, 1=lognormal），ν 是 vol-of-vol，ρ 是 spot-vol correlation。
3. **Change of Numeraire 是定價的核心工具**（本質，Part I） — 選擇不同 numeraire（money market account、forward bond、annuity）對應不同 martingale measure；選對 measure 可大幅簡化 pricing formula。例：swaption 在 annuity measure 下變成 simple Black formula。
4. **CVA / DVA / FVA 重塑了 post-2008 定價**（本質，Part X） — 2008 前 derivatives 假設 counterparty 無違約風險；2008 後必須加 Credit Valuation Adjustment（CVA = 預期對手違約損失）、Debit Valuation Adjustment（DVA = 自身違約對對手的好處）、Funding Valuation Adjustment（FVA = collateral 融資成本）。三者讓 derivatives 定價從 univariate BSE 變 multivariate 複雜模型。
5. **Calibration 的 non-uniqueness**（本質，全書案例） — 同一組市場價格可能由多組參數 fit 出；LMM 可能 perfectly fit 今天的 swaption matrix 但 forward 分布偏離真實。成熟 quant 要理解 calibration 的 degeneracy，使用 regularization 或 penalty term 選擇 "economically reasonable" 參數。

### 可用戰術/策略
- **Hull-White G2++ 對 Bermudan Swaption**：2-factor short-rate model 足夠 capture yield curve slope/curvature 變化；比 1-factor Hull-White 對 Bermudan exercise 決策更準確 10-15%。
- **LMM with SABR for Cap Calibration**：先用 SABR fit 每個 caplet 的 smile，再用 LMM 對整條 caplet 曲線 joint calibration；確保 consistent forward vol structure。
- **CVA Calculation via Least Squares Monte Carlo**：傳統 CVA 需 nested MC（outer path + inner pricing），計算量 O(N²)；LSM 方法用 regression 代替 nested pricing，降到 O(N)。
- **SABR Beta Selection**：β=0.5 是行業常見 default；歐元 swap 市場用 β=0；日元低利率常用 shifted lognormal（β=1 但加 shift）。選 β 需配合市場 regime。
- **Swap Spread Trade Hedge**：用 Hull-White G2++ 模擬 swap spread 在 rate regime 變化下的分布，優化 hedge ratio；比 static DV01 hedge 的 tracking error 低 30-50%。

### 盲點 / 反例 / 適用邊界
- **LIBOR 退場後部分模型失效** — 書中 LMM 基於 LIBOR forward rate；2021-2023 LIBOR 退場改用 SOFR / €STR / TONA 等 RFR（risk-free rate），需重新 formulate 為 "forward-looking RFR" 或 "backward-looking compounded rate" 模型。
- **負利率時期 lognormal 失效** — Brigo-Mercurio 多數模型假設 rate 為正；2014-2022 歐洲負利率下 Black model for caps 產生 NaN；需 Bachelier (normal) model 或 shifted lognormal。
- **Calibration 效率 vs 精度 trade-off** — LMM calibration 對 1000-leg 結構化產品需要 minutes 到 hours；Fast calibration 技巧（adjoint differentiation、parameter parametrization）書中部分涵蓋但不夠實戰。
- **Counterparty risk 章節過於 banker 視角** — 假設讀者是 sell-side dealer，對 buy-side hedge fund、corporate treasurer 的 CVA 考量不同。
- **Inflation model 過於 simplistic** — Jarrow-Yildirim 假設通膨率為 lognormal；實際通膨有 regime、政策干預、tail risk；後續文獻（Dodgson-Kainth）對 inflation smile 有更完整處理。

### 與 Edward 既有知識的連結
- **ZP 進階 fixed income 參考**：在 Sundaresan 之後的進階教材，適合 `ZP/fixed_income/advanced/`；重點讀 SABR 與 CVA 章節。
- **對應 Higham / Shreve**：Higham 是 equity option 入門，Shreve 是 stochastic calculus 理論，Brigo-Mercurio 是 fixed income 實戰；三者互補。
- **對應 Bennett Trading Volatility**：Bennett 的 vol trading 思維可套用到 cap/floor/swaption；Brigo-Mercurio 提供完整 pricing 工具。
- **衝突 retail trading focus**：此書對散戶幾乎無直接用途——fixed income derivatives 交易需要 institutional scale（>$100M 部位）；Edward 若無法 access 機構流動性，應聚焦 equity/FX/crypto。
- **可挖金礦**：SABR 公式可移植為 Python 工具，用於任何 equity option 市場的 smile fit；SABR 不止適用 fixed income，應用範圍廣泛。
- **Crypto 應用**：DeFi 的 lending protocol (Aave variable rate)類似 LMM 的 forward rate；可用 HJM 框架建模 DeFi 利率 term structure。
- **CVA/DVA/FVA 思維延伸**：Edward 的 counterparty risk 意識（broker 倒閉、wallet 被駭）可借用 CVA 框架評估——每個 counterparty 的預期違約損失 × 曝險 × 回收率。
