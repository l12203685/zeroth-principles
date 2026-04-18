## 專業投機原理 Trader Vic on Commodities — Victor Sperandeo

**來源**: E:/書籍/專業投機原理 Trader Vic.pdf + Trader Vic on Commodities.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄（合併兩本主要內容）
- 第 I 部分 交易員的自律與心態
  - 第 1 章 投機 vs 投資的定義（時間框架、風險承擔、勝算）
  - 第 2 章 professional speculator 的 3 要素（保本、持續獲利、追求超額）
- 第 II 部分 道氏理論的現代實作
  - 第 3 章 道氏理論三原則（趨勢有方向、trend 持續到反轉、volume 驗證）
  - 第 4 章 trend change 的 2B 規則（Sperandeo 自創：failed double top/bottom）
- 第 III 部分 市場分析
  - 第 5 章 fundamental vs technical 的結合（先 fundamental 定方向、TA 定時機）
  - 第 6 章 Fed 政策與商品週期（利率、美元、通膨的聯動）
- 第 IV 部分 Commodities 專論
  - 第 7 章 commodity futures 的獨特特徵（contango、backwardation、seasonality）
  - 第 8 章 各 commodity sector（穀物、金屬、能源、softs、livestock）
  - 第 9 章 各市場的基本面驅動（收成、天氣、政治、庫存報告）
- 第 V 部分 風險管理
  - 第 10 章 止損的藝術（fixed %、volatility-based、event-based）
  - 第 11 章 金字塔加碼（pyramid）規則
- 第 VI 部分 案例研究
  - 第 12 章 1980s 金價、1990s 原油、2000s 穀物的大行情案例
  - 第 13 章 Sperandeo 本人的失敗與教訓

### TL;DR (≤120字)
Sperandeo（Trader Vic）是華爾街傳奇——18 年連續正報酬、最大回撤僅 7%。兩本書合起來是他的**「professional speculator operating manual」**：道氏理論現代化 + commodities 深度分析 + 保本第一的風險管理哲學。與短線 algo 對立，他主張「研究 fundamental、用 TA 定 timing、保本 > 獲利」的長線 discretionary 方法。

### 核心本質 (3-5 條)
1. **保本 > 獲利**（本質非戰術） — Sperandeo 的 professional 定義：18 年連續正報酬比某年暴利 200% 更稀有與可貴。**每次交易的首要問題是「若錯了，會虧多少？能否承受？」，而非「若對了，會賺多少？」**。這顛覆了 retail 的「尋找大機會」心態，把保本置於獲利之前。
2. **道氏理論的現代化 = 區分「primary / secondary / minor」三層趨勢**（本質） — 第 3 章：primary trend 持續 1-3 年、secondary trend 持續 1-3 個月、minor trend 持續幾天到幾週。**獲利來自把 primary 方向當骨架、secondary 作為進場時機、minor 作為止損微調**。散戶常把 minor noise 誤認為趨勢反轉，頻繁換方向導致虧損。
3. **2B 規則（Sperandeo 自創）**（本質） — 第 4 章：當價格突破前高（新高）後快速回落至前高以下，這是「失敗突破」，暗示 primary trend 反轉。2B 信號通常提前 1-3 週出現在 classic 反轉（頭肩頂）之前；實戰價值極高。類似地下跌 trend 有 2B bottom。
4. **fundamental 定方向，technical 定時機**（本質） — 第 5 章：Sperandeo 反對純技術派（忽略 fundamental 是 gambling）與純基本面派（錯過 timing 是 wasted conviction）。**正確流程是先研究 fundamental 決定「該做多還做空」，再用 TA 決定「何時進場、何時出場」**。這是 discretionary 的嚴謹版。
5. **commodities 的 fundamental 由實體供需驅動**（本質） — 第 7-9 章：商品價格最終由供需決定（穀物 = 收成 + 天氣、金屬 = 工業需求 + 庫存、能源 = 地緣政治 + OPEC）。與股票不同，commodity 不受央行 QE 直接影響（間接通過通膨）；這給 commodity trader 相對獨立的 alpha 來源。

### 可用戰術/策略
- **2B 反轉訊號**：當 primary uptrend 中出現新高，回檔 1-3 天內跌破前高，形成 2B；做空並設止損於新高 + 1%；勝率 60-70%，R/R 1:3 以上。
- **三層趨勢對齊**：primary 上、secondary 回檔、minor 轉上 = 高勝率做多進場；三層均上 = 已過高點，風險報酬比差。
- **fundamental-driven 商品選擇**：每季研讀 USDA 穀物報告、EIA 能源庫存、LME 金屬庫存；選擇「庫存/需求比」極端（< 20% 或 > 80% 歷史分位）的商品作為 trade 候選。
- **Pyramid 加碼規則**：初始 1 unit、獲利 2-3% 後加 0.5 unit、再獲利 2-3% 後加 0.25 unit；最終 max 1.75 units。每次加碼後將全 stop 移至前次 entry 價。
- **止損三原則**：(1) 最大單筆虧損不超過 2% 帳戶、(2) 止損位設在「若觸及則策略 invalidated」的技術點（非主觀數字）、(3) 一旦止損觸發**絕不** override，即使當下看似「明顯會回來」。

### 盲點 / 反例 / 適用邊界
- **discretionary 難 scale** — Sperandeo 的方法需要深度研究 + 直覺，不易 systemize；對純 algo trader 參考價值低於對 discretionary trader。
- **對 HFT / algo 時代適應性** — 書成於 1990s-2000s，當時手動 + 直覺仍有空間；2015 後 HFT 壓縮了許多短期 edge，2B 等 pattern 的執行窗口縮短。
- **commodities 的 2020 後 regime shift** — 2020 pandemic + 2022 Ukraine 使傳統 commodity fundamental 失效；Sperandeo 的 seasonality 分析未更新此時期。
- **缺乏 options / volatility 內容** — 兩本都聚焦 outright futures，對 options 策略（spread、straddle）未涉及；而 commodity options 是 retail 現在重要的 alpha source。
- **樣本倖存者偏差** — Sperandeo 本人是 18 年正報酬的 outlier；他的方法 → 他的結果的 causal claim 不嚴謹，讀者需警覺。

### 與 Edward 既有知識的連結
- **保本 > 獲利」強對齊 Layer Zero 原則 1 與零式第 5 軸「無 edge = no move」**：Sperandeo 的 professional 定義就是 Edward 零式投資哲學的實戰版。
- **三層趨勢概念可搬入 B1 時間框架設計**：Edward 的策略應區分 primary (1-3 年 asset allocation)、secondary (1-3 個月 strategy rotation)、minor (days-weeks 訊號執行)。
- **2B 規則對應 population exploit（零式第 4 軸）**：失敗突破是大量散戶 FOMO 追高的被動反向信號，fade 他們正是 population exploit 的戰術。
- **可挖金礦**：2B pattern 的偵測可編為 Python 指標加入 `ZP/quant/signals/dow_theory/`，作為 regime change 預警。
- **衝突點**：Sperandeo 的 discretionary 主張與 Edward B1 的 algo/自動化方向衝突；應取其哲學（保本、多時間框架、fundamental-TA 結合）但實作用 quantitative 方法。
