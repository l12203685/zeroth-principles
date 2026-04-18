## Options, Futures, and Other Derivatives (5th Ed) — John C. Hull
**來源**: E:/投資交易/交易學習資料庫/@交易/@選擇權/John C. Hull/Options Futures and Other Derivatives, 5th, by Hull J. C..pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **1 Introduction** (exchange/OTC, forward/futures/options)
- **2 Mechanics of Futures Markets** (margin, convergence, delivery)
- **3 Determination of Forward and Futures Prices** (cost-of-carry, stock index, currency, commodity)
- **4 Hedging Strategies using Futures** (basis risk, minimum variance, rolling)
- **5 Interest Rates** (zero curves, forward rates)
- **6 Forward and Futures on Fixed Income** (T-bond, Eurodollar, duration hedge)
- **7 Swaps** (IR, currency, comparative advantage)
- **8 Mechanics of Options Markets**
- **9 Properties of Stock Option Prices** (bounds, put-call parity, early exercise)
- **10 Trading Strategies involving Options** (bull/bear spreads, straddles, strangles)
- **11 Binomial Trees**
- **12 Wiener Processes and Itô's Lemma**
- **13 The Black-Scholes Model**
- **14 Options on Stock Indices, Currencies & Futures**
- **15 The Greek Letters**
- **16 Volatility Smiles**
- **17 Basic Numerical Procedures** (binomial, MC, FD)
- **18 Value at Risk**
- **19 Estimating Volatilities and Correlations** (GARCH, EWMA)
- **20 Credit Risk**
- **21 Credit Derivatives**
- **22 Exotic Options**
- **23 Weather, Energy, Insurance Derivatives**
- **24 More on Models and Numerical Procedures**
- **25 Martingales and Measures** (risk-neutral, change of numeraire)
- **26 Interest Rate Derivatives: Standard Market Models**
- **27 Interest Rate Derivatives: Models of Short Rate**
- **28 Interest Rate Derivatives: HJM and LMM**
- **29 Swaps Revisited**
- **30 Real Options**
- **31 Insurance, Weather, Energy Derivatives**
- **Appendices** (Cumulative normal table, 延伸閱讀)

### TL;DR (≤120字)
衍生品的聖經級教科書:從 forward/futures/options 機制,到 BS 模型推導、Greeks、隱含波動率 smile、numerical methods (binomial tree / MC / FD),再到 VaR、IR derivatives、exotic options。完整覆蓋 sell-side 量化 analyst 基本功,是每個 option trader 必讀的 baseline。

### 核心本質 (3-5 條, 每條 50-120字)
1. **Cost-of-carry 是一切衍生品的結構性定價骨幹** — Forward 價格 = Spot × e^((r-q)T);futures 價格用同公式但邊際調整 mark-to-market。所有 derivative 定價先過 no-arbitrage cost-of-carry,然後再疊加波動率/利率/信用等修正。
2. **Risk-neutral valuation = 測度變換的工程化 workflow** — 把物理世界的 μ 換成 r,使所有資產折現後成為 martingale;實務意義:pricing 只靠 r,alpha 估計問題被繞過。但交易決策 (alpha 實現) 必須回到物理測度,兩者不可混淆。
3. **Greeks 是 hedge ratio 家族,不是風險指標** — Delta 不是風險,它是「需要多少標的才能一階線性中和選擇權風險」的技術數字。Gamma 才是告訴你 Delta 會變多快(需要多頻繁 rebalance)。實務 P&L 來自 Theta vs (Gamma × realized-vol² / 2) 的競爭。
4. **Volatility smile = BS 假設失敗的市場提醒** — 若 BS 是正確的,每一行權價隱含波動率應相同(扁平 smile);實證上出現 smile/smirk = 市場已知價格尾部非 lognormal。此為跳躍模型、stochastic vol 模型存在的根基。
5. **VaR 是監管標準 + 風險管理心錨,不是預測工具** — Ch18 明示 VaR 假設正態回報,低估尾部;Hull 自己是反 VaR 的理論家。真正風險工具組合:VaR (看常態部分) + CVaR / Expected Shortfall + 情境分析 (看尾部)。

### 可用戰術/策略
- **Option 策略選擇地圖 (Ch10)** — 依據 volatility view + direction view 決定組合:看漲+低 vol → long call;看漲+高 vol → bull put spread;不確定方向+高 vol → long straddle/strangle。把 Ch10 矩陣落地為 B1 自營選擇權模組的策略 router。
- **Binomial tree + FD 作為快速 pricing prototype** — 新 exotic 策略先用 binomial (Ch11) 或 explicit FD (Ch17) 驗證 PnL,再推到解析/Monte Carlo;Python 中可以 <100 行實現 Cox-Ross-Rubinstein 作為 sanity check。
- **Delta hedging rule-of-thumb** — 實務上不做連續 rebalance (交易成本),採 band-based hedging:Delta 超過閾值才調整。Ch15 附 Gamma/Theta 分析可推算最優 band width (Wilmott-Schönbucher-Whalley)。
- **Put-call parity 作為套利 / 報價檢驗** — C - P = S - K·e^(-rT);檢查市場報價是否違反 parity,若有持續背離 = 隱含額外成本(借券成本、Dividend、稅),亦為策略 edge 來源。

### 盲點 / 反例 / 適用邊界
- **假設連續交易 + 無交易成本 + 無價格跳躍** — 實務上這些假設全部違反;BS 只是 first approximation。Cetin-Jarrow-Protter 2004、Merton jump-diffusion、Heston stochastic vol 都是對 Hull 基礎架構的修正。
- **對實務 trader 的行為、情緒、倉位大小管理涉及不深** — Hull 是 quant mathematician 不是 trader practitioner;McMillan、Natenberg 補這一塊。
- **Chinese/Asian 市場結構微差異** — 書中例題多以 CME/CBOT 為主,台灣期交所、香港 HKEX、中國大陸 50ETF 選擇權的 margin、交易時段、稅務與美國不同,直接套用須調整。
- **第 5 版為 2002 年版本,未含 2008 後 OIS discounting、clearing 強制、XVA (CVA/DVA/FVA)** — 需以 Hull 後續版本 (9th/10th/11th) 或 Gregory《Counterparty Credit Risk and CVA》補強後續 10 年制度性變化。

### 與 Edward 既有知識的連結
- 這是 B2 Phase 2 書籍消化的核心節點書:Hull 覆蓋了 Natenberg 的定價理論底層,是選擇權策略模組的參考手冊。
- 對應 `information_asymmetry_action`:implied vol smile 是市場共識 vs 自身觀點的差距 → 每一組 smile 參數可以生成「市場預期 vs 自身預期」的信號。
- 銜接 `meta_strategy_over_strategy`:Ch18 VaR 與 Ch19 GARCH 告訴你「怎麼估風險」而非「怎麼賺錢」— 是風險管理 meta-layer 的經典工具。
- 對 B1 自營交易系統的貢獻:若擴展到選擇權策略,Hull Ch10 是 strategy router 的 checklist;Ch15 Greeks 是持倉監控 dashboard;Ch17 是回測 pricing engine 選型。
