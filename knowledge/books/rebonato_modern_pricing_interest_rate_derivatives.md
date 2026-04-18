## 利率衍生品的現代定價:LIBOR Market Model 及其超越 (Modern Pricing of Interest-Rate Derivatives: The LIBOR Market Model and Beyond) — Riccardo Rebonato (2002)
**來源**: E:/書籍/Quant/Rebonato_Modern_Pricing_Interest_Rate_Derivatives_2002.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Part I The Context**
  - Ch.1 No-arbitrage 復習 / Ch.2 The Landscape
- **Part II The LIBOR Market Model**
  - Ch.3-7 LMM 結構與校準 / 波動率函數選擇 / 相關性矩陣校準
- **Part III Calibration**
  - Ch.8-11 Caplet 校準 / 聯合 caplet-swaption 校準 / Historical vs Implied
- **Part IV Beyond the Standard LMM**
  - Ch.12-14 Local vol within LMM / Stochastic vol LMM / Jump-diffusion LMM
- **Part V Applications**
  - Ch.15-17 Bermudan swaption / Exotic callables / Monte Carlo for LMM
- **Part VI Back to Fundamentals**
  - Ch.18 模型選擇的哲學省思

### TL;DR (≤120字)
Rebonato 2002 LMM 時代經典。接續 1998 Interest-Rate Option Models,更深入聚焦 LMM 及其工業實現。核心三主題:(1) LMM 波動率函數的結構性選擇 (parametric vs flexibility 權衡);(2) 相關性矩陣校準 — 秩不足 (Rank reduction) 與金融直覺;(3) Smile 納入 LMM 的三條路 (Local vol/Stochastic vol/Jump),各有優缺。Ch.18 哲學章節總結模型選擇是工程+文化問題,非純數學。是 LMM desk 每位 quant 必讀。

### 核心本質 (3-5 條, 每條 50-120字)
1. **LMM 的工程魅力 (Ch.3-5)** — LMM 直接建模「市場可見」的 forward LIBOR rates 而非抽象 short rate/forward curve。每個 forward LIBOR 有自己的波動率,組成向量,通過相關性矩陣連結。好處:caplet 定價 closed-form Black-Scholes;壞處:swaption 需 Monte Carlo 或近似。市場報價結構和模型結構對應直接。
2. **波動率函數參數化選擇 (Ch.4)** — Rebonato 提出「time-homogeneous + hump-shaped」波動率:σ(T-t) = (a + b(T-t)) × exp(-c(T-t)) + d。參數 a-d 有金融意義 (short vol, peak, decay, long vol),限制模型同時保留靈活性。校準 4 參數到 market cap vol surface 通常可 <1% 誤差。
3. **相關性矩陣的秩不足 (Ch.6)** — N 個 forward rates 理論上 N×N 相關矩陣,實務上為了 Monte Carlo 效率 + 物理直覺,降至 rank k (通常 2-4)。Rebonato 的 rank reduction:用 Schoenmakers-Coffey 或直接 eigenvalue truncation。降秩後仍應保持正定與金融合理 (長短 correlation 遞減)。
4. **Smile 三條路 (Ch.12-14)** — (a) Local vol 作為 LMM 擴展 (SABR-LMM, Hagan-Rebonato-West):最自然,但 smile dynamics 可能不對;(b) Stochastic vol LMM (Heston-like):smile dynamics 對但數值困難;(c) Jump-diffusion LMM:skewness 快,但 smile tail 可能誇張。沒有 universal 答案,看具體 exotic。
5. **校準 caplet vs swaption 的哲學 (Ch.8-11)** — Caplet 是 LMM 自然原料 (forward LIBOR 的 Black formula);Swaption 是 forward swap rate 的 option,牽涉多個 forwards。聯合校準時常有衝突 — 完美 caplet 校準 = swaption 誤差 5-10%,反之亦然。市場 quote哪個更 liquid 就偏哪邊。Rebonato 建議以 exotic hedge 需求決定 weighting。

