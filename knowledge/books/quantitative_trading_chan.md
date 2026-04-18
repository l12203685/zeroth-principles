## Quantitative Trading: How to Build Your Own Algorithmic Trading Business — Ernest P. Chan (2008)

**來源**: E:/書籍/Ernest P. Chan/Quantitative Trading How to Build Your Own Algorithmic Trading Business, 2008, Ernest P. Chan.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 量化交易能否作為事業（獨立交易員的優劣、風險承受度、規模限制）
- 第 2 章 如何尋找策略（學術論文、部落格、模仿公募、自動化思維過濾）
- 第 3 章 回測（資料清理、survivorship bias、前視偏差、交易成本、進出場規則）
- 第 4 章 實戰建置（broker 選擇、API、回測轉實盤的陷阱、紀錄片化流程）
- 第 5 章 資金管理與風險（Kelly 準則、最大回撤、連續虧損序列、風險預算）
- 第 6 章 特殊問題（資料供應商、執行延遲、數據源同步、監控 dashboard）
- 第 7 章 量化交易的獨到見解（regime change、適應性、市場效率的時變性）
- 附錄：IB/TradeStation/MATLAB 程式碼範例、均值回歸與配對策略樣本

### TL;DR (≤120字)
Chan 的第一本書定位為「獨立交易員創業指南」：不是寫給 Two Sigma 工程師，而是給有 10 萬美元、想把業餘研究轉為全職的程式交易者。核心論點：**小資金（< 1M）的 retail quant 反而有大型機構做不到的策略空間**，但必須放棄過擬合的神話、接受 Sharpe 1.0-1.5 的現實，並建立工業化研究流程。

### 核心本質 (3-5 條)
1. **規模劣勢反轉**（本質非戰術） — Chan 在第 1 章的反直覺洞察：大型量化基金因容量限制（capacity）被迫避開 < 1M 美元流動性的策略，留下大片 retail 可獲利空間。例如小型股配對交易、微小市場的 momentum、特定 ETF 的日曆套利。這顛覆了「散戶總是被機構碾壓」的迷思，定義了 retail quant 的生存縫隙。
2. **Sharpe 1.0 是現實基準，不是失敗**（本質） — 第 5 章直言：聲稱 Sharpe > 3 的回測要麼 curve-fit、要麼忽略成本。真正經過 out-of-sample 與實盤驗證的策略通常 Sharpe 落在 1.0-1.5，對應年化 10-20% 配合 10-15% 波動。接受這個現實後，才能理性設計風險預算而不是追逐聖杯。
3. **回測 = 科學實驗而非拉曲線**（本質） — 第 3 章給出 14 項 checklist：avoidance of look-ahead bias、survivorship bias 的股票池重建、corporate action 調整（split/dividend）、bid-ask spread 精確估計。Chan 的核心觀點：**一個沒列出這 14 項問題處理方式的回測等於沒做回測**，這是量化研究的倫理底線。
4. **策略的可遷移性決定職業壽命**（本質） — 第 7 章：單一策略的 alpha 衰退期 (half-life) 通常 6-24 個月，但研究方法、資料管道、執行架構的可複用性可持續 10+ 年。個人 quant 的真正資產是 pipeline 而非當前策略。
5. **IB API + 1 台桌機 = 機構級基礎設施**（本質） — 第 4 章：2008 年之前 retail 無緣的自動化交易，現在用 Interactive Brokers TWS API + MATLAB/Python + 1 台 PC 即可搭建與 Goldman prop desk 相同的下單架構，差別只在速度與資料品質；Chan 親身示範這套搭建並給出具體代碼。

### 可用戰術/策略
- **配對交易（Pairs Trading）樣板**：選協整的兩支股票（例如 GLD/SLV），計算 spread = log(A) − β×log(B)，當 spread 超出 ±2σ 就進場反向，回歸至 0 平倉；第 7 章提供 MATLAB 原碼。
- **ETF 價差套利**：XLE 與成分股加權平均間的日內價差，正常 < 5 bps，偶爾因成分股劇烈移動超過 20 bps，此時做多 ETF 空成分股籃子或反之；要求 sub-second 執行。
- **研究-實盤轉換 checklist**（第 4 章）：1) 用相同代碼跑回測與 paper trade 至少 1 個月；2) paper trade vs 回測日報酬相關係數 > 0.9 才轉小資金實盤；3) 小資金 3 個月達到回測期望 Sharpe 的 70% 才放大。
- **Kelly 的實戰修正**：全 Kelly 的波動率使大多數人無法承受，建議用 0.25× Kelly（即 quarter-Kelly），期望成長率下降約 25% 但最大回撤減半。
- **日曆套利 VIX ETN**：VXX 對 VIX futures 的 contango/backwardation 結構性負 carry，做空 VXX 同時做多 S&P 作為 hedge，年化報酬 15-25% 但在 vol spike 時會有劇烈回撤。

### 盲點 / 反例 / 適用邊界
- **2008 年後時空變化** — 書成於 2008，當時 pairs trading、日內均值回歸策略仍有顯著 alpha；2015 後這些策略被大量 HF 做爛，Sharpe 降至 0.3-0.8，retail 難獨立獲利。Chan 本人在後續書與部落格承認這點。
- **忽略選擇權策略** — 全書聚焦股票/ETF，完全不涉及 options/vol trading，而 options 正是 retail 當前最具 alpha 密度的領域（相對於被機構壟斷的股票統計套利）。
- **資料供應商成本被低估** — Chan 推薦的 CRSP/Bloomberg 資料成本對 retail 來說仍高昂（5k-30k USD/年）；書中未充分強調這會吃掉小帳戶策略年化報酬。
- **IB API 延遲未量化** — 第 4 章簡單提到 API 延遲但未給出具體 benchmark；實戰上 IB 下單確認延遲 100-500ms，部分延遲敏感策略不可行。
- **策略容量上限未深入** — 大多數書中樣本策略在 < 1M 資金有效，但 Chan 對「當你的資金長到 10M 後該放棄哪些」缺乏具體門檻（對比 Narang 的 Inside the Black Box 有詳細容量分析）。

### 與 Edward 既有知識的連結
- **對齊 B1 經濟自給目標**：Chan 的「retail quant 生存縫隙」直接回應 Edward 的核心目標——用個人資金與工程能力建立可持續現金流；第 1 章的規模劣勢反轉是 B1 策略設計的理論基礎。
- **補強 Round 1 的 Kaufman/Faith**：Kaufman 給系統百科、Faith 給心理，Chan 給「從業餘到全職的工程化流程」。三本合讀是 B1 自營交易基礎設施的完整模板。
- **與 Narang (本輪後續) 互補**：Chan 是 bottom-up retail 視角，Narang 是 top-down 對沖基金視角；兩者對照可看出策略的 capacity 分層。
- **可挖金礦**：第 4 章的「回測-paper-實盤」三階段可直接搬入 ZP/workflow 作為新策略標準化上線流程，配合 `staging/b2_progress.jsonl` 風格的 JSONL 追蹤。
- **衝突點**：Chan 對 Kelly 的建議（quarter-Kelly）與 Vince 的 optimal-f 有張力；在 DNA 層面，可採用 Chan 的保守派作為 B1 初期預設。
