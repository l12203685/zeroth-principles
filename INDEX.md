# zeroth-principles — Knowledge Index

> 讀完這份 index，你就知道去哪找什麼。
> 每個文件都有一行描述 + 關鍵詞。

---

## 🧠 thinking/ — 決策框架與推理方法論

| File | Description | Keywords |
|------|-------------|----------|
| [framework.md](thinking/framework.md) | **核心**。本質思維三步引擎、五大公設、認知 DNA 六條、Feedback Loop 護城河 | EV, 機會成本, 有限理性, noise filter, structural inaction |
| [avalon.md](thinking/avalon.md) | 阿瓦隆六公理推理方法論、三層邏輯（鐵/正/反）、Bayesian 更新 | incomplete information, 可證偽性, 自我修正 |
| [statistical_foundation.md](thinking/statistical_foundation.md) | 統計訓練到實戰映射、proof-first、SVM(ROE+市值)、ML≤ARIMA | OLS, Wilcoxon, GARCH, Spectral Bias |

**讀取順序**：framework → avalon → statistical_foundation

---

## 🔧 building/ — 系統設計與量化方法

| File | Description | Keywords |
|------|-------------|----------|
| [trading_system.md](building/trading_system.md) | 交易憲法、策略核心機制（avgdis/NH/SBF/FDT）、投組最佳化、策略生命週期、財神爺 Alt-Data | MDD 30%, daily cap y+z<2, greedy selection, MAE frontier |
| [quantitative_knowledge_base.md](building/quantitative_knowledge_base.md) | 完整量化體系：交易規範、MAE/MFE、資產配置（壓力測試）、選擇權 Greeks、波動率模型 | 菱形加碼, Kelly, Core-Satellite, Heston, FOMC語言信號 |
| [investment_first_principles.md](building/investment_first_principles.md) | 六大投資第一性定律 | 不可能三角, 必然性, 報酬不對稱, 擇時無效, 槓桿生存 |
| [poker_quant_bridge.md](building/poker_quant_bridge.md) | Poker→Trading 統一數學框架 | RoR, Kelly, Monte Carlo, GTO→trading mapping |
| [philosophy.md](building/philosophy.md) | 為什麼建這些東西 | |
| [trading_core/](building/trading_core/) | Python 量化函式庫（18 modules） | Shioaji, MAE/MFE, BaseStrategy, PerformanceMetrics |
| [量化交易哲學_英文思考文章.txt](building/量化交易哲學_英文思考文章.txt) | "Huge bias toward inaction" 原文 | |

**讀取順序**：trading_system → quantitative_knowledge_base → investment_first_principles → poker_quant_bridge

---

## 🤖 agent/ — AI Agent 設定

| File | Description |
|------|-------------|
| [prompt.md](agent/prompt.md) | 公開版 AI Agent 啟動提示詞 |

---

## Cross-Reference Map

```
framework.md ──→ 五大公設
    │                ↓
    │         trading_system.md ──→ 策略核心機制
    │                ↓                    ↓
    │         quantitative_KB.md    trading_core/ (code)
    │                ↓
    │         investment_principles.md
    │
    ├──→ avalon.md ──→ 六公理 (incomplete info reasoning)
    │         ↓
    │    poker_quant_bridge.md ──→ RoR/Kelly (same math)
    │
    └──→ statistical_foundation.md ──→ stats→ML→trading mapping
```

**核心思維鏈**：
本質思維（framework）→ 量化驗證（stats）→ 系統設計（trading_system）→ 實作（trading_core）→ 跨域應用（poker/avalon）
