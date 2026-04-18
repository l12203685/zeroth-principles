## Investment Banking: Valuation, Leveraged Buyouts, and Mergers & Acquisitions — Joshua Rosenbaum & Joshua Pearl (Wiley Finance)
**來源**: E:/書籍/Investment Banking - Valuation, Leveraged Buyouts, and Mergers and Acquisitions (Wiley Finance) - 1 ed - 2009.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Introduction
- Part I Valuation（Comparable Companies Analysis, Precedent Transactions, DCF, Sum-of-the-Parts）
- Part II Leveraged Buyouts（LBO mechanics, financing structure, modeling, exit strategies）
- Part III Mergers & Acquisitions（Buy-Side, Sell-Side, process mapping, synergy analysis, accretion/dilution）
- Bibliography and Recommended Reading

### TL;DR (≤120字)
華爾街投行 analyst 入職必讀——Rosenbaum-Pearl 把 banker 最核心的三項技能（valuation、LBO、M&A）標準化成 step-by-step 操作手冊。每章都是「做 deal 流程 + 範例 Excel model」，非學術而是 practitioner 視角。此書基本上定義了 MBB/IBD analyst 第一年的知識體系。

### 核心本質 (3-5 條)
1. **Valuation 四大 technique 的互補**（本質，Part I） — Comparable Companies（相對估值、市場 sentiment）、Precedent Transactions（含 control premium、M&A reference）、DCF（內在價值、management assumption driven）、LBO（financial sponsor 的最大出價）。四種方法的結果構成 "football field chart"，重疊區間是 reasonable value range。
2. **LBO = 槓桿 + 營運改善 + 倍數擴張**（本質，Part II） — LBO 的 IRR 拆解：(a) EBITDA growth（營運改善 10-20%）；(b) debt paydown（負債下降 30-50% 股權比例提升）；(c) multiple expansion（進場 7x、退場 10x 的 exit 乘數變化）。成功 deal 三者皆正，平庸 deal 只靠一項。
3. **Accretion / Dilution 分析是 M&A deal structure 關鍵**（本質，Part III） — 收購方 EPS = (pro-forma net income) / (pro-forma shares)；若 EPS 上升 = accretive、下降 = dilutive。此分析決定 stock vs cash deal、collar、earnouts 的設計；違反 EPS accretion 的 deal 難說服 board 同意。
4. **Synergy 是 M&A pitch 的核心但最常高估**（本質，Part III） — Cost synergy（合併後裁員、供應鏈）通常 realize，Revenue synergy（cross-sell、geographic expansion）通常不 realize。McKinsey 統計 M&A 70%+ 失敗；Rosenbaum-Pearl 書中例子的 synergy 假設都偏樂觀，讀者需謹慎。
5. **DCF 的 terminal value 貢獻常 > 75%**（本質，Part I） — 10-year DCF 中 terminal value（永續成長期後的估值）往往佔總 EV 的 75%+；這意味 valuation 高度敏感於 terminal growth rate (g) 與 WACC 假設。小小 0.5% 的改變可翻倍估值。這是 DCF 最大的潛在問題。

### 可用戰術/策略
- **Football Field Chart for Any Valuation**：畫出 comps trading range、precedent transactions range、DCF range、LBO max bid 四條區間，找重疊處作為 fair value 中位數；單一方法估值不足為憑。
- **Sensitivity Table for DCF**：二維 sensitivity table (growth rate × WACC) 顯示估值範圍；任何 valuation 報告沒 sensitivity 都不可信。
- **LBO Model Checklist**：sources & uses of funds → debt schedule → EBITDA projection → interest expense → FCF → debt paydown → exit EBITDA × exit multiple → equity value → IRR。任何一步錯誤整個 model 失敗。
- **Accretion/Dilution Quick Test**：Target P/E vs Acquirer P/E（cash deal）；若 Target P/E < Acquirer P/E 通常 accretive。Stock deal 看 exchange ratio 與 financing structure。
- **Synergy Discount Heuristic**：cost synergy 假設實現 70%，revenue synergy 假設實現 30%；兩者 timing 延後 1 年。用此保守假設跑 model。

### 盲點 / 反例 / 適用邊界
- **WACC 的主觀性** — 書中用 CAPM + capital structure weight 算 WACC；但 beta 的估計期、risk-free 的 tenor 選擇、market premium（5% 還是 7%）都是 arbitrary，同一公司不同分析師可算出 WACC 差異 200 bps。
- **缺乏 distressed valuation** — 書中假設 going-concern；對 bankruptcy / restructuring / reorganization 估值（Altman Z-score、liquidation value、asset value）涵蓋薄弱。
- **未涵蓋 tech / growth company valuation** — DCF 對 high-growth / negative-EBITDA 公司不適用；SaaS/AI 公司的 NTM revenue multiple、Rule of 40、CAC-LTV 框架是當前 standard，書中沒有。
- **2008 年出版，post-GFC regulation 未涵蓋** — Dodd-Frank、Volcker Rule、Brexit 對 M&A 流程影響巨大；European antitrust、CFIUS review 變嚴；當前 deal 需要額外法遵層級書中沒提。
- **無 private market 視角** — PE secondary、continuation fund、GP-led 等 2015 後興起的結構書中沒有；當前 PE 市場的流動性管理工具 analysis 需補充。

### 與 Edward 既有知識的連結
- **ZP 估值模組基礎**：Rosenbaum-Pearl 是 `ZP/valuation/fundamentals/` 的標準參考；Edward 做 B1 經濟自給的單股投資決策可用 football field 做 sanity check。
- **衝突 quantitative trading**：本書立場是 fundamental / relative valuation，與 Kestner、Pole 的 quantitative 立場相反；Edward 做長期 value 投資用此書，做 systematic trading 用 Kestner。
- **對應 Damodaran Valuation**：Damodaran 偏 academic 深入，Rosenbaum-Pearl 偏 practitioner 快速；兩本互補。
- **可挖金礦**：書中 LBO / DCF / Comps Excel template 可 port 為 Python pandas / xlwings 模組，做半自動化 valuation；輸入公司 ticker → 自動抓 financials → 產出 football field。
- **延伸應用**：Edward 若將來做 family office 或天使投資，valuation 技能是評估 deal 的核心；此書 Part III M&A 流程可用於評估創業公司的 exit scenario。
- **Poker 類比**：LBO 的「槓桿 + 改善 + 倍數擴張」三源 alpha 類似 poker 的「牌力 + 位置 + 執行」——單一 source 不穩，三者齊備才有 consistent edge。
