## level_i_mock_exam_morning_questions_and_answers — 未標示
**來源**: E:/課程/CFA Level1 Mock exam/CFA Mock exam/2009/level_i_mock_exam_morning_questions_and_answers.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **2009 Level I Mock Exam: Morning Session**
- **Time**
- **A 270-day U.S. Treasury bill with a face value of $100,000 sells for $96,500 when issued. Assuming an investor holds the bill to maturity, the investor's money market yield is closest to:**
- **A. 3.63%.**
- **The portfolio's mean absolute deviation for the five-year period is closest to:**
- **If the risk-free rate of return is 4.25 percent, then the coefficient of variation is closest to:**
- **0.52.**
- **47.27%.**
- **$8,133.**
- **Current Liabilities**
- **"Long-Lived Assets," R. Elaine Henry, CFA and Elizabeth Gordon**
- **2009 Modular Level I, Volume 3, pp.340-341**
  - "Long-term Liabilities and Leases," Elizabeth Gordon and R. Elaine Henry, CFA
- **Expected return on the market**
- **2009 Modular Level I, Volume 6, pp. 90-93**
- **Study Session 17-70-d**
- **Define interest rate caps, and floors, and collars.**
- **2009 Modular Level I, Volume 6, pp. 130-141**
- **$96.**
- **2009 Modular Level I, Volume 6, pp. 55-60**
- **2009 Modular Level I, Volume 6, pp. 32-33**
- **A European bank wants to short a 1x3 forward rate agreement on Euribor. A dealer provides the bank with a quote of 1.75 percent. The bank agrees to enter the FRA with the dealer. At contract maturity, what Euribor rate would most likely result in t...**
- **60-day Euribor at 1.70%**
- **60-day Euribor at 1.80%**
- **90-day Euribor at 1.65%**
- **Answer: A**
- **"Forward Markets and Contracts," Don M. Chance**
- **2009 Modular Level I, Volume 6, pp. 38-41**
- **Study Session 17-68-g**
- **Calculate and interpret the payoff of an FRA and explain each of the component terms.**
- **According to put-call parity, a synthetic put contains a:**
- **long position in the call.**
- **long position in the underlying.**
- **short position in the risk-free bond.**
- **Answer: A**
- **"Option Markets and Contracts," Don M. Chance**
- **2009 Modular Level I, Volume 6, pp. 108-110**
- **Study Session 17-70-j**
- **Explain put-call parity for European options, and relate put-call parity to arbitrage and the construction of synthetic options.**

### TL;DR (≤120字)
本書屬於 portfolio optimization 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **MVO (均值變異數最佳化) 對輸入極敏感** — 預期報酬誤差 1% 可導致組合權重 30% 擺動
2. **Black-Litterman 透過混合市場均衡與主觀觀點穩定組合,是實務優於純 MVO 的路徑**
3. **Risk Parity 不需要預期報酬,但隱含假設各資產夏普比接近,槓桿需要嚴格風控**

### 可用戰術/策略

- shrinkage 估計共變矩陣 + 施加 weight bound (每資產 0-20%) 增強 robustness
- 實務上先配置 Risk Parity 底層,再疊加主觀 tactical overlay

### 盲點 / 反例 / 適用邊界

- Low vol 資產在極端事件中 vol 可以瞬間跳升,Risk Parity 高槓桿放大尾險

### 與 Edward 既有知識的連結

- 呼應零式原則 *meta_strategy_over_strategy* — 關注資金曲線與長期夏普、勝過單筆交易或單期回報
- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
