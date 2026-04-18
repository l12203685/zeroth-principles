# International Encyclopedia of Statistical Science — Miodrag Lovric (ed.)

### 目錄
1. 核心本質 — 統計學科 A-Z 百科全書：1800+ 條目、600+ 位作者
2. 可用戰術 — 查詢特定方法、跨領域概念 cross-reference
3. 盲點/反例 — 百科全書的廣度 vs. 深度困境
4. 與 Edward 既有知識的連結

### TL;DR
Lovric 編輯 (Springer 2011, 1673 頁超大本，約 8MB 純文字) 是統計學史上最龐大的 reference work。主編 Miodrag Lovric（Belgrade 大學）召集 **600+ 位來自 100+ 國的統計學者** 撰寫 **1800+ 個條目**，從 A (Absolute Penalty Estimation) 到 Z（各種 Z-test）——幾乎涵蓋統計學的每個活躍子領域。**結構**：按字母排序，每個條目 2-5 頁，由該領域活躍研究者撰寫，配 References。與傳統 textbook 不同，這本的優勢是**可直接查詢**——遇到不熟術語（如 partial least squares、ecological correlation、intrinsic credibility）可直接翻到對應字母查 2 頁精華。它不是給「從頭讀」用，而是給「遇到問題查」用。**對 quant 特別有用的條目**：Adaptive Sampling、Bootstrap、Bayesian Networks、Cointegration、Copula、GARCH、Hausman Test、Kalman Filter、Lasso、Markov Chain、Monte Carlo、Neural Networks、Principal Components、Random Walks、ROC Analysis、Structural Equation Models、Time Series、Vector Autoregression 等。每個條目作者多半是該領域現職教授，內容權威性高。

### 核心本質
1. **百科全書功能而非教科書**：傳統 textbook 要 linear 讀完，encyclopedia 是 reference——遇到 unknown term 跳進去看 2 頁就能大致理解，再決定是否深入 textbook。Lovric 的優勢在條目之間 cross-reference（▷mark）——查 "Absolute Penalty Estimation" 會連到 ▷Least Squares、▷Ridge Regression、▷Lasso，形成知識網絡。
2. **領域廣度是特色（也是限制）**：涵蓋 classical (frequentist)、Bayesian、nonparametric、time series、spatial、functional data、high-dim、ML 與 applied (biostatistics, psychometrics, econometrics, reliability) 多個子領域。每個條目本身深度有限（2-5 頁），但跨領域 breadth 無出其右。
3. **國際多元作者視角**：Lovric 刻意請各國學者寫，避免 US-centric。例如 Italian/German 統計學派傳統（Benzécri correspondence analysis、Castellani-Volkmann time series）的觀點可在此找到，與美系傳統（Fisher-Neyman-Pearson）形成對照。
4. **現代方法與歷史方法並陳**：既有 classical χ² test、ANOVA，又有 2010 前沿的 high-dim lasso、compressed sensing、graphical models、spectral clustering。查 "Regularization" 同時看到 Tikhonov (1963)、Ridge (1970)、Lasso (1996)、Elastic Net (2005)、Sparse Group Lasso (2010)。
5. **Controversies 章節**：有些條目 explicitly 比較不同學派觀點——例如 "Bayesian versus Frequentist Testing" 條目把 Lindley paradox、confidence vs. credible interval 差異、Savage's axioms 等爭論濃縮成 3 頁。這是 textbook 很少做的 meta-analysis。

### 可用戰術
1. **遇到論文生詞先查**：讀 quant paper 遇到 "J-test"、"Doornik-Hansen test"、"Shapiro-Wilk test"、"Brown-Forsythe test" 等 niche test，直接翻 L 查 2 頁 precis 比 Google 快且權威。
2. **Cross-Reference 走訪相鄰知識**：查 "Cointegration" 會連 ▷Unit Root、▷Vector Error Correction、▷Johansen Test，順藤摸瓜找到完整 toolkit。比純讀 textbook 更能建構知識網絡。
3. **比較 Competing Methods**：查 "Robust Regression" 可一次看到 M-estimator、S-estimator、MM-estimator、LTS、LMS 的 trade-off，快速決定採用哪個。若只讀單一 textbook 可能只看到作者偏好的一種。
4. **Historical Context**：許多條目有 "History" section 講發明者與思路——Fisher 為何發明 ANOVA（農業田間試驗）、Neyman 為何發明 confidence interval（與 Fisher 的 fiducial interval 對立）。這些 context 幫助理解「為什麼這方法這樣設計」。
5. **References 作為深度延伸**：每個條目尾部給 5-15 個核心文獻，省去自己從 Google Scholar 搜尋的時間。對博士生做 lit review 極有用。

### 盲點/反例
1. **深度不足以做 research**：2-5 頁的條目只能給概念與核心公式，嚴肅 research 仍需讀原始 paper 或 specialized textbook。Lovric 是 starting point 不是 destination。
2. **2011 年出版，2015+ 重大進展缺席**：Deep learning、transformer、causal inference with machine learning (Double ML, TMLE)、differential privacy、federated learning 等 2015+ 突破都沒收錄。補新教材或 review paper。
3. **條目品質不一**：600+ 作者寫作風格與詳盡度差異大——有些條目精雕細琢（如 Bootstrap 由 Efron 親寫），有些明顯是新手擬稿。讀者要自己判斷哪些條目可信。
4. **中文/日文統計學派幾乎缺席**：Lovric 的國際涵蓋仍以歐美為主；中國、日本、韓國統計學派的獨特貢獻（如 Gao's statistical learning theory）未充分反映。
5. **Software 與 computing 節略**：條目重理論輕實作，沒 R/Python code 範例。Software-oriented reader 要配合 Hastie-Tibshirani-Wainwright《Statistical Learning with Sparsity》這類現代教材。

### 與 Edward 既有知識的連結
- **對照 Casella-Berger《Statistical Inference》（本輪）**：C-B 是 PhD-level frequentist inference 教科書（12 章深入），Lovric 是 broad reference（1800 條 breadth）。讀 C-B 系統建構基礎，用 Lovric 填缺口或橫向擴展。
- **對照 Greene《Econometric Analysis》+ Wooldridge（本輪）**：Greene/Wooldridge 聚焦計量，Lovric 涵蓋 stats + econometrics + bio-stats 交集。若 Edward 發現某個計量方法在 bio-stats 有更成熟處理（如 survival analysis），Lovric 提供跨領域連結。
- **對照 Bayesian Methods in Finance (Round 1, Rachev)**：Rachev 專攻金融 Bayesian application，Lovric 的 Bayesian Networks、Hierarchical Bayesian Models、MCMC 等條目給 Rachev 技術的學科源頭。
- **對照 ZP/knowledge/statistics 索引**：我應該把 Lovric 當作 ZP 統計知識的「default lookup service」——任何 subagent 遇到 unknown term 先查 Lovric 對應條目，再決定是否 escalate 到 specialized source。類似把 Wikipedia 提升為專業版統計參考。
- **對照 Poker 的 math toolkit**：撲克 equity calculation、ICM、EV 計算本質都用 statistics——條件機率、combinatorics、decision theory。Lovric 的 Game Theory、Decision Analysis 條目提供 pure-math 根基，讓 poker 思維可以回到 statistical first principles 重新推演。
- **對照 Meta 層級**：Lovric 本身作為 reference work 的存在 reminds Edward：永生樹的知識結構應該像這本書——**可查詢、cross-linked、多作者、但統一索引**。ZP 的 knowledge tree 設計可借鏡此模式。
