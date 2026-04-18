# Option Volatility and Pricing (2ed 2015) — Sheldon Natenberg

### 目錄
1. 核心本質 — 選擇權交易是「買賣 volatility 的生意」而非方向性投注
2. 可用戰術 — Greeks、Spreads、Skew 交易、Volatility contract
3. 盲點/反例 — BSM 假設的 real world 偏差
4. 與 Edward 既有知識的連結

### TL;DR
Natenberg 2ed (McGraw-Hill 2015, 25 章 + 附錄) 是選擇權交易員的經典教材，1988 年首版被美國多家投行用做新人培訓讀物，2015 距首版 27 年後大幅翻新。25 章骨架：Ch 1-5 合約與理論定價模型 (BSM, binomial)、Ch 6 波動率基礎、Ch 7-9 Greeks (Delta/Gamma/Theta/Vega/Rho)、Ch 10-14 Spread 策略（Straddle/Strangle/Butterfly/Condor/Vertical/Synthetic）、Ch 15-17 套利與 hedging、Ch 18-19 BSM + Binomial 完整推導、Ch 20 Volatility Revisited（歷史/隱含/forward vol）、Ch 21 Position Analysis (market making 思維)、Ch 22 股指期權、Ch 23 Models and the Real World（BSM 七大假設的現實偏差）、Ch 24 Volatility Skews、Ch 25 Volatility Contracts（VIX, VXX, variance swap）。全書**核心論點**：選擇權交易的本質是 volatility 交易——方向性交易等於用股票就夠，選擇權的 edge 來自 realized vs. implied volatility 的差距。

### 核心本質
1. **選擇權的價值 = intrinsic + time value，time value 主導 deep OTM（Ch 3-4）**：Call 的 intrinsic = max(S-K, 0)，time value = option price - intrinsic。ATM 選擇權 time value 最大，deep ITM/OTM 最小。這決定 Gamma 與 Vega 的「集中在 ATM」。Delta-neutral 的 straddle 在 ATM 同時最大化 Gamma 暴露（賭大 move）與 Theta 消耗（每天繳時間費）。
2. **Gamma vs. Theta 是硬 trade-off（Ch 7, Ch 19）**：long option 永遠是 long Gamma + short Theta；short option 反之。沒有「又 long Gamma 又 long Theta」的 position。這個守恆律決定策略選擇：預期大波動 → long straddle（贏 Gamma 輸 Theta）；預期平穩 → short strangle（贏 Theta 輸 Gamma）。Gamma rent 概念（Ch 19）——「每天交多少時間租金換 Gamma 暴露」=implied vol² / 2。
3. **Implied Volatility ≠ Historical Volatility，差距 = Volatility Risk Premium（Ch 20）**：實證上 S&P 500 1-month ATM IV 長期高於 realized vol 約 3-4 vol points（2% 絕對差），此為 volatility risk premium——做 short vol 策略的「carry」。但這個 premium 在 volatility spike 事件（2008, 2020 Mar）會反噬——短一週虧掉過去兩年的 carry。
4. **Volatility Skew 是 BSM 的最大破綻（Ch 24）**：BSM 假設 IV 恆定，但實際 S&P 500 的 25-delta put 比 25-delta call IV 高 5-10 vol points（skew），OTM put/call 又比 ATM IV 高（smile + smirk）。原因：(a) crash risk premium (負尾事件機率被高估)、(b) supply/demand imbalance（避險 buyer 永遠多）、(c) leverage effect（股價跌波動率升）。Natenberg 介紹 sticky strike、sticky delta、sticky moneyness 三種 skew 動態假設。
5. **Models Assume Away Reality（Ch 23）**：BSM 的 7 個假設都在現實中違反——(1) frictionless（有 bid-ask + commission）、(2) constant r（利率波動 100+ bps/year）、(3) constant σ（skew + term structure）、(4) continuous trading（漲停板、熔斷）、(5) vol ⊥ price（明顯負相關）、(6) lognormal at expiry（skew + kurtosis）、(7) 無配息（ex-div 跳空）。每個假設違反都產生 pricing error 與潛在 edge。

