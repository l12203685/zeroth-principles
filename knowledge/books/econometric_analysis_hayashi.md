## Econometrics — Fumio Hayashi (Princeton)
**來源**: Princeton University Press canonical edition  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- 第 1 章 Finite-Sample Properties of OLS（Gauss-Markov、t/F-test、multicollinearity）
- 第 2 章 Large-Sample Theory（consistency、asymptotic normality、delta method、Slutsky）
- 第 3 章 Single-Equation GMM（linear GMM、over-identification、J-test）
- 第 4 章 Multiple-Equation GMM（3SLS、SUR、panel GMM）
- 第 5 章 Panel Data（fixed effects、random effects、Hausman test）
- 第 6 章 Serial Correlation（Newey-West HAC、stationarity、ergodicity）
- 第 7 章 Extremum Estimators（MLE、NLLS、M-estimator、QMLE、asymptotic inference）
- 第 8 章 Examples of Maximum Likelihood（probit、tobit、hazard models）
- 第 9 章 Unit-Root Econometrics（Dickey-Fuller、augmented DF、structural breaks）
- 第 10 章 Cointegration（Engle-Granger、Johansen、VECM、error correction）

### TL;DR (≤120字)
Hayashi 是研究生級計量經濟學教材的公認頂峰，比 Greene 更嚴謹、比 Wooldridge 進階。對交易者的價值：第 3-4 章 GMM 是資產定價模型（Hansen-Jagannathan, Euler eq）估計基石；第 9-10 章 unit root + cointegration 是 pairs trading 的統計正當性。數學密度極高（測度論 + asymptotic theory），但每章有金融例子。讀完 Greene + Hayashi 可獨立讀 academic finance 論文。

### 核心本質 (3-5 條)
1. **GMM 是一切估計的通用框架（本質，第 3 章）** — Moment condition E[g(z, θ)] = 0；樣本 moment condition 的最小化給出 θ̂。OLS、2SLS、MLE 都是 GMM 的特例。資產定價 Euler equation E[u'(c)R - 1] = 0 是金融 GMM 代表。
2. **Over-identifying restriction → J-test（本質，第 3.5 節）** — 當 moment conditions > parameters，可檢驗過度識別：Hansen J-stat = n × obj function asymptotic χ²(df)。拒絕 → 模型錯設。
3. **Newey-West HAC for autocorrelated errors（本質，第 6 章）** — 當 error 有 serial correlation（金融返利幾乎全有），standard error 需用 HAC 校正；否則 t-stat 膨脹導致偽顯著。
4. **Unit root 之前不能 regress（本質，第 9 章）** — 若 X, Y 皆 I(1)，普通 OLS 會產生 spurious regression（R² 虛高、t-stat 虛顯著）。必須先 ADF 測 stationarity。
5. **Cointegration = 長期均衡關係（本質，第 10 章）** — 兩 I(1) 序列若 β×X + Y 為 I(0) 則 cointegrated；這是 pairs trading 的統計根基。Johansen 檢驗多變量 cointegration。

### 可用戰術/策略
- **GMM for factor model**：用 moment condition E[(R_i - β_i' F) × Z] = 0 估計 β，Z 是工具變量；比 OLS 對 endogeneity 穩健。
- **HAC SE 校正 Sharpe t-stat**：策略年化 Sharpe 1.5，但 daily return 有自相關；用 Newey-West lag=√T SE，避免 false positive。
- **Johansen cointegration pairs**：3 支股票（S&P、Nasdaq、Dow）檢驗 cointegration rank；rank=2 → 可組 2 個 cointegrated pair 做 stat arb。
- **Error-correction model (ECM)**：若 pairs cointegrated，用 ΔY = α(Y_{t-1} - β X_{t-1}) + ε 估計回歸速度 α；α 越負收斂越快。
- **2SLS for asset pricing**：用滯後變量作為 instrument 解決 contemporaneous endogeneity（e.g., return × volume 的雙向因果）。

### 盲點 / 反例 / 適用邊界
- **假設 regular asymptotic theory**：很多 fat-tail 金融資料違反 Lindeberg CLT；需 robust M-estimator。
- **Unit-root test 低 power**：ADF 在 near-unit-root 情況有嚴重 power 問題；需用 KPSS 互驗、Bayesian unit root 補。
- **Cointegration 需 I(1) 同階**：若一 I(0) 一 I(1) 無法 cointegrate；差異數需先確認。
- **機器學習完全缺席**：本書 1990s 研究生教材，ML 不在。現代論文 ML + econometrics 需 Chernozhukov/Athey-Imbens。
- **Panel data 止於固定效應**：沒有 dynamic panel（Arellano-Bond）；需配 Baltagi。

### 與 Edward 既有知識的連結
- **對齊 ZP stat arb**：第 9-10 章 cointegration + ECM 是 pairs trading 框架；直接實作為 `ZP/quant/stat_arb/johansen_pairs.py`。
- **延伸 Tsay (Round 1)**：Tsay 重時序、Hayashi 重 cross-section + panel；兩書補完整計量。
- **衝突點**：Hayashi 假設 well-behaved asymptotic；Bennett/Kelly-Xiu 強調 fat-tail 下方法失效。Edward 實戰先假設 Hayashi，失效時退 robust M-estimator。
- **可挖金礦**：第 3.5 J-test 可驗 Fama-French 3 factor vs 5 factor 哪個 over-identifying restriction 失敗，指示 missing factor。
- **對接 Wooldridge（done）**：Wooldridge 是 undergraduate；Hayashi 是 graduate；Edward 已有 Wooldridge，補 Hayashi 完成計量鏈。
