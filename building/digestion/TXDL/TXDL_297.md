# TXDL_297 — TXDL_1_020_DCC01

> Batch 296-314 digestion, 2026-04-14 +08.
> Source: `E:/@交易/@AVAVA/Keep/!_TXDL_1_020_DCC01/!_TXDL_1_020_DCC01.txt`

## 核心論點
DonChian 通道 + 長 EMA 只抓最強勢突破

## 本質原理
通道=波動自適應，長 EMA=趨勢基座，兩者過濾小雜訊

## 策略摘要
GavinLu008_TX_DonChianChannel-D2106-K20m_LT — TAIEX 20-min day-session swing. Donchian Channel length 46 + EMA(320) trend filter. Entry: 2 consecutive breaks of DonChian upper/lower AND close on correct side of EMA(320). Four exits: (1) break-even stop after profit, (2) take-profit at maxRatio(5.8)x channel width, (3) stop-loss if losing + close reverts to DonAvg/EMA midline (best of two), (4) settlement close. Classic channel-breakout filtered by long EMA trend; only high-conviction moves trigger entry.

## Edward 視角 take-away
把 DCC 當 feature，不必當主策略；長 EMA(320) on 20-min = 約 6 天 — 合理中期尺度

## 參考
- digestion_log.jsonl entry timestamp: `2026-04-14T10:45:01+08:00`
- tier: 1
