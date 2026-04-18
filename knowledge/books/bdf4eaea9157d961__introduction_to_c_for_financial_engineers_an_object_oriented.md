## Introduction to C++ for Financial Engineers An Object — Oriented Approach (The Wiley Finance Series)
**來源**: E:/書籍/Introduction to C++ for Financial Engineers An Object-Oriented Approach (The Wiley Finance Series).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Introduction to C++ for Financial Engineers**
  - 0 Goals of this Book and Global Overview
  - 0.1 What is this Book?
  - 0.2 Why has this Book been Written?
  - 0.3 For whom is this Book Intended?
  - 0.4 Why should I read this Book?
  - 0.5 The Structure of this Book
  - 0.6 What this Book does not Cover
  - 0.7 More Information and Support
  - Part I C++ Essential Skills
  - Part II Data Structures, Templates and Patterns Data Structures, Templates and Patterns
  - Part III QF Applications
  - Part IV Background Information

### TL;DR (≤120字)
本書屬於 quantitative trading 範疇,作者 Oriented Approach (The Wiley Finance Series) 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **因子投資的本質是行為與制度偏誤的截面映射** — 小市值、價值、動能等溢酬來自群眾系統性誤定價
2. **因子之間相關性不穩定** — 多因子 portfolio 必須動態估計共變矩陣,否則 diversification 效果被高估
3. **交易成本是因子 alpha 的天敵** — 高週轉因子 (短期動能) 容易被 friction 吃掉

### 可用戰術/策略

- 構建多因子線性模型 + Ledoit-Wolf shrinkage covariance 做最小變異組合
- 設計 rebalance 週期 (月/季) 與 turnover 上限,平衡 alpha 與交易成本

### 盲點 / 反例 / 適用邊界

- 因子也會長期失效 (e.g. value 2008-2020),純因子暴露需要搭配 trend/meta signal 防禦

### 與 Edward 既有知識的連結

- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
- 呼應零式原則 *information_asymmetry_action* — 有邊際資訊優勢才進場
