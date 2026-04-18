# Market Risk Analysis Vol II: Practical Financial Econometrics — Carol Alexander

### 目錄
1. 核心本質 — 金融實務向的計量：從 factor model 到 copula 的工具箱
2. 可用戰術 — EWMA / PCA / GARCH / Copula / Cointegration
3. 盲點/反例 — 2008 後市場對經典模型的修正
4. 與 Edward 既有知識的連結

### TL;DR
Alexander Vol II (Wiley 2008, 408 頁 8 章) 是四卷《Market Risk Analysis》套書的第二冊，專攻「**實務財務計量**」。八章結構：II.1 Factor Models (single/multi-factor, style attribution, Barra-style)、II.2 PCA (term structure、yield curve)、II.3 Classical vol/correlation (EWMA, RiskMetrics)、II.4 GARCH-family (EGARCH, GJR, IGARCH, MV-GARCH)、II.5 時間序列模型（ARMA, unit root, stationarity）、II.6 共整合 (pair trading)、II.7 Copula models、II.8 Advanced econometric models (Kalman filter, regime-switching, SVM/NN 入門)。全書的區別特色是**每個理論立即配 Excel/MATLAB 案例**——UK 政府公債 yield curve PCA、DJIA 股票 factor model、GBP/USD EWMA 波動率估計等。Alexander 在 Sussex Business School 教風險管理多年，書中融合了她的 JPMorgan RiskMetrics 經歷，是風險管理 quant 面試的高頻參考。

### 核心本質
1. **Factor Model 的三種建構法（II.1.3）**：(a) Fundamental factors（Barra-style，用 P/E、size、industry 當 regressor），(b) Macroeconomic factors（Chen-Roll-Ross 用 GDP、利率、通膨），(c) Statistical factors（PCA / factor analysis 從共變異矩陣反推）。三者各有 trade-off——fundamental 解釋性強但需大量資料；macro 經濟直覺好但只解釋 10-15% 變異；statistical 解釋最多但因子缺經濟意義。Barra model (II.1.5) 結合 (a)+(c)，是業界最常用的 commercial risk model。
2. **PCA on Yield Curve 三因子解釋 95% 變異（II.2.3-II.2.4）**：UK government zero rates PCA 的 Factor 1 = level (平移)、Factor 2 = slope (陡峭化/趨平)、Factor 3 = curvature。前三個累計 explained variance >95%。這是 Litterman-Scheinkman (1991) 的實證重現，直接對應 DV01、duration、convexity 三種 hedging 工具。Ch II.2.5 延伸到 equity——DJIA 30 stock 的 PC1 就是 market factor，第二、三主成分常對應 sector 輪動。
3. **EWMA 的 λ 選擇決定遺忘速度（II.3.8）**：RiskMetrics 原廠 λ=0.94（daily）對應約 30 日 half-life；λ=0.97 對應 75 日半衰期。Alexander 示範在 2008 大崩盤時 λ=0.94 反應快但過度敏感，λ=0.97 穩定但落後。「正確」λ 沒有絕對答案——取決於應用場景：VaR 報告傾向較大 λ（穩定）、交易限額傾向較小 λ（敏感）。
4. **GARCH 家族的選擇（II.4）**：symmetric GARCH(1,1) 適合 FX；asymmetric GJR-GARCH / EGARCH 適合 equity（leverage effect：負回報後波動上升更大）；IGARCH 對 α+β=1 邊界案例；CGARCH 分解短期 + 長期 component。Alexander 強調「no single model dominates」——要在 training window 對比 AIC/BIC 與 out-of-sample VaR violation rate。
5. **Cointegration 與 Pair Trading 機制（II.6）**：Alexander 本人（2001）著作《Market Models》就以 cointegration 為核心。Ch II.6 示範兩個步驟——(a) Engle-Granger residual ADF test，(b) 若 cointegrated，建立 spread = y - β·x，用 Bollinger band 或 Ornstein-Uhlenbeck mean-reversion 時間估計進出場。實務上要過三個門檻：股價 cointegrated、spread 有 significant mean reversion、bid-ask spread < 1/2 expected profit。

