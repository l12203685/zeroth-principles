# Introductory Econometrics: A Modern Approach (4ed) — Jeffrey M. Wooldridge

### 目錄
1. 核心本質 — Wooldridge 的「現代」=識別策略先於估計方法
2. 可用戰術 — Cross-section / Time Series / Panel / IV 的使用時機
3. 盲點/反例 — 入門書未涵蓋的高階議題
4. 與 Edward 既有知識的連結

### TL;DR
Wooldridge 4ed (Cengage 2009, 19 章 + 7 附錄) 是美國大學部計量經濟學使用率最高的教材，結構簡潔：Ch 1 資料類型與 ceteris paribus、Part 1 截面回歸 (Ch 2-9)、Part 2 時間序列回歸 (Ch 10-12)、Part 3 進階議題（Ch 13-14 panel data、Ch 15 IV/2SLS、Ch 16 同時方程、Ch 17 LDV + Tobit/Heckman、Ch 18 unit root + cointegration + ARCH/GARCH、Ch 19 如何做一個實證專案）。相較 Greene 的「數學導向」，Wooldridge 的區別是**把識別 (identification) 放在估計 (estimation) 之前**——每個模型先談「怎麼詮釋係數」「什麼假設下 β̂ 才會一致」，再談估計公式。這正是 Angrist-Pischke 一派現代應用計量的精神。對 Edward 來說，這本是「用 Greene 做理論、用 Wooldridge 做操作」的組合。最實用章節：Ch 8 異變、Ch 15 IV、Ch 13-14 panel、Ch 18 進階時序。

### 核心本質
1. **Ceteris Paribus 是計量的哲學根基（Ch 1.4）**：Wooldridge 開篇第一章就花 10 頁辨析「其他條件不變」的意義——多元回歸係數 β_j 的詮釋永遠是「holding other x's fixed」下的 ∂y/∂x_j。若 omitted variable 與 regressor 相關，ceteris paribus 不成立，β̂ 就有 omitted variable bias。這個哲學貫穿全書——每個新模型都在問「這個估計量能不能回答 ceteris paribus 問題？」
2. **OLS 的四個 MLR 假設（Ch 3.3-3.5）**：(MLR.1) 線性 in parameters、(MLR.2) random sampling、(MLR.3) no perfect collinearity、(MLR.4) zero conditional mean E[u|X]=0、(MLR.5) homoskedasticity、(MLR.6) normality。前四個給出 unbiasedness、加第五個給 BLUE、加第六個給 exact t / F distribution。Wooldridge 清楚指出 MLR.4（exogeneity）是金融實證最難滿足的假設。
3. **Heteroskedasticity 不破壞一致性但破壞推論（Ch 8）**：異變下 β̂ 仍 unbiased & consistent，但 SE(β̂) 錯、t-stat 不再服從 t 分布。White (1980) 的 robust SE / HCCM 不需要知道異變結構，用殘差平方估計 Var(β̂)。實務：金融資料幾乎全部異變，`robust` 選項應該是默認。
4. **IV = 找外生工具為內生 regressor「代言」（Ch 15.1-15.3）**：若 x 內生 (E[u|x]≠0)，用 z 滿足 Cov(z,u)=0 且 Cov(z,x)≠0 可一致估計 β = Cov(z,y)/Cov(z,x)。兩個條件：exclusion restriction (z 只透過 x 影響 y) + relevance (first-stage 相關)。實證例：Angrist (1990) 用越戰 draft lottery 當 z 估計 schooling 對 earnings 的因果效果。
5. **Unit Root 與 Cointegration 是時間序列的分水嶺（Ch 18.2-18.4）**：Ch 18 Wooldridge 的 trilogy——(a) 若 y_t 是 I(1)，OLS 的標準 t-statistic 不服從 t 分布，必須用 ADF critical values；(b) 差分 I(1) → I(0) 再做迴歸；(c) 兩個 I(1) 序列可能 cointegrated，此時 levels regression 仍可行且 β̂ super-consistent（Stock 1987）。這決定 pair trading 合法性的理論根基。

