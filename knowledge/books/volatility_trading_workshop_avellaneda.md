# Volatility Trading Workshop — Marco Avellaneda (NYU, RiskMathics 2016)

### 目錄
1. 核心本質 — Vol 交易的 8 維度：realized / implied / correlation / dispersion
2. 可用戰術 — VIX futures roll, variance swap replication, dispersion trade
3. 盲點/反例 — 2020 Mar 與 2018 Volmageddon 對 vol 生態的衝擊
4. 與 Edward 既有知識的連結

### TL;DR
Avellaneda (NYU Courant Institute + Managing Principal at Finance Concepts) 這份 RiskMathics 2016 Mexico + Rio workshop 的講義（約 120 張投影片）是 vol trading 的精煉版大綱。作者為 mathematical finance 著名學者，代表作包括 Avellaneda-Park-Zhu (2010) 統計套利 + Avellaneda-Stoikov (2008) 最優 market making model。此 workshop 核心把 volatility 交易分成 8 個獨立維度：(1) realized vol、(2) implied vol、(3) implied vs realized (variance swap carry)、(4) implied vs implied (skew / term-structure arb)、(5) realized vs realized (cross-asset)、(6) correlation between assets、(7) implied correlation (index vs component)、(8) dispersion。然後聚焦 **VIX futures + ETN + variance swap** 三類工具的操作。**Avellaneda 核心貢獻**：把 BSM/Dupire 框架與 market microstructure 結合，教 trader 如何從 empirical high-frequency 資料中 extract alpha。

### 核心本質
1. **VIX 是 Variance Swap 的 Model-Free 表達（p.8-15）**：新 VIX (2000 後) 不再是簡單 ATM IV weighted，而是 **sqrt( 2/T · Σ over OTM strikes of [(ΔK/K²)·Q(K)] · e^{rT} − (F/K*-1)² )** 的 discretization——這恰好是 variance swap 的 fair value 公式。所以 VIX futures 等同交易 30-day forward variance swap。理論上 VIX² = expected realized variance under risk-neutral measure。
2. **Variance Swap Fixed Leg = -2·E[ln(F_T/F_0)]（p.15-25）**：Avellaneda 推導 `d(ln F)/F = dF/F - (1/2)σ²dt`，取期望 + 用 Itô 整理得 E[realized variance] = -2/T · E[ln(F_T/F_0)]。這讓 variance swap 可以用 log contract（= 無窮多 OTM option 的線性組合）完全 static replicate。
3. **VIX Term Structure 一般 Contango，偶發 Backwardation（p.30-40）**：VIX spot < VIX front futures < VIX 2nd month < ... 是 normal contango，反映「未來 vol 預期 higher + vol of vol premium」。2008、2020 Mar、2011 US debt crisis 時反轉——spot VIX > front month = severe backwardation，意味市場預期當前極端 vol 是 transient。
4. **VIX ETN 的 Roll Yield 詛咒（p.45-55）**：VXX、UVXY 等 ETN follow SPVIXSTR index (short-term VIX futures)，每日 roll front month → 2nd month。Contango 環境下每日虧 roll yield 1-3 bps，累積每月 -4~-8%。2009-2017 VXX 從 10000 美元跌到 50 美元——純 structure decay 不是行情。但 2018 Feb Volmageddon 反向 XIV（inverse VXX）一日 -90% 清算。
5. **Dispersion Trade: long component vol vs. short index vol（p.80-100）**：index variance = Σw_i²σ_i² + 2Σw_iw_jρ_{ij}σ_iσ_j。若 average correlation ρ̄ 遠低於 implied，則 long single stock variance + short index variance 賺 correlation reversion。2017 low-vol, low-correlation 環境 dispersion trade 年化 Sharpe 1.5；2020 Mar all-correlation → 1 時 dispersion 大虧。

