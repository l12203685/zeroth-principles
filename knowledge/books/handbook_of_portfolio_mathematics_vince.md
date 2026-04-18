## The Handbook of Portfolio Mathematics — Ralph Vince
**來源**: E:/書籍/Ralph Vince-The handbook of portfolio mathematics-Wiley (2007).pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Part I: Theory
  - Chapter 1: The Random Process and Gambling Theory
  - Chapter 2: Probability Distributions
  - Chapter 3: Reinvestment of Returns and Geometric Growth Concepts
  - Chapter 4: Optimal f
  - Chapter 5: Characteristics of Optimal f
  - Chapter 6: Laws of Growth, Utility, and Finite Streams
  - Chapter 7: Classical Portfolio Construction
  - Chapter 8: The Geometry of Mean Variance Portfolios
  - Chapter 9: The Leverage Space Model
  - Chapter 10: The Geometry of Leverage Space Portfolios
- Part II: Practice
  - Chapter 11: What the Professionals Have Done
  - Chapter 12: The Leverage Space Portfolio Model in the Real World

### TL;DR (≤120字)
Vince 把 Kelly Criterion 拆解、延伸、再升級為 "Optimal f" 與 "Leverage Space Model"：單一策略的最佳部位 f* 由幾何增長率推出；多策略組合不是 mean-variance 而是 leverage-space 幾何結構；真正能優化的是「回撤約束下的回報」不是「給定波動度下的回報」。

### 核心本質 (3-5 條)
1. **Geometric Growth > Arithmetic Mean**（本質，第 3 章） — 複利化投資的長期績效由 geometric mean 決定，不是 arithmetic mean。50% 漲 + 50% 跌（算術均值 0）的幾何均值是 -13.4%——連續兩次變 0.75。這個反直覺事實是 Vince 全書的邏輯基石。
2. **Optimal f 取代 Kelly 公式**（本質，第 4 章） — Kelly 公式假設 win/lose 二元結果；真實交易有連續回報分布。Vince 的 f* = argmax 幾何均值，透過 Terminal Wealth Relative（TWR）最大化求得。對有固定虧損金額（止損）的交易系統，f* = -A/minimum_loss，其中 A 是最優部位比例。
3. **Drawdown 才是真正的 risk，不是 variance**（本質，第 6 章） — Markowitz 的 variance 懲罰了 upside 波動，是錯的 risk proxy；投資人真正恐懼的是回撤。Vince 重構最優化框架為「最大化回報 subject to drawdown constraint」，這比 mean-variance 更貼近實際投資人效用函數。
4. **Leverage Space Model 是多策略最佳化的正確幾何**（本質，第 9-10 章） — 傳統 Markowitz 在 (return, variance) 2D 平面；Vince 在 N 維 leverage space（每策略的 f 值）中找 peak of geometric growth surface。此 surface 是凸的，單峰，有唯一最優；但對相關性高度敏感，regime change 時最優 f 會瞬移。
5. **負期望值系統無論怎麼下注都輸**（本質，第 1 章） — Vince 用賭博期望值的加總性質（ME of series = sum of individual ME）證明：任何試圖「輸了就加倍」（Martingale）、「贏了就加碼」等 money management 技巧，面對負期望值 edge 都無效。前提永遠是先確保 positive edge。

### 可用戰術/策略
- **f* 計算 cookbook**：(1) 收集策略 100+ 筆歷史交易的 P/L；(2) 用 parabolic interpolation 在 [0, 1] 區間找 TWR 最大值對應的 f；(3) 用 f/N（N 為安全係數 2-4）實際交易，保留 drawdown buffer。
- **Geometric 止損決策**：當累積 drawdown 達 Vince 模型預測的 max DD * 0.5 時，暫停該策略；複利受損比名義虧損嚴重得多。
- **Equalizing Optimal f**（第 4 章末）：多商品組合時，把每個商品的 f* 調整到「相同風險貢獻」而非相同絕對 f，降低單一商品爆掉的 tail risk。
- **Leverage space heat map**：每月重算 (f1, f2, ..., fn) surface，檢查當前策略組合是否仍在 peak 附近；若偏離 >10%，重新平衡。
- **避免連續贏後加碼**：Vince 明確警告——連勝後的信心驅動加碼是 ergodicity 違反；幾何增長會被一次大回撤抹平，必須機械化維持 f*。

### 盲點 / 反例 / 適用邊界
- **Fat tail 下 f* 崩潰** — Vince 的 TWR 假設有限 variance；若策略分布有無限 variance（如裸賣 OTM put），f* 公式不收斂，實作會推出激進過高的 f。期權賣方、CDO、crypto 高槓桿期貨直接套用會災難。
- **過度依賴歷史分布** — f* 是歷史 fit 最佳解，regime change 後的 out-of-sample f* 往往偏離歷史值 50-100%；Vince 建議用 f/2 或 f/4 本質上是 ad hoc fudge factor，缺乏理論依據。
- **忽略交易成本** — 書中計算 f* 時常假設 zero commission 與 zero slippage；實際 f* < 理論值通常 10-30%，因為高頻觸及止損時的摩擦會吃掉 edge。
- **Leverage Space 在高相關時退化** — 多策略如果相關性 → 1（危機時常見），leverage space surface 變平，最優 f 無意義；Vince 對 correlation regime shift 的處理相對薄弱。
- **書名誤導** — 叫 "portfolio mathematics" 但大半是 single-asset 賭博理論；portfolio 章節（7-10）只佔書的一半且偏理論，實務操作者期望的 multi-asset portfolio 建構細節不足。

### 與 Edward 既有知識的連結
- **對齊 ZP 零式本質**：「期望值為正是萬法之始」與 Edward 的零式對齊檢驗同構——任何加碼/減碼技巧都是 second-order，edge 正負是 zeroth-order。
- **延伸海龜交易法則**：費思的 2N 止損 + 1% 風險就是 Vince 的 f* 在保守化後的簡化版；海龜書沒說的數學推導 Vince 補齊了。
- **對應 DNA §5 交易心態**：Vince 的 "drawdown is the real risk" 與 Edward 對 CTBC 自營部離職的決策邏輯一致——不是擔心 variance 而是 survival 問題。
- **衝突點**：Vince 的 Optimal f 是 Kelly 激進版，對大部分散戶（包括 Edward）都太激進；實務用 Kelly/4 或 Kelly/8 更安全。
- **可挖金礦**：第 12 章 Leverage Space Portfolio Model in Real World 的計算範例可作為 `ZP/quant/portfolio_optimization/` 的 reference implementation，優於傳統 Markowitz。
- **Poker 應用**：Vince 的 geometric mean + f* 正是職業 poker bankroll management 的理論——玩多大 stakes 由 bankroll × Kelly fraction 決定，不是由勝率決定。
