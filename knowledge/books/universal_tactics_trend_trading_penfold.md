# The Universal Tactics of Successful Trend Trading — Brent Penfold

### 目錄
1. 核心本質 — Trend Trading 的四大核心：Knowledge / Risk / Application / Execution
2. 可用戰術 — Donchian breakout、ATR 停損、跨市場 diversification
3. 盲點/反例 — 2020 代 market regime 對 classic trend 的挑戰
4. 與 Edward 既有知識的連結

### TL;DR
Penfold (Wiley 2021, 多章節, 涉及 Knowledge/Risk/Application/Execution 四大支柱) 是澳洲資深系統交易員 Brent Penfold (1962 出生) 的 trend trading 綜述書，接續他 2010 年《The Universal Principles of Successful Trading》的續作。**核心結構**：Ch 1 The Paradox（trend trading 的心理困境——明知機械系統有效但難以長期 follow）、Ch 2 Key Messages 四大支柱（知識/風險/應用/執行）、後續章節展開每個支柱的實務細節。Penfold 自己是 Darvas Box 方法與 Turtle rules 的老派繼承者，但加入了更現代的 vol-scaling 與 risk parity 觀念。全書**最大價值**：他以 40 年交易經驗（1982 出道），經歷了 87 黑色星期一、97 亞洲金融風暴、08 金融海嘯、20 COVID——把不同 regime 中 trend trading 存活的共同 pattern 提煉成 Universal Tactics。核心訊息：**trend trading 不是演算法問題，是心理問題**——80% 的失敗者有正確的規則但執行不來。

### 核心本質
1. **Knowledge 是 Trend Trading 的 Foundation（Ch 2 Knowledge 一節）**：Penfold 要求 trader 先懂 (a) market structure（bid-ask, 流動性, spread, slippage）、(b) 合約規格（futures multiplier, margin, roll schedule）、(c) trend 的統計特性（fat-tailed distribution, serial correlation pattern）。若不懂「為什麼 trend exists」（典型解釋：risk premium + behavioral under-reaction + leverage constraints），就無法在 drawdown 時堅持下去。
2. **Risk Management 排第二優先（Ch 2 Risk 一節）**：Penfold 的第一條 rule——「trade small, trade long」。每筆 risk ≤ 1% total equity、total portfolio open risk ≤ 10%、single market 開倉 ≤ 3 倉。他的依據是 Ralph Vince 的 ruin theory——風險過大會在連續 losers 中讓帳戶進入不可恢復區（破產吸收態）。
3. **The Paradox（Ch 1）**：trend trading 系統提供的是「簡單規則+長期穩定報酬」，但散戶最難 follow 的也是「紀律 + 連續虧損後不亂調參」。Penfold 引用自己交過的 300+ 散戶學員——所有表現好的都是有系統 + 堅持執行，不管系統多 sophisticated。所有失敗的都是在 drawdown 20% 時「改參數」「放棄系統」「加碼」。
4. **Execution 是最後一道關卡（Ch 2 Execution 一節）**：有了 knowledge + risk + application 仍不夠——現實交易要面對 slippage、unfilled order、broker outage、data feed error。Penfold 強調至少要有 2 個 independent broker、每日 reconciliation、自動 stop loss 放市場而非 mental。2015 CHF unpeg 時他因為 stop loss 在 exchange 才沒爆倉。
5. **Find Opportunity in Uncertainty（書副標）**：trend trading 本質上是 bet on volatility of volatility——market regime shift 時 trend 最明顯（Phase transition）。Penfold 統計：2000 tech bust、2008、2015 oil crash、2020 Mar 都是 trend trader 最賺錢的時段，而平穩年（2013, 2017, 2019）反而 breakeven 或小虧。

