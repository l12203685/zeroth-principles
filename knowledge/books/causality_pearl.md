## Causality: Models, Reasoning, and Inference 2e — Judea Pearl
**來源**: Cambridge University Press canonical 2009 edition  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- 第 1 章 Introduction to Probabilities, Graphs, and Causal Models
- 第 2 章 A Theory of Inferred Causation（Causal Inference algorithm、IC、FCI）
- 第 3 章 Causal Diagrams and the Identification of Causal Effects（do-calculus 3 axioms）
- 第 4 章 Actions, Plans, and Direct Effects（causal effect of policy）
- 第 5 章 Causality and Structural Models in Social Science & Economics
- 第 6 章 Simpson's Paradox, Confounding, and Collapsibility
- 第 7 章 Structural Counterfactual Conditionals（twin networks）
- 第 8 章 Imperfect Experiments（IV, natural experiments、instrumental variable）
- 第 9 章 Probability of Causation: Interpretation and Identification（PN/PS/PNS）
- 第 10 章 The Actual Cause（but-for test、necessary cause）
- 第 11 章 Reflections, Elaborations, and Discussions with Readers

### TL;DR (≤120字)
Pearl 這本 *Causality* 是因果推論的數學聖經，確立 DAG + do-calculus 取代傳統 regression。對交易者的價值：區分相關 vs 因果——「回測統計顯著」只是相關；實際執行要能 intervene。第 3 章 do-operator 三規則是金融事件研究（earnings、M&A、政策）的嚴格工具。Simpson's paradox（第 6 章）在跨 regime 分析經常出現。數學密度極高。

### 核心本質 (3-5 條)
1. **do(X) 不等於 observe(X)（本質，第 3 章）** — P(Y|X=x) ≠ P(Y|do(X=x))；前者是觀察（含選擇偏差）、後者是介入（剝離 confounder）。交易信號 backtest 是 observational；實際下單是 intervention，效果可能不同。
2. **Do-calculus 3 規則化簡 intervention（本質，第 3.4 節）** — Rule 1: insert/delete observations (z ⊥ Y|X,W); Rule 2: action/observation exchange (do(Z) ↔ observe(Z) under back-door); Rule 3: insert/delete actions. 這三規則完整判定 identifiability。
3. **Back-door criterion 判斷 confounder 可否控制（本質，第 3.3.1 節）** — 存在 Z 阻斷所有 X→Y 的 back-door path ⇔ P(Y|do(X)) 可由觀察資料識別。實務：找 valid adjustment set 再 regress。
4. **Front-door adjustment（本質，第 3.3.2 節）** — 當所有 confounder 不可觀察時，若存在 mediator M 且 X→M→Y 無未觀察 confounder，可用 front-door 公式識別 causal effect。
5. **IV 是 unobserved confounder 下的救命工具（本質，第 8 章）** — Z → X → Y 且 Z 獨立於 unobserved confounder，2SLS 可一致估計；金融：貨幣政策作為 asset return 的 IV、shock 作為 volatility IV。

### 可用戰術/策略
- **Event study DAG**：earnings announcement → price → return；需控 market beta (confounder) 但不要控 analyst revision (mediator)。
- **IV for policy shock**：FOMC surprise 作為 rate 的 IV，估計利率→REIT return 因果效應。
- **Propensity score adjustment**：選股策略用 PS 匹配：高品質股（treated）vs 低品質股（control），平衡 size/beta 後比 return。
- **Counterfactual backtest**：用 structural causal model 模擬「若 2020 沒量化寬鬆，股價會如何」。
- **Mediator analysis for alpha decay**：alpha → (capacity → impact) → realized return；分析哪個 mediator 主導策略退化。

### 盲點 / 反例 / 適用邊界
- **數學密度極高**：測度論、圖論、邏輯演算皆用；非數學背景需配 McElreath 入門版。
- **DAG 正確性假設**：整個框架建立在 DAG 對；DAG 錯則推論全錯。金融 DAG 難驗證。
- **時間動態缺席**：Pearl 模型多 static；金融 dynamic causality 需 Granger/LiNGAM 擴展。
- **線性/加法假設常用**：實際 causal effect 常 heterogeneous；需 CATE/doubly robust ML 補（Chernozhukov、Athey）。
- **實作稀**：書多證明少 code；實作配 DoWhy/EconML 套件。

### 與 Edward 既有知識的連結
- **對齊 ZP event-driven strategy**：財報/M&A/policy 事件用 DAG + do-calculus 嚴格估計 treatment effect，取代粗糙「before-after」比較。
- **延伸 McElreath**：McElreath 直觀、Pearl 嚴謹；先 McElreath 建立 DAG 直覺，再 Pearl 補數學正當性。
- **衝突點**：Pearl 反對 potential outcomes 框架（Rubin 派）；Rubin (Hernán-Robins) 派偏應用。Edward 可混用：DAG 建模用 Pearl，估計用 Rubin。
- **可挖金礦**：第 8 章 IV 的 formal conditions 可驗證 Edward 的「貨幣政策→資產價格」因果鏈是否有效 IV。
- **對接 Hernán-Robins Causal Inference (What If)**：Hernán 偏 epidemiology/social science 應用；兩書互補。
