## Quantitative Trading Systems: Practical Methods for Design, Testing, and Validation — Howard Bandy

**來源**: E:/書籍/Quantitative Trading Systems_ Practical Methods for Design, Testing, and Validation ( PDFDrive ).pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 系統交易導論（為何量化、為何系統化、為何需驗證）
- 第 2 章 研究流程（hypothesis → design → test → validate → deploy）
- 第 3 章 資料清理（adjusted prices、splits、delisted stocks、survivorship）
- 第 4 章 Indicator 與 feature 設計（統計屬性、stationarity、normalization）
- 第 5 章 Entry / Exit 規則（precision 與 recall 的 trade-off）
- 第 6 章 Objective function 選擇（max return? min DD? best Sharpe?）
- 第 7 章 Optimization（grid search、genetic algorithm、particle swarm）
- 第 8 章 過擬合的識別與防範（cross validation、walk-forward、OOS）
- 第 9 章 Monte Carlo 模擬（隨機化訂單、bootstrap 評估 CI）
- 第 10 章 實盤部署（paper、small-scale、scale-up 的 checklist）
- 第 11 章 組合系統（多市場、多策略、多時間框架）
- 第 12 章 Live monitoring（drift detection、re-validation trigger）
- 第 13 章 案例集（Bandy 提供的 ETF rotation、VIX 策略、pair trading）

### TL;DR (≤120字)
Howard Bandy（PhD 統計 + 前 Raytheon 工程師、AmiBroker 合作者）的書是**「量化交易的統計學嚴謹教材」**。與 Davey 的實戰、Kaufman 的百科相比，Bandy 最接近學院派：嚴格分布檢驗、交叉驗證、Bayesian confidence intervals。適合有統計/ML 背景的讀者。**核心貢獻是把 ML 的 validation 方法論引入 trading system design**。

### 核心本質 (3-5 條)
1. **Trading system 是 classification / regression 問題**（本質） — Bandy 的獨特視角：entry 訊號 = binary classification（買 / 不買）、exit 訊號 = regression（最佳出場時機）。這使 **ML 的所有 validation 工具**（cross-validation、precision-recall curve、AUC、confidence interval）**直接適用 trading system**，給 trading system design 提供嚴謹統計框架。
2. **Objective function 的選擇決定最終策略形狀**（本質） — 第 6 章：優化 max return 得到高槓桿冒險策略；優化 Sharpe 得到低波動但低報酬；優化 Calmar（return/max DD）得到平衡。**沒有中性的 objective function**——每個 implicit 對 risk tolerance 與 time horizon 做假設。明確陳述自己的 objective function 是系統設計的第一步。
3. **Walk-forward 的嚴謹實作**（本質） — 第 8 章：naïve walk-forward 用 rolling window，但仍有 look-ahead bias（參數空間本身在所有歷史 tuning）。**嚴謹版 walk-forward**：每個 OOS 周期必須完全隔離——代碼、參數、特徵選擇全部只用 IS 期前的資訊。Bandy 給出 Python 偽碼示範。
4. **Bootstrap confidence interval 比點估計更誠實**（本質） — 第 9 章：回測給出 Sharpe = 1.5 是**點估計**，可能真實 Sharpe ∈ [0.8, 2.2]（95% CI）。Bandy 主張所有 performance metrics 都應以 CI 形式呈現——通過 Monte Carlo bootstrap 歷史訂單得到分布。策略只在 CI 下限 > 閾值（e.g. Sharpe CI lower > 0.8）才上線。
5. **Drift detection = 策略存活的 metric**（本質） — 第 12 章：即使策略通過驗證，實盤績效可能因 market regime change 漂移。**Drift detection** = 用 rolling window 比較最近 30-60 日績效與歷史分布；若 z-score < -2（低尾）連續 15+ 日，觸發 re-validation。這是將 ML 的 concept drift 應用到 trading。

### 可用戰術/策略
- **ML validation framework for trading**：對每個策略執行 (1) K-fold cross validation（K=5），確認各 fold Sharpe 一致、(2) precision-recall for entry signal、(3) AUC > 0.55 作為 signal 有 edge 的閾值。
- **Objective function 檢查**：在設計任何策略前明確寫下 objective（max return? max Sharpe? max Calmar? min DD?）；不同 objective 的最佳參數不同，混淆會導致策略不符實際需求。
- **嚴謹 walk-forward 實作**：將 10 年資料切 10 段；對每段，前 9 段 tune，第 10 段 test；每段 test 用的代碼/參數/特徵完全凍結；最終 OOS performance 是 10 個 test 段的平均，不是整體重新 tune。
- **Bootstrap CI 上線規則**：策略 bootstrap Sharpe CI 下限 > 0.8 才能進 paper trade；> 1.0 才能進小資金實盤；否則需更長樣本或更嚴格設計。
- **Drift detection daemon**：每日計算 rolling 30-day Sharpe 與歷史 distribution 的 z-score；< -1.5 警示、< -2 連續 15 日強制 re-validation、連續 30 日強制關閉。

### 盲點 / 反例 / 適用邊界
- **AmiBroker 綁定** — 大部分代碼範例是 AFL (AmiBroker 語言)；Python/R 讀者需重寫。
- **案例偏 US equity** — 第 13 章案例都是美股；對期貨、FX、options、crypto 的 generalization 需自行驗證。
- **ML 深度不足** — Bandy 介紹 ML validation 但不涉及深度 ML 模型（neural net、gradient boosting）；2020+ 的實務需配合 Lopez de Prado。
- **缺少交易心理** — 第 10-12 章實作偏技術、缺乏心理學（Douglas/Kiev 的強項）。
- **statistical rigor 雙刃劍** — 過度嚴格的統計檢驗可能過濾掉真正可用策略（type II error）；需平衡嚴謹與實用。

### 與 Edward 既有知識的連結
- **對齊 Round 1 Machine Learning R (Lantz) + Financial Machine Learning (Kelly-Xiu)**：Bandy 提供 ML validation framework、Lantz 提供 R 代碼、Kelly-Xiu 提供 empirical results；三本合起來是完整 ML-in-finance 教材。
- **與本輪 Davey / Tomasini 互補**：Davey/Tomasini 實戰派、Bandy 學院派；Edward 應用時 Davey 為 baseline、Bandy 作嚴謹補強。
- **Bootstrap CI 可 Python 化**：加入 `ZP/quant/backtesting/bootstrap_ci.py`，對所有策略輸出 CI 形式績效而非點估計。
- **可挖金礦**：Drift detection daemon 可作為 `staging/daemons/` 的一個持續運行 subagent，每日 scan 所有 live 策略並 alert。
- **衝突點**：Bandy 的嚴謹統計與 Chan 的「快速部署」哲學有張力；Edward 採 Bandy 嚴謹 validation 作為上線 gate、Chan 速度作為 deployment 原則。
