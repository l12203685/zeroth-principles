## Building Winning Algorithmic Trading Systems — Kevin J. Davey

**來源**: E:/書籍/Building Winning Algorithmic Trading Systems-A Trader's Journey from Data Mining to Monte Carlo Simulation to Live Trading, Kevin J. Davey.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 I 部分 前言（Davey 背景：World Cup Trading Championships 三連冠、獨立交易員）
- 第 1 章 系統化交易的現實（期望值、回撤、心理負荷、對手方）
- 第 2 章 研究平台（TradeStation、NinjaTrader、MultiCharts、Python 轉換成本）
- 第 3 章 策略構思（從經驗生成、從學術論文生成、從反向直覺生成）
- 第 4 章 資料與清理（tick data、連續合約拼接、survivor bias、corporate action）
- 第 5 章 初次回測（IS 樣本、OOS 保留、參數網格 vs 隨機搜尋）
- 第 6 章 穩健性測試（walk-forward、monte carlo、parameter sensitivity）
- 第 7 章 Monte Carlo 模擬（訂單序列洗牌、損益分布 CI 估計、最大回撤預測）
- 第 8 章 參數優化陷阱（curve fitting、in-sample overfitting、selection bias）
- 第 9 章 實盤部署（paper trading、small-size、scaling up、連線監控）
- 第 10 章 實盤監控與退出（drawdown triggers、strategy death detection）
- 第 11 章 組合與資金管理（多策略相關性、固定 fractional、pyramiding）
- 第 12 章 心理與紀律（連虧執行、超額報酬的貪婪陷阱、假期問題）

### TL;DR (≤120字)
Davey 是 World Cup Trading Championships 三連冠（2005/2006/2007）的獨立期貨交易員。本書是他 25 年自營的「血淚 SOP」：**如何把一個策略從 idea 走到 $1M 實盤，而不中途毀滅帳戶**。特色是對 Monte Carlo 模擬的工程化處理、以及對「策略死亡」的機械式偵測規則。是獨立 algo trader 最實在的工作手冊。

### 核心本質 (3-5 條)
1. **策略有生命週期，偵測死亡是第一要務**（本質） — Davey 第 10 章：每個策略從 alpha 發現到死亡通常 3-36 個月。關鍵不是找到永恆策略（不存在），而是**在策略死亡的前 3 個月偵測到**並退出。死亡訊號：最大回撤持續時間 > 歷史最大 × 2，或連續 3 個月績效落在歷史 5 分位以下。
2. **Monte Carlo 模擬比 walk-forward 更揭露真相**（本質） — 第 7 章：walk-forward 只測試了 1 種歷史序列，但策略在不同訂單順序下的最大回撤分布可差異 3 倍。正確做法是把歷史訂單洗牌 5,000-10,000 次，取最大回撤的 95% 分位數作為風險預算，而非歷史實際最大回撤。
3. **參數選擇的 selection bias 比 curve fit 更隱形**（本質） — 第 8 章：即使沒 curve fit 單一參數，在 10 個參數各 5 種選擇中挑「看起來最好的組合」仍會產生 selection bias。Davey 推薦 **parameter plateau** 方法：繪製績效 vs 參數的 3D 圖，只採用位於平坦高原而非尖峰的參數組合。
4. **paper trade 到實盤的銜接是最大坑**（本質） — 第 9 章：即使 paper trade 完美，轉實盤時仍可能因 broker API 行為差異、成交優先級、隔夜資料中斷等問題虧損。標準操作是 paper 60 天 → 1 contract 實盤 30 天 → 5 contracts 30 天 → 規模化。快於此流程的擴張是賭博。
5. **獨立 algo trader 的真正競爭者不是 Citadel，而是自己的心理**（本質） — 第 12 章：Davey 實證指出，他大部分虧損不來自策略失效，而來自「連虧 5 次後 override 規則」的人為干預。算法交易的 60% 工作是寫規則，40% 工作是建構「不讓自己 override 規則」的心理與流程防火牆。

### 可用戰術/策略
- **Monte Carlo 風險預算**：對任何完成回測的策略，把歷史訂單洗牌 10,000 次（用 bootstrap 或 permutation），取最大回撤的 95 分位數，乘以 1.5 作為實盤的最大允許回撤。
- **策略死亡偵測規則**：跟蹤最近 60 天績效的 z-score（相對歷史 mean/std）；z < −2 連續 30 天 → 減倉 50%；z < −2.5 連續 45 天 → 關閉策略。
- **Parameter plateau 選擇**：測試參數網格後，對每個參數組合計算其「鄰居 5 個組合的績效均值」，選平均最高而非單點最高；這自動避開峰值過擬合。
- **paper-to-live 4 階段流程**：paper 2 個月 → 最小單位（1 contract / 100 shares）2 個月 → 5 倍 1 個月 → 目標規模；任一階段績效低於前階段 50%，回退一階段。
- **多策略相關性監控**：跑 5+ 策略時每週算 pairwise 績效相關，若兩策略 30 日相關 > 0.6，削減其中一個權重；避免看似分散實則同源的風險。

### 盲點 / 反例 / 適用邊界
- **偏期貨 (futures) 視角** — Davey 的案例以 E-mini S&P、crude oil 等期貨為主，對股票/options/crypto 的適用需額外調整（futures 有 roll、continuous contract 處理獨特）。
- **不涉及因子模型** — 書中策略都是 single-symbol technical rules，沒涉及 cross-sectional factor、pairs arb、options vol；讀者需配合 Chan/Narang 補全策略類型。
- **TradeStation/NinjaTrader 綁定** — 代碼範例是 EasyLanguage，Python/R 讀者需自行轉譯；近年 QuantConnect/Backtrader 等平台已更通用。
- **回測平台的限制未深入** — 商業平台對 tick-level 處理、跨市場模擬的限制 Davey 僅輕描；實際上許多 retail 回測平台在滑點模擬上不夠真實。
- **心理章節偏雞湯** — 第 12 章的心理建議實用但結構化不足，對比 Steenbarger《The Daily Trading Coach》深度更高。

### 與 Edward 既有知識的連結
- **對齊 Round 1 Faith《海龜交易法則》**：Faith 給心理、Kaufman 給數學、Davey 給工程流程；三本是獨立 systematic trader 的三足鼎立教材。
- **Monte Carlo 模擬直接實作**：第 7 章的 MC 框架可 Python 化加入 `ZP/quant/backtesting/mc_simulator.py`，對 B2 所有候選策略強制跑 MC 風險預算。
- **策略死亡偵測是 B1 必備**：Edward 需把 z-score 死亡偵測內化為 daemon，避免「已經死的策略仍在跑」的隱形虧損。
- **paper-to-live 流程搬入 SOP**：可作為 `staging/` 新策略上線的標準化 checklist，每個策略必經 4 階段才進入 full size。
- **衝突點**：Davey 的 walk-forward 與 MC 搭配法與 Kestner (Round 1) 的純 walk-forward 觀點不同；Edward 採 Davey 的雙管齊下更保守。
