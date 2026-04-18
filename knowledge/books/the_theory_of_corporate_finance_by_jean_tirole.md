## The Theory of Corporate Finance — Jean Tirole
**來源**: E:/書籍/The Theory of Corporate Finance by Jean Tirole.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Part 1 An Economic Overview of Corporate Institutions**
  - Ch 1 Corporate Governance
  - Ch 2 Corporate Financing: Stylized Facts
- **Part 2 Corporate Financing and Agency Costs**
  - Ch 3 Outside Financing Capacity
  - Ch 4 Determinants of Borrowing Capacity
  - Ch 5 Liquidity, Risk Management, Free Cash Flow & Long-Term Finance
  - Ch 6 Corporate Financing under Asymmetric Information
  - Topic 7 Product Markets and Earnings Manipulation
- **Part 3 Exit and Voice: Passive and Active Monitoring**
  - Ch 8 Investors of Passage: Entry, Exit, Speculation
  - Ch 9 Lending Relationships and Investor Activism
- **Part 4 Security Design: Control Right View**
  - Ch 10 Control Rights and Corporate Governance
  - Ch 11 Takeovers
- **Part 5 Security Design: Demand Side View**
  - Ch 12 Consumer Liquidity Demand
- **Part 6 Macroeconomic Implications & Political Economy**
  - Ch 13 Credit Rationing and Economic Activity
  - Ch 14 Mergers and Acquisitions (equilibrium asset values)
  - Ch 15 Aggregate Liquidity Shortages and Liquidity Asset Pricing
  - Topic Institution/Public Policy/Political Economy of Finance
- **Part 7 Answers to Exercises & Review Problems**

### TL;DR (≤120字)
諾貝爾經濟學獎得主 Tirole 寫的現代公司金融 "聖經":以 agency theory + information asymmetry + incomplete contracts 為三支柱,嚴謹建模 governance、financing、takeover、liquidity、M&A。與 Brealey-Myers 實務書不同,此書是學術研究級 reference — 適合金融學 PhD、policy maker、深度投資者。

### 核心本質 (3-5 條, 每條 50-120字)
1. **Corporate governance 核心 = "managers vs shareholders" 的 agency problem** — Ch1 明確:manager (agent) 資訊多於 owners (principal),必有 moral hazard。所有公司金融制度(股權設計、董事會、DPS、股票選擇權補償)都是對這個 agency gap 的修補嘗試。理解這點 = 理解公司行為。
2. **Financing choice 不是「最便宜的資本」,是「最少 agency cost 的資本」** — Ch3-6:Modigliani-Miller 說 capital structure 無關緊要是錯的;實務上 debt 有 tax shield + 紀律效應,equity 有彈性但容易被管理層濫用。最優結構平衡 agency cost 各來源。
3. **Information asymmetry 驅動 security design** — Ch10-11:公司 issue 何種證券(普通股、優先股、可轉債、dual-class)本質是「在不同知情程度下給投資人什麼 control right」。Control right 配對 cash flow right 的程度決定公司治理品質。
4. **Liquidity 不是 "有錢在手",是 "有能力應對未來狀態"** — Ch5, Ch15 重新定義:公司 liquidity = 未來高機會時能獲得資金的期望能力,而非靜態 cash pool。這改變了 risk management 的目標 — 不是最小化波動,而是保住 "option to invest when opportunity comes"。
5. **Takeover (Ch11) = corporate governance 的最後手段** — 若內部 governance 失效,market for corporate control (敵意併購) 是 shareholders 的最後武器。但 takeover 有 "free rider" 與 "overpayment" 問題,實務上遠非完美紀律工具;poison pills 等反併購機制削弱此效應。

### 可用戰術/策略
- **Agency cost lens 分析個股** — 買股票前問:(a) 管理層持股多少?(insider holding ≥ 5% 是 alignment 訊號);(b) 董事會獨立性?(c) compensation 與長期績效掛鉤?(d) 大股東 monitoring 強度?這些是比單純 P/E、EPS 更深的質地指標。
- **Identify takeover targets** — Ch11 的 overpayment 與 managerial entrenchment 特徵:管理層持股低 + 大量閒置 free cash flow + 被低估 + 無 poison pill = 潛在 takeover 目標。可作為 event-driven strategy 的 screening criteria。
- **Convertible bonds pricing lens** — Ch10 的 control rights view:CB 是 "debt + equity option",對 信息不對稱情境(startup / distressed) 特別有價值。B1 策略若觀察 CB,需把 option value 拆為 delta (equity) + convexity (debt + conversion) 兩部分。
- **Liquidity management policy for trading operations** — Ch5 的「應對未來狀態的 liquidity」提示 B1 自營交易帳戶應保留 reserve (經測試可吸收 3σ drawdown) 而非全部動用;reserve = option to scale up when sharp opportunity appears。
- **Event study: M&A announcement abnormal returns** — Ch14 提供理論預測:bidder (收購方) 平均 abnormal return ≈ 0 或 -2%,target 顯著正 20-30%。可作為自家 event-driven strategy 的統計 benchmark。

### 盲點 / 反例 / 適用邊界
- **數學複雜,需 game theory + information economics 基礎** — Tirole 本身是 industrial organization 大師,模型硬核;沒有研究所程度的 microeconomics 讀起來吃力。實務 trader 用其 intuition 即可,不需逐步推導每個 mechanism design 模型。
- **理論導向,實務建議有限** — 書中目的是「解釋為什麼公司這樣」,非「告訴你如何估值」。Damodaran《Investment Valuation》、Koller《Valuation》才是實務 valuation manual。
- **2006 年版,缺 2010 後 fintech、direct listing、SPAC、加密上市等新結構討論** — 需補近年 working papers。
- **以 developed market + public company 為主** — emerging market、private equity、VC 的特殊 agency 問題(minority protection、exit constraints)涵蓋有限。

### 與 Edward 既有知識的連結
- 對應零式第 2 條 `information_asymmetry_action`:Tirole 全書的三大支柱(agency, info asymmetry, incomplete contract)都是「資訊不對稱 → 制度設計」的正面推理;應用到投資判斷就是「評估 management quality」這個 soft factor 的理論依據。
- 銜接 `meta_strategy_over_strategy`:Tirole 的 governance analysis 是「策略之上的制度 meta-layer」;選股時看的不只 EPS,而是「這家公司制度能不能長期 scale」。
- 對 B1 自營交易系統的貢獻:若加入 equity selection 策略,governance-quality factor (基於 Ch1-9 的判斷) 可作為 additional filter,過濾掉 agency-problem 嚴重的公司。
- 對 B7 ZP 寫作貢獻:可寫「從 Tirole 看散戶投資盲點」— 大多數散戶只看價格/基本面,忽略 governance 因子,這是結構性 alpha gap。
