## Fortune's Formula — William Poundstone（Kelly 準則與華爾街科學賭博史）
**來源**: staging/b2_batch_D_extracts/11c63c11b38cac78__fortune_s_formula... | **消化日**: 2026-04-18 | **模型**: opus-4.7 | **Round**: llm_round_6

### 目錄
- Prologue: The Wire Service（Payne 電報+黑手黨賭盤起源）
- PART ONE: ENTROPY（Shannon / Kelly 1956 論文 / Edward Thorp 初登場 / Gambler's Ruin / John Kelly Jr.）
- PART TWO: BLACKJACK（Reno & Vegas / Thorp 與 Kelly Criterion 實戰 / Las Vegas 首場穩贏系統）
- PART THREE: ARBITRAGE（Samuelson / Random Walk / Beat the Market / Merton / Princeton-Newport / Milken）
- PART FOUR: ST. PETERSBURG WAGER（Bernoulli / Latane / Shannon's Demon / Markowitz 爭議）
- PART FIVE: RICO（Ivan Boesky / Giuliani / Princeton-Newport 被起訴）
- PART SIX: BLOWING UP（Martingale / LTCM 與 Fat Tails / Survival Motive）
- PART SEVEN: SIGNAL AND NOISE（Shannon's Portfolio / 指標計畫 / 香港集團）

### TL;DR (≤120字)
Poundstone 以「一位電報員的舞弊→Shannon 資訊理論→Kelly 1956 論文→Thorp 賭場與華爾街實戰→Princeton-Newport 合夥公司→LTCM 崩盤」串起科學賭博 50 年史。核心論點：**Kelly 準則 f\* = edge / odds 是長期幾何增長的最優解，但代價是高波動與短期 drawdown**；大多數專業交易者應用 Half-Kelly 或 Fractional-Kelly 以換取心理可承受性。本書是理解「資金管理」與「長期增長率」的必讀史學敘事。

### 核心本質 (3-5 條)
1. **Kelly = 幾何增長最大化**（本質，Part One & Two） — Kelly 1956 在 Bell Labs 論文用「賽馬資訊傳輸」類比，推出 f\* = (bp - q) / b，其中 p 為勝率、q=1-p、b 為賠率。最大化 E[log(wealth)] 而非 E[wealth]；對數效用保證「幾乎必然」（almost surely）長期複利率最高。
2. **Shannon's Demon**（本質，Part Four） — Shannon 在 MIT 給出反直覺演示：即便單一資產期望值為零，用 50/50 rebalance 可產生正的幾何增長率（波動率收穫 volatility harvesting）。這預示了現代「rebalancing premium」與 Markowitz portfolio 的再平衡價值。
3. **Samuelson vs Kelly 學術戰爭**（本質，Part Three） — Samuelson、Merton 等新古典經濟學家嚴厲反對 Kelly：若效用函數非對數（例如風險規避度更高），Kelly 是次優。但 Thorp、Latane、Ziemba 等實戰派堅持：長期複合增長者應逼近 Kelly。這是「理論效用 vs 長期存活」的世紀辯論。
4. **Princeton-Newport：首檔量化避險基金**（本質，Part Three & Five） — Thorp 與 Regan 1969-88 運作 PNP，20 年無虧損年、年化 ~19%；用「凸性套利」（convertible bond + 股票對沖）賺取 edge。1988 被 Giuliani RICO 調查瓦解——並非因交易違法，而是政治打擊。啟示：edge 可以極大，但合規與法律風險是隱含左尾。
5. **LTCM 是 Anti-Kelly 的反面教材**（本質，Part Six） — LTCM 以槓桿 25x+ 下 fat-tail 暴露；Kelly 原則會建議「下注應遠小於此」。1998 年崩盤印證：若 f > f\*（overbetting），長期破產機率 → 1。Taleb 在本章登場，後來寫《黑天鵝》。

### 可用戰術/策略
- **Kelly 計算公式**：對於任一交易訊號，計算勝率 p、平均賺/賠比 b=win/loss ratio，f\* = p - (1-p)/b。實務使用 0.25-0.5 × f\* 以容忍參數估計誤差與規避左尾崩盤。
- **Half-Kelly / Fractional-Kelly**：Thorp 本人用 Half-Kelly——犧牲 25% 長期增長率，換取 50% 的短期波動率降低；心理與業務可持續性顯著提升。
- **動態 rebalance = Shannon's Demon**：對於 2+ 無相關資產，定期（月/季）重新調整回目標權重，即使個別資產 E[r]=0 也可獲得正幾何增長。
- **Drawdown 上限規則**：Kelly 最大化 E[log W] 但對應 drawdown 分佈為「任意比例 x 的最大回撤機率 = x」。預設 50% drawdown 可能發生一次於職業生涯。Fractional-Kelly 可將此降至 25% 或以下。
- **Edge 估計校準**：Kelly 對輸入誤差極敏感。若真實 edge 被高估 2x，即用 Full Kelly 會導致破產。Thorp 建議：用歷史樣本外測試 + 3σ 保守估計。

### 盲點 / 反例 / 適用邊界
- **需要重複、獨立、可估計的 edge**：Kelly 假設每次下注結構穩定、概率可估。現實市場 regime 會變，edge 衰減；盲目應用 Kelly 會在 regime shift 時災難。
- **忽略交易成本與滑點**：原始公式不含摩擦。實戰中 edge 要先扣除 commission + slippage + impact cost 再輸入 Kelly。
- **效用函數爭議**：若你非「對數效用」（例如有養老金硬目標），Kelly 未必最優；需考慮 target-date 的 shortfall risk。
- **心理承受度**：Full Kelly 的波動率令大多數人無法執行。Thorp 和 Ziemba 都強調：能執行的 Half-Kelly 遠勝於無法堅持的 Full Kelly。
- **書籍敘事偏英雄化**：Poundstone 以 Thorp 為主角，低估了同代其他量化先驅（Simons 僅輕描寫）；讀者應配合《The Man Who Solved the Market》補 Renaissance 視角。

### 與 Edward 既有知識的連結
- **對齊 ZP 零式本質**：Kelly 「最大化長期幾何增長率」＝ ZP 資金管理的數學本質；Edward 的「經濟自給 + 永續」正是 Kelly 命題，即 survival 優先於單期最大 EV。
- **延伸 Fooled by Randomness（Taleb）**：Taleb 在 Part Six 登場並警告 LTCM，呼應其後《Black Swan》。本書可視為 Taleb 思想的「前傳」。
- **對接撲克背景**：Kelly 準則在撲克 bankroll management 為基石（Harrington、Sklansky 引用），Edward 撲克經驗可直接映射到交易資金管理。
- **衝突點**：Samuelson 學派主張 MPT / 現代投資組合理論為主；Edward 若選 Kelly 路線，需先建立「為何我選 log-utility」的零式論證。
- **可挖金礦**：Shannon's Demon（rebalancing premium）可整合入 ZP/portfolio/ 作為低相關資產動態配置的理論基礎；這與 ZP/knowledge 既有的 Bodie & Kane 教材可形成互補。
