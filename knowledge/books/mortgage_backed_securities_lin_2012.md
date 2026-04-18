## Mortgage-Backed Securities and Mortgage Derivatives (NTHU Real Estate Finance Lecture) — Dr. Che-Chun Lin (2012)
**來源**: C:/Users/admin/staging/b2_batch_E_extracts/b17bc3dcbb024485__7_mortgage_backed_securities_mortgage_derivatives_2012.md  |  **消化日**: 2026-04-18  |  **模型**: claude-opus-4-7[1m] (main session)

### 目錄
- §1 MBS 作為 mortgage 衍生品的技術定義（derive value from mortgage pool）
- §2 IO/PO Strips（Interest-Only / Principal-Only 分解、反向 interest rate 敏感度、prepayment 對兩者的對稱相反衝擊）
- §3 CMO（Collateralized Mortgage Obligations）結構
  - 3.1 Tranching 邏輯（sequential pay、PAC/companion、Z-bond、Residual）
  - 3.2 Cashflow waterfall 機制
  - 3.3 WAC (Weighted Avg Coupon)、WAM (Weighted Avg Maturity)
- §4 Prepayment 模型
  - 4.1 OTS（Office of Thrift Supervision）prepayment function
  - 4.2 CPR (Conditional Prepayment Rate)、SMM (Single Monthly Mortality)、PSA 基準
  - 4.3 S-curve、burnout effect
- §5 OAS 模型（Option-Adjusted Spread）
  - 5.1 利率路徑模擬
  - 5.2 Path-dependent valuation
- §6 擴展（CMBS 對比、Subprime/Alt-A 危機教訓、REMIC 結構）

### TL;DR (≤120字)
Lin 教授從 MBS 本質出發：所有 mortgage 衍生品的存在理由是「讓投資人精確管理 prepayment 與 extension 風險」，而非憑空創造報酬；IO/PO 對利率的反向對稱反應是 2007 次貸危機前的關鍵定價錯配 — 投行把本該對沖的 IO/PO 拆開賣給不同投資人，但模型低估了 prepayment 的 state-dependent correlation。

### 核心本質 (3-5 條)
1. **IO/PO 的反向利率敏感度**（本質） — §2 核心洞察：IO 隨利率上升而升值（因為 prepayment 減少，interest 繼續流入）；PO 隨利率下降而升值（因為 prepayment 加速，本金提早回流）。兩者組合 = MBS 原型，拆開後可讓投資人取決定方向暴露。這比純債券的線性利率敏感度更豐富，提供了 regime-switching hedging 工具。
2. **CMO Tranching 是風險重分配而非風險消滅**（本質） — §3 關鍵：把 mortgage pool 切 tranches 不會讓總風險減少，只會重新分配：PAC tranche 獲得 prepayment 保護 → companion tranche 承擔 residual prepayment volatility；這是零和結構。2007 次貸危機的錯誤在於評等機構把 senior tranche 評為 AAA，忽略了 default correlation 讓 senior tranche 在尾部事件中也會血流成河（Gaussian copula 系統性低估 tail dependency）。
3. **OAS = Spread 減去 Option Cost 的純信用利差**（本質） — §5 關鍵工具：OAS 從 nominal spread 中扣除 embedded prepay option 的價值，剩下的就是「純粹補償 credit + liquidity」的 spread。若 OAS < Treasury spread 甚至為負，該 MBS 被過度定價；若 OAS > 100-150bp，值得進場。
4. **Prepayment 是 state-dependent，不是 constant CPR**（本質） — §4 的 OTS 模型證明：prepayment rate 是「當前利率 - mortgage coupon」、burnout、房價、季節性的函數；用 constant CPR 估值會嚴重偏誤。S-curve 形狀在 refinance incentive 100-200bp 區間最陡，這段的微小利率變動引發大量 prepay。
5. **Negative Convexity 是 MBS 的結構性缺陷**（本質） — MBS 投資人永遠是 short gamma：利率下降 duration 縮短（錯過漲勢）、利率上升 duration 延長（放大跌勢）；這種 negative convexity 必須靠 hedging（short bond futures）或靠更高的 spread 補償來管理，不能忽略。

### 可用戰術/策略
- **IO/PO Ratio Hedge**：同時持有 IO 與 PO，比例由對利率觀點調整（rate down → 重 PO、rate up → 重 IO）；風險中性組合約等於純 MBS。
- **PAC-Companion Barbell**：在 PAC tranche（風險低、yield 低）與 companion tranche（風險高、yield 高）間配置，取得 barbell 相對於中等 tranche 的超額報酬（若對 prepay vol 有觀點）。
- **OAS Zscore 交易規則**：歷史 OAS 的 z-score > 1.5 → 做多 MBS vs Treasury；< -1.5 → 做空 MBS；中間 regime 不動。
- **Prepayment Model 驗證**：每季將模型預測 CPR 與實際 CPR 比對；若誤差連續 3 季 > 20%，模型需重新校正；長期誤差往同方向偏則證明 structural regime shift。
- **MBS 對沖配方**：每 $100mm MBS 配 short $25-40mm 10yr UST 期貨 + $10-15mm 5yr UST 期貨 = 對 duration 與 convexity 的粗對沖；精細化需納入 key rate duration。

### 盲點 / 反例 / 適用邊界
- **Gaussian Copula 的 systemic 盲點** — 課程仍教傳統 Gaussian copula 建模 default correlation；2007-2008 證明此模型在 tail 時期低估 correlation，應搭配 Marshall-Olkin copula 或 Student-t copula 補強。
- **Agency MBS 假設 credit-risk free** — 實際 2008 FNMA/FHLMC 進入 conservatorship，雖然最終 government bailout，但期間 spread 急速擴張；課程假設太樂觀。
- **未納入 CRT（Credit Risk Transfer）新結構** — 2013 後 FNMA/FHLMC 開始發行 STACR、CAS 把信用風險轉給私人投資人，這創造了新的 spread 機會，但 2012 講義未涵蓋。
- **Servicer 與 Trustee 風險被忽略** — Real-world 的 servicer 倒閉（2008 IndyMac、2023 SVB 附屬 servicer）會中斷現金流；課程模型假設 servicer 永遠運作。
- **Non-agency market 微小** — 課程重心仍在 agency MBS，對 jumbo、Alt-A、subprime non-agency MBS 的獨特信用風險刻畫淺。

### 與 Edward 既有知識的連結
- **對齊 ZP 核心**：MBS 的 tranching 是「風險重分配不是消滅」完全呼應零式投資本質 — 結構化產品的本質是 repackaging risk，不創造價值；投資人應問「我實際承擔的 underlying risk 是什麼」，不要被 AAA rating 迷惑。
- **延伸既有 DNA**：IO/PO 的反向對稱結構可比喻 Edward 工作的雙重角色 — DNA §2 董事長-總經理分工中，總經理承擔「quick task execution」（類似 PO 收本金快），董事長承擔「long-term yield」（類似 IO 收每月利息）；兩者對不同 regime 反應相反，組合起來才是完整的永生樹運作。
- **衝突點**：台灣 MBS 市場幾乎不存在，此講義在台灣實務應用有限；但概念可延伸到 CBO（Collateralized Bond Obligation）、CLO（Collateralized Loan Obligation）等其他結構化信用產品。
- **可挖金礦**：§4 的 OTS prepayment model 與 §5 的 OAS 路徑模擬是 Python/R 可實作的 mini-project，可作為 Edward ZP 結構化信用模組的原型基礎；同時 2007 次貸教訓（tail correlation 被低估）應植入所有 tranched product 評估的自動警示規則。
