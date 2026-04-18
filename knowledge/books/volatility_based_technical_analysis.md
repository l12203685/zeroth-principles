## Volatility-Based Technical Analysis: Strategies for Trading the Invisible — Kirk Northington
**來源**: E:/投資交易/交易學習資料庫/@交易/@選擇權/Volatility-Based Technical Analysis, Companion Web site Strategies for Trading the Invisible.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Part I: Are You Prepared?（trader 心理準備、市場認知、traditional TA 的不足）
- Part II: Seeing the Invisible（volatility-based indicators, ATR envelopes, volatility cycles, MIDAS, detrended oscillators）
- Part III: Trading the Invisible（實戰策略、entry/exit rules, stop placement, position sizing based on volatility）
- Appendix A: TradeStation Examples and EasyLanguage Code
- Appendix B: The PIV Options Advantage（Projected Implied Volatility for butterfly, condor, strangle, straddle）
- Appendix C: Companion Web Site

### TL;DR (≤120字)
Northington 對傳統技術分析的一大批評：MA、MACD、RSI 等 oscillator 在波動率劇變時失效，因為它們未納入當前波動率 context。他提出 "volatility-based technical analysis" (VBTA)——把 volatility 當 explicit input 重新設計指標，讓 signal 自動 adapt 到不同波動率 regime。PIV（projected implied volatility）是其標誌工具。

### 核心本質 (3-5 條)
1. **Traditional TA 的 volatility 盲點**（本質，Part I） — 20-day SMA 在 VIX 15 和 VIX 50 的市場行為完全不同；同樣 RSI 70 在低波動市場是極端超買、在高波動市場是正常波動。Northington 主張所有傳統指標都應 normalize 到當前 ATR / VIX / HV，否則 signal 含義漂移。
2. **ATR Envelope > Bollinger Bands**（本質，Part II） — Bollinger Bands 用 SD，假設 Normal 分布；ATR envelopes 用 True Range 的 mean，更穩健處理 gaps 與 fat tails。Northington 的 envelope 公式 = MA ± k × ATR（k 通常 2-3）。
3. **Volatility Cycles 是可預測的**（本質，Part II） — Volatility 本身呈現 clustering + mean-reverting 性質（GARCH 核心）；vol cycle 持續 2-6 個月，low vol 後接 high vol，反之亦然。Northington 用 HV(10) vs HV(50) ratio 判斷當前 vol regime。
4. **MIDAS Method**（本質，Part II） — Midas 是 Paul Levine 發展的 volume-weighted moving average 變體，考慮 volume × volatility 做 dynamic support/resistance。比傳統 trend line 更符合 order flow 邏輯。
5. **PIV (Projected Implied Volatility) for Options**（本質，Appendix B） — 用歷史 IV time series + volatility cycle 預測未來 IV；PIV > current IV → 買 vol（straddle、strangle）；PIV < current IV → 賣 vol（iron condor、butterfly）。這是 option directional strategy 向 vol-based strategy 的轉換工具。

### 可用戰術/策略
- **ATR-Based Stop**：停損 = entry ± 2 × ATR(20)；隨 volatility 自動調整，避免 low-vol 時 stop 太寬、high-vol 時 stop 太窄。
- **Volatility Regime Filter**：HV(10)/HV(50) > 1.5 = high vol regime，暫停 mean-reversion 策略、啟動 breakout 策略。反之則切換。
- **Position Size Inverse Volatility**：position size ∝ 1 / current ATR；當 ATR 翻倍，倉位減半；確保 dollar risk 穩定。
- **PIV Straddle Entry**：PIV > current IV 且 PIV 在上升階段 → 買同 strike straddle；策略 PnL 來自 IV 上升（vega 正）+ 實際波動放大（gamma 正）。
- **MIDAS Support/Resistance Trading**：價格觸碰 MIDAS curve → 反彈進場；若 price decisively break MIDAS + volume 同向 → trend continuation 進場。

### 盲點 / 反例 / 適用邊界
- **Volatility Regime Switching 不總是 clear-cut** — Northington 假設 HV ratio > 1.5 就切換策略；實際 regime change 是 gradual，閾值附近信號噪音大。
- **PIV 的預測力有限** — IV 本身難以預測（半 random-walk），歷史 cycle 在新事件（COVID、戰爭）下失效；PIV 僅在 normal regime 有邊緣。
- **TradeStation EasyLanguage 綁定** — Appendix A 用 EasyLanguage code，非 Python/R 用戶需 port；TradeStation 在 2010s 後市場份額下降，多數 retail 移到 Interactive Brokers + Python。
- **缺少 large-sample backtest** — 書中 example 多是 cherry-picked case study；VBTA 方法的 statistical edge 未經嚴格驗證。
- **Option pricing context 弱** — PIV 方法未結合 BSE / SABR 的嚴謹定價；單看 IV trajectory 可能忽略 skew / term structure 的動態。

### 與 Edward 既有知識的連結
- **對應 Bennett Trading Volatility**：Bennett 從 institutional sell-side 角度講 volatility，Northington 從 retail technical trader 角度；兩本互補。
- **對應 Augen Option Handbook**：Augen 教 defensive adjustment，Northington 教 entry based on vol regime；組合起來是更完整的 option trading 流程。
- **ZP 應用**：volatility regime filter 可加入 `ZP/trading/risk/regime_detection/`，作為所有策略的 meta-level switch——不同 regime 啟動不同 sub-strategy。
- **衝突 Kestner Quantitative**：Kestner 偏向 static rule + K-Ratio 評估；Northington 偏向 adaptive rule + vol context；Edward 應在 static backtest 後加入 vol regime detection 驗證策略在不同 regime 下穩定性。
- **可挖金礦**：ATR envelope 與 MIDAS curve 可編寫為 Python indicator，整合到 `ZP/indicators/volatility/`；比 Bollinger Bands 更穩健。
- **Crypto 應用**：crypto market 的 volatility regime 切換更極端（BTC 從 20% 年化 vol 可跳到 100%），VBTA 框架在此場景反而比傳統 TA 更有價值。
