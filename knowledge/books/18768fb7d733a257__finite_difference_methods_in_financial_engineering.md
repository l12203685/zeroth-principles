## Finite Difference Methods in Financial Engineering — 未標示
**來源**: E:/書籍/Finite Difference Methods in Financial Engineering.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **0 Goals of this Book and Global Overview**
  - 0.1 What is this Book?
  - 0.2 Why has this Book Been Written?
  - 0.3 For Whom is this Book Intended?
  - 0.4 Why Should I Read this Book?
  - 0.5 The Structure of this Book
  - 0.6 What this Book Does Not Cover
  - 0.7 Contact, Feedback and More Information
- **Part I The Continuous Theory Of Partial DifferentialI Equations**
  - 1 An Introduction to Ordinary Differential Equations
  - 2 An Introduction to Partial Differential Equations
  - 3 Second-Order Parabolic Differential Equations
  - 4 An Introduction to the Heat Equation in One Dimension
  - 5 An Introduction to the Method of Characteristics
- **Part II FiniteI DifferenceI Methods: The Fundamentals**
  - 6 An Introduction to the Finite Difference Method
  - 7 An Introduction to the Method of Lines
  - 8 General Theory of the Finite Difference Method
  - 9 Finite Difference Schemes for First-Order Partial Differential Equations
  - 10 FDM for the One-Dimensional Convection-Diffusion Equation
  - 11 Exponentially Fitted Finite Difference Schemes
- **Part III Applying FDM to One-Factor Instrument Pricing**
  - 12 Exact Solutions and Explicit Finite Difference Method for One-Factor Models
  - 13 An Introduction to the Trinomial Method
  - 14 Exponentially Fitted Difference Schemes for Barrier Options
  - 15 Advanced Issues in Barrier and Lookback Option Modelling
  - 16 The Meshless (Meshfree) Method in Financial Engineering
  - 17 Extending the Black-Scholes Model: Jump Processes
- **Part IV FDM For Multidimensional Problems**
  - 18 Finite Difference Schemes for Multidimensional Problems
  - 19 An Introduction to Alternating Direction Implicit and Splitting Methods
  - 20 Advanced Operator Splitting Methods: Fractional Steps
  - 21 Modern Splitting Methods
- **Part V Applying FDM to Multi-Factor Instrument Pricing**
  - 22 Options with Stochastic Volatility: The Heston Model
  - 23 Finite Difference Methods for Asian Options and Other 'Mixed' Problems
  - 24 Multi-Asset Options
  - 25 Finite Difference Methods for Fixed-Income Problems
- **Part VI Free and Moving Boundary Value Problems**
  - 26 Background to Free and Moving Boundary Value Problems
  - 27 Numerical Methods for Free Boundary Value Problems: Front-Fixing Methods
  - 28 Viscosity Solutions and Penalty Methods for American Option Problems
  - 29 Variational Formulation of American Option Problems
- **Part VII Design and Implementation In C ++**
  - 30 Finding the Appropriate Finite Difference Schemes for Your Financial Engineering Problem
  - 31 Design and Implementation of First-Order Problems
  - 32 Moving to Black-Scholes
  - 33 C ++Class Hierarchies for One-Factor and Two-Factor Payoffs
- **Appendices**
  - A1 An Introduction to Integral and Partial Integro-Differential Equations
  - A2 An Introduction to the Finite Element Method

### TL;DR (≤120字)
本書屬於 general trading 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **交易的本質是資訊優勢 × 風險控制 × 執行紀律三乘效應** — 缺一無法長存
2. **策略績效 = alpha (訊號) − cost (成本) − drawdown (意外)** — 大部分策略在成本後 alpha 已近零
3. **歷史回測只是假設分布的抽樣,未來樣本外才是真實檢驗**

### 可用戰術/策略

- 建立寫成規則的交易系統,消除情緒干擾
- 追蹤 live 績效 vs backtest 偏差,快速發現模型失效

### 盲點 / 反例 / 適用邊界

- 過度依賴歷史 pattern,市場結構變化 (制度、流動性、參與者結構) 會使策略失效

### 與 Edward 既有知識的連結

- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
