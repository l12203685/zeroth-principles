# Volatility Information Trading in the Option Market — Ni, Pan, Poteshman (JoF 2008)

### 目錄
1. 核心本質 — 選擇權市場存在對 volatility 的私人資訊交易
2. 可用戰術 — Straddle volume signal 與 earnings-event timing
3. 盲點/反例 — 2008+ 後 option market 結構變化
4. 與 Edward 既有知識的連結

### TL;DR
Ni-Pan-Poteshman (Journal of Finance Vol LXIII No 3, June 2008，Kyle 1985 延伸) 用 CBOE 1990-2001 non-market-maker 每日 buy/sell volume 資料證明：**選擇權市場的 non-market-maker net demand for volatility 能預測未來 underlying stock 的 realized volatility**。作者群——Sophie Ni (HKUST)、Jun Pan (MIT Sloan, NBER)、Allen Poteshman (UIUC)——是 option microstructure 的權威群，這篇是 Back (1993) 延伸 Kyle 1985 到有選擇權的 informed trading 模型的第一個嚴謹實證驗證。核心實證結果：(1) volatility demand 預測 realized vol 延續至少一週、(2) 這個預測力在 earnings announcement 前 5 日最強（price impact +40%）、(3) open volume（新開倉）比 close volume（平倉）預測力強、(4) straddle volume 比 non-straddle volume 預測力強。意義：選擇權市場是 informed vol trader 的首選場所，因為 option 是 non-linear in vol——股票只能表達方向，選擇權才能 isolate vol bet。

### 核心本質
1. **Non-Market-Maker Net Demand for Volatility 是 actionable signal（Eq 1）**：作者構造 daily 指標 VOL_DEM = (buy-to-open call + buy-to-open put - sell-to-close call - sell-to-close put) weighted by Vega。如果 customer 大量 buy-to-open straddle，就是 long volatility 訊號。實證 VOL_DEM_t 對 realized_vol_{t+1 to t+5} 的回歸係數顯著正，t-stat > 5。
2. **Earnings Announcement 前資訊不對稱最強（Table 6）**：正常期 VOL_DEM 對 IV change 的 price impact 是 0.10；earnings 前 5 日跳到 0.14（+40%）；事件後 3 日回落至 0.08。這符合 Kyle (1985) 的 informed-trader driven price adjustment——informational asymmetry intensity ↑ → market maker 對 order flow 反應 ↑。
3. **Open Interest 比 Close 更 informative（Table 4）**：open-to-trade 的 order 承擔新部位風險，有內線的人才會做；close-to-exit 也可能是 lucky guesses 早期賣出。實證 open volume 的 R² 比 close volume 高 2x。
4. **Straddle 是純 volatility bet（Table 5）**：straddle = ATM call + ATM put 幾乎 delta-neutral，payoff 完全由 |ΔS| 決定。作者識別 straddle volume（同股同日 call 與 put 成交量比例接近 1:1）作為 「high purity vol signal」——這個 subset volume 對 future vol 的預測係數比 overall volume 大 30%。
5. **Derivatives 的「information aggregation」功能（Conclusion）**：傳統金融理論認為 derivatives 是 risk-sharing tool（Arrow 1964, Ross 1976）；但 Black 1975 與 Grossman 1977 提出 derivatives 的第二功能——為 informed trader 提供交易通路。這篇文章給這個理論明確實證證據：Δvolatility information 透過 option market 流動，事後在 stock market realized。

