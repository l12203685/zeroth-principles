# Building Winning Algorithmic Trading Systems — Kevin J. Davey

### 目錄
1. 核心本質 — 系統交易的流程化：從想法到 live 全流程
2. 可用戰術 — Walk-Forward、Monte Carlo、Incubation、Position Sizing
3. 盲點/反例 — 個人交易員視角對機構規模的侷限
4. 與 Edward 既有知識的連結

### TL;DR
Davey (Wiley Trading 2014, 25 章 + 3 附錄) 是 World Cup Futures Trading 三連冠（148%、107%、112% annual return）獨立交易員的實戰紀錄。**結構**：Part I 作者自傳（Ch 1-4，從航太工程師轉行、早期虧損、World Cup 冠軍心路）、Part II 系統測試（Ch 5-8 如何 evaluate 策略）、Part III 策略開發（Ch 9-17，含 trading idea → data → testing → walk-forward → Monte Carlo → diversification → position sizing）、Part IV 實作案例（Ch 18-19 Euro Night/Day 實策略）、Part V go-live 前檢核（Ch 20-22 帳戶、心理、雜項）、Part VI 活單監控（Ch 23-24）、Part VII Cautionary Tales（Ch 25 過往犯錯）。附錄給 TradeStation EasyLanguage 完整 source code。**核心立場**：獨立 retail trader 建立 algorithmic 策略的最大風險不是 idea 差，而是**自欺偏差**（optimization bias、curve fitting、overfitting）——他全書反覆強調 walk-forward + Monte Carlo + incubation 三層檢驗，90% 看似賺錢的策略在這套框架下會被淘汰。

### 核心本質
1. **Walk-Forward Analysis 是避免 overfitting 的關鍵（Ch 13）**：Davey 的標準流程——(a) 用前 70% 資料 optimize 參數、(b) 鎖定參數後在接下來 15% 做 validation，(c) 往前滑動視窗重複。若策略在多個 walk-forward window 中都能賺，代表參數不是偶然適配單一時期。對比 single in-sample optimization，walk-forward 能把「看似 150% 回報的策略」篩成「realistic 15% 回報」，差距就是 overfitting penalty。
2. **Monte Carlo Simulation 揭露 trade path 風險（Ch 14）**：拿到一組歷史 trades 後，重新打亂順序生成 1000 條 equity curve。若原始順序的 max drawdown 是 20%，Monte Carlo 顯示 95% confidence interval 可能是 10-40%——真實 live 可能遇到的 drawdown 遠大於回測那條路徑。position sizing 要依 MC 上緣 drawdown 決定，而非 historical。
3. **Incubation Period——強制冷卻期（Ch 14, Ch 19）**：即使通過 walk-forward + MC，策略仍需「養 3-6 個月」模擬或小倉位 live 運作，觀察是否繼續有效。Davey 自述他有多個「通過所有測試但上 live 就敗」的案例——唯一解釋是 market regime 變了而回測沒覆蓋到。Incubation 是最後一道防線。
4. **Position Sizing 決定破產機率（Ch 16, Ch 20）**：Davey 引用 Ralph Vince 的 optimal f 與 fixed fractional sizing。關鍵觀察——有 edge 的策略仍會因 over-sizing 破產；30% edge 的策略用 Kelly 全比例會在 5% 機率下破產。Davey 實務建議用 Kelly 的 1/4 到 1/2 作 fractional size，兼顧獲利速度與 drawdown 可承受性。
5. **Diversification across Uncorrelated Systems（Ch 15）**：Davey 同時 run 10-20 個策略，跨資產（futures、ETF）、跨時間框架（intraday、swing、trend）。系統間 correlation <0.3 時整體 equity curve 比單系統平滑 2-3x。但他警告「correlation 0.3 in 平時 = 0.9 in crisis」——2015 CHF unpeg、2020 Mar 時所有 trend-following system 同時 drawdown。

