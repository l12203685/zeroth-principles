## Modeling Derivatives in C++ (Wiley Finance 038) — Justin London
**來源**: E:/書籍/(Wiley Finance 038)Modeling Derivatives in C++.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **Ch 1-2** Options Fundamentals & BS Foundation
- **Ch 3** Monte Carlo Simulation (Box-Muller、polar rejection、Halton/Sobol quasi-MC)
- **Ch 4-5** Binomial / Trinomial Trees
- **Ch 6** Finite Difference Methods (explicit/implicit/Crank-Nicolson)
- **Ch 7** Exotic Options (Asian, Barrier, Lookback, Chooser)
- **Ch 8** Stochastic Volatility Models (Heston, SABR)
- **Ch 9** Stochastic Multi-Factor Models
- **Ch 10** Single-Factor Interest Rate Models (Vasicek, CIR, Hull-White)
- **Ch 11** Tree-Building for Short Rate
- **Ch 12** Two-Factor / Multi-Factor IR Models (Hull-White 2F、G2++)
- **Ch 13** LIBOR Market Models (LFM)
- **Ch 14** Bermudan & Exotic IR Derivatives (Longstaff-Schwartz, Stochastic Mesh)
- **Appendix A** Probability Review
- **Appendix B** Stochastic Calculus Review (Brownian, Itô, SDE, GBM)
- **Appendix C** Numerical Linear Algebra
- **Appendix D** Code snippets library

### TL;DR (≤120字)
專為 derivatives quant developer 寫的 C++ 實作手冊:把 BS / binomial / trinomial / FD / MC / Heston / LIBOR market model 等全部給完整可編譯 C++ 程式碼。強在「從公式到可跑的程式」的 gap-closing,是 bank/hedge-fund quant dev 的 cookbook。

### 核心本質 (3-5 條, 每條 50-120字)
1. **Pricing 演算法選型是精度 vs 速度 vs 適用場景的三維權衡** — Binomial tree 適合 simple vanilla + American;FD 適合 PDE-based exotics;MC 適合 path-dependent + high-dimensional;Heston analytic 適合 vanilla + smile。沒有單一 "最好",只有 "對當前場景最好"。
2. **隨機數生成的品質直接影響定價精度** — Ch3 詳述 Box-Muller vs polar rejection;Sobol / Halton 低偏差序列可使 MC 收斂從 O(N^-0.5) 提升到近 O(N^-1)。低品質 RNG (e.g., rand()) 會使 MC estimate 有系統偏差,這是初學者常犯的 subtle bug。
3. **LIBOR Market Model (LFM) 是 fixed income exotic 的 workhorse** — Ch13 完整實作:把 forward rates 建為 lognormal semi-martingale,可校準到 caplet & swaption 市場 prices 。Bermudan swaption、Range note、Quanto 等複雜 IR 衍生品都以此為定價引擎。
4. **Calibration 是每個 pricing model 的生死門** — Ch10-13 反覆強調:模型不校準市場 prices,給的 Greeks 和 hedging ratios 全錯。Hull-White、LFM 等都需先 calibrate to caps/swaptions,然後才能定價 exotic。誤差最小化通常用 Levenberg-Marquardt / simplex。
5. **Longstaff-Schwartz regression (Ch14) 是 American-style exotic 的 breakthrough** — 2001 年 LS 方法把 backward induction 的 continuation value 用多項式回歸估計,使 high-dim American options (Bermudan swaption、American Asian) 可用 MC 定價。至今仍是業界標準。

### 可用戰術/策略
- **建立 B1 交易系統的自家 pricing engine** — 從 BS + binomial 開始,逐步擴展到 FD / MC / Heston;每個 pricing function 都有對應 analytic benchmark 做 regression test。參考本書的 class hierarchy 設計(Option → European/American → Vanilla/Exotic)作為 C++/Python 架構起點。
- **Sobol/Halton quasi-MC 作為回測路徑生成的標配** — 純 pseudo-random MC 收斂慢、variance 高;用 Sobol 使 simulate 100K paths 的結果接近 pseudo-MC 1M paths。B1 回測若需大量 stress scenarios,quasi-MC 是 10x 速度提升。
- **Crank-Nicolson 作為 vanilla option 定價默認 solver** — 精度 O(Δt² + Δx²),比 explicit 穩定 + 比 implicit 精度高;對 European / barrier / simple American 都適用。實作 100-200 行 Python 完成。
- **Heston 模型 quick calibrator** — 用市場 ATM + skew + kurtosis 反求 (v₀, κ, θ, σ, ρ) 五參數;可快速重現市場 smile 並算 "market-consistent" Greeks。
- **Longstaff-Schwartz 實作作為 American exotic 定價 template** — 給定 payoff 函數與 basis functions (Laguerre polynomials, monomials),反推 optimal exercise boundary,算 expected discounted payoff。

### 盲點 / 反例 / 適用邊界
- **C++ 是 sell-side bank 主流,buy-side 更多 Python/Julia** — 程式碼需 port 到 Python 或 Rust;此書的 C++ 品質適中(2005 年版,缺 modern C++17+ idioms)。port 時可一併重構為 modern。
- **假設 OIS discounting 前的 LIBOR 世界** — 2010 後 multi-curve framework (OIS discount + LIBOR forecasting) 成主流;本書仍單曲線 — 需讀 Brigo-Morini-Pallavicini《Counterparty Risk》或 Henrard《Interest Rate Modelling after the Financial Crisis》補。
- **未涵蓋 XVA (CVA/DVA/FVA/KVA)** — 2008 後 counterparty credit adjustment 成定價必備;本書只做 pre-XVA pricing。
- **無 ML-based pricing (Deep-Hedging、Neural SDE)** — 2020+ 新興技術未涵蓋;需讀 Buehler《Deep Hedging》等 recent papers。

### 與 Edward 既有知識的連結
- 補完 Hull 與 Shiryaev:Hull 給觀念,Shiryaev 給嚴謹證明,此書給可編譯的程式碼。quant dev 學習鏈:Hull → Shiryaev → Modeling Derivatives in C++ → 自己的實作。
- 對應 `backtest_methodology`:Ch3 的 MC + quasi-MC 是回測路徑生成的底層;理解 convergence rate 才能判斷 backtest 結果的可信度。
- 連結 Wilmott FAQ Q31-33 (numerical methods):Wilmott 介紹 when to use which,此書教 how to implement each。
- 對 B1 自營交易系統的貢獻:若擴充到 exotic option strategy (barrier、Asian、range note),本書的 pricing code 可作為 Python port 起點;Longstaff-Schwartz 可立即應用於動態退場時機優化(策略本身 = American option)。
