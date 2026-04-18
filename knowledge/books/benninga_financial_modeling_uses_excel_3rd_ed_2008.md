## Financial Modeling (3rd Ed) — Simon Benninga
**來源**: E:/書籍/Benninga, Financial Modeling (Uses Excel), 3rd Ed. (2008).pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Part I: Corporate Finance Models**
  - Ch 1 Basic Financial Calculations (NPV, IRR, compounding, loan tables)
  - Ch 2 Cost of Capital (Gordon model, CAPM-based, WACC)
  - Ch 3 Financial Statement Modeling
  - Ch 4 Building a Financial Model: PPG Corporation
  - Ch 5 Bank Valuation
  - Ch 6-7 Financial Analysis of Leasing / Leveraged Leases
- **Part II: Portfolio Models**
  - Ch 8 Portfolio Models Intro
  - Ch 9 Efficient Portfolios (no short-sale restrictions)
  - Ch 10 Variance-Covariance Matrix
  - Ch 11 Estimating Betas & Security Market Line
  - Ch 12 Efficient Portfolios w/o Short Sales
  - Ch 13 Black-Litterman Approach
  - Ch 14 Event Studies
  - Ch 15 Value at Risk
- **Part III: Option-Pricing Models**
  - Ch 16 Intro to Options
  - Ch 17 Binomial Option-Pricing Model
  - Ch 18 Lognormal Distribution
  - Ch 19 Black-Scholes Model
  - Ch 20 Option Greeks
  - Ch 21 Portfolio Insurance
  - Ch 22-23 Monte Carlo for Option Pricing
  - Ch 24 Real Options
- **Part IV: Bonds**
  - Ch 25 Duration
  - Ch 26 Immunization Strategies
  - Ch 27 Term Structure Modeling
  - Ch 28 Default-Adjusted Expected Bond Returns
- **Part V: Technical Considerations** (Excel specifics)
  - Ch 29-35 (Random numbers, Data tables, Matrices, Gauss-Seidel, Excel functions, Hints)
- **Part VI: VBA Introduction** (Ch 36-41)
- **Appendices** (Excel Help excerpts, R1C1 reference style)

### TL;DR (≤120字)
MIT Press 出版的「用 Excel 學金融建模」:從 NPV/WACC 基礎到 Black-Litterman、portfolio insurance、MC 選擇權定價,每個章節配具體 .xls 範例 + VBA macro。強在把 quant finance 的抽象公式直接轉為可操作的試算表,是金融新手的橋樑書。

### 核心本質 (3-5 條, 每條 50-120字)
1. **公式 ≠ 模型,模型必須可計算、可驗證、可修改** — Benninga 全書主軸:把教科書公式 (如 BS、duration) 轉為 Excel 儲存格 = 把「知道」變成「會做」。抽象公式若不能在 spreadsheet 上產出與 analytic 一致的結果,等於沒真懂。這是每個 quant 必經的「動手」階段。
2. **Black-Litterman (Ch13) 是 Markowitz 的工程修正版** — 純 Markowitz 對 covariance 估計極敏感,常產出極端權重;Black-Litterman 引入「市場均衡先驗 + 投資人觀點」,以 Bayesian 更新得更穩健權重。這是實務 portfolio manager 日用工具。
3. **Monte Carlo (Ch22-23) 是 exotic option 定價的瑞士刀** — 當 option payoff 依賴路徑(Asian、Lookback、Barrier) 時解析解不存在;MC simulate 無數條路徑取均值即為定價。Benninga 用 Excel data table + VBA 實作,比用 Python 入門更直觀 — 初學者不被實作語法搞暈。
4. **Real options (Ch24) 是公司決策的「option thinking」** — 投資一個專案可視為一個 call (未來擴產選擇權) + 一個 put (退場選擇權);DCF 忽略 optionality 低估專案價值。這是策略思維(而非金融工具)的 application。
5. **Duration & Immunization (Ch25-26) = 對負債的 option 替代品** — 買對 duration 的 bond portfolio 可以免疫利率 parallel shock;Ch26 展示 matched cash-flow 與 duration immunization 兩種方法。是退休金、保險公司 liability-driven 投資的基石。

### 可用戰術/策略
- **NPV / IRR 作為任何投資決策(含自己的策略研發時間)的決策工具** — Ch1 NPV 公式可套用於評估「花 6 個月研發策略 A 的期望 IRR」;把研發時間成本和預期收益 discount 後比較,選擇高 NPV 的研發路徑。
- **VBA 自動化 = Excel + programming 的 gateway** — Ch36-41 VBA 教學是從 "Excel user" 到 "Excel developer" 的橋樑。B1 自營系統若有 rapid prototyping 需求,VBA 對於快速驗證公式、做 sanity check 仍是有效工具(雖 Python 更主流)。
- **Black-Litterman 實作為多策略 allocator** — 將「各策略的歷史 Sharpe」作為 market equilibrium prior,"目前 conviction level" 作為 view;weight = BL posterior。比純 equal-weight 或純歷史 Sharpe weight 更穩健。
- **Event study 框架** — Ch14 方法可用來驗證「新聞事件對市場報酬影響」,是 event-driven strategy 的統計基礎。abnormal return = actual - expected (用 market model 估);cumulative abnormal return 的顯著性檢定。
- **VaR 估計 + backtest** — Ch15 三種 VaR (historical、parametric、MC) 對比實作;B1 系統 risk module 可直接以 Benninga Excel template 為基礎 port 到 Python。

### 盲點 / 反例 / 適用邊界
- **Excel 是 prototype 工具,不是 production 工具** — 大資料、高頻、並行計算、版本控制、測試自動化都是 Excel 弱項;production 交易系統必須 Python/C++/Julia。此書位置是 "learning bridge" 而非 "end tool"。
- **2008 版本未涵蓋 2010+ 市場變化** — OIS discounting、negative rates、XVA、central clearing、machine learning 應用等都不在書中。需搭配 Hull 最新版與 López de Prado。
- **偏 corporate finance / static portfolio 視角** — 動態策略、市場微結構、HFT 等不涉及;量化交易 beyond vanilla portfolio management 需另補。
- **美股/美國會計準則為主** — GAAP vs IFRS 差異、台股財報解讀特徵(ROE 定義、負債比計算等) 需另學本地市場書籍。

### 與 Edward 既有知識的連結
- 補足 Wilmott FAQ + Hull 的理論;Benninga 提供「怎麼動手算」的實操路徑。三書組合形成 quant finance 入門完整階梯(理論 → 實作 → 應用)。
- 對應 `backtest_methodology`:Ch22-23 的 MC simulation 是 backtest 路徑生成的基礎;理解 MC 精度與 variance reduction 才能做可靠回測。
- 銜接 `risk_control_four_layers`:Ch15 VaR + Ch25-26 Duration immunization 提供「市場風險 + 利率風險」的 Excel 級量化工具,可直接 port 到 B1 risk module。
- 對 B1 自營交易系統的貢獻:Ch13 Black-Litterman 可成為「多策略資金分配」的 core algorithm;VBA template 作為 quick-and-dirty decision tool。
