## Market Turmoil: Timeline of Major Events (NTHU Class Notes) — Y.W. Lin (2008)
**來源**: C:/Users/admin/staging/b2_batch_D_extracts/aee1035fa3c6cee5__market_turmoil.md  |  **消化日**: 2026-04-18  |  **模型**: claude-opus-4-7[1m] (main session)

### 目錄
- §1 2007 H2 Fed Discount Rate 調降（8/17 5.75%、9/18-20 FOMC 4.75%、12/12 TAF Term Auction Facility 啟動）
- §2 2008 H1 連續降息（1/22-24 緊急降息、3/11 Term Securities Lending Facility、3/14 Bear Stearns 緊急貸款、3/16 JPM 併購 Bear、3/18-4/30 Fed Funds 至 2.00%）
- §3 2008 H2 金融體系崩潰（7/11 IndyMac、9/7 Fannie/Freddie 進入 conservatorship、9/15 Lehman 破產、9/16 AIG 850 億救助、9/19 Money Market Fund 擔保）
- §4 Emergency Economic Stabilization Act（10/3 TARP、10/8 國際協調降息 50bp）
- §5 量化工具箱對照表（TAF、TSLF、PDCF、CPFF、MMIFF、TALF、各工具目標與觸發）

### TL;DR (≤120字)
Y.W. Lin 於 2008 年 10 月清華計財所碩士研究整理的「次貸危機 Fed 工具時序表」— 從 2007/8 第一次降息到 2008/10 TARP 通過，Fed 在 14 個月內動用 10+ 種緊急流動性工具，展示「從降息 → 擴表 → 擔保 → 立法」的完整危機響應階梯；從新興市場（亞洲）角度觀察發達市場央行如何被推到極限。

### 核心本質 (3-5 條)
1. **央行工具箱的階梯式啟動**（本質） — 2007-2008 揭示：央行不會一次性動用所有工具，而是按「價格（利率）→ 數量（LSAP 擴表）→ 擔保（deposit insurance 擴大）→ 司法（TARP 授權）」階梯式升級；當前層失效才啟動下一層。Edward 觀察 2020 COVID、2023 SVB 危機時可用此框架預測 Fed 下一步。
2. **從亞洲視角看 Fed 政策的時間差**（本質） — 作為台灣學生整理的筆記，暴露了新興市場看發達市場的資訊滯後：Fed 9/18 降息後亞股 9/19-20 才反應；資訊時差是可交易的 arbitrage，但需要極低延遲才能獲利。
3. **TAF、TSLF、PDCF 等縮寫背後是流動性類別分工**（本質） — §5 工具箱：TAF 對 depository institutions、TSLF 換 Treasuries 對 primary dealers、PDCF 直接對 dealers 的 overnight credit、CPFF 買商業票據、MMIFF 買 MMF 資產；每個工具對應不同金融層級的 funding stress，揭示央行對金融網路拓撲的精細認知。
4. **9/15 Lehman 破產是危機拐點**（本質） — §3：Lehman 未被救 vs Bear Stearns 被救的對比顯示「moral hazard policy 選擇」直接引爆後續連鎖反應；Paulson 後悔事後公開承認政治因素超過 economic rationale。對量化 risk manager：政策響應不是完全 rational optimization，黑天鵝可能來自政治博弈而非純經濟。
5. **MMF 擠兌的獨特威脅**（本質） — 9/16 Reserve Primary Fund 跌破 $1 NAV、9/19 Treasury 宣布 MMF 擔保；危機並非從投行開始而是從 shadow banking（MMF）擴散；任何看似「現金等價物」的商品在壓力測試下都可能 break the buck。

### 可用戰術/策略
- **Fed 工具箱作為危機 leading indicator**：觀察 Fed 啟動哪個工具 → 推斷問題在金融網絡哪一層；TAF 啟動 → 商業銀行流動性；TSLF → primary dealer 資金；CPFF → non-financial corp 商業票據；MMIFF → MMF 系統；TALF → ABS 市場。
- **VIX 與 Fed Response Lag 的 Pair Trade**：歷史上 VIX 首次破 40 到 Fed 首次降息的 lag 平均 3-5 天；此期間可 short gamma（賣近月 VIX 選擇權）等待政策響應後 VIX 收斂。
- **Asia-Open Arbitrage**：Fed FOMC 結論通常美東時間 14:00 發布，此時亞洲已收市；台灣/日本/韓國隔日開盤會在 overnight futures 內 price in，可交易 E-mini 與亞股 futures 的 premium/discount。
- **Moral Hazard Switch 判讀**：當 Fed/Treasury 出手救特定機構時 → 短期市場恐慌緩解；當 Fed/Treasury 允許某機構破產時（Lehman、SVB 股東全失） → 系統性風險重估，需降 position size。
- **Tool Activation Priority**：新危機發生時，猜測 Fed 會啟動哪個工具；若啟動工具不在 2008 清單內 → 代表是新型危機，historical playbook 部分失效。

### 盲點 / 反例 / 適用邊界
- **時間只到 2008 年 10 月**：筆記為 2008/10/8 整理，未涵蓋 11 月後的 QE1（2008/11/25）、2009 春 QE 擴大、2010 QE2、2012 QE3、2020 COVID 無限 QE 等後續演化；讀者需自補 2009-2024 工具。
- **純時序性描述，缺乏效果定量評估**：筆記列出 Fed 在何時做了什麼，但未評估各工具的有效性（TAF 有效、PDCF 無效等 ex-post 研究）；需補 Fed 研究報告 + Bernanke/Geithner 回憶錄。
- **未涵蓋歐洲 ECB 與日本 BOJ 同期行動**：2008 全球協調降息是 10/8，但 ECB、BOE、SNB 各自的緊急工具與 Fed 不同；全球流動性真相需要多央行視角。
- **新興市場反向資本流動描述缺失**：2008 美元融資缺口導致 EM 貨幣崩盤（巴西 real -30%、韓元 -35%），Fed 後來提供 $30bn swap line 給 4 個 EM 央行（韓、星、巴、墨）；本筆記未討論此面向。

### 與 Edward 既有知識的連結
- **對齊 ZP 核心**：央行階梯式工具箱完全對應零式投資本質 — 任何系統（經濟、AI、人生）在危機中都是階梯式響應，能階越高需要觸發條件越嚴；理解「當前在哪一階、下一階需什麼觸發」比預測具體事件更重要。
- **延伸既有 DNA**：Fed tool box 結構可類比永生樹的危機響應 — 小問題主 session 處理、中等 subagent 平行分派、大問題回核心 zero (`0`) 對齊、系統性問題暫停所有非核心任務；每級有明確觸發與工具。
- **衝突點**：文件為 10/12 頁的 class notes，信息密度不如完整教科書；建議與 Bernanke《The Courage to Act》、Sheila Bair《Bull by the Horns》搭配閱讀補充多方視角。
- **可挖金礦**：§5 的工具箱對照表可作為 Edward 未來建立「全球央行 crisis response dashboard」的 schema 基礎；當 2025+ 新危機爆發時，用此 schema 逐條 checklist 哪些工具已啟用，推估當前危機嚴重度百分比（工具 10 種全啟用 → 100%；啟用 3 種 → 30%）。