### 可用戰術
1. **Daily Vol-Demand Signal 用於系統性交易**：每日收盤後計算 stock i 的 open-volume straddle 淨買量，若 >0.5σ 則 mark 為「informed bullish vol」訊號。實務可 long realized variance vs. short implied（若信號強）或 just long straddle。信號衰減約 5-10 天，捕捉一週級別波動 spike。
2. **Earnings Event Vol Trading**：在 earnings date 前 5 日追蹤 VOL_DEM；若大幅上升 → straddle long；若 neutral → 可考慮 short straddle 賺 IV crush（earnings 後 ATM vol 普遍 mean-revert 5-10 vol points）。
3. **Open vs. Close Volume 過濾**：訂閱 OPRA feed 可識別每筆 trade 的 open-vs-close flag；只 follow open side 的訊號 ensure trading 對手是新 risk taker。零售經紀商如 CBOE LiveVol 提供這個資料。
4. **Straddle-Purity Score**：對每個 underlying 每日計算 min(call_vol, put_vol)/max(call_vol, put_vol)；接近 1 則 high purity straddle volume，該股票的 vol-specific signal 最可靠。
5. **Price Impact Monitoring for Stealth Trade Detection**：若自營部位想做 big straddle 進場，要監測自己的 net demand 對 IV 的 slippage——Ni-Pan-Poteshman 顯示每 +1 std demand → IV +0.5 vol point，所以 100k vega 的 order 可能推高 IV 2-3 vol pts。拆單或 piece-wise execution 避免給市場發信號。

### 盲點/反例
1. **資料截止 2001 年，post-HFT 時代行為變化**：2005+ HFT 在 option market 大舉進入，現在 non-market-maker 的 "informed" 身份可能被 HFT 做 market making 污染（HFT 放大 liquidity 但也 piggyback informed flow）。需 replicate study on 2015+ data。
2. **CBOE 資料限於 US equity option，非普世結論**：歐洲 Eurex、亞洲 HKEX 的 option market maker 結構不同——尤其歐洲有 dealer-intermediated OTC option 佔大比例，訊號品質可能打折。
3. **信號衰減快**：Table 3 顯示 predictability 在 t+6 day 就接近 insignificant，實務 trading 要求 low-latency 反應，慢一日執行就沒 edge。對 discretionary daily-bar 交易者效果有限。
4. **Earnings pre-event IV 已普遍定價**：Ni-Pan-Poteshman 的資料 1990-2001 時代 earnings IV skew 還未完全 efficient；2015+ 已有 earnings-vol ETFs（e.g., OVXY）與 quantitative earnings trader 把大部分 edge 吃掉。
5. **交易成本未完全計入**：論文用 mid-price，實戰 1-2% bid-ask on option 就可能吃掉 signal 全部 edge。低流動性股的 straddle spread 常 >10%，根本不值 trade。

### 與 Edward 既有知識的連結
- **對照 Augen《Option Trader's Handbook》（Round 1）**：Augen 書中「trade straddle before earnings」策略其實就是這篇文章的 retail 版本——Augen 給操作 playbook，Ni-Pan-Poteshman 給學術驗證。
- **對照 Natenberg + Bennett Vol Trading（Round 1 + 本輪）**：Natenberg 教 straddle mechanics，Bennett 教 vol structure，Ni-Pan-Poteshman 給 empirical edge：「informed straddle volume 是 leading indicator」。三者結合可構 complete vol-info 交易系統。
- **對照 Aldridge《High-Frequency Trading》（Round 1）**：Aldridge 的 HFT 談 order flow toxicity（VPIN），概念上對應這篇的 informed trader detection。兩個領域都在問「能不能從 order flow 看出誰是 informed、誰是 uninformed」。
- **對照 Campbell-Lo-MacKinlay《Econometrics of Financial Markets》（本輪）**：CLM Ch 3 Market Microstructure + Ch 12 Nonlinearity 提供了 informed trading + option data analysis 的理論工具；Ni-Pan-Poteshman 是 CLM framework 的具體實證 application。
- **對照 ZP/signals/option_flow 模組**：若 ZP 要做台指選擇權的 option-flow 策略，Ni-Pan-Poteshman 的架構完全可移植——台灣證交所的每日 opt flow data 可公開取得，按外資 / 自營商 / 投信 / 散戶分類是天然的「informed vs. noise」分流。比 US OPRA 更清楚。
- **對照 Poker 的 size tell**：撲克對手的 bet sizing 洩漏 strength tell（超大 bet 常是強牌，標準 pot bet 可能 value bet 或 bluff），這篇文章的 volume magnitude 洩漏 informed intensity——size ≠ signal quality 但 size 的異常 pattern 值得關注。
