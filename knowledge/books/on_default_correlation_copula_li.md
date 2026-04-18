# On Default Correlation: A Copula Function Approach — David X. Li (2000)

### 目錄
1. 核心本質 — 用 survival time copula 建模 default correlation
2. 可用戰術 — Gaussian copula CDO 定價、first-to-default swap
3. 盲點/反例 — 這是 2008 金融危機的「公式元兇」
4. 與 Edward 既有知識的連結

### TL;DR
David X. Li (RiskMetrics Group Working Paper 99-07, April 2000) 是金融史上最有影響力、也最惡名昭彰的 quant paper 之一。Li 當時任職 RiskMetrics (JPMorgan 獨立出來的 risk 部門)，提出把 **default correlation 定義為 survival times 之間的 correlation**，並用 **Copula function**（特別是 Gaussian copula）建模聯合分布。這篇 paper 讓 CDO、basket default swap 的定價變得「可計算」——只需要一個參數 ρ（correlation）就能把複雜的多債聯合違約機率壓縮。**正面影響**：2000-2007 全球 CDO 市場從 $250B 爆炸到 $2 trillion，Wall Street 能量化 tranche pricing 並做動態 hedge。**負面影響**：2008 金融海嘯後，Wired 雜誌 Salmon (2009) 發表 "Recipe for Disaster: The Formula That Killed Wall Street"，直指 Li 的 Gaussian Copula model 讓投資銀行低估 correlated 違約的 tail risk，是造成次貸危機的主因之一。Li 本人 2003 離開 JPM 回中國，後來在中金公司任首席風險官。這篇 paper 是 quant 歷史課必讀——教訓：**一個 elegant 公式能掀起全球金融動盪**。

### 核心本質
1. **Time-Until-Default 取代 Discrete Default Event（§1）**：傳統 CreditMetrics 用「1 年內是否 default」的二元事件定義 correlation，Li 批評這種方法丟失 time structure 資訊——50 歲人 1 年內死亡機率 0.6% 但 100 年內幾乎 100%。Li 引入 **survival time T_i = 時間直到 default**，define default correlation = Corr(T_A, T_B)，這個量不依賴特定觀察期。
2. **Copula Function 分離 Marginal 與 Joint 結構（§2-3）**：Sklar 定理——任何多變量 CDF F(T_1,...,T_n) 都可分解成 F = C(F_1(T_1),...,F_n(T_n))，其中 C 是 copula，F_i 是邊際 CDF。意義：market 給出每個 credit 的 marginal survival curve（從 CDS spread 校準），剩下的 correlation structure 只需指定一個 copula。
3. **Gaussian Copula 是 CreditMetrics 的 latent 工具（§4）**：Li 證明 Merton 的 asset-based approach（CreditMetrics）等同於用 Gaussian copula——每個 obligor 的 asset value 是 Gaussian，default = asset < threshold，則 joint default probability 由 Gaussian copula C_Φ(u_1,...,u_n; Σ) 給出。這個等價性讓新方法與業界標準相容。
4. **First-to-Default Swap 定價（§5, Example 1）**：basket 內 n 個 credit，first-to-default 事件機率 P(min(T_1,...,T_n) < T)。Li 給 explicit formula——P(no default before T) = 1 - C(S_1(T),...,S_n(T))，其中 S_i = survival function。Correlation 低 → min(T_i) 更易短 → premium 高；Correlation 高 → 多個 default 集中 → min 更長 → premium 低。
5. **Default Correlation 的 time-dependency（§1）**：Li 以夫妻同齡 50 歲為例——1 年內都死亡的 correlation 很低（獨立事件），100 年內都死亡的 correlation 接近 1（必然事件）。這個觀察暴露 discrete-event correlation 的 arbitrariness——同一對 entity 依觀察期不同 correlation 可以從 0 跳到 1。

