## Book — Optimal Control Models in Finance
**來源**: E:/書籍/Book - Optimal Control Models in Finance.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Chapter 1: OPTIMAL CONTROL MODELS IN FINANCE Optimal control theory has been important in finance (Islam and Craven [38, 2002]; Taperio [81, 1998]; Ziemba and Vickson [89, 1975]; Senqupta and Fan-**

### TL;DR (≤120字)
本書屬於 algorithmic trading 範疇,作者 Optimal Control Models in Finance 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **演算法交易的邊際利潤來自執行細節** — 進出場時點、冰山單、VWAP/POV 切片,而非主策略
2. **策略衰退 (alpha decay) 是必然,持續研發管線是本質不是選項** — 單一策略 life cycle 常低於 2-3 年
3. **Latency 不是唯一賽道,穩定性與再現性才是散戶與機構都可 scale 的護城河**

### 可用戰術/策略

- 建立策略標準化介面與回測基建,把每個新策略的研發時間壓到 1-2 週
- 為每個 live 策略設定監控 (PnL/ drawdown/ trade frequency) 觸發自動下線閾值

### 盲點 / 反例 / 適用邊界

- 過度依賴歷史 backtest 而忽略線上資料源穩定性、訊號延遲、交易所規則變更

### 與 Edward 既有知識的連結

- 呼應零式原則 *meta_strategy_over_strategy* — 關注資金曲線與長期夏普、勝過單筆交易或單期回報
- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
