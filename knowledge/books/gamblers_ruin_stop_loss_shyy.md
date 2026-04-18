## Gambler's Ruin and Optimal Stop Loss Strategy — Gang Shyy（1989, Journal of Futures Markets, Bridgewater）
**來源**: staging/b2_batch_D_extracts/f58fb557b81baf84__gamblers_ruin_and_optimal_stop_loss_strategy.md | **消化日**: 2026-04-18 | **模型**: opus-4.7 | **Round**: llm_round_6

### 目錄
- Introduction（Stop loss 策略的實務背景、Fama 1970 相關）
- Gambler's Ruin（假設 1：Markov 價格過程；假設 2：stop loss A + profit take B）
- Level Crossing Theory（隨機過程的 first passage time）
- Derivation of Ruin Probability 公式
- Optimal Stop Loss（風險中立 utility 最大化、U(A) = PA×B - (1-PA)×A）
- Two Rules of Thumb（1. 越寬 stop 越少被停損 2. marginal gain 遞減）
- Numerical Examples（B=16, p=0.6 vs 0.4）
- Policy Implications

### TL;DR (≤120字)
Gang Shyy（後為 Bridgewater 研究主管）1989 年論文用**賭徒破產問題（Gambler's Ruin）+ 隨機過程 level-crossing theory** 給出「停損位 A 的最優選擇」嚴謹數學推導。**核心結論**：當 p > 0.5（策略有 edge），寬停損 → 較高勝率但單筆期望值可能降低；當 p < 0.5（劣勢），**不應該交易**。這顛覆了「停損越嚴越安全」的流行教條。論文的關鍵價值：首次把停損問題用嚴謹機率模型形式化，而非經驗法則。

### 核心本質 (3-5 條)
1. **Markov 離散價格模型**（本質，假設 1） — 價格在單位時間移動 ±1，上升機率 p、下降機率 q=1-p；這是 Bachelier-Einstein 隨機漫步的離散版。Shyy 明確設定賠率 b=1（對稱跳動），這簡化了 Kelly 複雜度。
2. **Gambler's Ruin 核心公式**（本質，核心推導） — 設 k = q/p，從狀態 i 出發觸及 A（停損）前觸及 B（獲利）的機率 = (k^A − k^(A+i)) / (k^A − k^(A+B))。等價地：順利達到獲利目標的機率 P_B = (1 − k^A) / (1 − k^(A+B))。對於長期正 edge（k < 1），P_B > 0.5 當 B 不太大、A 不太小。
3. **Optimal Stop Loss 的矛盾結論**（本質，Optimal Stop Loss 節） — 若 p > 0.5（有 edge）：**不應設停損**（讓獲利持續可提高期望值）。若 p < 0.5（劣勢）：**不應交易**（無論如何停損都是負期望）。這與主流「紀律交易=嚴停損」的教條相反。
4. **Marginal 收益遞減是 convex 優化前提**（本質，Rule 2） — 停損從 100 bps 放寬到 200 bps，會提升多少勝率？作者證明 d²P/dA² < 0，即 marginal gain 遞減。這保證了 U(A) = P_B×B - (1-P_B)×A 是凹函數、有內部最大值。
5. **Bridgewater 血統**（歷史本質） — 作者 Gang Shyy 當時為 Bridgewater（Ray Dalio）研究主管；Dalio 本人在致謝名單。這暗示 Bridgewater 早期（1989）的研究框架深受 gambler's ruin / rigorous probability 影響——後來演化為 Pure Alpha 的 risk budget 理論。

### 可用戰術/策略
- **停損/目標位設計公式**：給定策略 p、b，按 Shyy 公式計算到達目標前被停損的機率；實戰 p 應用歷史勝率 + 參數穩健性測試。
- **No-Stop 策略（p > 0.5）**：若確信 edge 存在，可以運用「部分獲利了結」代替停損——例如到達 1R 時減倉 1/3、到達 2R 時再減 1/3、剩餘留到趨勢反轉。
- **Trade-Size 動態調整**：若 p < 0.5，最優解是不交易；若 p 不確定，最優解是**減小 trade size**（Kelly fractional）使 drawdown 在可承受範圍內。
- **Profit Target B 的倒推**：設定 B 時，反向用 Shyy 公式求 P_B × B 最大化；實戰意味著「期望 R-multiple × 勝率」最大而非單純追求高 B。
- **驗證 Markov 假設**：實作前用 Runs Test、Hurst exponent 驗證價格序列的 Markov 性；若有長記憶（H > 0.5），公式需修正。

### 盲點 / 反例 / 適用邊界
- **對稱跳動假設**：Shyy 模型 b=1（跳動 ±1 等幅）；真實市場有跳躍、跳空、fat tails。對於高波動資產，此模型嚴重低估尾部風險。
- **Markov 假設**：現實金融序列有明顯自相關（動能效應）與 volatility clustering；純 Markov 模型未捕捉這些。
- **風險中立 utility 假設**：U(A) = PB - (1-P)A 是 linear utility；對風險規避投資者需換成 CRRA utility，最優 A 會不同。
- **未考慮交易成本**：公式未扣除 commission 與 slippage；實務 A 被觸及時通常以更差價格執行（slippage），使實質 A > 公式假設的 A。
- **單次 vs 重複**：本文分析單次交易；重複交易時考慮 drawdown 序列（Kelly）時，結論可能不同（重複交易需較小 A 以降低 ruin probability）。

### 與 Edward 既有知識的連結
- **對齊 ZP 零式本質**：Gambler's Ruin 是「風險不爆倉」的精確數學化；Edward 的經濟自給恰需要這個保證。
- **對接 Kelly Criterion（llm_round_6 Fortune's Formula, Kelly 1956）**：Shyy 論文是 Kelly 在「停損策略」語境的應用——長期 Kelly 等價於 Shyy 的「最優 A」。
- **對接海龜交易（Way of Turtle, llm_round_6）**：海龜使用固定 N×ATR 停損；Shyy 論文揭示，這個選擇在 p>0.5 場景下可能次優——如果 edge 足夠大，更寬停損（甚至 trailing）會有較高期望值。
- **衝突點**：Elder《Trading for a Living》主張 2% 硬停損；Shyy 論文指出若 edge 強，嚴停損可能降低期望值。Edward 需根據實測 p 決策。
- **可挖金礦**：Bridgewater 早期研究框架 + Dalio 致謝的歷史價值；可整合入 ZP/stop_loss/theoretical_foundations.md。對 B1T3 的停損參數設計提供嚴謹驗證工具。
