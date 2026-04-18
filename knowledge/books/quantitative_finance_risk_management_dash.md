# Quantitative Finance and Risk Management: A Physicist's Approach — Jan W. Dash

### 目錄
1. 核心本質 — 物理學家視角的 quant finance：從 path integral 到 VaR
2. 可用戰術 — Barrier options、Skew、Numerical methods、Integrated risk
3. 盲點/反例 — 2004 前的 model-heavy 視角 vs. post-2008 現實
4. 與 Edward 既有知識的連結

### TL;DR
Dash (World Scientific 2004, 約 1000 頁) 是前 Citi, UBS, HSBC 資深 quant Jan Dash 寫的巨著——**Part I 介紹**、**Part II Risk Lab (nuts & bolts)**、**Part III Exotics**、**Part IV Fixed Income**、**Part V Credit**、**Part VI Path Integrals & Stochastic Calculus**、**Part VII Numerical Methods**、**Part VIII Integrated Risk Management**、**Part IX Macroeconomics of Risk**。特色是 Dash 本人是 theoretical physics PhD（CERN 做粒子物理），用 Feynman path integral 語言重寫了大部分 quant finance——這讓 derivation 更直觀但 notation 偏 Feynman 路線積分而非 Ito。最實用的章節：**Ch 5 FX Options**（vol surface、quanto、two-country paradox）、**Ch 6 Equity Vol Skew**（Derman's rules of thumb for sticky strike/delta/local vol）、**Ch 25-28 Fixed Income Modeling**（HJM + LMM）、**Part V Credit Risk**（CreditMetrics、KMV、CDS）、**Part VIII Integrated Risk Management**（含 economic capital、limit setting、stress scenario）。**Dash 核心哲學**：quant finance 不只是 Black-Scholes + numerical implementation，還要能在 crisis 時定出 integrated 風險指標給 risk manager 決策——model risk、market risk、credit risk、operational risk 要在 common framework 內。

### 核心本質
1. **Path Integral 重寫 Option Pricing（Part VI）**：Dash 用 Feynman path integral 表達 BSM——option price = ∫ payoff(S_T) · P(path) D[path]，其中 P(path) = e^{-∫L dt} 的權重。這相當於 PDE 方法的 Lagrangian 版本，對 exotic options（Asian、lookback、barrier）的直觀理解特別有用——payoff 依賴 path 時，直接對所有 path 積分。
2. **Derman's Rules of Thumb for Skew（Ch 6）**：Dash 引述 Emanuel Derman (Goldman) 的三個 sticky rule——(a) Sticky Strike：IV(K, T) 只依 K，spot 變動時 IV 不變；(b) Sticky Delta：IV 依 ln(K/F)，spot-level independent；(c) Sticky Local Vol (Dupire)：σ_local 是 deterministic 函數 of (S, t)，IV surface 隨 spot 走。三個假設決定了 delta hedge 的微分方向。實證 equity 市場多落在 sticky strike 與 sticky delta 之間。
3. **Two-Country Paradox 與 Quanto Adjustment（Ch 5, p.48）**：FX option 從兩個 country 的角度看 drift 不同——美國 trader 的 USDJPY call 在 US risk-neutral measure 下 drift = r_US - r_JP，日本 trader 看同樣 option 的 drift 是 r_JP - r_US + σ_USD·σ_JPY·ρ。兩個都對，因為 measure 不同；quanto 產品的 correlation 調整就是在這個 paradox 上做的。
4. **Integrated Risk Management（Part VIII）**：Dash 強調 VaR 不夠——需要 market + credit + operational + liquidity + model risk 全部加總。他的 "cube" 框架把 risk 按 (time horizon × asset class × risk type) 三維分類，讓 CRO 可以一眼看出集中風險。這個想法 2011 Basel III 後成為主流（Economic Capital, ICAAP）。
5. **Model Risk 本身就是 risk（Ch 55）**：Dash 列出 5 種 model risk——(a) wrong model 選擇、(b) 正確模型但 parameter misestimation、(c) data error、(d) implementation bug、(e) regime change 讓假設失效。LTCM 1998 爆倉、Amaranth 2006 爆倉都是第 e 類。Dash 建議 reserve 10-30% 的 PnL 作 model reserve 緩衝。

