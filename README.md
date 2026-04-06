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
│   ├── framework.md              本質思維三步引擎 + 五大公設 + Feedback Loop 護城河
│   └── avalon.md                 阿瓦隆推理方法論（六公理 + Bayesian 更新）
├── building/
│   ├── philosophy.md             為什麼建這些東西
│   ├── trading_system.md         量化交易系統設計哲學 + 策略核心機制 + Alt-Data 框架
│   ├── trading_core/             量化交易統一函式庫（Python, 18 modules）
│   ├── investment_first_principles.md  六大投資第一性定律
│   └── 量化交易哲學_英文思考文章.txt
└── agent/
    └── prompt.md                 AI Agent 啟動提示詞（公開版）
```

## 如何使用

**給 AI**：讀 `agent/prompt.md`，再讀 `thinking/framework.md`。
**給人類**：從 `thinking/framework.md` 開始，再看 `building/investment_first_principles.md`。
**給開發者**：`building/trading_core/` 是可直接使用的量化交易函式庫。

---

*活文件。隨認知迭代更新。*

| 版本 | 日期 | 說明 |
|------|------|------|
| v1.0 | 2026-03-28 | 初始版本（原 digital-edward） |
| v1.1 | 2026-03-28 | 重命名為 zeroth-principles，移除個人資訊 |
| v2.0 | 2026-04-06 | 大幅擴充：trading_core 函式庫、策略核心機制、投資定律、Feedback Loop 框架、財神爺 Alt-Data |
