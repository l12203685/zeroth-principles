## Correlated Intensity, Counterparty Risks, and Dependent Mortalities — Jin Ma, Youngyun Yun
**來源**: Insurance: Mathematics and Economics 2010 (USC Math 學術論文 15 pages)  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **Introduction: intensity-based correlated defaults**
- **Representation theorem for joint survival probabilities**
- **Change-of-measure approach (following Collin-Dufresne 2004)**
- **Application: counter-party risk models (Jarrow-Yu 2001)**
- **Flight-to-quality phenomenon**
- **Dependent mortality: spousal bereavement**
- **Universal Variable Life (UVL) insurance indifference pricing**
- **Explicit first-to-default / last-to-default formulae**

### TL;DR
Ma & Yun 2010 論文統一「correlated intensity default」與「dependent mortality」的數學框架,用 representation theorem 導出多家企業聯合生存機率的顯式公式;可應用於 CCPR (counterparty credit risk)、flight-to-quality、Universal Variable Life (UVL) 保險定價。

### 核心本質
1. **Intensity-based framework 是結構化 default modeling 的現代主流** — 把違約事件視為首次 Poisson 跳事件,強度 λ(t) 可依狀態變數、市場因子隨機演化;比 structural model (Merton) 更靈活、計算更簡便、貼近 CDS 市場資料。
2. **Counterparty risk ≠ standalone default risk** — 在衍生品交易中,對手方違約的機率與本公司違約機率相依;若忽略相依性 (assumption of independence) 會 systematically underprice 對手方 CVA。Jarrow-Yu 2001 首先形式化此問題。
3. **Change-of-measure technique 把 correlated defaults 變為 tractable** — 本文核心貢獻:選擇適當 Radon-Nikodym derivative,讓相依違約下的聯合生存機率在新 measure 下變成獨立積,計算量從指數級降為 polynomial。
4. **Flight-to-quality 的數學化** — 當系統性風險升溫(如 2008 雷曼事件),違約強度正相關放大,投資人從高風險資產流向優質資產;本文提供 intensity correlation 的顯式建模,可量化 flight-to-quality 的 contagion 速度。
5. **Mortality correlation = corporate default correlation 的同構** — 夫妻喪偶後死亡率上升(widowhood effect)與企業間違約相依數學結構相同,本文展示「違約 = 首跳」的普適性,打通金融與保險精算的方法論橋樑。

### 可用戰術/策略
- **CVA 計算**:交易對手 CDS spread 反解 default intensity → 用本文公式計算與本公司 default 相依的 joint survival → CVA 調整 (wrong-way risk)。
- **First-to-default basket 定價**:N 家企業 basket CDS,用本文 representation theorem 對多變量 joint survival 直接 closed-form(避免 Monte Carlo)。
- **UVL 保險精算**:對 joint-life / last-survivor 保單,用本文 explicit 公式計算 indifference price,不需 solve PDE。
- **Regime-aware intensity**:在 stress regime 中提高 correlation 參數,在正常 regime 回落,做動態 intensity 調整。

### 盲點 / 反例 / 適用邊界
- **intensity 的 stochastic process 需假設**:本文假設 intensity 依 affine jump-diffusion,對非 affine 模型(如 Heston-type)延伸需額外工作。
- **校準困難:CDS 流動性不足**:對 illiquid credit (私募債、EM sovereign),CDS spread 不可信,intensity 反解噪音大。
- **correlation 參數歷史校準 vs 隱含校準**:歷史資料校準可能 underprice tail risk(尤其 2008 前的資料),implied calibration 依賴 CDO / CDS index 價格,兩者常不一致。
- **適用邊界**:信用組合風險量測、counterparty CVA、basket credit derivative、joint-life insurance;不適用 jump-to-default 或 contagion-driven 多 regime 系統。

### 與 Edward 既有知識的連結
- 呼應 **risk_control_four_layers**:counterparty risk 是「交易架構層」的關鍵風控,本文提供量化工具;四層風控的第二層 (策略風險) 與第四層 (系統風險) 的橋樑。
- 對照 **Li 2000 copula paper**:Li 用 copula 處理默契相依,本文用 intensity + change-of-measure,兩者數學等價但技術路徑不同;copula 更直覺、intensity 更通用。
- 補強 **meta_strategy_over_strategy**:2008 危機後,忽略 counterparty risk 的 meta-strategy 崩壞;本文是 meta-strategy 設計必備的風險量化工具。
- 連結 **information_asymmetry_action**:intensity correlation 是市場參與者普遍低估的相依結構,2008 證明這是系統性 asymmetry;2008 後才廣泛 pricing,先用者獲利超額。
