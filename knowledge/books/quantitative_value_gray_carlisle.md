## Quantitative Value — Wesley Gray, Tobias Carlisle
**來源**: E:/書籍/Quantitative Value, Gray & Carlisle, Wiley 2012.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **Part 1: The Foundation of Quantitative Value**
  - Chapter 1: The Paradox of Dumb Money
  - Chapter 2: A Blueprint to a Better Quantitative Value Strategy
- **Part 2: Margin of Safety-How to Avoid a Permanent Loss of Capital**
  - Chapter 3: Hornswoggled! Eliminating Earnings Manipulators and Outright Frauds
  - Chapter 4: Measuring the Risk of Financial Distress: How to Avoid the Sick Men of the Stock Market
- **Part 3: Quality-How to Find a Wonderful Business**
  - Chapter 5: Franchises-The Archetype of High Quality
  - Chapter 6: Financial Strength: Foundations Built on Rock
- **Part 4: The Secret to Finding Bargain Prices**
  - Chapter 7: Price Ratios: A Horse Race
  - Chapter 8: Alternative Price Measures-Normalized Earning Power and Composite Ratios
- **Part 5: Corroborative Signals**
  - Chapter 9: Blue Horseshoe Loves Anacott Steel: Follow the Signals from the Smart Money
- **Part 6: Building and Testing the Model**
  - Chapter 10: Bangladeshi Butter Production Predicts the S&P 500 Close
  - Chapter 11: Problems with the Magic Formula
  - Chapter 12: Quantitative Value Beats the Market
- **Appendix: Analysis Legend**

### TL;DR
Gray & Carlisle 把價值投資系統化的 232 頁實戰書。核心主張:人類分析師最大敵人是自己的行為偏誤,唯有機械式量化篩選能結構性消除。以 Greenblatt Magic Formula 為基礎,疊加詐欺/破產風險濾網 + Piotroski F-score 品質因子 + 多維度價格比,最終的 Quantitative Value 策略在 1964-2011 實證打敗 S&P 500。書末「人 vs 機器」直接論證機器全勝。

### 核心本質
1. **行為偏誤是價值投資最大敵人,紀律靠 algorithm 非意志** — Paradox of Dumb Money:即使擁有正確框架 (Graham/Buffett),真人操作也被 loss aversion / 錨定偏誤破壞。Greenblatt 實驗:同 Magic Formula 手動執行組大輸自動組 4-8%/年。紀律是結構而非道德。
2. **價值 edge 來自「買便宜 × 避開垃圾」** — 單看 P/E 的便宜股常是 value trap。真 edge 是 filter chain:剔除會計詐欺 → 剔除破產風險 → 剔除低品質 → 再挑最便宜。順序與深度決定 edge 強度。
3. **Franchise quality = 護城河量化代理** — Ch.5 把 Buffett 的 franchise 量化:高 ROIC 持續性 + 低資本需求 + 穩定毛利率。把軟性「品質」變硬性指標,是定性直覺翻譯為可驗證規則。
4. **多因子組合 edge > 單因子,但必須正交** — Ch.11 指出若所有因子都是 P/X 變體就等於沒分散。真正的多因子要跨不同訊息源 (價格、品質、動量、內部人交易、short interest)。
5. **回測必須抗 data snooping** — Ch.10 sustainable alpha 框架:大想法需理論支撐 → 參數穩健性 → out-of-sample → economic significance (扣成本仍正)。與 Aronson 的 Reality Check 精神一致。

### 可用戰術/策略
- **Quantitative Value Checklist**:① 盈餘操縱濾網 (accrual) ② 破產風險 (改良 Altman Z) ③ Piotroski FS_Score ≥7 ④ 高 ROIC 前 30% ⑤ EBIT/EV 便宜前 10% ⑥ 內部人淨買入加分。全通過才進場。
- **Accrual screen**:Scaled Net Operating Accruals > 0.1 = 盈餘品質差,剔除;防 Enron-style 詐欺。
- **多期 price ratio 平均**:不用單期 P/E,用 5 年平均 earning / current price (Shiller-style),平滑景氣雜訊。
- **Equal-weight > Market-cap weighting**:篩選 universe 內等權持前 20-30 檔,避免大型 value trap 拉低整體。

### 盲點 / 反例 / 適用邊界
- **Look-ahead bias 難完全消除**:F-Score 需當年財報但發布有延遲,實戰需 lag 3-6 個月;書中案例處理嚴謹度參差。
- **小型股流動性問題被忽略**:策略在微市值效果最強,但實盤 bid-ask spread + 市場衝擊吃掉理論 alpha,書中回測未充分調整。
- **適用邊界:美股等成熟市場**。台股/陸股財報可靠度較低,直接套用 Piotroski FS 會被造假污染,需本地化濾網。

### 與 Edward 既有知識的連結
- 核心呼應 **population_exploit**:「行為偏誤是 systematic 非 random」正是零式「群體 X → 逆向 +EV」的定量版;Magic Formula 有效是因大多數人不敢買又便宜又小的股票。
- 呼應 **bias_toward_inaction**:Checklist 全通過才進場,任何一項失敗否決——等同「沒 edge 不動」;結構化 inaction 是它勝人的主因。
- 強化 **meta_strategy_over_strategy**:「Man vs Machine」直接論證 meta-discipline > 個別 trade 選擇;長期 equity curve 輸給無情緒機器,對應零式第三公理。
