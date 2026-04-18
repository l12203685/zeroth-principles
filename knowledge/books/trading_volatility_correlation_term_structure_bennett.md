# Trading Volatility, Correlation, Term Structure and Skew — Colin Bennett (Santander 2012)

### 目錄
1. 核心本質 — 波動率、相關性、期限結構、偏斜是 vol 交易的四大維度
2. 可用戰術 — 變異數 swap、correlation swap、forward starting、skew trade
3. 盲點/反例 — 2020+ 低利率環境對 vol 交易的衝擊
4. 與 Edward 既有知識的連結

### TL;DR
Bennett-Gil (Santander Equity Derivatives 2012, 六章 + 附錄，約 300 頁) 是歐洲 sell-side 研究典範的 vol 交易手冊——相較 Round 1 讀的 Bennett JPM 版 (2015)，這版是他早期在 Santander 的系統化整理。結構：(1) Directional Volatility（用選擇權做方向性 + 收 premium 策略）、(2) Volatility & Correlation Trading（var swap, gamma swap, correlation trade, dividend vol）、(3) Opportunities, Imbalances & Myths（為何 vol 看似貴、為何 long vol 不是好 hedge）、(4) Forward Starting Products & Light Exotics（barrier, worst-of, outperformance, look-back, contingent premium, composite/quanto）、(5) Advanced Volatility Trading（相對價值、earnings 交易、stretch BSM 假設）、(6) Skew & Term Structure Trading（skew 與 term structure 的連結、如何測量、skew trade 實戰）、附錄則有 local vol、variance swap 複製、BSM 推導、Greek 與實務 shadow Greek。Bennett **核心立場**：vol is an asset class——與 equity、bond、commodity 同級，有自己的 carry, term structure, skew, correlation 結構，需要專門 framework 來交易。

### 核心本質
1. **Variance 而非 Volatility 才是「可複製的」（Ch 2, p.47-49）**：標準差（volatility）無法用有限組合 static replicate，但變異數（variance）可以——付 log contract 的 payoff = -2·ln(S_T/S_0) 就能得到 realized variance。這個數學事實是 variance swap 存在的基礎，也解釋為何 VIX 公式是 variance weighted strip 而非 vol weighted。
2. **Correlation 是 index vol 與 single stock vol 的「缺口」（p.66）**：index variance = Σw_i²σ_i² + 2Σw_iw_jρ_{ij}σ_iσ_j。若 average correlation = ρ̄，則 index σ² ≈ ρ̄·(Σw_iσ_i)² + (1-ρ̄)·Σw_i²σ_i²。market-wide fear 提升 ρ̄ 讓 index vol 放大，但 single stock vol 不變——這正是 correlation swap / dispersion trade 的理論基礎（long single stock vol + short index vol）。
3. **Skew 與 Term Structure 的 Square-Root-of-Time 連結（Ch 6, p.144）**：Bennett 指出 skew steepness 隨到期時間 t 以 1/√t 衰減。意義：要比較不同到期時間的 skew 必須先 normalize by √t——2 月份 25d put-call vol diff = 3%，6 月份 diff = 2%，看似平坦但 normalize 後 2 月 steeper。同理 term structure 的 slope 也隨 moneyness 距離以 √t 縮放。
4. **Variable Annuity Hedging 扭曲 long-dated vol（Ch 3, p.89）**：保險公司賣 VA (variable annuity) 產品含 guaranteed minimum benefit，對 long-dated equity put 有系統性買方需求。2008-2010 這批 liability re-hedge 推高 S&P 500 2-3 year ATM vol 至 25-30%。意義：long-end vol 有「結構性買方」，short long-dated vol 看似 cheap 實為永久 carry positive。
5. **Dividend Volatility 是被忽略的獨立維度（Ch 2, p.80）**：歐洲股票有 active dividend future market（Euro Stoxx 50 dividend futures 流動）。Implied dividend 本身有 volatility，且與 equity vol 獨立——2020 Mar 歐洲 dividend futures 跌 -50%（擔心禁發）而 SX5E vol +100%，兩者 decoupled。Dividend swap 提供純 cash flow 暴露，與 equity price 無關。

