## 賺贏大盤的動能投資法 — Andreas F. Clenow (繁中)
**來源**: E:/書籍/賺贏大盤的動能投資法 Stocks on the Move Beating the Market with Hedge Fund Momentum Strategies, Andreas F.Clenow.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- 第一章 動能投資的歷史（Jegadeesh-Titman 1993、AQR、對沖基金實作）
- 第二章 為何動能有效（行為偏差、逐漸揭露訊息、羊群效應）
- 第三章 定義動能指標（對數回報斜率、校正 R²、漂移量）
- 第四章 股票池選擇（S&P 500、Russell 1000、防止流動性陷阱）
- 第五章 排序與進場邏輯（每週排名前 20%、市場 regime filter）
- 第六章 頭寸分配（波動率平權，ATR-based sizing）
- 第七章 再平衡頻率（每週？每月？交易成本考量）
- 第八章 Regime Filter（S&P 指數 > 200 日均線才買）
- 第九章 完整回測結果（1999-2014 年化 18.4%、Sharpe 1.0）
- 第十章 與其他策略的 correlations
- 第十一章 實作坑（股利、拆股、併購、退市）
- 第十二章 零售版本縮減策略
- 第十三章 常見疑問

### TL;DR (≤120字)
Clenow 為股票動能策略的系統化指南：用 90 日對數回報斜率 × R² 的校正動能作為排序，每週買最強 20% 的股票，用波動率平權 + regime filter 控制風險。1999-2014 年化 18.4%，Sharpe 1.0。繁中版完整翻譯 + 台灣市場適用性討論。屬於「個股動能 + 機械化執行」派的教科書。

### 核心本質 (3-5 條)
1. **動能的本質是行為偏差**（本質，第 2 章） — 投資者 under-react to news（訊息逐漸消化）+ 羊群效應（贏家繼續買贏家）造成價格延續；這是學術界 100+ 篇文獻支持的真實 anomaly，但 anomaly 不等於永恆——2007-2009 動能大爆炸即反例。
2. **R²-校正斜率 > 純回報**（本質，第 3 章） — 僅看 N 天回報會混淆「長期穩定上漲」與「最後兩天暴衝」；Clenow 用 log-regression slope × R² 把「趨勢品質」納入排序，避開跳空/炒作股。
3. **Regime Filter 是動能策略的生死開關**（本質，第 8 章） — 當 S&P 500 < 200 日均線時關閉所有多單、全部現金；2008 年此開關可避免 -40% 回撤，回到 -10%。沒 regime filter 的純動能策略在熊市會災難性虧損。
4. **Sector/行業濃度會自動偏集中**（本質，第 4、5 章） — 純動能排序前 20% 經常集中於 2-3 個熱門行業（2020 的 Tech、2022 的 Energy）；Clenow 主張接受這種集中，因為這反映真實市場動能，強行分散會削弱 alpha。
5. **每週再平衡 vs 每月再平衡的取捨**（本質，第 7 章） — 週度更新動能訊號最即時但交易成本高；月度更新訊號延遲但成本低。Clenow 實證：週度 Sharpe 1.05、月度 0.95、差距小，推薦月度降成本。

### 可用戰術/策略
- **Clenow 動能排序**：每月底計算 S&P 500 每檔 90 日對數回報 regression slope × R²（校正波動品質），由高到低排序，買前 20 檔等波動率權重。
- **Regime Filter**：S&P 500 < 200 日均線 → 持現金；> 200 日均線 → 動能買股。
- **波動率平權頭寸**：每檔股票頭寸 = (Account × 0.002) / (ATR × Price)；使每筆交易預期損失標準化。
- **換股規則**：每月重新排序，當前持倉不在前 20% 即賣出換入新進者；個股止損 = 落出前 40%。
- **台股版改良**：用 TAIEX 0050 指數作 regime filter、台 50 成份股作標的池、動能排序前 10 檔（標的池較小）。

### 盲點 / 反例 / 適用邊界
- **動能 crash 風險**：2009 年 3 月動能策略瞬間虧損 > 30%（空軍補平倉買成長股，價值股暴漲 50%）；即使 regime filter 也難避免反轉 crash。
- **2015-2020 動能表現低迷**：Clenow 書於 2015 年，但 2015-2019 動能策略相對大盤 alpha 微薄甚至為負；非永恆 anomaly。
- **小市值股流動性陷阱**：書中 S&P 500 範圍流動性充足，若擴展到 Russell 3000 小市值，滑價會吃掉 50% alpha。
- **基本面完全缺席**：純動量策略不看估值/ROE/品質；2000 網路泡沫頂點與 2021 meme 股頂點都會買入被炒作的垃圾股。
- **稅務問題**：高換手率在美國產生短期資本利得稅 37%，免稅帳戶外會大幅侵蝕稅後回報。

### 與 Edward 既有知識的連結
- **對齊 ZP 美股模組**：Clenow 動能策略可直接作為 Edward ZP/quant/us_equity/ 的第一個 production strategy；邏輯清晰、歷史可驗證、資金門檻低。
- **延伸既有 DNA**：§4 階段性完成——作者承認動能會有 drawdown 年，但整體仍 profitable；接受 downside 換 long-run alpha 符合 Edward 長期主義。
- **衝突點**：Clenow 主張集中於熱門板塊，與 Bogle《Common Sense on Mutual Funds》分散化哲學相反；Edward 可用 Clenow 做 alpha 引擎、Bogle 核心做底倉。
- **可挖金礦**：第 3 章 R²-校正斜率公式 + 第 8 章 regime filter 可作為 ZP 通用 momentum scoring + market regime detection module。
- **對接 Kelly-Xiu Financial ML**：Clenow 的 R²×slope 是 hand-engineered momentum feature；Kelly-Xiu 可把此作為 baseline，再加上 ML regularization 提升 OOS。
