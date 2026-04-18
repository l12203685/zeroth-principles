## Time-series and Cross-sectional Momentum Strategies under Alternative Implementation Strategies — Ron Bird, Xiaojun Gao, Danny Yeung
**來源**: Paul Woolley Centre, UTS — 學術論文 35 pages  |  **消化日**: 2026-04-18  |  **模型**: sonnet

### 目錄
- **Introduction: time-series vs cross-sectional momentum**
- **Literature review: Jegadeesh-Titman 1993 vs Moskowitz et al. 2012**
- **Data & methodology across 24 markets**
- **Implementation variants: lookback, holding period, portfolio construction**
- **Results: TS momentum dominates CS under most implementations**
- **Robustness: market regimes (bull/bear/volatility)**

### TL;DR
學術比較 24 市場內 TS 動量 (Moskowitz et al. 2012) vs CS 動量 (Jegadeesh-Titman 1993)。在大多數實作設定下兩者皆盈利,但 TS momentum 明顯勝出。差異源於 TS 會依市場狀態動態調整 winner/loser 池子數量,而 CS 永遠等量抽取。

### 核心本質
1. **Momentum 是「尾部資訊」現象** — 動量訊號的 edge 集中在報酬分佈的兩端尾部(強贏家、強輸家),不是分佈中央;TS 動量用絕對績效門檻天然抓尾部,CS 動量用相對排名在弱市場會挖到中段,稀釋 edge。
2. **TS 動量的市況適應性是結構優勢** — 弱市時 TS 動量自動持有較少 long、較多 short(甚至全 cash);CS 動量強制等量 long/short 排名頂尾 n% 個股。TS 框架讓曝露量與 edge 強度同步,CS 則不同步。
3. **跨 24 市場驗證 = 穩健不是偶然** — 股票、債券、匯率、商品全面支持 TS momentum 的穩健性,排除單一市場 data mining。Moskowitz et al. 2012 + Baltas-Kosowski 2013 + 本文構成三階段驗證鏈。
4. **匯率例外顯示 asset class heterogeneity** — Menkhoff et al. 2012 發現匯率市場 CS momentum 勝 TS,可能源於匯率的 carry-factor 與 momentum 耦合方式不同於其他資產類別;警示「普世法則」不存在,需 asset-by-asset 調校。
5. **實作細節決定半成敗** — lookback 長度 (3/6/12m)、volatility scaling、rebalance 頻率、交易成本設定都顯著影響最終績效;本文比較多種實作後,12m lookback + vol target + 月 rebalance 是 TS 動量的最佳 baseline。

### 可用戰術/策略
- **TS 動量基準策略**:對 24 個 liquid futures 各自計算 12m trailing return,若 > 0 做多、< 0 做空,vol target 10%,月 rebalance。
- **混合 TS+CS 動量**:對於大型股組合先用 TS 篩掉「市場多空」曝露,剩餘基礎上用 CS 篩前 20% 個股 — 利用兩者各自的 edge。
- **動態市場 regime 判斷**:用 aggregated TS momentum signal(全市場多寡比例)作為 regime filter,low-breadth 時期降部位,high-breadth 時期加部位。
- **匯率特殊處理**:對 FX 改用 CS momentum + carry factor 疊加,避免 TS momentum 在匯率上的結構性劣勢。

### 盲點 / 反例 / 適用邊界
- **忽略 2010s 動量衰減**:論文樣本期多在 1990-2010,但 2011-2019 主要市場動量報酬顯著下滑 (Asness et al. 2020 記錄),本文結論對 post-2010 適用性需打折。
- **交易成本假設可能過於寬鬆**:學術回測常用 10-20 bps 單邊成本,實際小型股動量策略遇到衝擊成本 + 做空成本後,淨報酬可能歸零。
- **leverage 風險未深究**:TS 動量配 vol target 時,低波動期會用 3-5x 槓桿,當波動率突然 regime shift 時(如 2015 Q3 CHF shock)可能遭遇 margin call 或強制平倉。
- **適用邊界**:深度流動 futures、中大型股;小型股、EM 商品 momentum 因流動性與 microstructure 問題不成立。

### 與 Edward 既有知識的連結
- 對齊 **population_exploit**:動量 anomaly 源於「散戶慢反應 + 機構 herd」的 population 錯誤定價,TS/CS 都是同一 edge 的不同收割工具;本文幫助理解收割效率差異。
- 呼應 **derivative_over_level**:momentum 本身就是「對報酬變化率的外推」= 第一公理 derivative_over_level 的具體實現。
- 補強 **backtest_methodology**:24 市場 × 多實作變體的 robustness 檢驗是回測方法論的教科書示範,應納入 ZP backtest_methodology.md 作為 cross-market validation 的 case study。
- 連結 **entry_diversity_exit_convergence**:TS 動量與 CS 動量在同一市場可同時運作(不同 lookback、不同實體池),entry 多元化;但 exit 訊號(動量翻轉)需 converge 避免重複曝險。
