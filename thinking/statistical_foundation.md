# 統計學基礎 — 從考試到實戰的知識映射

> Edward 的統計訓練路徑：統計所/高考準備 → 政府統計實務 → 量化交易應用 → ML for Finance

---

## 一、核心統計訓練特徵

### 證明導向（Proof-first）
不只記公式，做完整推導：
- E[MSE] = σ² 完整證明
- OLS estimators β̂₀, β̂₁ 抽樣分布
- SST = SSR + SSE 分解
- ANOVA F-table 推導

### 無母數直覺（Nonparametric Instinct）
深入掌握 Wilcoxon Rank-Sum Test：
- 理論推導 + 實際數據演練
- 處理 ties（平均 rank）
- 大樣本 Normal 近似

金融數據違反常態假設 → 無母數方法是自然選擇。

### 政府統計實務
- 景氣循環：成長循環法、Bry-Boschan 轉折點演算法
- 季節調整：X-12-ARIMA
- 趨勢估計：Phase Average Trend (PAT)
- 領先指標：6 月平滑年變動率
- 人口學：完整生命表（qx/lx/Lx/Tx/ex）

---

## 二、統計 → ML 的橋接

| 統計層 | ML 層 | 共同問題 |
|--------|--------|---------|
| 假設檢定 (Type I/II error) | Precision/Recall | 錯誤類型分析 |
| 時間序列分解 (T/C/S/I) | LSTM sequence prediction | 序列金融數據 |
| OLS 迴歸 | Linear regression baseline | 基線模型 |
| Sampling theory | Train/test split | 樣本代表性 |

### ML 應用到交易的具體實作
| Module | 方法 | 交易應用 |
|--------|------|---------|
| SVM | SVC + ROE+市值 features | 預測漲/平/跌（基本面特徵）|
| Random Forest | Feature importance | 選股因子排序 |
| LSTM | Sequence modeling | 價格時序預測 |
| Technical indicators | TA-Lib feature engineering | 信號生成 |
| Candlestick patterns | Pattern recognition + Pyfolio | 型態策略回測 |

**關鍵選擇**：SVM 用 ROE + 市值作為 features — 不是隨機選的，是 value-factor 思維嵌入 ML。

---

## 三、統計方法在交易中的延伸

### Runs Test
驗證策略回報序列是否隨機。非隨機 = 有 edge（或有 bug）。

### Kelly Criterion
`f = (b×p - q) / b`
實務用半凱利（1/2 或 1/3）降低波動。
模擬：25% 下注（富貴）> 12%（小康）> 50%（破產）。
Martingale 標記「絕對不可用」。

### Monte Carlo for Options
LSM（最小平方蒙地卡羅）用於美式選擇權定價。
效率：Control Variate > Antithetic Variate > 基本型。

### FOMC 語言信號量化
信號強度：`one → couple → few → a number of → several → some → many → most → consensus`
從 `several` 升至 `many/most` → 下次政策改變機率大增。

---

## 四、預測方法論

### Tetlock 框架（狐狸 vs 刺蝟）
- 刺蝟（單一大觀點）預測不準
- 狐狸（接受多種資訊，Bayesian 更新）較準
- 避免「濕偏差」（寧可報雨）和過度自信

### ML vs 傳統模型的結論
LSTM 預測股價不優於 ARIMA — Spectral Bias（優先擬合低頻 = 移動平均）。
歷史波動率無法解釋未來；隱含波動率是市場對未來的定價。

---

## 五、知識映射：考試 → 實戰

```
高考統計理論
  ↓ OLS/假設檢定/抽樣理論
政府統計實務
  ↓ 景氣循環/季節調整/生命表
鉅亨網數據分析
  ↓ 財神爺框架 (browsing → prediction)
量化交易
  ↓ MAE/MFE + Kelly + ATR position sizing
ML for Finance
  ↓ SVM/RF/LSTM applied to stock selection
零式系統
  ↓ 全部整合：本質思維 + 統計驗證 + 系統化執行
```
