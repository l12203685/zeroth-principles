## A Practical Guide to Quantitative Finance Interviews — Xinfeng Zhou
**來源**: E:/書籍/Xinfeng Zhou-A Practical Guide To Quantitative Finance Interviews-CreateSpace (2008).pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
（PDF bookmarks 質量低，TOC 空；實際章節依據書籍結構推斷）
- Part I: General Principles (interview preparation, communication, problem-solving framework)
- Part II: Brain Teasers（邏輯謎題、鴿籠原理、反證法、歸納法案例）
- Part III: Calculus and Linear Algebra（Taylor、拉格朗日、矩陣分解）
- Part IV: Probability Theory（條件機率、Bayes、Martingale）
- Part V: Stochastic Processes and Stochastic Calculus（Brownian motion、Ito's lemma）
- Part VI: Finance（債券定價、option pricing、portfolio theory、CAPM）
- Part VII: Algorithms and Numerical Methods（二分搜尋、dynamic programming、蒙特卡洛）

### TL;DR (≤120字)
Zhou 的 quant interview bible：不是給答案集，而是示範「面試官要看的思考過程」。內容橫跨 brain teasers、機率、隨機微積分、衍生品定價、數值方法；核心訊息是——quant interview 看的是問題拆解能力與數學素養的交匯，背公式者必敗。

### 核心本質 (3-5 條)
1. **Interview = 思考過程展示**（本質） — Zhou 的解法排版都從「問題簡化」開始（例：5 bags → 2 bags 先解 → 反推），再給最終解。面試官要看的是能否從一般化問題退回最小案例、再用歸納法／對稱性推廣。死背題目答案會在微調後立即失效。
2. **Pigeonhole Principle（鴿籠原理）是 quant 通用工具**（本質） — 螞蟻題（51 隻在單位方形、杯子半徑 1/7）用 5x5 劃分推出 25 格中至少一格有 3 隻；這不是技巧而是離散數學的基本結構。任何「一定存在」的存在性證明問題都應先考慮鴿籠。
3. **Invariant（不變量）方法**（本質） — 變色龍題（13 紅、15 綠、17 藍兩兩相遇變第三色）用 mod 3 不變量證明「永遠無法全部同色」。這是組合數學中的 state-space 簡化技巧，在量化模型中對應守恆量、gauge transformation。
4. **整除性的 base-10 分解技巧**（本質） — 9 的整除規則證明（位數和為 9 倍數 ⟺ 整除 9）利用 10^k − 1 皆可被 9 整除的代數結構；同邏輯延伸到 11（交錯和）。這類技巧在隨機過程裡對應 characteristic function 的分解。
5. **數學素養是 quant 的最低門檻**（本質） — 書中題目不考 finance 知識而考 math 基礎；隱含訊息：面試官假設 finance 可以半年學會，但數學直覺（spatial reasoning, proof intuition, numerical sense）要靠十年訓練。

### 可用戰術/策略
- **面試開場三問**：先問「是否可簡化？是否有對稱性？是否有不變量？」三問涵蓋 80% 的 brain teaser 類型。
- **從 N=2 或 N=3 開始解 general N**：先做最小可解案例，找模式，再猜通式，最後數學歸納法證明。Zhou 的 5-bags 題示範完整流程。
- **Pigeonhole 觸發條件**：任何「至少一個 X 包含 ≥ k 個 Y」的存在性問題，先嘗試鴿籠；尋找 pigeon 數與 hole 數的對應關係。
- **Invariant 工具箱**：mod 運算、奇偶性、著色法（棋盤黑白染色）、勢函數（potential function）。複雜狀態機問題先找不變量。
- **Brain teaser → 實戰交易類比**：鴿籠 = 分散化必要樣本數；Invariant = 套利無風險條件；整除性 = 狀態離散化建模。把 interview 技巧抽象化為實戰思維工具。

### 盲點 / 反例 / 適用邊界
- **缺乏實際業務 context** — 全書聚焦「能解題 = 可僱用」，但實際 quant 工作中更多時間花在數據清洗、infra、溝通而非解題；過度準備 interview 反而錯失實戰技能。
- **已更新多版、2008 版遠遠過時** — 當前 2026 年 quant interview 加入大量 ML、deep learning、systems design 題目；Zhou 2008 版只涵蓋傳統 quant skill set，缺 Python/SQL/coding interview 內容。
- **extraction OCR 品質差** — 此版 extract 因 PDF OCR 問題產生大量拼字錯誤（如 "5o1u'io~"、"cam"→"coin"）；原書 PDF 清晰版應從其他源取得。
- **解題思維 ≠ 研究思維** — interview 題有唯一答案，研究沒有。書中培養的「快速找答案」習慣在研究階段是災難——早期固化方向，錯失更好方法。

### 與 Edward 既有知識的連結
- **對齊 ZP 零式本質**：Zhou 強調的「先簡化、找不變量、歸納推廣」正是零式思維的量化版本；可整理成 `ZP/math/problem_solving/` 的方法論模組。
- **延伸 DNA §9 Hobbies**：Avalon 策略推理需要同樣的狀態機思維（誰知道誰是好人）與 invariant 尋找（某些組合永遠推不出結論）；brain teaser 訓練可直接提升 Avalon 技能。
- **對應 Poker 應用**：鴿籠原理可用於手牌組合數估算、mod 運算可加速 pot odds 心算；EV 計算是 Zhou Part IV 機率論的直接實作。
- **衝突點**：Zhou 的解題思維偏向 clean problem（所有資訊已知、唯一解）；Edward 的交易決策是 noisy problem（資訊不完全、多解並存）。Part I 的 communication 原則需要 adapt。
- **可挖金礦**：Part IV 機率與 Part V 隨機微積分的例題可改寫為 `ZP/quant/exercises/` 的自我訓練題庫，每週做 3-5 題維持數學肌肉。