### 可用戰術
1. **Calibrate Copula Correlation from CDS Index（§5 後記）**：CDX IG 的 base correlation curve (每個 tranche attachment/detachment 對應一個 implied Gaussian correlation) 是 standard market convention。traders 買/賣 tranche 等同 view on correlation surface 形狀。
2. **Factor Copula for Large Portfolio（後續文獻引用）**：n 個 credit 的 n×n correlation matrix 校準太多參數；改用 single-factor Gaussian（所有 credit 與 common factor 有 correlation ρ，彼此 conditional independent）把參數數壓到 1。基本上是 Vasicek (1987) portfolio loss model 的 copula 版本。
3. **Student-t Copula 改善 Tail Dependence**：Gaussian copula 的 tail dependence = 0，意即極端事件 correlation 歸 0。Student-t copula 有正 tail dependence，更適合 crisis modeling。Mashal-Zeevi (2002) 實證 equity returns 的 t-copula 比 Gaussian fit 好。
4. **Credit Default Swap Self-Hedging**：counterparty CDS seller 違約時，買方無法收到 protection payment = 雙重違約。Li §5 示範 combined default probability by Gaussian copula (ρ = CDS seller 與 underlying 的 asset correlation)，可定 counterparty credit adjustment (CVA) premium。
5. **Rating Transition Correlation**：延伸 Li 的 framework，CreditMetrics 的 transition matrix 加 copula 可以做 correlated rating migration——AAA → AA 與另一家 AA → A 同時發生的機率。這對 bank portfolio 的 economic capital 估計重要。

### 盲點/反例
1. **Gaussian Copula 低估 Joint Extreme Events**：Gaussian copula 的 upper tail dependence = 0——即使邊際 marginal 相同，Gaussian copula 預測「兩個都爆」的機率遠低於 Student-t 或 Clayton。2008 subprime CDO market 全面使用 Gaussian，假設 ρ=0.3，實際 ρ→0.9 時預測損失低估 5-10x。Salmon 2009 Wired 文章詳細記錄這個 dissonance。
2. **Single-Factor Assumption 在 Crisis Break**：factor copula 假設 common factor 是 Gaussian，conditional on factor 各 credit 獨立。但 2008 MBS/CDO 的 losses 同時來自 housing price crash + mortgage fraud + rating agency conflict of interest，不是單一 factor。
3. **參數 Stability 假設錯誤**：Li 假設 ρ 是 constant，實務上 correlation 是 regime-dependent——平時 0.3，crisis 0.9。Dynamic copula model（Patton 2006）試圖 address 但實務應用有限。
4. **Rating-Based Correlation 不是 Market-Implied**：很多 desk 用歷史 rating migration 資料估 ρ，約 0.1-0.3；但 CDS market implied correlation 可達 0.6-0.8。兩者巨大差異意味「model ρ」vs. 「market ρ」不一致，有 mark-to-market 問題。
5. **Li 本人的後悔**：Salmon 2009 訪問 Li，Li 承認 "The most dangerous part is when people believe everything coming out of it (my formula)." Li 在 2008 已離開華爾街回中國。
  
### 與 Edward 既有知識的連結
- **對照 Schmid《Credit Risk Pricing Models》（本輪）**：Schmid Ch 4.4 直接引用 Li 2000 並討論其 copula framework。Schmid 給出完整 theory + pricing，Li 是原始 paper source。
- **對照 Frontiers QF Part II Credit Risk（本輪）**：Laurent-Cousin Ch 7 的 "Factor Modeling for CDO Pricing" 是 Li 2000 的 post-crisis refinement——用 Student-t、Archimedean copula 替代 Gaussian，Turc-Very Ch 9 local correlation 讓 ρ 隨 loss level 變化。
- **對照 Engle SRISK（Round 1）**：Engle 的 systemic risk measurement 本質也是 joint tail event probability，但用 GARCH + time-varying conditional correlation 而非 copula——兩條技術路線對同一問題。
- **對照 ZP 的「模型風險」警示**：這篇 paper 是 model risk 最著名案例——elegant mathematics 在錯誤場景應用會造成 trillion-dollar 災難。ZP 若未來用任何 copula 方法都要加 stress test：ρ=0.9 的情況下 portfolio loss 是多少？否則重蹈覆轍。
- **對照 Poker 的「collusion detection」**：撲克桌上多玩家配合作弊的 collusion 機率模型也用 copula——每個玩家獨立 call/fold 是 baseline，observed correlation 偏離代表 collusion。金融 default correlation 與 poker 行為關聯模型本質同構。
- **對照 DNA §2 axiom 4 "Population exploit"**：Li 的 paper 在 2000-2007 是市場 mainstream 模型。2008 它的 failure 讓 short CDO (via CDS) 的 hedge fund 大賺（e.g., Paulson & Co 一年賺 $15B）——這正是「眾人同向時 contrarian +EV」的極端案例。