### 可用戰術
1. **Log-Log Regression 係數 = 彈性（Ch 2.4 / 6.2）**：log(y)=β₀+β₁log(x)+u ⇒ β₁ 是 elasticity。財經常用：log(quantity) on log(price) 直接讀出需求彈性；log(volume) on log(volatility) 讀出 trading activity elasticity。比百分比變化直覺。
2. **Dummy Variable + Interaction（Ch 7）**：加 regime dummy D=1(post-crisis) 與 x 交互項 x·D 可讓 slope 在 pre/post 不同。回測中檢驗「策略在低 vol regime 參數 β_vol=0.5，高 vol 跳到 1.2」就用這個。
3. **First-Difference vs. Fixed Effects（Ch 14）**：Panel data 兩種主要方法——FE（demeaning within group）和 FD（first-difference）對兩期 panel 完全等價，對多期 panel 在 ρ≠1 時 FD 更有效率（Wooldridge 建議）。金融上做 firm-level regression 要同時 cluster by firm + by time (Petersen 2009, Thompson 2011)。
4. **Newey-West HAC（Ch 12.5）**：序列相關 + 異變同時存在時用 Newey-West，truncation lag 取 ⌊4(T/100)^{2/9}⌋。R 用 `sandwich::NeweyWest()`，Python 用 `statsmodels.stats.sandwich_covariance.cov_hac`。
5. **Empirical Project 19 步驟（Ch 19）**：整本書最實用的附錄——從 research question → data collection → exploratory → choose model → identification strategy → robustness → write-up。正是一個 ZP 實證研究的 Template。

### 盲點/反例
1. **涵蓋深度有限，不是 PhD 級別**：Wooldridge 省略 Greene 的 Bayesian、simulation-based estimation、nonlinear GMM 等進階。嚴肅 econometric research 仍需補 Greene 或 Hayashi《Econometrics》。
2. **Time series 章節僅基礎**：Ch 18 只到 unit root + simple ARCH；沒 VECM 細節、沒 state-space、沒 Kalman filter、沒多變量 GARCH。對金融時間序列必補 Tsay 系列。
3. **Panel data 處理偏 micro-econ**：Ch 13-14 的例子都是 wage/education 等勞動經濟學；FX panel、international finance panel 有特殊 issue（cross-section correlation, common factor）沒涵蓋。補 Pesaran《Time Series and Panel Data》。
4. **沒 modern causal inference 工具**：沒 DiD、RD、synthetic control、matching estimator、Rubin causal model。2014 後的 applied micro 論文幾乎都用這些——Imbens-Rubin《Causal Inference》或 Angrist-Pischke《MHE》補之。
5. **2009 出版**：Wooldridge 後來寫了《Econometric Analysis of Cross-Section and Panel Data》2ed (2010) 更深入；這本入門書的部分素材已由第 5-7 版更新，但核心未變。

### 與 Edward 既有知識的連結
- **對照 Greene《Econometric Analysis》（本輪）**：Greene 是 Wooldridge 的進階版——同樣 topic 範圍但深度高 3x。Wooldridge 適合第一遍建立直覺，Greene 回去深化理論。兩本互為雙層階梯。
- **對照 Casella-Berger（本輪）**：Wooldridge Appendix B, C 是 C-B 精簡版本——sufficient 只到 Ch 3, MLE 只到 Ch 4。嚴格理論基礎必須讀 C-B。
- **對照 Tsay《Multivariate Time Series》（本輪）**：Wooldridge Ch 18 的 VECM 只一節，Tsay 全書 Ch 5 + Ch 7 深挖。金融時間序列以 Tsay 為主，Wooldridge 當參考。
- **對照 Angrist-Pischke《Mostly Harmless Econometrics》**：Wooldridge 是 old-school 計量（structural model + assumption-laden），MHE 是 modern applied（potential outcomes + quasi-experiment）。Edward 做政策衝擊（Fed 決策、稅改）event study 時 MHE 更有用；做結構化迴歸時 Wooldridge 更合適。
- **對照 ZP 的「簡單模型優先」原則**：Wooldridge Ch 6.1「Parsimony」一節強調「模型愈複雜不一定愈好」——BIC 懲罰參數、cross-validation 檢驗。這與 Occam's razor + DNA §2 axiom 5 (Bias toward inaction) 思路一致——沒強證據不加變數、沒強訊號不進場。
- **對照 Poker Game Theory Optimal vs. Exploitative**：Wooldridge 的「assumption-laden structural model」= Poker 的 GTO（自一套模型完全解出策略），「quasi-experiment + IV」= 撲克 exploitative（從對手實際動作識別偏差）。兩種思維互補。
