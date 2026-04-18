## Legal, Accounting and Ethics for Derivatives (PASS PRO 考題彙編) — Inmarkets Ltd (2004)
**來源**: C:/Users/admin/staging/b2_batch_D_extracts/91aea3e6e8c108df__legal_accounting_and_ethics.md  |  **消化日**: 2026-04-18  |  **模型**: claude-opus-4-7[1m] (main session)

### 目錄（主題分類重整）
- §A 會計準則（FAS 133 / SFAS 133 金融衍生品會計、hedge accounting 效益測試、fair value 測量、cash flow hedge vs fair value hedge）
- §B G-30 衍生品治理原則（外包限制、從業人員資格、風險管理結構、independent valuation）
- §C Mark-to-Market 方法論（OTC 契約估值優先順序、observable prices > broker quotes > simulation > trader's EOD）
- §D Hedge Effectiveness 測試（prospective vs retrospective assessment、80-125% rule）
- §E Embedded Derivatives（何時應與 host contract 分離、經濟特性「clearly and closely related」判準）
- §F Cross-Border Mark-to-Market（跨時區 Singapore/London 期貨部位估值規則）
- §G Hedge Fund 風險（槓桿、對沖 vs 投機、不對稱資訊）
- §H Suspense Account 處置（交易差異發生時的內控流程）
- §I Net Investment Hedge 會計（外幣子公司權益的特殊處理、P&L 時機）
- §J 衍生品定義例外（保險合約、財務擔保）

### TL;DR (≤120字)
Inmarkets PASS PRO 考題彙編揭露 2004 年全球衍生品從業人員需通過的法律、會計、倫理關卡：FAS 133 規定所有 derivatives 必須 mark-to-market 並上資產負債表、hedge accounting 嚴格的 80-125% 效益測試門檻是 Enron/Worldcom 後的監管遺產；對量化交易者啟示：策略 alpha 再強，若會計/法律結構錯，利潤會被 restate 與罰款吃光。

### 核心本質 (3-5 條)
1. **FAS 133 = 衍生品上表強制令**（本質） — 題 3、13、15 反覆考：2001 後 SFAS 133 要求所有 derivatives 以 fair value 計入資產負債表；這終結了 Enron 時代「把衍生品放在 footnote」的 off-balance-sheet 財技。對量化基金：策略內含的 swap、forward、option 無論實體上是不是 derivative 合約，都需 fair value 計價，若無法取得市場價需自行 modeling + audit 驗證。
2. **Hedge Accounting 的門檻非常高**（本質） — 題 4、6、7、9、10 揭示：僅當 derivative 通過 highly effective 測試（80-125% 範圍內的價值變動相互抵銷）才能享 hedge accounting 待遇；未通過則衍生品的 P&L 當期入帳，造成盈餘波動。實務意義：大多數 hedge 策略並不享會計優惠，名義「hedge」可能在會計上加劇波動。
3. **Observable Price > Broker Quote > Simulation > Trader EOD**（本質） — 題 8、19 的 mark-to-market valuation hierarchy 是後來 IFRS 13 / ASC 820 的 Level 1/2/3 分級前身：observable 市價最可信、broker 報價次之、模擬結果再次、交易員自報值最不可信（利益衝突）；內控要求優先使用高階層資料。
4. **Embedded Derivative 分離原則**（本質） — 題 1：當 embedded derivative 與 host contract 的「經濟特性 not clearly and closely related」時需分離會計處理；此判斷影響 convertible bond、structured notes 的會計處理，錯誤分類會導致重大 restatement 風險。
5. **G-30 治理建議的 10 大條**（本質） — 題 2：衍生品活動不可完全外包、人員需具備技能與經驗、會計需 consistent income recognition、中後台需獨立於交易員；這套 1993 年的 G-30 建議後來演化為 Barings 倒閉後的 OCC 指引、Basel II operational risk 章節，是現代 bank risk mgmt 的治理根基。

### 可用戰術/策略
- **選擇是否 hedge accounting**：評估策略是否會影響公司損益波動門檻；若策略 P&L 波動小 → 不需 hedge accounting，用 mark-to-market 入帳；若策略 P&L 會衝擊到 quarterly earnings target → 嚴格走 hedge accounting 流程。
- **OTC 估值流程**：建立 valuation hierarchy policy：1) 若同商品有 liquid exchange price → 直接用；2) 若有 broker consensus → 平均 3 家以上；3) 若只能 model → 文件化 calibration + monthly back-testing。
- **Suspense Account 管控**（題 5、16）：建立 daily reconciliation SOP，交易差異當日 identify 後 1) 小於 $1K 可當日 clear；2) $1K-$10K 進 suspense 當週解決；3) 超 $10K 立即升級給 CFO。
- **Net Investment Hedge 操作**：外幣子公司權益只有在 subsidiary 被清算時才計入 P&L（題 21）；平時 FX 衝擊放 OCI（Other Comprehensive Income），不影響 earnings；可利用此機制規劃跨國交易策略。
- **衍生品例外 checkpoint**（題 17）：遇到保險合約、financial guarantee、某些「impede sale accounting」的衍生品，不套用 FAS 133 規則；需先檢查例外再考慮一般規則。

### 盲點 / 反例 / 適用邊界
- **考題形式限制深度** — 59 頁考題彙編，每題 4 選 1；缺乏實際案例分析與應用情境；需搭配 PwC/Deloitte 的 FAS 133 implementation guide 才能完整理解。
- **2004 年 snapshot，已過時** — FAS 133 已被 ASC 815 取代（2009 整合），IFRS 9 取代 IAS 39；2010 Dodd-Frank 對 swap 分類、clearing 要求大幅改變；2018 FASB ASU 2017-12 簡化 hedge accounting。
- **美國 GAAP 中心** — 台灣上市公司採用 IFRS + TIFRS；雖然 IFRS 9 與 ASC 815 核心邏輯相近，但細節差異（如 OCI 選項、hedge documentation 要求）可能不同。
- **Hedge Fund 風險論述過簡**（題 18）— 「hedge funds 高槓桿所以更風險」的教科書答案在 LTCM、Archegos 事件後被複雜化；當代理解需加入「hidden leverage via swap」「prime broker concentration」等現代視角。
- **倫理部分稀薄** — 雖書名含 ethics，考題絕大多數是 FAS 133 技術題；真正的 ethics（front-running、material non-public info、conflicts of interest）討論有限。

### 與 Edward 既有知識的連結
- **對齊 ZP 核心**：mark-to-market valuation hierarchy 對應零式投資本質 — 任何「價值」都是某種資訊源的函數；source 越不獨立越不可信；這套層級可延伸到 Edward 對 AI 輸出結果的信度評估（live benchmark > committed output > unverified claim）。
- **延伸既有 DNA**：hedge accounting 的 80-125% 效益測試是「量化 rules 控制主觀判斷」的經典範例，符合 DNA §2 「Work model」鐵律 — 主 session 的情緒判斷需被規則框住，否則退化為直覺交易。
- **衝突點**：本文完全 US public company 中心，Edward 自營交易無此會計合規要求；但建立內部「shadow hedge accounting」框架仍有價值，可作為自我評估策略一致性的工具。
- **可挖金礦**：G-30 建議的「人員、系統、流程、governance 四軸」可複製為 Edward 永生樹的 operational risk framework：人員=subagent 能力檢核、系統=dashboard/credential vault、流程=`/go` SOP + tree_registry、governance=零式檢核 + Edward overrides。這套 framework 可避免「系統運作但方向偏離」的 slow drift。
