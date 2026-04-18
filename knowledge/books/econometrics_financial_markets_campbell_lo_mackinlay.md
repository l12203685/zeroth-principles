# The Econometrics of Financial Markets — Campbell, Lo, MacKinlay (CLM)

### 目錄
1. 核心本質 — 金融經濟學的計量聖經，從 EMH 到衍生品皆有
2. 可用戰術 — Variance Ratio / Event Study / Factor Model / SDF
3. 盲點/反例 — 2008 後學術共識的修正
4. 與 Edward 既有知識的連結

### TL;DR
CLM (Princeton 1997, 611 頁 12 章 + 4 個 GMM/IV 附錄) 是金融經濟學博士班標準教科書，涵蓋範圍比任何其他書都廣：Ch 1-2 market efficiency + random walk tests、Ch 3 market microstructure、Ch 4 event-study、Ch 5-6 CAPM + multi-factor models、Ch 7 present-value relation (Campbell-Shiller 分解)、Ch 8 intertemporal equilibrium (SDF, Hansen-Jagannathan bound)、Ch 9 derivative pricing、Ch 10-11 fixed income term structure + affine-yield models、Ch 12 nonlinearity (ARCH/GARCH、neural net、kernel regression、overfitting/data snooping)。三位作者本身都是 Harvard/MIT/Wharton 的大牛，整本書把 1970-1995 的金融實證研究整合成一套 coherent econometric framework。**核心思想**：金融資料有三個特殊性——(1) 均值極小相對於變異（signal/noise 1:100）、(2) 非定常（regime shifts）、(3) 非高斯（fat tails）——所有標準計量工具必須針對這三點做修正。

### 核心本質
1. **Market Efficiency 的三個版本（Ch 1.5, 2.1）**：CLM 用 Random Walk 1 (IID increments)、RW2 (independent but non-identically distributed)、RW3 (uncorrelated increments only) 把 Fama 1970 的 Weak/Semi-Strong/Strong 三分法精細化。Ch 2.4.3 的 Variance Ratio Test (Lo-MacKinlay 1988) 檢驗 RW3：若 returns uncorrelated 則 Var(r_k)/k = Var(r_1)，否則比例偏離 1。實證：US equity weekly returns 的 VR(2) ≈ 1.3，拒絕 RW3，但效應量小。
2. **市場微結構引入 non-trivial dynamics（Ch 3.1-3.2）**：Nonsynchronous trading 會產生 spurious autocorrelation（Lo-MacKinlay 1990）——portfolio 的 autocorrelation 約 20-30% 但來自資產間成交時間差而非真預測性。Bid-ask bounce（Roll 1984）造成一階負自相關 ρ_1 = -s²/4σ²，實務估計 effective spread 的經典方法。
3. **Event Study 的事件窗 & normal performance model（Ch 4.1-4.4）**：Brown-Warner (1985) event study 法的標準流程——估計窗 (-250 to -20 trading days) 擬合 market model，事件窗 (-10 to +10) 計算 abnormal return CAR = Σ(r_it - α̂_i - β̂_i r_mt)。用於併購、分割、盈餘公告等 corporate event 實證。統計力量依賴 event day precision——若 event 是連續事件，summed variance 會 explode。
4. **CAPM / Multi-Factor Models 的檢定（Ch 5-6）**：GRS test (Gibbons-Ross-Shanken 1989) 檢定 zero alpha 虛無假設，T²/F distribution。實證上 US equity 市場的 Fama-French 3-factor（market, SMB, HML）把 CAPM 的 alpha 顯著壓下；Carhart (1997) 加 momentum 為第四因子。Ch 6.4 討論「多少個 factor」——statistical 方法 (PCA, factor analysis) vs. theoretical 方法 (macro variables 如 Chen-Roll-Ross 1986)。
5. **Present-Value Relation 與股價波動之謎（Ch 7）**：Campbell-Shiller (1988a, 1988b) 的 log-linear 分解：股價超額波動 = future dividend growth variation + future return variation。US 長期資料顯示 60-75% 股價變異來自 expected return 變動（discount rate shocks），只 25-40% 來自 cash flow 變動。這徹底顛覆「股價反映未來股息」的直覺。