### 可用戰術
1. **Donchian 20-day Breakout + ATR Stop**：這是 Turtle 原版+Penfold 改良。buy when close > 20-day high, sell when close < 10-day low. Stop loss at entry_price - 2×ATR。Penfold 測 1990-2020 在 30 個 futures 上年化 Sharpe 0.6, max DD 35%——不 glamorous 但 stable。
2. **Vol Targeting at Portfolio Level（Ch 2 Risk）**：整體 annual vol target 15%，若當前 portfolio vol > 18% 則按比例減倉。這讓策略在 2008、2020 這類 crisis 自動 deleverage，降低 ruin 機率。
3. **Donchian Exit 早於 Signal Reverse**：entry 用 20-day breakout，exit 用 10-day breakout（方向相反）。exit 更快減少 round-trip drawdown，比 entry-exit 對稱的版本年化多 2%。
4. **Skip Small Signals**：Penfold 提 signal 必須至少 1.5×ATR deep into breakout 才算有效——排除 flash spike 與 noisy whipsaw。這個 filter 把 trade frequency 降 20% 但勝率提 10%。
5. **Uncorrelated Market Grouping**：把 30 個 market 歸 5-6 組（equity indices, rates, currencies, metals, energy, softs），每組 active position ≤ 2 + total ≤ 10 prevent 集中在同一 theme。Oil + gold + copper 同一天 trigger 是 warning——可能不是獨立 bet 而是通膨主題的多面 exposure。

### 盲點/反例
1. **2021 出版恰逢 QE 退場前夕，未反映 2022-2023 rate hike 週期的新動態**：2022 Fed 升息讓 bond-commodity-equity correlation 全盤翻轉（60/40 failure），傳統 trend framework 在 2022 年 SG Trend Index 還是賺（+25%）但 2023 年回吐。Penfold 寫作時沒預見 post-covid 通膨 regime。
2. **純 discretionary 與 systematic 界線模糊**：書中 Penfold 又講「系統紀律」又鼓勵「market intuition」，某些章節建議 discretionary override signal。這個「灰色地帶」對散戶不友善——要嘛全 systematic 要嘛全 discretionary，mixed mode 容易藉口。
3. **沒 ML / alternative data**：2020 後 CTA 普遍加 satellite imagery（for oil storage, crop yield）、natural language sentiment 等 alt data，Penfold 停在純 price-based indicator。
4. **Back-test 樣本有限**：書中實證多半 1990-2020 期間（30 年），但 2008 前 commodity trend 比 2008 後好得多（pre-GFC 每年平均 Sharpe 1.0, post-GFC 降到 0.3）。不分 sample 的整體 stats 誤導。
5. **Australia/Futures 偏向，缺 equity/options/crypto**：Penfold 主要交 ASX + US futures，對 crypto 只輕描淡寫。2021 年後 crypto trend following（e.g., BTC momentum）是新 opportunity set，書中未涵蓋。

### 與 Edward 既有知識的連結
- **對照 Clenow《Following the Trend》（本輪）**：Clenow 是 institutional CTA 視角（systematic diversified futures），Penfold 是 retail 視角（individual trader 角度）。內容大量重疊但取向不同——Clenow 要你模仿 Winton，Penfold 要你生存下去賺小錢。
- **對照 Faith《Way of the Turtle》（Round 1）**：Penfold 明顯是 Turtle 派繼承者——Donchian breakout、ATR sizing、rule-based exit 一脈相承。但 Penfold 加了 post-2000 的 vol targeting 觀念，對現代市場更 robust。
- **對照 Davey《Building Winning Algo Systems》（本輪）**：Davey 的「Monte Carlo + incubation」process 與 Penfold 的 Knowledge/Risk/Application/Execution 四支柱互補——Davey 著重個別策略驗證，Penfold 著重整體 trader 素養。
- **對照 Psychology of Money (Round 1, Kingsbury)**：兩本都強調心理紀律是長期致勝關鍵。Psychology of Money 從普通投資人視角，Penfold 從專業 trader 視角，但核心都在「時間架構 + 紀律 + 避免破產」。
- **對照 ZP/strategies/discretionary 分支**：Penfold 的 Paradox（系統規則有效但執行難）對 ZP 是警告——我不能只寫好策略 code，還要設計「系統無法被我 override」的機制（例 stop loss 設 exchange 不用 mental、参數修改需 ZP-wide approval）。
- **對照 Poker 的 tilt control**：撲克的 bad beat 後情緒失控類比 trend trading drawdown 後亂調參數。兩個領域的頂尖玩家都有一套「發現自己 tilt 就走人」的 early warning + circuit breaker 機制。
