## Mostly Harmless Econometrics — Joshua D. Angrist & Jörn-Steffen Pischke
**來源**: E:/書籍/Mostly Harmless Econometrics An Empiricists Companion, 2008, by Angrist J. D. and J.-S. Pischke.pdf  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- 第 1 章 Questions about Questions（哪些因果問題可答）
- 第 2 章 The Experimental Ideal（RCT 的黃金標準、實驗與觀察的橋樑）
- 第 3 章 Making Regression Make Sense（OLS 的 5 個因果解讀）
- 第 4 章 Instrumental Variables in Action（LATE interpretation、IV exclusion restriction）
- 第 5 章 Parallel Worlds: Fixed Effects, Differences-in-Differences, and Panel Data
- 第 6 章 Getting a Little Jumpy: Regression Discontinuity Designs
- 第 7 章 Quantile Regression
- 第 8 章 Nonstandard Standard Error Issues（clustered SE、bootstrap）
- 附錄 Econometric Methods（linear algebra、OLS、MLE）

### TL;DR (≤120字)
Angrist-Pischke 這本「大部分無害」是應用計量經濟學最被推崇的一本，芝加哥/MIT 研究生必讀。核心：**IV、Diff-in-Diff、Regression Discontinuity、Fixed Effects 四大 quasi-experiment 工具 + 正確 SE**。寫法幽默、例子經典（越戰抽籤、Angrist 自己的當兵 IV）。對交易者：backtest 實際上是 quasi-experimental design，Angrist 的因果方法可顯著提升回測嚴謹度。

### 核心本質 (3-5 條)
1. **Experimental ideal = 因果推論的 benchmark（本質，第 2 章）** — 所有 observational 方法都是在回答「若能 RCT 結果會如何」；Angrist 強烈主張先問「我的 ideal experiment 是什麼」再選方法。
2. **OLS 仍是因果王者（本質，第 3 章）** — 在正確條件下 regression 就是 causal；用 CEF (conditional expectation function) 視角理解 OLS = best linear approximation to E[Y|X]。
3. **IV LATE 而非 ATE（本質，第 4 章）** — 有 heterogeneity 時 IV 只估計 complier 的 local ATE，不是整體 ATE。exclusion restriction（IV 僅透過 X 影響 Y）是核心不可 testable 假設。
4. **DiD 假設 parallel trends（本質，第 5 章）** — Treatment 前 treatment/control 差異必須 parallel；post-period 差異除 treatment 外皆相同。金融：事件研究前需驗 pre-event trend 一致。
5. **Clustered SE 是 panel 必備（本質，第 8 章）** — Panel data 有 within-cluster correlation；普通 SE 低估真實變異 → false positive。用 clustered SE（by firm/industry/date）。

### 可用戰術/策略
- **DiD for policy shock**：2018 中美貿易戰 → 比較受影響 vs 未受影響產業 pre/post 報酬差異；driven by policy 還是其他因素？
- **IV for sentiment endogeneity**：新聞情緒 → return 同時 return → 新聞；用週末新聞作為 IV（exclusion 是週末新聞不由當日 return 影響）。
- **RDD for index inclusion**：Russell 1000/2000 cut-off 附近公司幾乎隨機分配 index；比較 incidence 前後 liquidity/return 變化。
- **Fixed effects panel regression**：控 firm + month FE，看 idiosyncratic factor（corp governance 改變）對 return 的效應。
- **Clustered bootstrap SE**：Fama-MacBeth 的 t-stat 嚴重 overstated（double clustering by firm × time）；用 Thompson 2011 的 double-cluster SE。

### 盲點 / 反例 / 適用邊界
- **2008 出版，近年 quasi-exp 方法**：ML + causal（Athey-Imbens 2019 forest）、synthetic control 皆未涵蓋。
- **實證偏總體經濟**：勞動、教育範例多；金融讀者需自行 porting。
- **Non-linear 方法輕**：Cox PH、probit 簡短提及；深入需配 Wooldridge Micro Panel。
- **時序非重點**：time series DiD 假設 stationary 很重；金融 non-stationarity 下 DiD 可能失效。
- **數據需求高**：quasi-exp 要有 clean identification；金融資料經常沒清楚 treatment。

### 與 Edward 既有知識的連結
- **對齊 ZP event-driven 策略評估**：policy shock、earnings surprise、M&A 都是自然實驗；用 DiD + RDD 正確估計事件 alpha。
- **延伸 Pearl/Hernán**：Pearl/Hernán 理論、Angrist 應用；三書組成因果推論完整教材。
- **衝突點**：Angrist 強調「credibility revolution」偏經驗主義；McElreath/Pearl 偏結構模型。Edward 雙派並用。
- **可挖金礦**：第 5 章 DiD parallel trend 診斷圖直接可成 ZP event study checklist；event 前 12 個月的 pre-trend 需視覺驗證。
- **對接 Athey-Imbens 2019 Econometric Theory review**：Athey 把 ML + causal 推到前沿；Angrist 是前 ML 時代集大成。
