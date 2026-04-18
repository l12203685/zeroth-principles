## Investments (10th Ed) — Zvi Bodie, Alex Kane, Alan J. Marcus
**來源**: E:/書籍/Investments, 10ed, 2014, by Bodie Z., Kane A. and A. J. Marcus.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Part I: Introduction**
  - Ch 1 The Investment Environment
  - Ch 2 Asset Classes and Financial Instruments
  - Ch 3 How Securities Are Traded
  - Ch 4 Mutual Funds and Other Investment Companies
- **Part II: Portfolio Theory and Practice**
  - Ch 5 Risk, Return, and the Historical Record
  - Ch 6 Capital Allocation to Risky Assets
  - Ch 7 Optimal Risky Portfolios (Markowitz)
  - Ch 8 Index Models (single-factor, Sharpe diagonal)
- **Part III: Equilibrium in Capital Markets**
  - Ch 9 CAPM
  - Ch 10 APT and Multifactor Models
  - Ch 11 Efficient Market Hypothesis
  - Ch 12 Behavioral Finance and Technical Analysis
  - Ch 13 Empirical Evidence on Security Returns
- **Part IV: Fixed-Income Securities**
  - Ch 14 Bond Prices and Yields
  - Ch 15 The Term Structure of Interest Rates
  - Ch 16 Managing Bond Portfolios
- **Part V: Security Analysis**
  - Ch 17 Macroeconomic and Industry Analysis
  - Ch 18 Equity Valuation Models (DCF, multiples)
  - Ch 19 Financial Statement Analysis
- **Part VI: Options, Futures, and Other Derivatives**
  - Ch 20 Options Markets Introduction
  - Ch 21 Option Valuation
  - Ch 22 Futures Markets
  - Ch 23 Futures, Swaps, and Risk Management
- **Part VII: Applied Portfolio Management**
  - Ch 24 Portfolio Performance Evaluation (Sharpe, Treynor, Jensen, M²)
  - Ch 25 International Diversification
  - Ch 26 Hedge Funds
  - Ch 27 The Theory of Active Portfolio Management (Treynor-Black)
  - Ch 28 Investment Policy and CFA Framework
- **References to CFA Problems**, Indices

### TL;DR (≤120字)
CFA 考試的官方指定教材之一(與 Reilly-Brown 並列):MBA 級別投資學通論,從 CAPM/APT/EMH 等均衡理論到實務 portfolio management、衍生品、hedge funds。強在「理論 + CFA 實題 + historical data」整合,是 buy-side analyst 的 baseline reference。

### 核心本質 (3-5 條, 每條 50-120字)
1. **Passive portfolio 是所有 active 策略的唯一 benchmark** — EMH (Ch11) 的推論:若無 edge,市場組合是 mean-variance optimal。主動策略若無法 outperform 等 β 的 passive 組合 (扣手續費 + 稅後) = 實質 destroying value。每個 active trader 都該誠實自問 benchmark。
2. **Systematic risk vs idiosyncratic risk 的根本分離** — CAPM/APT (Ch9-10) 的核心 insight:只有 systematic risk (β) 獲得市場風險溢酬;idiosyncratic risk 可透過 diversification 消除,故無溢酬。Active trading 想要 alpha,必須接受非 systemic 風險暴露;這就是 edge 的代價。
3. **Behavioral finance (Ch12) 是 EMH 的限制條件而非對立** — 認知偏誤 (over/underreaction、loss aversion) 使得短期定價有系統偏差;但 arbitrage limits (costly short selling、noise trader risk) 讓這些偏差無法被套利完全消除。行為偏差 = active alpha 的可能來源之一。
4. **Duration/Convexity hedging 不是固定收益專利,是利率敏感資產通用語言** — Ch14-16 的框架可類比到股票 (equity duration)、房地產、外匯的利率敏感部分。Duration matching 與 immunization 是 liability-driven portfolio 核心技法。
5. **Performance evaluation 必須扣除 benchmark + risk-adjust** — Ch24 詳列 Sharpe、Treynor、Jensen's α、Information Ratio、M² 的適用情境。分辨「運氣 vs 技巧」的唯一路徑是 risk-adjusted + 長期樣本;否則 noise dominates。

### 可用戰術/策略
- **Treynor-Black active portfolio (Ch27) 作為 multi-strategy combination** — 每個 alpha source 根據其 (預期 α / residual variance) 分配權重,再與 passive 組合線性混合。是 multi-strat fund 的經典定量配置公式,可直接用於 B1 多策略 allocation。
- **Sharpe ratio bootstrap 作為上線門檻** — 任何策略要上線,過 24 個月 in-sample Sharpe > 1.5 + bootstrap 95% CI 下限 > 0.5;否則視為過擬合。結合 López de Prado Deflated Sharpe 進一步校正 multiple testing。
- **Factor tilt based on Ch10 APT** — Fama-French 三因子(size、value、momentum) 再加 quality、low-vol 是常見 systematic alpha 來源;可作為 B1 多因子選股策略的 factor library 起點。
- **Bond immunization** — 當 future cash flow 已知(如退休目標、負債),以 duration = liability duration 建立 bond portfolio,可免疫 parallel yield shock。這是保守資金管理的重要技法,與 active trading 互補。

### 盲點 / 反例 / 適用邊界
- **CAPM 實證問題持續未解** — Fama-French (1992) 證 CAPM β 在橫截面上對預期報酬解釋力微弱;Ch13 討論但不能算解決。Multi-factor 模型較佳但仍非完美;實務上 factor zoo (300+ 聲稱因子) 多半是 data mining。
- **EMH 在極短期與極長期都失效** — Ch11 的 semi-strong EMH 聚焦於 "average" 資訊處理效率;但 flash crashes、bubbles、反轉效應在短期存在;long-horizon 有 value premium、reversal 等持續模式。
- **Hedge fund chapter (Ch26) 資料為 survivorship-biased** — 失敗的 hedge fund 消失不再被統計;歷史平均 return 高估。Ch26 有提但未充分修正;要看 Ibbotson-Chen 的 hedge fund index 論文。
- **偏美股,emerging market 與加密市場未涵蓋** — 2014 年版本對 crypto 無提;新興市場只在 Ch25 國際分散化簡短討論;需另讀 Aswath Damodaran《Investment Valuation》或 Barberis《Psychology and Economics of Financial Markets》補地區+行為特徵。

### 與 Edward 既有知識的連結
- 對應零式第 3 條 `meta_strategy_over_strategy`:Ch24 的 performance evaluation = 對策略的評估(meta-strategy);Sharpe ratio 是資金曲線的 quality metric 而非單筆交易。
- 銜接 `bias_toward_inaction`:Ch11 EMH + Ch24 performance evaluation 實證告訴你,多數主動策略 underperform 被動;若無明確 edge,買 index + 停手是最佳策略。這是零式第 5 條的實證底層。
- 連結 Wilmott FAQ (Q10 MPT, Q11 CAPM, Q12 APT) 與 Jorion FRM (risk management):此書提供 buy-side portfolio 角度,與 Jorion sell-side risk + Wilmott pricing 形成完整三角。
- 對 B1 自營交易系統的貢獻:Ch7-8 portfolio theory + Ch27 Treynor-Black active management 是「多策略資金配置」模組的理論基礎;CFA 實務題庫(book 內附) 可作為系統工程師的考試+認證參考。
