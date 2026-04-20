## PriceAction+Protocol+V2.0完整中文版（No-secured) — 未標示
**來源**: E:/書籍/Price Action/PriceAction+Protocol+V2.0完整中文版（No-secured).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Introduction 简介**
- **What Markets To Trade 什么样的品种适合用这套方法交易**
- **Trending Markets 趋势行情**
- **Ranging Markets 横盘震荡 区间**
- **Dynamic Support & Resistance 动态的支撑阻力位--均线组**
- **Trend Lines 趋势线**
- **The Rejection Candle 折回线, 简称 Pinbar**
- **The 2 Bar Reversal 双K反转**
- **The Outside Bar 吞噬线**
- **Comparing the 3 Rejection Setups 比较三种K线信号**
- **The Hot Spots 热点区域**
- **Entry Methods 入场模式**
- **Timing Your trade Entries 时间段的选择**
- **Stop Loss Placement 如何设置止损**
- **Consolidation 盘整节奏**
- **The Inside Bar 孕中线**
- **The Indecision Bar 犹豫不决的k线-- 十字星线**
- **The Price Squeeze Pattern 汇价不断收缩的形态-三角形态**
- **False Breakouts 假突破**
- **Trending Markets - Advanced 如何跟随趋势-进阶版**
- **Money Management 资金管理**
- **Money Management - Pyramid Trading 资金管理-金字塔加仓法**
- **Trading Psychology 交易心理**

### TL;DR (≤120字)
本書屬於 statistics evidence based 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **多次檢驗問題會偽造 alpha** — data mining 若不做 Bonferroni/BH 校正,幾乎任何「策略」都能在歷史上跑贏
2. **統計顯著 ≠ 經濟顯著** — t-stat 3.0 但年化超額 0.3% 在扣手續費後無法存活
3. **前瞻偏誤 (look-ahead bias) 在學術論文與商業回測都普遍** — 特別留意財報日、指數調整日的訊號重建

### 可用戰術/策略

- 採用 white's reality check / stepwise superior predictive ability 做多重檢驗修正
- 所有 backtest 引入交易成本、滑價、融資成本,再看 net Sharpe

### 盲點 / 反例 / 適用邊界

- 統計檢驗預設資料獨立,金融時序高度相關,block bootstrap / stationary bootstrap 才能貼近實際分布

### 與 Edward 既有知識的連結

- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
- 呼應零式原則 *derivative_over_level* — 關注變化率/拐點而非單期水準
