# Statistical Inference (2ed) — George Casella & Roger L. Berger

### 目錄
1. 核心本質 — 充分統計量、完備性、極大似然是推論的三大基石
2. 可用戰術 — 估計量選擇、檢定構造、區間估計
3. 盲點/反例 — 古典框架在金融資料上的張力
4. 與 Edward 既有知識的連結

### TL;DR
Casella-Berger 2ed (Duxbury 2002，本 extract 是 Utah State U. STAT 6720 講義引用 Ch 5-10) 是美國統計 PhD qual exam 的標準教科書，12 章結構：前 4 章機率基礎、Ch 5 sampling 分布、Ch 6 limit theorems（LLN, CLT）、Ch 7 point estimation、Ch 8 充分統計量與完備性、Ch 9 Neyman-Pearson 檢定、Ch 10 LRT/Wald/Score、Ch 11 confidence intervals、Ch 12 nonparametric。核心哲學是 **Fisher-Neyman-Pearson 的「頻率派」範式**：Theorem 6.2 弱大數法則、Theorem 6.4 中央極限定理、Factorization theorem (T 充分統計量⇔likelihood 可分解)、Cramér-Rao 下界、Rao-Blackwell 定理、Lehmann-Scheffé UMVUE、Neyman-Pearson lemma（最佳檢定結構）、Likelihood Ratio Test 大樣本分布收斂至 χ²。第 8.7 節 MLE 的 invariance property、第 9.2 節 Neyman-Pearson lemma、第 10.1 節 LRT 是全書的三個高峰。

### 核心本質
1. **Sufficient Statistic 是「壓縮不失真」的關鍵（Ch 8.3 / Factorization Theorem）**：統計量 T(X) 對參數 θ 充分⇔聯合似然可分解成 f(x|θ) = g(T(x)|θ) · h(x)。例 8.3.8 的 Normal(μ,σ²) 得到 T=(ΣX_i, ΣX_i²) 充分，例 8.3.7 Poisson 得到 T=ΣX_i 充分。意義：做推論時不必保留全部原始資料，只需充分統計量即可。金融上這對即時交易系統有直接意涵——只需保留累計成交量與累計成交額²就能估 trend + volatility，不必記每一筆 tick。
2. **Cramér-Rao Lower Bound 界定「不可能更準」的下界（Ch 8.5）**：任何無偏估計量的變異數 Var(T) ≥ 1/I(θ)，其中 I(θ) = E[(∂log f/∂θ)²] 是 Fisher Information。達到下界的估計量叫 efficient。這給回測評估一個硬下界——即使有完美模型，參數估計誤差也被資料量下界住。T=252 日的 Sharpe ratio 估計標準差約 √(2/252)≈0.089，所以兩個 Sharpe 差 <0.1 在統計上無意義。
3. **Neyman-Pearson Lemma 指引最佳檢定構造（Ch 9.2）**：simple-vs-simple hypothesis 下，Likelihood Ratio f(x|θ₁)/f(x|θ₀) 是 most powerful test，閾值由 Type I error α 決定。意義：所有檢定問題都回到「LR 是否超過 critical value」。這也是 Black-Litterman 模型 posterior weighting 的理論根基。
4. **LRT 的 Wilks 定理是「通用」檢定工具（Ch 10.1）**：-2·log(Λ) →_d χ²(r)，其中 r = 自由度差。只要模型 nested 就能比較，不必特別推導。實證 asset pricing 常用的 Wald test、LR test、Score test 在漸近下等價（三大 test 三角形）。
5. **Modes of Convergence 的層級（Ch 6.1）**：a.s. ⇒ in prob ⇒ in distribution；L^r ⇒ in prob（r-th moment convergence）。但反過來不對。例 6.1.22 的 P(X_n=n)=1/n^r 序列 converges in prob 但 E|X_n|^r=1 不收斂——「尾部不可控」導致期望值不收斂。金融上的啟示：VaR 的 Monte Carlo 估計即使 converge in probability，tail expectation（CVaR/ES）不一定 converge——需要有限 r-th moment 假設才能 bootstrap CI。

