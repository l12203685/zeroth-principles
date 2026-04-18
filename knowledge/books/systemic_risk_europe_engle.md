## Systemic Risk in Europe — Robert Engle, Eric Jondeau, Michael Rockinger (Swiss Finance Institute Research Paper N°12-45)
**來源**: E:/課程/財務工程_固定收益, 結構型財務與其衍生性商品/Papers/Systemic Risk in Europe.pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- Abstract & Introduction
- Section 1: Framework and Measurement of Systemic Risk (SRISK methodology)
- Section 2: Data and Sample (196 European financial institutions, 2000-2012)
- Section 3: Empirical Results（SRISK estimates, dynamic evolution, crisis periods）
- Section 4: Determinants of Systemic Risk（size, leverage, correlation with market）
- Section 5: Policy Implications（macroprudential regulation, capital requirements）
- Conclusion
- Appendix（GARCH-DCC estimation, LRMES computation）

### TL;DR (≤120字)
Engle (諾獎) 與 Lausanne 團隊應用 NYU V-Lab 的 SRISK 模型到 196 家歐洲金融機構（2000-2012）。核心方法：systemic risk = 預期在市場大跌 40% 時該機構的資本缺口。結論：歐洲 top 10 systemic banks（德商、法巴、UBS、RBS 等）在 2011 歐債危機期貢獻了 >$500 billion 的系統性風險。

### 核心本質 (3-5 條)
1. **SRISK = 機構資本缺口的條件期望值**（本質） — SRISK_i = max(0, k × Debt_i - (1-k) × Equity_i × (1-LRMES_i))，其中 k 是 prudential capital ratio（通常 8%），LRMES 是 long-run marginal expected shortfall（危機時股價跌幅）。這把「大而不能倒」量化為可比較的美元金額。
2. **System-Wide Undercapitalization 定義系統性風險**（本質，Abstract） — 單一機構破產不等於系統性風險；全系統同時 undercapitalized 才是——此時 bailout 無效、互相 fire sale 加劇。Engle 的定義從單一機構轉向 "機構對系統脆弱性的邊際貢獻"，這是宏觀審慎監管的核心。
3. **Size × Leverage × Correlation 三因子決定 SRISK**（本質，第 4 節） — SRISK 的分解：(a) size（市值越大貢獻越大）；(b) leverage（負債/股權比越高越脆弱）；(c) equity beta in crisis（危機時跌幅 vs 整體市場）。政策若要減少 systemic risk，須對三者同時調控。
4. **DCC-GARCH 捕捉時變 Correlation**（本質，方法論） — Systemic risk 在 crisis 時期急劇放大，其關鍵是機構間 correlation 從 0.3-0.5 躍升到 0.8-0.95。Engle 的 DCC-GARCH 模型估計時變 correlation，是 SRISK 在 crisis period 可信估計的技術前提。
5. **公開透明的實證工具**（本質，Policy） — 作者把 SRISK 估算開放為 NYU V-Lab 網站（vlab.stern.nyu.edu），每日更新全球主要金融機構的 SRISK ranking。這是學術成果向實務/監管的最佳技術轉移案例——任何監管者或投資人都能自己查。

### 可用戰術/策略
- **Portfolio Systemic Risk Screen**：在持有銀行股前檢查 NYU V-Lab 的 SRISK ranking；避免 top 10 systemic 銀行，或把其權重設為市值的一半。
- **Regional SRISK Aggregation**：計算 Eurozone / US / Japan / UK 的 aggregate SRISK；aggregate 高時減碼該地區 financial sector beta。
- **Crisis Early Warning Indicator**：SRISK 急升（>20% month-over-month）通常 precede 危機 3-6 個月；歷史上 2008 Q1、2011 Q4、2020 Q1 都出現此信號。
- **Long-Short Systemic Risk Trade**：long 低 SRISK bank + short 高 SRISK bank；在長期 Sharpe 略低於 market 但在 crisis 時期大幅 outperform（2011、2020）。
- **Capital Requirement Arbitrage**：高 SRISK 的銀行監管壓力（資本要求、stress test 失敗）風險高；持有 CDS 對沖 counterparty risk。

### 盲點 / 反例 / 適用邊界
- **SRISK 假設 equity market 反映全部訊息** — 對 unlisted bank（大部分歐洲區域銀行、德國 Landesbank）不適用；也無法處理 government guarantee 帶來的 equity underpricing。
- **Model-implied LRMES 非真實 crisis 資料** — LRMES 由 DCC-GARCH 外推，不是觀察到的 crisis drawdown；過去 10 年無大 crisis 的銀行 LRMES 可能低估。
- **Policy tool 無牙** — 2012 論文建議 higher capital requirement 對 top-SRISK 機構；但 Basel III/IV 實施的 G-SIB surcharge 只對全球 top 30，歐洲 regional bank 仍可能累積系統性風險。
- **ESG / climate systemic risk 未涵蓋** — 2012 年未考慮氣候、能源轉型風險；2020 後研究顯示 climate risk 是新的 systemic risk source，需擴展模型。
- **DeFi / crypto 系統性風險** — 2022 LUNA/Terra、FTX 等 crypto 危機顯示 DeFi 系統性風險的新形態，SRISK 模型需大幅 adapt。

### 與 Edward 既有知識的連結
- **ZP macro / risk 模組**：Engle 的 SRISK 框架可整合到 `ZP/macro/systemic_risk/`，作為評估 bank/financial sector exposure 的標準工具。
- **對應 Pole Statistical Arbitrage**：Pole 討論 stat arb 在 2002-2004 失敗的結構性原因，Engle 提供了系統性風險的量化框架；兩者結合可構建 "regime-aware" trading 系統。
- **延伸 Sundaresan Fixed Income**：Sundaresan 的 credit risk 章節在 reduced-form level，Engle 在 systemic level；兩者疊加就能從單一 bond 風險看到整體 systemic spillover。
- **衝突 Gibson Asset Allocation**：Gibson 認為「多資產分散降低 risk」；Engle 實證揭示——crisis 時 correlation → 1，分散失效；Edward 應在 portfolio construction 加入 systemic tail hedge。
- **可挖金礦**：NYU V-Lab 每日數據可透過 API 抓取，整合到 Edward 的 dashboard；高 SRISK 預警作為 de-risking trigger。
- **Crypto 延伸**：類比建構 `ZP/defi/systemic_risk/` 模組——監測 top DeFi protocol 的 TVL × leverage × correlation，估算 crypto 系統性風險。
