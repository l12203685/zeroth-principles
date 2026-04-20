## 1082AIIA10_AI_for_Investment_Analysis — 未標示
**來源**: E:/投資交易/交易學習資料庫/@交易/temp/1082AIIA10_AI_for_Investment_Analysis.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1. Payments**
- **2. Insurance**
- **3. Deposits & Lending**
- **4. Capital Raising**
- **5. Investment Management**
- **6. Market Provisioning**

### TL;DR (≤120字)
本書屬於 ml for finance 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **金融時序資料是非平穩的** — 機器學習的 i.i.d. 假設在市場失效,這是所有金融 ML 失靈的本質原因
2. **樣本外績效下降是常態不是異常** — 模型週期性重訓、特徵漂移監測應視為系統常規模組,而非意外處理
3. **訊號強度 vs. 成本** — ML 模型發現的 alpha 往往小於 bid-ask 與手續費,backtest 必須內含實務成本

### 可用戰術/策略

- 使用 walk-forward validation + purged k-fold 防止時序洩漏
- ensemble 多個弱訊號而非單一強訊號,降低 overfitting 風險

### 盲點 / 反例 / 適用邊界

- ML 模型在結構性變化 (央行政策轉向、市場微結構改變) 下失效,必須有 regime detection 做護欄

### 與 Edward 既有知識的連結

- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
- 呼應零式原則 *information_asymmetry_action* — 有邊際資訊優勢才進場
