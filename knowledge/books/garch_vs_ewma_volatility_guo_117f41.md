## Estimating Volatilities by GARCH and EWMA: PetroChina and TCL — Haochen Guo
**來源**: 6th International Scientific Conference (Ostrava, 2012) conference paper 12 pages  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **Introduction: volatility in VaR / option pricing / portfolio optimization**
- **Estimating Volatility: historical / GARCH(1,1) / EWMA**
- **Maximum Likelihood Estimation**
- **Case study: PetroChina (SSE) & TCL (SZSE)**
- **Mean Square Error comparison**
- **Conclusion**

### TL;DR
小型比較研究,用 PetroChina + TCL 股價資料比較 GARCH(1,1) 與 EWMA 波動率預測。主要結論:GARCH(1,1) 在 PetroChina (大型、高流動性) 表現較佳;EWMA 在 TCL (小型) 因參數穩定且計算簡單而 MSE 較低。

### 核心本質
1. **GARCH 捕捉 volatility clustering,EWMA 是其限制特例** — EWMA 等價於 GARCH(1,1) 在 ω=0、α+β=1 的極限;GARCH 能捕捉 long-run mean reversion,EWMA 假設波動率無長期平均,只是指數加權歷史。
2. **MLE 校準 GARCH 需要足夠樣本** — GARCH(1,1) 三參數,需要 ≥250 日資料才能穩定估計;小樣本下 GARCH 不一定優於 EWMA,因為 overfitting 風險 > 結構靈活性收益。
3. **模型選擇應依市場特性而非理論優越性** — 本文展示同一方法在不同股票上相對表現不同:liquid 大型股 GARCH 勝,illiquid 小型股 EWMA 勝。模型選擇是 empirical question。
4. **MSE 不是唯一評價準則** — 波動率預測還需考慮 VaR 覆蓋率、選擇權定價誤差、bias-variance trade-off;純 MSE 可能偏袒平滑模型(EWMA),忽略尾部準確性。
5. **中國 A 股有特殊微觀結構** — 漲跌停限制、T+1、散戶主導造成波動率行為與美股差異;直接套用西方 GARCH 參數可能系統性失準,需本地化校準。

### 可用戰術/策略
- **雙模型備援**:主策略用 GARCH(1,1),備援 EWMA(λ=0.94, RiskMetrics 預設);比較兩者預測差異 > 1 σ 時視為 regime shift 警訊。
- **樣本自適應切換**:樣本 <250 點用 EWMA,>500 點用 GARCH(1,1);避免 GARCH 在小樣本下的參數不穩定。
- **VaR backtesting**:用 Kupiec POF test 或 Christoffersen 獨立性檢定衡量 VaR 覆蓋率,不只看 MSE。
- **隱含 vs 實現波動率套利**:用 GARCH 預測實現波動率,對比 option 隱含波動率,建立 variance risk premium 套利倉。

### 盲點 / 反例 / 適用邊界
- **樣本量不足**:僅兩檔個股、短樣本,結論無法一般化;應至少 50+ 股票、10+ 年資料才能 robust conclusion。
- **未納入 asymmetric GARCH (EGARCH, GJR)**:忽略 leverage effect(壞消息比好消息推波動率更強),尤其股市資料 asymmetric GARCH 通常顯著勝過對稱 GARCH。
- **out-of-sample 驗證不足**:MSE 比較是 in-sample,缺 rolling window 的 OOS 測試,結論可能 overfit。
- **適用邊界**:教學展示 / 初階應用;專業實務應採用 realized volatility + HAR-RV 模型(更精確)、多變量 DCC-GARCH(捕捉相關性動態)。

### 與 Edward 既有知識的連結
- 對齊 **derivative_over_level**:volatility 是報酬的 derivative quantity,預測 vol 比預測 return 更有 structural edge;本文是具體方法論呈現。
- 補強 **backtest_methodology**:模型選擇需 empirical test (MSE, VaR coverage) 而非理論優越性;符合 Aronson evidence-based TA 原則。
- 連結 **risk_control_four_layers**:vol forecast 是 risk-budgeting 的核心輸入,vol 估計誤差會傳導到 position sizing / VaR / margin call 機率。
- 呼應 **information_asymmetry_action**:EWMA 簡單穩定,是大量市場參與者共用的基準;edge 在能否用更精細的 HAR-RV、SV、jump-GARCH 取得預測優勢。
