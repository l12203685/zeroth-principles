# Principles of Financial Engineering (2ed) — Salih N. Neftci

### 目錄
1. 核心本質 — 財務工程是「合成品組合」的學問
2. 可用戰術 — Synthetic / Replication / Swap engineering / Convexity
3. 盲點/反例 — 2008 後 derivatives 市場結構轉型
4. 與 Edward 既有知識的連結

### TL;DR
Neftci 2ed (Academic Press/Elsevier 2008, 25 章) 是 Hong Kong UST + New School 教授 Salih Neftci 寫的財務工程實務教科書，有別於 Hull《Options Futures and Other Derivatives》的百科全書風格，Neftci 聚焦在**「如何用基本元件組合出目標 payoff」**——每章以「some problem → synthetic solution → contractual equation」展開：Ch 1-3 基礎（cash flow engineering, forward contract）、Ch 4-5 利率衍生品與 swap engineering、Ch 6 repo market、Ch 7 dynamic replication methods、Ch 8-11 options (mechanics, Greeks, convexity, option strategies)、Ch 12-15 pricing tools (risk-neutral, BSM, PDE, Monte Carlo)、Ch 16-20 fixed income pricing (bootstrap, LIBOR market model, credit default swap)、Ch 21-25 advanced (exotics, securitization, CDO, counterparty risk, commodity & energy)。**核心概念**：每個 derivative 都可用現金 + 基本 building blocks（stock、bond、forward、option）「合成」出來；若市場價格 ≠ 合成成本，則存在套利。這個「contractual equation」框架讓讀者看穿所有產品的本質。

### 核心本質
1. **Contractual Equation 是財務工程的核心語言（Ch 3.6）**：任何衍生品都可寫成 Σα_i · Instrument_i = 0 的等式。例：FRA = long short-term deposit + short long-term deposit 的合成組合。LIBOR-OIS basis swap = 1-year LIBOR payer - 1-year OIS receiver。這個等式思維讓你立即看出：若 observed FRA rate ≠ synthetic，套利空間在哪。
2. **Synthetic Replication 有 static vs. dynamic 兩類（Ch 7）**：Static replication 用 fixed basket，例如 forward contract = long spot + short deposit；Dynamic replication 需要連續調整，例如 BSM 中的 delta hedge。Static 較 robust 但只適用有限產品（linear payoff）；Dynamic 覆蓋面廣但承受模型風險——hedge error ≈ ∫(realized vol² - implied vol²)·Γ dt。
3. **Swap Engineering 是 rates 市場的通用語言（Ch 5）**：Plain vanilla IRS = 兩個債券的差（fixed bond - floating bond），premium 是 par swap rate；Currency swap = two single-currency bonds + FX leg；Cross-currency basis swap 的 spread 來自不同 country 的 funding advantage 差異（e.g., USD funding 稀缺時歐洲銀行付 premium 借 USD）。2008 後 LIBOR-OIS basis 大幅擴大反映 counterparty risk premium。
4. **Convexity 是非線性 payoff 的來源（Ch 9）**：Bond 價格對 yield 是 convex 函數——yield 降 1% 的價格漲 > yield 升 1% 的價格跌。這個 second-order effect 被 delta hedge 忽略。Neftci 示範 long bond + short 同 duration 的 IRS 可鎖定 convexity value，而 bullet call + bullet put 的 straddle 是純 convexity play。
5. **Quanto Adjustment 是跨幣別衍生品的隱含成本（Ch 9.5）**：Nikkei 225 以 USD 結算的 option（quanto）= JPY nominal payoff × fixed FX rate。若 JPY/USD 與 Nikkei 相關，risk-neutral pricing 要加 quanto adjustment：drift 修正項 = -ρ·σ_S·σ_FX。實證日本 JPY 與 Nikkei 負相關，quanto Nikkei call 的 implied drift 比標準 Nikkei call 低約 1-2%。

