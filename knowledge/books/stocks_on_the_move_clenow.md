## Stocks on the Move: Beating the Market with Hedge Fund Momentum Strategies — Andreas F. Clenow (趋势永存：打败市场的动量策略)
**來源**: C:/Users/admin/staging/b2_batch_E_extracts/3bf3f101d4eb8c80__stocks_on_the_move_beating_the_market_with_hedge_fund_moment.md  |  **消化日**: 2026-04-18  |  **模型**: claude-opus-4-7[1m] (main session)

### 目錄
- Ch1 序言（"買入上漲的股票" 的一行摘要、與前作《跟隨趨勢》的關係）
- Ch2 共同基金的問題（指數化管理的誤導、相對 vs 絕對報酬、closet indexing）
- Ch3 動量策略核心邏輯（跨時段可持續性、horizon 選擇）
- Ch4 股票排序系統（ATR-normalized return、exponential regression slope、R² 過濾）
- Ch5 篩選規則（市值、流動性、corporate action、缺口、成分股變動）
- Ch6 資金管理（ATR 動態頭寸、parity 權重、最大部位限制）
- Ch7 再平衡頻率（週級 vs 月級、税務考量、交易成本）
- Ch8 市場環境過濾器（指數 200 日均線、指數動能、crash filter）
- Ch9 回測實作（資料準備、survivorship bias、look-ahead bias）
- Ch10 年度交易回顧（2000-2014 逐年 P&L 分析、2008 與 2011 的 drawdown 心理學）
- Ch11 Python/Matlab 實作建議

### TL;DR (≤120字)
Clenow 把 ACIES Asset Management 管理十年的動能策略完整公開：策略核心「買入上漲的股票」配合 ATR 波動正規化 + exponential regression slope 排名 + 市場環境過濾器，2000-2014 SPY 漲 60% 時策略漲 600%；書的真正價值在 Ch10 逐年交易筆記揭示動能策略長期有效但心理難捱。

### 核心本質 (3-5 條)
1. **簡單策略經得起時間考驗**（本質） — Ch1 Clenow 直言：動能策略的核心「買上漲、賣下跌」無法被「更複雜」改進；增加 20 個指標、10 個 filter 只會讓 backtest 更漂亮、實盤更差（overfitting）。Edward 的自營系統原則應對齊：初版用 3-5 條 rule 即上線，而不是追求「最優化」所有參數。
2. **Exponential Regression Slope + R² 是動能的量化語言**（本質） — Ch4 核心：用 90 日對數價格做指數迴歸，slope 代表年化動能、R² 代表線性（趨勢品質）；score = annualized slope × R²。這比簡單的 return 排名更 robust，因為 R² 懲罰「突然漲跌」的假動能。
3. **ATR 正規化解決跨股票可比性**（本質） — Ch4 與 Ch6：不同股票波動率不同，純 return 排名會偏向高波動小市值股；用 ATR 標準化後，不同波動率的股票可公平比較；部位用 1/ATR 加權，風險預算平均分配到每一筆。
4. **Market Regime Filter 是動能的救命符**（本質） — Ch8：當 S&P 500 跌破 200 日均線時停止新進場、逐步出清舊部位；這一條 rule 讓策略在 2008、2020 COVID 急跌中倖存；動能策略 without regime filter 會在 crash 中毀滅（Asness 發現純動能在崩盤當月可跌 40%）。
5. **心理耐性 > 策略本身**（本質） — Ch10 逐年回顧震撼：動能策略有 2-3 年連續跑輸 SPY 的時期（2001、2011），連續 18 個月 drawdown 是常態；沒有足夠心理準備的人 5 年內必放棄並在最低點割肉。Edward 需評估自己對動能策略的 temperament fit。

### 可用戰術/策略
- **Score 公式 = annualized_slope × R² × risk_adjust**：直接可編程，用過去 90 日對數價格線性迴歸取得 slope 與 R²。
- **Portfolio 構建法則**：前 Top-N（通常 10-20% 股票池）做多，等權重 or 1/ATR 加權；週一或月一檢視是否需換股。
- **ATR-Based Position Sizing**：每股頭寸 = Target Portfolio Vol / (stock ATR × position count)；目標 vol 通常設 10-15%。
- **200DMA Regime Filter**：指數 < 200 日均線 → 停止新進場、現有部位逐步減倉；指數 > 200 日均線 → 正常運作。
- **流動性與 Corporate Action Filter**：ADV < $10m 或月內有 split/spin-off/merger 的股票排除；避免 liquidity trap 與 data contamination。

### 盲點 / 反例 / 適用邊界
- **2000-2014 美股大多頭樣本**：書中驗證期恰好是美股 secular bull market；2015-2022 的低利率環境 + tech-narrow leadership 讓動能策略表現平庸；在真正 bear market（1970s stagflation）的穩健性未驗證。
- **忽略交易成本詳細模型**：Clenow 假設 $0.01/share commission；若在台股（0.1425% + 0.3% sell tax）或新興市場，同樣策略報酬率會被吃掉一半以上。
- **動能策略 crash risk 本質（Moreira-Muir 研究）**：即使加 200DMA filter，動能仍是 short volatility 特性；book 未深入 Asness、Moreira、Muir 的 momentum crash literature。
- **Survivorship bias 的殘留**：雖然作者聲稱排除，但真正 survivorship-free 資料極昂貴且繁雜；retail 讀者自己回測時 99% 會帶入 bias。
- **Smart Beta 興起後動能已擁擠**：2015 後 MTUM ETF 讓動能策略 AUM 飆升，alpha 快速衰減；書中效應有部分是 pre-crowding 環境產物。

### 與 Edward 既有知識的連結
- **對齊 ZP 核心**：「簡單策略經得起時間考驗」對應零式投資本質 — 增加複雜度通常降低 robustness；Edward 的 B2 策略初版應遵循 3-5 條核心規則 + 1-2 條 meta regime filter。
- **延伸既有 DNA**：Exponential regression slope 與 R² 的 score 設計可用於評估「永生樹分支的成長動能」— 某子專案的 commit velocity × 完成率 R² 可作為是否加碼資源的量化指標。
- **衝突點**：Clenow 完全專注在股票做多端；Edward 若擴展到加密、期貨、選擇權 market making，動能策略不是主角；但 regime filter 概念仍通用。
- **可挖金礦**：Ch11 Python/Matlab 實作建議可直接落地，配合台灣上市股票資料（以台股 50 為池）做類似策略；主要需修改交易成本模型 + 除權息處理；若每月換股頻率且稅金壓縮後還能打贏 0050 年化 3%，就值得當做 B2 的 systematic equity leg。
