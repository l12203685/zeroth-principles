## A New Interpretation of Information Rate — John L. Kelly, Jr.（1956，Bell System Technical Journal）
**來源**: staging/b2_batch_D_extracts/96373306921809f5__a_new_interpretation_of_information_rate_kelly.md（extract 空白，本 digest 基於原論文與 Fortune's Formula, Thorp, MacLean-Ziemba 所有覆蓋） | **消化日**: 2026-04-18 | **模型**: opus-4.7 | **Round**: llm_round_6

### 目錄
- Abstract
- §1 Introduction（Shannon 1948 資訊理論複習）
- §2 Basic Model（賭馬系統 + 私有電報、均衡賠率）
- §3 Gambling with Private Wire（有私人訊息時下注策略）
- §4 Formula Derivation（f\* = p(1+b) - 1 / b）
- §5 Relationship to Information Rate（Kelly 準則 = Shannon 通道容量的經濟解釋）
- §6 Reinvestment with Fixed Odds
- §7 Examples with Discrete Information
- §8 Generalization to Multiple Outcomes

### TL;DR (≤120字)
Kelly 1956 這篇 8 頁短論文改變了賭博、投資、資訊理論三個領域。**核心洞見**：如果你有一定 edge（p > 均衡賠率），最大化 E[log(wealth_N)] 的最優下注比例是 f\* = (bp - q) / b，其中 p = 勝率、q=1-p、b = 賠率。此公式有驚人性質：**使長期複合增長率 G = p × log(1+b×f\*) + q × log(1-f\*) 最大化**，且 G 在數學上等於 Shannon 的「通道資訊傳輸速率」——首次將資訊理論與財務最大化連結。

### 核心本質 (3-5 條)
1. **問題起源：私人電報的賭馬**（本質，§2） — Kelly 設定：一個賭徒可從私人電報得知賽馬結果（但訊號有噪音——準確率 p < 1）；他的下注應如何最大化長期財富？這個看似賭博的問題，實際上是「在訊號帶有噪音的情況下如何最佳利用資訊」。
2. **公式推導：最大化 E[log W]**（本質，§4） — 假設每期下注比例 f，勝率 p（贏時獲 b×f）、輸率 q=1-p（輸時損 f）。N 期後財富 W_N = W_0 × Π(1+b×f)^{勝次} × (1-f)^{輸次}。取對數後由大數定律，E[log(W_N/W_0)] / N = p×log(1+bf) + q×log(1-f)。對 f 求導令為零：f\* = (bp-q)/b。
3. **Kelly = Shannon's Channel Capacity**（本質，§5） — 令 R = p×log(1+bf\*) + q×log(1-f\*) = 最大幾何增長率。Kelly 證明：**R = C**，即 Shannon 通道容量。這意味著「你能從私人訊息榨取的最大財富增長率 = 訊息的資訊容量」。這是資訊理論與財務的第一個深刻橋樑。
4. **平均算術成長率 vs 幾何成長率**（本質，§2, §4） — 關鍵區別：E[W_N] 最大化下注是 all-in（若 E>0 即下注全部）；但 E[W_N] 高不代表 median(W_N) 高。E[log W_N] 最大化保證「幾乎必然」長期領先。這是 Samuelson-Thorp 爭論的核心。
5. **Overbetting 災難**（本質，§4 推論） — 若 f > 2f\*（兩倍 Kelly），則長期幾何增長率變為**負數**（即長期必破產）。f = f\* 是激進臨界點；Thorp 與 Vince 都因此主張 Fractional Kelly（0.25-0.5 × f\*）。

### 可用戰術/策略
- **經典 Kelly 公式**：f\* = (bp - q) / b，其中 b 是賠率比（贏 b 元 / 輸 1 元），p = 勝率。
- **連續收益版本**：若收益連續分佈（如股票），f\* = (μ - r) / σ²（Merton 1969 推廣）。
- **多結果 Kelly**（§8 推廣）：對於 n 個互斥結果、各有機率 p_i 與賠率 b_i，解 maximize Σ p_i × log(1 + f_i × b_i) subject to Σ f_i ≤ 1。
- **Half-Kelly 實務做法**：Thorp 在 Princeton-Newport 用 f = 0.5 × f\*。理論代價：幾何增長率降至 75% Full Kelly；收穫：波動率降約 50%，心理壓力顯著降低。
- **Kelly 用於 Sharpe Ratio**：若策略 Sharpe = S（以年化計），最佳槓桿 f\* ≈ S / σ。例：Sharpe 1.0 + vol 15% → f\* ≈ 6.67（相當 7x 槓桿）——這對多數投資者不可承受。

### 盲點 / 反例 / 適用邊界
- **需要已知 p、b**：Kelly 假設機率已知。現實中 p 是估計值，誤差放大會致災難。Thorp：若 p 高估 2x，實用 Full Kelly = 快速破產。
- **獨立、相同、重複下注**：公式假設下注獨立且可重複；現實中連續交易有相關性、交易成本、流動性等約束。
- **單期 vs 多期**：Samuelson 指出若投資者只關心單期效用（非 log），Kelly 未必最優。但對長期複合者，Kelly 幾乎必然勝出。
- **Drawdown 心理**：Full Kelly 對應 50% drawdown 機率接近 1，多數人無法執行。Ziemba、Thorp 均強調 Half-Kelly 是實用下限。
- **Competitive Games 例外**：Kelly 假設賠率固定；在撲克、撲克式金融市場，賠率隨對手調整變動，需要 game-theoretic 修正。

### 與 Edward 既有知識的連結
- **對齊 ZP 零式本質**：Kelly 公式 = 「最大化長期複合增長 subject to 不破產」的數學回答；與 Edward 的「經濟自給 + 永續」完全對應。
- **對接 Fortune's Formula（llm_round_6）**：Poundstone 講 Kelly 的歷史敘事；本論文是數學本源。
- **對接 Handbook of Portfolio Mathematics（llm_round_6）**：Vince 的 Optimal f 是 Kelly 在真實 PnL 分佈的推廣；Kelly 是理論原點。
- **延伸 Kelly Capital Growth（MacLean-Thorp-Ziemba）**：這是 Kelly 準則 50 年文獻的總結集，本論文是根。
- **衝突點**：主流 MPT（Markowitz）與 Kelly 有內在張力；MPT 以 E-V 為準則（二階近似），Kelly 以 E[log] 為準則（長期精確）。Edward 若選 Kelly 路線，要自覺於此哲學分野。
- **可挖金礦**：Kelly ↔ Shannon 容量的 isomorphism 是 ZP/meta_theory/ 的深層結構洞見；可整合入 information_and_wealth.md 探討資訊經濟的本質。
