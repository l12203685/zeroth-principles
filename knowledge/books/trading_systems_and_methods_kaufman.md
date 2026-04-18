## 交易系統與方法 (第 5 版) — Perry J. Kaufman

**來源**: E:/書籍/Trading Systems and Methods, Perry J. Kaufman.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 緒論（系統化交易的定義、為何使用系統、本書結構）
- 第 2 章 基礎概念（報酬計算、複利、夏普比率、MAR 比率、最大回撤）
- 第 3 章 圖表學（道氏理論、K 線、趨勢線、支撐阻力、箱型）
- 第 4 章 圖表形態（頭肩、三角、旗形、缺口、Gann 角度）
- 第 5 章 事件驅動與季節性（年/月/週效應、過期日、期權到期、持倉報告）
- 第 6 章 回歸分析（線性、對數、殘差分析、多元回歸的變數選擇）
- 第 7 章 時間序列與線性方法（ARMA/ARIMA、Hurst 指數、光譜分析）
- 第 8 章 趨勢計算（移動平均 SMA/EMA/WMA/Kaufman AMA、拐點判定）
- 第 9 章 動量與振盪器（RSI、MACD、隨機指標、過濾規則）
- 第 10 章 季節性與週期交易（日曆套利、週期濾波、Fourier）
- 第 11 章 突破系統（Donchian、Turtle、波動率突破、Bollinger 突破）
- 第 12 章 型態識別（candlestick、三兵、晨昏星、N 字結構）
- 第 13 章 交易組合與配對交易（價差比例、協整、StatArb）
- 第 14 章 波動率與風險模型（ATR、GARCH、VaR、regime shifts）
- 第 15 章 系統績效（Sharpe、Sortino、Calmar、walk-forward）
- 第 16 章 資金管理與頭寸規模（Kelly、fixed fractional、最優 f）
- 第 17 章 投資組合建構（min-var、risk-parity、相關性矩陣估計）
- 第 18 章 系統實作（滑點、延遲、限價/市價、資料品質）
- 第 19 章 系統哲學與心理（過擬合、資料挖掘偏差、研究紀律）

### TL;DR (≤120字)
這本 1,200 頁的百科是「系統交易的 SICP」，Kaufman 30 年交易系統研究集大成。不提供聖杯策略，而是教你如何**把任何市場直覺數學化、回測、套上風險模型、組合成分散化系統**。特別珍貴是每章都附公式 + Excel/TradeStation 代碼 + 反例警告，是少見敢承認系統局限的實戰書。

### 核心本質 (3-5 條)
1. **系統化 ≠ 自動化**（本質） — Kaufman 在第 1 章明確區分：系統化指的是「規則可重複 + 結果可測量 + 邊緣可驗證」，與是否由電腦執行無關。手動執行嚴格規則的交易者也是系統化的；相反，即使跑在 C++ 的混亂 tinkering 也不是系統化。這顛覆了「algo = system」的誤解，把紀律放在工具之上。
2. **Kaufman 自適應移動平均（KAMA）= 市場微觀結構對觀察窗口的適應**（本質） — 第 8 章的 KAMA = EMA(ER × fast + (1-ER) × slow)，ER 為 Efficiency Ratio（訊號/噪音比）。這不只是個指標，而是**自動切換 regime 的元框架**：趨勢市場用短週期（反應快），盤整市場用長週期（過濾噪音）。所有 regime-switch 模型的直覺先驅。
3. **每個指標都是對「趨勢定義」的一種表態**（本質） — 第 8-11 章貫穿：沒有「客觀的趨勢」，只有「以 X 窗口、Y 濾波定義下的趨勢」。同一段價格可以同時在 10 日 SMA 下是上升趨勢、在 200 日 SMA 下是下降趨勢。承認這點後，「組合多趨勢定義」才有理論依據（而不只是 diversification 修辭）。
4. **滑點、延遲、手續費決定策略存活，而非訊號強度**（本質） — 第 18 章實作章節毫不留情：高頻策略的邊緣若在每筆 2 tick 以下，實盤執行必吃光 alpha。Kaufman 給出明確公式 `實際邊緣 = 理論邊緣 − 2×spread − 1×commission − 0.5×slippage`，並指出 retail broker 下單介面的 60-200ms 延遲足以摧毀大多數日內訊號。
5. **過度擬合 = 研究者自由度的平方**（本質） — 第 19 章的黃金句：若你嘗試了 N 個參數組合，則最佳績效的 p-value 應乘以 N，不是按原始回測比例。一個看起來 Sharpe 2.0 的策略若經過 200 次參數嘗試，實際期望 Sharpe 可能只有 0.3。Bonferroni 修正 + walk-forward 是唯一誠實的回測方式。

