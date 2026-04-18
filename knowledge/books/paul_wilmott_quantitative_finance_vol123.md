## Paul Wilmott on Quantitative Finance (3-Volume Set, 2nd ed) — Paul Wilmott (2006)
**來源**: E:/書籍/Quant/4d3cda2b71deaa3b__paul_wilmott_quantitative_finance_vol_1_3_2nd_ed.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Volume 1 Mathematical and Financial Foundations**
  - 第 1-11 部分 / 25 章 — Black-Scholes、Greeks、American option、binomial、PDE 數值法
- **Volume 2 Exotic Contracts and Path Dependency**
  - 第 12-17 部分 / ~27 章 — Exotic options、barrier、asian、lookback、compound、cliquet、forward-start
- **Volume 3 Advanced Topics**
  - 第 18-22 部分 / ~22 章 — 利率衍生品 (HJM、BGM/LMM)、信用衍生品、非 Black-Scholes 模型、boundary exotic、數值方法
- **Appendix** — 數學速查 / 機率 / 微分方程 / 程式實作
- **CD-ROM** — VBA/Excel spreadsheets 實作所有模型

### TL;DR (≤120字)
Wilmott 三卷 1500 頁,定位為從 Black-Scholes 到 exotic + rates + credit 的全方位 quant 手冊。風格:嚴謹但口語化,動手寫 VBA + PDE 求解器。最核心貢獻 — 堅持「模型是地圖」,每個定價模型配「何時此模型會失效」討論。與 Hull (教科書) 和 Shreve (數學) 不同,Wilmott 是「實務者寫給實務者」的百科,強調直覺、代碼、反例,比兩者更接近 trading desk 思維。Vol 3 的 HJM/BGM 和信用衍生品章節在 2008 後尤其有價值。

### 核心本質 (3-5 條, 每條 50-120字)
1. **直覺+代碼+反例三位一體 (全書風格)** — Wilmott 寫法不同於 Shreve (純數學) 或 Hull (教科書):每個模型先給直覺 (why), 再給公式 (how), 最後給 VBA 代碼 (do) 和反例 (breakage)。讀者可以真的實作並測試。這是 B1 自營系統開發的最佳參考風格。
2. **Vol 1 Ch.3-7 Black-Scholes 的 12 種推導** — 從 delta hedge 到 martingale 轉換到 EDP 到 binomial 再到 Monte Carlo,每種角度揭示不同直覺。例:用 PDE 法看,BS 方程是一個擴散 PDE + boundary condition;用 martingale 看,是 risk-neutral expectation。交易員須能在腦中切換這些角度才能真正理解 Greeks 的來源。
3. **Exotic options 的路徑依賴分類 (Vol 2)** — Barrier (KI/KO)、Asian (path average)、Lookback (path extremum)、Cliquet (path segments) 四類構成絕大多數場外衍生品。每類給出定價方法 (PDE、closed-form 特殊情況、Monte Carlo) 和套利關係 (In-Out parity, Lookback ≡ BS + correction)。
4. **Vol 3 Ch.18-20 Interest Rate Models** — 從 Short Rate (Vasicek, CIR) 到 HJM (forward rate curve) 到 BGM/LMM (LIBOR-based tradable)。LMM 是 2000 年代利率期權市場主流定價工具,2008 後因 LIBOR-OIS basis 擴大、collateral 折現引入 CSA 複雜化。Wilmott 對 LIBOR 轉 SOFR 未覆蓋 (2006 版),需配 Rebonato 後期作品。
5. **非 Black-Scholes 模型 (Vol 3 Ch.19)** — Heston stochastic volatility、SABR、Jump-diffusion (Merton, Kou)、Local Vol (Dupire)、Variance Gamma、CGMY。Wilmott 強調:真實市場 smile 需這些模型,但校準+穩定性是日常苦痛。對 Edward:實盤 volatility trading 不能單用 BS,必須有至少一個 smile-aware 模型。

