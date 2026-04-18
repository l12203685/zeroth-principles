## Algorithmic Trading and DMA: An Introduction to Direct Access Trading Strategies — Barry Johnson

**來源**: E:/書籍/Algorithmic Trading and DMA, Barry Johnson.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 引論（直接市場存取 DMA 的源起、演進、參與者）
- 第 2 章 市場結構（order-driven vs quote-driven、continuous vs call auction）
- 第 3 章 訂單類型（market、limit、stop、iceberg、peg、hidden）
- 第 4 章 交易成本（impact、spread、delay、opportunity cost、revenue leakage）
- 第 5 章 執行演算法基礎（VWAP、TWAP、POV、Implementation Shortfall、IS 變體）
- 第 6 章 VWAP 演算法深入（歷史曲線擬合、動態調整、反操縱設計）
- 第 7 章 Implementation Shortfall 與其變形（Almgren-Chriss、adaptive、arrival price）
- 第 8 章 流動性獲取演算法（sniffer、stealth、liquidity-seeking）
- 第 9 章 Smart Order Routing (SOR)（跨市場價格搜尋、dark pool 選路）
- 第 10 章 演算法交易的策略互動（signaling、反偵測、adversarial trading）
- 第 11 章 transaction cost analysis (TCA)（pre-trade、in-flight、post-trade）
- 第 12 章 演算法交易的未來（ML 執行、crypto microstructure、監理挑戰）

### TL;DR (≤120字)
Johnson（前 HSBC algo trading 主管）的書是 **buy-side 執行演算法的權威教材**，把 VWAP/TWAP/IS 等每個 algo 拆到可實作細節：歷史波動率曲線、slippage control、反 gaming 設計。不涉及 alpha 產生，純粹「如何把 100M 訂單送進市場不被吃掉」。是機構 trader 與 algo 供應商的必讀。

### 核心本質 (3-5 條)
1. **執行是獨立於 alpha 的第二場戰鬥**（本質） — Johnson 貫穿全書的論點：即使有完美 alpha，若執行不當（滑點 > 預期 alpha），策略仍為負報酬。執行 = 在「速度、價格、訊號隱藏」三者間求 trade-off 的動態優化問題，不是「盡快買完」就行。
2. **VWAP 的本質是「成為平均數而非驚奇」**（本質） — 第 6 章：VWAP 演算法的真正目的不是最低價，而是**貼近當日成交量加權平均價**（通常衡量執行品質的 benchmark）。過度追求低價會暴露交易意圖；完美 VWAP 執行 = 執行後看起來像市場自然流量的一部分，留下零足跡。
3. **Implementation Shortfall (IS) = 機會成本 + 衝擊成本的最優平衡**（本質） — 第 7 章 Almgren-Chriss 框架：執行越快 → 市場衝擊越大；執行越慢 → 機會成本（價格移動）越大。最優解在 IS' = 0，形如「前半高速、後半低速」或反之，視波動率與緊迫度而定。
4. **SOR 不是選最好的市場，而是 aggregating fragmented liquidity**（本質） — 第 9 章：現代美國 equity 有 13 個主要交易所 + 數十個 dark pools。SOR 演算法的價值在於併發掃描所有場所、按流動性與價格加權下單。單一市場下單丟失 30-50% 潛在流動性，重創執行品質。
5. **演算法的對抗設計決定長期有效性**（本質） — 第 10 章：市場中其他演算法可偵測 VWAP pattern 並搶先（front-run），設計者必須加入隨機性（sub-order size 與 timing 的隨機化）與反偵測（偶爾反向小單作為誘餌）。Algo 若暴露可預測 pattern，阿爾法被 HFT 吃光是時間問題。

### 可用戰術/策略
- **VWAP 實作要點**：以歷史 20-60 日的分鐘成交量曲線建立基準、當日按比例切單、每 5-10 分鐘根據實際進度動態調整；目標是執行結束時的 executed volume 分佈貼近 market volume 分佈。
- **POV (Percentage of Volume) 規則**：設定為市場當日 ADV 的 5-20%（retail 建議 5%），當市場成交量上升時自動加速、下降時減速；避免成為 ADV 100% 來源的唯一做市者。
- **Almgren-Chriss 最優執行**：對波動率 σ、日均量 V、緊迫度 λ、訂單量 Q，最優執行路徑 `v(t) = Q × sinh(κ(T−t))/sinh(κT)`，κ 由 σ、V、λ 決定；給定公式可直接代入算最優分切。
- **dark pool 排序**：按「歷史 fill ratio × 價差改善 × anti-gaming 評分」排序，IEX/UBS MTF/Liquidnet 通常優於 Barclays LX/Citi Match（後者的 information leakage 問題曾被 SEC 罰款）。
- **TCA 三階段**：pre-trade 估計預期成本、in-flight 即時調整（若當前執行偏離模型 > 20 bps 則換 algo）、post-trade 比較實際 vs 預期並回饋 TCA database 用於模型校正。

### 盲點 / 反例 / 適用邊界
- **retail 幾乎不適用** — 所有演算法的價值在於 6 位數以上 USD 單筆訂單；retail 10k USD 訂單用 market order 即可，不需要 algo。本書對 Edward 個人交易的直接價值有限，但對「理解對手方」有意義。
- **未涵蓋 crypto execution** — crypto 的 maker/taker rebate 結構、MEV、limit order book 深度等需他處補充。
- **成書於 2010，部分 dark pool 資料過時** — Barclays LX、UBS ATS 等的 fee/fill 結構經歷 SEC 2014-2016 監管後變化大。
- **ML 執行 algo 僅展望未提供細節** — 2020+ 的 RL-based execution (如 DeepSor、Lopez de Prado 的 meta-labeling) 未覆蓋。
- **回避 HFT 爭議** — Johnson 對 HFT 的正面影響持溫和立場，但 Michael Lewis《Flash Boys》的 IEX 對立觀點缺席，讀者需補充對立視角。

### 與 Edward 既有知識的連結
- **補強 Round 1 HFT Aldridge**：Aldridge 教你做 HFT alpha，Johnson 教你的 agent 怎麼送單；兩本組合看懂完整 HFT 生態。
- **對 B1 retail 的價值：理解對手**：Edward 的市價單會被 Johnson 教出來的 algo 接單；理解 algo 的 behavior 能避免在 VWAP 完成點（通常 15:45-16:00）下大單被吃。
- **適用於未來 B3 規模擴張**：若未來 Edward 規模 > 1M，VWAP/POV 將成必備工具；現在先建立概念框架。
- **可挖金礦**：第 11 章 TCA 三階段可內化為 `ZP/quant/execution/tca.py`，對所有實盤訂單計算預期 vs 實際 slippage。
- **衝突點**：Johnson 代表機構 buy-side 視角，與散戶「用 IB/TDAmeritrade retail broker」的技術限制不匹配；Edward 應採用概念框架但不照搬實作細節。
