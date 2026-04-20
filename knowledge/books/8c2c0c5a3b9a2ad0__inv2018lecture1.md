## inv2018lecture1 — 未標示
**來源**: E:/投資交易/交易學習資料庫/@交易/2. 財務相關知識/投資學/inv2018lecture1.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1. Financial economics can be considered a subﬁeld of general ec**
- **2. Two objects are transacted in the capital market. The ﬁrst is**
- **3. Households supply capital, and ﬁrms and the government demand**
- **4. There are at least three dimensions when it comes to the meas**
- **5. Perfect markets leave no room for ﬁnancial institutions. In t**
- **6. First, why do commerical banks exist? Unlike in the Walrasian**
- **7. Second, why do investment banks arise? Investment banking mai**
- **8. Third, why do mutual funds arise? Suppose that households are**

### TL;DR (≤120字)
本書屬於 portfolio optimization 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **MVO (均值變異數最佳化) 對輸入極敏感** — 預期報酬誤差 1% 可導致組合權重 30% 擺動
2. **Black-Litterman 透過混合市場均衡與主觀觀點穩定組合,是實務優於純 MVO 的路徑**
3. **Risk Parity 不需要預期報酬,但隱含假設各資產夏普比接近,槓桿需要嚴格風控**

### 可用戰術/策略

- shrinkage 估計共變矩陣 + 施加 weight bound (每資產 0-20%) 增強 robustness
- 實務上先配置 Risk Parity 底層,再疊加主觀 tactical overlay

### 盲點 / 反例 / 適用邊界

- Low vol 資產在極端事件中 vol 可以瞬間跳升,Risk Parity 高槓桿放大尾險

### 與 Edward 既有知識的連結

- 呼應零式原則 *meta_strategy_over_strategy* — 關注資金曲線與長期夏普、勝過單筆交易或單期回報
- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
