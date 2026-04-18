## Modern Portfolio Theory and Investment Analysis (9ed) — Elton, Gruber, Brown, Goetzmann (2014)
**來源**: C:/Users/admin/staging/b2_batch_E_extracts/e2c02dfa7e5b1dfa__elton_gruber_brown_goetzmann_modern_portfolio_theory_and_inv.md  |  **消化日**: 2026-04-18  |  **模型**: claude-opus-4-7[1m] (main session)

### 目錄
- Part 1 描述性（證券與市場結構、機構背景）
- Part 2 Modern Portfolio Theory 基礎
  - Ch4-6 投資組合理論（Markowitz mean-variance、efficient frontier）
  - Ch7-8 輸入簡化（correlation structure model、single index model）
  - Ch9 計算程序簡化
  - Ch10 expected return 預測
  - Ch11 最優組合選擇（individual investor 角度、utility functions）
  - 國際分散化
- Part 3 資本市場均衡（CAPM、APT）
- Part 4 個別證券（efficient market test、equity valuation、earnings、bond、option、future、behavioral finance）
- Part 5 評估（分析師預測、portfolio performance measurement）

### TL;DR (≤120字)
Elton-Gruber-Brown-Goetzmann 九版是 portfolio management 教科書的 gold standard，2014 版針對 2008 危機新增「factor-based investing」、「mutual fund industry 結構變化」、「emerging market diversification」三章；核心訊息：2008 沒有打倒 Modern Portfolio Theory 而是驗證了其底層邏輯 — 分散化、長期視角、多因子暴露仍是 robust 投資原則。

### 核心本質 (3-5 條)
1. **Mean-Variance 是投資學的「歐氏幾何」**（本質） — Part 2 核心：Markowitz 1952 證明 portfolio risk ≠ sum of individual risks；加入 correlation < 1 的資產後 portfolio variance 嚴格降低；這是所有分散化的數學根基。即使 2008 危機中 correlation 奔向 1，「平時 correlation < 1」的平均效應仍成立，故長期 portfolio theory 不失效。
2. **Single Index Model 是 Markowitz 的實用簡化**（本質） — Ch7-8：純 Markowitz 需估 N(N+1)/2 個 covariance（100 股要估 5050 個），實務不可行；Sharpe (1963) 的 single-index model 假設所有相關性透過單一 market factor，把參數降到 N+2 個。這啟發了後來 Fama-French 多因子模型，是 factor investing 的根源。
3. **CAPM 是理論美、實證粗糙**（本質） — Part 3：CAPM 假設均衡下個別資產 expected return 僅依賴 systematic beta；實證上（Fama-French 1992）size、value、momentum 因子都有解釋力；2014 版坦承 CAPM 不是全部真相，但 beta 仍是 risk decomposition 的有用起點。
4. **Efficient Market 不是 "price is right"，是 "you can't easily beat it"**（本質） — Part 4：有效市場三種形式（weak / semi-strong / strong），empirical evidence 支持 weak form 但拒絕 strong form；實務意義是「 technical analysis 沒用、insider trading 有用」的中間地帶；這對量化交易策略的 ex-ante 勝率估計至關重要。
5. **Behavioral Finance 是 MPT 的補丁不是替代**（本質） — Part 4 新章節：系統性的 cognitive biases（loss aversion、overconfidence、herding）會創造 temporary mispricings，但無法打破長期市場均衡；MPT + behavioral overlay = 完整投資觀；純 behavioral 派（如 Shiller）忽略 arbitrage force 修正錯誤的速度。

### 可用戰術/策略
- **Mean-Variance Optimizer 框架**：給定 expected returns μ、covariance Σ、risk aversion λ → w* = (1/λ) × Σ⁻¹ × μ；加入 constraint（sum to 1、long-only、max position）後用 quadratic programming 解；需特別注意 Σ 的 conditioning number，poor 的需 shrinkage estimator。
- **Black-Litterman 混合 view**：Ch10 延伸：將 market-cap 隱含 equilibrium returns 與 investor 自己的 view（P、Q 矩陣）透過 Bayesian 更新混合；避免純 optimizer 對 estimation error 極度敏感的問題。
- **Ex-ante 投資評估 Sharpe Ratio Framework**：計畫策略前先問：historical excess return / volatility ratio 是多少？Ch25 提示超過 1.0 是頂級、0.5-1.0 是良好、<0.3 不值得 deploy。
- **Performance Attribution 分解**：Ch28 的 Brinson-Fachler 歸因：total excess return = allocation effect (sector weights) + selection effect (stock picks within sector) + interaction；可用於評估自己策略的 alpha 來源。
- **International Diversification 評估**：Ch12：international correlation 歷史 0.3-0.5，2008 後升至 0.6-0.8；仍建議 20-30% international allocation 但不再期待 naive diversification 可完全 cross-country hedge。

### 盲點 / 反例 / 適用邊界
- **Normal Distribution 假設** — Markowitz 框架假設 returns 近似 normal；實證是 fat-tail + skewness；tail risk 無法純靠 variance 量化，需 CVaR、expected shortfall 等 coherent risk measures。
- **Covariance Stability 假設** — 2008、2020 危機證明 correlation 不 stable；regime-switching 環境中 static covariance estimation 失效，需 dynamic（DCC-GARCH）。
- **Transaction Cost 未納入 core framework** — Kissell 等書強調 transaction cost 至關重要，但 Elton-Gruber 主線框架假設 frictionless trading；實務中 high-turnover optimal portfolio 可能被成本吃光 alpha。
- **"Market Portfolio" 難以定義** — CAPM 要求 true market portfolio（包含所有可投資資產），實務用 S&P 500 或 MSCI World 只是 proxy；Roll critique（1977）至今未完全解決。
- **Survivorship bias 在 mutual fund 章節** — 雖然 2014 版新增 mutual fund 章節，分析資料仍有部分 survivorship bias；倖存基金的績效被自動高估。

### 與 Edward 既有知識的連結
- **對齊 ZP 核心**：MPT 的 "diversification is free lunch" 對應零式投資本質 — 當兩個資產 correlation < 1 時，portfolio risk 嚴格低於加權平均 risk；這是少數在經濟學中經數學證明的「無中生有」。Edward 的 B2 經濟自給策略應內建 multi-strategy diversification，而非單一 all-in。
- **延伸既有 DNA**：single-index model 的概念可延伸到永生樹 subagent 管理 — 所有 subagent 的表現可能由單一「主 session 品質 factor」驅動；estimation 與 risk decomposition 用此簡化可大降複雜度。
- **衝突點**：Elton-Gruber 仍大量依賴 CAPM/Markowitz 框架；現代量化基金（Two Sigma、Renaissance）早已跳脫 mean-variance paradigm，改用 machine learning + alternative data；教科書對應 1990 年代最佳實踐，不是 2024 cutting-edge。
- **可挖金礦**：Ch28 的 performance attribution 框架可直接套用到 Edward 自營交易的月度回顧 — 把 P&L 拆成「資產配置效果（大類選擇）+ 擇時效果（時點）+ 標的選擇效果（個別）」三者；持續追蹤可找到自己真正的 alpha 來源。
