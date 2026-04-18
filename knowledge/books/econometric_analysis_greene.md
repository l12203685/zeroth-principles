# Econometric Analysis (7ed) — William H. Greene

### 目錄
1. 核心本質 — 計量經濟學是「識別因果」而非「預測」的技藝
2. 可用戰術 — OLS/IV/GMM/Panel/MLE 的使用時機
3. 盲點/反例 — 計量方法在金融實務上的失效
4. 與 Edward 既有知識的連結

### TL;DR
Greene 7ed (Pearson 2012, 1241 頁 21 章 + 6 附錄) 是北美 PhD 計量的標準教科書，骨架分六部：Part I 線性回歸 (Ch 1-8)、Part II 廣義回歸 (Ch 9-11)、Part III 估計方法論 (GMM/MLE/Bayesian，Ch 12-16)、Part IV 離散選擇 (Ch 17-19)、Part V 時間序列 (Ch 20-21)、Part VI 矩陣與漸近理論。全書的**哲學核心**是 Chapter 1 第 41 頁開宗明義的一句：「**the paradigm of econometrics is the identification of causal effects, not merely prediction**」——OLS、GLS、2SLS、GMM、FE/RE panel、probit/logit、Heckman、ARIMA/VAR 都是圍繞這個目標展開的工具。Ch 8 的內生性 / 工具變數是全書的精神主軸：當 E[ε|X]≠0 時，OLS 怎麼失效、工具變數怎麼救回一致性、弱工具如何拖垮推論。對 quant 投資來說最關鍵的不是預測精度，而是 Chapter 19-21 的選擇偏差、存活偏差、單根與共整合。

### 核心本質
1. **內生性是計量真正的敵人（Ch 8.1-8.2）**：Greene 列出四大根源——omitted variables、feedback effects、dynamic effects、endogenous sample design。每一項都讓 OLS 變得 inconsistent 不僅 biased。Job Training Partnership Act 示範 self-selection 如何讓「訓練提高薪資」的回歸係數失去因果意義；Ashenfelter-Krueger (1994) 用 twin data 的 measurement error 示範 attenuation bias。金融版本：以事後的 mutual fund 樣本估「選股能力」必然高估，因為爆倉的基金已從資料庫刪除（survivorship bias，Ch 8 Attrition）。
2. **Gauss-Markov 定理只在四個假設齊備時成立（Ch 2.3）**：Linearity / Full Rank / Spherical Disturbances (homo + no autocorr) / Exogeneity。違反任一項 OLS 都不再是 BLUE。這個教條重要到 Ch 9-11 整個 Part II 都在討論如何修補：heteroscedasticity 用 robust SE 或 GLS、autocorrelation 用 Newey-West、endogeneity 用 IV/GMM、panel data 用 FE/RE 控制不可觀測異質。
3. **GMM 是「統一框架」而非單一估計法（Ch 13）**：Hansen (1982) 的 GMM 把 OLS、IV、2SLS、MLE 全部視為「選不同 moment condition」的特例。當你有比參數更多的工具變數，over-identifying restrictions 可用 J-test 檢驗模型設定。對 asset pricing 極有用——Euler equation m(θ)E[R]=1 本身就是 moment condition。Hansen-Singleton (1982) 的 CCAPM 就是 GMM 最早的成功應用。
4. **Weak Instruments 比無工具變數更危險（Ch 8.7）**：弱工具會讓 2SLS 的 bias 接近 OLS，但 SE 膨脹讓統計顯著性消失——看似「沒結果」其實是 sample 不夠。Staiger-Stock (1997) 的 first-stage F-statistic > 10 門檻、Stock-Yogo critical values 是標準診斷。金融應用裡任何聲稱「用 lag 當 IV」的論文必須先跑 F-test。
5. **時間序列的「非定常」是另一個內生性（Ch 21）**：兩條獨立 random walk 的迴歸可以得到 R²>0.9 + t-stat>5 的虛假顯著（spurious regression, Granger-Newbold 1974）。單根檢定 (ADF/Phillips-Perron) 與共整合 (Engle-Granger, Johansen) 是金融統計套利 pair trading 的理論根基——不 cointegrated 的 pair 不能 mean-revert。

