## The Universal Tactics of Successful Trend Trading — Brent Penfold

**來源**: E:/書籍/The Universal Tactics of Successful Trend Trading, Brent Penfold.pdf + (z-lib.org 版本)  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 1 章 為何 trend trading 仍然有效（2008 後爭議、CTA 衰退、簡單規則的持久性）
- 第 2 章 Trend trading 的六大流派（Dow、Turtle、Donchian、MA crossover、Darvas box、momentum）
- 第 3 章 Universal principles across 六流派（survivorship bias、testing methodology）
- 第 4 章 策略設計要素（entry、exit、position sizing、time frame）
- 第 5 章 Entry 技術（breakout、pullback、moving average cross）
- 第 6 章 Exit 技術（fixed target、trailing stop、time-based、volatility-based）
- 第 7 章 Position Sizing（fixed %、ATR-based、volatility targeting）
- 第 8 章 選市場（liquidity、volatility、trendiness 的三維評估）
- 第 9 章 多市場組合（diversification、correlation、capacity）
- 第 10 章 測試與驗證（in-sample/out-of-sample、walk-forward、monte carlo）
- 第 11 章 心理與執行（drawdown 容忍、規則遵循、生活平衡）
- 第 12 章 Penfold 本人的三十年實戰案例

### TL;DR (≤120字)
Penfold 是澳洲 30+ 年 CTA/futures trader，本書定位為**「trend trading 的最後實戰教材」**——在 2010s 許多 trend follower 質疑 edge 消失的背景下，證明簡單 trend rule 配合嚴格 risk management 仍可維持 Sharpe 0.6-1.0。與 Kaufman 百科式相比，Penfold 更聚焦、更實戰、更強調跨市場組合。

### 核心本質 (3-5 條)
1. **Trend edge 並未消失，只是 Sharpe 降低**（本質） — Penfold 的核心論點：1980-2008 年 trend following CTA 年化 15-20%，2010-2020 降至 5-10%，但**仍正報酬**。原因是 QE 環境使 trend 變短但未消失；關鍵是降低 expectation 與提升 correlation diversification。完全放棄 trend 的 trader 錯過了 2016 oil、2020 gold、2022 bond/USD 等清晰 trend。
2. **六流派的共同本質 = 截斷虧損 + 放任利潤**（本質） — 第 3 章：不論 Donchian、MA cross、Darvas box，本質都是 **small loss + big win**。**勝率通常 35-45%**（不重要），盈虧比 2-4（重要）；一年內 2-3 個大獲利決定全年報酬，其餘 50+ 筆小虧損是 cost of doing business。大多數 retail 因此輸——無法忍受連續 10+ 次小虧損等待大贏。
3. **市場選擇的三維：liquidity × volatility × trendiness**（本質） — 第 8 章：(1) liquidity 決定 slippage；(2) volatility 決定 ATR-based position size 與 reward magnitude；(3) trendiness（用 ADX 或 Hurst 指數量化）決定策略有效性。三者兼具的市場不多——典型為 gold、oil、US bonds、major FX pairs、S&P 500；avoid 小市值 commodity、emerging FX、low-vol bonds。
4. **Trailing stop 的選擇決定 trend 策略成敗**（本質） — 第 6 章：too tight → 小波動就止損、丟失大 trend；too wide → 大回撤吃光早期獲利。Penfold 推薦 **Chandelier Stop**（最近 22 日 high − 3×ATR），在大 trend 中 hold 時間足夠長、中等回撤中快速出場。Donchian 20-day low 作為備選。
5. **Trend following 是「高 pain tolerance」資產**（本質） — 第 11 章：trend 策略的 drawdown 可持續 2-3 年（2011-2013 CTA 期間）。交易者需有「可等待 3 年」的 mental capital；否則會在 drawdown 末期放棄，錯過後續 recovery。與 mean reversion 的短 drawdown 但頻繁出場心理完全不同。

### 可用戰術/策略
- **簡化 Donchian Breakout**：20 日 breakout 進場 + 10 日 breakout 反向出場 + 2 ATR 止損 + 1% 帳戶風險每筆；適用 5-10 個跨 asset 市場（gold、oil、bonds、S&P、EUR/USD）。
- **Chandelier Stop**：trailing stop = highest(22-day high) − 3 × ATR(14)；適合 trend-up，可配合 MA cross 作 entry filter。
- **三維市場評分**：對候選市場計算 (20-day avg turnover × volatility × 60-day Hurst)；只交易 3 者皆 > 歷史中位數的市場；低分市場捨棄。
- **ATR-based position size**：每筆風險 = 帳戶 × 1%；每 contract 風險 = 2 × ATR × multiplier；contracts = 帳戶風險 / contract 風險。自動根據波動率調整。
- **Correlation-constrained 組合**：選 5-7 個市場，確保 pair 相關 < 0.3；若某 pair 相關 > 0.5 持續 60 日，剔除其中一個。

### 盲點 / 反例 / 適用邊界
- **期貨為主** — Penfold 主要交易 futures，對股票 trend trading 適用性較低（個股 trend 比 index trend 少見且短）。
- **2008 後 CTA 衰退未完全解答** — Penfold 給出「Sharpe 降低但未歸零」的 empirical 觀察，但未提供 QE 終結後 trend 會否復興的 forward 預測。
- **mean reversion 完全未涵蓋** — 本書 100% trend；若讀者想組合 trend + mean reversion（推薦做法），需配合 Chan 等。
- **Crypto 完全缺席** — crypto 在 2015+ 有強 trend（BTC 2017、ETH 2021），但本書未涵蓋。
- **樣本倖存偏差** — Penfold 30 年活下來是 survivorship；他的規則是否能複製給新 trader 不確定。

### 與 Edward 既有知識的連結
- **對齊 Round 1 Faith《海龜》與 Kaufman《Trading Systems》**：三本都是 trend trading 基礎；Faith 給哲學、Kaufman 給百科、Penfold 給精選實戰。Edward 先讀 Penfold 快速上手，再深入 Kaufman 查細節。
- **Trend+Range 雙引擎對應 ZP 框架**：Edward 的 B1 策略需 trend engine（本書提供）+ range engine（本輪 Brooks）+ vol engine（Round 1 Bennett），三者互補覆蓋 90% 市場 regime。
- **ATR-based position size 可直接 Python 化**：加入 `ZP/quant/sizing/atr_based.py`，對所有策略強制使用 ATR-normalized risk。
- **可挖金礦**：三維市場評分可作為 B1 股票池/商品池的自動化篩選器；每週 refresh 一次評分。
- **衝突點**：Penfold 的 trend 專一與 Douglas/Kiev 的「process 不分風格」觀點互補而非衝突——Edward 可採 trend 策略但用 Douglas 的 mental framework 執行。
