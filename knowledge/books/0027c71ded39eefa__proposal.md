## proposal — 未標示
**來源**: E:/課程/資訊工程_計算機程式設計/proposal.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **1. 這個期末程式佔總成績30%，比期中考還重，所以請同學自己規劃時間進度**
- **2. Demo 安排在6/24 晚上、6/25 晚上和6/28 下午（詳細規劃另行公佈在課程網頁上）**
- **3. 繳交方式為Demo 前上傳至助教FTP**
- **4. 報告不用上傳，請印出帶來Demo，詳細規格請見第九節說明**
- **5. 若在期限內沒辦法完成，還是請準時來Demo，助教跟老師會依完成度給部份分數**
- **1. 定義一個struct User，裡面需包含單一使用者的所有資訊，包話帳號、密碼、login**
- **2. 需先讓使用者輸入username 和password**
- **3. 依這個username 到檔案users.txt 裡面尋找是否有相同的，若有且檢驗其密碼正確，**
- **4. 主選單中有六個選項，分別是 (1)猜數字遊戲 (2)撲克牌遊戲 (3)自創遊戲 (4)查看紀**
- **5. 選到0 則結束遊戲，在結束前需先將使用者所有資料，寫回users.txt**

### TL;DR (≤120字)
本書屬於 game theory poker 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **GTO 是不被剝削的下限,exploitative 才是追求上限的模式** — 兩者取捨依對手群體而定
2. **Range vs Hand 思維是核心轉換** — 只想自己手牌是業餘,思考對方 range 才是專業
3. **EV 決策 ≠ 結果決策** — long run EV 才是技能標準,短期 variance 會掩蓋技能差距

### 可用戰術/策略

- 用 solver 驗證關鍵決策點,建立自己的 GTO baseline 再針對池子偏態做 exploit
- 持續紀錄 HUD 統計,量化自己與對手的泄漏 (leak),系統化修正

### 盲點 / 反例 / 適用邊界

- 純 GTO 在低注有池對抗 calling station 會 lose EV,過度追求理論純度忽略對手池實情

### 與 Edward 既有知識的連結

- 呼應零式原則 *population_exploit* — 群眾偏態可以反向 +EV 佈局
- 呼應零式原則 *meta_strategy_over_strategy* — 關注資金曲線與長期夏普、勝過單筆交易或單期回報

<!-- QA_FAIL: extract_below_10k_chars, OCR re-extraction queued -->