### 可用戰術
1. **先做 Hausman Test 再決定 FE vs. RE（Ch 11.5）**：Panel data 時，Fixed Effects 消除所有 time-invariant 變數但允許個體特質與 regressor 相關；Random Effects 假設 E[c_i|X]=0 但獲得效率。Hausman test 的虛無假設是「RE 一致」，拒絕就用 FE。實務上做風險模型的 cross-sectional regression (Fama-MacBeth) 其實是 FE 的變形。
2. **Robust SE + Cluster（White 1980 / Ch 9.4）**：Heteroscedasticity-consistent covariance matrix 不需知道異變結構，只用 OLS 殘差估計 (X'X)^{-1}X'diag(ε²)X(X'X)^{-1}。在 panel 上要 cluster by firm 或 time——Petersen (2009) 在 RFS 指出，不 cluster 的話金融 panel 的 SE 會被嚴重低估。
3. **Newey-West lag 長度 = ⌊T^{1/4}⌋（Ch 20.5）**：HAC 估計量的 bandwidth 選擇沒有唯一答案，但 Newey-West (1987) 建議 truncation lag = 0.75*T^{1/3} 或 Stock-Watson 的 T^{1/4}。在 monthly 30 年的 return 回歸上大約是 4-5 lag。
4. **Probit/Logit 邊際效果≠係數（Ch 17.3）**：Discrete choice 的 coefficient 只有符號有意義，必須用 marginal effect at mean 或 average marginal effect 才有直觀解讀。預測「公司違約機率」時用 logit 而不是 OLS on default dummy（LPM 會產生 <0 或 >1 的預測）。
5. **Cointegration 檢定 + ECM（Ch 21.4-5）**：兩個 I(1) 序列若 Y-βX = I(0)，則 long-run 的 cointegrating vector 就是 β。Error Correction Model y_t = αZ_{t-1} + γ(y_{t-1} - βX_{t-1}) + ε 同時告訴你長期均衡與短期調整速度——用在股價配對、FX carry trade 都有效。

### 盲點/反例
1. **全書以 iid 或弱相依為基本假設，無法應付厚尾**：Greene 偶爾提及 robust regression 與 Huber-White，但沒深入 extreme value 或 copula。對衍生品定價與尾部風險估計，必須補 McNeil-Frey-Embrechts《Quantitative Risk Management》。
2. **Bayesian 只有 Ch 16 淺嘗**：Greene 的 Bayesian chapter 停在 conjugate prior + Gibbs sampling 的入門，缺 MCMC diagnostics、HMC、Bayesian Model Averaging 等現代工具。做 regime-switching 模型與參數不確定性建模時要補 Rachev《Bayesian Methods in Finance》（Round 1）。
3. **Machine Learning 完全缺席**：7ed 2012 年出版，沒有 cross-validation、regularization (Ridge/Lasso)、ensemble 的討論。做 high-dim factor model (100+ characteristics) 必須補 Kelly-Xiu《Financial Machine Learning》（Round 1）與 Géron（本輪）。
4. **因果識別的現代進展（Angrist-Pischke, RD, DiD）很少**：Ch 19 只有 Heckman selection，缺 Regression Discontinuity、Difference-in-Differences、Synthetic Control 等現代 applied micro 的主流識別策略。Edward 若要做 event-study（政策衝擊、央行行動）應補 Angrist-Pischke《Mostly Harmless Econometrics》。
5. **Backtest overfitting 沒著墨**：Greene 的「data mining」警告停在 specification search（Leamer），沒觸及 Harvey-Liu-Zhu 的 multiple testing 修正（RFS 2016 "...and the Cross-Section of Expected Returns"）。用 Greene 做 factor investing 必須自己加 deflated Sharpe ratio 或 haircut t-stat。

### 與 Edward 既有知識的連結
- **對照 Casella-Berger（本輪）**：Greene 是「應用計量」，Casella-Berger 是「理論統計」。Greene 用到的 delta method、MLE consistency、likelihood ratio test 都在 Casella-Berger 7-10 章嚴格證明。讀 Greene 遇到收斂性存疑的段落就翻 C-B 查定理。
- **對照 Tsay《Analysis of Financial Time Series》（Round 1）**：Tsay 對 ARIMA/GARCH/VAR 的金融應用更深入，Greene 的 Part V 像是 Tsay 的 pedagogical preview。ZP 時間序列模組主要讀 Tsay，Greene 只翻 Ch 20.5 HAC 與 Ch 21.4 cointegration。
- **對照 Hansen-Singleton CCAPM**：Greene Ch 13 GMM 的示範例子就是 consumption-based asset pricing，這是 asset pricing 最早的 empirical test。Edward 的 ZP 長期投資論點「折現率而非 cash flow 解釋大部分 stock return variance」（Campbell-Shiller）在 CCAPM 框架內可以直接檢定。
- **對照 Poker 的 Bayesian update**：Greene Ch 16 的 conjugate prior（Beta-Binomial）恰好對應 poker 裡「對手 fold 頻率的先驗 + 後驗」。撲克用 exploitative thinking 更新 range，正是 Bayesian econometrician 用 likelihood 更新 posterior。
- **對照 DNA §10 Edward-Koko 決策分工**：Greene 的內生性分析提醒我，「Edward 越幫 Koko 喝水」與「Koko 越健康」之間的回歸不能做因果解釋——她本來就會在症狀惡化時接受提醒（reverse causation）。要真的量化「提醒效果」需要 RCT 或 RD 設計，而非 self-reported data 的 OLS。