### 可用戰術
1. **Static Replication 做 Barrier Option（Ch 6 p.58）**：knock-out barrier option = vanilla option - rebate at barrier（若 knocked out 給 cash）。用 vanilla strip 加一個 digital 近似 rebate，避免 dynamic delta hedge 的 gap risk（barrier 附近 delta 可能 explode）。
2. **Perturbative Skew（Ch 6 p.56）**：近似 local vol 模型用 expansion in skew slope。對 small skew 準確且快，比 Monte Carlo 快 100x；但 extreme skew（2008 tail）失準。實務 tier-2 business 用 perturbative，tier-1 才跑 full numerical。
3. **Historical Simulation VaR（Part II）**：用過去 250 個 daily return 直接抽樣做 P&L distribution，取 99% percentile。比 parametric (Gaussian) VaR 更抗厚尾但需大量歷史 + 新 product 沒歷史就不能用。Dash 建議 blend: 80% 權重用 historical, 20% 用 stressed scenario。
4. **Scenario Analysis 補 VaR 不足**：VaR 看 99% percentile 忽略 >99% 的 tail；stress scenario（2008 崩盤情境、1987 Black Monday、1998 LTCM、2000 dotcom bust）把 portfolio 丟進歷史情境跑 P&L。監管現在都要 reverse stress test——多大 shock 會讓 capital 見底？
5. **Numerical Code Sanity Check（Ch 5 p.51）**：所有 pricing code 要有 closed-form benchmark——對 BSM vanilla option 跑 Monte Carlo，結果要 match 理論值 within 0.1%；barrier option 跑 reflection principle analytic formula。No benchmark = potential silent bug producing wrong hedges.

### 盲點/反例
1. **2004 年出版，重大 post-crisis 變化未涵蓋**：FVA、XVA suite (CVA/DVA/FVA/MVA)、bilateral vs. cleared OTC、CCP default waterfall、SOFR transition 全都在 Dash 之後。補 Gregory《Counterparty Credit Risk》或 Andersen-Piterbarg 系列。
2. **Heavy on Physics Notation**：Lagrangian、path integral、Feynman diagram 等物理術語 quant 讀者需要額外適應。現代 quant 教科書（Shreve、Glasserman）傾向 stochastic calculus 標準 notation，更 interoperable。
3. **Implementation 細節略少**：Dash 給 pricing formulas 與 intuition，較少實作 code。生產級 quant library 要 port 到 C++/Python 自己寫。
4. **Machine Learning 完全缺席**：2004 年 ML 在金融還未起飛；現在 vol calibration、TCA、credit scoring 普遍用 neural net。補 Kelly-Xiu《Financial ML》（Round 1）。
5. **Crypto / Structured Products 缺席**：Dash 時代 crypto 不存在、結構化商品剛起步。crypto option market 的特殊性（24/7、high IV、infrastructure 風險）需另讀。

### 與 Edward 既有知識的連結
- **對照 Neftci《Principles of Financial Engineering》（本輪）**：Neftci 是 synthetic/engineering approach（pedagogical），Dash 是 comprehensive encyclopedic（reference）。同樣的 option pricing 從兩個角度切入——Neftci 問「這 payoff 怎麼 synthesize」，Dash 問「這 formula 背後的 path ensemble 長什麼樣」。
- **對照 Brigo-Mercurio《Interest Rate Models》（Round 1）**：Brigo-Mercurio 專注 rates 隨機模型，Dash Part IV Fixed Income 是簡化版 + 加 risk management 視角。兩者 HJM + LMM 討論技術互通。
- **對照 Frontiers QF Vol+Credit（本輪）**：Frontiers QF 是 post-crisis 現代學術前沿（rough vol、jump-diffusion、local correlation），Dash 是 pre-crisis 的 baseline。兩本合看可以看到 2008 對 quant finance 的洗禮。
- **對照 ZP/integrated_risk 模組**：Dash Part VIII 的 integrated risk framework 正是我 ZP 還缺的——目前 ZP 有單獨的 market risk (VaR)、個別策略 drawdown，但沒 cross-strategy / cross-asset 的 total risk view。應補一個「risk cube」view。
- **對照 Poker 的 multi-table variance**：撲克 multi-tabling 需要 total bankroll 管理（不是每桌獨立），Dash 的 integrated risk 就是金融版的 multi-desk P&L 合計風險。兩個都需要 top-down 的 drawdown limit 而非 bottom-up 單項。
