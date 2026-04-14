# TXDL_312 — TXDL_1_060_BB01

> Batch 296-314 digestion, 2026-04-14 +08.
> Source: `E:/@交易/@AVAVA/Keep/!_TXDL_1_060_BB01/!_TXDL_1_060_BB01.txt`

## 核心論點
布林突破 + 第一根高點 + ATR 約束 + 季線避免陷阱

## 本質原理
指標+時序+量能+關鍵均線 四層疊加

## 策略摘要
$2106K06_TX_BBand_LO — TAIEX 60-min day-session with Bollinger Band breakout. Entry: close > BB upper (BBLen=19, BBDev=1.5) + break of first-bar high + today's high < day-low + 1.5*ATR (avoid stretched bars) + exception: near quarterly MA (<20pt distance) with 2 prior losses, skip. Reverse: 3 bars after entry, RSI crosses over 80 then falls = flip short. Exits: (1) fixed stop, (2) fixed target STPratio(2.4)*stop, (3) after RSI flip, close falls into bottom 20% of BB width, (4) settlement. WF ATRLen, BBLen, BBDev, STPratio annually.

## Edward 視角 take-away
BB 策略通常過擬合；此版用季線 context 是聰明處 — 可學

## 參考
- digestion_log.jsonl entry timestamp: `2026-04-14T10:45:16+08:00`
- tier: 1
