## Forecasting: Principles and Practice 3e — Rob J. Hyndman & George Athanasopoulos
**來源**: otexts.com/fpp3 canonical edition  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- 第 1-2 章 概論（forecaster 的角色、time series graphics：seasonal plot、STL 分解）
- 第 3 章 Time Series Decomposition（additive vs multiplicative、STL、X-13ARIMA-SEATS）
- 第 4 章 Time Series Features（strength of trend、seasonality、lumpiness、flat spots）
- 第 5 章 Toolbox（naive、drift、mean methods；residual diagnostics：Ljung-Box、Breusch-Godfrey）
- 第 6 章 Judgmental Forecasts（Delphi method、scenario forecasting）
- 第 7 章 Time Series Regression（TSLM、spurious regression、dummy seasonality）
- 第 8 章 Exponential Smoothing（SES、Holt、Holt-Winters、ETS state-space）
- 第 9 章 ARIMA Models（differencing、ACF/PACF、auto-selection、seasonal ARIMA）
- 第 10 章 Dynamic Regression（ARIMA errors、lagged predictors、intervention）
- 第 11 章 Hierarchical & Grouped Forecasts（bottom-up、top-down、middle-out、optimal reconciliation）
- 第 12 章 Advanced Forecasting（TBATS、NNETAR、bootstrapped prediction intervals、Prophet）
- 第 13 章 Practical Issues（weekly data、missing values、COVID-19 outliers）

### TL;DR (≤120字)
Hyndman 這本 fpp3 是時間序列預測的現代標準教材，免費線上 + R `fable` 套件實作。對交易者最寶貴：第 3-9 章傳統方法（STL、ETS、ARIMA）+ 第 11 章 hierarchical（多資產 coherent forecast）+ 第 12 章 Prophet/NN 混合。比 Box-Jenkins 1976 更現代、比 Shumway-Stoffer 更實用；R 碼可直接跑。對波動率/成交量預測特別好用。

### 核心本質 (3-5 條)
1. **ETS state-space = exponential smoothing 的完整架構（本質，第 8 章）** — ETS(Error, Trend, Season) 15 種組合；自動選擇 via AICc；給出 point forecast + prediction interval。對 vol/volume 的 seasonality 最適用。
2. **ARIMA 需看 ACF/PACF 決定 p,q（本質，第 9 章）** — AR(p): PACF 截尾 at lag p；MA(q): ACF 截尾 at lag q；也可用 `auto.arima()` AICc 自動搜。但金融價格通常 non-stationary，需先 differencing。
3. **Hierarchical forecasting 的 coherency（本質，第 11 章）** — 板塊 → 產業 → 個股若各自預測，加總通常不一致（incoherence）；optimal reconciliation（Wickramasuriya 2019）用 MinT 最小化 reconciled forecast variance。
4. **CV for time series = rolling origin（本質，第 5.10 節）** — 不能隨機 KFold，必須 time-ordered；`tsCV()` 函式用 expanding/sliding window 算 CV error。
5. **Prediction interval 比 point forecast 重要（本質，第 5.5、8.7 節）** — 點預測總是錯，區間涵蓋真值機率才有意義。`bootstrap = TRUE` 用 residual resampling 得 non-Gaussian PI（對 fat-tail 必要）。

### 可用戰術/策略
- **STL + Prophet 預測成交量**：先 STL 分解 seasonality，再用 Prophet 預測 trend 與 holiday；合成回 forecast。
- **ETS for vol**：對 σ_t 用 ETS(A, N, A)（additive error、no trend、additive season）；AICc 約束自動。
- **Hierarchical portfolio forecast**：10 產業 + 500 股票，用 `reconcile(method = "mint_shrink")` 讓產業與個股 forecast 加總一致。
- **ARIMA-GARCH hybrid**：mean 用 ARIMA、variance 用 GARCH；`rugarch` 套件標準做法。
- **TSCV rolling origin**：`time_slice()` with assess=5, skip=1；對每 window 算 MASE，平均評估策略穩健性。

### 盲點 / 反例 / 適用邊界
- **假設 short-memory 時序**：ARIMA/ETS 對 long-memory（Hurst > 0.5）或 regime-switching 失效；金融需 FIGARCH 或 HMM。
- **Univariate 為主**：多變量 VAR 僅略提；需搭 Lütkepohl 或 Hamilton。
- **ML 輕輕帶過**：第 12 章 NN/Prophet 各一節；深入需配 Goodfellow/Tsay-Chen ML。
- **單純 additive noise**：大多假設 residual iid N(0, σ²)；金融 residual heavy-tailed，需 Student-t。
- **無 intraday 章節**：以日/月/季資料為主；高頻 tick 資料需別書。

### 與 Edward 既有知識的連結
- **對齊 ZP volatility forecast**：ETS/ARIMA 用於低頻 vol 預測；GARCH 高頻。兩者 ensemble。
- **延伸 Tsay (Round 1)**：Tsay 數學深但 R 少；Hyndman 實用碼多。Tsay 理論 + Hyndman 實作 = 完整。
- **衝突點**：Hyndman 注重 statistical；Edward 的 ML factor model 偏機器學習；hybrid 方法 = STL 去季節 → XGBoost 學殘差。
- **可挖金礦**：第 11 章 MinT 最優 reconcile 可以套 ZP 「資產 → 策略 → 風格 → 組合」層級預測。
- **對接 Box-Jenkins 原版**：Box-Jenkins 1976 是 ARIMA 原文；Hyndman 是現代化 re-presentation；兩書先後讀。
