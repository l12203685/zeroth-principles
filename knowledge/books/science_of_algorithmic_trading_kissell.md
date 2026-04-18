# The Science of Algorithmic Trading and Portfolio Management — Robert Kissell

### 目錄
1. 核心本質 — 執行與組合構建的統一框架
2. 可用戰術 — TCA / VWAP / Implementation Shortfall / I-Star 模型
3. 盲點/反例 — HFT arms race 對 buy-side algo 的衝擊
4. 與 Edward 既有知識的連結

### TL;DR
Kissell (Academic Press/Elsevier 2014, 13 章) 是前 J.P.Morgan Morgan Stanley 量化 execution research 主管寫的 buy-side algorithmic trading 教科書，三部結構：Part I 電子市場環境（algo 類型、microstructure、TCA）、Part II 數學模型（市場衝擊校準、 volatility/factor model、流動性預測）、Part III 組合管理（納入 TCA 的優化、MI factor score、multi-asset、HFT）。Ch 13 由 Ayub Hanif (UCL) 撰寫 HFT + black box models，是本書最獨立章節。**核心立場**：execution is alpha——對大型 institutional order，執行成本可達 50+ bps，與 alpha signal 同階；忽略 TCA 的 portfolio optimizer 會系統性 under-perform。Kissell 的招牌模型是 **I-Star market impact model**——單一參數 I\* 描述 block trade 的平均 impact，由 volume、volatility、order size 三個 input 決定 impact bps。

### 核心本質
1. **Implementation Shortfall = Paper Portfolio - Actual Portfolio（Ch 2-3）**：Perold (1988) 定義的執行成本衡量——paper portfolio 假設所有 order 在決策時刻以 mid-price 成交，actual portfolio 反映實際成交價格 + 機會成本（來不及成交的部分）。IS 分解為：(a) delay cost（決策到下單的 price drift）、(b) market impact cost（下單到成交的價格位移）、(c) opportunity cost（未成交 portion 的 alpha loss）、(d) commission & fees。這個框架統一了買賣雙方對 broker 的績效衡量。
2. **I-Star Model（Ch 5）**：Kissell 招牌公式 impact (bps) = a1·(Q/ADV)^a2·σ^a3，其中 Q/ADV 是 order size relative to average daily volume、σ 是 daily vol、a1/a2/a3 是校準參數（典型 a2 ≈ 0.5-0.6，即衝擊與 size 的 sqrt 關係）。這是 Almgren-Chriss (2000) 與 Bertsimas-Lo (1998) 之後的實務版本——用 S&P 500 的數億筆歷史 order 校準得到穩健係數。實務應用：order size >5% ADV 時 impact >30bps，已等於典型 monthly alpha，必須分拆 execution。
3. **Algo Taxonomy：Arrival Price / VWAP / TWAP / IS（Ch 2-3）**：(a) Arrival Price：minimize 相對 arrival 時刻 mid-price 的 slippage；(b) VWAP：follow 成交量 profile，減少 signaling；(c) TWAP：等時間切分；(d) Implementation Shortfall：dynamic between passive 與 aggressive，根據 price drift 實時調整 urgency。IS 在理論上最優但對 adverse selection 最脆弱——若 price 快速偏離則自動加速執行，被 HFT 利用。
4. **Market Impact 的 Square-Root Law（Ch 6）**：經驗上 permanent impact ≈ σ·√(Q/V)，其中 V 是 trading volume。這個 sqrt 定律（Gatheral 2010; Tóth et al. 2011）有深刻 propagator 理論根基——limit order book 的 supply curve 是 concave 而非 linear。實務上 size 翻倍，impact 只增加 41% 而非 100%。
5. **Factor Exposure Investing（Ch 11-12）**：不同於 Qian-Hua-Sorensen 的 single-stock factor model，Kissell 主張直接 trade 「factor-mimicking portfolio」——把每個 factor（value/momentum/quality）包成可交易的 basket，portfolio manager 直接 over/under weight basket。這套 methodology 跟 BlackRock iShares 的 smart beta ETF 推廣有關。

