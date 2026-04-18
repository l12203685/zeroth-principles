## Trading Systems: A New Approach to System Development and Portfolio Optimisation — Emilio Tomasini & Urban Jaekle

**來源**: E:/書籍/Trading Systems A new Approach to System Development and Portfolio Optimisation, Emilio Tomasini & Urban Jaekle (2009).pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 系統交易的理由（為何 retail 需要 system、discretionary 的不可複製性）
- 第 2 章 開發方法論（假設 → 編碼 → 回測 → 穩健性檢驗的迭代流程）
- 第 3 章 基本架構選擇（breakout、moving average、oscillator、pattern）
- 第 4 章 參數優化的陷阱（in-sample 過擬合、monkey problem）
- 第 5 章 穩健性檢驗（parameter sensitivity、walk-forward、robustness ratio）
- 第 6 章 交易成本的精確建模（spread、slippage、overnight fees、borrow cost）
- 第 7 章 組合交易系統（多策略、多市場、correlation matrix）
- 第 8 章 portfolio optimization（equal-weight、risk-parity、Markowitz、Black-Litterman）
- 第 9 章 實戰上線流程（paper、minimum size、scale up、monitoring）
- 第 10 章 持續改進與策略退化偵測
- 第 11 章 案例研究：德國股指 DAX 的長期 trend system 實作
- 第 12 章 reading list 與 further study

### TL;DR (≤120字)
Tomasini（義大利交易員）與 Jaekle（德國 quant）合著，是**歐洲視角的系統交易教材**：融合 German engineering 與 Italian 實戰。核心貢獻是「**robustness ratio**」（樣本外績效/樣本內績效 > 0.7 才算穩健），以及 DAX 案例的完整 end-to-end 開發流程。與 Davey 形成 US 與 EU 雙視角對照。

### 核心本質 (3-5 條)
1. **Robustness Ratio = 樣本外/樣本內績效比**（本質） — 第 5 章的關鍵指標：RR = out-of-sample Sharpe / in-sample Sharpe；RR > 0.7 穩健、0.4-0.7 可疑、< 0.4 過擬合。多數 retail 策略 RR < 0.3 但看不到這個指標，誤以為 in-sample Sharpe 高就是好策略。
2. **Monkey Problem**（本質） — 第 4 章形象比喻：如果讓 1,000 隻猴子隨機生成策略，必定有幾隻在歷史上 Sharpe > 3（純運氣）。你的策略可能就是那隻幸運猴子——in-sample 看起來天才，out-of-sample 歸零。防範靠 Bonferroni 修正 + out-of-sample 測試，沒有捷徑。
3. **parameter sensitivity 比最優參數更重要**（本質） — 第 4 章：選參數應看「績效 vs 參數」圖的形狀而非單點最高。**平坦高原 > 尖峰**——即使最高點低 10%，平坦高原意味著真實環境下仍有穩定邊緣。尖峰 = curve fit artifact。
4. **overnight / financing cost 往往被低估**（本質） — 第 6 章：對持隔夜部位的策略，borrow cost（做空成本）、overnight swap（FX）、futures roll cost 每年可吃 2-5% 淨值。多數 retail 回測只算手續費，忽略這些，導致實盤比回測差 30-50%。
5. **組合多系統比單系統的 Sharpe 提升有限制**（本質） — 第 7 章：理論上 N 個獨立系統組合 Sharpe 提升 √N，但實際 correlation ~0.3 時只提升 1.5-2×；且超過 5-7 個系統後 marginal gain 極小（correlation 難以進一步降低）。專注 3-5 個真正 uncorrelated 系統優於 20 個 marginally correlated 系統。

### 可用戰術/策略
- **Robustness Ratio 門檻**：任何策略上線前必須通過 RR > 0.7 檢驗；用 50/50 in-sample/out-of-sample 分割，分別計算 Sharpe；不達標則回到開發階段而非 paper trade。
- **Parameter plateau 選擇法**：對每個參數組合計算「鄰居 ±10% 範圍內的平均績效」；選「鄰居平均」最高的組合而非單點最高，自動避免尖峰過擬合。
- **Full-cost 回測模板**：手續費 + bid-ask × 0.7（平均執行在 mid-spread） + slippage (1 tick 固定) + overnight cost (per day holding) + financing (for leveraged positions)。
- **4-system portfolio 規則**：選擇 4 個策略，每個針對不同 regime（trend-up、trend-down、range、high-vol）；任意 pair correlation < 0.3；等權分配後實測 Sharpe 提升應 > 30%。
- **DAX 長期 trend system**（第 11 章示範）：20-day breakout + 55-day confirmation + 2 ATR trailing stop，1990-2008 回測年化 18%、Sharpe 0.8、max DD 25%；可作為歐洲股指 baseline。

### 盲點 / 反例 / 適用邊界
- **案例過度聚焦 DAX 期貨** — 第 11 章深入 DAX 但其他市場/資產類別的 generalization 需自行驗證。
- **2009 年成書，未涵蓋 QE 時代影響** — 2010-2015 央行 QE 扭曲了許多 trend system，書中回測期未包含此 regime。
- **ML 完全缺席** — 書以 rule-based systems 為主，對 ML-augmented system (Chan 2017, Lopez de Prado 2018) 無提及。
- **retail broker 實作細節簡** — 對 Interactive Brokers、FXCM 等具體 broker 的 API/slippage 特性未深入；需配合 Chan《Quantitative Trading》補充。
- **portfolio optimization 偏 Markowitz** — 第 8 章 Markowitz 優化在實務中對 input 參數極敏感；Robust Optimization、Black-Litterman 需更深入處理。

### 與 Edward 既有知識的連結
- **與 Davey《Building Winning Algo Systems》高度互補**：兩本都是獨立 algo trader 手冊，Davey 美式 + 期貨視角、Tomasini EU + 股指視角；合讀覆蓋更完整。
- **Robustness Ratio 直接搬入 B1 回測流程**：可加入 `ZP/quant/backtesting/rr_checker.py`，強制所有策略通過 RR > 0.7 才能進入 paper trade。
- **Parameter plateau 選擇法是反過擬合利器**：對應 Layer Zero「不追尖峰」精神；可實作為 optimization wrapper。
- **Full-cost 回測模板直接可用**：對 B1 所有策略標準化 cost 模型，避免回測樂觀偏差。
- **衝突點**：Tomasini 的 Markowitz portfolio optimization 對 input 敏感，與 Edward 零式「保守決策」有張力；建議用 risk-parity 或 equal-weight 作為 baseline，Markowitz 作為補強而非主力。
