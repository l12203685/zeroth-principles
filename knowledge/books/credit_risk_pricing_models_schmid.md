# Credit Risk Pricing Models: Theory and Practice (2ed) — Bernd Schmid

### 目錄
1. 核心本質 — 信用風險是 default、recovery、correlation 三變數的聯合建模
2. 可用戰術 — Asset-based vs Intensity-based vs Copula 三種模型家族
3. 盲點/反例 — 2008 金融危機暴露的模型失效
4. 與 Edward 既有知識的連結

### TL;DR
Schmid 2ed (Springer Finance 2004, 387 頁 6 章) 是 risklab Germany Director 寫的信用風險模型綜覽，結構嚴謹：Ch 1 動機、Ch 2 建模 credit risk factors (transition + default + recovery)、Ch 3 公司/主權債券定價、Ch 4 相關違約、Ch 5 信用衍生品、Ch 6 三因子可違約期限結構模型 + Kalman Filter 校準 + 組合優化。全書**最大貢獻**是把 Merton 1974 asset-based approach、Jarrow-Turnbull 1995 intensity-based approach、Li 2000 copula correlation 三個分離的學派統整成可比較的框架；Ch 6 Schmid 自己提出的 three-factor model (risk-free rate + credit spread intensity + common risk factor) 用 affine term structure 同時處理 defaultable bond 與 swap。最實用的章節是 Ch 2.3 transition matrix（ordered probit 從主權 rating 估計）、Ch 2.4.5 Moody's LossCalc 模型（seniority × industry × business cycle 預測 recovery rate）、Ch 4.4 copula 方法建相關違約、Ch 5.4.3 CDO 定價。

### 核心本質
1. **Credit Risk 的三元組：PD × EAD × LGD（Ch 2.2）**：default probability × exposure at default × loss given default。Schmid 強調三者都是隨機變數，不能分開獨立估計——例 business cycle 既影響 PD（經濟衰退違約率上升）也影響 LGD（景氣差 collateral 拍賣價低）。2005-2007 高峰期 CDO 模型假設 PD 與 LGD 獨立，2008 同時惡化讓預測損失低估 3-5x。
2. **Asset-based vs. Intensity-based 是兩種世界觀（Ch 3.2 vs. 3.3）**：Merton 把 default 看作「公司價值 V 跌破負債 D 的 barrier event」，default time 是 hitting time（Black-Cox 1976 first passage time model）。Jarrow-Turnbull 把 default 看作「exogenous Poisson process 到達」，intensity λ(t) 可以 calibration 到 CDS spread。Asset-based 好處是有微觀因果，但對短期 PD 預測不準（jump-to-default 需要加 jump process）；Intensity-based 好處是好校準，但缺經濟基礎。
3. **Correlation 是信用組合最大難題（Ch 4）**：兩種作法——(a) correlated asset values (Vasicek 1987)：把每家公司 asset 分解成 systemic + idiosyncratic 因子，default correlation 來自 systemic 暴露，這是 Basel II IRB 的理論根基；(b) correlated intensities：doubly stochastic process，intensity 自己服從 stochastic process 帶共同因子。Ch 4.4 Gaussian Copula（David Li 2000 JoFI）則是把邊際 PD 與聯合結構分開估計——這個模型後來在 2008 被指為 CDO 爆雷元兇。
4. **Recovery Rate 不是常數（Ch 2.4.4）**：Moody's 歷史資料顯示 recovery rate 隨 seniority（Senior Secured 64% vs. Subordinated 30%）、industry（utility 高 tech 低）、business cycle（衰退期降 5-10%）變化。Schmid Ch 2.4.5 介紹 LossCalc：一個使用 Bayesian + 回歸 ensemble 的 recovery rate 預測模型（Moody's 2001）。對 CDS 實務校準至關重要——假設 R=40% 與 R=30% 給出的 implied hazard rate 差近 15%。
5. **三因子模型統一定價各類 credit-linked 工具（Ch 6.2-6.4）**：Schmid 的 r (risk-free rate) + s (short spread) + u (intensity) 三因子 affine 模型同時給出 defaultable discount bond、FRN、callable debt、credit default swap、credit spread option 的封閉解。Ch 6.6.3 用 Kalman Filter 校準 unobservable state variables（典型 state-space model 應用）。

