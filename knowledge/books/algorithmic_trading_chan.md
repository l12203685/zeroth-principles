## Algorithmic Trading: Winning Strategies and Their Rationale — Ernest P. Chan (2013)

**來源**: E:/書籍/Ernest P. Chan/Algorithmic Trading Winning Strategies and Their Rationale, 2013, Ernest P. Chan.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 回測的要素（look-ahead、survivorship、data-snooping、統計顯著性）
- 第 2 章 均值回歸因子與時序（Hurst 指數、variance ratio 測試、ADF test 協整）
- 第 3 章 股票與 ETF 的均值回歸實務（pairs、triplets、index arb、crypto 前夕探討）
- 第 4 章 其他資產類別的均值回歸（貨幣、利率、商品、ETF 季節）
- 第 5 章 利差交易間的（金融期貨 spread、inter-exchange arb、跨期套利）
- 第 6 章 動量策略 (Momentum)（TS momentum、CS momentum、衰退半衰期）
- 第 7 章 因子動量與事件動量（earnings drift、FOMC drift、analyst upgrade）
- 第 8 章 風險管理與頭寸規模（CPPI、Kelly、drawdown duration）
- 第 9 章 展望（機器學習、replication、策略退化週期）

### TL;DR (≤120字)
Chan 第二本書的定位是「第一本的技術升級版」：更多統計嚴謹性 + 更多策略 case + 增加利差與跨資產。**核心貢獻是把 mean reversion / momentum 的二元分類升級為 7 種子類別**（固定時間 vs 信號觸發、單資產 vs 籃子、截面 vs 時序）。Sharpe 測量與 half-life 成為本書兩大標籤性方法論。

### 核心本質 (3-5 條)
1. **均值回歸的可交易性由 Hurst 指數決定**（本質） — 第 2 章核心：Hurst < 0.5 是 mean-reverting、= 0.5 是 random walk、> 0.5 是 trending。但實戰中更重要的是 **half-life of reversion**：hf = −log(2)/log(1−λ)，λ 為 OU 過程衰退速率。hf < 5 天的資產適合日內均值回歸，hf > 30 天則要用 swing。
2. **協整 ≠ 相關**（本質） — 第 3 章反覆強調：兩隻高度相關的股票不一定協整（短期同步但長期無錨），反之有時負相關也可協整（長期有共同驅動因子）。配對策略必須用 Johansen/ADF 測試協整，而非用相關係數挑對——這是 90% retail pairs 策略失敗的根本原因。
3. **momentum 的半衰期 = 策略的使用壽命**（本質） — 第 6 章給出經典實證：cross-sectional momentum (CS-Mom) 在 1980-2008 Sharpe ~1.2，但 2009 後降至 0.4；time-series momentum (TS-Mom) 較為穩健但也在 QE 期間失效。這指出 **momentum 不是永恆 factor，而是制度依賴 phenomenon**。
4. **data snooping bias 的量化公式**（本質） — 第 1 章引入 White's Reality Check 與 Hansen's SPA test：若從 N 個策略中選出表現最好的，其 Sharpe 需 deflate 因子 `√(2 × log(N))`。測試 100 個策略，最佳 Sharpe 3.0 實際期望約 1.2。這是打擊過度擬合的量化工具。
5. **風險管理 = 流動性 × 波動率 × 杠桿的聯合函數**（本質） — 第 8 章：CPPI (Constant Proportion Portfolio Insurance) 規則 = 目前頭寸不超過 (NAV − floor) × multiplier；當回撤接近 floor 時自動降杠桿。這比固定比例 Kelly 更能在市場 regime change 時保護資本。

### 可用戰術/策略
- **Hurst + half-life 策略選擇器**：對任一資產計算 20-252 日 Hurst 與 OU half-life；Hurst < 0.4 且 hf < 10 日 → 均值回歸 daily swing；Hurst > 0.55 → momentum weekly。第 2 章附 MATLAB 腳本。
- **三元組配對 (Triplet arbitrage)**：找三隻協整資產（例如 SPY、IVV、VOO），價差 spread = a×SPY + b×IVV − c×VOO 比單對更穩定，協整測試需 Johansen 而非 Engle-Granger。
- **Earnings drift 策略**：財報公布後 30-60 分鐘觀察價格反應，若方向一致且動量強則跟隨做 3-5 日，Sharpe 在 2010 前達 1.5，後降至 0.6（第 7 章實證）。
- **OU 過程參數估計 + z-score 進出場**：spread 擬合 dx = θ(μ−x)dt + σdW，當 z = (x−μ)/σ > 2 做空、< −2 做多，回歸至 |z| < 0.5 平倉。
- **CPPI 風險控制**：設 floor = 起始資金 × 0.8，multiplier = 3；當前曝險 = (NAV − floor) × 3，NAV 接近 floor 時自動降至 0，避免爆倉。

### 盲點 / 反例 / 適用邊界
- **樣本均集中在 2000-2012** — 大部分回測範例用 2000-2012 資料，這段時期是 mean reversion alpha 的黃金年代；2015+ 許多相同策略 Sharpe 腰斬（QE 扭曲、HFT 擠壓）。
- **交易成本估計偏樂觀** — Chan 多數策略假設 $0.01/股手續費 + 5 bps 滑點，但在 10M+ 資金或小市值股票實際成本可能 20-50 bps，吞噬 50%+ alpha。
- **對 ML 持保留態度** — 第 9 章對機器學習持懷疑（2013 年觀點），認為規則 + 經濟直覺優於黑箱模型；後續 Lopez de Prado、Dixon 等已實證 ML 在適當處理下可穩定加值。
- **不處理期權波動率微觀結構** — Chan 的策略生態幾乎不涉及 options，但 options 的 gamma/theta 結構帶來的非線性 alpha 是 retail 當前主要機會，本書完全缺席。
- **crypto 只在後記輕描** — 書成於 2013 BTC ~100 USD 時代，當時 crypto 未被正視；現今 crypto 市場的微觀結構與 2013 US equity 高度類似，給 retail 再一次 arb 窗口。

### 與 Edward 既有知識的連結
- **對齊零式第 2 軸「資訊不對稱 → 行動」**：Chan 的 Hurst + half-life 架構正是量化「這個資產我有沒有邊緣」的具體工具；可搬入 ZP 核心的 edge-detection layer。
- **補強 Round 1 的 statistical_arbitrage_pole**：Pole 的 Stat Arb 偏學術，Chan 的配對/三元組是實戰實作，兩本合讀是 pairs trading 的完整方法論。
- **與下一本 Machine Trading (Chan 2017) 連接**：本書是 rule-based 方法論，2017 版本加入 ML 與 crypto；兩本建議同時讀以看出 Chan 對 ML 態度的轉變。
- **可挖金礦**：第 2 章 Hurst + half-life 的 MATLAB 代碼可改寫為 Python 加入 `ZP/quant/signals/regime_detector.py`，作為所有策略的前置 regime classifier。
- **衝突點**：Chan 對 ML 持保留（2013），與 Round 1 Financial Machine Learning (Kelly-Xiu 2023) 觀點不同；Edward 需判斷 B2 階段是採 rule-based (Chan) 還是 ML-augmented (Kelly)，建議 rule-based 為 baseline、ML 為補強。
