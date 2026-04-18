## An Introduction to Game Theory — Martin J. Osborne（2000）
**來源**: staging/b2_batch_D_extracts/e81b4bd43a26269d__an_introduction_to_game_theory_2000_by_osborne_m_j.md | **消化日**: 2026-04-18 | **模型**: opus-4.7 | **Round**: llm_round_6

### 目錄
- Chapter 1 Introduction（什麼是博弈論、歷史、von Neumann、理性選擇）
- Part I Games with Perfect Information
  - Ch2 Nash Equilibrium Theory（Prisoner's Dilemma、Bach or Stravinsky、Matching Pennies、Stag Hunt、Nash、Best Response、Dominated Actions）
  - Ch3 Nash Equilibrium Illustrations（Cournot / Bertrand Oligopoly、Electoral Competition、War of Attrition、Auctions、Accident Law）
  - Ch4 Mixed Strategy Equilibrium（混合策略、報警悖論、期望效用）
  - Ch5 Extensive Games: Theory（Subgame Perfect、Backward Induction、Tic-tac-toe / Chess）
  - Ch6 Extensive Games: Illustrations（Ultimatum / Holdup、Stackelberg、Buying Votes、A Race）
  - Ch7 Extensive Games: Extensions（同步行動、選舉多回合競爭）
- Part II-IV（非本擷取涵蓋）Bayesian Games, Imperfect Information, Coalitional Games, Bargaining, Matching

### TL;DR (≤120字)
Osborne 是本科至碩士階段最廣泛使用的博弈論教科書。**核心邏輯鏈**：策略型博弈 → Nash Equilibrium → Extensive-form + Subgame Perfect → Mixed Strategies → Bayesian Games。書的特色是大量具體案例（拍賣、選舉、公司寡占、事故法）將抽象概念落地。對交易者而言，本書提供的思維工具：「你的每一決策不是獨立，是他人決策的響應 + 他人對你決策的響應」，這是市場微結構與 game-theoretic 訂單流的理論底座。

### 核心本質 (3-5 條)
1. **Nash Equilibrium 的本質是「最佳回應的不動點」**（本質，Ch2） — 策略組合 (s₁\*, s₂\*) 是 Nash 若且唯若：每個玩家的 s\* 是其他人 s\* 的最佳回應。換言之，無人單方面偏離可獲利。這看似平凡的定義帶來深刻結果：(a) 均衡可能多個、(b) 可能無均衡（需混合策略）、(c) 均衡未必 Pareto 最優（Prisoner's Dilemma 就是反例）。
2. **Prisoner's Dilemma：為何理性導致集體次優**（本質，Ch2.2） — 兩囚犯個人最佳是「背叛」（dominant strategy），但雙方都背叛結果比雙方合作差。這是博弈論最著名的悖論，解釋了公共財、氣候變化、核武競賽、加密交易所流動性碎片化等現象。
3. **Mixed Strategy = 無 pure 均衡時的隨機化**（本質，Ch4） — Matching Pennies 沒有 pure Nash；唯一 Nash 是雙方各以 50/50 隨機出 H/T。關鍵原理：混合策略是為了讓對手**無法利用你的可預測性**。撲克的 GTO（Game Theory Optimal）策略即建立在此。
4. **Backward Induction + Subgame Perfect**（本質，Ch5） — 連續博弈（如談判、棋局）從終局向回推：每個子博弈都達到均衡。這排除了「不可信威脅」——例如母親說「不乖就殺了你」，但到了真的時候她不會殺；所以 subgame perfect 要求威脅是可信的（credible）。
5. **Ultimatum Game: 理論 vs 實驗**（本質，Ch6.2） — 100 元分配：提議者給 A、接受者可接受或雙方歸零。理論：任何 A > 0 都應被接受，故提議者可給 $1。實驗：接受者常拒絕 < 30% 的提議，偏好公平。顯示人類不是純粹期望效用最大化者，有「負效用+報復動機」——這是行為經濟學起點。

### 可用戰術/策略
- **Cournot / Bertrand 模型**：Cournot（量競爭）均衡利潤 > 0、價格 > MC；Bertrand（價競爭）均衡趨向 P = MC、零利潤。應用：產業分析時判斷競爭者以量還是價決策，結果天壤之別。
- **Best Response Function**：固定對手策略，畫出自己最佳回應曲線；兩條曲線交點 = Nash 均衡。實用工具，適用於有限選項決策分析。
- **Auction 設計四種**：First-Price Sealed、Second-Price (Vickrey)、English（公開上漲）、Dutch（公開下降）。Vickrey auction 達致誠實出價 dominant strategy——對於制定拍賣規則極重要。
- **Mixed Strategy 計算**：對手對自己 pure strategies 無偏好（期望報酬相等），即為混合均衡；求解公式是對手在每個策略下自己的期望報酬相等。撲克下注頻率分析的基礎。
- **War of Attrition**：雙方競爭一個獎金，每單位時間支付成本；獨特的混合均衡是指數分布退出時間。應用：IPO 等待期、談判僵持、營業模式競爭。

### 盲點 / 反例 / 適用邊界
- **完美理性假設**：所有玩家被假設完全理性 + 完美計算；真實決策者受限於認知資源、情緒、偏誤（Kahneman）。
- **均衡選擇問題**：多個均衡時，理論無法告訴你哪個會被玩成。Schelling 的 focal point 理論補充此缺口。
- **信息結構假設**：Osborne 基礎版假設完美信息；現實多為不完全信息，需 Bayesian Games（Harsanyi，本書後半章節）。
- **靜態 vs 動態**：教材以一次性均衡為主；重複博弈（Folk Theorem、聲譽機制）與演化博弈（Maynard Smith）需額外學習。
- **實驗結果常違反理論**：Ultimatum、Public Goods、Dictator Game 等實驗顯示人類有 fairness、reciprocity 等行為動機，純理論無法解釋。

### 與 Edward 既有知識的連結
- **對齊 ZP 零式本質**：博弈論框架讓 Edward 理解「市場不是單獨的分布，而是多玩家策略互動的均衡結果」；這是真正的零式思維起點。
- **對接撲克 DNA §9**：撲克是 imperfect-information extensive game；GTO 策略直接建立在 Nash Equilibrium 概念上；Edward 可直接遷移。
- **延伸 Speculators Poker 18 years（llm_round_5 已消化）**：該書用撲克比喻市場；Osborne 提供數學化框架，讓比喻變成精確工具。
- **衝突點**：市場不是封閉博弈——有隨機事件、流動性衝擊、HFT 等外生因素；純博弈分析需配合機率模型與 regime detection。
- **可挖金礦**：Ch4 Mixed Strategies 對訂單流偽裝（冰山單、TWAP 拆單對抗機器人）有直接應用；Ch6 Ultimatum 對 M&A、併購溢價談判有應用。建議整合入 ZP/microstructure/game_theory_applied.md。
