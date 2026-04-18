## Capital Market Theory II, Lecture 1: Separating Hyperplane Theorems — Chyi-Mei Chen (NTU)
**來源**: inv2017separatinghyperplanetheorem.pdf (NTU CMT II 數學基礎講義 11 pages)  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **Definition of hyperplane H(p, α) in R^N**
- **Strict vs weak separation of sets**
- **Bounding & supporting hyperplanes**
- **Hahn-Banach separation theorem statements**
- **Applications: no-arbitrage pricing, convex optimization duality**

### TL;DR
資本市場理論 II 的數學預備課,嚴格陳述凸集分離定理 (separating hyperplane) 的定義與變體,並指出其在 no-arbitrage pricing 與 utility maximization duality 上的核心作用。核心:分離定理是「無套利 → 存在線性定價」的橋樑。

### 核心本質
1. **分離定理 = 對偶性的幾何源頭** — 任何兩個不相交凸集可用超平面分離,這個 Hahn-Banach 版本是線性規劃對偶、凸優化 KKT、無套利定價等多個金融結果的共同數學基石。
2. **No-arbitrage ≡ 存在風險中性 measure** — 用分離定理在 payoff space 把「可達 payoffs」與「非負 non-zero payoffs」分離,得到的分離超平面法向量 p 就是 risk-neutral pricing kernel;這是 Fundamental Theorem of Asset Pricing 的幾何證明。
3. **Supporting hyperplane 是 marginal pricing 工具** — 在 concave utility / convex constraint 的 optimal point,supporting hyperplane 提供邊際替代率;對應的 Lagrange multiplier 就是 shadow price。
4. **Strict vs weak 分離的實務差異** — weak 分離允許「接觸」,strict 要求嚴格分離。金融應用中,strict 對應 arbitrage-free (嚴格正價格),weak 對應 no-free-lunch (允許零價格)。
5. **無限維延伸 (Hahn-Banach) 處理連續時間**: 離散時間 payoff space 是 R^N,可用幾何定理;連續時間是 L^2 空間,需無限維版本的 Hahn-Banach,這是 continuous-time finance 的技術關鍵。

### 可用戰術/策略
- **定價 checklist**:先確認 payoff space 是 closed convex cone + no free lunch → 分離定理保證 pricing kernel 存在;實務中就是檢查模型結構是否允許套利。
- **對偶問題建構**:解 constrained optimization 卡住時,寫出對偶問題用分離定理解釋 — 常有幾何直覺。
- **無套利檢測**:在 Monte Carlo 生成情境時,檢查所有 state price 是否正(分離定理要求),若負值出現就是 arb opportunity 或模型錯誤。
- **Shadow price 解讀**:Lagrange multiplier = supporting hyperplane coefficient = 資源約束的邊際價值;可用於資源配置、risk budget 設計。

### 盲點 / 反例 / 適用邊界
- **凸性假設是嚴格要求**:若 payoff space 或 preference 非凸(e.g., Cobb-Douglas with integer constraints),分離定理失效,需用非凸優化技巧。
- **closedness 是技術細節**:數學嚴格證明需 closed cone 假設,若市場有開放式 payoff (無上限)會崩潰。
- **連續時間的技術複雜度**:L^2 空間的分離需測度論工具,超出本講義範圍;實務上連續時間 asset pricing 常忽略技術細節。
- **適用邊界**:理論基礎的必備工具;實務應用要配合 specific model (BS, Heston, stochastic vol) 才能落地。

### 與 Edward 既有知識的連結
- 對應 **derivative_over_level**:supporting hyperplane 的法向量 = derivative of value function,這是數學上「變化率優於水準」的精確化。
- 補強 **meta_strategy_over_strategy**:對偶性思維讓我們從 primal (直接解 portfolio) 切換到 dual (找 pricing kernel),有時後者更容易 — 是 meta-strategy 選擇層面的工具。
- 呼應 **information_asymmetry_action**:分離定理的 p 向量是 market implicit 的 pricing kernel,若你的信念 p' ≠ p,就存在 asymmetry-driven position;no-arb 假設下 p 是 unique。
- 連結 **backtest_methodology**:驗證策略前應先確認模型無套利(分離定理成立),否則回測出的「alpha」可能是模型內部套利,不是真 edge。
