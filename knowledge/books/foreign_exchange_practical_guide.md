## Foreign Exchange: A Practical Guide to the FX Markets — Tim Weithers

**來源**: E:/書籍/Foreign Exchange A Practical Guide to the FX Markets 0471732036.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 I 部分 FX 基礎
  - 第 1 章 FX market 結構（spot、forward、swap、options）
  - 第 2 章 報價慣例（base/quote、interbank convention、retail convention）
  - 第 3 章 主要參與者（central banks、interbank dealers、corporates、retail）
- 第 II 部分 Spot FX
  - 第 4 章 Spot 價格決定機制（supply/demand、macro factors）
  - 第 5 章 Cross-rate 與 triangular arbitrage
  - 第 6 章 Bid-ask spread 的組成與決定因素
- 第 III 部分 Forward FX
  - 第 7 章 Forward rate 的 covered interest parity 推導
  - 第 8 章 Forward points 報價（pip 計算、non-deliverable forward）
  - 第 9 章 FX swap 的結構與應用
- 第 IV 部分 FX Options
  - 第 10 章 FX option 的定價（Garman-Kohlhagen 模型、two interest rates）
  - 第 11 章 Implied volatility surface 的特殊結構（risk reversal、butterfly）
  - 第 12 章 Barrier options 與 exotic structures
- 第 V 部分 實務與風險
  - 第 13 章 Corporate hedging 實務（translation、transaction、economic exposure）
  - 第 14 章 Speculative trading strategies（carry trade、trend、mean reversion）
  - 第 15 章 FX market 的監理與合規
  - 第 16 章 Emerging market currencies 的特殊性
- 第 VI 部分 Advanced Topics
  - 第 17 章 FX volatility products（vol swap、variance swap）
  - 第 18 章 FX algo trading（VWAP FX、dark pool for FX）

### TL;DR (≤120字)
Weithers（Chicago 大學教授 + 前 UBS FX director）的書是 **FX practitioner handbook**——兼具理論完整性與市場實務。600+ 頁涵蓋從 spot quote convention 到 FX options 定價的全光譜。特色是**clean 介紹 FX option 的 Garman-Kohlhagen 雙利率模型**，與 Hull 的純股票 options 形成對照。

### 核心本質 (3-5 條)
1. **FX 是雙利率資產，不能直接套用股票 options 模型**（本質） — 第 10 章：FX spot 不支付 dividend 而是 **domestic - foreign interest rate differential**；Garman-Kohlhagen 公式 `F = S × exp((r_d - r_f)T)` 替代股票的 `F = S × exp(rT)`。忽略 foreign rate 會使 put/call 評估錯誤 1-5%（低利率時影響小、高利率差時影響大）。
2. **Covered Interest Parity 是 FX 的基礎 identity**（本質） — 第 7 章：`(1+r_d)T = (S_0/F_T) × (1+r_f)T`；任何違反此 identity 的 FX 價差等同無風險套利。正常市場內 CIP holds within 1-2 bps；2008 / 2011 / 2020 危機期間 CIP 可破到 50-100 bps（dollar shortage 驅動），暗示融資市場問題。
3. **FX vol surface 有獨特的 3-point parameterization**（本質） — 第 11 章：FX options 市場不像股票用 strike-based quote，而是 delta-based：25-delta risk reversal (RR) + 25-delta butterfly (BF) + ATM vol。**RR 揭示 skew 方向**（正值 = call 貴 = 市場怕漲多於跌）、**BF 揭示 kurtosis**（正值 = tail 重）。quant 需能把 (ATM, RR, BF) 轉為完整 vol surface。
4. **Carry Trade 是 FX 最著名但最危險的策略**（本質） — 第 14 章：借低利率幣（JPY, CHF）買高利率幣（AUD, NZD, EMFX），賺 interest differential。**平時 Sharpe 1-1.5、但 tail event 一次吃光多年獲利**（2008 AUD/JPY 從 108 崩至 60，60% 下跌）。正確姿勢是 dynamic hedge（VIX/VXY 高時減碼）與 option overlay（買 OTM put 保護）。
5. **FX 市場的監理鬆散度是雙刃劍**（本質） — 第 15 章：FX spot 在美國不受 SEC 監管（屬 commodity），結構上類似 OTC；這給了 retail broker（FXCM、Oanda）可用 50-500x 槓桿，但也意味著 **broker 倒閉時投資者保護極少**（無 SIPC）。2015 CHF unpegged 事件多家 FX broker 倒閉，客戶資金受損。

### 可用戰術/策略
- **CIP 違背監控**：每日計算主要貨幣對的 CIP deviation (in bps)；> 20 bps 警示、> 50 bps 可能存在風險溢價或信用事件前兆。
- **Triangular arbitrage 檢查**：監控 EUR/USD × USD/JPY vs EUR/JPY direct quote；> 3 bps 差異理論上套利機會（實務上 sub-second 被 HFT 吃光）。
- **Risk Reversal as sentiment indicator**：25-delta RR 持續偏離歷史均值 2σ 時預示方向偏好；配合 spot 走勢作為確認信號。
- **Carry trade 帶 hedge**：做多 AUD/JPY 時同步買 3-month 25-delta put；保費耗 1-2% carry 的一部分，但 tail event 保全本金。
- **FX broker redundancy**：交易 FX 時用 2-3 個 broker（Interactive Brokers + OANDA + Saxo），分散 broker 倒閉風險；IB 有 SIPC-like 保護較佳。

### 盲點 / 反例 / 適用邊界
- **成書於 2006，錯過 2008 / 2015 CHF / 2022 GBP** — 這些重要事件的教訓未涵蓋。
- **retail FX 風險警告不夠** — Weithers 是 institutional 背景，對 FXCM 類 retail broker 的 conflict of interest（bucket shop vs true ECN）未深入。
- **Crypto 完全缺席** — 2006 BTC 尚未存在；crypto 對 FX 市場的衝擊（尤其在 emerging market 的美元化）未涵蓋。
- **algo FX 章節淺** — 第 18 章只是概念；具體 FX algo 實作需配合 Johnson《Algorithmic Trading and DMA》。
- **emerging market 章節偏 2000s** — 新興市場 FX 的流動性、清算結構在 2010-2020 變化大（人民幣國際化、DeFi stablecoin 等）。

### 與 Edward 既有知識的連結
- **對齊 Round 1 day_trading_currency_market_lien**：Lien 偏日內 retail 操作、Weithers 偏 institutional 理論基礎；Edward 讀 Lien 學戰術、讀 Weithers 學架構。
- **Garman-Kohlhagen 適用 B2 options 研究**：若 Edward 未來涉及 FX options（例如 EUR/USD 選擇權），需基於 GK 模型而非 Black-Scholes。
- **CIP 作為市場壓力指標**：對 B1 宏觀判斷有用——CIP 違背放大是信用事件前兆，可作為 de-risking 訊號。
- **可挖金礦**：第 11 章 FX vol surface 的 (ATM, RR, BF) parametrization 可編程為 `ZP/quant/fx/vol_surface.py`，配合 FX options strategies。
- **衝突點**：Weithers 的 institutional 重心與 retail 交易者實務有差距；需批判取用，不直接照搬 institutional 工具。
