## 給工程師的第一本理財書：程式金融交易的 118 個入門關鍵技巧
**來源**: E:/書籍/給工程師的第一本理財書：程式金融交易的118個入門關鍵技巧.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Part 1 資料來源（TEJ、Yahoo Finance、期交所、證交所、FinMind）
- Part 2 Python 生態（pandas、numpy、backtrader、ta-lib、finlab）
- Part 3 策略開發（技術指標、財務因子、組合建構）
- Part 4 回測工具（backtrader、zipline、vectorbt 比較與實作）
- Part 5 機器學習應用（sklearn、隨機森林、XGBoost 股票排序）
- Part 6 可視化（matplotlib、plotly、Streamlit dashboard）
- Part 7 自動化（排程、通知、LINE Notify、Discord webhook）
- Part 8 部署（雲端主機、Docker、GitHub Actions、資安）

### TL;DR (≤120字)
針對軟體工程師從零入門程式交易而寫，特色是把金融知識翻譯成工程師熟悉的抽象（DataFrame = table、策略 = function、回測 = unit test、實盤 = CI/CD）。不追求 alpha 創新，追求「用工程力讓理財自動化」。最大價值是介紹台灣在地工具鏈（FinMind、finlab、XQ API）。

### 核心本質 (3-5 條)
1. **交易系統是 CRUD + 事件迴圈**（本質，Part 1-3） — 工程師只需把交易看成「讀資料 → 計算訊號 → 下單 → 記錄」四步 CRUD + 事件迴圈，即可快速上手。無需先懂金融理論。此抽象降低跨域門檻。
2. **DataFrame 是金融資料的通用語言**（本質，Part 2） — pandas MultiIndex (symbol, date) 可表達絕大多數金融資料；學好 pandas resample / rolling / groupby 就能實作 90% 技術指標與因子。作者把這套寫成「10 個 pandas 必學函式」。
3. **回測 = 單元測試**（本質，Part 4） — backtrader/vectorbt 本質上是 event-driven 測試框架；策略是被測函數，歷史資料是測試 fixture，績效指標是 assert。工程師可套用 TDD 工作流：先寫 expected Sharpe，再實作策略。
4. **機器學習在個人理財的正確角色是「排序」而非「預測」**（本質，Part 5） — 絕對回報預測幾乎不可能（SNR 太低），但「哪些股票比其他股票強」的相對排序可達 55-60% 準確；作者建議工程師直接做 ranking problem，而非 regression。
5. **自動化的終點是「被動通知」而非「主動操作」**（本質，Part 7） — 作者強調：程式交易的極致不是 100% 無人參與，而是「系統自己跑、出問題自動 alert、重大決策人類審核」。LINE Notify + Discord webhook 比全自動下單 ROI 更高。

### 可用戰術/策略
- **FinMind / finlab API 一鍵抓台股資料**：台灣在地替代 Yahoo Finance 的封裝，免費涵蓋股票/期貨/財報，作者給出可直接跑的 minimum working example。
- **vectorbt 向量化回測**：相比 backtrader 慢但易讀，vectorbt 可在 1 分鐘內跑 10 萬次參數掃描，適合過擬合診斷。
- **XGBoost 台股 monthly ranking**：用 ROE、M12-1 動能、P/B、ILLIQ 四因子訓練 XGBoost ranker；每月買前 10 檔賣後 10 檔，作者實測 2015-2022 年化 18%。
- **LINE Notify 事件通知**：策略觸發訊號、停損觸發、回撤突破閾值 → LINE 推播，不影響主業工作節奏。
- **Docker + GitHub Actions 自動化部署**：每日收盤後 CI 自動重訓 + 重算 signal + 推播結果，工程師零維運成本。

### 盲點 / 反例 / 適用邊界
- **金融深度有限**：作者自承是「工程師寫給工程師」，對衍生品、固定收益、選擇權 Greeks、無套利原理等缺席；要深化需補 Natenberg/Hull。
- **策略樣本偏個股選股**：對期貨/外匯/加密幣/選擇權的涵蓋薄弱；作者的「排序 ML」方法對連續商品無效。
- **法規/稅務/合規簡略**：台灣程式交易稅制（證交稅、期交稅、境外所得）未深入，實盤前需自行補足。
- **資金量假設散戶（<1000 萬）**：書中策略未考慮 capacity 問題（大資金進場即改變價格），作者的 ranking strategy 在 > 5000 萬部位會自打自臉。
- **ML 章節偏入門**：第 5 部止於 XGBoost，未涵蓋 deep learning/Transformer 應用；對進階讀者需補 Lopez de Prado。

### 與 Edward 既有知識的連結
- **對齊 ZP 經濟自給**：作者「系統自動化、重大決策人審核」的哲學可直接搬入 ZP 自營系統——主 session 做策略研究、subagent 做每日執行、Discord/LINE 通知 Edward 重大事件。
- **延伸既有 DNA**：§11 Queue 模型——作者的 Docker + GitHub Actions 自動化對應 Edward 的「排程任務自動跑 + 異常才通知」哲學。
- **衝突點**：作者 ML 觀點偏樂觀（XGBoost 年化 18%），Lopez de Prado 警告多數此類 backtest 是 overfitting；Edward 應先對作者數字做 OOS 驗證。
- **可挖金礦**：Part 7 LINE Notify + Part 8 Docker 部署可直接整合入 Edward Dashboard 架構，補齊當前缺乏的「異常通知」鏈路。
- **對接 (繁中) Python 期貨 121 技巧**：兩本同一本土技術棧，可組合——本書教 infrastructure 與個股選股，Python 期貨 121 教 期貨日內策略。
