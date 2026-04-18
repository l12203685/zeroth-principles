## 財務數學 — An Example of No-Arbitrage Pricing — (講義作者未註明)
**來源**: 0001Intro to pricing-b.pdf 財務數學無套利定價教學導論 (45 pages)  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **Betting on A/B game: the bookie example**
- **Representing bets as vectors**
- **Arbitrage: negative-cost non-negative payoff**
- **Replicating portfolio and pricing**
- **Extension to multi-period tree**
- **Risk-neutral probability interpretation**

### TL;DR
用「甲乙賽局的莊家賭注」做為 no-arbitrage pricing 的入門類比。把每個賭注表示為向量、市場為線性空間,透過 replicate portfolio 推出唯一公允價;是 Cox-Ross-Rubinstein 二項模型的前置概念課。

### 核心本質
1. **任何「支付 claim」可用既有資產 replicate,則有唯一 no-arbitrage price** — 這是 one-period finance 最基本定理:若存在 replicating portfolio,其成本即 claim 的公允價;任何偏離該價格都可套利。
2. **市場完備性 (completeness) = 所有 claims 可 replicate** — 本例有限狀態空間 + 足夠線性獨立資產時,市場完備;每個衍生品都有唯一 no-arb 價。實務大部分市場不完備,故 bid-ask spread 自然出現。
3. **套利機會 = 負成本 + 非負終端 payoff** — 用向量表示:存在 portfolio h 使得 price(h) ≤ 0 且 payoff(h) ≥ 0 (非零)。若找到,則系統有套利;反之 no-arb。
4. **賭注設定等價於狀態價格** — 莊家 even money 賭 A/B 隱含 50/50 機率;實務中隱含機率即 risk-neutral probability,可從市場資產價格反解,不等同真實機率。
5. **從 one-period 推廣到 multi-period** — 多期樹的 backward induction 是本章後續內容;核心技術不變:每個節點 replicate → 逆推價格 → discount。這是所有 option pricing 樹方法的基石。

### 可用戰術/策略
- **replicating portfolio 建構**:給定衍生品 payoff,寫出 N 個 state 的 equations,解 portfolio weights;weights × spot prices = 公允價。
- **risk-neutral probability 萃取**:求解 q 使 spot = E_q[discounted payoff];用於定價未 hedged 的 claims。
- **套利檢測 algorithm**:求解 LP — 若可行解 (feasible) 有負目標值,則存在套利;實務可用來驗證模型 consistency。
- **incomplete market 的 super-replicating**:當 claim 不可完全 replicate,用 super-replication (最便宜的支配策略) 給出 upper bound 價格。

### 盲點 / 反例 / 適用邊界
- **離散狀態假設簡化現實**:實務資產有無限 continuum 狀態,需用連續時間 SDE + Itô's lemma,framework 複雜度陡增。
- **無交易成本的假設**:實際有 bid-ask、commission、margin requirements,完美 replication 不可能,no-arb price 變為 bid-ask 區間。
- **無流動性限制**:假設任意量可交易,現實大單會推動市場價,見 Çetin-Rogers 2005。
- **適用邊界**:理論入門、BS 推導前置;專業定價需延伸到 stochastic volatility、jumps、liquidity、counterparty risk 等。

### 與 Edward 既有知識的連結
- 對應 **information_asymmetry_action**:no-arbitrage 告訴我們「市場價 = 所有參與者共同 implicitly price」,edge 在於你對 replicating cost 的估計優於市場 mid-price。
- 呼應 **derivative_over_level**:替代組合的 delta(derivative of payoff w.r.t. spot) 是 replicating weights,這是一階變化率的金融實例。
- 補強 **meta_strategy_over_strategy**:no-arb pricing 是所有 derivative pricing 的 meta-strategy 基石,任何定價模型必須先通過 no-arb consistency。
- 連結 **risk_control_four_layers**:模型風險層 — 確認定價模型 no-arb 是最低要求,否則模型本身藏有 free lunch 陷阱。