### 可用戰術
1. **Variance Swap Replication via OTM Strip**：實務上用 20-30 個 OTM strike 以 (1/K²) weighting 建 variance swap synthetic。SPX monthly expiry 有 >100 個 strike，replication accuracy >99%。
2. **VIX Futures Calendar Roll**：long 3-month VIX futures + short 1-month VIX futures = term structure spread play。Contango 時 long short-end 吃 roll yield 虧、short short-end 吃 long-end 保護，這個 calendar spread 可 isolate "vol of vol" exposure。
3. **Short VIX ETN 長期 positive carry，但需 tail hedge**：short VXX 每月期望賺 4-8%，但承受 tail event catastrophic loss。實務：short VXX 再 buy deep OTM VIX call（10 vol points OTM）作保護，把 max loss cap 在可承受範圍。2020 Mar 這個組合仍賺 5% 而裸 short VXX 虧 80%。
4. **Dispersion via Listed Options**：long single-stock ATM straddles (top 10 constituents by weight) + short SPX ATM straddle。delta 中性，gamma + vega 長 dispersion。hedge 成本約 2-3 vol points，若 realized dispersion > implied by 1+ vol point 就賺。
5. **VIX Futures Mean Reversion Trade（p.60-70）**：當 VIX 飆到 >30 (2 std above LT mean 18-20)，歷史上 3-6 個月內 mean-revert 機率 >80%。short front VIX futures 配合 stop loss at 40。但在 2008 Sep, 2020 Mar 這個 trade 會嚴重 drawdown，需 position size 控制在總 capital 1-2%.

### 盲點/反例
1. **2016 出版，2018 Volmageddon 與 2020 COVID 未覆蓋**：Feb 2018 XIV / SVXY 結構性爆裂、2020 Mar VIX 飆到 83 與 HYG OMM 停擺都顛覆了 vol 交易生態。Avellaneda 這份 workshop 的 contango ETN short 策略在 2018 Feb 一日內 wipeout。
2. **0DTE options 爆發後 vol market 結構改變**：2022+ SPX 0DTE options 每日成交量 >50% of total SPX option volume，對 VIX 計算與 term structure 產生扭曲。VIX 用 30 day IV，0DTE 不直接進入但 spill over 影響 30DTE 微笑形狀。
3. **Liquidity crisis 時 replication fails**：書中 variance swap replication 假設 continuous strike coverage，但 2020 Mar OTM option bid-ask 一度 wider than mid-mid price——replication breakdown，各 desk 的 variance swap 定價差異達 10 vol points。
4. **只聚焦 S&P / VIX ecosystem**：歐洲 V2X、日本 JNIV、亞洲 HSVI 等其他 vol index 的 term structure 動態不同，workshop 沒觸及。台灣的 VIX-TW (2020+ 上市) 流動性極差，實務不能套 US playbook。
5. **Monte Carlo code 與 backtest 細節不足**：投影片重 intuition 輕 implementation，讀者要自己寫 Python 複製策略。沒 data pipeline 教學。

### 與 Edward 既有知識的連結
- **對照 Natenberg（本輪） + Bennett（Round 1 + 本輪）**：Natenberg 是 directional + spread retail focus，Bennett 是 institutional vol mechanics，Avellaneda 是 quant academic + market microstructure 視角。三合一構成 vol trading 的 retail / desk / quant 三層 view。
- **對照 Frontiers QF Vol（本輪）**：Frontiers 的 Bergomi variance curve 與 Henry-Labordère heat kernel 是 Avellaneda workshop 沒深入的前沿學術工作。本 workshop 是 applied 版，Frontiers 是 academic 版。
- **對照 Kissell《Science of Algo Trading》（本輪）**：Kissell 教執行成本，Avellaneda 教 vol alpha。執行 vol 策略時兩個視角都需要——尤其 VIX futures roll 對 transaction cost 敏感。
- **對照 Stat Arb / Pole（Round 1）**：Avellaneda-Park-Zhu (2010) 的統計套利 model 是 Pole 書中方法的升級——用 PCA residual 做 mean reversion，配合跟蹤 vol-of-vol 做 risk management。
- **對照 ZP/strategies/volatility 模組**：若 ZP 加 VIX ecosystem 策略，Avellaneda workshop 是最簡短的 onboarding 參考——8 dimensions of vol + VIX ETN roll yield + dispersion trade + mean reversion 四個 sub-strategy 構成完整 vol book。
- **對照 Poker 的 ICM in late stage**：VIX 在 crisis 時的非線性行為（up 3x in week）類比 poker tournament 到 bubble 時 ICM 急劇 skew 正確 play——兩個場景都有「正常時 linear / crisis 時 non-linear」的 regime switch。
