## Accelerated.C++_En — 未標示
**來源**: E:/書籍/Accelerated.C++_En.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **The C++ In-Depth Series**
- **Chapter 0 Getting Started**
  - 0.1 Comments
  - 0.2 #include
  - 0.3 The main function
  - ... (5 more sections)
- **Chapter 1 Working with strings**
  - 1.1 Input
  - 1.2 Framing a name
  - 1.3 Details
- **Chapter 2 Looping and counting**
  - 2.1 The problem
  - 2.2 Overall structure
  - 2.3 Writing an unknown number of rows
  - ... (4 more sections)
- **Chapter 3 Working with batches of data**
  - 3.1 Computing student grades
  - 3.2 Using medians instead of averages
  - 3.3 Details
- **Chapter 4 Organizing programs and data**
  - 4.1 Organizing computations
  - 4.2 Organizing data
  - 4.3 Putting it all together
  - ... (3 more sections)
- **Chapter 5 Using sequential containers and analyzing strings**
  - 5.1 Separating students into categories
  - 5.2 Iterators
  - 5.3 Using iterators instead of indices
  - ... (6 more sections)
- **Chapter 6 Using library algorithms**
  - 6.1 Analyzing strings
  - 6.2 Comparing grading schemes
  - 6.3 Classifying students, revisited
  - ... (2 more sections)
- **Chapter 7 Using associative containers**
  - 7.1 Containers that support efficient look-up
  - 7.2 Counting words
  - 7.3 Generating a cross-reference table
  - ... (3 more sections)
- **Chapter 8 Writing generic functions**
  - 8.1 What is a generic function?
  - 8.2 Data-structure independence
  - 8.3 Input and output iterators
  - ... (2 more sections)
- **Chapter 9 Defining new types**
  - 9.1 Student_info revisited
  - 9.2 Class types
  - 9.3 Protection
  - ... (4 more sections)
- **Chapter 10 Managing memory and low-level data structures**
  - 10.1 Pointers and arrays
  - 10.2 String literals revisited
  - 10.3 Initializing arrays of character pointers
  - ... (4 more sections)
- **Chapter 11 Defining abstract data types**
  - 11.1 The Vec class
  - 11.2 Implementing the Vec class
  - 11.3 Copy control
  - ... (3 more sections)
- **Chapter 12 Making class objects act like values**
  - 12.1 A simple string class
  - 12.2 Automatic conversions
  - 12.3 Str operations
  - ... (4 more sections)
- **Chapter 13 Using inheritance and dynamic binding**
  - 13.1 Inheritance
  - 13.2 Polymorphism and virtual functions
  - 13.3 Using inheritance to solve our problem
  - ... (4 more sections)
- **Chapter 14 Managing memory (almost) automatically**
  - 14.1 Handles that copy their objects
  - 14.2 Reference-counted handles
  - 14.3 Handles that let you decide when to share data
  - ... (2 more sections)
- **Chapter 15 Revisiting character pictures**
  - 15.1 Design
  - 15.2 Implementation
  - 15.3 Details
- **Chapter 16 Where do we go from here?**
  - 16.1 Use the abstractions you have
  - 16.2 Learn more
- **Appendix A Language details**
  - A.1 Declarations
  - A.2 Types
  - A.3 Expressions
  - ... (1 more sections)
- **Appendix B Library summary**
  - B.1 Input-output
  - B.2 Containers and iterators
  - B.3 Algorithms

### TL;DR (≤120字)
本書屬於 algorithmic trading 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **演算法交易的邊際利潤來自執行細節** — 進出場時點、冰山單、VWAP/POV 切片,而非主策略
2. **策略衰退 (alpha decay) 是必然,持續研發管線是本質不是選項** — 單一策略 life cycle 常低於 2-3 年
3. **Latency 不是唯一賽道,穩定性與再現性才是散戶與機構都可 scale 的護城河**

### 可用戰術/策略

- 建立策略標準化介面與回測基建,把每個新策略的研發時間壓到 1-2 週
- 為每個 live 策略設定監控 (PnL/ drawdown/ trade frequency) 觸發自動下線閾值

### 盲點 / 反例 / 適用邊界

- 過度依賴歷史 backtest 而忽略線上資料源穩定性、訊號延遲、交易所規則變更

### 與 Edward 既有知識的連結

- 呼應零式原則 *meta_strategy_over_strategy* — 關注資金曲線與長期夏普、勝過單筆交易或單期回報
- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