### 可用戰術
1. **Calendar Spread 賺 vol term structure（Ch 11）**：buy long-dated ATM + sell short-dated ATM of same strike。若 short-dated 快到期且 realized < implied，short leg 賺 Theta；long leg 保留 Vega 暴露。2020 年 3-6 月 term structure 倒掛（short-dated vol >> long-dated）時 calendar spread 大賺。
2. **Risk Reversal（Ch 14 Synthetic）**：buy 25d call + sell 25d put 無成本（skew flat 時）或正 delta 收 premium（skew steep 時）。FX vanna-volga pricing 標準工具；equity 做 long-equity-tilt 的低成本 bet。
3. **Gamma Scalping（Ch 21）**：delta-hedged long-Gamma 倉位每次 underlying move 都要重新 hedge，賺「high-low range × Gamma」，但每天繳 Theta。實戰經驗：realized vol > implied vol 時賺錢；realized < implied 時虧錢。Market making 業務的骨幹 P&L。
4. **VIX Futures Term Structure Trade（Ch 25）**：VIX futures 通常 contango（遠期 > near），roll yield 為負；short VIX futures 長期賺 carry 但承受 spike 風險。2018 "Volmageddon" XIV 單日 -90% 清算。
5. **Butterfly 精準 view 特定價格（Ch 11 eq 11.2）**：long 1 low-K call + short 2 mid-K call + long 1 high-K call = 三角形 payoff，最大 payoff at mid-K。max risk = net debit；max profit = wing width - debit。適合 earnings event 後對 stuck at K 的 view。

### 盲點/反例
1. **2015 年出版，沒涵蓋 0DTE 與 retail option boom**：2020+ 起 0DTE (zero-day-to-expiry) options 爆炸成長（Jan 2024 佔 S&P 500 option volume 50%+），對 intraday gamma dynamics、market maker 避險行為產生新影響，Natenberg 完全未涵蓋。補 Nassim Taleb《Dynamic Hedging》或 Euan Sinclair《Volatility Trading》。
2. **Exotic options 輕描淡寫**：barrier options、Asian options、lookback、basket 等 OTC exotics 只在 Ch 14 提一下 synthetic 結構。做 structured products 或 variance swap replication 要補 Wilmott 系列或 Derman《Volatility Smile》。
3. **Quantitative vol modeling 缺席**：Heston stochastic vol model、SABR、local vol (Dupire)、Bergomi variance curve model 全書沒觸及。Natenberg 的取向是「trader 直覺與經驗」而非數學建模，對 PhD quant 不夠。
4. **Risk management 過於簡化**：Ch 21 的「market making」章節只談 delta hedge 與 position limit，沒談 VaR、stress test、correlated book risk、wing pricing policy。現代 OTC option market maker 都用 Monte Carlo scenario analysis。
5. **美國市場中心視角**：幾乎所有例子都是 S&P 500、OEX、US equity options。亞洲市場（Nikkei、Hang Seng、Kospi）的 skew 動態與美國不同（例 Kospi 200 index 的 skew 偏向 call side）——台指選擇權的 volatility surface 也有自己的特性，Natenberg 沒觸及。

### 與 Edward 既有知識的連結
- **對照 Higham《Financial Option Valuation》（Round 1）**：Higham 是數學家寫的 BSM 嚴格推導，Natenberg 是交易員寫的直覺 + 實務。讀 Higham 懂「why BSM works」，讀 Natenberg 懂「how to trade options」。互補不重疊。
- **對照 Bennett《Trading Volatility》（JPM, Round 1）**：Bennett 是 JPM sell-side 的 institutional vol 交易教材（含 variance swap, forward starting, skew arbitrage）；Natenberg 是 retail/prop firm 視角。Bennett 技術更深，Natenberg 直覺更廣。
- **對照 Augen《Option Trader's Handbook》（Round 1）**：Augen 專注 earnings event、expiration 交易，Natenberg 是 general framework。Augen 是 Natenberg 的 specialization。
- **對照 Velez Option Trading Tactics（Round 1）**：Velez 偏零售 directional + technical，Natenberg 偏 volatility-neutral 策略。兩本代表 option trader 的兩個 school——directional 與 quantitative。
- **對照 ZP/strategies/options 架構**：若 ZP 未來加台指選擇權策略，Natenberg Ch 21 Position Analysis 的 market maker 思維直接可用——先把手上倉位的 Delta/Gamma/Vega/Theta 全部算清，再想「接下來報什麼價單能讓總風險可控」。比單純方向性買權+賣權要專業得多。
- **對照 Poker 的 equity calculation**：撲克的 pot odds = option 的 implied vol——pot odds 告訴你「對手出多少錢你才該跟」，implied vol 告訴你「股價要動多少你才能回本」。兩個都是 breakeven probability 的市場價格表達。
