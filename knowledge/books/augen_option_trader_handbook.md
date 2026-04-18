## The Option Trader's Handbook — Jeff Augen
**來源**: E:/投資交易/交易學習資料庫/@交易/@選擇權/Jeff Augen - The Option Trader's Handbook.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Pricing Basics（隱含波動率、skew、Greeks 基礎）
- Ch2 Purchasing Puts and Calls（7 個基本 + 12 個 protection + 19 個 defensive problems + 8 個 skew/theta problems）
- Ch3 Covered Puts and Calls（23 個 traditional + 5 個 pure option covered 問題）
- Ch4 Complex Trades - Part 1（15 個 vertical spreads + 15 個 calendar spreads + 4 個 diagonal + 7 個 ratio trades）
- Ch5 Complex Trades - Part 2（8 個 butterfly + 8 個 straddle/strangle + 6 個 four-part + 2 個 VIX + 1 個 dividend arb）

### TL;DR (≤120字)
Augen 把整本書設計成 problem-solution 格式：每個期權情境先給「建倉後市場動了 X%」，再問「下一步怎麼調整」。核心訊息：期權交易不是「一次下注」而是「動態管理」，大部分 PnL 來自調倉決策而非初始選擇；90% 的書只教建倉，此書專教 defensive adjustment。

### 核心本質 (3-5 條)
1. **Option = 動態管理不是一次性決策**（本質，全書基調） — 傳統期權書教 "buy call when bullish"，但真實 trader 90% 時間在調倉：部位獲利後 roll up、部位虧損後 roll out、隱含波動率變化後 restructure。這本書把「建倉後怎麼辦」從附錄升格為主旨。
2. **Defensive Action 是期權交易的核心技能**（本質，Ch2 第 20-38 題） — 當 short put 被 ITM 套牢，你可以：(a) 接受 assign + 合成 covered call 轉多頭持有；(b) roll forward + roll down；(c) 轉 spread 降低風險；(d) 轉 iron condor 做兩邊 range。每個選擇的 payoff、BE、新 Greek 都需計算。書中逐題示範。
3. **Vertical, Calendar, Diagonal, Ratio 四類 spread 的 context 選擇**（本質，Ch4） — Vertical = directional + limited risk；Calendar = 吃 theta decay + volatility exposure；Diagonal = 同時做 directional + time + vol 三維；Ratio = 非對稱 payoff。Augen 按每題情境示範選哪一種最優。
4. **Butterfly ≠ 中性策略**（本質，Ch5） — 常見誤解 butterfly 是 "low-risk market-neutral"；實則 butterfly 的 gamma 在中間 strike 達最大負值，若市場短期震盪會快速虧損。Augen 用多個 example 示範 butterfly 的正確使用情境（預期超低波動 + 時間 decay）。
5. **Volatility Index (VIX) 作為對沖工具**（本質，Ch5） — 直接買 VIX options 或 VIX futures 作為 portfolio tail hedge；當 S&P 跌 VIX 通常飆，但 VIX options 自身 skew 極陡，長期持有 VIX call 的 cost-of-carry 會吃掉保護價值。Augen 示範何時 short-term buy VIX protection 划算。

### 可用戰術/策略
- **Rolling Strategy Flowchart**：short option ITM → 判斷 days to expiry。DTE > 45 → roll same strike 向後一個月；DTE < 45 → roll down + forward（wider spread, later month）。
- **Short Put Defense**：當 AAPL 150 put short，股價跌到 145 時：(a) 如願意擁有 AAPL：讓 assign；(b) 若不願意：roll to 140 strike + next month，收取額外 credit。
- **Calendar Spread for Earnings**：earnings 前 1 週建 long back-month / short front-month same strike；earnings 後 IV crush 使 front-month 大跌，back-month 保留 gamma，賺取 vol skew。
- **Ratio Spread for Skew**：當 put skew 極陡（far OTM puts expensive），建 1:2 put ratio——long 1 near-money put + short 2 far-OTM puts；賺取 skew 回歸但需控制 tail risk。
- **VIX-SPX Pairs Hedge**：每月用 portfolio value 的 0.5-1% 買 VIX 1-month OTM call；災難時 VIX 3-5 倍槓桿放大，80% 平靜時權利金歸零。

### 盲點 / 反例 / 適用邊界
- **全部是 US equity option**，未涉及 commodity、FX、index option 的特殊 mechanics（如每月 settlement vs continuous, European vs American, cash-settled vs physical）。
- **2013 年出版，未涵蓋 0DTE 革命**（每日到期期權）——2020 後 SPX weekly expiry 變 daily，改變了 gamma exposure 結構；Augen 的 theta decay 策略在 0DTE 世界需要重構。
- **手工計算示範多** — 書中 example 多用紙筆計算，實務需用 TradingView / ThinkOrSwim / QuantConnect 即時計算 Greeks；純看書學習到下單會有 gap。
- **缺機率思維** — Augen 專注「這筆交易下一步怎麼辦」，但對策略整體期望值、100 次交易後的分布、Kelly fraction 等 meta-level 討論不足。需搭配 Sinclair《Option Trading》補強。
- **problem-solution 格式的侷限** — 書中 problem 是 curated scenarios，現實市場可能同時觸發多個情境（IV crush + delta move + skew shift），需綜合應用。

### 與 Edward 既有知識的連結
- **對應 Natenberg**：Natenberg 建立直覺，Augen 練習解題；兩本搭配才完整。Edward 自營期權交易應先讀 Natenberg 打基礎，再做 Augen 的 75 道題目磨練反射。
- **對應 Higham**：Higham 的 BS pricing 程式碼可直接拿來計算 Augen 題目的 payoff / Greeks，整合為自己的 option calculator 工具。
- **實戰 ZP 應用**：Ch3 Covered Call 策略可作為 Edward 長期持股（台股 2330 等）的增強回報工具；每月 short call 預計年化增加 5-15% premium income。
- **衝突 HFT 立場**：Augen 的 defensive adjustment 是 human decision，不可自動化；自營 HFT 策略無法直接套用 Augen 思維，必須預先 encode 規則。
- **可挖金礦**：75+ problems 可改寫為 `ZP/options/training_problems/` 模組，Edward 每週自解 3-5 題保持交易決策肌肉；不同 strike/expiry/IV 組合的決策樹可 tabulate。
- **Poker 類比**：Augen 的 "continuation after action" 思維對應 poker 的 "line building"——每個 action 後基於新資訊重新判斷最優下一步，不是預設完整 plan。
