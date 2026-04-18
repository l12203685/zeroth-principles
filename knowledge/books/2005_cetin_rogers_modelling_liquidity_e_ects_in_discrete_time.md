## Modelling Liquidity Effects in Discrete Time — Umut Çetin, L. C. G. Rogers
**來源**: E:/投資交易/量化金融文獻/2005 Cetin-Rogers-Modelling liquidity effects in discrete time.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Abstract** (liquidity cost 在 terminal utility 最大化下的 optimal portfolio)
- **1 Introduction** (liquidity risk 在兩大研究方向:large-trader 影響 / market-maker 即時成本)
- **2 The modelling framework** (離散時間 + 遞增凸 liquidity cost 函數 φ)
- **3 Existence of optimal strategy** (supermartingale argument)
- **4 Martingale characterisation** (marginal price 非 notional price 成為 martingale)
- **5 Cox-Ross-Rubinstein binomial example with liquidity cost + CARA utility**
- **6 Reservation ask price for European put options**
- **Appendix** (主要定理證明)

### TL;DR (≤120字)
把 liquidity 成本內生為「凸函數 φ(交易量)」,在離散時間下證明 terminal utility 最大化問題仍有解,但「成為 martingale 的是邊際價 (marginal price),不是帳面價 (notional price)」。套利不需排除,因凸成本已天然限制套利規模。CRR 二元 + CARA 數值示範定出 reservation ask price。

### 核心本質 (3-5 條, 每條 50-120字)
1. **流動性成本 = 凸函數,不是固定點差** — 傳統交易成本模型把 slippage 視為固定比例或 bid-ask spread,Çetin-Rogers 將其建為嚴格凸、嚴格遞增的 φ(ΔX) 函數,捕捉「大單吃深度」的真實結構。這個凸性是全篇結論的關鍵。
2. **Arbitrage 不需被強制排除** — 嚴格凸成本自動限制套利規模:你想佔便宜,邊際成本會隨量急升,使套利上限有限。這對熟悉「完整市場 = NFLVR」的直覺是反轉:流動性友善理論,放寬對市場完美性的要求。
3. **Marginal price 是 hedging 參考價,不是 quote 價** — 最優策略的 marginal utility 作為測度變換,把「邊際價格過程」 而非「帳面報價」轉成 martingale。實務意義:決定是否交易時,用「下一單位將付的價格」而非 screen price 做判斷。
4. **Incomplete market + utility maximisation = 內生定價** — 透過 reservation ask price(agent 願意賣出 put 的最低價)建立選擇權的 utility-indifference price;liquidity 會讓這個價格高於 BS 理論價,差額是 agent 承擔不可完全避險風險的補償。
5. **離散時間比連續時間更適合 liquidity 建模** — 連續 hedging 在有交易成本下會產生無限成本(Soner-Shreve-Cvitanić);離散時間天然有最小時間步,使凸成本積分有限。這與真實交易週期(每分鐘 / 每秒 rebalance)更吻合。

### 可用戰術/策略
- **部位大小關聯 transaction cost 的非線性估計** — 在 B1 自營交易系統中,不要假設滑點是固定 bps,而是建一個基於 order book depth 的 φ(size) 函數;做策略時將 φ 乘入期望報酬計算,大單策略先過此 filter。
- **Reservation price 作為 option writing 的下限** — 若做 covered-call / put-selling 作為收益增強策略,用 reservation ask (utility-indifference) 而非 BS 定價;高於 BS 的差額反映自身流動性限制。
- **CARA + binomial tree 作為快速原型工具** — 論文第 5 節的數值範例可用幾百行 Python 重現,作為新流動性假設下的「玩具箱」驗證策略在 thin market 的行為。
- **Position sizing = solve φ-convex-opt** — 對每一筆交易解 max{return - φ(size)} 的凸最佳化,獲得「此訊號下的最優單量」,直接對應流動性預算。

### 盲點 / 反例 / 適用邊界
- **假設 notional price process S 獨立於 agent 行為** — 意即「我交易不影響後續市場」的 small-trader 假設。對大型基金 / HFT market maker 不成立;需要 Jarrow 1994 的 large-trader 模型補。
- **CARA utility 為簡化選項,偏好現實中隨財富變化** — 論文的數值示範採 CARA 係因它讓問題降維;實務上人類偏好接近 CRRA / prospect theory,reservation price 會有不同。
- **φ 的具體形式靠估計,極具雜訊** — 實務上要從 order book + TCA (Transaction Cost Analysis) 資料拟合 φ,少樣本或稀薄市場下估計不穩。凸性是結構假設,符合直覺但非恆真(如深度不均的 DEX pool 可能在某些 size 範圍反凸)。
- **無明示 funding cost / 利率** — 設定利率為零;在利率環境變動大的時期(如 2022-2024 美聯儲升息)需要加入 funding term,模型擴展非平凡。

### 與 Edward 既有知識的連結
- 直接支撐 `risk_control_four_layers` L4 (流動性準備):此文把 "流動性風險" 從抽象轉為可計算的成本函數 φ,供自營交易系統內建 position sizing 模組。
- 銜接 `meta_strategy_over_strategy`:reservation price 思維把「我該做這筆交易嗎?」內生化為「利得 > 邊際不可避險風險成本嗎?」,屬於策略之上的效用層決策。
- 對 B1 自營交易系統的直接貢獻:建議實作一個 `liquidity_cost.py` 模組,以 order book depth 估計 φ,並在 entry/exit module 將 φ(size) 乘入 expected return;此為 infrastructure 級別的升級。
- 對應 Wilmott FAQ Q36 (complete vs incomplete markets):Çetin-Rogers 是不完整市場 + utility 最大化的嚴謹 instantiation。
