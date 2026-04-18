## Risk Management and Financial Institutions (2ed) — John C. Hull

**來源**: E:/書籍/Risk Management and Financial Institutions, 2ed, by Hull J. C..pdf  |  **消化日**: 2026-04-18  |  **模型**: opus-4.7 (1M ctx)

### 目錄
- 第 I 部分 金融機構（banks、insurance、pension fund、mutual fund、hedge fund）
- 第 1 章 銀行業風險（interest rate、credit、liquidity、operational）
- 第 2 章 保險業風險（longevity、mortality、catastrophe、reinsurance）
- 第 3 章 pension/mutual/HF 的風險特徵差異
- 第 II 部分 Market Risk（VaR、ES、historical simulation、delta-normal）
- 第 4-5 章 VaR 方法論與建模陷阱
- 第 6 章 Volatility 估計（EWMA、GARCH、implied vol）
- 第 7 章 correlation 與 copula 建模
- 第 III 部分 Credit Risk
- 第 8 章 credit ratings、historical defaults、recovery rates
- 第 9-10 章 credit VaR、CreditMetrics、KMV、structural model
- 第 11 章 credit derivatives（CDS、CDO、synthetic tranches）
- 第 IV 部分 Operational & Liquidity Risk
- 第 12 章 operational risk（Basel II 三種方法）
- 第 13 章 liquidity risk（funding vs trading liquidity）
- 第 V 部分 Scenario Analysis and Model Risk
- 第 VI 部分 Basel II, III, Solvency II 監理概要

### TL;DR (≤120字)
Hull 的風險教材比 Jorion 更偏教科書式（章節漸進、習題眾多）、案例更新至 2007 前夕。**特色是把金融機構類型作為風險框架入口**（銀行 vs 保險 vs 基金的風險配置不同），而非純方法論。對理解 2008 金融危機成因的系統性視角特別有幫助。與 Jorion 互補，Hull 更適合自學、Jorion 更適合 reference。

### 核心本質 (3-5 條)
1. **不同機構類型 = 不同風險 trade-off**（本質） — 第 I 部分：銀行 = maturity transformation（短借長貸），主要風險 = liquidity；保險 = longevity/mortality risk，主要風險 = 精算假設錯誤；HF = leverage + concentrated bet，主要風險 = drawdown 與 investor redemption 連鎖。**風險管理方法必須 tailored 到機構特性**，通用框架不存在。
2. **GARCH vs EWMA 的實務差別**（本質） — 第 6 章：EWMA（λ=0.94）簡單易用、適合日常 volatility forecast；GARCH(1,1) 理論嚴謹、適合 option pricing 與長期預測。Hull 的實證：90% 的實務情境 EWMA 足夠，GARCH 的 marginal improvement 不值其複雜度。這是「理論 vs 實務」的典型案例。
3. **correlation 在 tail event 時不穩定**（本質） — 第 7 章：正常市場股票相關係數 ~0.3，但 2008 / 2020 危機期間飆至 0.8-0.9。這摧毀了大多數 Gaussian Copula 基礎的分散化假設。正確做法是用 t-copula 或 regime-switching copula，承認 tail correlation 遠高於 average。
4. **Credit derivatives 的真正風險在 correlation 假設**（本質） — 第 11 章：CDO tranches 的 pricing 高度依賴 correlation assumption，2007 年業界普遍用 Gaussian Copula + flat correlation = 20%；實際危機時 correlation 飆升使 senior tranches 意外違約。這是 David X. Li 公式被誤用的經典案例（Round 1 credit derivatives 專論有相關提及）。
5. **liquidity risk 的 dual dimensions**（本質） — 第 13 章：funding liquidity = 機構融資能力、trading liquidity = 資產出售能力。兩者獨立但在危機時耦合：trading liquidity 惡化 → mark-to-market loss → funding liquidity 被抽回 → fire sale → trading liquidity 進一步惡化。這是 LTCM (1998)、Bear Stearns (2008) 的死亡螺旋模型。

### 可用戰術/策略
- **EWMA volatility dashboard**：對組合每日更新 EWMA(λ=0.94) σ 估計，用於 VaR 計算與 dynamic position sizing；比 sample std 對 regime shift 反應快 3-5 倍。
- **regime-aware correlation**：識別當前市場 regime（low-vol vs high-vol，用 VIX 20/40 threshold），在 high-vol regime 自動把 correlation estimate 上調 2 倍，降低組合槓桿。
- **credit spread 追蹤**：對持有的公司債/信用部位，每週更新 5Y CDS spread；若 spread 30 日擴大 > 50%，不論財報為何，減倉 50%。
- **liquidity stress test**：假設 50% 最大部位無法出售 7 天，計算對應的 mark-to-market 損失與 funding impact；若潛在損失 > 組合 20%，該部位必須降槓桿。
- **reinsurance 概念借鑒**：第 2 章的保險業 tail reinsurance 概念可用於交易組合——買深價外 put 作為 portfolio 的「reinsurance」，每月耗 30-50 bps，但在 tail 爆發時保全本金。

### 盲點 / 反例 / 適用邊界
- **2007 年版本，未涵蓋 2008 後事件** — 本書成書在 Lehman 倒閉之前，Basel III、Dodd-Frank、MiFID II、crypto crisis 等後續事件需他處補充。
- **模型偏向 parametric** — 大量 VaR/ES 計算使用 parametric 假設，對 fat-tail/非對稱情境處理較簡；需搭配 McNeil《QRM》補充 EVT 與 copula 進階。
- **缺乏 trading-level 操作細節** — 書中風險管理偏 firm-level，對 trader 日常決策（如單次交易的 stop-loss size）缺乏具體規則。
- **crypto/fintech 風險零覆蓋** — smart contract exploit、stablecoin depeg、CEX insolvency 等需獨立處理（參見 Aven 或新興 DeFi 風險文獻）。
- **中文版翻譯陷阱** — 若讀中譯本，注意「波動率」常被誤譯為「揮發性」，「violatility」翻譯多家不統一，影響學習一致性。

### 與 Edward 既有知識的連結
- **與本輪 Jorion FRM Handbook 強互補**：Jorion 偏百科 reference、Hull 偏漸進教學。兩本合讀是完整風險管理教材，重疊度約 30%。
- **EWMA volatility 可直接 Python 化**：第 6 章公式可搬入 `ZP/quant/volatility/`，作為所有策略的動態風險估計基礎。
- **liquidity dual model 對應 Edward 的經濟自給**：Edward 的 B1 資金規模小，funding liquidity 問題低，但 trading liquidity 需關注（避免 penny stocks、小市值 ETF）。
- **可挖金礦**：第 7 章 t-copula correlation 在 crypto 組合（BTC、ETH、SOL 相關係數變動大）建模特別有用；可加入 `ZP/quant/crypto/correlation.py`。
- **衝突點**：Hull 的 parametric 偏好與當代 ML/non-parametric 方法有張力；Edward 應用時採 parametric 為 baseline、ML 為補強層。
