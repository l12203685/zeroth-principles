## The Handbook of Portfolio Mathematics — Ralph Vince（2007，Formulas for Optimal Allocation & Leverage）
**來源**: staging/b2_batch_D_extracts/22a0960eb9b862ff__ralph_vince_the_handbook_of_portfolio_mathematics_wiley_2007.md | **消化日**: 2026-04-18 | **模型**: opus-4.7 | **Round**: llm_round_6

### 目錄
- PART I Theory
  - Ch1 The Random Process and Gambling Theory（獨立 vs 依存序列、數學期望、正態分佈、莊家優勢、Baccarat、Pari-Mutuel、連勝連敗、Runs Test、相關係數）
  - Ch2 Probability Distributions（基礎、矩、正態、CLT、Lognormal、Uniform、Bernoulli、Binomial、Geometric、Hypergeometric、Poisson、Exponential、Chi-Square、Student's t、Multinomial、Stable Paretian）
  - Ch3 Reinvestment of Returns and Geometric Growth（TWR、幾何平均、Kelly Criterion、Optimal f 的推導）
  - Ch4 Optimal f（Vince 原創：Optimal f 作為 Kelly 的實務延伸；每交易最大幾何增長的下注比例）
  - Ch5-7 Parametric Optimal f（對連續機率分佈、混合分佈、實務參數估計）
  - Ch8 The Geometry of Mean HPR（Holding Period Return 幾何）
- PART II（後半）Leverage Space Portfolio Theory
  - Ch9-12 The Leverage Space Portfolio Model（多資產 Optimal f、Drawdown 限制、Risk of Ruin）
  - Ch13-15 Applications to Real-World Portfolios（期貨、股票、期權組合）

### TL;DR (≤120字)
Vince 是繼 Thorp/Kelly 之後最深入的「資金管理數學家」，本書整合他前三本書的精華。**核心貢獻：Optimal f**——對於非 binary outcomes 的真實交易序列，推廣 Kelly 公式到「最大化 TWR（Terminal Wealth Relative）」的下注比例。書的另一里程碑是 **Leverage Space Portfolio Theory**，將 Optimal f 從單資產推廣到 N 資產組合，內建 drawdown constraint。全書偏重計算與機率，是量化資金管理的 canonical reference。

### 核心本質 (3-5 條)
1. **E[log(wealth)] ≠ log(E[wealth])**（本質，Ch3） — Vince 強調，複利下長期幾何平均報酬才是投資者真正關心的。公式：Geometric Mean Holding Period Return = G = (HPR₁ × HPR₂ × ... × HPRₙ)^(1/n) 必須 > 1 才能長期獲利。
2. **Optimal f 的精確公式**（本質，Ch4） — 對於一連串交易（w₁, w₂,..., wₙ，含虧損），解 f 最大化 TWR(f) = Π(1 + f × wᵢ / |worst_loss|)。Optimal f 是 Kelly 公式在真實 R 分佈下的對應。實戰意義：若 Optimal f = 0.4，代表每次交易下注帳戶的 40% × (worst case loss)；比 Kelly 更激進，但幾何增長率最大。
3. **Anti-Martingale ≠ Martingale**（本質，Ch1 + Ch3） — 賭博體系分兩大類：(a) Martingale（虧損後加碼）必破產，因為 bankroll 有限而損失可放大到 ∞；(b) Anti-Martingale（獲利後加碼）是 Optimal f 的精神——贏時增加下注，虧時減少。所有穩健策略必須是 Anti-Martingale。
4. **Drawdown 的數學宿命**（本質，Ch4-8） — Vince 證明：任何策略在 Optimal f 下，**任意比例 x 的最大 drawdown 發生機率為 x**。即：100% drawdown（破產）的機率是 0，但 50% drawdown 幾乎必然、20% drawdown 是 20% 機率。實戰啟示：許多人在 -30% drawdown 時放棄，但那其實是 Optimal f 的正常波動。
5. **Leverage Space**（本質，Part II） — Vince 原創：將 N 資產的每個 f 組合視為 N 維空間中的點；每個點對應一個 (Expected Return, Variance, Drawdown Prob) 三元組。投資者選擇 Pareto 前沿上的點——這是 Markowitz Mean-Variance 的動態延伸，考慮了路徑依賴性（drawdown）。

### 可用戰術/策略
- **Optimal f 計算步驟**：(1) 取歷史交易 PnL 序列；(2) 設 worst loss = WL；(3) 對不同 f 計算 TWR = Π(1 + f × PnLᵢ / WL)；(4) 取使 TWR 最大的 f\*。
- **Fractional-f 實務**：Full Optimal f 波動極大；Vince 建議用 0.1-0.3 × f\* 以換取心理承受性。這與 Thorp 的 Half-Kelly 思想一致。
- **Runs Test 檢測依存性**：Ch1 用 Z-score 統計檢驗連續交易是否獨立。若 prove 交易序列 + 相關，可用 autocorrelation 改進 Optimal f 估計。
- **Stable Paretian Distribution**（Ch2）：對 fat-tail 回報分佈用 stable paretian（α-stable）建模，而非常態；這是 Mandelbrot 的主張，Vince 將其納入資金管理公式。
- **Leverage Space 多資產配置**：對於 N 資產組合，不做傳統 MVO（Mean-Variance Optimization），而是搜尋 leverage space 中 drawdown probability ≤ 閾值的最大 TWR 點。

### 盲點 / 反例 / 適用邊界
- **需要大樣本歷史交易**：Optimal f 要求至少 30-50 筆歷史交易才能可靠估計；初學者或新策略難適用。
- **參數過擬合風險**：Ch11 的 Parametric Optimal f 對分佈假設敏感；若實際分佈偏離假設，f\* 可能嚴重錯誤。
- **忽略 regime shift**：公式假設交易序列的 drop-down 分佈穩定；真實市場有 fat-tail regime shifts（2008、2020 Covid）使歷史 WL 嚴重低估。
- **單純追求幾何最大化忽略 utility**：若投資者非 log-utility，Optimal f 非最優；需配合 Samuelson 的目標函數修正。
- **高 leverage 在實務中受合約約束**：保證金要求、強制平倉等機制使 f 有實務上限，公式未納入這些約束。

### 與 Edward 既有知識的連結
- **對齊 ZP 零式本質**：Optimal f 的目標 = 「幾何增長最大化 subject to 生存約束」＝ Edward 的經濟自給+永續。這是數學化的本質對齊。
- **對接 Fortune's Formula（llm_round_6 同批）**：Poundstone 講 Kelly 歷史，Vince 提供實務計算公式；兩者互補為資金管理完整地圖。
- **延伸 Kelly Capital Growth**（同批將處理）：Vince 的 Optimal f 是 Kelly 在 real-world PnL 分佈的推廣。
- **衝突點**：Vince 激進派（主張逼近 Full Optimal f），Thorp / Elder 保守派（主張 Fractional）；Edward 應根據自身心理 bucket 選擇。
- **可挖金礦**：Leverage Space Portfolio Theory 是多資產系統（B1T3 未來擴展到多市場）的理論基礎；可整合入 ZP/portfolio/vince_leverage_space.md。Optimal f 的 python 實作可作為 ZP/tools/risk_calc.py 的核心函數。
