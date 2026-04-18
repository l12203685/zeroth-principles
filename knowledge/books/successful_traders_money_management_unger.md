## The Successful Traders Guide to Money Management — Andrea Unger

**來源**: E:/書籍/The Successful Traders Guide to Money Management Proven Strategies, Applications, and Management Techniques by Andrea Unger (z-lib.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 為何資金管理重要（Unger 自述 World Cup Trading Championships 四連冠經驗）
- 第 2 章 基本統計（期望值、標準差、Sharpe、相關性的實務含義）
- 第 3 章 Fixed Fractional 方法（Ralph Vince 的固定比例、實作陷阱）
- 第 4 章 Optimal f（Vince 的最優 f、其危險性、模擬比較）
- 第 5 章 Secure f（Unger 自創：基於歷史最大回撤的「安全 f」）
- 第 6 章 Anti-Martingale 與 Martingale（平均回測、pyramiding、攤平的陷阱）
- 第 7 章 Monte Carlo 模擬與 drawdown 預測
- 第 8 章 組合多策略的資金分配（等權 vs risk-parity vs volatility-weighted）
- 第 9 章 實戰案例（Unger 本人在 2008-2012 的 futures 策略配置）
- 第 10 章 心理與紀律（連虧時的資金管理執行）
- 第 11 章 如何設計個人化資金管理規則

### TL;DR (≤120字)
Unger 是 World Cup Trading Championships 唯一四連冠（2008/2009/2010/2012），本書是他對 Ralph Vince《Portfolio Mathematics》(Round 1) 的實戰補充。**核心貢獻是「Secure f」框架**：基於歷史最大回撤反推最大可承受槓桿，避開全 Optimal f 的 15%+ 毀滅機率。對獨立 algo trader 特別實用。

### 核心本質 (3-5 條)
1. **Optimal f 的理論最優在實務是災難**（本質） — 第 4 章：Vince 的 optimal f 雖然數學上最大化期望成長率，但對應 70%+ 最大回撤，99% 的交易員無法心理承受。Unger 實證：用 full optimal f 的交易員中 3 年內退出市場率 > 80%；實務最優是「能持續執行」的分數 f。
2. **Secure f = 基於最大歷史回撤的逆推槓桿**（本質） — 第 5 章 Unger 自創：`secure_f = max_drawdown_tolerance / historical_max_drawdown × current_capital`。例如歷史最大回撤 30%、你可忍受 15%，則 secure_f = 0.5 倍固定比例。這比 Kelly 公式更貼近行為約束。
3. **攤平（Martingale）是帳戶殺手**（本質） — 第 6 章：攤平在統計上看似聰明（降低平均成本），但**單次黑天鵝足以毀滅整個帳戶**。Unger 提供實證：用固定攤平規則的 1000 次模擬中，15% 在 3 年內爆倉；而 anti-martingale（只加碼贏錢部位）爆倉率 < 1%，即使期望值略低。
4. **多策略配置不是等權**（本質） — 第 8 章：大多數獨立交易員的「多策略」實則高度相關（都是 trend-following 或 mean-reversion 變形）；正確配置需 volatility-weighted + correlation-constrained。Unger 示範：3 個策略等權 Sharpe 1.2 → correlation-aware 可達 1.6。
5. **資金管理的真正挑戰在執行而非公式**（本質） — 第 10-11 章：公式再好，連虧 10 次後交易員常 override 規則（「這次特殊」）。Unger 建議建立機械化執行（自動下單限制）+ 每日日誌（寫下所有違規）+ 外部監督（夥伴 accountability），用系統迫使自己遵守資金管理規則。

### 可用戰術/策略
- **Secure f 計算**：`secure_f = (個人最大可忍受回撤 %) / (策略歷史最大回撤 %)`；例如策略歷史 max DD = 25%，你能忍 12%，則 secure_f = 0.48，用 48% 的 Optimal f。
- **Anti-Martingale 加碼規則**：只在贏錢後加碼（例如第 1 筆 1 contract、若賺 2% 則第 2 筆 2 contracts、再賺 2% 則 3 contracts），虧錢立刻回到 1 contract；避免攤平。
- **多策略相關矩陣監控**：每週計算 5 個策略的 20 日績效相關矩陣；任一 pair 相關 > 0.6 時，減倉其中一個至原規模 50%。
- **Monte Carlo 預期 DD 估計**：把策略歷史訂單洗牌 10,000 次，取最大回撤的 95 分位數；若 > 個人忍受度，降槓桿至 secure_f。
- **違規日誌**：每日記錄 (策略訊號 vs 實際執行) 的差異，月底審視模式；若違規 > 3 次/月，簡化規則或降規模直到 100% 遵守。

### 盲點 / 反例 / 適用邊界
- **案例集中於 futures** — Unger 是期貨冠軍，大部分案例是 E-mini、Bund、Crude；對股票、options、crypto 需 adapt。
- **樣本是存活者** — Unger 本人是存活下來的冠軍，他的策略是選擇性樣本；他提到的「80% 用 full optimal f 退出」是他觀察，但沒嚴格樣本調查。
- **未深入多資產 correlation modeling** — 第 8 章的多策略 correlation 處理較為 ad-hoc，缺乏 Hull/Narang 的 copula/factor 嚴謹度。
- **缺乏 tail event 處理** — 2008/2020 type 的 tail event 如何影響 secure f 未充分討論；在 black swan 下 historical max drawdown 可能被快速擊穿。
- **心理章節偏個人經驗** — 第 10-11 章的心理建議實用但不如 Steenbarger/Douglas 結構化。

### 與 Edward 既有知識的連結
- **對齊 Round 1 Vince《Handbook of Portfolio Mathematics》**：Vince 給理論最優、Unger 給實戰安全；Edward 應以 secure f 為 default、optimal f 為理論上限參考。
- **對齊 Davey《Building Winning Algorithmic Trading Systems》**：兩人都是 World Cup 冠軍（Davey 三連冠、Unger 四連冠），觀點高度一致；Unger 偏資金管理、Davey 偏系統建構，是獨立 algo trader 的雙 bible。
- **Secure f 直接進 B1 風險預算**：可實作為 `ZP/quant/risk/secure_f.py`，對每個策略計算個人化 secure_f 而非全 optimal f。
- **Anti-Martingale 規則對應 Edward 的「不攤平」直覺**：符合零式「不確定不出手」與 Layer Zero 5 的 bias toward inaction 精神。
- **衝突點**：Unger 的 secure_f 與 Jorion 的 VaR-based 資本配置有張力；前者行為驅動、後者統計驅動。實務可並行使用，取兩者中較嚴格者作為最終槓桿。
