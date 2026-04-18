# Multivariate Time Series Analysis: With R and Financial Applications — Ruey S. Tsay

### 目錄
1. 核心本質 — 多變量時間序列是「跨序列動態依賴」的統計學
2. 可用戰術 — VAR/VARMA/Cointegration/DCC-GARCH 建模流程
3. 盲點/反例 — 高維資產組合的維度詛咒
4. 與 Edward 既有知識的連結

### TL;DR
Tsay (Wiley 2013, 522 頁 7 章 + 附錄) 是他 2010 年《Analysis of Financial Time Series》的多變量進階版，聚焦於**多資產間動態關係**：Ch 1 基本概念（weak vs strict stationarity、linearity、Wold decomposition）、Ch 2 平穩 VAR（Least Squares、MLE、Granger causality、Bayesian 估計、impulse response、FEVD）、Ch 3 VARMA（包括辨識問題、exact likelihood、Kronecker index）、Ch 4 VARMA 結構化設定、Ch 5 單根非平穩（unit root tests、共整合、spurious regression）、Ch 6 因子模型 + PCA + exogenous variables、Ch 7 多變量波動率模型（CCC, DCC, BEKK, GO-GARCH）。書中大量用 R 套件 MTS、vars 做實證示範。**核心哲學**：單變量 AR/ARIMA 假設序列「自給自足」，但實務中利率、匯率、股價相互影響（Fed 升息→美元升→新興市場股跌），多變量模型才能捕捉這種 cross-dependence。Ch 5 的共整合與 Ch 7 的 DCC-GARCH 對金融實務最實用。

### 核心本質
1. **Granger Causality 是「預測貢獻」而非「因果」（Ch 2.2.1）**：x Granger-causes y 意指：已知 y 的歷史，額外加入 x 的歷史能顯著降低 y 的預測誤差。這是可檢定的線性假設（Wald test on 對應 VAR 係數），但與真實因果不同——confounding、reverse causality、common factor 都會造成 spurious Granger causality。用在 lead-lag 效果測試（如「原油對黃金」或「利率對股票」）可靠，用於政策推論不可靠。
2. **Impulse Response + Cholesky 排序決定結果（Ch 2.10-2.11）**：IRF 回答「若 x 有 +1 單位震盪，y 未來 k 期會怎樣」。但 Cholesky decomposition 需要指定變數順序——排第一的被視為「最外生」其 shock 立即影響所有其他。實務上 vmon/ffr 排前 vs. 股價排前得出天差地別的 IRF。現代做法用 SVAR + sign restriction 或 Blanchard-Quah long-run restriction。
3. **共整合 = 多個 I(1) 的線性組合是 I(0)（Ch 5.3-5.7）**：若 y_t, x_t 都是 I(1) 但 y_t - βx_t 是 I(0)，則存在 cointegrating vector (1, -β)。Engle-Granger 兩步法：(i) OLS 得 β̂；(ii) 殘差做 ADF test 檢定 I(0)。Johansen procedure 用 VECM 同時估計 cointegration rank r 與 loading matrix α。對 pair trading 策略：找出 cointegrated pair 後建 Error Correction Model z_t = αΔ + γ(y-βx) + ε 即可回歸均值。
4. **DCC-GARCH 讓相關矩陣動態（Ch 7.7）**：Engle 2002 的 DCC 把多變量波動率分解成 σ_i · R_t · σ_j，其中 R_t 是動態相關矩陣。Ch 7.7 給出 estimation 兩步法：先分別估單一 GARCH(1,1)，再用 standardized residual 估相關矩陣 AR(1) 結構。比 BEKK 參數少得多，適合 >10 資產。金融應用：2008 崩盤時 equity-bond correlation 從 -0.4 跳到 +0.3，DCC 能即時捕捉。
5. **Spurious Regression 在多變量更嚴重（Ch 5.3）**：兩條獨立 random walk 跑 OLS，R² 期望值約 0.45、t-stat 期望值 >>4。若沒先做單根檢驗，幾乎所有金融序列迴歸都「顯著」。Tsay 複述 Granger-Newbold 1974 的警告——差分前必做 ADF 或 Phillips-Perron。

