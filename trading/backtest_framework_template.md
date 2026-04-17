# Backtest Framework Spec — Template

> Generic methodology template. Personal parameters stripped.
> Source: 投資交易 consolidation 2026-04-17.

---

## 目標

建一個最小可用的台指期策略回測系統。能做到：
1. 載入歷史 K 線數據（台指期 1min/5min/日K）
2. 定義策略邏輯（進場/出場/停損/停利）
3. 跑回測 → 產出績效報告（PnL/MDD/MAE/MFE/勝率/期望值）
4. IS/OOS 分割 → 比較落差
5. 多策略批次跑 → 排序

---

## 技術選擇

| 項目 | 選擇 | 理由 |
|------|------|------|
| 語言 | Python | 生態系完整 |
| 回測引擎 | 自建（不用 backtrader/zipline）| 「先窄後寬」+ 完全控制 MAE/MFE 計算 |
| 數據格式 | CSV / Parquet | 簡單，不依賴外部 DB |
| 績效計算 | 自建（MAE/MFE/DD/FitnessValue）| 對齊自有評分邏輯 |
| 可選加速 | VectorBT | 先用 naive loop，有需要再換 |

---

## 模組設計

```
backtest/
├── data/           # 數據載入 + 清洗
│   └── loader.py   # load_klines(symbol, timeframe, start, end) → DataFrame
├── strategy/       # 策略定義
│   └── base.py     # Strategy ABC: on_bar(bar) → Signal
├── engine/         # 回測引擎
│   └── runner.py   # run(strategy, data) → TradeLog
├── metrics/        # 績效計算
│   └── stats.py    # calc_stats(trade_log) → {pnl, mdd, mae, mfe, win_rate, ev, sharpe}
│   └── oos.py      # split_is_oos(data, ratio) + compare(is_stats, oos_stats)
├── report/         # 報告輸出
│   └── summary.py  # print_summary + export_csv
└── main.py         # CLI entry point
```

---

## 第一個策略（MVP 驗證用）

**均線交叉**（最簡單，用來驗證框架，不期待盈利）
- 進場：MA5 上穿 MA20
- 出場：MA5 下穿 MA20
- 停損：-2%
- 部位：1 口台指期

---

## 數據來源

1. **免費**：Yahoo Finance API（日K，延遲）
2. **付費**：嘉實資訊、精誠資訊（tick/分K，即時）
3. 第一步用免費日K 驗證框架。真正上線需要分K 數據。

---

## IS/OOS 篩選標準（參考值，需依策略特性校準）

```
淘汰 = OOS 績效 vs IS 績效落差過大
具體（參考起點，非固定值）：
- MDD_OOS / MDD_IS > 1.5x → 警告
- MDD_OOS / MDD_IS > 2.0x → 淘汰
- Sharpe_OOS / Sharpe_IS < 0.5 → 淘汰
- Win_rate 方向翻轉 → 直接淘汰
```

---

## 執行計畫

| Step | 內容 | 預估 |
|------|------|------|
| 1 | data/loader.py（Yahoo Finance 台指期日K）| 30 min |
| 2 | strategy/base.py + 均線交叉策略 | 30 min |
| 3 | engine/runner.py（naive loop backtester）| 1 hr |
| 4 | metrics/stats.py（PnL/MDD/MAE/MFE）| 1 hr |
| 5 | metrics/oos.py（IS/OOS split + compare）| 30 min |
| 6 | 跑一次完整回測 → 產出報告 | 30 min |
| 7 | Review + 調整 | depends |

---

## 市場分類框架（通用）

```
Step 0: 市場分類（最重要）
  辨識長期模式：往上 / 往下 / 震盪
  ↓
Step 1: 順勢追價型（長期趨勢市場）
  主力做趨勢方向 + 反向 = hedge
  避險拆分：當盤（當沖避開高走低）+ 隔日（避跳空）
  理想權益曲線 = 階梯狀（下跌空手 + 上漲滿倉）
  ↓
Step 2: 逆勢回歸型（長期震盪市場）
  蛛網來回：波動度自適應 + 偏離合理範圍 → 高拋低接
  ↓
Step 3: 選擇權
  賺時間價值（theta decay）
  ↓
Step 4: 跨市場擴展
  CB / 債 / crypto / polymarket — 有機會就嘗試
  回測成本 ≈ 0（AI 時代）
```

## 長期目標

框架驗證後 → 市場分類器 → 順勢+避險模組 → 逆勢模組 → 選擇權 → 跨市場 → 產生 cash flow。
