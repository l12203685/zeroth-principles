## Optimal Dynamic Portfolio Selection: Multiperiod Mean-Variance Formulation — Duan Li, Wan-Lung Ng
**來源**: E:/投資交易/量化金融文獻/知識素材/2000 Li-Ng-Optimal dynamic portfolio selection- multiperiod mean-variance formulation.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **1. Introduction** (multiperiod mean-variance 歷史與問題)
- **2. Mean-Variance Formulation for Multiperiod Portfolio Selection** (P1, P2 基本式)
- **3. Analytical Solution to Multiperiod MV Formulation** (核心定理陳述)
- **4. Detailed Derivation** (auxiliary problem embedding + dynamic programming)
- **5. Risk-Free Asset Available Case** (特例簡化)
- **6. Utility Function of Mean & Variance** (generalization)
- **7. Case Studies** (三個數值範例)
- **8. Conclusions**

### TL;DR (≤120字)
Markowitz 1956 單期均值-變異數 (MV) 組合最優化在多期情境下 40 年無解析解;此文引入「embedding auxiliary problem」技巧,給出多期 MV 前緣的閉形公式與最優政策。解決了動態再平衡與終端財富風險控制的經典 gap。

### 核心本質 (3-5 條, 每條 50-120字)
1. **Variance 在期望效用架構下不可加,是多期 MV 的核心困難** — 傳統 DP 之所以無法直接處理 Var(x_T),是因為變異數非期望值,Bellman 最優原則不成立。Li-Ng 的 embedding 把 MV 嵌入一個輔助線性-二次問題,讓 DP 能遞迴求解。
2. **多期 MV 的最優策略是「動態線性回饋」** — 每期應投資的金額是當期財富的線性函數 + 常數,係數由剩餘期數、各資產動差決定。這意味實務上可透過遞迴公式即時計算,不需每期重解最佳化。
3. **效率前緣在多期下呈二次曲線,形狀由投資期數 T 擴張** — T 越大,同樣 variance 下可達期望報酬越高 (time diversification),但前提是各期報酬獨立同分布;若 return process 有依賴性,time diversification 效果減弱甚至反轉。
4. **這是 Kelly 增長法則之外,唯一有解析解的多期最優化** — Kelly 最大化 E[log(wealth)] 也是多期最優,但目標是對數效用;Li-Ng 是對「終端 MV 偏好」最優,兩者服務不同風險容忍。理論完整性上兩者互補。
5. **無短賣限制、無交易成本、無 regime 變化是最強假設** — 這三條在實務上全部違反;Li-Ng 主要做為 benchmark 與教學案例,而非直接可交易策略。

### 可用戰術/策略
- **Portfolio 自動再平衡系統的 backbone 公式** — 若 B1 自營交易系統需要建構多資產權重分配模組,Li-Ng 解析公式可作為 baseline,再根據交易成本 / 短賣限制做 penalty 修正(轉化為 SOCP)。
- **當作 robust MV 的 lower bound** — 文章公式作為 upper performance bound,若實務上策略表現遠低於此 bound,說明 friction (成本、滑點、資訊落後) 吞掉大部分 theoretical edge;可作為策略失敗歸因的診斷工具。
- **配合 stress test** — 用 bootstrap / regime-switch 模擬打破 IID 假設,觀察 Li-Ng 公式偏差程度;偏差大 = 該時期須切換到其他模型(如 robust MV、CVaR)。
- **教學工具** — 新策略工程師培訓時,Li-Ng + Markowitz + Merton 三篇一起讀,建立「閉形解 vs 數值最優化」的分界判斷力。

### 盲點 / 反例 / 適用邊界
- **不處理交易成本、稅、流動性約束** — 實務加上這些後,解析解消失,須回到 stochastic control numerical methods。
- **Return 假設獨立同分布** — 與 Cont 2001 stylized facts 中的 volatility clustering / long-range dependence 衝突;實務上最優權重對 covariance 估計錯誤極敏感(Michaud 的 "estimation error maximizer" 批評)。
- **MV 框架假設投資者只關心前兩動差** — 忽略 skewness、kurtosis、drawdown;在 fat-tailed / crash-prone 市場(加密幣、2008)失效。2000 年後的 robust portfolio / Black-Litterman / risk parity 都是對此的修補。

### 與 Edward 既有知識的連結
- 連結 `risk_control_four_layers` L1:多資產下的部位上限可直接用多期 MV 最優權重作為出發點,再加壓測 penalty。
- 對應零式第 5 條 `bias_toward_inaction`:Li-Ng 的「每期最優線性政策」其實告訴你,在無 edge 訊號時,最佳策略是維持 base allocation 而非頻繁調倉;動態再平衡只在參數真變時才啟動。
- 銜接 Wilmott FAQ Q10 (Markowitz MPT) 與 Q15 (Kelly):三者構成 portfolio theory 三腳架 — 單期 MV / 多期 MV / Kelly,覆蓋不同目標函數。
- 對 B1 自營交易系統的貢獻:若系統含多策略資金分配模組 (multi-strategy allocator),此文給出 closed-form baseline 公式可直接 port 到 Python;再以實務 friction 修正為 practical policy。
