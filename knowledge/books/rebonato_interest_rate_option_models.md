## 利率選擇權模型 (Interest-Rate Option Models, 2nd ed) — Riccardo Rebonato (1998)
**來源**: E:/書籍/Quant/Rebonato_Interest_Rate_Option_Models_2ed.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Part I Basic Concepts**
  - Ch.1-3 利率入門 / 風險中性定價 / 零息曲線構造
- **Part II Short-Rate Models**
  - Ch.4-6 Vasicek / CIR / Hull-White / Black-Karasinski
- **Part III No-Arbitrage Yield-Curve Models**
  - Ch.7-9 HJM 架構 / 一因子 HJM / 多因子 HJM
- **Part IV Market Models**
  - Ch.10-11 BGM (Brace-Gatarek-Musiela) / LIBOR Market Model 雛形
- **Part V Calibration & Implementation**
  - Ch.12-15 市場數據擬合 / 模型比較 / 數值方法 / PDE vs trees vs Monte Carlo
- **Appendix** — 統計、SDE、numerical 背景

### TL;DR (≤120字)
Rebonato 利率衍生品定價經典 2nd 版。定位在「數學家不夠直覺、Hull 不夠深」之間,是 1990 年代後期固定收益 desk 必備。核心:(1) 介紹利率模型三大家族 (short-rate, HJM, BGM) 及其實作;(2) 強調校準 (calibration) 是實務最大痛點,不是推導;(3) 大量「模型選擇」討論 — 為何一家 desk 喜歡 Hull-White,另一家用 BGM? 讀者能學到「模型作為工程選擇」而非「模型作為數學發現」。2000 年 Rebonato 寫 LMM 專書前的過渡作。

### 核心本質 (3-5 條, 每條 50-120字)
1. **三大家族架構 (Ch.4-11)** — (a) Short-rate (Vasicek/CIR/HW):建模瞬時利率,簡單、closed-form、但 forward rate 行為有限;(b) HJM:建模整條 forward curve 演化,一般性最高,數學上完整,但實作困難 (state-dependent drift);(c) BGM/LMM:建模可觀察 LIBOR rate,自然對應市場報價,2000 年代成主流。每家適合的場景不同。
2. **校準的重要性大於推導 (Ch.12)** — 學術論文多集中模型推導,實務 quant 80% 時間在校準 (calibrate) — 選參數讓模型重建市場 cap/swaption 價格。校準準則 (caplet 擬合? swaption 擬合? 兩者權衡?) 影響定價 exotic 時的 hedge PnL。Rebonato 反覆提醒:校準選擇比模型選擇更重要。
3. **Mean reversion & 波動率結構 (Ch.4)** — 短期利率 mean reversion (Vasicek/CIR/HW 共性) 反映實務:低利率時期利率總會反彈,高利率時期利率總會下跌。這是 1980-90 實證穩定 pattern,但 2008 後日本/歐元區零利率持續多年,挑戰 mean-reversion 強度的校準。
4. **波動率期限結構 (Volatility Term Structure, Ch.11)** — 市場 caplet 波動率通常中期較高 (2-5Y) 兩端較低 (hump-shaped)。Rebonato 示範如何用 LMM 擬合此結構,這是 swaption + cap/floor 混合 desk 的日常。Edward 對加密永續期限結構類似 (funding rate term structure) 可借鑑。
5. **模型比較方法論 (Ch.13)** — 不同模型在「flat」香草產品定價可能相近,但在 exotic (Bermudan、callable、CMS spread option) 上顯著分歧。Rebonato 建議至少用兩個家族模型 benchmark 每個 exotic,差異 > 5% 時警示。

### 可用戰術/策略
- **利率模型家族選擇指南** — 對具體產品選模型:(a) 香草 cap/floor → LMM (直接); (b) short-date bond option → HW; (c) Bermudan swaption → HW 或 LMM; (d) exotic callable → LMM + Longstaff-Schwartz; (e) 教學/原型 → Vasicek (簡)。
- **波動率校準流程** — (1) 取當日 ATM swaption 波動率矩陣 (2) 選模型 (如 LMM 參數化) (3) 最小化定價誤差 (4) 檢驗 exotic 定價穩定性。每日 re-cal,比較參數漂移。漂移大 = 模型可能誤認或市場破壞假設。
- **Mean reversion 估計** — 用歷史 rate data 跑 AR(1) regression 估 κ (mean reversion speed)。對美元 short rate,歷史 κ ~ 0.3/年 (半衰期 ~2.3 年);2020s 來源重新估計可能顯著降低。
- **Exotic benchmark practice** — 任何 exotic pricing 前:用兩家族模型計算,取差異作 model risk 估計。5% 內可接受;10%+ 須追蹤差異來源並報告。
- **SOFR transition 實務啟示** — 雖 1998 版未涵蓋,框架可應用 — SOFR 取代 LIBOR 後,LMM 需重參數化。2022 後 SOFR-LMM/SOFR-HJM 正是 Rebonato 框架的 SOFR adaptation。

### 盲點 / 反例 / 適用邊界
- **1998 版 Libor-centric** — 所有 cap/floor 假設基於 LIBOR;2022 LIBOR 退場後,SOFR/SONIA/ESTR 等 risk-free rate 成為基準,書中框架須重建。讀 Rebonato 新版或後續作品 (Modern Pricing of Interest Rate Derivatives 2002) 補完。
- **負利率挑戰** — 模型多假設 rate > 0 (log-normal 結構);2014-2022 歐元區 ESTR 負利率破壞。Shifted log-normal (如 Bachelier/Normal 模型) 才適用,Rebonato 後期作品補。
- **Multi-curve framework 未涵蓋** — 2008 後 collateral (CSA) 定價引入 OIS discount + LIBOR projection 雙曲線;單一曲線折現已過時。本書框架需 2008 後擴展。
- **Smile modelling 僅概述** — LMM 本身不帶 smile,需擴展到 SABR-LMM (Hagan) 或 local vol-LMM。本書僅觸及,深入需 Rebonato-McKay-White《SABR/LMM》(2009) 或 Andersen-Piterbarg 三卷。
- **Credit risk 完全未提** — 本書純利率風險,忽略 counterparty credit (CVA)、XVA (FVA, KVA)。2010 後 XVA 已是 desk 日常,必須配 Gregory《XVA Challenge》補。

### 與 Edward 既有知識的連結
- 深化 `interest_rate_models_brigo_mercurio`:Brigo 更數學完整,Rebonato 更實務。可 Rebonato 入門、Brigo 進階。
- 對齊 `paul_wilmott_quantitative_finance_vol123` Vol 3 rates 章節:Wilmott 介紹三家族,Rebonato 深入每家族細節。
- 連結 B1 加密策略的 funding rate 理論:Crypto 永續 funding rate 類似 LIBOR,可用 Rebonato mean-reversion + vol term structure 框架建模。Funding rate 衍生品 (options on funding) 將成未來交易標的。
- 對 ZP 固定收益 playbook:Rebonato 提供校準 practical workflow,是 ZP 「每日 rates desk 流程」模板。
- 延伸零式 `information_asymmetry_2`:Rebonato 強調校準參數漂移偵測 — 當參數異常漂移時,可能市場即將發生 regime change。Edward 的 alpha 有一類正是「參數漂移 → 預判結構性事件」。
- 衝突於 Shreve 學術派:Shreve 強調嚴謹推導,Rebonato 強調工程實作。Edward 實務傾向 Rebonato;但數學證明時仍需 Shreve。
