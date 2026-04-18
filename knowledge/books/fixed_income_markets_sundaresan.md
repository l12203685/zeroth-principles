## Fixed Income Markets and Their Derivatives, 3rd Edition — Suresh Sundaresan
**來源**: E:/書籍/Fixed income markets and_their derivatives, 3ed, 2009, by Sundaresan S..pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- PART 1 Institutions and Conventions
  - Ch1 Overview of Fixed Income Markets
  - Ch2 Price-Yield Conventions
  - Ch3 Federal Reserve (Central Bank) and Fixed Income Markets
  - Ch4 Organization and Transparency of Fixed Income Markets
  - Ch5 Financing Debt Securities: Repurchase (Repo) Agreements
  - Ch6 Auctions of Treasury Debt Securities
- PART 2 Analytics
  - Ch7 Bond Mathematics: DV01, Duration, and Convexity
  - Ch8 Yield Curve and the Term Structure
  - Ch9 Models of Yield Curve and the Term Structure
  - Ch10 Modeling Credit Risk and Corporate Debt Securities
- PART 3 Market Segments
  - Ch11 Mortgages, Federal Agencies, and Agency Debt
  - Ch12 Mortgage-Backed Securities
  - Ch13 Inflation-Linked Debt: TIPS
- PART 4 Fixed Income Derivatives
  - Ch14 Derivatives on Overnight Interest Rates
  - Ch15 Eurodollar Futures Contracts
  - Ch16 Interest-Rate Swaps
  - Ch17 Treasury Futures Contracts
  - Ch18 Credit Default Swaps
  - Ch19 Structured Credit Products: CDOs

### TL;DR (≤120字)
Sundaresan (Columbia) 教科書——從 institutional details（repo、auctions、settlement）到數學工具（DV01、duration、convexity、HJM term structure）到 instrument（MBS、TIPS、swap、CDO）完整覆蓋。Part 1 的 institutions 章節是多數 fixed income 書忽略的，但對實盤交易至關重要。

### 核心本質 (3-5 條)
1. **Fixed Income = Convention > Math**（本質，Part 1） — 債券市場的價格表達有 10+ 種 convention（actual/360, 30/360, semi-annual, continuous compounding, clean vs dirty price, running coupon vs settlement date accrued）。不懂 convention 的 quant 算出的 DV01 可能錯 10%。機構對 convention 的嚴謹超過數學複雜度。
2. **Duration ≠ Time to Maturity**（本質，Ch7） — Macaulay duration = 加權平均 cash flow 到期時間；modified duration = -1/P × dP/dy（對 yield 變化的敏感度）；dollar duration (DV01) = modified duration × P × 0.0001。三者常混淆；交易員用 DV01（絕對金額敏感度），PM 用 modified duration（相對%變化）。
3. **Repo 是 Fixed Income Market 的 Blood**（本質，Ch5） — 所有 leveraged fixed income trade 都靠 repo funding——買 bond 後 reverse-repo 出來借錢，再買更多。repo rate 與 Fed Funds 的 spread（repo specialness）是 alpha 來源。2008、2019、2020 repo market 動盪直接推動 Fed 干預。
4. **Yield Curve 的三因子結構**（本質，Ch8-9） — Level、Slope、Curvature 三個 principal components 解釋 95%+ 的利率曲線變化；duration-hedged portfolio 仍有 slope + curvature 暴露。Nelson-Siegel 與 Svensson 是實務常用參數化；HJM 與 LMM 是學術 standard。
5. **Credit Risk Modeling 的 Structural vs Reduced-Form 分裂**（本質，Ch10） — Structural（Merton model）把 default 當資產價值跌破負債的 option exercise；Reduced-Form（Jarrow-Turnbull、Duffie-Singleton）把 default 當外生 Poisson process。前者更有經濟直覺，後者更能 fit 市場 CDS spread。

### 可用戰術/策略
- **DV01-Neutral Barbell vs Bullet**：同 DV01 下 barbell（短+長）與 bullet（中期）策略對 slope / curvature 變化響應不同；長期看 convexity 使 barbell 略優，但 carry 低。
- **Curve Steepener / Flattener**：bet yield curve slope 變化。Steepener = long 短 + short 長（受益於 curve 變陡）；Flattener = 反向。適用於央行政策預期改變時。
- **Repo Specialness Trade**：新發行 on-the-run 債券常有 repo specialness（可用低 repo rate 融資）；買 on-the-run 同時 repo 出來，賺 specialness premium（5-50 bps/year）。
- **Swap-Treasury Spread**：swap rate vs treasury rate 的 spread 反映銀行信用與供需；spread 偏離歷史均值 >2σ 時 convergence trade，但有 basis risk。
- **CDS-Bond Basis Arbitrage**：理論上 CDS spread = bond yield - risk-free rate；實際 basis 可正可負（受供需、流動性、reg 影響）；基差 > 50 bps 時配對交易。

### 盲點 / 反例 / 適用邊界
- **2009 年出版，未涵蓋 post-GFC regulation** — Dodd-Frank、SEF mandate、UMR（margin rules）、LIBOR-SOFR transition 都改變了 IR derivatives landscape。書中大量假設已不適用。
- **LIBOR-SOFR 轉換未涉** — 2021-2023 全球 LIBOR 退場、SOFR 為新 benchmark；Eurodollar futures 2022 已改為 SOFR futures。書中 Eurodollar 章節需整體翻新。
- **Negative interest rates regime 不涵蓋** — 書中 pricing model 假設 rate ≥ 0；歐洲 2014-2022、日本長年負利率下，Black model for caps 失效、需 shifted lognormal 或 normal model。
- **ESG / Green Bond 未涵蓋** — 2015 後 green bond、sustainability-linked bond 崛起，占 fixed income 新發行 20%+；相關 pricing、liquidity、ratings 差異書中沒討論。
- **Structural credit model 的股權假設** — Merton 假設 lognormal asset value；實際公司資產 +/- jumps、deleveraging、bailout 常發生，單純 Merton 常 underestimate default probability。

### 與 Edward 既有知識的連結
- **ZP fixed income 基礎**：適合作為 `ZP/fixed_income/fundamentals/` 的主參考；特別是 Part 1 institutions 對台灣讀者陌生的美國 Treasury 市場機制。
- **對應 Brigo-Mercurio Interest Rate Models**：Sundaresan 偏 institutional + intuitive，Brigo-Mercurio 偏 advanced math；兩本讀完覆蓋 fixed income 完整。
- **衝突 Gibson Asset Allocation**：Gibson 把 bond 當 single asset class，Sundaresan 展示 bond 內部的 duration/credit/curve/carry 多維度 exposure；Edward 應避免把 bond 當 monolithic 資產。
- **可挖金礦**：Ch7 bond math 可 port 為 Python quantlib 範例；Ch14-17 derivatives 定價是 structured product 基礎，可作為自營交易擴展方向。
- **延伸應用**：若 Edward 未來投資台灣 government bond、public debt ETF，Ch2 convention、Ch7 duration 必需；TIPS (Ch13) 類比台灣通膨連結債券思維。
- **Crypto 類比**：DeFi 的 lending protocol（Aave、Compound）本質是演算法化 repo market；理解 Ch5 repo 機制有助於評估 DeFi 利率風險。
