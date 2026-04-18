## Causal Inference: What If — Miguel A. Hernán & James M. Robins
**來源**: Harvard canonical 2020 edition (free PDF)  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- **Part I Causal inference without models (1-10)**：a definition of causal effect、randomised experiments、observational studies、effect modification、interaction、graphical representation、confounding、selection bias、measurement bias、random variability
- **Part II Causal inference with models (11-18)**：why model、IP weighting and marginal structural models、standardisation and the parametric g-formula、g-estimation of structural nested models、outcome regression and propensity scores、instrumental variable estimation、causal survival analysis、variable selection
- **Part III Causal inference from complex longitudinal data (19-21)**：time-varying treatments、treatment-confounder feedback、target trials

### TL;DR (≤120字)
Hernán-Robins 是 Rubin/counterfactual 派因果推論聖經，從流行病學源頭但完美 porting 到金融。Part I 免模型直覺（randomisation、confounding、selection）；Part II 四大估計法（IPW、g-formula、g-estimation、OR/PS）；Part III 時變 treatment（交易策略日日下單 = 完美 time-varying）。寫法比 Pearl 更應用、數學輕但概念密。Target trial emulation 是 backtest 的正確框架。

### 核心本質 (3-5 條)
1. **Potential outcomes framework（本質，第 1 章）** — 每人有 Y^a=1 和 Y^a=0 兩個 potential outcome；causal effect = E[Y^1] - E[Y^0]。觀察資料只看到一個，另一個是 missing data（「fundamental problem of causal inference」）。
2. **隨機化 → exchangeability（本質，第 2 章）** — 隨機分配 treatment 使 (Y^0, Y^1) ⊥ A，於是 E[Y|A=1] - E[Y|A=0] = ATE。交易策略「隨機選股 vs 基金選股」的 RCT 在現實很難。
3. **IPW、g-formula、g-estimation 三大方法等價但穩健性不同（本質，第 12-14 章）** — IPW 用 propensity score 權重；g-formula 用 outcome regression；g-estimation 用 structural nested model。Doubly robust 方法（AIPW）任一對就 consistent。
4. **Time-varying treatment 需 g-methods（本質，第 19-21 章）** — 傳統 regression 在時變 treatment + time-varying confounding 同時存在時會偏差；必須用 g-formula 或 IPW of marginal structural model。
5. **Target trial emulation（本質，第 22 章 新版）** — 從 observational data 做 causal inference 的正確框架：先設計「若能做 RCT 會如何」，再從 observational data 模擬。backtest 就是 target trial emulation；多數 backtest 不自覺違反。

### 可用戰術/策略
- **IPW for survivorship bias**：stock universe 生存偏差 → 用 hazard model 估計 delisting propensity，加權 historical return 做 IPW correction。
- **G-formula for rebalance rules**：各 rebalance 日的 treatment 與後續 confounder 時變；用 g-formula 估計不同 rebalance 策略的 long-run return。
- **Propensity score matching**：比較 ESG 高 vs 低公司 return 時，用 size/ROE/leverage 做 PS，匹配後比較。
- **Instrumental variable**：央行政策 shock 作為利率 IV；比較利率對 REIT return 因果。
- **Target trial emulation backtest**：每個策略寫下「ideal RCT 版本」：eligibility、treatment、follow-up、outcome；對照 backtest 是否真正估計該 effect。

### 盲點 / 反例 / 適用邊界
- **假設 positivity**：每個協變數組合都要有 treatment/control 樣本；實務金融常違反（e.g., 小型股很少被 short）。
- **DAG 仍需**：雖然是 Rubin 派，但 Part I ch 7 大量用 DAG；沒 DAG 思維寸步難行。
- **時間動態仍有限**：Part III 寫得完整但假設仍 sequential ignorability。
- **Epidemiology 範例**：HIV、cancer、smoking；交易者要自行 porting。
- **估計量估計 variance 複雜**：IPW、g-formula 的 bootstrap SE 需小心；大樣本實務用 sandwich estimator。

### 與 Edward 既有知識的連結
- **對齊 ZP 因果 backtest 框架**：target trial emulation 成為標準流程；每個策略明確寫 eligibility/treatment/follow-up/outcome，再評估 backtest 是否 valid。
- **延伸 Pearl**：Pearl 數學嚴格、Hernán 應用豐富；Edward 的金融因果分析雙書互補。
- **衝突點**：Hernán 強調 potential outcomes；Pearl 強調 structural causal model；兩派有「DAG vs Rubin」世紀辯論。Edward 可兩派取所長。
- **可挖金礦**：第 22 章 target trial emulation 是 Edward 回測框架改造的藍圖。一套 CSV 格式每個欄位對應 eligibility/treatment/confounder/outcome。
- **對接 Chernozhukov Double ML**：Hernán 是 parametric 估計；Chernozhukov 的 Double/Debiased ML 是 ML + 因果的 current SOTA。