### 可用戰術
1. **Cash-and-Carry Arbitrage（Ch 3.7）**：long spot + short forward = arbitrage if 實際 forward > synthetic (= spot·(1+r)^T)。實務操作在 gold、crude oil 等實物商品常見；當 contango 陡峭時 physical trader 儲油賺 carry。
2. **Callable Bond Decomposition（Ch 10）**：callable bond = plain bond + short embedded call (on the bond)。投資人賣了 call 給 issuer，換取較高 coupon。duration 分析要扣除 call 的負凸性——低利率環境 callable bond 的 effective duration 遠低於 maturity。
3. **Repo Market Strategies（Ch 6.5）**：(a) specials trade：某特定券在 repo 市場 demand 特別高，repo rate 可比 general collateral 低 50-100bps，賺 specialness premium；(b) butterfly bond strategy：用 repo 融資買中期券、賣短+長期券，賺 curve belly steepening。
4. **Dynamic Replication 下的 Gamma Trading（Ch 7.5）**：delta-hedged long gamma option 的 P&L = ½·Γ·(realized return)² - option's theta decay。若 realized vol > implied vol 就賺錢。配合期權交易員的 realized - implied spread 估計是每日 P&L source。
5. **Cross-Currency Basis Trade（Ch 5.11）**：post-GFC 的 EUR-USD basis 長期負（-40 to -80 bps）——持有 USD 的機構願意借出 USD 換 EUR 要收 premium。利用此 basis 的 synthetic USD funding（EUR-denominated 資產 + FX hedge）vs. direct USD funding 可賺 carry。

### 盲點/反例
1. **2008 出版，post-crisis reform 未涵蓋**：Dodd-Frank, EMIR, clearing mandate, SA-CCR counterparty risk, SOFR transition 全部在 Neftci 之後。2020+ derivatives market 的結構已完全轉型——讀者要補 Gregory《Counterparty Credit Risk and Credit Value Adjustment》。
2. **LIBOR-based 範例已過時**：LIBOR 2023 年底退場，SOFR、SONIA、ESTR 成為主流。書中 FRA、swap 大量用 LIBOR 當 benchmark，概念仍適用但 quote convention 要更新。
3. **Credit Derivatives 章節相對簡單**：Ch 21 CDS + Ch 22 CDO 只基礎介紹，沒 CDX/iTraxx index mechanics、single-name CDS roll、sovereign CDS 的特殊性。要補 Schmid（本輪）或 Frontiers QF（本輪）Part II。
4. **Commodity 章節（Ch 25）偏油/金簡述**：電力、天然氣、農產品、軟性商品的 basis risk、storage 特殊性沒展開。做 energy trading 要補 Eydeland-Wolyniec《Energy and Power Risk Management》。
5. **Salih Neftci 2009 去世**：沒再有新版，2014 之後的 rate crisis, negative rate period, LDI crisis 等新現象都沒這本的注解；只能從 2ed 基礎推論。

### 與 Edward 既有知識的連結
- **對照 Hull《Options Futures and Other Derivatives》**：Hull 是百科全書（覆蓋 instruments 多但淺），Neftci 是 problem-solving approach（覆蓋少但深入）。學生用 Hull 記憶各種 instruments，實戰 quant 用 Neftci 培養 engineering 思維。
- **對照 Sundaresan《Fixed Income Markets》（Round 1）**：Sundaresan 是 rates market 機構結構為主，Neftci 是 rates instrument engineering 為主。兩本互補——前者教「這市場長什麼樣」，後者教「怎麼在這市場設計產品」。
- **對照 Brigo-Mercurio《Interest Rate Models》（Round 1）**：BM 是 rates 隨機模型（數學），Neftci 是 rates instruments 工程（應用）。Neftci Ch 4-5 的 FRA/swap engineering 是 BM 模型的實物對照。
- **對照 ZP 的「第一性原理」思維**：Neftci 的 contractual equation 方法符合 Edward 的「回本質推理」——任何新產品先拆成 primitive block（spot, forward, option），再看 market price vs. synthetic 差距；這比「記公式」更可延伸。
- **對照 Poker 的 range construction**：Neftci 的 synthetic 方法類比 poker 的 range balancing——每個 action（bet/check/raise）都是不同 hand combination 的「組合」，對手看到 action 後反推 range。Poker strategist 與 financial engineer 都在做「從基本元件構造複雜結構」的工作。
