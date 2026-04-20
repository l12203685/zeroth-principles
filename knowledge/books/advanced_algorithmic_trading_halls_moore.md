## Advanced Algorithmic Trading — Michael L. Halls-Moore
**來源**: E:/書籍/Advanced Algorithmic Trading-Bayesian Statistics, Time Series, ML, Halls-Moore.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **I Introduction**
  - Introduction To Advanced Algorithmic Trading
- **II Bayesian Statistics**
  - Introduction to Bayesian Statistics
  - Bayesian Inference of a Binomial Proportion
  - Markov Chain Monte Carlo
  - Bayesian Linear Regression
  - Bayesian Stochastic Volatility Model
- **III Time Series Analysis**
  - Introduction to Time Series Analysis
  - Serial Correlation
  - Random Walks and White Noise Models
  - Autoregressive Moving Average Models
  - Autoregressive Integrated Moving Average and Conditional Heteroskedastic Models
  - Cointegrated Time Series
  - State Space Models and the Kalman Filter
  - Hidden Markov Models
- **IV Statistical Machine Learning**
  - Introduction to Machine Learning
  - Supervised Learning
  - Linear Regression
  - Tree-Based Methods
  - Support Vector Machines
  - Model Selection and Cross-Validation
  - Unsupervised Learning
  - Clustering Methods
  - Natural Language Processing
- **V Quantitative Trading Techniques**
  - Introduction to QSTrader
  - Introductory Portfolio Strategies
  - ARIMA+GARCH Trading Strategy on Stock Market Indexes Using R
  - Cointegration-Based Pairs Trading using QSTrader
  - Kalman Filter-Based Pairs Trading using QSTrader
  - Supervised Learning for Intraday Returns Prediction using QSTrader
  - Sentiment Analysis via Sentdex Vendor Sentiment Data with QSTrader
  - Market Regime Detection with Hidden Markov Models using QSTrader
  - Strategy Decay

### TL;DR
QuantStart 創辦人 Halls-Moore 的 517 頁量化實戰書,三主軸:貝氏統計 (PyMC3/MCMC) → 時間序列 (AR/MA/ARIMA/GARCH/state-space) → 機器學習 (SVM/RF/DL),搭配 QSTrader 回測引擎。不教策略,教「如何用現代統計工具把不確定性量化」,偏學術工具箱但指向實戰 edge。

### 核心本質
1. **Bayes 是「先驗 + 資料 → 後驗」的結構化信念更新** — 每次新資料更新後驗,策略參數成為可機率化的不確定量而非點估計。是處理小樣本 / 高雜訊金融資料的本質工具,對應零式「邊際資訊決定下注」。
2. **時間序列核心是分解:趨勢 + 季節 + 自相關 + 隨機波動** — 價格序列應拆成可預測與不可預測分量,前者建模後者量化 risk。ARIMA 處理均值結構,GARCH 處理方差結構,兩者必並用否則低估尾部。
3. **Stationarity 是所有統計推論的地板** — 原始價格是 random walk (non-stationary),必須先差分、log-return、cointegration 等轉換才能套標準工具。忽略 stationarity 檢驗的回測是在浮沙上蓋樓。
4. **ML 的 edge 來自特徵工程而非模型** — RF/XGBoost/LSTM 理論可擬合任何函數,但金融 SNR < 0.1,越複雜越過擬合。真 edge 在找弱但穩定因子 (因子投資、cross-sectional momentum、liquidity),模型只是加權工具。
5. **Walk-forward + Nested CV 是時序 ML 唯一安全驗證** — 傳統 K-fold 在時序會洩漏未來資訊,必須 expanding-window walk-forward,每視窗內再 nested CV 選超參數,否則 hyperparameter selection 本身過擬合。

### 可用戰術/策略
- **Bayesian 勝率評估**:Beta 先驗 + Bernoulli 似然推論真實勝率,取後驗 5th percentile 為下限,仍 > 50% 才放行。
- **Cointegration pair trading**:Engle-Granger / Johansen 找配對,對殘差建 mean-reversion 模型,z-score > 2 且 stationarity 維持時進場。
- **GARCH(1,1) + VaR 部位控制**:GARCH 估計 conditional volatility,risk per trade 動態縮放至 1% VaR;波動率上升自動降槓桿。
- **HMM regime detection**:訓練 2-3 state HMM 偵測 bull/bear/chop regime,策略只在對應 regime 啟動。

### 盲點 / 反例 / 適用邊界
- **模型越複雜,過擬合風險越高而非降低**:書中仍給 Deep Learning 章節,無嚴格 walk-forward 紀律會把 noise 當 signal。
- **MCMC 收斂診斷常被略過**:實戰需檢查 trace plot、R-hat、effective sample size,否則後驗分佈完全錯誤;書中範例偏簡化。
- **適用邊界:能寫 Python/R 且有耐性調參**。散戶無編程盲信 black-box 反而陷阱。

### 與 Edward 既有知識的連結
- 強呼應 **derivative_over_level**:GARCH/ARIMA 處理「變化率的變化率」,stationarity 要求對差分建模,對齊零式一階軸。
- 呼應 **information_asymmetry_action**:Bayesian prior-posterior 更新是「觀察到 edge 才下注」的數學框架;後驗分佈窄 = 有 edge,寬 = 無 edge。
- 銜接 **backtest_methodology / walk_forward**:nested CV + walk-forward 可作為 ZP 回測方法論細則的外部佐證,與 Davey 互補 (Davey 偏流程,Halls-Moore 偏統計嚴謹)。
