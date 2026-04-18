## Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues — Rama Cont
**來源**: E:/投資交易/交易學習資料庫/@交易/2. 財務相關知識/papers/2001 Cont-Empirical properties of asset returns-stylized facts and.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Abstract / Introduction**
- **1. What is a stylized fact?**
- **2. Stylized statistical properties of asset returns** (11 項)
  - 無自相關 / 厚尾 / 得失不對稱 / 尺度聚合高斯化 / 間歇性
  - 波動率群聚 / 條件厚尾 / 絕對報酬慢衰減 / 槓桿效應 / 量價相關 / 時間尺度不對稱
- **3. Some issues about statistical estimation**
  - 3.1 Stationarity / 3.2 Ergodicity / 3.3 Sample size
- **4. Distributional properties of returns**
- **5. Tail properties and extreme fluctuations**
- **6. Dependence properties**
- **7. Cross-sectional dependence**
- **References** (14 頁, 114 條)

### TL;DR (≤120字)
跨市場、跨商品、跨週期的資產報酬呈現 11 項「風格化事實」——無線性自相關卻有厚尾、波動群聚、槓桿效應、絕對報酬長記憶——任何定價模型若無法同時重現這組現象,即為錯誤假設。此文是量化金融的「必須通過的考試」。

### 核心本質 (3-5 條, 每條 50-120字)
1. **報酬分佈非高斯,模型假設正態即為結構性錯誤** — 無條件報酬呈 Pareto 厚尾 (tail index 2-5),極端事件頻率遠高於常態預測。Black-Scholes、VaR (常態版) 等依賴正態假設的工具在尾部失效,所謂「黑天鵝」在統計上是可預期的厚尾現實。
2. **波動率群聚 = 隱藏狀態變量** — 波動率本身呈正自相關且絕對報酬自相關以冪律 β∈[0.2, 0.4] 慢衰減,意味存在長記憶隱藏變量驅動。GARCH 族捕捉短期但無法解釋 long-range dependence。
3. **線性統計不可靠,非線性依賴才是訊號** — 報酬線性自相關幾乎為零(市場效率),但絕對報酬/平方報酬自相關顯著。做 alpha 不看原始報酬相關,要看|r| 或 r² 的依賴結構。
4. **時間尺度是一個獨立參數,不是無關細節** — 分布形狀隨 Δt 由厚尾向高斯收斂 (aggregational Gaussianity),粗粒度波動率預測細粒度波動率效果好於反向 (HARCH asymmetry)。任何策略都須標明「在什麼時間尺度成立」。
5. **Stationarity 與 ergodicity 是所有統計分析的暗前提** — 長記憶過程可能不遍歷,意味樣本平均 ≠ 期望。這直接挑戰「拿 10 年數據估未來均值」這類做法,尤其在崩盤樣本少時。

### 可用戰術/策略
- **做風險管理前先做「stylized facts 核對表」** — 任何模型/策略上線前,列出它隱含的機率假設並對照 Cont 11 條檢驗:假設是否允許厚尾?是否允許波動群聚?是否允許槓桿效應?不過關則已知會在極端市況失效。
- **以 |r| 或 r² 自相關為因子原料,而非 r** — 量化訊號設計時優先利用絕對報酬/平方報酬的長記憶,而不是報酬本身的線性預測(後者已被市場效率吃掉)。
- **尺度選擇 = 策略設計一部分** — 在策略文件中明定回測尺度 (tick/分鐘/日/週),評估在相鄰尺度 (×2、×0.5) 上是否仍有 edge;若只在單一尺度顯著,屬於過擬合紅旗。
- **尾部採用 semi-parametric / EVT 估計** — Hill estimator、peaks-over-threshold,比全分布擬合更穩健地捕捉 tail index,用於壓力測試與倉位上限。

### 盲點 / 反例 / 適用邊界
- **11 條普適性被限於 developed liquid markets** — 新興市場、流動性極低標的、加密資產早期數據可能違反 (如交易量 / 波動相關性在某些 DEX 上反向)。盲目套用於小幣或鏈上活動須重新驗證。
- **極短 (<20 分鐘) 尺度下,微結構效應反轉若干 stylized facts** — 如負的一階自相關 (mean reversion from bid-ask bounce)。純高頻策略要另建 stylized facts 集。
- **2001 年文章,未納入 HFT、算法交易興起後的結構性變化** — 2010 後的閃崩 / 電子化交易使部分依賴/分布性質略有變化;論文結論的 direction 仍成立,magnitude 須重估。

### 與 Edward 既有知識的連結
- 直接對應零式第 5 條 `bias_toward_inaction` 的底層:厚尾 + 槓桿效應 → 不對稱損失,No edge → No move 在統計上是 EV 保護。
- 連結 `risk_control_four_layers` L1 (倉位上限):Cont 的 tail index 估計就是「多少倍標準差對應多少機率」的量化依據。
- 擴展 `backtest_methodology`:回測若無法重現 11 條 stylized facts,必屬模擬偏差;蒙地卡羅資料生成器須匹配這些特徵方可壓力測試。
- 衝突於 `derivative_over_level` 的「純一階變化率」直覺:絕對報酬的 long-range dependence 提示二階/高階動能也含 alpha,不只一階 derivative 有效。
