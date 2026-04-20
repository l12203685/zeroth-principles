# TXDL_299 — TXDL_1_022_VHF01

> Batch 296-314 digestion, 2026-04-14 +08.
> Source: `E:/@交易/@AVAVA/Keep/!_TXDL_1_022_VHF01/!_TXDL_1_022_VHF01.txt`

## 核心論點
VHF 判別 trending vs choppy；兩種進場、四種出場

## 本質原理
Regime detection > signal timing；對 regime 誤判=策略結構性死亡

## 策略摘要
2007TX_VHF_LinR_22K — TAIEX 22-min day-session. Two entry modes: (1) VHF (Vertical Horizontal Filter) directional + Linear Regression confirmation + session-time filter, (2) overnight-gap-in entry. Four exits: (1) PB2/2 pivot point reversal, (2) pb2 zone + VHF > average(VHF,10), (3) ATR-expansion widens stop loss, (4) settlement close. WF params PB2 245:320:15 and stpinput 17000:29000:2000. Demonstrates VHF as regime filter (trending vs choppy) combined with price-based Linear Regression trigger.

## Edward 視角 take-away
VHF 是 DNA_v18 提過的 regime filter；值得獨立抽成 module 給其他策略用

## 參考
- digestion_log.jsonl entry timestamp: `2026-04-14T10:45:03+08:00`
- tier: 1
