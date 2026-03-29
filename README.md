# zeroth-principles

> 比 first principles 更底層。從更根本的地方出發的思維工具集。

這是從實戰（量化交易 + 不完整資訊博弈）提煉出來的決策框架。
任何人或 AI 讀完可以直接使用這套邏輯。

## 核心主張

> **「一切都是資訊不完全下做出的選擇問題。」**

## 結構

```
zeroth-principles/
├── thinking/
│   ├── framework.md        本質思維三步引擎 + 五大公設
│   └── avalon.md           阿瓦隆推理方法論（六公理 + Bayesian 更新）
├── building/
│   ├── philosophy.md       為什麼建這些東西
│   └── trading_system.md   量化交易系統設計哲學
└── agent/
    └── prompt.md           AI Agent 啟動提示詞（公開版）
```

## 如何使用

**給 AI**：讀 `agent/prompt.md`，再讀 `thinking/framework.md`。
**給人類**：從 `thinking/framework.md` 開始。

### 30 秒 Quick Start

拿一個你現在面對的問題，跑一遍三步引擎：

```
1. 本質辨識：「這個問題拿掉所有修飾後是什麼？」
   例：「要不要學 Rust？」→「學 Rust 的 EV 是否 > 學其他語言或不學？」

2. 從零拆解：列出假設和變數
   → 假設：Rust 在我的領域有需求。可控：學習時間。不可控：市場需求變化。

3. 決策輸出：
   → 如果目標是系統程式 → 學，因為沒有替代品
   → 如果目標是快速出產品 → 不學，Python/Go 的 EV 更高
   → 第一步：花 30 分鐘查你目標領域的 Rust 職缺數量
```

---

*活文件。隨認知迭代更新。*

| 版本 | 日期 | 說明 |
|------|------|------|
| v1.0 | 2026-03-28 | 初始版本（原 digital-edward） |
| v1.1 | 2026-03-28 | 重命名為 zeroth-principles，移除個人資訊 |
| v1.2 | 2026-03-29 | 全文件內容補充：實戰範例、數值計算、策略細節、領域映射展開 |
