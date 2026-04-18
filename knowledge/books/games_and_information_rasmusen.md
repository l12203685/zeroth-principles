## Games and Information: An Introduction to Game Theory — Eric Rasmusen（3ed, 2000）
**來源**: staging/b2_batch_E_extracts/c59c96f913546858__games_and_information_an_introduction_to_game_theory_3ed_200.md | **消化日**: 2026-04-18 | **模型**: opus-4.7 | **Round**: llm_round_6

### 目錄
- Part I Game Theory
  - Ch1 Rules of the Game（Prisoner's Dilemma、Iterated Dominance、Nash、Focal Points）
  - Ch2 Information（Extensive Form、Information Sets、Perfect/Certain/Symmetric/Complete、Harsanyi Transformation、Bayesian Games）
  - Ch3 Continuous and Mixed Strategies（Welfare Game、Chicken、War of Attrition、Correlated Strategies、Civic Duty、Auditing、Cournot）
  - Ch4 Dynamic Games with Symmetric Information（Subgame Perfectness、Entry Deterrence、Credible Threats、Pareto Perfection）
  - Ch5 Reputation and Repeated Games（Chainstore Paradox、Folk Theorem、Product Quality、Hawk-Dove）
  - Ch6 Dynamic Games with Incomplete Information（Perfect Bayesian、PhD Admissions、Common Knowledge、Gang of Four Model、Axelrod Tournament）
- Part II Asymmetric Information
  - Ch7-8 Moral Hazard（Principal-Agent、Broadway Game、Efficiency Wages、Tournaments、Teams）
  - Ch9 Adverse Selection（Lemons、Insurance、Kyle Model of Market Microstructure）
- Part III（後半章節）Mechanism Design、Signalling、Bargaining

### TL;DR (≤120字)
Rasmusen 是應用博弈論最經典的研究所教材，特色是**每個概念都用具體模型（約 100+ 具名範例）說明**：Boxed Pigs, Entry Deterrence, Broadway Game, Kyle Model, PhD Admissions。書的重心是**資訊非對稱**（Moral Hazard、Adverse Selection、Signalling）——這是現代微觀經濟學與金融市場微結構的核心工具。Ch9 收錄 Kyle (1985) 市場微結構模型，直接連結到高頻交易與 informed trading 研究。

### 核心本質 (3-5 條)
1. **Harsanyi Transformation：轉化不完全信息為完全信息**（本質，Ch2.4） — Harsanyi 1967-68 提出的深刻想法：不完全信息博弈（你不知道對手的報酬函數）可**轉化**為 Nature 先選擇「types」的完全信息博弈。這讓 Bayesian Nash 成為可計算對象，為保險、合約、拍賣等應用打開大門（Harsanyi 1994 諾貝爾獎）。
2. **Chainstore Paradox（連鎖店悖論）**（本質，Ch5.1） — 連鎖店面對多地潛在進入者：若用「一律打擊」威脅，backward induction 證明不可信（最後一個進入者必然被允許，逆推到第一個也被允許）。但實驗與現實均顯示威脅常被相信——Selten 1978 用此表明「完美理性」假設的極限。
3. **Folk Theorem：無限重複博弈中合作可持續**（本質，Ch5.2） — 只要折現因子 δ 夠大（未來報酬權重高），幾乎任何「可行且個人理性」的報酬組合都可作為 Nash 均衡支撐。這解釋了為何長期商業關係、國際外交、OTC market-making 中，即使單次博弈是 Prisoner's Dilemma，合作仍可穩定（例如 Axelrod Tournament 的 Tit-for-Tat 策略）。
4. **Kyle Model (1985)：Adverse Selection 的市場微結構應用**（本質，Ch9.5） — 單一 informed trader（有內幕）+ noise traders + market maker（需從 order flow 推斷是否有 insider）。解出：市場深度 λ（價格對 order size 的敏感度）= σ_v / (2σ_u)，即資產波動性 / 噪音交易波動性之比。這是解釋 bid-ask spread 的經典模型，Hasbrouck、Foster-Viswanathan 等都基於此延伸。
5. **Principal-Agent 與最適合約**（本質，Ch7） — 委託人（股東、董事會）無法觀察代理人（CEO、員工）努力，只觀察結果。最適合約平衡 IR（參與）、IC（誘因相容）、競爭約束；通常形式為「績效獎金 + 底薪」。解釋為何 CEO 薪酬與股價掛鉤、為何對沖基金收取 20% performance fee。

### 可用戰術/策略
- **Entry Deterrence via Commitment**：位於市場的老公司可藉由「過量建廠」（sunk cost）使降價打擊新進入者變得可信，從而嚇阻進入。應用：新創公司評估「巨頭反擊能力」時關注其固定成本結構。
- **Tit-for-Tat 於重複 PD**：Axelrod Tournament 中，Anatol Rapoport 的 TFT 策略（首輪合作、之後照搬對手上一輪）獲勝。啟示：合作時直接報復、原諒時迅速回歸合作；對長期商業、聯盟談判極具啟發。
- **Signalling by Costly Action**：高品質的新創公司願意自掏腰包買下市場、接受低估值 IPO，作為「我夠好」的訊號；低品質者模仿成本太高所以放棄。
- **Mechanism Design 反向設計**：想要特定結果，設計誘因結構讓玩家「自願」達成。應用：Incentive pay structure、Tax policy、Dynamic pricing。
- **Market Microstructure 實戰**：Kyle Model 指出 market depth 正比於真實波動率 / 噪音波動率；實戰若觀察到 spread 突然變窄，可能暗示 insider 消失或 noise trader 增加——這是短線擠壓前兆的線索。

### 盲點 / 反例 / 適用邊界
- **模型簡化嚴重**：Kyle Model 假設單一 insider、noise traders 是外生常態；現實市場有多個 informed、跨資產訊息流動，實證偏離大。
- **行為經濟學衝擊**：書中所有模型假設理性玩家；Thaler、Kahneman 的實驗證據顯示人類系統性偏誤，需補充行為博弈論（Camerer 2003）。
- **多重均衡選擇**：許多模型有多個 PBE，書中無統一 refinement；應用時需依賴 focal points 或 forward induction（Kohlberg-Mertens）。
- **計算複雜性**：大型博弈求解需數值方法（Homotopy continuation、Gambit 軟體）；書中推導是小型解析例子，大型實證需程式工具。
- **忽略動態演化與網絡效應**：對平台經濟（Uber、抖音）的 multi-sided network externalities 解釋不足；需補充 Jackson 《Social and Economic Networks》。

### 與 Edward 既有知識的連結
- **對齊 ZP 零式本質**：Information asymmetry 是交易的根源——若所有人知道相同資訊，無交易發生（Milgrom-Stokey no-trade theorem）。這給 Edward 的 edge 尋找提供框架：尋找信息不對稱的環節。
- **對接 Kyle Model 與微結構研究**：ZP/knowledge 已有 Kyle 1989 等論文（book_id: 00408f9526906c75__kyle_1989_res）；本書 Ch9.5 提供理論背景。
- **撲克應用深入**：Repeated Games + Reputation 解釋為何撲克場「歷史悠久的 regular」比「新來生面孔」更易詐唬成功——reputation 建立信號成本。
- **衝突點**：Rasmusen 的理性框架與 Taleb 的 fat-tails / 不可計算性有張力；Edward 需在「策略選擇」階段用博弈論、在「尺度與風控」階段用 Taleb。
- **可挖金礦**：Kyle Model + Foster-Viswanathan 擴展模型可整合入 B1T3 的微結構策略；Principal-Agent 章節對設計自營交易團隊的薪酬結構有直接應用。
