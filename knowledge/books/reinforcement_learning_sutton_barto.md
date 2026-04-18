## Reinforcement Learning: An Introduction 2e — Richard S. Sutton & Andrew G. Barto
**來源**: MIT Press canonical 2018 edition (free PDF)  |  **消化日**: 2026-04-18  |  **模型**: Claude Opus 4.7 (1M context)

### 目錄
- **Part I Tabular Solution Methods (1-8)**：
  - 第 1 章 Introduction（RL problem、historical perspective）
  - 第 2 章 Multi-armed Bandits（ε-greedy、UCB、gradient bandit）
  - 第 3 章 Finite MDPs（Markov property、value functions、Bellman equations）
  - 第 4-5 章 Dynamic Programming、Monte Carlo Methods
  - 第 6-7 章 Temporal-Difference Learning、n-step Bootstrapping
  - 第 8 章 Planning and Learning（Dyna、prioritized sweeping）
- **Part II Approximate Solution Methods (9-13)**：
  - 第 9-10 章 On-policy & Off-policy Prediction with Approximation
  - 第 11 章 Off-policy Methods with Approximation（deadly triad）
  - 第 12 章 Eligibility Traces（TD(λ)）
  - 第 13 章 Policy Gradient Methods（REINFORCE、actor-critic）
- **Part III Looking Deeper (14-17)**：psychology、neuroscience、applications、frontiers

### TL;DR (≤120字)
Sutton-Barto 是 RL 聖經，MIT 出版 + 作者免費放網上。從 bandit → MDP → DP → MC → TD → policy gradient 漸進；第 13 章 policy gradient 是 AlphaGo/ChatGPT RLHF 的源頭。對交易者的價值：交易 = 連續決策問題 = RL 定義域。第 2 章 bandit 對應 A/B test 策略選擇；第 13 章 policy gradient 直接可做「動態倉位分配」。但 RL for trading 有獨特陷阱（non-stationary, overfitting）。

### 核心本質 (3-5 條)
1. **MDP (Markov Decision Process) = RL 的數學框架（本質，第 3 章）** — 5-tuple (S, A, P, R, γ)；state、action、transition prob、reward、discount factor。Bellman equation v(s) = Σ π(a|s) Σ p(s',r|s,a)[r + γv(s')] 是核心遞迴。
2. **TD learning = DP + MC 的混合（本質，第 6 章）** — TD update: V(s_t) ← V(s_t) + α[r + γV(s_{t+1}) - V(s_t)]；比 MC 少等 episode 結束、比 DP 無需模型。SARSA、Q-learning 皆 TD 變種。
3. **On-policy vs off-policy 的差異（本質，第 5-6 章）** — On-policy (SARSA): 用當前 policy 收集資料 + 更新；Off-policy (Q-learning): 用任意 policy 收集、更新最優 policy。交易中 off-policy 允許 replay buffer 重用舊資料。
4. **Deadly triad: bootstrapping + off-policy + function approximation（本質，第 11 章）** — 這三者同時啟用 → 可能發散（非收斂）；Q-learning + NN = 可能爆炸。DQN (Mnih 2015) 用 target network + replay buffer 才穩住。
5. **Policy gradient 直接優化 policy（本質，第 13 章）** — ∇J(θ) = E[Σ ∇log π_θ(a|s) × Q(s,a)]；REINFORCE、actor-critic、PPO、TRPO 皆此家族。對連續 action（持倉比例）優於 value-based。

### 可用戰術/策略
- **Contextual bandit for strategy selection**：context = market regime，arms = 5 個策略，reward = daily PnL；LinUCB 或 Thompson sampling 動態選策略。
- **DQN for entry timing**：state = 近期價量特徵，action = {buy, hold, sell}，reward = next-period return。注意 reward shaping（log return vs raw）。
- **PPO for position sizing**：continuous action space = position weight ∈ [-1, 1]；PPO 的 clip 避免 policy 突變。
- **Replay buffer + target network**：DQN 核心技巧；對 high-variance 金融 reward 尤其有效。
- **Risk-sensitive RL**：reward 包含 -λ × variance(return)；或用 CVaR RL 優化 tail。

### 盲點 / 反例 / 適用邊界
- **RL for trading 獨有陷阱**：non-stationarity（市場演化）、overfitting（exploit 歷史）、reward misspec（sharpe vs raw return）；直接套 Sutton-Barto 常失敗。
- **Sample efficiency 差**：RL 需海量 episode；金融歷史 20 年日線 = 5000 days，遠不足 DQN 所需 millions。
- **Simulator 不可得**：trading market 非像 Atari 可重跑；真實 live trading 樣本極貴。
- **Action space curse**：多資產組合 action space 爆炸；需 hierarchical RL 或 action decomposition。
- **Policy 最優 ≠ Sharpe 最優**：默認 reward = return，但交易者要 Sharpe；需自訂 reward function。

### 與 Edward 既有知識的連結
- **對齊 ZP adaptive allocation**：將多策略 allocation 視為 RL bandit / contextual bandit；context = 當前 regime、reward = sharpe。
- **延伸 Goodfellow DL + Murphy ML**：RL 的 function approximation 建立於 DL；讀完 Goodfellow 再看 Sutton 13-17 章深度 RL 更順。
- **衝突點**：Sutton-Barto 假設 stationary MDP；金融 market 非 stationary；需 meta-RL 或 online adaptation。
- **可挖金礦**：第 2 章 bandit 演算法可直接實作成 ZP strategy selector（UCB1、Thompson sampling 各 20 行碼）。
- **對接 Deep RL (Silver courses)**：Sutton-Barto 第 2 版加 DL 章節但不深；深度 RL 需 Silver UCL 課 + Spinning Up OpenAI 資源。
