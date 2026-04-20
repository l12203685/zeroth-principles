# TXDL_311 — TXDL_1_050_Gap01

> Batch 296-314 digestion, 2026-04-14 +08.
> Source: `E:/@交易/@AVAVA/Keep/!_TXDL_1_050_Gap01/!_TXDL_1_050_Gap01.txt`

## 核心論點
昨日與前日 close 夾住今日開盤=gap-between 進場

## 本質原理
gap 相對位置比 gap 絕對值更重要；夾帶=結構性訊號

## 策略摘要
yita_TX_50k_20210515_LO_003 — TAIEX 50-min day-session long-only. Single param in(3) for pivot-math. Setup: today's open is between closeD(1) and closeD(2) (gap-between) = pivot context. Entry: max(highD(0),highD(1)) stop-buy long; mirror short. Skip settlement, only when mp=0. Three exits: (1) half-day pass-through stop, (2) entry lasts >3 days AND floating losing AND entry-price gets breached = stop, (3) non-settlement day + break of entry-week's open = stop. 7-year stable PF > MDD with pf/mdd>1 for past 3 yrs. Example of minimal-param gap-inside-yesterday setup.

## Edward 視角 take-away
gap-between 是 TXF 特色；港股、美股未必成立 — 不可移植假設

## 參考
- digestion_log.jsonl entry timestamp: `2026-04-14T10:45:15+08:00`
- tier: 1
