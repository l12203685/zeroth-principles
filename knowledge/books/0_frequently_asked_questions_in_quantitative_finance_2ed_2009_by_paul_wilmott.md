## Frequently Asked Questions In Quantitative Finance (2nd Ed) — Paul Wilmott
**來源**: E:/書籍/0. Frequently Asked Questions in Quantitative Finance, 2ed, 2009, by Paul Wilmott.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **1 The Quantitative Finance Timeline**
- **2 FAQs** (61 題,從 arbitrage、put-call parity、VaR、Extreme Value、CAPM、Kelly、Black-Scholes、Greeks、volatility smile、GARCH、Dynamic Hedging、Copulas、Low-Discrepancy、Bastard Greeks 直到 "Best-Kept Secret")
- **3 The Financial Modellers' Manifesto** (2009, Derman/Wilmott)
- **4 Essays**
- **5 The Commonest Mistakes in Quantitative Finance: A Dozen Basic Lessons in Commonsense**
- **6 The Most Popular Probability Distributions and Their Uses in Finance**
- **7 Twelve Different Ways to Derive Black-Scholes**
- **8 Models and Equations**
- **9 The Black-Scholes Formulæ and the Greeks**
- **10 Common Contracts**
- **11 Popular Quant Books**
- **12 The Most Popular Search Words and Phrases on Wilmott.com**
- **13 Brainteasers**
- **14 Paul & Dominic's Guide to Getting a Quant Job**

### TL;DR (≤120字)
量化金融百科全書 + 防呆手冊:61 個核心問答 + 12 種 Black-Scholes 推導 + 12 堂常識性錯誤課。核心訊息:數學是簡單的部分,「模型會在哪裡崩潰」才是真正的戰場;2008 崩盤證明 Nobel 級學者也會信錯假設。

### 核心本質 (3-5 條, 每條 50-120字)
1. **模型是地圖不是地盤 (Model ≠ Reality)** — Derman/Wilmott Manifesto 的底線:模型是 "metaphor" 不是物理定律。實務上模型失效來自使用者把假設當真。Black-Scholes 的 "12 種推導" 正是要你理解它的假設結構 (正態、連續、無摩擦、波動率固定) 在現實中條條被違反。
2. **動態避險 ≠ 風險歸零,只是風險轉移** — 書中反覆強調 delta hedging 在跳躍/間斷/崩盤下失效;市場崩盤時相關性→1,所有「分散化」同時失靈。Margin hedging 和 CrashMetrics 才是尾部風險的真正工具,而非 Greeks。
3. **common sense > math sophistication** — Ch. 5 的 "12 堂常識課" 明確:過擬合、信 VaR 之類模型指標、把歷史波動率當未來、把正態當真、忽略 counterparty risk,都是「聰明人犯的笨錯」。LTCM 和 2008 都是數學勝出但常識缺席的結果。
4. **不完整市場(Incomplete Market)是常態不是例外** — Ch. 2 Q36 明確:跳躍、隨機波動率、交易成本、離散時間都讓市場不完整,意味無法用動態 delta 完美複製選擇權。務實路徑是 superhedging 和保守定價,而非假裝完整後再用 BS。
5. **Kelly criterion = 長期資本增長最優,但需接受高波動性** — Ch. 2 Q15 把 Kelly 放在和 EMH 同級核心地位:最大化 E[log(wealth)] 是數學上唯一保證不破產且長期最優的加碼法則,但半 Kelly / 四分之一 Kelly 是實務標配。

### 可用戰術/策略
- **把「12 堂常識課」做成自營交易系統預發行檢查表** — 模型上線前強制對照:是否假設正態?是否忽略 jump?是否信任歷史 vol?是否考慮 counterparty?未通過 = 阻塞上線。
- **Dispersion trading (Q43) 作為統計套利候選** — 賣出指數隱含波動率、買入成份股隱含波動率,押注「指數 vol 高估 vs 個股 vol 低估」— 可納入 B1 交易系統的非相關 alpha pool。
- **Brainteasers 作為面試 / 自檢練習** — Ch. 13 的機率題與定價謎題是識別「你以為懂但其實沒懂」的快速篩,特別是條件機率、martingale 性質、風險中性轉換。
- **CrashMetrics 為 tail risk 保險策略** — 當傳統 delta 在崩盤失效時,以 "最壞情況最小化" 優化的固定避險部位(不調整 vol 參數)作為 fat-tail 對沖,配合 margin hedging 管現金流。

### 盲點 / 反例 / 適用邊界
- **2009 版未涵蓋加密、永續合約、DeFi AMM、高頻做市** — 書中定價框架基於中央清算/雙邊 OTC/連續交易假設,直接套用到 Uniswap v3 集中流動性或 Binance perp funding 會失真。
- **偏理論與 sell-side 視角** — 對 buy-side 回測、factor investing、機器學習策略著墨少。若主要目標是「自營交易系統訊號」,需以 Aronson、López de Prado、Marcos 補足。
- **布朗運動 / Itô 框架在分數布朗運動/多分形市場下失準** — Wilmott 本人承認但書中處理不深;符合 Cont 2001 的 stylized facts 警告。

### 與 Edward 既有知識的連結
- 強化零式第 3 條 `meta_strategy_over_strategy`:Modellers' Manifesto 和 "12 堂常識課" 本質是 meta-strategy:先管理「我對模型的信任」,再管理市場。
- 對應 `risk_control_four_layers`:L2 (停損) ≈ margin hedge;L3 (尾部保險) ≈ CrashMetrics;L4 (流動性準備) ≈ 避免 Metallgesellschaft/LTCM 式擠兌。
- 連結 B1 自營交易系統:Q31 (哪個數值方法何時用)、Q32 (MC)、Q33 (FD) 是回測引擎選型的直接指引;Kelly 準則落在 `bias_toward_inaction` 的資金曲線管理。
- 衝突於 `derivative_over_level` 的快取直覺:BS 假設下一階 Greek 即足夠,但 Ch. 8 與 bastard greeks (Q59) 顯示二階/高階(vomma, charm)在真實市況才是風險主因。
