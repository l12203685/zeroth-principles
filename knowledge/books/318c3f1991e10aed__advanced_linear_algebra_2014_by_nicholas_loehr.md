## Advanced Linear Algebra, 2014 — Nicholas Loehr
**來源**: E:/書籍/Advanced Linear Algebra, 2014, by Nicholas Loehr.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Front Cover**
- **Part I: Background on Algebraic Structures**
  - 1. Overview of Algebraic Systems
  - 2. Permutations
  - 3. Polynomials
- **Part II: Matrices**
  - 4. Basic Matrix Operations
  - 5. Determinants via Calculations
  - 6. Concrete vs. Abstract Linear Algebra
- **Part III: Matrices with Special Structure**
  - 7. Hermitian, Positive Definite, Unitary, and Normal Matrices
  - 8. Jordan Canonical Forms
  - 9. Matrix Factorizations
  - 10. Iterative Algorithms in Numerical Linear Algebra
- **Part IV: The Interplay of Geometry and Linear Algebra**
  - 11. Affine Geometry and Convexity
  - 12. Ruler and Compass Constructions
  - 13. Dual Spaces and Bilinear Forms
  - 14. Metric Spaces and Hilbert Spaces
- **Part V: Modules, Independence, and Classification Theorems**
  - 15. Finitely Generated Commutative Groups
  - 16. Axiomatic Approach to Independence, Bases, and Dimension
  - 17. Elements of Module Theory
  - 18. Principal Ideal Domains, Modules over PIDs, and Canonical Forms
- **Part VI: Universal Mapping Properties and Multilinear Algebra**
  - 19. Introduction to Universal Mapping Properties
  - 20. Universal Mapping Problems in Multilinear Algebra
- **Appendix: Basic Definitions**
- **Further Reading**

### TL;DR (≤120字)
本書屬於 statistics evidence based 範疇,作者 Nicholas Loehr 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **多次檢驗問題會偽造 alpha** — data mining 若不做 Bonferroni/BH 校正,幾乎任何「策略」都能在歷史上跑贏
2. **統計顯著 ≠ 經濟顯著** — t-stat 3.0 但年化超額 0.3% 在扣手續費後無法存活
3. **前瞻偏誤 (look-ahead bias) 在學術論文與商業回測都普遍** — 特別留意財報日、指數調整日的訊號重建

### 可用戰術/策略

- 採用 white's reality check / stepwise superior predictive ability 做多重檢驗修正
- 所有 backtest 引入交易成本、滑價、融資成本,再看 net Sharpe

### 盲點 / 反例 / 適用邊界

- 統計檢驗預設資料獨立,金融時序高度相關,block bootstrap / stationary bootstrap 才能貼近實際分布

### 與 Edward 既有知識的連結

- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