### 可用戰術
1. **VAR 訂階用 AIC/BIC/HQ（Ch 2.6.2）**：AIC 偏向過參數化（傾向選高階），BIC 對 n→∞ consistent，HQ 介於兩者。實務上 BIC 為主、AIC 為敏感度分析。R 套件 `vars::VARselect()` 一次給四個準則的最佳 lag。
2. **Forecast Error Variance Decomposition（Ch 2.11）**：把 y_t h-step-ahead MSE 拆成各衝擊的貢獻比例。若 FFR 解釋股價變異數的 30%，則 monetary policy shock 對 equity return 有實質解釋力。對 asset allocation regime analysis 很有用。
3. **Johansen Trace Test vs Max-Eigen Test（Ch 5.6）**：檢定 cointegration rank。Trace test 虛無假設是「rank ≤ r」，Max-Eigen 虛無假設是「rank = r」。兩者在 MC 研究顯示 Max-Eigen 小樣本更 powerful 但也更容易 over-reject。實務上兩個一起看，一致才可靠。
4. **Temporal Aggregation 會改變 VARMA 階數（Ch 3.8）**：把 daily VAR 聚合成 monthly 會新生 MA 項（Stram-Wei 1986）。意義：若你在 monthly data 上發現 VAR(1) 適配良好，不代表 daily 上也是 VAR(1)；反之亦然。用不同頻率做 robustness check 時必須考慮 aggregation 扭曲。
5. **GO-GARCH 做高維組合波動率（Ch 7.8）**：把 k 資產線性變換成 k 個不相關的「因子」，每個因子跑獨立 GARCH，再逆變換回來。對 >20 資產的波動率建模比 DCC 更快，但假設變換矩陣 time-invariant。

### 盲點/反例
1. **線性 + 高斯假設**：Ch 1.2.2 明說「real multivariate time series are nonlinear, but linear models can often provide accurate approximations」——這對 regime shift 與極端事件是錯的。VAR 在 2008, 2020 這類非線性 regime change 直接爆掉；threshold VAR (TVAR) 或 Markov-switching VAR 才能處理。
2. **VARMA 的 identifiability 問題（Ch 3.5.1）**：VARMA(p, q) 有無窮多個等價 representation，需加入 identifiability constraint（scalar component approach, Kronecker index）才能估計。實務上多數人直接跳過用純 VAR，但 true DGP 若真是 VARMA，純 VAR 需要很高階才近似，造成 overfitting。
3. **維度詛咒未被解決**：VAR(p) 在 k 變量需要估計 k²·p 個係數；k=20, p=4 就是 1600 參數。Ch 6 提 PCA + factor model 緩解，但 factor 選擇與解釋仍是難題。現代做法用 sparse VAR（Lasso on coefficient matrix）或 FAVAR（Bernanke-Boivin-Eliasz 2005）。
4. **R 套件 MTS 穩定性不佳**：Tsay 本人寫的 MTS 套件 2016-2020 多次回報 numerical issue（特別是 VARMA estimation），業界多轉 MARSS 或 Python statsmodels 的 VECM。讀者須把書當概念教材而非產線程式碼。
5. **沒討論 backtest overfitting 多重比較**：Tsay 全書用 traditional p-value，沒碰 Harvey-Liu-Zhu、Lopez de Prado 的 false discovery rate 修正。做策略 VAR 訊號時若跑 100 個 lead-lag 關係，≥5% 偽陽性是預期的。

### 與 Edward 既有知識的連結
- **對照 Tsay《Analysis of Financial Time Series》（Round 1）**：那本是單變量 (ARIMA, GARCH, stochastic vol)，這本是多變量延伸 (VAR, VARMA, DCC-GARCH, cointegration)。兩本互為姊妹，Edward 的 ZP 時間序列模組兩本都讀完才完整。
- **對照 Greene《Econometric Analysis》（本輪）**：Greene Ch 20-21 是簡版的時間序列入門，Tsay 這本是重版深入。Johansen cointegration、VECM 在 Greene 只有幾頁，Tsay Ch 5 花 40 頁仔細推導。
- **對照 Engle《Systemic Risk in Europe》（Round 1）**：SRISK 的 MES 用 DCC-GARCH 估條件相關，直接對應 Tsay Ch 7.7。這是「學術工具 → 實務應用」的漂亮示範。
- **對照 Campbell-Lo-MacKinlay《Econometrics of Financial Markets》（本輪）**：CLM Ch 9 談 non-linear model / threshold / Markov-switching，Tsay 這本僅線性。兩者互補——Tsay 給線性基礎，CLM 給非線性延伸。
- **對照 ZP/strategies/pair_trading 架構**：我的 pair trading 策略目前只做 OLS residual + Bollinger band。Tsay Ch 5.7 的 VECM 框架給出更嚴謹的「長期均衡 + 短期調整速度」兩層分解，可升級信號產生邏輯。用 Johansen test 先驗證 cointegration 再決定是否加入交易對，能有效篩掉 fake pair。
- **對照 Poker 的「隱含 odds」**：VAR 的 FEVD 其實類比撲克的「對手 action 分解」：對手 raise 可解釋多少由 value hands、多少由 bluffs、多少由 semi-bluffs 貢獻。這種概率分解思維在兩個領域本質同構。
