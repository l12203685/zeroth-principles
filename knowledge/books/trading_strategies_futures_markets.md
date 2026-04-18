## Trading Strategies in Futures Markets（學術論文合輯，Imperial College / QMUL）
**來源**: E:/書籍/Trading Strategies in Futures Markets.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Abstract / Introduction
- Paper 1: The Returns to Carry and Momentum Strategies
  - Returns, Leverage and Trading Strategies / Characterizing Carry and Momentum Returns
  - Understanding Return Premia to Carry and Momentum
  - What We Can Learn About Momentum by Observing Carry?
  - Appendix (Tables, Figures, Recessions and Hedge Fund Liquidity)
- Paper 2: Optimal Futures Portfolios and Hedge Fund Capital
  - Portfolio Construction (Optimal with Predictable Returns, Tradable Futures Return Series, Transaction Costs)
  - Data (Price, Macro/Liquidity, Hedge Fund)
  - Characterising Optimal Futures Portfolios (Carry & Momentum across Asset Classes, Risk Aversion, Diversified Investor)
  - Business Cycles, Limits to Arbitrage and Hedge Fund Capital (Risk Factor Exposure, Macro/Funding Liquidity, HF Activity)
- Paper 3: Assessing the Economic Significance of Commodity Futures Price Predictors
  - Methodology / Data / Results / Robustness
- Conclusions

### TL;DR (≤120字)
三篇學術論文的合輯，核心實證：Carry 與 Momentum 是期貨市場兩大普適 alpha 來源（跨 FX、commodities、bonds、equities）。兩者 Sharpe 相近但回撤時機相反——危機時 momentum 掙錢 carry 虧錢；在 optimal futures portfolio 中兩者互補帶來 Sharpe ~1.5，顯著高於單因子。限制套利因素（hedge fund capital flows）解釋了 premia 的時變特性。

### 核心本質 (3-5 條)
1. **Carry ≠ Momentum 但互補**（本質） — Carry = 買高 yield + 賣低 yield 資產（currency：高利率 vs 低利率；commodity：backwardation vs contango；bond：高 yield vs 低 yield）。Momentum = 過去 12 個月漲的買、跌的賣。兩者 ex-ante 看似都是 trend-following 但實質 exposure 不同——危機時 carry 趨同崩盤，momentum 往往正收益，兩者合成 portfolio 有負 correlation。
2. **Carry 的 crash risk = Momentum 的 hedge**（本質） — Carry trade 承受 "peso problem"（長期小賺，偶發大虧）；momentum 在 carry 崩盤時因為 loss 累積已經 short，天然 hedge。這解釋了為何 CTA 基金同時用兩策略。
3. **Limits to Arbitrage 導致 Premia 時變**（本質） — hedge fund capital 是 carry/momentum risk premia 的最大邊際參與者；當 funding liquidity 收縮（如 2008、2020），HF 被迫 delever，造成 strategy 暫時失效但長期重新修復。這是 Shleifer-Vishny 限制套利理論在期貨市場的實證。
4. **Predictability 的經濟顯著性 ≠ 統計顯著性**（本質，Paper 3） — 很多 commodity predictor（basis、hedger position、open interest）統計上顯著但扣除 transaction cost + turnover 後經濟上不顯著。真正有 alpha 的是能在 monthly 或更低頻捕捉 persistent trend 的因子，不是 daily 噪音中的偶然 signal。
5. **Optimal Portfolio 權重受 Risk Aversion 影響大**（本質，Paper 2） — 傳統 mean-variance 假設 risk aversion 固定；論文發現 risk aversion 時變時，最優 portfolio 的 carry/momentum 權重波動 50%+。保守投資人應重 momentum（low tail risk），aggressive 投資人可重 carry（high Sharpe 平靜期）。

### 可用戰術/策略
- **跨資產 Carry Portfolio**：FX carry（long 高利率 currency basket + short 低利率 basket）+ Commodity carry（long nearby - long farther basket 按 slope）+ Bond carry（long 高 yield country + short 低 yield）。每類分配 30% 風險預算。
- **Cross-Sectional Momentum**：每月 rank 各資產過去 12 個月 return，long top 20% + short bottom 20%；每月 rebalance。期貨因 no short-sale constraint 對稱性強。
- **Risk Parity + Carry/Momentum**：先用 inverse volatility 給各資產類相同風險貢獻，再疊加 carry 與 momentum signal 做 tilting；比純 60/40 Sharpe 高 30-50%。
- **Crisis Indicator**：監測 funding liquidity proxies（TED spread、VIX、LIBOR-OIS）；當急升時減碼 carry，增碼 momentum + tail hedge。
- **Transaction Cost 嚴格估計**：扣除 1 basis 以上 per rebalance 的成本才算 net alpha；論文示範 raw Sharpe 可達 2.0 但 net Sharpe 降到 1.0-1.3 是正常。

### 盲點 / 反例 / 適用邊界
- **2018-2022 Momentum crash** — 2018-2020 momentum 表現糟糕（利率、value、growth 翻轉），論文發表前未涵蓋；純 momentum CTAs 同期虧損 20-30%。
- **Carry crash 的 fat tail** — Paper 1 的 carry risk premia 部分解釋是 "crash risk compensation"，但歷次 crisis 的虧損分布是 heavy-tailed，VaR 估計不準確。
- **Hedge fund capital 測量困難** — 論文用 TASS/HFR database，但自營部位、家族辦公室、主權基金的資金未涵蓋；實際 marginal buyer/seller 結構複雜得多。
- **Survivorship bias 在 commodity futures data** — 老舊合約（如 1970s Lead、Zinc）已退出；論文樣本偏向倖存市場，實際歷史 carry/momentum 表現可能更差。
- **未涵蓋 crypto** — crypto 期貨的 carry（perpetual funding rate）與 momentum 結構不同，論文框架需 adapt。

### 與 Edward 既有知識的連結
- **ZP B1 經濟自給**：Carry + Momentum 是少數有數十年 out-of-sample 證據的 systematic strategy，可作為 Edward 自營基金的核心 alpha engine。
- **對應 Kestner**：Kestner 的 quantitative trading 框架可用 Carry/Momentum 作為 main signal，配以 K-Ratio + money management。
- **對應 Vince Portfolio Math**：Carry+Momentum 組合的 optimal f 可用 Vince 方法精確推導；兩者相關性低時 f* 可較純單策略高 20-30%。
- **衝突 Gibson Asset Allocation**：Gibson 主張 60/40 passive；論文實證 systematic futures 可大幅 enhance passive portfolio；Edward 的家庭資金仍用 Gibson，自營用本論文思路。
- **可挖金礦**：三篇論文完整 carry/momentum factor 建構 code 可直接複製到 `ZP/strategies/cross_asset/`；每日抓期貨數據即可實盤。
- **延伸應用**：AQR、Winton、MAN AHL 等 CTA 基金都公開使用類似 systematic carry/momentum；Edward 可對標他們的公開 factsheet 作為實盤 benchmark。
