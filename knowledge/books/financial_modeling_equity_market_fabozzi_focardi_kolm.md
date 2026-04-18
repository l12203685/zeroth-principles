# Financial Modeling of the Equity Market: From CAPM to Cointegration — Fabozzi, Focardi, Kolm

### 目錄
1. 核心本質 — 股市建模的全景：從 mean-variance 到 cointegration pair
2. 可用戰術 — 風險調整、higher moments、transaction cost 整合
3. 盲點/反例 — 2008 後的新架構未涵蓋
4. 與 Edward 既有知識的連結

### TL;DR
Fabozzi-Focardi-Kolm (Wiley 2006, 約 17 章) 是 Yale 的 Fabozzi (編纂過 50+ 本 fixed income 教科書)、NYU Polytechnic 的 Focardi、Courant Institute 的 Kolm 三位聯手編的 equity market quant modeling 綜述。**結構**：Part I Portfolio Allocation（Ch 2-6 classical Markowitz + modern extensions 含 transaction cost、higher moments、mathematical optimization）、Part II Managing Uncertainty（Ch 7-9 equity price model, expected return forecasting, estimation risk）、Part III Advanced Portfolio Management（Ch 10-12 Robust optimization, Bayesian, re-sampling, simulation）、Part IV Equity Derivatives & Hedging（Ch 13-14）、Part V Cointegration & Trading Strategies（Ch 15-17 pair trading, statistical arbitrage, momentum）。**核心定位**：這本是連接「PhD academic framework」與「institutional practitioner tool」的橋樑——書中對每個模型都同時給 mathematical derivation + implementation issue + empirical evidence。**特別有用章節**：Ch 3 Transaction Cost（Almgren-Chriss framework）、Ch 5 Higher Moments（Markowitz mean-variance 不夠抓到 skewness/kurtosis）、Ch 10 Robust Optimization（Ledoit-Wolf shrinkage, worst-case analysis）、Ch 15-17 Cointegration（pair trading 的嚴謹框架）。

### 核心本質
1. **Markowitz Mean-Variance 的限制（Ch 2-5）**：Markowitz 1952 mean-variance 假設 (a) 報酬率 joint normal、(b) 投資人只關心 μ,σ²、(c) 已知 parameters。全部在實務上失敗——股票報酬有 fat tails + skew、投資人有 loss aversion + higher-moment preference、parameter estimate 有大 estimation error。Ch 5 的 higher moments（skewness, kurtosis）與 downside risk measure（CVaR、LPM）把框架從 two-moment 擴到 four-moment+。
2. **Transaction Cost 必須整合進 optimization（Ch 3）**：傳統 mean-variance 假設無摩擦，實務上 TC 可吃掉 50+ bps alpha。Ch 3 示範把 market impact 作為 quadratic penalty 加入 objective：min w^T Σ w - λ·μ^T w + γ·|w - w_0|^T |w - w_0|。對 rebalance frequency 與 turnover 都有約束。書中提供 closed-form solution（linear TC）與 QP solution（quadratic TC）。
3. **Estimation Risk 比 Sample Risk 大（Ch 10）**：Ledoit-Wolf (2003) 顯示 historical covariance matrix Σ̂ 的 max eigenvalue 方向誤差最大——MV optimizer 偏向把重倉放到「最大估計 Sharpe ratio」，這正是 estimation error 最 blown up 的地方。Ledoit-Wolf shrinkage (λ·I + (1-λ)·Σ̂) 降低 estimation noise；Michaud (1998) 的 portfolio resampling 提供另一條路。
4. **Cointegration-Based Pair Trading 是 Equity Stat Arb 的理論根基（Ch 15-17）**：兩個 I(1) 股價若 cointegrated 則 spread = A·P_A - B·P_B 是 I(0) mean-reverting。Vidyamurthy (2004) 的三步驟——(a) Johansen test 識別 pair，(b) 估計 OU process 決定 mean-reversion speed，(c) Bollinger band 或 optimal stopping theory 決定進出場。Ch 17 給 explicit code workflow。
5. **Factor Model 統一 Alpha 與 Risk（Ch 8）**：r_i = Σ β_{i,k}·f_k + α_i + ε_i，其中 f_k 是 observable (macro factor) 或 latent (PCA factor)。α_i 是「真 alpha」，β 是 risk exposure。Fundamental law of active management 把 IR = IC·√breadth，在 factor model 內可精確拆解——哪些是 factor alpha (common)，哪些是 specific alpha (idiosyncratic)。

