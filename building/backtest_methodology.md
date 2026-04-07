# 回測方法論

> 從零到自主交易的完整流程。2026-04-07 實戰萃取。

---

## 核心原則

1. **Walk-forward > single IS/OOS split** — 單一分割會騙人，walk-forward（N=5+窗口）才是真相
2. **Game selection > strategy optimization** — 先掃全市場，再在最好的市場優化。「台指期冠軍不如 BTC pr80」
3. **Staircase equity curve** — 理想不是 45 度角，是階梯狀（flat→jump→flat→jump）
4. **簡單平均 > 最佳化權重** — Equal weight ≈ risk parity when strategies have similar MDD

---

## 流程

```
Step 0: 市場掃描（game selection）
  多市場 × 基線策略 → 排序 OOS expectancy → 只做 top 1-2

Step 1: 策略開發
  趨勢市場 → trend-following / momentum
  震盪市場 → mean reversion
  多時間框架 → 慢TF用MR，快TF用momentum

Step 2: Walk-forward 驗證
  N=5 rolling windows
  通過標準：>60% windows positive
  淘汰：OOS vs IS 落差 > 2x MDD ratio

Step 3: Portfolio 組合
  多策略相關性檢查（目標 < 0.3）
  Equal weight（除非有強理由不等權）
  Combined staircase score

Step 4: Paper trading
  自動化（cron + state persistence）
  最少 1 周觀察
  無 real signal = 正確（bias toward inaction）

Step 5: Real money
  API key + 最小部位
  菱形加碼 [2,3,3,2]（確認後才放大）
```

---

## 實測結果（2026-04-07）

| 市場 | WF 結果 | 結論 |
|------|---------|------|
| BTC daily MR | 4/5 ✅ | 主力 |
| BTC 4H MR | 4/5 ✅ | 補充 |
| BTC 1H Momentum | 4/5 ✅ | 補充 |
| Gold daily | 0-2/5 ❌ | 跳過 |
| TAIEX | negative ❌ | 跳過 |
| ETH/SOL 1H | marginal | 跳過 |

Portfolio correlation: -0.04（近零 = 理想）