### 可用戰術/策略
- **LMM 生產工作流** — (1) 取 market discount curve (2) 取 cap vol surface + swaption vol matrix (3) 參數化 σ(T-t) 擬合 cap (4) 參數化 Schoenmakers-Coffey correlation 擬合 swaption (5) Monte Carlo 驗證。每日 re-cal,存參數時間序列監測漂移。
- **Rank reduction 實戰** — 對 N=60 forward rates (15 年季度),降到 k=3 通常保留 >95% variance。使用 eigendecomposition 然後 truncate + normalize。Python numpy.linalg.eigh + normalize 一行可做。
- **Bermudan swaption 定價** — 標準 Longstaff-Schwartz in LMM: (a) Monte Carlo forward 路徑 (b) 逆向歸納用 regression 估計 continuation value (c) exercise decision 比較 intrinsic vs continuation。書中 Ch.15 給參考 implementation。
- **Smile inclusion 選擇樹** — 產品是 callable exotic? → SV-LMM; 是 CMS spread? → SABR-LMM; 是 digital barrier? → Jump LMM。不同產品不同 smile model,單一模型 cover 所有 = 校準失敗。
- **Correlation shock 敏感度** — 除 delta/vega 外定期跑 correlation shock (+/- 10% off-diagonal)。Bermudan swaption 和 CMS 對 correlation 非常敏感,但傳統 desk risk report 少報。

### 盲點 / 反例 / 適用邊界
- **LIBOR 退場 (2021-2023)** — 本書完全基於 LIBOR;SOFR transition 要求重新考慮:SOFR 是 overnight rate,compound 計算 forward;LMM 需改為「SOFR compound rate market model」(SABR 的 SOFR 版本)。Piterbarg/Andersen 2020+ 論文補。
- **負利率與 log-normal 假設** — LMM Ch.3-7 假設 forward rates > 0 (log-normal dynamics)。2014-22 歐元區 EUR forwards 轉負,log-normal 破壞。Shifted log-normal + displaced diffusion 實用變形。
- **Multi-curve framework 未內化** — 2008 後 CSA discounting (OIS) vs projection (LIBOR) 分家,本書仍是單一曲線。實務生產系統已是多曲線 (USD: SOFR discounting + LIBOR/Term SOFR projection)。
- **XVA 完全缺席** — CVA/FVA/KVA 在 2010 後是 rates desk 日常,需配 Gregory 或 Andersen-Piterbarg Vol 2-3 補完。
- **Crypto 利率衍生品未涵蓋** — DeFi 上 Aave/Compound 利率是 on-chain 動態,非 LIBOR 樣式,無法直接套用。但 Rebonato 方法論 (波動率函數參數化 + 相關性校準) 原理可借鑑到 DeFi curve。

### 與 Edward 既有知識的連結
- 直接延續 `rebonato_interest_rate_option_models` (1998):兩本是姊妹篇,1998 版介紹三大家族,2002 版深入 LMM 實作。合讀 = Rebonato 整體利率學派。
- 對齊 `interest_rate_models_brigo_mercurio`:Brigo 更數學嚴謹,Rebonato 更實務文化 + 工程直覺。實際 desk 兩本都不可缺。
- 深化 `paul_wilmott_quantitative_finance_vol123` Vol 3 rates:Wilmott 快速概覽,Rebonato 深入校準與 smile 處理。
- 連結 B1 加密策略:DeFi 利率衍生品 (Pendle、Notional、IPOR) 正在萌芽,可借鑑 LMM 思想開發 on-chain 利率交易策略。Funding rate 亦類似。
- 對 ZP 固定收益 playbook:Rebonato 的校準 workflow (caplet + swaption 聯合 + rank reduction) 是 standard desk operations,可作為 ZP 固定收益教學材料骨架。
- 延伸零式 `derivative_over_level`:LMM 本質是 forward LIBOR 的 dynamics — derivative 的 derivative (forward 是 derivative of zero-coupon)。Edward 的 alpha 永遠是理解多層 derivative 結構。
- 衝突於純 HJM 學派:HJM 更一般 (建模 forward curve 演化),LMM 更實務 (建模可觀察 LIBOR)。兩者各有優劣,Edward 工程優先偏 LMM。
