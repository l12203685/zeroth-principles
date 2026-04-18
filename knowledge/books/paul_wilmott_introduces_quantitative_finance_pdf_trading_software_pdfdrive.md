## Paul Wilmott Introduces Quantitative Finance (2nd Ed) — Paul Wilmott
**來源**: E:/投資交易/交易學習資料庫/@交易/@選擇權/Paul Wilmott - Introduces Quantitative Finance.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Ch 1-2** Products and Markets, Derivatives
- **Ch 3** The Binomial Model
- **Ch 4** The Random Behavior of Assets
- **Ch 5** Elementary Stochastic Calculus
- **Ch 6** The Black-Scholes Model
- **Ch 7** Partial Differential Equations
- **Ch 8** The Black-Scholes Formulæ and the Greeks
- **Ch 9** Overview of Volatility Modeling (GARCH, SV, stochastic & jump)
- **Ch 10** How to Delta Hedge (discrete rebalancing, transaction costs)
- **Ch 11** Exotic and Path-dependent Options
- **Ch 12** Multi-asset Options (basket, correlation)
- **Ch 13** Barrier Options
- **Ch 14** Fixed-income: Yield, Duration and Convexity
- **Ch 15** Swaps
- **Ch 16** One-factor Interest Rate Modeling
- **Ch 17** Yield Curve Fitting
- **Ch 18** Interest Rate Derivatives
- **Ch 19** HJM and BGM/Musiela Models
- **Ch 20** Investment Lessons from Blackjack and Gambling
- **Ch 21** Portfolio Management
- **Ch 22** Value at Risk
- **Ch 23** Credit Risk
- **Ch 24** RiskMetrics and CreditMetrics
- **Ch 25** CrashMetrics
- **Ch 26** Derivatives F***-Ups (著名案例)
- **Ch 27-30** Numerical Methods (FD, MC, Numerical Integration)
- **Appendix A-E** Math Summary, Forecasting digression, Trading Game, CD contents, PWOQF2 upgrade

### TL;DR (≤120字)
Wilmott 的入門教材(姐妹篇為 FAQ),比 Hull 更 pedagogical + 幽默:完整覆蓋 derivatives 定價 + 利率模型 + 風險管理 + 數值方法,每章配帶故事的實務警示。Ch20「從 Blackjack 學投資」、Ch25 CrashMetrics、Ch26 F-Ups 等章節是此書靈魂,給 quant 學生最好的 "常識 + 理論" 綜合引子。

### 核心本質 (3-5 條, 每條 50-120字)
1. **Binomial Tree 是 "從離散到連續" 的最佳教學橋樑** — Ch3 先給 binomial,才進 BS (Ch6);這順序讓學生看到 BS 其實是 binomial 的連續極限。理解這一點 = 理解所有 pricing 方法的共同結構:backward induction + risk-neutral expectation。
2. **Blackjack card-counting 是 investment 的正確直覺** — Ch20 的核心:投資不是「預測未來」,是「識別 edge + 正確 sizing (Kelly)」。Card counting 有 edge 時加碼,無 edge 時 sit out。這比所有 "賺錢秘訣" 書都誠實地描繪真實投資本質。
3. **CrashMetrics (Ch25) 是對 VaR 的必要補充** — VaR 假設正態 + 歷史重現;崩盤時兩者都失效。CrashMetrics 問:若某因子突然跳 X 個標準差,組合會損失多少?答案不用統計分布假設,直接用 sensitivity + stress test。適用於 fat tail 情境。
4. **Derivatives F***-Ups (Ch26) 是活生生的教訓** — Barings (Leeson)、LTCM、Metallgesellschaft、Orange County 等案例詳解:共同特徵 = 忽略模型假設的限制、倉位過大、缺乏獨立風控。每個 quant 每 5 年應重讀此章。
5. **Delta hedging 在現實中不是 "連續 rebalance" 而是 "band-based discrete"** — Ch10 明確:交易成本下連續 delta 對沖是成本無窮大;實務採 "當 delta 超過 band 才 rebalance",最優 band width 由 Whalley-Wilmott 公式給出 (∝ vol^(2/3)/cost^(1/3))。

### 可用戰術/策略
- **實作 binomial tree + BS 雙引擎做 sanity check** — 同一 option 用 binomial (Ch3) 與 BS analytic (Ch6) 兩種方法定價,差異 < 1 cent 才信任程式碼。這是 quant dev 的基本手法 — 任何新 pricing code 都需兩種獨立方法驗證。
- **Whalley-Wilmott delta hedging band** — 實務 options market making 或 gamma scalping 的最優 rebalance band;公式 = C × (cost/vol²)^(1/3) × S^(2/3) × |Γ|^(1/3)。可直接實作到 B1 選擇權策略。
- **Kelly criterion 半凱利 / 四分之一凱利** — Ch20-21:純 Kelly 波動性極大(短期 drawdown 可能 -50%);實務採 0.25-0.5 × Kelly 作為 trade-off。B1 策略倉位 sizing 可用此 rule 代替固定百分比。
- **CrashMetrics 作為 tail risk stress test** — 定義極端情境 (股票 -30%、VIX +200%、credit spread +500bp),算組合損失;若超過 risk budget 則減倉或買 tail hedge。B1 系統 weekly stress run。
- **Ch26 F-Ups 案例作為新員工培訓教材** — 每個案例提取 lessons,整理成 ZP 知識庫的「交易災難分析」子目;新 quant 工程師上線前必讀。

### 盲點 / 反例 / 適用邊界
- **2007 版,缺 2008 後 XVA、multi-curve、LIBOR 退場(→ SOFR)等監管演進** — 利率章節 (Ch14-19) 需以 Henrard 或 Gregory 更新版本補。
- **強理論,實作 code 靠 CD 附件(Excel/Matlab)** — 對 Python quant 不如 Benninga 直接;與《Modeling Derivatives in C++》互補(理論+實作)。
- **偏 sell-side derivatives quant 角度,buy-side 策略研究覆蓋淺** — Ch21 Portfolio Management 只是 introduction level;買方 alpha research 需另讀 López de Prado、Kakushadze-Serur。
- **Ch9 volatility modeling 概覽但缺深度** — 實務 vol trader 需讀 Gatheral《Volatility Surface》、Bergomi《Stochastic Volatility Modeling》補 smile 動態與 local-stoch vol 細節。

### 與 Edward 既有知識的連結
- Wilmott 的 "commonsense + theory + fun" 風格最契合 Edward 的「零式本質 + 實務戰場」雙軌思維。Ch20-21-25-26 四章是零式思維的金融工程版表達。
- 對應 `meta_strategy_over_strategy`:Ch20 Blackjack 比喻、Ch25 CrashMetrics、Ch26 F-Ups 都在 meta-strategy 層 — 不是「如何做某策略」,是「在什麼原則下選擇/放棄策略」。
- 連結 Wilmott 同作者的 FAQ 書:本書是入門教材,FAQ 書是 reference;可以先讀本書建立框架,FAQ 書做速查。兩書組合是 quant 學生的最強 Wilmott 套餐。
- 對 B1 自營交易系統的貢獻:Ch21 的 Portfolio Management + Ch22 VaR + Ch25 CrashMetrics 可作為「風險管理模組」的 top-level architecture;Ch10 Whalley-Wilmott band 是 option rebalancer 的 default 參數。
