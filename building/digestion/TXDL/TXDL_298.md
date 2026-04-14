# TXDL_298 — TXDL_1_020_WeekTrade01

> Batch 296-314 digestion, 2026-04-14 +08.
> Source: `E:/@交易/@AVAVA/Keep/!_TXDL_1_020_WeekTrade01/!_TXDL_1_020_WeekTrade01.txt`

## 核心論點
只在週四、週五進場做 1 週持倉，週末強制平倉

## 本質原理
週末留倉心理成本 > 邊際 Sharpe；心理可持續性也是 edge

## 策略摘要
2106_Ivan_TX_WeekTrade20k_LT — TAIEX 20-min weekly-swing (Mon-Fri close-out) to avoid weekend holding risk. Filters: Thu/Fri only, non-settlement, skip first 30 min and last bar, max 2 entries/week. Entry: close > weekly open + today's weak price > yesterday's strong price + 60-min high breakout. Trailing stops use entry-day low then prev-two-day low. Moving exit triggered after profit > STP(285) or 5-day avg HL * golden ratio. Profit target 2x STP. Weekly sweep at Fri close; Mon-resume with gap-down stop. Friday/settlement entries use tighter day-trade-like thresholds.

## Edward 視角 take-away
風險=心理續航力被低估；週沖 template 值得 port 進 trading_core 當 low-stress 套餐

## 參考
- digestion_log.jsonl entry timestamp: `2026-04-14T10:45:02+08:00`
- tier: 1