### 可用戰術
1. **Pre-Trade TCA 評估 order feasibility（Ch 4）**：下單前跑 I-Star 預估 impact + schedule impact curve。如果 impact + schedule >150 bps 直接放棄或改 split over multiple days。這是 institutional buy-side 標準 pre-trade check。
2. **Dark Pool Routing 避免 Info Leakage（Ch 3）**：大 order 先去 dark pool（IEX、UBS ATS）測試 liquidity，有 fill 就成交，沒 fill 再去 lit market。Kissell 強調 dark pool 有 gaming risk（HFT 的 pinging），需監測 fill rate 與 reversion rate（fill 後 mid 立即 adverse 移動 = pinger）。
3. **Participation Rate Optimization（Ch 3）**：每個 5-min interval 參與市場成交量的 % vs. time 是 trade schedule 的核心 knob。10% POV 是常見起點；urgent 時拉到 25%，patient 時降到 5%。POV algo 的好處是 adaptive——若市場突然成交量大增，絕對量自動等比例放大。
4. **Multi-Asset Trading Cost Index（Ch 12）**：Kissell 提出跨資產類別的 Cost Index——把 equity、futures、FX、fixed income、commodities 的 execution cost 整合。對 global macro fund 或 multi-asset strategy 極有用，可判斷 rebalance 時哪個資產 class 最貴、調整 rebalance 頻率。
5. **MI Factor Score 納入 alpha model（Ch 11）**：把 expected market impact 直接當作負的 alpha factor——high impact stock 的 signal 需要更強才值得 trade。這把 TCA 從 ex-post 事後分析提升為 ex-ante 決策變數。

### 盲點/反例
1. **Buy-side 視角，缺 sell-side（market maker）互動**：書中以 institution 為主，沒深入討論 HFT market maker 的報價策略、internalizer 的交易決策。要完整理解市場 dynamics 需配合 O'Hara《Market Microstructure Theory》或 Cartea-Jaimungal《Algorithmic and High-Frequency Trading》。
2. **2014 年出版，SIP 與 speed race 的 2015+ 變化未涵蓋**：2016 IEX speed bump approval、2018 MiFID II 改變 broker landscape、2021 零佣金時代的 retail order flow internalization 都在 Kissell 之後。補 Michael Lewis《Flash Boys》與 Aldridge 後續作品。
3. **Crypto 與 24/7 market 完全缺席**：Kissell 2014 時代 Bitcoin 仍是 fringe；現在 crypto market 成為 algo trading 主戰場之一，liquidity pattern 與 traditional equity 完全不同——跨所價差 + 無熔斷 + funding rate 市場影響力變化多端。
4. **Linear TCA 模型低估 tail risk**：I-Star model 對中等 size trade 準確，但對 >20% ADV 的 block trade 常低估 impact。實務上 10% ADV 以上 trade 要加入 stress scenario（volatility 翻倍、half-day 事件）。
5. **Machine Learning for TCA 未融入**：LightGBM / neural net 預測 market impact 在 2019+ 已成為主流（Citadel、Two Sigma 內部模型）。Kissell 停在 linear regression + OLS calibration。

### 與 Edward 既有知識的連結
- **對照 Aldridge《High-Frequency Trading》（Round 1）**：Aldridge 是 sell-side/market-maker 視角（HFT 做 market making 與 arb），Kissell 是 buy-side institutional 視角（minimize execution cost）。兩本互補——一個教 how to make money by trading fast，一個教 how to lose less money when trading slowly.
- **對照 Qian-Hua-Sorensen 《Quantitative Equity Portfolio Management》（本輪）**：Qian 的 turnover optimization 假設 linear TC，Kissell 的 I-Star 提供 sqrt-law 修正——兩書 together 形成「alpha model (Qian) + TCA (Kissell)」的完整 portfolio workflow。
- **對照 Lien《Day Trading FX》（Round 1）**：Lien 是 retail 視角，Kissell 是 institutional；但 POV、dark pool、reversion rate 等概念 retail 操作 smaller size 時也能借鏡——例如觀察 Asia FX 市場 liquidity pocket 避開 Tokyo fix。
- **對照 ZP/execution 框架**：我若要系統化 ZP 的執行品質，Kissell Ch 2 的 IS decomposition 是必建 metric。目前我只記 TRADE_PRICE vs DECISION_PRICE slippage，沒切分 delay cost vs. impact cost vs. opportunity cost——這個三分法能精確定位是「決策慢」還是「下單大」造成 cost。
- **對照 Poker 的 sizing**：sqrt-law of market impact 類比撲克的「bet sizing diminishing return」——bet pot vs. half-pot 的 fold equity 差不多，但 bet 2x-pot 不會比 pot 多賺 2x equity。兩者都是 convex-concave interaction 的 optimal operating point 問題。
