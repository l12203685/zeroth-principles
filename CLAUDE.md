# zeroth-principles — Claude Code 啟動協議

> 這個 repo 是 Edward (林盈宏) 思維框架的公開版本。
> 個人資訊已脫敏。任何人或 AI 讀完可直接使用這套邏輯。

---

## 雙窗口系統說明

此 repo (`ZP`) 與私人代理人 repo (`LYH`) 並行運作：

```
Google Drive（原始資料）
    ├── 私人面 → LIN-YING-HUNG (LYH)   個人DNA、職涯、量化
    └── 公開面 → zeroth-principles (ZP)  思維框架、方法論（脫個資）
```

同一台電腦開兩個 VSCode 窗口：
- Window 1：`LYH/` 資料夾 → 私人 Claude Code
- Window 2：`ZP/` 資料夾（本 repo）→ 公開 Claude Code

---

## 啟動序列

```
1. 讀 agent/prompt.md          → 公開版 AI Agent 提示詞
2. 讀 thinking/framework.md    → 本質思維三步引擎
3. 讀 thinking/avalon.md       → 阿瓦隆推理方法論
4. 讀 building/philosophy.md   → 建造哲學
5. 如有 GDrive，掃描公開內容
6. 接收任務
```

---

## 核心識別

- **本質思維三步引擎**：剝離 → 本質 → 重建
- **核心公設**：一切都是資訊不完全下做出的選擇問題
- **決策方法**：Bayesian 更新 + 期望值最大化

---

## ZP 的職責範圍

| 屬於 ZP | 不屬於 ZP（屬於 LYH） |
|---------|---------------------|
| 思維框架（通用） | 個人 DNA、身份資訊 |
| 阿瓦隆推理方法論 | 量化策略細節（PLA/MR_Total 等） |
| 建造哲學（脫個資） | 職涯記錄、財務資料 |
| 公開版 Agent 提示詞 | Session log、工作記憶 |

---

## GDrive 內容分流原則

從 Google Drive 讀到的內容，判斷放 ZP 還是 LYH：

```
含個人姓名/身份/財務/帳號 → LYH（私人）
純方法論/框架/哲學/通用邏輯 → ZP（公開）
兩者兼有 → 脫個資後摘要放 ZP，原版放 LYH
```

---

## Git 工作流程

```bash
# 每次開始前
git pull origin master

# 完成後推送
git add -A
git commit -m "ZP vX.X: <更新說明>"
git push origin master

# 本機 clone（可用短名稱）
git clone https://github.com/l12203685/zeroth-principles.git ZP
```

Remote: `https://github.com/l12203685/zeroth-principles.git`

---

## 與 LYH 的同步節點

當 LYH 的 DNA 有重大框架更新時，評估是否提煉公開版本同步至 ZP：

1. LYH DNA 版本升級（如新增決策框架）
2. 脫個資處理
3. 更新 `thinking/framework.md` 或 `building/philosophy.md`
4. ZP push
