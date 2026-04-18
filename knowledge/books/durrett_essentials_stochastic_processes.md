## Essentials of Stochastic Processes, 2nd Edition — Richard Durrett
**來源**: E:/課程/[7] 隨機過程/Essentials of Stochastic Processes, 2ed, 2012, Durrett R.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Ch1 Markov Chains（definition, transition matrix, classification of states, stationary distribution）
- Ch2 Poisson Processes（exponential inter-arrival, compound Poisson, nonhomogeneous）
- Ch3 Renewal Processes（elementary renewal theorem, key renewal theorem, age process）
- Ch4 Continuous Time Markov Chains（generator Q, Kolmogorov equations, reversibility）
- Ch5 Martingales（discrete-time, optional stopping）
- Ch6 Mathematical Finance（Black-Scholes, binomial tree, American options）
- Ch7 Brownian Motion（construction, properties, quadratic variation）
- Ch8 Queueing Theory（M/M/1, M/M/s, networks）

### TL;DR (≤120字)
Durrett 的《Essentials of Stochastic Processes》是本科生友好版——比《Probability: Theory and Examples》更輕量，以應用為導向，例題豐富。Ch6 mathematical finance 章節用極簡框架教 Black-Scholes 與 American option，對 quant 入門極有效。適合作為「機率論之後、連續時間隨機過程之前」的橋樑。

### 核心本質 (3-5 條)
1. **Markov Chain Stationary Distribution 的計算** (Ch1) — 對 irreducible 且 aperiodic MC，存在唯一 π 滿足 πP=π 與 Σπᵢ=1；計算 stationary 的實用方法是解此線性方程組或用 detailed balance 條件 πᵢPᵢⱼ=πⱼPⱼᵢ（可逆 MC）。Quant：regime-switching 模型的 long-run regime probability。
2. **Poisson Process 的三種等價定義**（Ch2） — (a) 計數過程，increment 獨立 & Poisson 分布；(b) inter-arrival 時間為 iid Exponential；(c) 在 (0,t) 內 n 個事件條件下，事件時刻為 uniform 分布。三個視角互相印證，對 rate modeling 提供靈活工具。
3. **Continuous-Time Markov Chain via Generator Q**（Ch4） — Q 是 transition rate matrix (off-diagonal 為 rate，row sum=0)；P(t) = exp(Qt)；對 finite state space，可用 spectral decomposition 封閉求解。金融 applied：credit rating transition model。
4. **Optional Stopping 的金融應用**（Ch5） — 在離散 martingale 框架下證明「gambler's ruin」：從 a 到 N 的機率=a/N (對 simple random walk)，對應零均值 game 的 stopping 結果。
5. **Black-Scholes via Binomial Tree Limit**（Ch6） — 離散 binomial（p=(r+σ√δt - d)/(u-d)) 在 δt→0 極限下收斂到 BS formula。此書用非常簡化的途徑呈現此收斂，繞開測度論，適合初學。

### 可用戰術/策略
- **Classification of States**：對 MC 劃分 recurrent/transient/absorbing，確定策略在 long-run 是否會絕對破產（hit absorbing state）。
- **Poisson Process for Order Flow Modeling**：HFT 訂單流可建模為 Poisson（rate λ）或 compound Poisson（rate λ + 訂單大小分布）；用此估計 flow intensity。
- **Renewal Theorem for Reward Per Unit Time**：對 renewal-reward process，long-run 每單位時間獎勵 = E[reward per cycle]/E[cycle length]；計算 market making spread capture。
- **Generator Q for Credit Migration**：Moody's rating transition 可建模為 CTMC with Q matrix；用此計算從 AA 到 CC 的遷移機率，作為信用風險估計。
- **Binomial Tree for American Option**：離散 backward induction：V_n = max(payoff_n, E[V_{n+1}|F_n]/R)；實作簡單但需要 enough steps (~1000) 收斂到 BS。

### 盲點 / 反例 / 適用邊界
- **Brownian motion 章節簡單**（Ch7） — 只 40 頁，不涉及 Itô 積分嚴格理論；需 Shreve 補足。
- **缺少 Lévy 過程** — 只有純 Poisson，沒 general Lévy；跳躍-擴散 jump-diffusion 需其他書。
- **Finance 章節太簡化**（Ch6） — 只有 BS 基礎，沒 exotic options、greeks、vol smile；僅適合入門。
- **習題以基礎為主** — 深度習題少，適合 self-teaching 但博士資格考用不夠。

### 與 Edward 既有知識的連結
- **ZP 入門教材**：在完成 Baby Rudin + 基礎機率論後，作為隨機過程入門；Edward 節省時間的選擇。
- **對應 Williams**：Williams 偏 martingale 深度，Durrett Essentials 偏廣度（MC/Poisson/renewal/BM 全覆蓋）。
- **延伸 Shreve Vol II**：讀完 Durrett Essentials 第 6-7 章後，可直接進 Shreve BM 與 Itô calculus。
- **衝突：過於應用導向**：缺嚴格 measure-theoretic foundation；若要深入理論研究需 Durrett PTE 或 Billingsley。
- **可挖金礦**：Ch2 Poisson process 的 thinning/superposition 性質可直接用於 order flow decomposition——把總流量分成 buy/sell/cancel 三個獨立 Poisson stream。
