## Money Management Strategies for Serious Traders — David C. Stendahl

**來源**: E:/書籍/Money Management Strategies for Serious Traders, David C. Stendahl.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 資金管理：被忽略的交易支柱（為何大多數交易員失敗的真正原因）
- 第 2 章 風險分析基礎（期望值、標準差、variance、Sharpe 的實務推導）
- 第 3 章 回撤分析（drawdown 類型、duration、pain index）
- 第 4 章 固定金額方法（fixed dollar、逐筆等額下單的優劣）
- 第 5 章 固定比例方法（fixed fractional、Vince optimal f、Ryan Jones 的 fixed ratio）
- 第 6 章 Kelly 公式（理論推導、實務修正、Kelly 的心理要求）
- 第 7 章 波動率加權（ATR-based sizing、風險平價）
- 第 8 章 Anti-Martingale 積累（profit compounding 規則）
- 第 9 章 組合配置（多策略、多市場的 capital allocation）
- 第 10 章 回測資金管理規則（將 MM 納入歷史模擬）
- 第 11 章 心理層面的 MM 執行（紀律、情緒劫持、長期堅持）

### TL;DR (≤120字)
Stendahl 是 RINA Systems 創辦人 + 系統交易軟體設計者，本書是 **資金管理的「方法對照表」**：把 fixed dollar、fixed fractional、optimal f、Kelly、fixed ratio、ATR-based 等所有主流方法並排比較，用同一組歷史資料跑每種方法，展示實際 drawdown/growth 差異。適合做「選擇 MM 方法」的決策工具。

### 核心本質 (3-5 條)
1. **方法差異 = 成長率 vs 回撤的 trade-off frontier**（本質） — 第 4-7 章的對比：同一策略用不同 MM 方法，年化報酬可從 15% 到 60%、最大回撤從 10% 到 70%。**沒有「最好的 MM 方法」**，只有「最匹配個人 risk appetite 的方法」。Stendahl 的貢獻是提供了這個 frontier 的可視化。
2. **Fixed Ratio (Ryan Jones) 的逐漸加速邏輯**（本質） — 第 5 章：Jones 的 fixed ratio 不同於 fixed fractional，它是「每賺 $delta 才加 1 contract」而非按比例。優點是初期慢速（保護小帳戶）、後期指數加速（放大勝利）；缺點是 delta 選擇主觀。Stendahl 示範 delta 選擇方法：歷史最大回撤的 1-2 倍。
3. **Pain Index 比 Max Drawdown 更能捕捉痛苦**（本質） — 第 3 章：max drawdown 只記錄一個點的深度，但交易員實際承受的痛苦是「花多久恢復」+「多少天在水下」的總和。Pain Index = 水下天數的積分。兩個策略同 max DD 20%，恢復 3 個月 vs 2 年，pain index 差 8 倍。
4. **Kelly 的心理要求遠超一般人**（本質） — 第 6 章：Kelly = 理論最優但波動率極高（典型最大回撤 50%+）；半 Kelly 犧牲 25% 成長率但回撤減半；1/4 Kelly 犧牲 44% 成長率但回撤 1/4。絕大多數交易員應選 1/4-1/2 Kelly，滿 Kelly 只給「對 edge 極度自信且心理強大」的人。
5. **MM 回測時必須一起測試，不是事後加**（本質） — 第 10 章：許多交易員先找出「好策略」，再決定 MM 規則；這是錯的，因為 MM 本身影響複利軌跡與止損決策。正確做法是把 MM 規則作為策略的一部分寫入回測代碼，整體測試。

### 可用戰術/策略
- **MM 方法選擇決策樹**：帳戶 < $25k → Fixed Dollar（最保守）；$25k-$100k → Fixed Fractional 2%；$100k-$1M → Fixed Ratio 或 1/4 Kelly；$1M+ → 組合 1/4 Kelly + ATR-based；根據個人 risk tolerance 微調。
- **Ryan Jones Fixed Ratio 實作**：起始 1 contract、delta = $5,000；每累積 $5k 獲利加 1 contract；每虧損 $5k 減 1 contract；下不減至 0 contract（最小仍保 1）。
- **ATR-based sizing**：每筆部位大小 = (帳戶 × 1%) / (2 × ATR × contract multiplier)；自動根據當前波動率調整，高 vol 時小單、低 vol 時大單。
- **Pain Index 追蹤**：每日計算組合淨值與歷史高點的差，累積「水下天數」；若 pain index > 歷史 90 分位，減倉 30% 直到恢復新高。
- **MM 回測強制規則**：所有策略回測時都必須包含完整 MM 邏輯（含開倉、加倉、止損、獲利回吐規則），不可用「不含 MM 的理論 Sharpe」做決策。

### 盲點 / 反例 / 適用邊界
- **偏期貨視角** — 大部分案例是 commodities/E-mini 期貨，對 options/crypto/股票的特殊性（如 options 的 theta 衰減、crypto 的 24×7）考慮不足。
- **方法選擇偏主觀** — 雖然 frontier 可視化好，但「我該選哪個」仍需個人判斷；缺乏嚴格 optimization criteria。
- **未深入 correlation** — 多策略配置章節較簡，對 factor exposure、tail correlation 處理有限；需配合 Narang/Hull 補足。
- **crypto/DeFi 完全缺席** — 書成於 2000s，crypto 的 maker fee rebate、DeFi yield farming 等 MM 考量未涉及。
- **回測軟體綁定 RINA/Portfolio Maximizer** — 許多具體工具綁定 Stendahl 的商業軟體；Python/R 讀者需自己重寫。

### 與 Edward 既有知識的連結
- **對齊 Round 1 Vince、本輪 Unger**：三本合讀是資金管理的完整譜系——Vince 理論基礎、Stendahl 方法比較、Unger 實戰冠軍經驗。
- **Pain Index 適合 Edward 的自我監控**：相比單純 max drawdown，pain index 更能反映實際心理壓力；可內建於 Dashboard 作為每日指標。
- **MM 選擇決策樹直接適用**：Edward 當前帳戶規模 (B1 階段) 對應 Fixed Fractional 2% 或 1/4 Kelly；未來規模擴張自動升級配置方法。
- **可挖金礦**：Fixed Ratio (Ryan Jones) 的逐漸加速邏輯適合 B1 初期「慢速啟動 → 後期加速」的成長路徑；可加入 `ZP/quant/sizing/fixed_ratio.py`。
- **衝突點**：Stendahl 的 Kelly 保守派 (1/4 Kelly) 與 Vince 的 optimal f 樂觀派有張力，Edward 在 B1 階段採 Stendahl 保守派；未來策略成熟後可逐步放大。
