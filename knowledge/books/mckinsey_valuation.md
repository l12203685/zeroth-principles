## Valuation: Measuring and Managing the Value of Companies, 5th Ed — McKinsey (Tim Koller, Marc Goedhart, David Wessels)
**來源**: E:/書籍/McKinsey_Valuation_Measuring and Managing the Value of Companies_5th Ed.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Part One: Foundations of Value（core principles, value creation, value drivers）
- Part Two: Core Valuation Techniques（DCF, economic profit, enterprise DCF, APV, WACC）
- Part Three: Intrinsic Value and the Stock Market（markets, investors, market value vs intrinsic value）
- Part Four: Managing for Value（performance measurement, target setting, management compensation）
- Part Five: Advanced Valuation Issues（multibusiness companies, intangibles, emerging markets, cyclical companies）
- Part Six: Special Situations（high-growth, financial institutions, cross-border, distressed debt）
- Appendices（Economic profit formula, WACC derivation, levering equations, P/E leverage）

### TL;DR (≤120字)
McKinsey valuation 是企業估值的 bible——800+ 頁，從 "value 創造本源" 到 DCF 機械化流程到財務機構 / 跨國 / 新興市場特殊情境的完整指南。核心論斷：value is created by ROIC > WACC + growth；管理層的任務是最大化「經濟利潤」而不是 EPS / revenue 等會計指標。

### 核心本質 (3-5 條)
1. **Value = ROIC, Growth, WACC 三參數函數**（本質，Part One） — 企業 value = Invested Capital × (ROIC - g) / (WACC - g)；只有 ROIC > WACC 時 growth 才創造價值，否則 growth destroys value。這個公式是 McKinsey 全書的邏輯支柱；所有策略決策都要回到這三個 driver。
2. **Economic Profit > Accounting Earnings**（本質，Part Two） — Economic Profit = Invested Capital × (ROIC - WACC)；measure 企業是否「賺超過 capital cost」。公司可能 GAAP 獲利但 economic loss（ROIC < WACC），這解釋了為何股價與 EPS 脫鉤的現象。
3. **Market Value ≠ Intrinsic Value 但收斂**（本質，Part Three） — 短期市場受情緒、 noise trader、liquidity 影響；長期（5-10 年）market value 與 intrinsic value 收斂於 +/- 20%。McKinsey 的視角：不要試圖 time market，而是 build intrinsic value，市場終會認可。
4. **Managing for Value 的 Compensation 設計**（本質，Part Four） — 高管薪酬應與 long-term EP 連結，不是 EPS 或股價。書中批評 EPS-linked bonus 導致短期行為（買庫藏股、砍 R&D、延遲 capex）；理想是 5+ year TSR（total shareholder return）+ rolling vesting。
5. **Emerging Market 估值的多重調整**（本質，Part Five） — 新興市場 DCF 需加：country risk premium（3-5%）、sovereign rating spread、inflation 調整、currency forward assumption。McKinsey 反對單一「加 risk premium」的粗暴方法，主張 scenario-based valuation + 分開 model operational risk vs macro risk。

### 可用戰術/策略
- **Value Driver Tree**：從 EPS / Revenue 逐層拆解到 operational drivers（price, volume, cost, invested capital）；每個 driver 設定 5-year 假設；驅動 bottom-up DCF。
- **WACC Estimation Standard**：WACC = (E/V)×Re + (D/V)×Rd×(1-t)；Re 用 CAPM；β 用 5-year weekly regression + industry average；market risk premium 5-7%；risk-free 用 10-year sovereign。
- **Sensitivity + Scenario Together**：Sensitivity 變動單一 input（e.g., WACC ±1%），Scenario 同時變動多 inputs（e.g., recession = lower growth + higher WACC）；兩者結合 presents realistic range。
- **ROIC Decomposition (DuPont)**：ROIC = (NOPLAT / Revenue) × (Revenue / Invested Capital) = operating margin × capital turnover；改善哪項更容易？margin 多為 strategic，turnover 多為 operational。
- **Peer Comparable with Forward Multiples**：trailing P/E vs forward P/E 差異大，用 forward 12-month；EV/EBITDA 比 P/E 更 capital-structure-agnostic；EV/Sales 用於 unprofitable growth companies。

### 盲點 / 反例 / 適用邊界
- **高成長 / 虧損公司 DCF 困難** — DCF 對 steady-state 公司有效；對 Amazon、Uber、SpaceX 等長期虧損 + 高增長公司，terminal value 敏感度爆炸；McKinsey 的解法 (Part Six)是多 scenario 但仍不精確。
- **Intangibles 價值低估** — GAAP 不計自產 intangibles（brand, R&D, customer relationships）；book invested capital 低估導致 ROIC 虛高。McKinsey 提 adjust 方法但未標準化，跨公司比較困難。
- **WACC 的 circular reasoning** — WACC 用 market value 權重，但 market value 來自 DCF，DCF 用 WACC；理論上 iterative solver，實務多用 target capital structure 近似。
- **管理層 short-termism** — McKinsey 提倡 long-term EP 但承認多數上市公司做不到——董事會、機構投資者、sell-side analyst 都以 quarterly EPS 為導向；書中批評現狀但解法有限。
- **未充分涵蓋 ESG / stakeholder capitalism** — 2020 後 BlackRock、Business Roundtable 等提倡 stakeholder value，與 McKinsey 的 pure shareholder value 觀點有張力；最新版需更新。

### 與 Edward 既有知識的連結
- **對應 Rosenbaum-Pearl**：後者是 banker 操作手冊，McKinsey 是 strategic 長期思維；兩本互補——做 deal 用 Rosenbaum-Pearl，管公司用 McKinsey。
- **對應 Buffett / Munger 框架**：McKinsey 的 ROIC > WACC 原則正是 Buffett 的「moat + 長期複利」在財務指標上的量化表達；兩者同源。
- **ZP 應用**：McKinsey 框架可用於 Edward 個人事業決策——把「數位永生樹」當 company，評估每個 branch 的 ROIC（投入 vs 回報）；低 ROIC 的 branch 應 prune。
- **衝突 Quant Trading**：McKinsey 偏 fundamental long-term investor 視角，Edward 的自營交易偏 short-term systematic；應明確 separate 兩個 mental model。
- **可挖金礦**：Part Six Special Situations 的 distressed / emerging market / financial institutions 估值方法可作為 Edward 評估不同 asset class 的 reference；特別是 cross-border 章節對台灣公司估值有直接應用。
- **延伸應用**：若 Edward 將來做 family office 或公司投資（如技術入股新創），McKinsey 是評估 target 的 standard framework；加上 Rosenbaum-Pearl 的 M&A 流程知識即完整。
