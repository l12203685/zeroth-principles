## Understanding Algorithmic Trading — JPMorgan (Institutional Equities Guide)
**來源**: C:/Users/admin/staging/b2_batch_E_extracts/68dec0ca3ad1a3f1__understanding_algorithmic_trading_jpmorgan.md  |  **消化日**: 2026-04-18  |  **模型**: claude-opus-4-7[1m] (main session)

### 目錄
- §1 演算法交易背景（機構投資人為何轉向 algo、broker 競爭、買方 vs 賣方 algo 選擇）
- §2 JPM Algorithm Family
  - 2.1 Schedule-based（VWAP、TWAP、PoV）
  - 2.2 Benchmark-based（Arrival Price、Implementation Shortfall）
  - 2.3 Liquidity-seeking（SIGMA X / dark aggregator）
  - 2.4 Peg 與被動策略（Midpoint Peg、Primary Peg）
- §3 Smart Order Routing 機制（venue selection、priority ranking、fee rebate 優化）
- §4 Dark Pool 使用情境（minimum size、price improvement、IOI 信號）
- §5 Algorithm Customization Parameters（urgency、style、constraint）
- §6 Execution Quality 評估（post-trade TCA、algorithm attribution）
- §7 典型應用案例（IPO 組合、index rebalance、程式交易）

### TL;DR (≤120字)
JPMorgan 機構版演算法交易指南，簡明概述買方 trader 該懂的 algo 分類、何時用哪個、如何評估執行品質；特色是把 schedule-based（VWAP/TWAP）、benchmark-based（IS）與 liquidity-seeking 三類對比清楚，並給出 urgency × style × constraint 的三維參數選擇框架。

### 核心本質 (3-5 條)
1. **Algorithm 分三大類：Schedule-based / Benchmark-based / Liquidity-seeking**（本質） — §2 核心分類：VWAP/TWAP 是按時間表拆單（schedule），IS/Arrival Price 是按 benchmark 偏差優化（benchmark），SIGMA X/liquidity aggregator 是 sensing 瞬時流動性（opportunistic）。三類對應不同市場情境與 trader 偏好，不是互相取代關係。
2. **Urgency × Style × Constraint 三維參數化**（本質） — §5 揭示：任何 algo 都可由三個 dimension 定義 — urgency（aggressive/normal/passive）、style（participation rate、max volume limit）、constraint（price band、venue preference、min size）；不同組合產生不同 execution trajectory；trader 選 algo 實際是選這三個 dial 的組合。
3. **Dark Pool 是雙面刃**（本質） — §4：Dark pool 優勢是 minimum info leakage + potential price improvement；劣勢是 adverse selection（對手可能是 HFT 或 informed trader）；聰明的 routing 不是 all-dark 也不是 all-lit，而是根據 order size、market condition、venue statistics 動態 split。
4. **Smart Order Routing (SOR) 的多目標優化**（本質） — §3：SOR 同時考量 price、size、queue position、fee rebate、adverse selection history；每個 venue 有不同 rebate（maker 0.3¢ rebate、taker 0.3¢ fee）；理論最優解需要 multi-objective optimization，實務上靠 heuristic rules。
5. **Post-Trade TCA 是 algo 改進的閉環**（本質） — §6 核心紀律：每筆執行後算 IS、Arrival Price 偏差、VWAP deviation、fill rate；按 broker/algo/venue 分組；持續 3-6 個月後找出 systematic bias；若某 algo 在 earnings week 表現不佳 → 避免該類情境用該 algo；這是 execution alpha 的工程化改進。

### 可用戰術/策略
- **Algo 選擇 Decision Tree**：
  - 若 need urgent fill + willing to pay spread → Arrival Price
  - 若 need quiet execution + OK with slower fill → VWAP
  - 若 large order + time-flexible → Implementation Shortfall
  - 若 uncertain about size/price → Liquidity-Seeking + dark pool
  - 若 need anonymity + OK with partial fill → Midpoint Peg
- **Urgency Dial Setting**：
  - Aggressive（1-3）：高 participation rate、允許 take liquidity、適合 signal 敏感
  - Normal（4-7）：平衡被動主動、適合日常 flow
  - Passive（8-10）：低 participation、等 midpoint、適合 low urgency + price sensitive
- **Venue Rebate Arbitrage**：maker-taker 模型下，掛 passive limit 賺 0.3¢ rebate，market order 付 0.3¢ fee；若 fill rate 允許，passive routing 可把 commission 變正值。
- **Minimum Size Filter in Dark Pool**：設定 min size = 1/3 of order 避免被 HFT 小單 pick off；此 filter 會降低 fill rate 但大幅降低 adverse selection。
- **Earnings Week Algo Swap**：財報週 volatility 高 + 流動性分散；避免純 VWAP（易被 news 衝擊）；改用 IS + tight 進度追蹤 + 必要時 manual override。

### 盲點 / 反例 / 適用邊界
- **Broker-centric 內容** — 本指南是 JPM 為買方 trader 寫的推銷材料；雖客觀但難免偏好介紹 JPM SIGMA X、自家 algo；其他 broker 的 LOXM (JPM 自己)、SMART (Citi)、Premio (GS) 也有差異；需跨 broker 比較。
- **僅股票市場** — 期貨、FX、fixed income 的 algo 邏輯不同；股票 algo 邏輯無法直接套用到 CME Bund、USDJPY spot；需補 Cartea 等跨資產書籍。
- **2010s 版本資料** — 2020 後 retail PFOF、internalizer、Robinhood 對 SOR 影響巨大；機構 algo 與 retail 環境逐漸分化。
- **Adverse Selection 量化不足** — §4 承認 dark pool 有 adverse selection 但未提供具體檢測公式；實務需整合 Kissell 或 Almgren-Chriss 的 model。
- **Regulatory 影響被跳過** — MIFID II（2018）對 dark pool 有 4% cap、Reg NMS 在美國的 order protection rule，本指南偶爾提但未深入影響分析。

### 與 Edward 既有知識的連結
- **對齊 ZP 核心**：urgency × style × constraint 三維框架對應零式投資本質 — 任何決策都需在三個正交維度下選擇，不是單一 tuning；Edward 設計 AI 代理 dispatch 時也可參考此框架（任務緊急度 × 品質要求 × 成本約束）。
- **延伸既有 DNA**：post-trade TCA 的閉環自我改進對應 DNA learning loop — 每輪 recursion 後必須 persist 結果 + 分析偏差 + 調整下輪參數；單次 dispatch 不留資料 = 無法累積 execution alpha。
- **衝突點**：此指南為大型機構設計，Edward 自營規模無需完整 algo suite；但「先分類 order、再選 algo、後做 TCA」的三步流程仍可簡化為 Edward 的 trading checklist。
- **可挖金礦**：§5 的 urgency × style × constraint 三維參數化可直接移植到 Edward 的任務 dispatch 框架；每個 task 先標註三維（例：「分析市場報告」= urgency normal / style detailed / constraint 2hr budget），自動推導最適 subagent 與 model tier。
