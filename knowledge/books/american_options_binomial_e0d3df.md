## American Options (Binomial Pricing Lecture) — (講義作者未註明)
**來源**: 0009American option.pdf (51 pages 選擇權定價教學講義)  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **American option definition: early exercise right**
- **Comparison: American vs European option value**
- **Intrinsic value vs continuation value**
- **Binomial tree backward induction**
- **Optimal exercise boundary**
- **American put vs call: dividend effects**
- **Numerical examples**

### TL;DR
美式選擇權定價的教學講義,51 頁深度講解二項樹 backward induction、optimal exercise boundary、以及美式 put 與 call 的 early exercise 經濟邏輯。核心:美式 put 常有提前履約價值,美式 call 無股息則無提前履約價值(Merton 1973)。

### 核心本質
1. **美式 ≥ 歐式,差價 = early exercise premium** — 額外履約權只能增加價值不會減少;差值反映提前履約的最佳期望收益。若 premium = 0,美式等同歐式(如無股息 call)。
2. **每一節點選 max(立即履約, 持有)** — Backward induction 從到期日往前推,每個內部節點值 = max(intrinsic value, discounted expected continuation value);這是 dynamic programming 的 Bellman 方程應用。
3. **Merton 1973 定理:無股息美式 call 永不提前履約** — 因 call 時間價值 > 0 且無 carry benefit 可能損失,持有優於提前履約;對應無股息美式 call ≡ 歐式 call,可直接用 BS 公式。
4. **美式 put 常提前履約:early exercise boundary 隨時間單調上移** — 股價低於 boundary 時立即履約最優;boundary 在到期日趨近 strike K,在 t=0 最低。Put 有提前履約是因無風險利率讓「立即拿 K」相對「等到期」的 time value 優勢顯著。
5. **股息會讓美式 call 有提前履約誘因** — 股息支付會讓股價跳下,持有 call 的人會在除息前履約拿股息;因此含股息美式 call > 歐式 call;Roll-Geske-Whaley 有準 closed-form。

### 可用戰術/策略
- **binomial tree 定價**:選擇 step 數 N,計算 up/down factor (u = e^(σ√Δt)),backward induction — 每個節點查 max(intrinsic, continuation) — 得出 t=0 公允價。
- **early exercise boundary 估計**:對 deep ITM put 計算 boundary,實務交易時當 spot < boundary 則履約最優;可用於 structured product 設計。
- **Longstaff-Schwartz LSM**:高維度或 path-dependent 美式 option 用 Monte Carlo + regression on continuation value;適用籃子型 basket options、convertibles。
- **Delta hedge 調整**:美式 option delta 不連續 (early exercise boundary 跨越點),需更頻繁 rebalance 或使用 exotic hedging。

### 盲點 / 反例 / 適用邊界
- **binomial converge 到 BS 需 N → ∞**:實務 N=100-1000 才 stable,計算量 O(N^2);高精度需 trinomial tree 或 finite-difference。
- **離散股息處理複雜**:確定股息時 underlying 要減去 PV of dividend;隨機股息時需額外假設股息過程,誤差放大。
- **volatility smile 未處理**:教科書用常數 σ,實務中 vol surface 依 strike+expiry 變化;需用 local vol / stochastic vol 模型校準 smile。
- **適用邊界**:教學入門;專業定價需延伸到 vol smile、jump diffusion、interest rate term structure。

### 與 Edward 既有知識的連結
- 對應 **derivative_over_level**:optimal exercise boundary 是價值函數對時間的 derivative 的直接應用,符合第一公理。
- 補強 **backtest_methodology**:策略中用美式選擇權對沖時必須正確建模 early exercise 機率,否則 P&L 回測失真。
- 連結 **risk_control_four_layers**:美式 put 是 portfolio insurance 的標準工具,boundary 計算支持 stress-test 情境下的 hedge cost。
- 呼應 **entry_diversity_exit_convergence**:美式 option 天然有「最佳退出時機」= optimal exercise,這是 exit convergence 的理論範本。
