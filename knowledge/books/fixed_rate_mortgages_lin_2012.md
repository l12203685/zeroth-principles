## Fixed Rate Mortgages (NTHU Real Estate Finance Lecture) — Dr. Che-Chun Lin (2012)
**來源**: C:/Users/admin/staging/b2_batch_E_extracts/2e8dcaa2ba4e125d__2_fixed_rate_mortgages_2012.md  |  **消化日**: 2026-04-18  |  **模型**: claude-opus-4-7[1m] (main session)

### 目錄
- §1 固定利率貸款構成（違約風險、利率風險、預期通膨 + 未預期通膨、提前清償風險、流動性風險、立法風險 — Fed 利率政策影響）
- §2 機械原理（Cash₀ = PV₀(Future Cash Flows)、本金 Principal、利率、期限、月付額、攤銷表）
- §3 利率風險分解（通膨預期扭曲 borrower-lender 風險對稱性）
- §4 預付選擇權（burnout effect、S-curve prepayment、OAS 分析）
- §5 違約選擇權（房價下跌時 put 選擇權、LTV 敏感性）
- §6 CPR, SMM, PSA 指標家族與應用
- §7 攤銷表延伸（balloon mortgage, negative amortization, interest-only periods, ARM 的對照）

### TL;DR (≤120字)
Lin 教授把貸款利率拆成「實質利率 + 風險溢價 + 通膨預期」三部分，核心洞察：固定利率貸款是「借方持有雙重 option 的複合債」— 違約 put + 提前清償 call；貸款人定價必須對這兩個嵌入式選擇權收費，單純的年金 NPV 計算會嚴重低估利率 + 信用風險，進而低估 MBS 風險溢價。

### 核心本質 (3-5 條)
1. **固定利率貸款 = 債券 - 嵌入選擇權的複合合約**（本質） — 第 1-2 節關鍵分解：mortgage 對 lender 看似是簡單 annuity，但 borrower 保留了兩個選擇權（prepay / default）；完整定價必須是 PV(年金) - 提前清償選擇權價值 - 違約選擇權價值。忽略這兩個選擇權的定價會導致 2000-2007 次貸泡沫期的系統性低估。
2. **利率 = 實質利率 + 通膨預期 + 風險溢價**（本質） — Fisher 方程 iₜ = rₜ + pₜ + fₜ 的實務拆解；當未預期通膨偏離預期通膨時，borrower 若為固定利率會獲得通膨保護的 embedded inflation hedge，這是 lender 承擔的 unanticipated inflation risk。2022 美國通膨爆表，借 30yr 低利率 mortgage 的人得利，lender 失血，正是此原理。
3. **立法風險：政府可單方面改遊戲規則**（本質） — 被嚴重低估的風險：Fed 的 QE/QT、consumer protection rule、各州 foreclosure 法、Dodd-Frank 修法都直接改變 mortgage 價值。2010 後 foreclosure 程序延長、2020 COVID 暫停 eviction 都實證顯示 legislative risk 遠超 interest rate risk 的單獨貢獻。
4. **PV(Future CF) = 當下市價 只在 t=0 成立**（本質） — §2 強調：當貸款發放後，二級市場價格會與 future CF 的 PV 偏離，因為市場會重新定價 prepay/default option；此時 mortgage 成為 path-dependent 資產，不能用 YTM 計算，必須用 Monte Carlo 路徑法 + OAS 模型（Option-Adjusted Spread）。
5. **Prepayment 與 Extension 的雙向風險**（本質） — 利率下降 → 借款人 refinance → prepay 風險 → lender 收回本金只能以低利率再投資；利率上升 → prepay 減少 → extension 風險 → lender 資金鎖在低利率資產。不是單邊利率風險，是 convexity 負值（negative convexity）— MBS 的經典特徵。

### 可用戰術/策略
- **30yr Mortgage 作為通膨對沖工具**：借 30yr 固定低利率貸款等於做空「利率 + 通膨」；若 Edward 在台灣預期 10 年通膨將高於銀行鎖定利率，30yr 固定利率房貸是資本結構優化動作（而非消費）。
- **OAS 評估 MBS 投資**：當 Fannie/Freddie MBS 的 OAS > 100bp 時，隱含 prepay option 被低估，值得進場；< 50bp 時撤退。此心法可延伸到可轉換公司債 (convertible bond) 的 embedded call option 定價。
- **違約選擇權定價快速法**：以 LTV（Loan-to-Value）大於 1 時 put option at-the-money；當 LTV < 0.7 時，put 虛值且 time decay 快，違約 option 近乎歸零。Edward 觀察台灣房市時可用此心法判斷斷供潮可能性。
- **Prepay S-curve 校正**：refinance incentive = (current rate - mortgage rate) 超過 150bp 時 prepay 加速、> 200bp 飽和；與 burnout（已經 refi 過的人降低敏感）結合使用。
- **利率 shock + 通膨 shock 雙對沖**：持有 MBS 時同時做空 10yr UST 期貨（對 rate）+ 買入 TIPS breakeven（對 inflation surprise），結構性對沖但留下 credit spread 因子。

### 盲點 / 反例 / 適用邊界
- **美國 agency MBS 中心** — 講義假設 Fannie/Freddie 提供信用擔保；台灣、日本、德國 mortgage 市場結構完全不同（無政府擔保、recourse 差異、prepayment penalty 存在），直接套用會誤判。
- **未納入 2020-2024 REMIC 與結構化創新** — 2012 年教材之後，RPL（Re-Performing Loan）、Non-QM、Investor loan 等新類別興起，定價模型需延伸；ECB、BOE 買 MBS 也改變了供需結構。
- **信用評等依賴歷史模型** — 2007 次貸教訓：rating 機構的 default correlation 假設低估了 tail risk；講義只講 individual loan 違約機率，沒有對 systemic correlation 提供警告。
- **對手方風險未涵蓋** — servicer default、trustee default、insurance company（MBIA/AMBAC）違約的結構風險被淡化；2008 讓人見識到 monoline insurer 崩盤如何傳染 MBS。

### 與 Edward 既有知識的連結
- **對齊 ZP 核心**：mortgage 作為「債券減嵌入選擇權」的觀念完全對應零式投資本質 — 任何複雜金融資產都要分解回 fundamental building blocks（bond + option + forward），不應整包估值。
- **延伸既有 DNA**：prepayment vs extension 的 convexity 概念可比喻永生樹任務管理 — 任務推進太快（prepay）會把未來規劃搞短，推進太慢（extension）會讓過時任務鎖定資源，管理層要做的是「maintain positive convexity in task pipeline」。
- **衝突點**：台灣房貸市場多為浮動利率 + 可提前清償無罰金，與美國 30yr 固定不同；此講義對台灣市場直接應用有限，需重寫符合國內結構的模型。
- **可挖金礦**：§2 的 Cash₀ = PV₀(Future CF) 邏輯可直接應用於評估自己房貸的再融資決策 — 若新 rate 比舊 rate 低超過 50-100bp 且剩餘年限 > 5 年，值得 refinance；此計算可寫成簡單 Python 腳本供 Edward 家庭財務決策使用。