### 可用戰術/策略
- **Greek book 全面檢視** — 自營系統開發 Greeks 計算時,參考 Wilmott Vol 1 Ch.5 「bastard Greeks」— vomma (dVega/dVol), vanna (dDelta/dVol), charm (dDelta/dTime)。實盤 Iron Condor 管理這些二階 Greek 比 delta 更重要。
- **PDE finite-difference 求解器** — Wilmott Vol 1 Ch.28 給出 explicit、implicit、Crank-Nicolson 三種 FD 方案。對 American option 和 exotic 定價實用。直接拿 VBA 代碼移植到 Python。
- **Exotic option 快速分類** — 拿到任何異型合約,先問:是 barrier 嗎 (Asia barrier option 常見 KO)? 是 Asian 嗎 (大宗商品)? 是 lookback 嗎 (罕見)? 分類後對應 Vol 2 對應章節,標準處理框架。
- **Heston/SABR 校準基線** — 初次做 vol smile 交易,以 Heston (index/equity) 和 SABR (rates) 為起手;Wilmott 提供的初始值猜測 + Levenberg-Marquardt 迭代,是實務起點。
- **Model risk 清單** — 每個模型的 "assumptions that can break" 清單 (Vol 1 Ch.6):連續時間? 零交易成本? 有限波動率? 連續 rebalance? 任一違反即 model risk。定價時加相應 buffer。

### 盲點 / 反例 / 適用邊界
- **2006 年出版未覆蓋** — (a) LIBOR → SOFR 轉型 (2021-23), (b) Perpetual futures (crypto), (c) Options on ETFs volatility target (XIV), (d) OIS discounting 後 CSA 折現複雜化。讀者需自行延伸。
- **VBA 代碼已 legacy** — 現代實務應移植到 Python + NumPy + Numba + QuantLib;Wilmott 代碼僅作直覺參考,不宜直接運行。
- **Crypto derivatives 超出框架** — Perp funding、延期合約、日內 options (0DTE)、on-chain settlement 皆需新定價框架,Wilmott 2006 書未提。
- **Market microstructure 淡化** — Wilmott 主要從 pricing 視角,對 HFT、market making 結構性問題 (adverse selection, inventory) 涉獵少,需配 Harris、O'Hara、Aldridge。
- **Fixed-income 章節偏短** — Vol 3 的 rates 章節僅 ~200 頁,比起 Brigo-Mercurio 專書 (1000 頁+) 算精簡介紹,深入實作需進階書。

### 與 Edward 既有知識的連結
- 對齊 `0_frequently_asked_questions_in_quantitative_finance_2ed_2009_by_paul_wilmott` (FAQ 2009 版):FAQ 是入門問答,本書是深入實作。兩者配讀 = 從概念到代碼完整 Wilmott 體系。
- 深化 `wilmott_on_quantitative_finance` 和 `paul_wilmott_introduces_quantitative_finance_pdf_trading_software_pdfdrive`:都是 Wilmott 不同層次著作,這本最厚最全。Edward 的衍生品定價模組可以 Wilmott 三卷為骨,Python 實作。
- 連結 B1 自營系統:Edward 若要做 options MM 或 vol trading,必須至少實作 Heston 或 SABR + 校準 + Greeks。本書 Vol 3 Ch.19 正是藍圖。
- 對齊 `interest_rate_models_brigo_mercurio`:Brigo-Mercurio 更學術嚴謹;Wilmott Vol 3 更實務直覺。可以 Brigo 為理論,Wilmott 為程式起手。
- 延伸零式 `bias_toward_inaction`:Wilmott 反覆強調 "know your model assumptions";未滿足時勿用。這是「不動作」(skip this trade) 的理論基礎。
- 衝突於純 Shreve 流派:Shreve 嚴謹但遠離實作,Wilmott 寬鬆但能動手。Edward 務實傾向 Wilmott 風格。
