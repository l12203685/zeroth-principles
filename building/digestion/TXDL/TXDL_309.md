# TXDL_309 — TXDL_1_030_RSI01

> Batch 296-314 digestion, 2026-04-14 +08.
> Source: `E:/@交易/@AVAVA/Keep/!_TXDL_1_030_RSI01/!_TXDL_1_030_RSI01.txt`

## 核心論點
RSI cross + 閾值 boost/floor 非對稱進場

## 本質原理
RSI 不對稱閾值回映市場買賣力量的不對稱性

## 策略摘要
TAIEX 30-min RSI swing strategy. Entry: RSI crosses BuyLine from below = long; crosses SellLine from above = short. Boost: RSI climbs through 72 from below AND breaks prior day-high + 5pt = stronger long. Floor: once RSI falls back below 15, cheap-long on break of prior day-low - 5pt. Fixed stop SLPoint(60:135:15). Two flip-style exits using the mirror RSI threshold cross. Params RSILength 5:8:1, BuyLine 57:72:5, SellLine 5:20:5. Classic RSI cross with threshold-boost + threshold-floor asymmetric entries.

## Edward 視角 take-away
對稱並非預設；不對稱閾值=反映 TXF 多頭偏多結構，可量化

## 參考
- digestion_log.jsonl entry timestamp: `2026-04-14T10:45:13+08:00`
- tier: 1
