## Hedge Fund Market Wizards: How Winning Traders Win — Jack D. Schwager (2012)

**來源**: E:/書籍/Book - Hedge fund market wizards how winning traders win (WILEY 2012).pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄（15 位 hedge fund manager 訪談）
- 第 1 章 Colm O'Shea — global macro（預測危機、但只在 setup 對時下注）
- 第 2 章 Ray Dalio — Bridgewater（all weather、pure alpha 分離）
- 第 3 章 Larry Benedict — S&P 500 期貨 intraday（pattern recognition + scalping）
- 第 4 章 Scott Ramsey — managed futures（trend following + rigorous risk）
- 第 5 章 Jaffray Woodriff — statistical trading（ML factor models）
- 第 6 章 Edward Thorp — Princeton Newport（量化先驅、優勢原則）
- 第 7 章 Jamie Mai — Cornwall Capital（asymmetric bets、Big Short 參與者）
- 第 8 章 Michael Platt — BlueCrest（多策略、risk allocation 系統）
- 第 9 章 Steve Clark — Omni Global（event-driven）
- 第 10 章 Martin Taylor — Nevsky Fund（emerging markets discretionary）
- 第 11 章 Tom Claugus — GMT Capital（long/short equity、fundamental）
- 第 12 章 Joe Vidich — Manalapan（short selling specialist）
- 第 13 章 Kevin Daly — Five Corners（small-cap 深度研究）
- 第 14 章 Joel Greenblatt — Gotham Capital（special situations、value）
- 第 15 章 結論：40 條跨訪談的 meta-lessons

### TL;DR (≤120字)
Schwager 的 Market Wizards 系列第四本，**訪談 15 位不同風格的成功 hedge fund manager**。核心不是抄襲他們的策略（無法複製），而是提煉**跨風格的共同 meta-lessons**：紀律、風險管理、自知之明、持續學習。每位 manager 都是一個 case study，每章末的 lessons 可作為獨立交易員的 checklist。

### 核心本質 (3-5 條)
1. **成功 manager 的共同點是 process，不是 outlook**（本質） — 第 15 章 meta-lesson：15 位 manager 的市場觀點差異極大（Dalio 看 deflation、Benedict 看 intraday noise、Woodriff 只看 statistical pattern），但他們**流程紀律幾乎相同**——明確風險預算、嚴格止損、持續記錄與反思。**過程 > 預測**是 Market Wizards 系列一貫主題。
2. **Risk management 優先於 return optimization**（本質） — 跨 15 位 manager，10+ 位明確表示「保本第一、獲利第二」；Dalio 甚至說「做對事情 vs 做對事情的錯方法，後者更危險」。**大多數失敗交易員試圖最大化報酬，成功交易員最大化「不爆倉」**。這對齊 Sperandeo、Unger、Douglas 的共識。
3. **Asymmetric betting 是多位 manager 的共同武器**（本質） — Thorp、Mai、Clark、Greenblatt 都強調：尋找「輸少贏多」的 setup，即使勝率 < 50%。Mai 在 Big Short 中的 put option 策略：「虧全部保費 vs 賺 100×」在 expected value 為正時值得下注。此概念對應 Nassim Taleb 的「凸性」。
4. **ego kills more traders than bad strategies**（本質） — 多位 manager 強調：承認錯誤的速度 = 生存機率。Clark 說「我每天問自己哪裡可能錯了，而不是哪裡對」；Platt 建立 risk committee 來 override 自己的 conviction。**對錯比金額更 ego-triggering**，不承認錯就會加碼錯誤直到毀滅。
5. **Jaffray Woodriff 是 ML trader 的先驅案例**（本質） — 第 5 章：Woodriff 的 QIM 基金純用 ML factor model（~1000 factors + ensemble），在 2000s 達到 Sharpe 1.5+。關鍵洞察：(1) 單一 factor 的 IC 小但組合可穩定、(2) out-of-sample 測試比 in-sample Sharpe 重要 10×、(3) 每個 factor 有 alpha decay，需持續引入新 factor。這是 Kelly-Xiu《Financial Machine Learning》(Round 1) 的實戰前身。

### 可用戰術/策略
- **process 紀律 checklist**（第 15 章 40 條 meta-lessons 精選 5 條）：(1) 明確 risk per trade、(2) 每日日誌含情緒記錄、(3) 每月 performance attribution、(4) 不超過 3 個策略、(5) drawdown > 預期時停手檢討而非加碼。
- **Dalio risk-parity 概念**：不按資本配置 asset，而按 risk contribution 配置；每個 asset 貢獻相同 variance，降低單一 asset 主導組合的風險。
- **Asymmetric option trading**：尋找 tail event 的 deep OTM put/call（implied vol 被低估時買入）；虧損上限 = 保費，獲利上限 = 10-100× 保費。適合 low-probability, high-payoff 交易。
- **Platt 的 risk budget allocation**：多策略時，對每個策略分配 risk budget（如 VaR limit 1%、stop at 2%），超限自動停手而非加碼；這防止單一策略毀滅整個組合。
- **Ego-check exercise**：每週問「如果 market 反向 10%，我最怕的 5 筆部位是什麼？」；若某部位你強烈不願答（因會揭露錯誤），該部位需減倉。

### 盲點 / 反例 / 適用邊界
- **訪談主觀性** — manager 回答帶 self-justification 與 survivorship bias；某些「運氣歸因為紀律」的回答需批判性審視。
- **sample 集中於 US** — 15 位中 13 位是美國 manager；歐洲/亞洲視角缺失。
- **未涵蓋 2010 後的 manager** — 2012 成書，未包含 Jim Simons（Renaissance 後期）、Marko Kolanovic、或 crypto 時代的 Su Zhu 等新星。
- **讀者易陷入 hero worship** — 過度崇拜成功 manager 可能導致忽略「他們的邊緣不可複製」的事實；真實學習應是 meta-process 而非具體策略。
- **缺乏量化驗證** — Schwager 呈現 manager 的說法但未獨立驗證其績效數字；部分基金後續倒閉或風格漂移。

### 與 Edward 既有知識的連結
- **對齊 Layer Zero 原則 1 核心身份 + 原則 4 階段性完成**：成功 manager 的「process > outlook」完全是 Edward「自我持續演化」的商業版；不追求完美 outlook，只追求完美 process。
- **Asymmetric option trading 是 B1-B2 options 策略的靈感**：deep OTM put 作為 tail hedge 或 asymmetric speculation 的工具；配合本輪 Douglas《Zone》的心理、Chan《Machine Trading》的 gamma scalping，形成完整 options 策略組合。
- **Woodriff ML 案例預示 ZP 方向**：他的 1000-factor ensemble 是 Kelly-Xiu 2023 書的前身；Edward 可採類似架構但用現代 ML stack（Python + scikit-learn + lightgbm）。
- **可挖金礦**：第 15 章的 40 條 meta-lessons 可 distill 為 `LYH/agent/dna/trading_meta_lessons.md`，作為 B1 執行時的 sanity check reference。
- **衝突點**：訪談的 discretionary 偏好與 Edward 的 algo 方向有張力；但 meta-lessons（process、risk、ego check）是 transcend 方法論的通用原則。
