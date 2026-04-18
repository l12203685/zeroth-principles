## Financial Risk Manager Handbook (4ed) — Philippe Jorion

**來源**: E:/書籍/[@License] Financial Risk Manager Handbook, 4ed, 2007, by Philppe Jorion [#FRM].pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 I 部分 Quantitative Foundations (機率統計、Monte Carlo、計量經濟)
- 第 II 部分 Financial Markets and Products (bond、equity、derivatives、commodity、FX)
- 第 III 部分 Financial Instruments (forward/future、option、swap 定價與 greeks)
- 第 IV 部分 Market Risk Management
  - Ch VaR 方法（historical、parametric、MC）
  - Ch Stress testing 與情境分析
  - Ch fixed income VaR、equity VaR、option VaR
- 第 V 部分 Credit Risk Management
  - Ch credit exposure、expected/unexpected loss
  - Ch credit VaR、CreditMetrics、KMV 模型
  - Ch counterparty risk、CVA、DVA
- 第 VI 部分 Operational & Integrated Risk
  - Ch operational risk measurement (LDA, scenario)
  - Ch enterprise risk management、risk aggregation
- 第 VII 部分 Regulation and Compliance (Basel II/III、SOX、SEC、CFTC)
- 第 VIII 部分 Investment Management & Hedge Funds Risk

### TL;DR (≤120字)
Jorion 是 UC Irvine 教授 + FRM 考試設計者，本書是 GARP 官方 FRM Level I/II 教材主要參考。**定位是「風險管理整全知識樹」**，從數理基礎到 Basel 法規一網打盡。與其說是讀物，不如說是 reference manual——用於 on-demand lookup 而非線性通讀。對 Edward 而言是風險管理的工具百科。

### 核心本質 (3-5 條)
1. **VaR 不是風險的度量，而是「特定機率下的最大損失」**（本質） — 第 IV 部分的核心警訊：VaR (1-day, 99%) = X 意思是 **99% 的日子損失不超過 X**，沒說剩下 1% 有多糟。金融危機幾乎都發生在 1% tail，所以 VaR 在其最需要時最無用。正確做法是 VaR + ES (Expected Shortfall) 雙指標，ES 揭示 tail 平均損失。
2. **Basel III 的真實影響是資本成本而非風險**（本質） — 第 VII 部分：Basel III 要求 tier 1 capital ratio 10.5%+、liquidity coverage ratio 100%+；這使銀行的無風險策略（market making）從 ROE 15%+ 降至 5-8%。結果是機構撤離某些業務，為 retail + HF 留下空間（如 US Treasury spread 交易）。
3. **credit risk 的三元結構**（本質） — 第 V 部分：Expected Loss (EL) = PD × LGD × EAD；PD = probability of default、LGD = loss given default、EAD = exposure at default。三者獨立估計，錯估任一都會系統性偏差。多數 retail 投資者只關注 PD（信用評級），忽略 LGD（違約時收回率）與 EAD（當時曝險），低估實際損失。
4. **Stress testing 必須超越歷史極值**（本質） — 第 IV 部分：2008 之前的 stress test 大多用 1987/1997/2001 歷史最壞案例，結果 2008 損失遠超所有 stress scenario。Jorion 警告：stress test 需加入 hypothetical scenarios（例如「美元崩跌 20%+ 油價漲 50%+ 信用利差擴張 500 bps」），即使從未發生過。
5. **Operational risk 常被低估但可能致命**（本質） — 第 VI 部分：LTCM (1998)、Amaranth (2006)、JPM London Whale (2012)、MF Global (2011) 的真正損失來源多不是 market risk 而是 operational（集中於單一交易員、流程失效、欺詐）。operational VaR 難量化但 top 10 基金倒閉案中 7 起與 operational 相關。

### 可用戰術/策略
- **日常 VaR + ES dashboard**：對組合每日計算 historical VaR (99%, 1-day) + ES (平均 tail loss)；ES > VaR × 2 代表 tail 風險異常，需降槓桿。
- **Stress scenario 庫**：建立 10-15 個歷史 + 5 個 hypothetical 情境（如 COVID 2020、SVB 2023、LUNA 2022），每月重跑一次組合在各情境下的潛在損失。
- **Credit exposure 三元追蹤**：對每個對手方記錄 PD（評級）、LGD（歷史賠付率）、EAD（當前未結算）；任一異常（如 LGD > 60% 或 EAD 超月均 3×）觸發對手方降級。
- **Basel 資本模擬**：若未來 Edward 成立 RIA/fund，按 Basel III 計算所需資本（即使監理未要求），作為 internal floor；避免在順風時過度槓桿。
- **Operational checklist**：每季審視 (1) 單點故障人員/流程、(2) 代碼/資料備份、(3) broker API 多路備援、(4) 應急停損觸發器；任一項失效立即修復。

### 盲點 / 反例 / 適用邊界
- **2007 版本，crypto/DeFi 完全缺席** — 所有 VaR 框架針對傳統金融商品；crypto 的 24×7 交易、on-chain 風險、smart contract exploit 需獨立風險框架（2022 Terra/LUNA, FTX 皆不在 Jorion 模型涵蓋內）。
- **VaR 假設 normal distribution 問題** — parametric VaR 假設報酬常態，但 tail event 比常態分布預測頻繁 5-20 倍；需補 fat-tail distribution（t、EVT）。
- **缺乏 model risk 獨立章節** — Jorion 把 model risk 併入 operational，但 2012 JPM London Whale 等案例顯示 model risk 有獨立結構（複雜模型 + 無挑戰文化），值得獨立治理。
- **regulator-facing 偏重** — 書中大量討論 Basel/SEC/CFTC 合規要求，對 retail/獨立交易員直接應用度低；需 distill 出「個人版風險管理」。
- **過於百科式，缺實戰整合** — 各章獨立，讀者須自行組合為 end-to-end 風險流程；對比《Essentials of Risk Management》Crouhy 等整合度較高。

### 與 Edward 既有知識的連結
- **補強 Round 1 Systemic Risk Europe (SRISK)**：SRISK 是 Engle 的 tail risk 集合度指標、Jorion 是傳統 VaR 視角；兩者互補——前者看市場系統性、後者看組合獨立性。
- **VaR/ES 工具可直接搬入 B1 自營系統**：每日 VaR (99%, 1-day) + ES dashboard 是 Edward 自營資本的基本監控，可內建於 daemon 每日推送至 dashboard。
- **Stress testing 對齊零式「回本質驗證」**：壓力測試就是「這個策略在最糟 scenario 還活著嗎？」的量化版；符合 Edward 零式思維。
- **可挖金礦**：第 V 部分 credit 模型在 Edward 未來涉及 DeFi lending、crypto margin 時有用（雖然 Jorion 本身不涵蓋 crypto）；PD/LGD/EAD 概念可映射到 crypto counterparty risk。
- **衝突點**：Jorion 的 institutional + Basel 框架與 retail 的敏捷實務有張力；Edward 採納核心概念（VaR、ES、stress test）但用簡化版實作，不需完整 Basel 模擬。
