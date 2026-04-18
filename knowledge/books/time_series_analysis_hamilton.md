## Time Series Analysis — James D. Hamilton (1994)
**來源**: Princeton University Press canonical  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- 第 1-3 章 difference equations、lag operator、stationary ARMA、forecasting ARMA
- 第 4-5 章 MLE、asymptotic distribution theory
- 第 6 章 Spectral analysis（power spectrum、periodogram、cyclical decomposition）
- 第 7 章 Asymptotic Distribution Theory
- 第 8-9 章 Linear regression review、linear systems of simultaneous equations
- 第 10 章 Covariance-stationary vector processes（VAR、Wold decomposition）
- 第 11 章 Vector Autoregressions（estimation、testing、Granger causality、IRF、variance decomposition）
- 第 12 章 Bayesian analysis
- 第 13 章 Kalman filter（state-space representation、MLE via Kalman）
- 第 14-15 章 GMM、models with heteroskedasticity (GARCH)
- 第 16 章 Nonstationary time series
- 第 17-18 章 Unit root (ADF, Phillips-Perron)、unit roots in multivariate (Johansen)
- 第 19 章 Cointegration
- 第 20 章 Full-Information Maximum Likelihood Analysis
- 第 21 章 Monte Carlo methods
- 第 22 章 Modeling time series with changes in regime（Markov-switching）

### TL;DR (≤120字)
Hamilton 1994 是時序計量經濟學公認最權威單冊，800 頁。比 Tsay 廣（Bayesian、Markov-switching、FIML）、比 Enders 深。對交易者特別重要：第 13 章 Kalman filter、第 17-19 章 unit root + cointegration（stat arb 根基）、第 22 章 Markov-switching（regime model 原文）。寫法極嚴謹（每定理有證明），適合研究生而非初學；實作需自行 R/Python porting。

### 核心本質 (3-5 條)
1. **Wold decomposition = 任何 stationary 序列 = deterministic + MA(∞)（本質，第 4.7 節）** — 理論根基告訴你：任何 stationary 序列都有 MA 表達式；也就是 ARMA 的存在基礎。
2. **Kalman filter 是 state-space 通用引擎（本質，第 13 章）** — 把 ARMA、unobserved component、time-varying parameter、stochastic volatility 通通寫 state-space，用 Kalman 算 likelihood → MLE。金融動態模型黃金工具。
3. **Unit root 判斷走哪條路（本質，第 17 章）** — I(0) → 普通 ARMA；I(1) → differencing 後 ARMA；I(1) + cointegration → VECM。ADF、Phillips-Perron、KPSS 是三大 unit root test。
4. **Markov-switching 處理 regime change（本質，第 22 章）** — S_t ∈ {1,...,K} latent state 按 Markov chain 轉移；參數 θ_{S_t} 依狀態改。金融 bull/bear regime 經典應用；作者 1989 JPE 原論文也在此書。
5. **GMM 比 MLE 對分布錯設更穩健（本質，第 14 章）** — MLE 需知道真實分布；GMM 只需 moment condition。當分布未知（金融 fat-tail）優先 GMM。

### 可用戰術/策略
- **Markov-switching GARCH**：2 state（low-vol/high-vol）的 GARCH；transition prob 矩陣刻劃 regime 轉換頻率。實作 Hamilton filter + EM。
- **VECM for currency triangle**：EUR/USD、GBP/USD、EUR/GBP 三角 cointegration；Johansen 測 rank=1，VECM 估速回率，stat arb。
- **Kalman for stochastic volatility**：log(σ²_t) = μ + φ log(σ²_{t-1}) + η_t；state-space + Kalman 得 MLE 估計（相較 MCMC 快）。
- **Granger causality for lead-lag**：VAR(4) 估 VIX → S&P，F-test VIX 滯後對 S&P 顯著性；發現 VIX 週領先 S&P 數日。
- **FIML for structural model**：三方程總體模型（GDP、利率、股價）聯立估計，比分別 OLS 更 efficient。

### 盲點 / 反例 / 適用邊界
- **1994 出版，fractional + long-memory 未重**：FIGARCH、Long-memory models 在此書邊緣；需 Beran/Baillie 補。
- **機器學習缺**：本書純 econometric；ML + TS（Prophet、LSTM、Transformer）需 Hyndman/Goodfellow/Murphy 補。
- **Multivariate GARCH 僅一節**：DCC/BEKK 僅略提；需 Bauwens et al. 2006 專書。
- **計算重**：很多章節需 heavy numerical optimization；不給 code，MATLAB/R 得自寫。
- **Bayesian 章淺**：第 12 章只是導入；深入需 West-Harrison 或 Rachev。

### 與 Edward 既有知識的連結
- **對齊 ZP dynamic alpha**：Kalman filter + Markov-switching 是「state-aware 策略」雙核；Edward 可直接實作為 `ZP/quant/regime/{kalman, markov_switching}.py`。
- **延伸 Tsay (Round 1)**：Tsay 偏 financial TS 應用；Hamilton 偏 theory + macro。兩書並讀完整。
- **衝突點**：Hamilton 假設 well-behaved asymptotic；Lo-MacKinlay 等人強調 fat-tail 下失效。Edward 實戰先假設 Hamilton，失效退 simulation-based。
- **可挖金礦**：第 22 章 Markov-switching EM 演算法可直接實作 regime filter；2019 年後 RegimeAware trading 的基礎。
- **對接 Box-Jenkins**：BJ 1976 是源頭；Hamilton 1994 是集大成；Hyndman 2021 是現代化 re-presentation。三書線性遞進。
