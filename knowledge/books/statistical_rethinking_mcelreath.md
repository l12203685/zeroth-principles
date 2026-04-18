## Statistical Rethinking 2e — Richard McElreath
**來源**: Online canonical + PDF circulation  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- 第 1 章 Golem of Prague（反對「一鍵統計機器」、擁抱因果）
- 第 2 章 Small Worlds & Large Worlds（模型 = 小世界；真實 = 大世界）
- 第 3 章 Sampling the Imaginary（posterior 採樣、predictive distributions）
- 第 4 章 Geocentric Models（linear regression、splines、prior predictive simulation）
- 第 5 章 Many Variables（multiple regression、causal salad、masked relationships）
- 第 6 章 Haunted DAG & Causal Terror（collider bias、confounder、selection bias）
- 第 7 章 Ulysses' Compass（過擬合、正則化、information criteria、cross-validation）
- 第 8-9 章 Conditional Manatees & MCMC（interactions、HMC 在 Stan/ulam）
- 第 10-11 章 Generalized Linear Models（binomial、Poisson、multinomial、ordered）
- 第 12 章 Monsters & Mixtures（zero-inflated、ordered categorical、Gamma-Poisson）
- 第 13 章 Models With Memory（multilevel models、partial pooling）
- 第 14 章 Adventures in Covariance（random slopes、covariance prior、LKJ）
- 第 15 章 Missing Data & Other Opportunities（Bayesian imputation、measurement error）
- 第 16 章 Generalized Linear Madness（monomial、ODE、Markov chain）
- 第 17 章 Horoscopes（警示：統計無法替代科學問題）

### TL;DR (≤120字)
McElreath 這本書是 Bayesian + 因果推論的入門神書。用「Golem of Prague」比喻警告讀者：統計軟體是沒良心的黃土人，盲目餵資料會給荒謬答案。強制你先畫 DAG（因果圖）再寫模型。第 5-6 章 collider bias、confounder 是交易者最容易踩的洞（回測時誤用未來資訊）。Stan + brms 實作風格輕鬆、例子有趣（身高、咖啡、婚姻）。

### 核心本質 (3-5 條)
1. **統計不是目標，因果才是（本質，第 1、5-6 章）** — McElreath 稱「純 predictive 思維是危險的」；沒有 DAG 思維會把 collider 當 confounder 控制，反而引入偏差。交易：控制太多變數 = 在 selection 後分析 = 倖存者偏差。
2. **Prior predictive simulation 是必做步（本質，第 4 章）** — 在擬合前，用先驗抽樣看模型預測是否荒謬；若 prior 對身高預測給出 -1000 cm 到 5000 cm，你的先驗太 flat。
3. **DAG (Directed Acyclic Graph) 區分 confounder/mediator/collider（本質，第 6 章）** — Fork (X←Z→Y confounder：要控)、Chain (X→Z→Y mediator：別控)、Collider (X→Z←Y：千萬別控)。交易策略因果鏈必須畫 DAG。
4. **Multilevel model = 部分 pooling 是正則化的 Bayesian 版（本質，第 13 章）** — 完全不 pool = 過擬合各組；完全 pool = 忽略差異；部分 pool = 資料驅動折衷。跨資產/跨時段建模必用。
5. **Information criteria (WAIC/PSIS-LOO) 比 AIC 更準（本質，第 7 章）** — AIC 假設 MLE 且 flat prior，Bayesian 模型用 WAIC（widely applicable IC）或 PSIS-LOO；對 hierarchical 模型 AIC 嚴重低估 effective parameters。

### 可用戰術/策略
- **DAG 先於策略設計**：任何新 alpha 先畫 DAG：market_regime → factor_z → return；確認沒 collider 被誤控。
- **Prior predictive for Sharpe**：寫策略前用 prior 抽 Sharpe 100 次；若 10% 給出 Sharpe > 10 → prior 太 flat。
- **Partial pooling for style rotation**：各風格（value/momentum/quality）β 用 hierarchical，超參數 τ 決定 pooling 強度，資料驅動。
- **Robust Bayesian regression (Student-t)**：把 likelihood 從 Normal 換成 Student-t(ν=4)，自動降低 outlier 影響，對金融 fat-tail 尤其重要。
- **PSIS-LOO 選模型**：比較競爭策略用 PSIS-LOO 比 AIC/BIC 更準；`loo::loo_compare()` 給出 ΔELPD ± SE。

### 盲點 / 反例 / 適用邊界
- **範例非金融**：咖啡、婚姻、身高；讀者需 porting 到金融。
- **MCMC 仍慢**：ulam/Stan 對 n > 1e5 會痛苦；高頻需改 VI。
- **2e 更新停在 2020**：Transformer、因果表徵學習、diffusion 模型不在；為補充需讀 Pearl 2000/2019。
- **DAG 需要背景知識**：DAG 不是資料驅動自動產生的；策略師必須寫下假設。
- **Python 讀者吃虧**：官方碼 R + Stan；Python 版 `pymc3` brmstan 轉寫需自行補。

### 與 Edward 既有知識的連結
- **對齊 ZP causal alpha**：先用 DAG 定義 regime→factor→return 因果；回測時用 do-calculus 做 intervention analysis。
- **延伸 BDA3 (Gelman)**：BDA3 更數學，McElreath 更 pedagogic；新手順序：McElreath 1-7 → BDA3 → McElreath 8-17。
- **衝突點**：McElreath 強調 DAG 優先，金融業傳統「先 backtest 再想 why」與他相反；Edward 須改掉「回測導向」習慣。
- **可挖金礦**：第 6 章 collider bias 的 4 例幾乎都能 porting 金融（倖存者偏差、post-event selection、SR screening 後的雙倍挑選）。
- **對接 Pearl Causality**：McElreath 是 Bayesian 派的因果；Pearl 是結構方程式派；兩書結合讓 Edward 能橫跨實作與理論。
