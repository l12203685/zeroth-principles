## Time Series Analysis: Forecasting and Control 4e — George E.P. Box, Gwilym M. Jenkins, Gregory C. Reinsel
**來源**: E:/書籍/George E.P. Box, Gwilym M. Jenkins, Gregory C. Reinsel-Time Series Analysis_ Forecasting and Control-Wiley (2008).pdf  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- **Part I Stochastic Models and Their Forecasting (1-5)**：
  - 第 1 章 Introduction（time series、stochastic process、stationarity）
  - 第 2 章 Autocorrelation Function & Spectrum of Stationary Processes
  - 第 3 章 Linear Stationary Models（general linear process、AR、MA、ARMA）
  - 第 4 章 Linear Nonstationary Models（IMA, ARIMA, fractional differencing）
  - 第 5 章 Forecasting（minimum MSE forecast、forecast error variance）
- **Part II Stochastic Model Building (6-8)**：
  - 第 6 章 Model Identification（ACF/PACF、subset models）
  - 第 7 章 Model Estimation（LS、MLE、backcasting）
  - 第 8 章 Model Diagnostic Checking（residual ACF、overfitting check、Ljung-Box）
- **Part III Special Topics (9-14)**：seasonal models、nonlinear models、intervention analysis、outlier detection、multivariate TS、state-space transfer function models
- 第 15 章 Aspects of Process Control

### TL;DR (≤120字)
Box-Jenkins 1976 原典（第 4 版 2008 與 Reinsel 合編）是 ARIMA 方法論的發源地。Box-Jenkins methodology 三階段（Identification → Estimation → Diagnostic Checking）成為 TS 分析的標準 workflow。比 Hamilton 實用但數學仍嚴謹；包含 intervention analysis、transfer function 等 Hamilton 未涵蓋主題。對 process control / quality control 背景讀者尤其友善。書較重理論，R/Python 實作需配合 Hyndman FPP3。

### 核心本質 (3-5 條)
1. **Box-Jenkins 三階段方法論（本質，Part II）** — Identification（看 ACF/PACF 猜 p,q）→ Estimation（MLE 估參數）→ Diagnostic Checking（殘差 ACF 應為白噪）→ 不合格則 Identification 重來。這是 TS 分析的 golden standard workflow。
2. **Ljung-Box test 是殘差白噪檢驗（本質，第 8 章）** — Q = T(T+2)Σ ρ̂_k²/(T-k) ~ χ²(h-p-q)；殘差若為白噪則 p-value 大，否則模型 misspec。實務 lag h = min(20, T/4)。
3. **ARIMA(p,d,q) 統一 stationary + nonstationary（本質，第 4 章）** — 先 difference d 次讓序列 stationary，再對差分後序列套 ARMA(p,q)。d=1 對 random walk 就足夠；d=2 對 double-trend。
4. **Transfer function 是「動態回歸」（本質，第 11 章）** — y_t = Σ v_k X_{t-k} + ε_t 的 dynamic model；比簡單 regression 更好刻劃 lead/lag 結構。輸入/輸出系統標準工具。
5. **Intervention analysis 處理 structural break（本質，第 12 章）** — Policy shock / natural disaster 產生 pulse 或 step intervention；在 model 加 indicator × ω 捕捉 intervention effect。Box-Tiao 1975 原文在此書第 12.3 節。

### 可用戰術/策略
- **Airline model SARIMA(0,1,1)(0,1,1)_12**：Box-Jenkins 的經典範例；對月頻資料（如月成交量、月 vol）完美對應。
- **Outlier detection via residuals**：擬合 ARIMA 後，檢查殘差是否超出 ±3σ；逐一添加 outlier indicator 重估，直到殘差乾淨。
- **Intervention for regulation shock**：2020 年 3 月美聯儲零利率為 step intervention；y_t = ARIMA + ω × I(t ≥ March 2020)；ω 估計該政策對 VIX 的永久影響。
- **Transfer function for lead indicator**：PMI leading GDP；TF model GDP_t = Σ v_k PMI_{t-k} + noise；v_k 估計 lead structure。
- **Box-Pierce + Ljung-Box 雙檢驗**：Box-Pierce 小樣本失真，Ljung-Box 修正；金融小樣本用 Ljung-Box。

### 盲點 / 反例 / 適用邊界
- **Univariate 為主**：多變量 VAR 章節淺（第 13 章）；深入需 Lütkepohl / Hamilton。
- **Linear 假設**：第 10 章 nonlinear model 較短；金融 TS 強非線性需 Tsay / Tong。
- **Gaussian 殘差假設**：金融 fat-tail 下 Ljung-Box 的 χ² 假設失效；需 bootstrap-based 版本。
- **計算實作需 R/SAS**：書給公式不給代碼；現代實作用 R `forecast::auto.arima()` 或 Python `statsmodels.tsa.arima`。
- **Frequency-domain 輕**：Box-Jenkins 以 time-domain 為主；頻譜分析只第 2 章略提。

### 與 Edward 既有知識的連結
- **對齊 ZP time series baseline**：任何新 TS model 需 beat ARIMA(p,d,q) baseline + Ljung-Box 殘差檢驗；這是最低標準。
- **延伸 Hyndman FPP3**：Box-Jenkins 是 FPP3 第 9 章 ARIMA 的理論源頭；先讀 Hyndman 實用再讀 Box-Jenkins 理論。
- **衝突點**：Box-Jenkins 強調 identification 靠目視 ACF/PACF；`auto.arima()` 自動化但可能選到次優。Edward 實務應兩者互驗。
- **可挖金礦**：第 12 章 intervention analysis 直接套用 ZP event-driven 策略——FOMC、earnings、M&A 皆是 intervention。
- **對接 Hamilton / Brockwell-Davis**：Box-Jenkins 是源頭、Hamilton 集大成、Brockwell 實用版；三書線性遞進。
