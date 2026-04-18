# Quantitative Equity Portfolio Management: Modern Techniques and Applications — Qian, Hua, Sorensen

### 目錄
1. 核心本質 — 量化選股是「系統化擷取 information」的工業流程
2. 可用戰術 — IC / IR / Multifactor Alpha / Turnover 約束
3. 盲點/反例 — 2008 後 quant meltdown 對此框架的衝擊
4. 與 Edward 既有知識的連結

### TL;DR
Qian-Hua-Sorensen (Chapman & Hall/CRC Financial Mathematics Series #6, 2007) 三位作者均為 PanAgora Asset Management 的資深 quant，這本是 Grinold-Kahn 2000《Active Portfolio Management》的深化版，把 quant equity 的工作流程從理論到實作完整展開。**結構**：Part I 基礎（Ch 1 信念與風險流程、Ch 2 portfolio theory、Ch 3 APT 風險模型）、Part II 選股因子（Ch 4 alpha benchmark / IC / IR、Ch 5 Value/Quality/Momentum 三類量化因子、Ch 6 DCF valuation、Ch 7 Multifactor Alpha）、Part III 組合構建（Ch 8 turnover optimization、Ch 9-10 rebalancing + execution、Ch 11 risk parity）。**核心哲學**：quant equity 不是「找最好的單一因子」而是「把多個弱訊號透過風險模型 + 優化器聚合成 IR 高的 portfolio」——正是 Grinold 1989 的 Fundamental Law of Active Management: IR = IC · √breadth。

### 核心本質
1. **Information Coefficient × Breadth = Information Ratio（Ch 4.2-4.3, Fundamental Law）**：IC 是因子預測能力（預測 return 與實際 return 的相關係數），breadth 是獨立 bet 的數量，IR (Sharpe ratio of alpha) = IC · √breadth。IC 提升 0.01 或 breadth 翻倍同等 powerful。這公式決定 quant equity 的兩個 levers：找更強的因子（難） vs. 擴大覆蓋範圍（易）。實證 US equity value factor IC 約 0.03-0.05，Russell 3000 提供 3000 bets，IR = 0.03·√3000 ≈ 1.6（理論上限）。
2. **Value / Quality / Momentum 是長期有效的三大因子家族（Ch 5）**：Qian 實證 1987-2006 Russell 1000——(a) Value (P/E, P/B, EV/EBITDA): IC ~0.04, IR ~1.0；(b) Quality (ROA, earnings stability, low leverage): IC ~0.03, IR ~0.8；(c) Momentum (12-1 return, earnings revision): IC ~0.04, IR ~1.1。三者 correlation 低（avg pairwise 0.2），combine 後 IR 可達 1.8。這驗證 Asness-Moskowitz-Pedersen 2013 "Value and Momentum Everywhere" 的跨市場結論。
3. **Multifactor Alpha 的「最佳組合」有解析解（Ch 7.2）**：Qian 證明 optimal weights = Σ^{-1}·IC，其中 Σ 是 factor correlation matrix，IC 是各因子 IC 向量。這是標準 mean-variance 的衍生——把 alpha 看作 mean，factor correlation 看作 covariance。實務上用 shrinkage (Ledoit-Wolf 2003) 穩定 Σ^{-1}。
4. **Turnover 約束在 optimizer 中內生化（Ch 8.3-8.6）**：naive 的 alpha optimization 忽略交易成本——high-turnover portfolio 在 live 表現遠差於回測。Qian 提出 signal decay (Ch 8.5)：factor forecast 的 half-life 決定 rebalance 頻率——momentum ~1 月，value ~1 年，earnings revision ~1 週。Optimizer 加入 transaction cost penalty 後，turnover 自動降至 carrying value information vs. cost 的 optimal 水平。
5. **Barra-style Risk Model 的多因子分解（Ch 3.1）**：r_i = Σ β_{i,k}·f_k + ε_i，其中 f_k 是 industry, style (size/value/momentum/volatility/growth), macro factor。Portfolio risk = factor risk (σ_factor) + specific risk (σ_specific)。Active management 要同時 manage 兩者——factor exposure 決定 systematic alpha/risk，specific risk 決定 stock-picking noise。

### 可用戰術
1. **IC Decay 作為因子 horizon 測量（Ch 4.2）**：對每個 forecast horizon t 計算 IC(t) = corr(factor_0, return_t)，看衰減速度。Momentum 的 IC decay 快（1 月內從 0.05 降到 0.01），value 慢（12 月內仍 >0.03）。據此決定 rebalance 頻率與 weight——快衰因子大權重高頻。
2. **Fama-MacBeth Cross-Sectional Regression（Ch 7.5）**：每月對所有股票做 cross-section regression：r_i = α + Σ λ_k · X_{i,k} + ε_i，λ_k 是該月 factor 的「true return」。用時間序列 λ 計算 t-stat 判定因子顯著性。這是 1973 Fama-MacBeth 的標準做法，現代 factor discovery 仍用。
3. **Multipath DCF Analysis（Ch 6.7-6.8）**：把傳統 DCF 的單一 terminal value 擴展成多路徑（bull/base/bear/disaster），每條路徑有機率，取期望 NPV。比 stock screening 的 P/E 法則「有價值觀」——抓到 optionality 高的公司（bull path reward 大）。
4. **Fade Period 三段式估值（Ch 6.5）**：explicit (5 年) + fade (5 年 ROIC 線性回到 industry mean) + terminal（perpetuity）。Fade period 的引入防止 terminal 假設過度樂觀——「該公司將永遠保持 25% ROIC」在競爭下不可能。這讓 DCF 更 robust。
5. **Orthogonalized Factor Composite（Ch 7.4）**：multifactor 若原始 factor 高度相關（如 B/P 與 E/P correlation 0.7），直接加權會 double-count。先用 Gram-Schmidt 或 PCA 正交化再組合，避免維度壓縮扭曲 alpha。

### 盲點/反例
1. **2007 年出版，沒觸及 2007 Aug quant meltdown**：Khandani-Lo (2007) 指出 Aug 2007 第一週許多 quant equity strategy 同時崩潰（經典 factor 的 daily correlation 從 0.3 飆到 0.9）——crowded trade + deleveraging spiral。Qian-Hua-Sorensen 的框架假設 factor returns iid，但 crowded quant 的同質性打破了這個假設。
2. **Transaction Cost Model 過於簡化**：Ch 8 的 TC 模型只用 linear + quadratic，沒 market impact的冪次律（Almgren-Chriss 2001 的 3/5 power），對 size >1% ADV 的 trade 嚴重低估成本。實務上要用 Kissell《Science of Algo Trading》的 propagator model。
3. **High-frequency 與 intraday 完全缺席**：全書以 monthly rebalance 為基準，沒討論 intraday signal、reversal alpha、microstructure edge。做 Market Neutral 或 HFT 要補 Aldridge《High-Frequency Trading》（Round 1）。
4. **Factor Zoo 現象未預見**：Harvey-Liu-Zhu (2016 RFS) 整理出 316 個「顯著」因子，其中大部分是 data mining 結果。Qian 的 IC 檢定沒做 multiple testing correction，若對 100 個因子各測 IC，>5 個偽陽性是預期。
5. **Machine Learning 時代替代品**：2018+ Gu-Kelly-Xiu RFS 用 neural net 做 return prediction 顯示 R² 比 linear factor model 高 2-3x。Qian 2007 寫作時 sparse regression 剛起步，整本書沒 regularization、沒 cross-validation、沒 ensemble。

### 與 Edward 既有知識的連結
- **對照 Kelly-Xiu《Financial Machine Learning》（Round 1）**：Kelly-Xiu 是 Qian 框架的「ML 升級版」——同樣是多因子 return prediction，但用 ridge / neural net / autoencoder 替代 linear regression。Qian 提供 quant equity 的理論骨架，Kelly-Xiu 提供現代 ML 實作。
- **對照 Gibson《Asset Allocation》（Round 1）**：Gibson 是 macro asset class level (stocks/bonds/cash/real estate)，Qian 是 single stock level within equity class。兩個 layer 互補——asset allocation 決定 strategic β，quant equity 決定 tactical α。
- **對照 Greene / Wooldridge（本輪）**：Qian Ch 7.5 的 Fama-MacBeth regression 與 Greene Ch 11 panel data / Wooldridge Ch 14 FE-demean 技術上同源。多因子模型本質上是 cross-section panel regression 的實證應用。
- **對照 ZP/strategies/quant_equity 架構**：我 ZP 目前沒有 quant equity 策略，若要加這個 branch，Qian Ch 4 的 IC/IR evaluation + Ch 8 的 turnover optimization 是最小可行組合。Breadth = Taiwan listed stocks ~1700，若能做到 IC=0.03 則 IR ~1.2 理論上限。
- **對照 Poker 的「多手聚合 edge」**：撲克的 hourly win rate = per-hand EV × hands played，正是 IR = IC · √breadth 的同形式表達。Poker 玩 6 max vs. 9 max 的 breadth 差異也影響 overall EV。兩個領域 "small edge × high repetition = reliable P&L" 是同樣邏輯。
