## Analysis of Financial Time Series, 3rd Edition — Ruey S. Tsay
**來源**: E:/課程/[5] 時間序列/Analysis of Financial Time Series, 3ed, 2010, Ruey S. Tsay.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Financial Time Series and Their Characteristics
- Ch2 Linear Time Series (ARMA, ARIMA, unit root)
- Ch3 Conditional Heteroscedastic Models (GARCH family)
- Ch4 Nonlinear Models (TAR, STAR, Markov switching)
- Ch5 High-Frequency Data Analysis and Market Microstructure
- Ch6 Continuous-Time Models (GBM, Ito, jump diffusion, Merton, Heston)
- Ch7 Extreme Values, Quantiles, and Value at Risk (EVT, POT)
- Ch8 Multivariate Time Series (VAR, cointegration, VECM)
- Ch9 Principal Component Analysis and Factor Models
- Ch10 Multivariate Volatility Models (DCC, BEKK)
- Ch11 State-Space Models and Kalman Filter
- Ch12 Markov Chain Monte Carlo Methods

### TL;DR (≤120字)
Tsay 教科書是金融時序分析的 de facto 標準——從 ARMA 到 GARCH 到 Kalman 到 MCMC 一本打通。第 3 版加入 Realized Volatility、DCC multivariate、Stochastic Volatility 的 MCMC 估計，把 10 年前還在 research paper 的工具變成標準教材。

### 核心本質 (3-5 條)
1. **Stylized Facts of Financial Returns**（第 1 章） — Tsay 歸納金融時序五大經驗事實：(1) return 無自相關但 |return| 有強序列相關（volatility clustering）；(2) fat tail；(3) 波動率長記憶；(4) leverage effect；(5) 多資產相關性時變。任何模型都必須 capture 這些才有實用價值。
2. **GARCH 是 volatility modeling 的最小共通語言**（第 3 章） — GARCH(1,1) 用 3 個參數 capture 波動率 clustering，成為期權定價、VaR、portfolio optimization 的基本工具。EGARCH/TGARCH 處理 leverage effect，IGARCH 處理波動率近單根性質。
3. **Cointegration 是 Pair Trading 的理論基石**（第 8 章） — 兩個非平穩序列的線性組合若平穩，即為 cointegrated；long-run equilibrium 提供 mean-reverting 交易機會。Johansen test 可同時檢定多變量 cointegration rank。
4. **EVT for Tail Risk**（第 7 章） — 傳統 VaR 假設 Normal 嚴重低估 tail；EVT 的 POT 方法用 Generalized Pareto 分布 fit tail，更準確估計 99%/99.9% quantile。
5. **State-Space + Kalman 是時變參數通用框架**（第 11 章） — 當模型參數時變（regime switching、time-varying beta、vol），state-space representation + Kalman filter / smoother 提供統一估計框架。

### 可用戰術/策略
- **GARCH(1,1) Volatility Forecast**：rolling window 估計 GARCH 參數，做 1-step 到 20-step ahead forecast；用於期權 implied vs realized spread 策略。
- **ADF + Johansen Pair Selection**：掃描同產業股票對，ADF 確認單根，Johansen 檢定 cointegration；選 test statistic < -3.5 的 pair 做 trading universe。
- **POT VaR**：用 past 1000 days 以 95% quantile 為 threshold fit GPD，產生 99.5% VaR 估計；Christoffersen test 檢定 breach 獨立性。
- **DCC Portfolio**：multivariate GARCH 估計時變 correlation matrix，每月 rebalance minimum-variance portfolio；correlation regime shift 時比 static covariance 穩健。
- **Kalman Filter for Time-Varying Beta**：CAPM β_t 當 state variable 做 filtering，用於風險管理與避險比率動態調整。

### 盲點 / 反例 / 適用邊界
- **線性模型主導的偏見** — 大半篇幅是 ARMA/GARCH 變體；當前 deep learning / LSTM / Transformer 完全未涵蓋。
- **2010 年出版部分方法過時** — Realized Volatility 用 5-min sampling；當前 microsecond-level tick data 的 HF estimators（Realized Kernel、Pre-Averaging）是新標準。
- **假設金融市場穩態** — GARCH 及 cointegration 假設長期參數穩定；2008 後多次 regime change 讓模型在 structural break 時失效。
- **R 程式碼分散** — 當代讀者用 `rugarch` / `rmgarch` / `urca` 等 package 更輕鬆，書中手工 code 學習成本高。

### 與 Edward 既有知識的連結
- **ZP quant finance 基礎教材**：所有 strategy 建構都建立在其 stylized facts 與 volatility modeling 基礎上。
- **延伸 Bayesian Methods**：第 12 章 MCMC 與 Rachev《Bayesian Methods in Finance》直接銜接。
- **對應 Statistical Arb**：第 8 章 cointegration + VECM 是 Pole《Statistical Arbitrage》的理論基礎。
- **衝突 Kelly-Xiu ML**：Tsay 偏 interpretable model + economic theory，Kelly-Xiu 偏 black-box ML；Edward 應兩路並行。
- **可挖金礦**：第 7 章 EVT 可直接作為 `ZP/risk/tail_risk/` 模組基礎；第 10 章 DCC 可作為 multi-asset portfolio 的時變 correlation 估計標準。
- **學術傳承**：Tsay 是芝加哥大學與 Academia Sinica 高頻金融聯合項目主導人，代表芝加哥學派在金融計量的共識。