### 可用戰術
1. **Style Attribution via OLS（II.1.3.2）**：portfolio return 對多個 index（growth/value/large/small）回歸，殘差就是「純 alpha」、係數就是「style exposure」。Sharpe (1992) 的原版方法。對評估 mutual fund / hedge fund 的風格偏離 benchmark 極有用。
2. **Orthogonal Regression 解 multicollinearity（II.1.4.3）**：Fundamental factor 之間（如 size、value）高度相關，OLS 係數解釋不穩定。Alexander 提出用 PCA 先正交化再回歸，把 loading 投影回原因子。數值更穩定但係數失去「單一特徵」意義。
3. **EWMA Volatility Forecast 一日領先（II.3.8.1）**：σ²_t = λ·σ²_{t-1} + (1-λ)·r²_{t-1}，σ_t 是「t 日收盤後 estimate，用於 t+1 日 VaR」。比 rolling historical 對新資訊反應快；但缺 mean reversion，long-horizon forecast 直接線性外推（h-day σ = √h · σ_daily）會低估極端情境。
4. **Copula 分離 marginal 與 dependence（II.7）**：Sklar 定理——聯合 CDF = C(F_1(x_1), ..., F_n(x_n))，其中 C 是 copula、F_i 是 marginal。Gaussian copula、Student-t copula、Clayton copula（lower tail dependence）、Gumbel copula（upper tail）。實務：用 t-copula 模擬 portfolio loss 比 normal 更好捕捉「同時爆掉」尾部。
5. **Kalman Filter 用於 state-space 估計（II.8.1）**：適用於 dynamic factor loading（β 隨時間變動）、implied volatility surface calibration、latent regime detection。Alexander 示範用 Kalman filter 追蹤 CAPM 的 time-varying beta——2008 金融股 β 從 1.0 飆到 1.8 的現象即被捕捉。

### 盲點/反例
1. **2008 出版恰好趕上金融危機**：書中部分案例（如 2006-2007 的「low vol, low corr」環境）在實務上被 2008 打臉——Gaussian copula 在信用衍生品應用普遍失效（Salmon 2009 Wired 文章）、CDS 市場流動性枯竭讓 cointegration 破裂。後續新版需補 jump diffusion + tail copula。
2. **Machine Learning 章節（II.8.6-7）過時**：SVM + feedforward NN 只有 3 頁，2015 後 XGBoost、deep learning 成為 factor model 的主流，這本未觸及。補 Kelly-Xiu（Round 1）或 Géron（本輪）。
3. **HFT 與 intraday 模型缺席**：書中所有例子都是 daily/weekly，沒 5-min bar、沒 tick-level、沒 limit order book model。做 market making 或 intraday arb 要補 Aldridge《High-Frequency Trading》（Round 1）或 Cartea-Jaimungal《Algorithmic and High-Frequency Trading》。
4. **Excel/MATLAB 為主，Python 缺席**：2008 年 pandas 還沒流行，書中 code 都是 Excel spreadsheet 或 MATLAB script。現代讀者要自己 port 到 Python statsmodels + numpy。
5. **英國學院派偏向理論呈現**：某些章節（如 II.4.3 EGARCH 推導）過於詳盡，實務 quant 可直接用 arch package 跳過。相對地缺 operational 議題（how to deploy in production、monitor model drift）。

### 與 Edward 既有知識的連結
- **對照 Tsay 系列 (Round 1 + 本輪)**：Tsay 是學術經典（理論推導嚴謹），Alexander 是實務視角（Excel/MATLAB 直接可跑）。同樣的 GARCH/cointegration 從兩個角度切入，概念互補。
- **對照 Wooldridge（本輪）**：Wooldridge 教 identification 與標準推論；Alexander 跳過 identification 直接說「how to use the model」。兩本搭配：理論從 Wooldridge、實作從 Alexander。
- **對照 Engle《Systemic Risk in Europe》（Round 1）**：Engle 自己發明 GARCH、SRISK，Alexander 把 Engle 的方法整合進 commercial risk framework。兩者技術根源相同但取向不同——Engle 做學術測量，Alexander 做業務應用。
- **對照 ZP/risk_model 架構**：Alexander Ch II.1.6 Tracking Error 計算正是我 ZP portfolio 績效評估需要的工具——ex-post vs. ex-ante 的區分特別重要，實現績效≠預期績效時必須兩者都看。
- **對照 Poker 的 variance control**：撲克的 tournament stack management 本質上是 VaR + tracking error 的聯合優化——既不要一次 all-in 爆掉（downside VaR），也不要保守到追不上 blind up（跟不上 benchmark tracking error）。Alexander Ch II.1.6 的 active risk 框架提供量化語言。
