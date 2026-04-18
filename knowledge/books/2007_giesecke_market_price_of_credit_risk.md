## The Market Price of Credit Risk — Kay Giesecke, Lisa R. Goldberg
**來源**: E:/投資交易/交易學習資料庫/@交易/2. 財務相關知識/papers/2007 Giesecke- MARKET PRICE OF CREDIT RISK.pdf  |  **消化日**: 2026-04-18  |  **模型**: opus 4.7

### 目錄
- **1 Introduction** (credit risk premium 經驗證據 + 既有文獻缺口)
- **2 The I² Model** (incomplete information 對 default barrier 的假設)
- **3 Space of Pricing Measures** (透過 Jacod 1977 martingale representation)
- **4 Risk Premium Decomposition** (Diffusive premium + Event premium)
- **5 Pricing Formulas for Credit-Sensitive Securities** (fractional recovery)
- **Appendix A** (probabilistic structure details)

### TL;DR (≤120字)
把信用風險溢酬拆為兩塊:diffusive premium (對公司價值波動的補償) 與 event premium (對違約跳躍不可預期性的補償)。透過「投資人對違約門檻資訊不完整」的 I² 模型,自然產出正的短期 credit spread,解決 Black-Cox / Leland 完整資訊結構模型無法解釋「信用違約突發性 + 短期 spread > 0」的缺陷。

### 核心本質 (3-5 條, 每條 50-120字)
1. **違約是不可預期事件,不是可觀測門檻觸發** — 完整資訊結構模型 (Merton / Black-Cox) 假設市場能觀測 distance-to-default,但實證上公司違約前股債常突然跳水,顯示市場並不完整掌握門檻位置。I² 模型將門檻當作 latent random variable,使違約成為 totally inaccessible stopping time。
2. **短期 credit spread > 0 的數學必要條件 = 資訊不完整** — 若投資人完全掌握 distance-to-default,第一-passage time 變成可預期事件,短期 spread 必趨近於零(與資料矛盾)。市場的「違約瞬間」驚嚇效應反映了 Knight 的 ambiguity,而非 Black-Scholes 式 risk。
3. **信用風險溢酬有兩個獨立來源** — diffusive premium = 價格波動補償(傳統 Sharpe-ratio 思維);event premium = 違約瞬間跳躍的風險嫌惡補償。實證(Berndt et al 2005、Collin-Dufresne et al 2002)顯示 event premium 是 credit spread 主成分之一,卻被純 diffusion 模型遺漏。
4. **Pricing measure 透過 Jacod martingale 表徵完整參數化** — 任一 pricing measure 可由 (Brownian drift 修正, default intensity ratio) 兩個 predictable process 決定。前者給 diffusive premium,後者給 event premium;數學結構乾淨,可逐項估計。
5. **Event premium 隨 running minimum firm value 而變** — 公司價值不斷觸及新低時,event premium 動態更新;這直接對應「逆境累積 → 違約機率跳升 → spread 擴張」的市場觀察。

### 可用戰術/策略
- **Credit spread 拆解為 benchmark** — 用模型對 corporate bond 或 CDS spread 做 two-component fit,剔除 diffusive premium 後剩下 event premium;若 event premium 突升 = 市場資訊惡化訊號,可作領先指標。
- **High-yield bond 交易 decision rule** — 在 event premium 高於歷史中位數時買入 (risk-on 補償較高),或避開 event premium 崩解預示的全面 risk-off 階段。結合 Cont stylized facts,形成一個「信用因子」策略。
- **Capital structure arbitrage signal** — Equity vs CDS 聯動關係在 I² 模型下明確;若 equity 下跌但 CDS 未擴,表示 latent barrier assumption 有 mispricing,可做 equity short + CDS long 的收斂交易(LTCM 後被謹慎使用)。
- **壓力測試情境生成** — 用 I² 模型 simulate「門檻突然在 running min 附近」的情境,回測策略在「違約叢生」期間的表現,測試尾部。

### 盲點 / 反例 / 適用邊界
- **GBM firm value + 單一 barrier 假設過簡** — 實務公司價值有跳躍(併購、會計醜聞)、門檻因債務結構而 state-dependent;I² 是 benchmark 而非 trading model。Merton 類結構模型都有共同批評:model-to-default 估計與市場 spread 有系統差異(credit spread puzzle)。
- **Jacod 1977 martingale representation 需要 uniform integrability** — 在 far-right tail / heavy-tail 環境下理論邊界模糊,估計量化誤差難界定。
- **忽略 contagion (違約傳染)** — 2008 次貸危機和 2020 COVID credit event 顯示單一公司獨立 default 假設會漏掉 systemic risk;需搭配 Duffie-Singleton copula 或 Hawkes process 補強。
- **需要高頻 CDS/bond 價格資料估計** — 對新興市場、民間公司違約研究仍困難;此模型多應用於 IG/HY 市場中具流動性標的。

### 與 Edward 既有知識的連結
- 連結 `derivative_over_level`:event premium 是對 default intensity 「跳變率」敏感的 derivative,正是零式第 1 條「rate-of-change + inflection」的量化實踐。
- 對應 `risk_control_four_layers` L3 (尾部保險):I² 模型告訴你 event jump 是 credit 資產的尾部主要風險源;對應的對沖是買 credit protection / CDS,並承認 diffusion 對沖不夠。
- 補強 `information_asymmetry_action`:I² 核心是「投資人資訊不完整 = pricing model 核心變量」,與零式第 2 條「資訊不對稱 → action」直接呼應;實務上可建置內部 fundamental research 蒐集 firm value 線索,建立相對 market 的 information edge。
- 對 B1 自營交易系統的貢獻:若系統擴充到固定收益/信用衍生品,建立 credit factor module 可直接用 I² 架構;spread decomposition 作為 daily signal,event premium 動能作為 proprietary factor。
