## options_futures_and_other_derivatives_8th_ed_part2 — 未標示
**來源**: E:/投資交易/交易學習資料庫/@交易/@選擇權/John C. Hull/options_futures_and_other_derivatives_8th_ed_part2.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Chapter 19: Daily changes exceed 3 standard deviations on 1.34% of days. The lognormal model predicts that this should happen on only 0.27% of days. Daily changes exceed 4, 5, and 6 standard deviations on 0.29%, 0.08%, and 0.03% of days, respectively. The lognormal**
  - Chapter 19: what is observed for currency options. (It is also what is observed for options on most other assets.) When a new option has to be valued, financial engineers look up the appropriate
  - Chapter 19: 19.8 WHEN A SINGLE LARGE JUMP IS ANTICIPATED Let us now consider an example of how an unusual volatility smile might arise in equity
  - Chapter 19: 19.17. ''The Black-Scholes-Merton model is used by traders as an interpolation tool.'' Discuss this view. 19.18. Using Table 19.2, calculate the implied volatility a trader would use for an 8-month
  - Chapter 19: which leads directly to gðKÞ ¼ erT c1 þ c3  2c2 2
  - Chapter 19: Basic Numerical Procedures This chapter discusses three numerical procedures for valuing derivatives when analytic
  - Chapter 20: Hence, pu2 þ ð1  pÞd 2  e2ðrqÞt ¼ 2t From equation (20.1), eðrqÞtðu þ dÞ ¼ pu2 þ ð1  pÞd 2 þ ud, so that
  - Chapter 20: The stock price at the jth node (j ¼ 0; 1; . . . ; i) at time i t (i ¼ 0; 1; . . . ; 5) is
  - Chapter 20: time i t captures not only the eﬀect of early exercise possibilities at time i t, but also the eﬀect of early exercise at subsequent times. In the limit as t tends to zero, an exact value for the American put is obtained. In
  - Chapter 20: 20.2 USING THE BINOMIAL TREE FOR OPTIONS ON INDICES, CURRENCIES, AND FUTURES CONTRACTS
  - Chapter 20: Example 20.4 Consider a 1-year American put option on the British pound (GBP). The current exchange rate (USD per GBP) is 1.6100, the strike price is 1.6000, the US risk-free
  - Chapter 20: The node-proliferation problem can be solved by assuming, as in the analysis of European options in Section 14.12, that the stock price has two components: a part that

### TL;DR (≤120字)
本書屬於 options volatility 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **波動率是選擇權定價的核心變量** — 方向性預測失敗時,波動率結構 (ATM/IV skew/term structure) 仍可創造 +EV 機會,這是本質而非戰術
2. **Greeks 是部位面的座標軸** — 任何 payoff 都可以分解為 delta/gamma/vega/theta 的組合,這讓風險管理從「個別部位」升級為「組合相對曝險」
3. **波動率回歸均值是經驗命題,非數學恆等式** — 做 long vol 或 short vol 必須結合結構性事件與資金面,否則長期 short vol 即撿銅板在推土機前

### 可用戰術/策略

- 當 IV rank 高於歷史 80 分位且事件已過,考慮 short iron condor / short strangle,控制 vega 曝險
- 用 calendar spread 捕捉 term structure 扭曲 (近月 IV 高於遠月),對沖市場方向

### 盲點 / 反例 / 適用邊界

- 選擇權策略高度依賴流動性與 bid-ask spread;台指 TXO 週選以外、個股選擇權與期貨選擇權的交易成本可能吞掉理論 edge

### 與 Edward 既有知識的連結

- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
- 呼應零式原則 *meta_strategy_over_strategy* — 關注資金曲線與長期夏普、勝過單筆交易或單期回報