### 可用戰術
1. **Variance Ratio with heteroscedasticity-robust SE（Ch 2.4.3 eq 2.4.44）**：Lo-MacKinlay 的 M*_c 統計量對 ARCH / Heteroscedasticity 穩健，是實務檢定 mean-reversion 的首選。用在 index vs. individual stocks 可比較 aggregation level 的預測力差異。
2. **Long-horizon regression 搭配 overlapping return（Ch 2.5, 7.2.1）**：用 5-year overlapping return 對 D/P 回歸，R² 在 US 資料達 0.3+（Fama-French 1988）。但要注意 standard error 計算需用 Hodrick (1992) 或 Newey-West with lag=k（否則 Type I error 嚴重膨脹）。
3. **Hansen-Jagannathan bound 篩選 SDF candidates（Ch 8.1.1）**：任何 candidate stochastic discount factor m 必須滿足 σ(m)/E(m) ≥ |Sharpe_max|。US 1947-93 max Sharpe ratio 約 0.5，所以 SDF 的 volatility/mean 必須 >0.5。這把 representative agent CCAPM 釘在牆上——power utility 要 γ>50 才能達到。
4. **Implied Volatility 從 option market 反解（Ch 9.3.5）**：BSM 的 σ 是唯一 unknown parameter，given option price 可反推 implied σ。實務上 VIX = 30-day S&P 500 OTM option 加權平均 IV。Ch 9.3.6 提 stochastic volatility model (Hull-White, Heston) 對 IV smile/skew 提供經濟學解釋。
5. **Kernel Regression 估計 state-price density（Ch 12.3.4）**：Ait-Sahalia-Lo (1998) 用 option price 的 nonparametric kernel regression 反推 risk-neutral density，然後與 historical return distribution 比較得到 pricing kernel。這是 nonparametric asset pricing 的奠基方法。

### 盲點/反例
1. **1997 年出版，沒涵蓋 2000+ 的重大進展**：behavioral finance（Shleifer, Barberis）、limit to arbitrage、noise trader risk、low vol anomaly、quality factor、Q-factor model (Hou-Xue-Zhang)、Stambaugh 的 mispricing model 都未涵蓋。ZP 若做現代 factor investing 必須補 Ang《Asset Management: A Systematic Approach》（Ilmanen 也值得讀）。
2. **市場微結構只到 1990s 紙帶交易**：Ch 3 討論的都是 Specialist/NYSE 架構；現代電子交易、HFT、dark pool、iceberg order、NBBO 全缺失。補 Harris《Trading and Exchanges》或 O'Hara《Market Microstructure Theory》。
3. **Derivative pricing 只到 BSM + simple stochastic vol**：Ch 9 沒涵蓋 local volatility (Dupire 1994)、LIBOR market model (BGM 1997)、SABR (Hagan et al. 2002)、variance swap replication (Carr-Madan 1998)。做 vol arb 必須補 Brigo-Mercurio（Round 1）或 Derman《Volatility Smile》。
4. **Machine Learning 只停在 neural net 入門（Ch 12.4）**：1990s 的 MLP + projection pursuit，沒 deep learning、XGBoost、transformer。Ch 12.5 的 overfitting/data snooping 警告是前瞻但沒給可操作的 false discovery rate 工具。
5. **2008 後的 systemic risk 完全缺失**：CLM 沒 CoVaR、SRISK、SES、MES 等 systemic risk 測度；沒 quant crash 2007、flash crash 2010、LDI crisis 2022 這類 non-IID 事件的處理。

### 與 Edward 既有知識的連結
- **對照 Greene《Econometric Analysis》（本輪）**：Greene 是「通用計量」教科書，CLM 是「金融計量」專論。CLM 附錄 A 專門講 GMM/IV，與 Greene Ch 13 重疊。讀 CLM 遇到 GMM 細節翻 Greene 補。
- **對照 Tsay《Multivariate Time Series》（本輪）**：Tsay 做 VAR/VECM 細節，CLM Ch 11.1 做 affine-yield model（Vasicek, CIR, 雙因子）——都是「結構化 VAR」的不同視角。CLM 的 7.2.3 用 VAR 做 long-horizon predictability 也與 Tsay 技術互通。
- **對照 Kelly-Xiu《Financial Machine Learning》（Round 1）**：Kelly-Xiu 是 CLM Ch 12 + data snooping 的「ML 版本」——把傳統因子回歸升級為 penalized regression、neural net、autoencoder。Kelly 本人是 CLM 的徒孫輩（Cochrane 門生）。
- **對照 ZP/finance/asset_pricing 模組**：CLM Ch 8 SDF 是 ZP asset pricing 支柱——任何「為何這個資產報酬率應該是 X%」的問題回到 E[m·R]=1 這個基本等式。我還沒系統整理 SDF 框架進 ZP，應補一份 `sdf_framework.md`。
- **對照 Poker 的 ICM (Independent Chip Model)**：ICM 本質上是「tournament chip 不是 cash 的等價轉換」，對應 CLM Ch 8 的「non-traded income 破壞 SDF linearity」。撲克錦標賽 bubble 附近的 ICM pressure 與宏觀的 marginal utility 非線性是同樣的數學現象。
