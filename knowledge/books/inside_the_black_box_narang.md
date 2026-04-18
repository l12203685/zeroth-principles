## Inside the Black Box: The Simple Truth About Quantitative Trading — Rishi K. Narang

**來源**: E:/書籍/Inside the Black Box The Simple Truth About Quantitative Trading, Rishi K. Narang.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 I 部分 量化交易的基本概念
  - 第 1 章 為何量化交易重要（資產管理業的量化份額、對市場的影響）
  - 第 2 章 量化交易過程（策略產生、回測、執行、風險管理的串聯）
- 第 II 部分 量化策略的組成模組
  - 第 3 章 alpha 模型（趨勢、均值回歸、價值、品質、growth、情緒）
  - 第 4 章 風險模型（factor model、optimization、constraint design）
  - 第 5 章 交易成本模型（市場衝擊、機會成本、回測中的執行建模）
  - 第 6 章 組合建構（min-var、risk-parity、Black-Litterman、固定組合）
  - 第 7 章 執行系統（algo execution、smart order routing、dark pool）
- 第 III 部分 資料與基礎設施
  - 第 8 章 資料（來源、清理、survivorship、corporate action）
  - 第 9 章 研究方法論（overfitting、walk-forward、out-of-sample）
  - 第 10 章 基礎設施（hardware、software stack、risk monitoring）
- 第 IV 部分 評估與展望
  - 第 11 章 如何評估量化基金（due diligence checklist）
  - 第 12 章 批評與回應（flash crash、quant quake、未來展望）

### TL;DR (≤120字)
Narang 是 Telesis Capital 的 fund-of-fund 管理人，本書定位是「給 LP/allocator 的量化策略說明書」。**核心貢獻是把量化策略拆成 6 個可獨立評估的模組（alpha/risk/cost/portfolio/execution/infra）**，配合 due diligence checklist，打破「量化 = 黑箱」的迷思。適合讀者從 manager selection 視角反向學習量化交易。

### 核心本質 (3-5 條)
1. **量化策略 = 6 模組的組合，非單一神秘公式**（本質） — 第 2 章的核心圖：alpha model → risk model → cost model → portfolio construction → execution → infrastructure。任何量化基金的績效可拆解為這 6 模組各自的貢獻度；把整體視為黑箱的人無法 due diligence，把每塊視為可替換模組的人才能評估。
2. **alpha 只有 4 大類**（本質） — 第 3 章 Narang 的分類學：(1) trend following（包含 momentum）、(2) mean reversion（包含 statistical arb）、(3) value（基本面錯誤定價）、(4) growth/quality（成長性持續）。99% 的量化 alpha 是這 4 類的排列組合；聲稱發現第 5 類的多為 data mining artifact。
3. **執行成本可能是最大的 alpha 殺手**（本質） — 第 5 章反復強調：對 10M+ 資金，市場衝擊（market impact）通常大於手續費 10-100 倍；一個回測 Sharpe 2.0 的高頻策略可能因 impact 在實盤只剩 0.5。這是 retail 回測與機構實盤巨大落差的根源。
4. **組合建構的藝術 = 如何不讓兩個好策略互相打架**（本質） — 第 6 章：兩個各自 Sharpe 1.5 的策略若相關 0.8，組合 Sharpe 只有 1.6（vs 不相關可達 2.1）。Optimizer 的關鍵是 covariance estimation（EWMA > sample、shrinkage > full MLE），錯的 cov matrix 比沒有 optimizer 更糟。
5. **回測 overfitting 是工業病，不是道德問題**（本質） — 第 9 章：即使最有紀律的研究者，測試 N=100 個策略後選最佳的，期望 Sharpe 膨脹 1.5-2×。這不是研究者不誠實，是統計必然。防治方法只有 walk-forward + out-of-sample + 小資金驗證，沒有捷徑。

### 可用戰術/策略
- **6 模組評估框架**：對任何策略（包括自己的），分別評分 alpha/risk/cost/portfolio/execution/infra 各 0-10 分；總分低於 40/60 不應投入實盤資金。
- **alpha 分類測試**：用 Fama-French 3-factor + momentum 4-factor 做回歸，看殘差是否還有 alpha；若因子已解釋 80%+，該策略 alpha 只是變形的 factor exposure 而非 novel。
- **交易成本模型 (Almgren-Chriss)**：impact = γ × σ × (Q/V)^α，γ 為永久衝擊係數、σ 波動率、Q 訂單量、V 日均量、α 約 0.5-1；回測時必須扣除這項成本。
- **due diligence 問題清單**（第 11 章）：策略容量？Sharpe 的 out-of-sample 實盤記錄（非回測）？最大回撤及持續時間？策略在 2008/2020/2022 的表現？基礎設施在極端流動性事件的故障紀錄？
- **Quant quake 2007 教訓**：當 crowding 發生時（多家 quant 持類似部位），去槓桿連鎖反應 3-5 天內觸發 20%+ 損失。偵測方法：追蹤 beta-neutral 策略的月度相關性，若 > 0.3 且仍上升則預警。

### 盲點 / 反例 / 適用邊界
- **聚焦 institutional，忽略 retail 特性** — Narang 的 6 模組對 100M+ 基金是關鍵，但 retail < 1M 資金時執行成本影響小、組合建構重要性低；本書不適合直接 retail 應用。
- **另類資料缺席** — 書成於 2013（2nd edition），當時 alt-data 尚未工業化；2017 後的衛星/信用卡/社交流等 alpha source 未涵蓋。
- **crypto 與 defi 完全無** — 量化基金的新興藍海在 crypto（arb、MEV、DeFi yield）書中零覆蓋。
- **對 ML 持懷疑態度** — 書中認為 ML 在金融作用有限（2013 觀點），未預見 2020+ transformer 與 LLM 在另類資料處理的價值。
- **執行章節偏概念** — 第 7 章談 VWAP/TWAP 但無具體演算法細節；深入執行請看 Johnson《Algorithmic Trading and DMA》。

### 與 Edward 既有知識的連結
- **補強 Round 1 HFT Aldridge**：Aldridge 偏 HFT 技術，Narang 偏 LP 視角；Aldridge 告訴你怎麼做、Narang 告訴你怎麼評估別人做的。
- **6 模組框架對齊 ZP 架構**：可直接映射為 `ZP/strategy_spec.md` 的標準化字段（alpha/risk/cost/portfolio/execution/infra），每個策略入庫時強制填寫 6 欄位。
- **due diligence checklist 可內化為 Edward 自評工具**：第 11 章的問題每月對自己跑一次，避免自欺偏差。
- **可挖金礦**：第 5 章 Almgren-Chriss cost model 可搬入 ZP/quant/cost/ 作為所有策略的 pre-trade cost calculator。
- **衝突點**：Narang 對 retail 不太友善的立場與 Chan《Quantitative Trading》的 retail 主義相反；Edward 應採 Chan 的 retail 視角但用 Narang 的框架自我審視。