### 可用戰術/策略
- **KAMA 規則**：`ER = |Price[t] − Price[t−n]| / Σ|Price[i] − Price[i−1]|`，當 ER > 0.5 用 2-day EMA，ER < 0.3 用 30-day EMA；實戰上可替代 retail 常用的 EMA 組合過濾。
- **波動率突破 (Bollinger + ATR 複合)**：開盤價 ± k×ATR(20) 作為當日進場觸發，k=1.5 日內策略、k=3 搖擺；第 11 章給出 1980-2012 在商品/股指的回測分布。
- **walk-forward 研究協議**：把 10 年資料切成 10 個 1 年視窗，在 t1-t5 優化、t6 測試；向前滾動；最終只採用「在 8/10 視窗保持正報酬」的參數族，避免 curve-fit。
- **最優 f 的保守版（Kaufman fractional f）**：建議用 Ralph Vince 最優 f 的 1/4 到 1/2（因樣本偏差使真實最優 f 低於回測估計），第 16 章給出模擬實證顯示全最優 f 的毀滅機率約 15%。
- **相關係數動態估計**：不用樣本相關係數而用 EWMA(λ=0.94)，在 2008-style 危機時相關係數會快速上升，觸發降槓桿規則而非等月底重平衡。

### 盲點 / 反例 / 適用邊界
- **所有回測默認流動性充足** — 第 11-13 章的大量策略 Sharpe 數字在 1M 美元資金下有效，但 100M+ 會被市場衝擊吃光；Kaufman 在版本更新中補充警告，但正文仍充斥「策略可縮放」的樂觀假設。
- **指標章節過於包容** — 第 8-12 章收錄了 50+ 個指標，有些（如 Commodity Channel Index 的固定常數 0.015）的理論基礎極弱，但書中給予相同權重呈現，初學者易誤信所有指標都具統計顯著性。
- **未處理交易員偏見的心理學** — 儘管第 19 章談過擬合，但對「研究者情緒影響參數選擇」缺乏結構化討論（對比 Kahneman/Tversky 或 Steenbarger 的行為金融實證）。
- **固定 regime 思維** — Kaufman 的案例多在 1980-2010 年間，該時期趨勢性顯著；2010 後的零利率 + QE + passive flow 環境下很多趨勢策略 Sharpe 減半，本書未更新此時期數據。

### 與 Edward 既有知識的連結
- **補強 ZP 核心**：Kaufman 的「系統化 = 紀律 + 可重複」完全對齊 ZP 零式投資的 axiom 5（「bias toward inaction」— 無邊緣不出手）；KAMA 的 regime adaptive 邏輯可直接搬入 `ZP/quant/signals/` 作為 baseline。
- **與海龜交易法則 (Round 1) 互補**：Faith 給心理學，Kaufman 給數學；兩者合起來是完整的「systematic trader 教材」。海龜的 2N 止損是 Kaufman 第 16 章「fixed fractional」的特例。
- **對齊 DNA §7 決策分工**：KAMA 的 ER 參數 = 「讓數據決定 regime，而非主觀 override」，符合 Edward 的 substance-lead 原則；在人際決策模型上也有對稱意義。
- **可挖金礦**：第 18 章的滑點/延遲框架可直接用於 B2 自營交易系統的 pre-trade cost model，計算「訊號最小可交易邊緣」；若邊緣 < 2× spread，策略自動降級為 paper trade。
- **衝突點**：Kaufman 對 options 與 crypto 著墨極少（書成於 2012），Round 2+ 需補足 Euan Sinclair、Natenberg、Antonopoulos 等延伸。