### 可用戰術
1. **Call Overwriting 收 Premium（Ch 1, p.20-25）**：long stock + sell covered call = synthetic short put。Bennett 實證：EuroStoxx 50 的 covered call 指數在 2000-2011 比 benchmark 高 2%/year，Sharpe +0.3——volatility risk premium 長期正，但要承受 upside cap。
2. **Variance Swap 複製 via Log Contract（Appendix, p.184）**：realized variance = 2·∫(K*)strike * put(K) dK + 2·∫(>K*) call(K) dK，用 infinite OTM options strip 完全複製。實務用 25d, 50d, 75d 三個 strike 近似，已能達到 95%+ replication。
3. **Dispersion Trade: Long Single Vol, Short Index Vol（Ch 2, p.66-75）**：long single stock variance + short index variance = long correlation. 若 correlation 回落（sector 分化），賺單一股票 realized vol 更高於 index。2017 年 low-correlation 環境 dispersion trade 賺 15%+。
4. **Forward Starting Swap（Ch 4, p.96）**：以 1-year-forward 1-year variance swap 鎖定「明年」的 vol。用 Y1 variance - Y0 variance 可分解出 calendar spread。市場隱含 vol term structure 時的套利工具。
5. **Skew Trade via Risk Reversal（Ch 6, p.154）**：sell 25d put + buy 25d call = positive-carry（正 skew 下）+ delta positive。若 skew 歷史均值 5 vol points 而當前 3 vol points，可做「bet skew widening」——賣 -50d put + 買 -25d put。

### 盲點/反例
1. **2012 年出版，缺 QE + 零利率環境的新動態**：2010s 的 low-rate regime 讓 structural vol seller（volatility-target ETF、risk parity fund）扭曲 vol market——2018 Volmageddon 與 2020 3 月 dislocation 顯示 vol market 有流動性陷阱。補 Artemis Capital 研究與 Euan Sinclair《Positional Option Trading》。
2. **Exotic 章節涵蓋較淺**：Barrier、look-back、outperformance options 各一頁介紹，缺 PDE 定價與 hedging 細節。做 structured products 定價要補 Haug《Option Pricing Formulas》或 Wilmott PDE 書。
3. **Statistical vol models 缺席**：GARCH、SV model、HAR-RV 等 realized vol 預測模型全書未觸及。Bennett 的取向是「market-implied」而非「statistical forecast」；做 long vol 方向性交易需要兩個視角。
4. **Asia vol market 沒覆蓋**：Hang Seng、Nikkei、Kospi 的 skew dynamics 與歐美不同（Kospi 200 的 reverse skew），但書全是 EuroStoxx / S&P 500 / FTSE 例子。台指選擇權策略需自行調整。
5. **0DTE 與 short-dated vol 大潮未涵蓋**：2020+ 起 SPX weekly / 0DTE options 改變整個 market maker 避險動態，Bennett 這本（2012）完全沒預測到這個趨勢。

### 與 Edward 既有知識的連結
- **對照 Bennett《Trading Volatility》（JPM, Round 1）**：這本（Santander 2012）是 Bennett 的早期作品，JPM 版（2015）是擴充版。核心 idea 一致但 Santander 版更精煉、JPM 版更深入 SABR 等模型校準。ZP 讀兩本會有大量重複，但 Bennett JPM 版附錄比這版更全。
- **對照 Natenberg《Option Volatility & Pricing》（本輪）**：Natenberg 是 retail/prop firm 視角（偏 directional + spread），Bennett 是 sell-side institutional 視角（偏 derivatives structure + exotics）。Natenberg 教基本，Bennett 教高階。
- **對照 Sundaresan《Fixed Income》（Round 1）**：Ch 4 Forward Starting 的思路與利率 Forward Rate Agreement 完全同構——vol 的 term structure = 利率的 yield curve。Bennett 附錄的 local vol 與 Dupire 公式也與 HJM 框架對應。
- **對照 Engle SRISK（Round 1）**：systemic risk event 時 correlation 飆升，dispersion trade 會 take max loss。Bennett Ch 2 p.66 的 correlation swap mechanics 直接對應 SRISK 的 conditional correlation 估計——兩個在不同術語描述同一 phenomenon。
- **對照 ZP/strategies/vol 架構**：Bennett Ch 2 「variance is the key, not volatility」是重要提醒——我 ZP 的 vol strategy 若要專業化，應該先把所有 signal/position 轉成 variance unit 而非 vol unit，否則 convexity 誤算會產生隱性 P&L。
- **對照 Poker 的 tournament structure**：var swap 的 convexity（payoff quadratic in vol move）類比撲克 tournament 的 ICM non-linearity——每一手贏的邊際價值隨 stack 升高遞減。兩個都是 non-linear payoff 產生 optimal strategy 的不對稱性。