### 可用戰術
1. **MLE + invariance（Ch 8.7）**：若 θ̂ 是 θ 的 MLE，則 g(θ̂) 是 g(θ) 的 MLE。例：估計 GARCH 的 persistence α+β 時，分別估 α̂、β̂ 再相加就是 MLE。極方便。
2. **Lehmann-Scheffé: 充分+完備+無偏 = UMVUE（Ch 8.4-8.5）**：Rao-Blackwell 把任何無偏估計量條件到充分統計量上可降變異；再加完備性確保唯一。實用：在 Normal(μ,σ²)，X̄ 是 μ 的 UMVUE，S² 是 σ² 的 UMVUE。
3. **Pivotal Quantity 構造 CI（Ch 11.1-11.2）**：pivot Q(X,θ) 的分布不依賴 θ。例 Normal mean：(X̄-μ)/(S/√n) 服從 t(n-1)。這套方法延伸到 bootstrap-t 是實務上最穩健的 CI 構造方式，特別是 non-normal 金融資料。
4. **Wald/Score/LR Trinity（Ch 10.1）**：三種檢定漸近等價但小樣本表現不同——LR 通常最穩健，Wald 計算最快（只要 MLE 變異數），Score 不需要算 alternative 下 MLE。回測時用 LR 比較 regime-switching 模型 vs. single-regime GARCH 最可靠。
5. **Sequential Probability Ratio Test（Ch 14.2 / SPRT）**：Wald (1947) 的 SPRT 允許樣本 stopping time 隨資料變化，在金融上天然對應「繼續交易或停止」的決策——當 LR 超過 A 或低於 B 時停止。相較於固定 sample size 可省 >30% 樣本達同樣 α, β。

### 盲點/反例
1. **整本書以 iid 為基本假設**：Ch 7.1 random sampling 直接假設 iid，後續 MLE consistency、asymptotic normality 證明都依賴這個假設。金融時間序列 autocorrelated + heteroscedastic 必須用 GMM/QMLE 重推——Greene Ch 13（本輪）接棒。
2. **沒有 Bayesian 的實質討論**：Ch 8.8 Bayes estimation 只停在 prior-posterior 的基本介紹，沒 MCMC、HMC、conjugate prior families 的應用。作 regime-switching 用 Gibbs sampler 或 factor model 用 variational inference 必須另補。
3. **Asymptotic 主義的盲區**：Ch 6 CLT 的收斂速度是 O(1/√n)——Berry-Esseen 界限顯示對非對稱厚尾分布 n=100 仍不夠近似 Normal。股票 daily return 有 kurtosis 10+，asymptotic p-value 常嚴重低估 Type I error；應用 bootstrap 或 permutation test 更穩。
4. **沒有 high-dim（p>n）的現代處理**：Casella-Berger 是 1990-2002 寫作，當時 Lasso 剛出來，sparse recovery 理論（Candès, Tao, Donoho 等）還沒進教科書。做 quant factor model 有 100+ 特徵 <100 periods 時，必須補 Hastie-Tibshirani-Wainwright《Statistical Learning with Sparsity》。
5. **Nonparametric 章節（Ch 12）只到 Wilcoxon/Kolmogorov-Smirnov**：沒 kernel density estimation、local regression、spline 等現代 nonparametric。做 stochastic volatility 的 implied vol 曲面估計必須用 Nadaraya-Watson 或 spline smoothing。

### 與 Edward 既有知識的連結
- **對照 Greene《Econometric Analysis》（本輪）**：Greene 應用 C-B 的理論做計量——Fisher information → MLE 標準誤、Wald/LR → hypothesis test、delta method → asymptotic 分布。讀 Greene 遇到證明不完整處翻 C-B 補理論。
- **對照 Rachev《Bayesian Methods in Finance》（Round 1）**：Rachev 用 Bayesian 框架克服 C-B Ch 7-8 的頻率派限制——事前信念可編碼市場觀點、posterior 天然給出區間估計。兩本互補。
- **對照 ZP/statistics 模組**：我目前的 ZP 統計基礎缺一份權威的 frequentist 推論參考，Casella-Berger 填這個洞。特別是 Ch 8 充分統計量的 factorization theorem 對設計 online learning algorithm（只存 sufficient stats 不存 raw data）有直接價值。
- **對照 Poker 的 EV 計算**：Casella-Berger Ch 9 Neyman-Pearson lemma 是決策理論的根源——poker GTO solver 本質上是在約束 P(Type I) ≤ α 下最大化 power；exploitative play 則是引入先驗（對手類型）偏離 NP lemma 的 minimax 解。兩套思維對應兩種 metagame。
- **對照 DNA §2 決策五公理的「Bias toward inaction」**：CR 下界給出「不動手的資訊門檻」的量化版本——若預期訊號幅度 < 2·√(1/I(θ))，就算方法正確也沒統計顯著。這讓 axiom 5 從哲學變成可計算的停損線。