### 可用戰術
1. **Robust Optimization with Box/Ellipsoidal Uncertainty（Ch 10）**：μ ∈ box [μ̂ - δ, μ̂ + δ] 的 worst-case minmax optimization 給出比 Markowitz 更保守但 stable 的 weight。TurkQuant 等機構實證 post-2008 period outperform naive mean-variance。
2. **Black-Litterman Posterior Blending（Ch 11）**：市場 implied equilibrium return π (by reverse optimization) 當 prior，manager view q = P·μ + ε 當 data，posterior = Ω^{-1}(Ω_prior·π + P^T·Ω_view^{-1}·q)。輸入只需 view 的相對 strength（not absolute），實務遠比 raw mean-variance stable。
3. **Partial Cointegration Analysis（Ch 15.4）**：完全 cointegration 很難在 equity 上實現，Vidyamurthy 用 partial cointegration——spread 有 slow mean-reversion 但非 stationary。用 Ornstein-Uhlenbeck fit + half-life 估 mean-reversion speed，half-life <30 days 即可 trade。
4. **CVaR-Optimal Portfolio via LP（Ch 5）**：Rockafellar-Uryasev (2000) 把 CVaR 最小化轉成 linear programming：min w,α,z  α + (1/(1-β)T)·Σ z_s subject to z_s ≥ -w^T r_s - α, z_s ≥ 0。只需 scenario return，不需分布假設。適合 tail-risk 管理。
5. **Random Matrix Filter for Covariance（Ch 8）**：empirical covariance matrix 的 eigenvalue 很多落在 Marchenko-Pastur band 內（純噪聲）。Plerou et al. (2002) 把 band 內 eigenvalue 設為 mean value（去噪），band 外保留。實證 filtered covariance 做 MV optimization 比 raw 穩定 30%+。

### 盲點/反例
1. **2006 出版，post-2008 reform 未涵蓋**：Dodd-Frank、SEC Reg NMS、HFT 普及、dark pool、maker-taker fee、meme stock era 都在書後發生。對 current market 適用性打折。
2. **線性 factor model 主導，ML 缺席**：所有 factor model 都是 linear regression 類型，沒 neural net、XGBoost。Kelly-Xiu《Financial ML》（Round 1）顯示 nonlinear factor model R² 高 2-3x。
3. **Equity 特化，缺 cross-asset**：書名 From CAPM to Cointegration 基本聚焦美國 equity；debt vs. equity allocation、commodity、currency 應用有限。做 global macro 或 multi-asset 策略要補其他書。
4. **PhD-heavy，可讀性中等**：約一半章節是數學推導，非 PhD 讀者需跳讀。Practitioner 可直接看 summary + example + code，skip proof。
5. **Focardi 2016 去世**：Fabozzi 高齡 75+ 仍出新書，但 Focardi 的 mathematical rigor 缺失後續版本品質下降。最新 Handbook of Finance 系列比這本更新但深度不一。

### 與 Edward 既有知識的連結
- **對照 Qian-Hua-Sorensen《Quantitative Equity Portfolio Management》（本輪）**：Qian 是 practitioner 視角（多 fund manager 實戰例），Fabozzi-Focardi-Kolm 是 academic + practitioner 混合。Qian 給「怎麼跑」，FFK 給「為什麼這樣跑」。
- **對照 Gibson《Asset Allocation》（Round 1）**：Gibson 是 high-level asset class allocation（strategic），FFK 是 within-equity 的 detailed portfolio construction（tactical）。兩個 layer 互補。
- **對照 Vince《Handbook of Portfolio Math》（Round 1）**：Vince 強調 geometric mean + optimal f，FFK 涵蓋 utility-based + Bayesian + robust optimization。Vince 偏 futures trader，FFK 偏 equity long-only + long-short。
- **對照 Pole《Statistical Arbitrage》（Round 1）**：Pole 專注 stat arb 實作，FFK Ch 15-17 給 stat arb 的學術基礎（cointegration theory + OU process）。兩者合在一起是 pair trading 完整教學。
- **對照 ZP/equity 策略**：若我 ZP 要加 equity stat arb branch，FFK Ch 15-17 是理論起點——先 Johansen test 篩對、再 OU fit 估 mean-reversion speed、再 OLS hedge ratio 決定 position sizing。實作可用 statsmodels.tsa.vector_ar.vecm.VECM 與 scipy.stats.pearsonr.
- **對照 Poker 的 stack-utility relationship**：poker tournament 的 ICM 本質上是 non-linear utility function（winning $100 from 1k = 10% stack vs from 10k = 1% stack 心理價值不同），FFK Ch 2.6 的 utility function framework 完全適用。頂級 poker player 用 ICM calculator 像 FFK 讀者用 CVaR optimizer。
