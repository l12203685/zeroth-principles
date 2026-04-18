## Trading Volatility: Trading Volatility, Correlation, Term Structure and Skew — Colin Bennett (JP Morgan 研究)
**來源**: E:/投資交易/交易學習資料庫/@交易/@選擇權/Trading Volatility.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Executive Summary
- Option Trading in Practice / Maintenance of Option Positions
- Call Overwriting / Protection Strategies
- Option Structures Trading
- Volatility Trading (Variance is the Key, not Volatility)
- Volatility, Variance, Gamma Swaps / Options on Variance
- Correlation Trading (Correlation Swaps, Dispersion, Basket Options, Covariance Swaps)
- Dividend Volatility Trading
- Long Volatility is a Poor Equity Hedge
- Structured Products Vicious Circle
- Forward Starting Products (Fwd starting options, VIX futures, Fwd starting var swaps)
- Exotic Structures (Barrier, Worst-of/Best-of, Outperformance, Look-back, Contingent Premium, Composite/Quanto)
- Relative Value Trading / Earnings Jumps
- Stretching Black-Scholes Assumptions / Skew & Term Structure
- Skew Trading (Sticky Delta, Sticky Strike, Sticky Local Vol, Jumpy Vol)
- Local Volatility / Measuring Historical Volatility
- Proof Variance Swaps via Log Contract
- Greeks / Advanced Shadow Greeks
- Capital Structure Arbitrage

### TL;DR (≤120字)
JP Morgan 研究部出品，可能是市面上最接近 sell-side volatility desk 實戰的書籍。核心論斷：(1) 波動率交易真正的 exposure 是 variance 不是 volatility（gamma × return² 是日 PnL 公式）；(2) skew trade 等同 2nd-order gamma trade；(3) long vol 不是好的股票 hedge（carry 太貴）。

### 核心本質 (3-5 條)
1. **Variance is the Key, not Volatility**（本質） — 期權 delta-hedged PnL = ½ × gamma × (return² − implied_var × Δt)，是 variance 的差而不是 volatility 的差。Variance swap 讓交易者純粹 exposure variance，不受 BS 非線性干擾；這是 vol trading 從「option-based hedging」升級到「pure vol exposure」的關鍵工具。
2. **Skew Trading = 2nd Order Gamma Trading**（本質） — skew 表達的是「大跌時波動率上升更多」這個二階關係；long skew 等同於 long vol-of-vol + correlation-of-vol-with-spot。Sticky Delta / Sticky Strike / Sticky Local Vol / Jumpy Vol 四種 regime 下 skew 的 PnL 完全不同，只有 jumpy vol 下 long skew 確實賺錢。
3. **Long Vol 是糟糕的股票避險**（本質） — carry cost 極高（var risk premium 常年負），長期持有 long vol 會 bleed；只在 short-term 高機率 crash 時有效。更好的 hedge 是 put spread 或動態 beta-adjusted short。書中用 20 年回測數據證明 long vol portfolio 長期 Sharpe < 0。
4. **Correlation Trading 的四種工具**（本質） — dispersion（long basket var, short constituent var）是 correlation bet 的主流；correlation swap 純 exposure correlation 但流動性差；basket options 隱含 correlation 風險；covariance swap 更好代表 structured product 的真實 risk。每個工具對應不同的 market view + 流動性需求。
5. **Structured Product Vicious Circle**（本質） — sell-side 結構化產品銷售導致 dealer 長期 short skew 與 short convexity；市場波動時 dealers 必須 short gamma squeeze 覆蓋，放大 tail risk。這是 2008 與 2020 VIX spike 的 microstructure 根源之一。

### 可用戰術/策略
- **Variance Swap Implementation**：透過 strip of options (from near-ATM to far-OTM) 複製 var swap；依 log contract 公式 2/K² weighting 各 strike。適合大戶做 pure vol bet。
- **Dispersion Trade**：short index var swap + long weighted basket of constituent var swaps；implicit short correlation；correlation 上升（危機時）虧損，平靜期 harvest risk premium。
- **Call Overwriting on Long Holdings**：針對長期持股賣 short-dated OTM call（delta 15-25），每月收 premium；策略年化 5-15% enhancement，但 cap upside；Bennett 提供最佳 strike 與 maturity 選擇框架。
- **Forward Starting Variance Swap**：買 6M forward 3M variance swap；避免當前 realized vol 的短期噪音，純粹 bet 未來 term structure 變化。
- **Skew Trade via Risk Reversal**：long put + short call 同 delta；sticky strike regime 下賺取 skew 回歸；需配合 delta hedge 避免純方向暴露。

### 盲點 / 反例 / 適用邊界
- **Sell-side 視角** — 書中假設讀者有 JPM 級別的 execution + pricing infrastructure；retail / small hedge fund 無法直接複製 variance swap、dispersion 等 trade（OTC market, minimum ticket $1M+）。
- **Exotic structures 的複雜性** — Worst-of/Best-of、contingent premium 等 exotic options 的定價與風險管理需要 Monte Carlo + PDE + Stochastic vol 模型組合；書中點到為止，不足以單獨實作。
- **未涵蓋 post-2018 vol regime shift** — 2018 Volmageddon、2020 COVID、2022 tightening 都改變了 vol surface 的微結構；書中部分 empirical regularity（如 VIX futures contango）需要更新。
- **Hedge 策略失敗案例的少量樣本** — 作者傾向展示 hedge 成功的回測，對失敗期間（如 2017 超低 vol 整年）的 strategy bleed 討論不夠平衡。

### 與 Edward 既有知識的連結
- **對齊 ZP options**：Bennett 的「variance > volatility」觀點可作為 ZP 期權交易系統的核心原則——策略的真正 PnL 驅動是 realized vs implied variance spread，不是 IV 點估計差。
- **衝突 Natenberg / Augen**：Natenberg/Augen 是 retail-facing，Bennett 是 sell-side institutional；Edward 作為自營交易者位置介於兩者間，需取 Natenberg 的直覺 + Bennett 的工具 + Augen 的調倉。
- **對應 Higham**：Bennett 的 log contract proof 可用 Higham 的 Monte Carlo / PDE code 實現驗證；理論與計算 cross-check。
- **延伸應用**：Edward 的 portfolio hedge 策略應避開「長期 long vol」陷阱，改用 put spread ratio + dynamic delta；可具體化為 `ZP/hedging/strategies/` 模組。
- **可挖金礦**：Correlation Trading 章節（dispersion 特別）可用於台股 vs 成分股的相對 vol 交易；台灣 50 成分股的 dispersion premium 在全球危機時擴大，是未被充分利用的 alpha。
- **0DTE 時代延伸**：Bennett 的 variance swap 思維在 0DTE SPX options 時代可轉換為 intraday gamma trading——每日 implied vs realized variance 差異為主要 edge。
