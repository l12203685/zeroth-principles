## Extreme Value Methods with Applications to Finance — Serguei Y. Novak
**來源**: E:/書籍/Novak, Serguei-Extreme Value Methods with Applications to Finance-CRC Press (2011).pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Part I: Distribution of Extremes**
  - Ch 1 Methods of Extreme Value Theory (EVT 基礎)
  - Ch 2 Maximum of Partial Sums
  - Ch 3 Extremes in Samples of Random Size
  - Ch 4 Poisson Approximation
  - Ch 5 Compound Poisson Approximation
  - Ch 6 Exceedances of Several Levels
  - Ch 7 Processes of Exceedances
  - Ch 8 Beyond Compound Poisson
- **Part II: Statistics of Extremes**
  - Ch 9 Inference on Heavy Tails (Hill estimator, POT)
  - Ch 10 Value-at-Risk (VaR based on EVT)
  - Ch 11 Extremal Index (dependence in extremes)
  - Ch 12 Normal Approximation
  - Ch 13 Lower Bounds
- **Ch 14 Appendix** (probability background)

### TL;DR (≤120字)
CRC Monograph 級 EVT (Extreme Value Theory) 完整教材,應用聚焦金融:heavy-tail distribution 識別、POT (Peaks-Over-Threshold) 方法、VaR based on EVT、extremal index (連續超越的相依結構)。比 Embrechts 1997 更新,比 de Haan-Ferreira 更偏 finance 應用。是專業 risk manager 的深度參考。

### 核心本質 (3-5 條, 每條 50-120字)
1. **金融報酬尾部非常態,VaR 基於常態的結構性錯誤** — Ch1, Ch9 實證:股市日報酬尾部指數 (tail index) 通常在 2-5 之間;用 Gaussian VaR 會低估尾部 50%+。EVT 是唯一為「尾部」而設計的統計方法,提供 non-degenerate 的漸進分布 (Fréchet / Gumbel / Weibull GEV 族)。
2. **Peaks-Over-Threshold (POT) 方法優於 Block Maxima** — Ch1 主張:用「超過某閾值的全部觀測」比「每週/月的最大值」更有效利用資料;超越量的條件分布漸進為 Generalized Pareto Distribution。金融實作上 POT 是 standard,閾值選擇是關鍵技巧(u-plot)。
3. **Extremal Index θ 衡量尾部事件的「連發性」** — Ch11:IID case θ=1 (每次超越獨立);金融實證 θ≈0.3-0.7,意味一旦出現極端事件,有顯著機率短期內再次發生 (volatility clustering 的尾部表現)。忽略 θ 會嚴重低估短期連續損失機率。
4. **Hill estimator 是 tail index 的最廣泛使用估計量** — Ch9:取前 k 大觀測,Hill = (1/k) Σ log(X_{(i)} / X_{(k+1)})^(-1);對 Pareto-like 分布 consistent;但對 k 選擇極敏感,需 bias-variance tradeoff 分析。實作上 Hill plot 是判斷 k 的標準工具。
5. **EVT-based VaR 與 Expected Shortfall 是真正的 tail risk metrics** — Ch10:標準 Gaussian VaR 在 99% 以上嚴重低估;EVT-based ES(99.5%) 提供更穩健的極端損失期望值,符合 Basel 2.5 與 III 的 "sensitivity to tail" 要求。

### 可用戰術/策略
- **Hill estimator + POT 作為 B1 系統的 tail risk module** — 對每個 strategy 的 daily PnL 分布套 POT 擬合 GPD,估計 99.5% VaR 與 ES;用 Hill plot 決定閾值;比 historical VaR 在小樣本下更穩定。
- **Extremal index 監控作為 regime shift 訊號** — 動態估計 recent 60 日的 θ;若 θ 從 1 (IID) 降至 0.3 (高度 clustered),表示市場進入 regime — 啟動減倉規則。
- **Stress test with EVT-calibrated extreme scenarios** — 用 POT 擬合的 GPD 生成極端情境(如 1-in-1000 日損失);B1 系統的壓力測試情境應以此方式生成,而非純歷史最大值(太保守)或純 Gaussian 3-5σ(太不保守)。
- **Copula + EVT 的 multivariate extreme 建模** — Ch 以 EVT 處理 marginal tail;跨資產的 joint extremes 須配 extreme value copula 或 t-copula with high df;用於 portfolio tail risk (多資產同時暴跌的機率)。

### 盲點 / 反例 / 適用邊界
- **樣本需求高,短歷史資料難以 reliable 估計 tail index** — 通常需 10+ 年日頻資料;對新資產(加密幣、新上市 ETF)EVT 結果不穩,需用 prior / hierarchical approach 補救。
- **POT 對閾值選擇敏感,主觀性殘留** — u-plot + mean excess plot 提供 guidance 但非確定性 rule;兩個分析師可能給出顯著不同 VaR 估計;文化上稱為 "art of threshold choice"。
- **假設 stationarity** — 金融時序常有 regime shift,tail structure 本身隨時間變化;Dynamic EVT / time-varying GPD 是延伸但更複雜;常規 POT 需搭配 rolling window 重新估計。
- **純數學教科書,實作 code 自備** — 不附 Python/R code;實作可用 `scipy.stats.genpareto`、`evir` 套件、或自己寫 100-200 行 MLE + numerical optimization。

### 與 Edward 既有知識的連結
- 補完 Cont 2001 (stylized facts 提出 heavy tail 事實) → Jorion FRM (VaR 基本) → Novak (EVT 嚴謹處理) 的 tail risk 理論 → 估計鏈。
- 對應 `risk_control_four_layers` 的 L3 (尾部保險):Novak 告訴你「尾部有多厚 + 有多 clustered」,決定 tail hedge 規模與類型(OTM put、VIX calls、CDS);不做 EVT 分析的 tail hedge 是盲猜。
- 連結 `backtest_methodology`:回測的 Sharpe / Max DD 受 tail 影響極大;用 EVT-based confidence intervals 比 bootstrap 更可靠地量化策略 tail risk 不確定性。
- 對 B1 自營交易系統的貢獻:tail risk module 建議核心採用 EVT POT;任何 position sizing 以「99.5% EVT-ES」為硬約束,不超此值進場。
