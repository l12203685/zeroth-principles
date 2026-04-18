## Modelling Liquidity Effects in Discrete Time — Umut Çetin, L. C. G. Rogers
**來源**: LSE Stats + Cambridge Stat Lab Sep 2005 working paper (學術論文 ~30 pages)  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **Introduction: liquidity risk in two streams (large trader / market maker)**
- **Market model with supply curve & liquidity cost**
- **Optimal portfolio existence under utility max**
- **Bellman equation & HJB solution**
- **Equivalent martingale measure transformation**
- **Cox-Ross-Rubinstein binomial example: reservation ask prices for European puts**
- **Numerical results**

### TL;DR
Çetin-Rogers 在離散時間下建構含流動性成本的投資組合最佳化框架。主要貢獻:(1) 證明 liquidity cost 下最佳組合存在;(2) 最佳終端財富的邊際效用可作為「測度變換」把邊際價格轉為鞅;(3) 用 CRR 二項模型展示歐式 put 的 reservation ask price 計算。

### 核心本質
1. **流動性風險 = 市場風險、信用風險後的第三大金融風險** — 1998 LTCM、2008 雷曼倒閉都是流動性 → 信用 → 市場的傳導鏈;傳統 BS 框架假設可無限量交易、無衝擊成本,是「無摩擦」假設下的特例。學術與實務對 liquidity 建模的重要性一直被低估。
2. **supply curve 取代單一價格** — 現實中 asset 不是單一 P,而是 depth-dependent supply curve S(t, x):買 x 單位要付 S(t,x),賣 -x 單位只能拿 S(t,-x)。這直接反映 bid-ask spread + price impact 的經濟結構,而非事後用 transaction cost 硬加在 BS 上。
3. **Reservation price ≠ fair price** — 在流動性約束下,衍生品的「合理賣價」(reservation ask) 嚴格高於無摩擦 fair price,且與交易規模、風險偏好相依;單一 no-arbitrage 價格崩潰,變成 bid-ask 區間。這是流動性建模的核心哲學轉折。
4. **效用最大化下的測度變換存在** — 即便市場不完備、有摩擦,只要 agent 有凹效用 u,最佳策略的 marginal utility 仍可當 Radon-Nikodym derivative,把邊際價格轉為鞅。這保留了定價理論的核心結構,只是參照 measure 不是 Q 而是 u-dependent。
5. **離散時間方法論優勢:直接對應實務** — 連續時間 liquidity model (Bank-Baum, Schied 等) 數學優美但計算困難;Çetin-Rogers 的 CRR 離散框架可直接套入 TLT、lattice option pricer,工程化成本低。

### 可用戰術/策略
- **帶流動性成本的選擇權定價**:對 illiquid 標的(小型股、OTC 衍生品)使用 Çetin-Rogers reservation ask/bid 而非 BS mid;留出 liquidity premium 作為 hedging 成本緩衝。
- **大宗交易 slicing 最佳化**:把大單拆成 n 個小單,每段根據 supply curve 最佳化 → 最小化市場衝擊;本文框架提供 HJB 方程式為解決此 problem 的數學基礎。
- **liquidity-adjusted VaR / ES**:在風險測量中把 liquidity cost 直接納入,特別是高峰期(如月末流動性枯竭)時 VaR 要加補貼;離散框架便於按日 rebalance。
- **reservation price spread 作為市場信號**:reservation ask - reservation bid 可作為流動性壓力指標,擴大時市場承壓;可入量化策略的 regime filter。

### 盲點 / 反例 / 適用邊界
- **supply curve 形狀的實證校準困難**:理論假設 supply curve 已知,但實務上需從訂單簿資料反解,requires 分鐘級 LOB 資料,對大多數 retail 投資者不可得。
- **單一 agent 假設過度簡化**:框架假設其他參與者不對 agent 行動反應,忽略策略互動、front-running、反饋迴路;真實市場(特別是 HFT-heavy)是多 agent 博弈。
- **連續時間極限未完整處理**:離散時間模型在 Δ → 0 時是否收斂到有 liquidity 的連續模型,本文僅在特定假設下證明,推廣到無限活動跳躍過程需後續工作。
- **適用邊界**:中低頻交易、中大型機構;HFT 與 market making 需對 supply curve 做更精細的 order-book-level 模型,本文是中度粒度的最佳化框架。

### 與 Edward 既有知識的連結
- 對應 **risk_control_four_layers**:流動性風險是第四層「市場結構風險」,2008 教訓證明即便 modelled 單一資產 VaR 對齊,流動性擠兌仍可導致組合崩潰;本文提供量化納入 liquidity 的方法論入口。
- 呼應 **meta_strategy_over_strategy**:liquidity 不是個股 strategy 層面的問題,而是 bankroll / 資金存活層面的問題;Çetin-Rogers 讓 meta-strategy 把流動性成本 endogenize 進效用函數。
- 連結 **entry_diversity_exit_convergence**:entry 多元化要考慮單一標的 liquidity capacity,避免「策略多但共用一個 illiquid 標的」的假分散;exit convergence 在 liquidity crunch 時會放大衝擊成本。
- 補強 **backtest_methodology**:傳統回測假設 market-open 可自由交易,本文提示應對大單(>0.1% ADV)加入 slippage model + supply curve 扣抑;否則回測高估 alpha。