### 可用戰術
1. **Ordered Probit 估計主權 rating transition（Ch 2.3 eq 2.3）**：當部分主權沒 rating 歷史只有 default 紀錄時，ordered probit 模型結合兩類 likelihood entries 估計 β 與 threshold。對新興市場 sovereign debt 建模極為有用——用 macro factors (debt/GDP, current account, reserves) 預測 rating。
2. **Pseudo-Bayesian 合併多個 transition matrix（Ch 2.3 eq Λ·Trs&p + (1-Λ)·Trop）**：把 S&P historical matrix 當 prior，自己估的 probit matrix 當 update，diag(α) 由 goodness-of-fit χ² 決定 row-by-row weight。抗雜訊、適用於樣本稀疏的 speculative grade。
3. **Copula-based CDO Tranche 定價（Ch 5.4.3）**：假設每個債名 default time 由 Gaussian Copula 連結，equity tranche loss = max(L-K, 0)，mezzanine = max(L-Ka, 0) - max(L-Kd, 0)。用 recursive convolution 或 Fourier transform 計算 portfolio loss distribution，代入 tranche payoff。這是標準 base correlation 的理論基礎。
4. **Kalman Filter 校準 latent state（Ch 6.6.3）**：observable: bond/CDS prices；state: r(t), s(t), u(t)。Transition equation 用 affine SDE discretization，observation equation 用 Duffie-Kan affine pricing formula。每日 close 後更新 state，對 live market-making 至關重要。
5. **Portfolio Credit VaR via Monte Carlo（Ch 6.7）**：對 correlated asset value 模擬 N 次路徑，每條計算 loss，取 99% percentile。配合 control variates（風險較低的 homogeneous portfolio 當 CV）可降 20x variance。

### 盲點/反例
1. **Gaussian Copula 低估尾部相關（Ch 4.4）**：2005-2007 CDO 市場普遍用 ρ=0.3 的 Gaussian Copula，2008 實際 default correlation 飆到 0.6-0.8。Student-t copula 或 Clayton copula（lower tail dependence）能部分修正但沒被普遍採用。Salmon (Wired 2009) "Recipe for Disaster: The Formula That Killed Wall Street" 直指 Li 模型是 CDO 爆雷關鍵。
2. **歷史違約率假設平穩（Ch 2.3）**：time-homogeneous Markov 假設轉移矩陣不隨時間變。但 2020 COVID、2008 次貸時 speculative grade default rate 從 3% 跳到 15%，time-homogeneous 模型完全失效。實務上要加 regime-switching 或 macro-conditional transition matrix。
3. **Recovery Rate 預測仍不佳（Ch 2.4）**：LossCalc RMSE 約 0.18，等於 18% 的 LGD 誤差區間；對 pricing 幾乎無用，只用於 regulatory 合規。2008 後 Basel III 推 downturn LGD (stressed estimate) 承認這個盲點。
4. **沒涵蓋 Sovereign Default 現代議題**：2010-2012 歐債危機催生一系列新問題——self-fulfilling default、OMT 後的 redenomination risk、CDS Big Bang / Small Bang、Greece PSI credit event ISDA ruling 等，Schmid 2004 版都沒涵蓋。
5. **Machine Learning credit scoring 缺席**：書中所有違約預測還停在 ordered probit / logit / Altman Z-score。2015+ 已轉向 gradient boosting、random forest、neural net 做 PD 預測（KGI、Ant Financial 的消金 credit scoring 即用 XGBoost）。

### 與 Edward 既有知識的連結
- **對照 Brigo-Mercurio《Interest Rate Models》（Round 1）**：Brigo-Mercurio 的 affine term structure 與 Schmid Ch 6 的三因子模型用相同數學工具——CIR/Hull-White/HJM 的 credit extension 就是 Schmid 做的。兩本一起讀完整張 rates + credit 的 term structure 圖。
- **對照 Sundaresan《Fixed Income Markets》（Round 1）**：Sundaresan 的「credit spread decomposition = expected loss + liquidity + risk premium」在 Schmid Ch 3.1 有嚴格數學推導。兩者互補——Sundaresan 提供市場直覺，Schmid 提供 pricing formula。
- **對照 Engle SRISK（Round 1 systemic_risk_europe）**：SRISK 用 long-run 機率模型估系統性風險；Schmid Ch 4.2 correlated asset value 用 factor model 估組合違約——兩個都是「條件 portfolio loss」的估計，前者看整個市場，後者看信用組合。
- **對照 ZP 交易系統風險管理**：若 ZP 會加 corporate bond 或 CDS 策略，Schmid Ch 5.3.3 Credit Default Products + Ch 5.4.2 Basket Default Swaps 是必讀。實務上 CDX/iTraxx index + basket hedge 需要 base correlation 的跨 tranche 對沖邏輯。
- **對照 Poker 的 bluff-vs-value 邏輯**：credit market 的 spread widening 類似 poker 的「對手 raise 可能 value 或 bluff」——liquidity crisis 讓 good credit 與 distressed credit 一起 spread widen（pooling equilibrium），這時買入 investment grade = value bet。2020 年 3 月 IG spread 一週從 100bps 飆到 400bps 就是極端案例，Pimco、Blackrock 這時進場抄底獲利豐厚。
