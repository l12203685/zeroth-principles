## Machine Trading: Deploying Computer Algorithms to Conquer the Markets — Ernest P. Chan (2017)

**來源**: E:/書籍/Ernest P. Chan/Machine Trading Deploying Computer Algorithms to Conquer the Markets, 2017, Ernest P. Chan.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 機器學習的基本模型（線性/邏輯回歸、SVM、隨機森林、RNN 在金融的適用性）
- 第 2 章 動能與均值回歸的 ML 升級（特徵工程、目標變數設計）
- 第 3 章 時間序列模型（ARMA-GARCH、Kalman Filter、Hidden Markov 體制切換）
- 第 4 章 因子模型與另類資料（新聞情緒、社群、衛星影像、信用卡流）
- 第 5 章 期權策略（vol arb、skew arb、gamma scalping 的演算化）
- 第 6 章 加密貨幣交易（BTC/ETH 的 microstructure、交易所套利）
- 第 7 章 交易基礎設施（co-location、FIX vs REST、GPU 在回測的用途）
- 第 8 章 風險管理新觀念（drawdown prediction、tail risk premium）

### TL;DR (≤120字)
Chan 的第三本書標誌著他從 rule-based 轉向 rule + ML 混合的立場轉變。**核心訊息是 ML 在金融的成功 = 80% 特徵工程 + 20% 模型**；SVM 與 RF 優於深度學習（樣本數不足）。首次納入 options 與 crypto 兩個 retail 新藍海，是 2017 年最實戰的 quant 藍圖。

### 核心本質 (3-5 條)
1. **ML 在金融的真正價值是「自動特徵組合」而非「自動預測」**（本質） — 第 1 章明確：單一特徵的預測力在金融多為 IC < 0.05（correlation），ML 的價值是在 50-100 個弱特徵中找出穩定組合（ensembles），而非發現單一聖杯特徵。這重構了「ML = 黑箱預測」的誤解，把 ML 定位為 feature selection 工具。
2. **Hidden Markov Model 是 regime detection 的正確工具**（本質） — 第 3 章主張：市場不是 stationary，而是在 2-3 個 regime 間跳躍（bull/bear/choppy）。HMM 學出 transition matrix 後可即時判斷當前 regime 並切換策略，比 static 模型穩健 2-3 倍。Chan 實測 SPX 日線資料顯示 HMM 能準確辨識 2008/2011/2015 三次 regime shift 的前 2-5 天。
3. **另類資料的 alpha 半衰期 = 3-12 個月**（本質） — 第 4 章警示：2014-2016 年衛星影像（停車場車數預測零售業績）曾有 Sharpe 2+，但隨 SpaceKnow 等商業化，2017 後邊緣消失。任何 alt-data 策略都該預設 1 年壽命，而非永續。
4. **options gamma scalping = retail 當前 alpha 密度最高的區域**（本質） — 第 5 章：做空 short-dated ATM options 並動態 delta hedge，賺 theta 但受 gamma 反咬。關鍵在於**波動率預測誤差**——若預測波動率比實際隱含高 1%，長期年化 alpha 約 15%。需要自動化 delta hedge 架構（每 10 分鐘 rebalance）。
5. **crypto 的微觀結構類似 2005 年的 US equity**（本質） — 第 6 章：2017 年 BTC/ETH 在主流交易所間的 arb 機會仍達 50-200 bps（vs 股票 1-5 bps），原因是 (a) 交易所間缺乏 SIP、(b) 單一交易所深度低、(c) 大量散戶非理性下單。這是 retail 最後的 pure arb 藍海。

### 可用戰術/策略
- **HMM regime switching 策略**：用 2 個 state 的 HMM 擬合 SPX 20 日波動率，預測 state 0 (低 vol, trending) vs state 1 (高 vol, mean-reverting)；state 0 用動量、state 1 用均值回歸，第 3 章給出 MATLAB 代碼。
- **Random Forest 特徵組合**：輸入 50 個技術 + 基本面特徵（RSI/MACD/PE/earnings revision 等），目標為次日 excess return 的 sign；使用 OOB score 做穩健度檢查，只採 top-10 特徵的 voting。
- **crypto 跨交易所 arb**：監控 Binance/Coinbase/Kraken 的 BTC/USDT 價差，價差 > 30 bps 同時做多低價、空高價，等價差收斂至 < 10 bps 平倉；要處理提幣延遲與手續費。
- **gamma scalping 框架**：賣出 5-delta put + 5-delta call，每日 delta hedge 至 0，月頻滾倉；vol premium 約 2-5% 年化；需監控 VIX term structure backwardation 作為風險訊號。
- **情緒因子 (News sentiment)**：用 Thomson Reuters MarketPsych 或自建 BERT-finance model 處理新聞流，構建 sentiment score；與 momentum 結合（sentiment + price momentum 同向才進場）Sharpe 比純 momentum 高 30-50%。

### 盲點 / 反例 / 適用邊界
- **ML 過擬合警告不夠嚴厲** — 儘管 Chan 警告過擬合，但書中多個 RF 案例的 Sharpe 仍可能被 data snooping 污染；讀者應用 walk-forward + deflated Sharpe 再驗證。
- **crypto 章節過時** — 2017 後 crypto 市場結構巨變（2020 DeFi、2022 LUNA/FTX、2024 spot ETF），書中的交易所套利機會在 2020 已被 HFT 擠壓至 < 10 bps。
- **另類資料成本** — MarketPsych、衛星影像等資料源對 retail 價格在 10k-100k USD/年，書中建議但未充分處理成本效益對 retail 的不可行性。
- **期權執行假設** — gamma scalping 需要連續 delta hedge，retail broker 的 options 下單延遲 (IB ~200ms) + 手續費 ($0.65/contract) 可能吃掉 1/3 alpha；Chan 未詳述此。
- **生存者偏差在案例選取** — 書中呈現的 ML 策略是 Chan 的 QTS Capital 選來展示的成功案例；未成功的策略通常不會被寫入，讀者不知真實命中率。

### 與 Edward 既有知識的連結
- **對齊 Round 1 Financial Machine Learning**：Kelly-Xiu 是學術嚴謹版，Chan 是實戰工程版；Kelly 給理論基礎，Chan 給 step-by-step 實作；建議先讀 Chan 啟發後再回 Kelly 深化。
- **補強 B1 crypto 觸及**：第 6 章 crypto arb 可作為 B1 經濟自給第二條腿（主腿為股票/期權系統），低資本需求 + 高頻機會適合 Edward 個人規模。
- **Gamma scalping 是 B2 options 研究的起點**：第 5 章框架可直接搬入 ZP/options/ 作為第一個完整 vol trading 策略原型；需求的 delta hedge 自動化與 `staging/` 的 async 任務管理可重用。
- **HMM 與 Kaufman KAMA 的對照**：兩者都是 regime detection，KAMA 是確定性（效率比），HMM 是機率性（隱狀態）。組合起來可做 meta-signal（兩者同向才信號強）。
- **衝突點**：Chan 的 ML 擁抱與 Round 1 Tsay 的傳統時間序列有張力；實務建議以 ARMA-GARCH 為 baseline，HMM + RF 為補充層，避免過度依賴 ML。
