## Maximum Adverse Excursion: Analyzing Price Fluctuations for Trading Management — John Sweeney

**來源**: E:/書籍/$$$ 1. Maximum Adverse Excursion, John Sweeney.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 為何需要 MAE 分析（傳統止損規則的盲點）
- 第 2 章 MAE 定義：每筆 trade 在生命週期中的最大逆向移動
- 第 3 章 MAE vs MFE（Maximum Favorable Excursion）的互補關係
- 第 4 章 收集資料：如何從交易紀錄計算 MAE/MFE
- 第 5 章 MAE 分布分析（贏家 MAE vs 輸家 MAE）
- 第 6 章 設定最佳止損位（基於贏家 MAE 95 分位數）
- 第 7 章 MFE 分析：何時停利（贏家 MFE 分布）
- 第 8 章 組合規則：MAE 止損 + MFE 停利
- 第 9 章 跨市場/策略的 MAE 對比
- 第 10 章 實戰案例（S&P、bonds、soybeans 的 MAE 分析）
- 第 11 章 MAE 分析的陷阱與誤用

### TL;DR (≤120字)
Sweeney 的書（1996）是**「止損位置的統計學基礎」**開山作。核心發現：**贏家的 MAE 遠小於輸家的 MAE**——成功 trade 通常不會先逆行超過 X%。用這個事實逆推最佳止損位：設在「若超過則此 trade 極少贏」的位置，而非主觀數字。這是把止損從 art 轉為 science 的關鍵工具。

### 核心本質 (3-5 條)
1. **止損 = 統計推斷 而非 主觀規則**（本質） — Sweeney 核心洞察：止損不應基於「我能承受多少虧損」（心理），而應基於「贏家 trade 通常不超過多少逆行」（統計）。收集 50-100 筆歷史贏家的 MAE 分布，95 分位數就是最佳止損——之上 95% 的贏家仍活著、之下則被過濾的 mostly 輸家。
2. **贏家 MAE 與 輸家 MAE 的 bimodal 分布**（本質） — 第 5 章關鍵觀察：贏家 MAE 典型分布在 0.3-1.5 ATR、輸家 MAE 典型分布在 2-5 ATR；**兩者間有「no man's land」**——設止損在此區域（約 1.5-2 ATR）可過濾大部分輸家同時留住 95% 贏家。這給出具體止損數字的統計依據。
3. **MFE 分析揭示停利的最佳位置**（本質） — 第 7 章：收集贏家的 MFE 分布；典型發現是 50% 贏家 MFE > 2 ATR、25% > 4 ATR、10% > 8 ATR。這意味著**設單一固定 target 會丟失 tail returns**；正確做法是 partial profit taking：在 2 ATR 平 30%、4 ATR 平 30%、剩下 trailing stop。
4. **不同策略/市場需獨立的 MAE 分布**（本質） — 第 9 章：trend-following 策略的 MAE 分布與 mean-reversion 不同；S&P 的 MAE 分布與 gold 不同；時間框架改變也改變分布。**不能用通用 ATR 倍數**（如「2 ATR 止損」），需對每個策略-市場組合分別建立 MAE 分布。
5. **MAE/MFE 是 post-hoc 分析，需 prospective 驗證**（本質） — 第 11 章：用歷史 trade 計算 MAE/MFE 會有 survivorship bias（早已止損的 trade 沒有真實 MAE）。需要用「原始進場 + 假設無止損」的 simulation 獲取真實分布；或用 minimum initial stop 之後再統計。

### 可用戰術/策略
- **MAE-based 止損設定**：收集過去 100 筆 winning trades，計算每筆 MAE（以 ATR 歸一化）；取 95 分位數作為止損位。例如 95 分位 = 1.8 ATR，則止損設 2 ATR（略寬以留 margin）。
- **MFE-based 多階段停利**：對贏家 MFE 分布計算 50%, 75%, 90% 分位數；在這些點分別平倉 30%, 30%, 30%，剩餘 10% 留 trailing stop。
- **策略-市場 MAE matrix**：對每個策略 × 市場組合建立 MAE 分布表；止損參數 tailored 而非一刀切。
- **Minimum Initial Stop 規則**：進場時設保守初始止損（2.5-3 ATR），運行 30 筆後根據實際 MAE 分布收緊至 95 分位數；避免過早用猜測止損。
- **Adverse Excursion Journal**：每筆 trade 記錄 entry、exit、max drawdown during trade (MAE)、max rise during trade (MFE)；每月 review 分布變化。

### 盲點 / 反例 / 適用邊界
- **需充足樣本** — MAE 分布需 ≥ 50 筆歷史 trade 才可靠；新策略初期無法應用，需先用保守止損。
- **regime shift 使分布無效** — 2020 COVID 或 2022 inflation 等 regime change 可能使過去 MAE 分布失效；需定期重新校準。
- **未考慮 slippage** — MAE 基於 mark-to-market 價格，但實際止損 fill 會有 slippage；尤其 overnight 或 gap open 時 MAE 止損失效。
- **對 intraday 策略過於粗糙** — 書中以日線為主，intraday 策略需 minute/tick level 的 MAE；概念相同但資料處理複雜。
- **1996 年成書，過時** — 書中例子是 80-90 年代商品；現代股票與 ETF 的分布差異需自行驗證。

### 與 Edward 既有知識的連結
- **對齊 Round 1 Faith《海龜》的 2N stop**：Faith 用 2 × ATR 作為通用 stop，Sweeney 用 statistical MAE 作為 precise stop；Sweeney 是 Faith 的 quantitative 升級版。
- **對齊本輪 Stendahl/Unger/Harris 的 MM 框架**：止損設定是 MM 的一部分，Sweeney 提供止損的 statistical 基礎；三者合起來是完整 risk management 鏈條。
- **MAE/MFE Journal 可搬入 B1**：每筆實盤 trade 自動 log MAE/MFE；日後分析可校正止損規則。
- **可挖金礦**：MAE-based 止損可編為 `ZP/quant/risk/mae_stop.py`，對每個 live 策略自動計算並應用 MAE 分位數止損。
- **衝突點**：Sweeney 要求大樣本與 Davey 的快速 deployment 哲學有張力；Edward 初期用 2-3 ATR 保守止損，累積 100 筆後切換 MAE-based。
