## Financial Risk Manager Handbook (4th Ed) — Philippe Jorion
**來源**: E:/書籍/[@License] Financial Risk Manager Handbook, 4ed, 2007, by Philppe Jorion [#FRM].pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Part One: Quantitative Analysis**
  - Ch 1 Bond Fundamentals (Duration, Convexity)
  - Ch 2 Fundamentals of Probability (Distributions, Copulas)
  - Ch 3 Fundamentals of Statistics (Regression, Parameter Estimation)
  - Ch 4 Monte Carlo Methods (Cholesky, Curse of Dimensionality)
- **Part Two: Capital Markets**
  - Ch 5-6 Derivatives, Forward/Futures/Swaps
  - Ch 7-8 Options, Option Strategies
  - Ch 9-10 Fixed Income, Convertibles
  - Ch 11-12 Equities, Market Microstructure
- **Part Three: Market Risk Management**
  - Ch 13-14 VaR Methods (Parametric, Historical, Monte Carlo)
  - Ch 15-16 VaR Models, Stress Testing, Liquidity Risk
- **Part Four: Investment Risk Management**
  - Ch 17-19 Portfolio Risk, Asset Allocation, Hedge Funds
- **Part Five: Credit Risk Management**
  - Ch 20-23 Credit Exposure, Default Probability, Ratings, Credit Derivatives
- **Part Six: Operational & Integrated Risk**
  - Ch 24-26 Basel II, Operational Risk, Firmwide Risk
- **Part Seven: Legal / Accounting / Regulation**
- **Appendices** (Formulas, Sample FRM questions)

### TL;DR (≤120字)
FRM 全球證照的官方指定教材,Jorion (VaR 發明者之一) 執筆:從 quant analysis 到市場/信用/操作風險全覆蓋,是 risk manager 的 one-stop reference。核心訊息:風險管理是分類學+度量學+策略學的三合一體系,每一類風險需專屬模型與治理框架。

### 核心本質 (3-5 條, 每條 50-120字)
1. **風險分 4 類且相互耦合** — 市場風險 (價格波動)、信用風險 (違約)、操作風險 (人為/系統失誤)、流動性風險 (無法出場)。2008 金融海嘯是市場→流動性→信用→系統性級聯崩潰的教科書案例;每一類獨立建模但相關性在壓力情境下急升為 1。
2. **VaR 是 risk budget 分配工具,不是「損失上限」** — Jorion 明確:VaR 是「99% 信心下單日損失不超過 X」,但 1% 尾部可無限大。用 VaR 做風險預算(各部門/策略分配 VaR 限額)是合理;當成最大損失保證則會步 LTCM 後塵。
3. **Duration / Convexity 是所有 rate-sensitive 資產的共同語言** — Ch1 的 Taylor 展開揭示:債券價格變動 = -Duration × ΔY + 0.5 × Convexity × ΔY²。此框架推廣到任何 rate 敏感的 Greek、VIX、FX 衍生品,一階風險用 Duration,二階用 Convexity。
4. **Copula = 跨資產尾部相關性的建模關鍵** — Ch2 指明:單用 linear correlation 會嚴重低估尾部相依;Gaussian copula 又會低估(2008 CDO 教訓);需用 Student-t copula、Clayton/Gumbel Archimedean copulas 模擬崩盤時相關性趨 1 的現實。
5. **Monte Carlo 不是萬能,受限於 curse of dimensionality + random seed 偏差** — Ch4.3.2 警告:5+ assets 時純 MC 收斂慢,需用 Sobol / Halton 低偏差序列或 quasi-MC;且 MC 結果對 random seed 敏感,生產環境須多次跑取均值。

### 可用戰術/策略
- **VaR decomposition for strategy budgeting** — 把 total VaR 分解到每個策略/帳戶的 Marginal VaR contribution,據此動態調整資金分配;績效考核用 RoVaR (return / VaR) 而非純 return,符合 FRM 第 17 章投資組合風險管理標準。
- **Historical simulation VaR 作為 baseline** — 不假設分布、直接用歷史回報序列排序取 99% 分位;實作 <50 行 Python;比 parametric VaR 更貼近現實厚尾,適合作為 B1 自營交易系統的 risk module 第一版。
- **Cholesky correlated MC 生成壓力情境** — 以多資產 covariance 矩陣 Cholesky 分解 (Ch4.3.1) 生成相關隨機變數,模擬未來損益分布;加入「stressed covariance」 (相關性全部拉到 0.9+) 做極端壓測。
- **Duration-convexity hedging 的完整對沖模板** — 債券部位 + 利率期貨/swap,以 Duration match 一階、Convexity match 二階,Residual 留給 gamma hedge;可直接作為 B1 固定收益策略模組的對沖 class。

### 盲點 / 反例 / 適用邊界
- **FRM 是 "teach-to-exam" 教材,深度常犧牲給廣度** — 每個 risk topic 給 2-3 個公式 + 簡化推導,但實務細節(如 PDE 求解、Malliavin calculus、實際 bank risk system architecture)需後續專書。
- **偏 sell-side / 銀行 risk manager 視角** — 強在 credit / operational / regulatory 側;buy-side quant 做 alpha 策略時需補 López de Prado、Bergomi《Stochastic Volatility Modeling》等。
- **2007 版未含 2008 後 Basel III、CVA/DVA/FVA、CCP clearing 強制化、SA-CCR 取代 CEM 等制度變遷** — 2010-2020 監管巨變需以 Gregory《Counterparty Credit Risk and CVA》、Hull 最新版補。
- **加密/DeFi 風險管理框架完全缺位** — 鏈上 protocol risk、bridge 攻擊、oracle 操縱、smart contract bug 這些新型操作風險在此書不覆蓋,需另立新框架。

### 與 Edward 既有知識的連結
- 直接支撐 `risk_control_four_layers` 四層框架:Jorion 的市場/信用/操作/流動性對應 Edward 的 L1 倉位 / L2 停損 / L3 尾部保險 / L4 流動性準備;建議 B1 自營交易系統 risk module 採 Jorion 分類法為 top-level schema。
- 連結 `meta_strategy_over_strategy`:FRM 的 risk budget 思維(先分配再交易)就是 meta-strategy 核心。VaR allocation + monitoring + rebalance 是「策略之上的策略」。
- 對應 Hull 教科書 Ch18 (VaR) 的深化:Hull 教基礎概念,Jorion 給實務 risk manager 的操作手冊。兩書組合可覆蓋 B1 交易系統風控模組 90% 需求。
- 對 B7 ZP 寫作貢獻:可提取 Jorion 對 VaR 限制的論述(尤其尾部風險)寫成〈VaR 的五大誤解〉專文,對應 `risk_control_four_layers` 的延伸。