### 可用戰術
1. **Strategy Development 六階段流程（Ch 9-17）**：(1) Idea (有經濟直覺的 hypothesis)、(2) Limited Testing (先看是否值得深挖)、(3) In-depth testing + walk-forward、(4) Monte Carlo、(5) Incubation、(6) Live small。每階段有明確 go/no-go 準則，避免 emotional attachment。
2. **In-Sample / Out-of-Sample 4:1 split**：1980-2014 的 34 年資料，前 27 年做 optimization，留 7 年完全不看作 final validation。若 IS Sharpe 1.5 但 OOS Sharpe 0.3 = overfitting；OOS Sharpe >60% of IS = 健康策略。
3. **Easy Language Source Code 範例（Appendix B, C）**：Euro Night 策略（21:00 EST 方向性 bet overnight，profit target + stop loss）、Euro Day 策略（10:00 EST breakout），完整 TradeStation code 可直接移植。這是少有的 retail 級別完整 code 公開，對初學者幫助極大。
4. **Real-Time Monitoring（Ch 23-24）**：生 strategy 後每週檢查三個指標——(a) rolling 3-month Sharpe 是否 >0、(b) equity curve 與歷史 Monte Carlo band 是否在 2σ 內、(c) 平均 trade profit 是否 consistent with backtest。任何一項連續 2 月異常即 re-evaluate。
5. **Monkey Trading Benchmark（Appendix A）**：隨機進出場的「猴子策略」當 baseline——若你的策略 long-term Sharpe 低於猴子（~0），根本沒 edge。看似廢話但 Davey 指出 >50% 的 retail 策略實際表現不如隨機。

### 盲點/反例
1. **個人交易員視角，不適合 institutional scale**：Davey 的策略都是 1-5 contracts 規模，沒 market impact；一旦放大到 500 contracts 或機構 portfolio size，slippage 與 execution 成本會吃掉大部分 edge。對 institutional 要補 Kissell《Science of Algo Trading》（本輪）。
2. **心理管理章節偏成功偏差（Ch 21）**：Davey 描述的都是「我贏三次 World Cup」經驗，沒深入處理 90% 失敗者的心理。真正的 losing trader 心理學應看 Van Tharp《Trade Your Way to Financial Freedom》或 Mark Douglas《Trading in the Zone》（Round 1 已讀 Psychology of Money）。
3. **Futures Focus 偏窄**：全書幾乎只談 futures (CL、ZN、ZC、ES、6E)，沒涵蓋 equity options、FX spot、crypto。Futures 的 trend-following 特性在其他 asset class 有變化——equity 的 mean-reversion 傾向更強。
4. **TradeStation EasyLanguage 過時**：2014 出版時 TS 仍流行，2020+ 已被 TradingView Pine Script、Python QuantConnect、Zipline 取代。讀者要把 code port 到現代平台。
5. **沒 Machine Learning / AI 成分**：整本書停在 classical trend-following + breakout logic。Davey 後來（2018+）的新書《Building Trading Systems with the World Cup Advisor》略補 ML，但此書仍純規則式。

### 與 Edward 既有知識的連結
- **對照 Faith《Way of the Turtle》（Round 1）**：Faith 是 Turtle 隊員視角，Davey 是獨立 retail trader 視角；兩人都強調 mechanical rule + position sizing + 心理紀律。Faith 給歷史典故（Dennis-Eckhardt training），Davey 給現代 algo 實作步驟。
- **對照 Elder《New Trading for a Living》（Round 1）**：Elder 偏 discretionary trading（用 technical indicator 手動判斷），Davey 偏 systematic algo（完全規則化）。兩人對 risk management 原則相通但執行方式完全不同。
- **對照 Vince《Handbook of Portfolio Mathematics》（Round 1）**：Davey Ch 16 position sizing 直接引用 Vince 的 optimal f 與 Kelly criterion。Vince 給數學根基，Davey 給實務應用 caveats（用 1/4 Kelly 而非 full）。
- **對照 Kestner《Quantitative Trading Strategies》（Round 1）**：Kestner 側重各種 systematic 策略設計（momentum、breakout、mean-reversion）的數學框架；Davey 側重「如何從想法到上線」的 process management。兩書合在一起是 system trading 的完整 playbook。
- **對照 ZP/backtest 框架**：我 ZP 的 backtest 目前只有 in-sample / out-of-sample split，沒加入 Davey 的 walk-forward + Monte Carlo + incubation 三層檢驗。應該把 incubation phase 正式寫入策略上線 checklist——任何新策略 live money 前必須有 3 個月 paper trading 證明 regime-robust。
- **對照 Poker 的 bankroll management**：Davey 的 position sizing 哲學與撲克 bankroll management 完全同構——100 BB 限注玩 400BB bankroll + 20 buy-in down rule。在 poker 界這叫 conservative；在 trading 界 Davey 的 1/4 Kelly 是同樣邏輯。
