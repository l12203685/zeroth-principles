## Profitability and Systematic Trading: A Quantitative Approach to Profitability, Risk, and Money Management — Michael Harris

**來源**: E:/書籍/Profitability and Systematic Trading A Quantitative Approach to Profitability, Risk, and Money Management, Michael Harris.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 系統交易的三要素：profitability、risk、money management 的不可分離
- 第 2 章 Expectancy 的數學（E = W × avg_win − L × avg_loss、Kelly 前身）
- 第 3 章 Profitability 分析（drawdown、recovery time、profit factor、payoff ratio）
- 第 4 章 Risk 分析（VaR、CVaR、tail ratio、worst-case scenarios）
- 第 5 章 Money Management 方法對比（fixed %、Kelly、Optimal f、ATR-based）
- 第 6 章 策略生命週期（alpha 發現、成熟、衰退、死亡的偵測）
- 第 7 章 多系統組合（correlation、capital allocation、rebalance）
- 第 8 章 案例：股票 momentum 策略的完整 P/R/MM 分析
- 第 9 章 案例：期貨 trend 策略的完整 P/R/MM 分析
- 第 10 章 案例：pairs trading 的 P/R/MM 分析
- 第 11 章 心理學：規則遵循與 over-optimization 的鬥爭

### TL;DR (≤120字)
Michael Harris（知名交易研究員、Price Action Lab 創辦人）的書是 **systematic trading 三要素整合教材**：Profitability、Risk、Money Management 不能獨立優化。核心論點：**許多策略失敗不是因為 signal 錯，而是因為把三要素分開處理**。本書用統一框架評估每個策略，避免「高 Sharpe 但無法 scale」或「好策略但 MM 規則毀滅它」等常見錯誤。

### 核心本質 (3-5 條)
1. **Profit、Risk、MM 是三角形而非 pipeline**（本質） — Harris 核心論點：傳統流程是先找 profitable signal → 加 risk management → 套 MM；實際上三者互相影響。**提高 MM 槓桿會改變 risk profile；改變 risk profile 會改變實際 P/L 分布**。需同時優化三者（3D 優化），而非依序處理。
2. **Expectancy > Sharpe 對 retail trader 更相關**（本質） — 第 2 章：E = W×avg_win − L×avg_loss，是單筆交易的期望值。Sharpe 對 institution 有用（有穩定流入流出），但 retail 的資本是固定的，E（配合 trade frequency）更直接決定年化報酬。高 Sharpe 低 E 的策略可能不值得 retail 執行（因 frequency 太低）。
3. **Drawdown recovery time 比 drawdown depth 更重要**（本質） — 第 3 章：max drawdown 20% 可能 3 個月 recover、也可能 3 年 recover；後者實務上摧毀 trader。Harris 提出 **DDR (Drawdown Duration Ratio)**：max DD depth / recovery time；DDR > 1 (月) 視為 toxic 策略，即使 Sharpe 好看。
4. **Kelly 的假設在實務多不成立**（本質） — 第 5 章：Kelly 公式假設 (1) 勝率與盈虧比穩定、(2) 獨立事件、(3) 連續再投資。實際交易中這些假設常被違反——勝率在 regime change 時波動、連續虧損有相關、資金非連續 re-invested。Harris 建議用 **empirical Kelly**（從歷史訂單 bootstrap 估算）而非理論公式，通常結果是 full Kelly 的 30-50%。
5. **策略死亡的 3 階段信號**（本質） — 第 6 章：(1) 初期：Sharpe 逐月下降、profit factor < 1.5；(2) 中期：max DD 超越歷史、recovery time 拉長；(3) 末期：期望值負、profit factor < 1。Harris 的 rule：第 2 階段出現即減倉 50%，第 3 階段出現立即關閉。大多數 retail 在第 3 階段才認知失效，已虧光先前獲利。

### 可用戰術/策略
- **三要素整合評估**：對每個策略同時計算 P（profit factor、expectancy、annual return）、R（max DD、DD duration、VaR、CVaR）、MM（Kelly、Optimal f、secure f）；任一維度不達標不上線。
- **Empirical Kelly 計算**：bootstrap 歷史訂單 10,000 次，計算每次 sample 的 optimal Kelly；取分布的 25 分位數作為實務 Kelly（保守派）；通常為理論 Kelly 的 0.3-0.5 倍。
- **DDR 監控**：對所有運行策略每月計算 DDR = max DD / recovery months；DDR > 1 時警示並考慮降倉；DDR > 2 時強制關閉。
- **3 階段死亡偵測**：每月對每個策略跑 (Sharpe, PF, max DD) 三指標的 z-score（相對歷史）；三者全 < −1 為第 1 階段、兩個 < −2 為第 2 階段、三者全 < −2 為第 3 階段。
- **P/R/MM dashboard**：每日更新每個策略 P/R/MM 三維評分 (0-10)；總分低於 18/30 需人工 review。

### 盲點 / 反例 / 適用邊界
- **理論整合但缺少 empirical depth** — Harris 的三要素整合框架論述清晰，但實證案例（第 8-10 章）僅 3 個，未充分驗證跨風格/跨市場。
- **crypto 完全缺席** — 成書於 2000s，crypto 的 MM 特殊性未涵蓋。
- **不涉及 options volatility** — options 的 P/R/MM 需特殊處理（theta decay、gamma 變化），Harris 完全未觸及。
- **DDR 指標的時間單位選擇** — Harris 用「月」作為 recovery 單位但對高頻策略過長；可改為 days 或 trades。
- **與 Stendahl / Vince 等的差異化不足** — 部分章節重複其他 MM 書的內容；Harris 的 originality 集中在 integration framework，其他是 rehash。

### 與 Edward 既有知識的連結
- **與本輪 Stendahl/Unger 互補**：Stendahl 給方法對比、Unger 給冠軍實戰、Harris 給整合框架；三本合讀是 MM 的完整三角形。
- **三要素整合符合 Edward 零式思維**：不分開處理 P/R/MM，而是從 essence（策略的本質是什麼？）出發同時評估；對齊 Layer Zero 原則 1。
- **Empirical Kelly 可直接 Python 化**：加入 `ZP/quant/sizing/empirical_kelly.py`，用 historical bootstrap 計算保守 Kelly。
- **可挖金礦**：DDR 監控可作為 `ZP/quant/risk/strategy_health.py` 的核心指標，配合 Davey 的 z-score 死亡偵測，建立多層監控。
- **衝突點**：Harris 對 theoretical Kelly 的批評與 Vince 理論派有張力；Edward 採 empirical Kelly 作為 B1 預設。
