# TXDL_303 — TXDL_1_024_3DHL

> Batch 296-314 digestion, 2026-04-14 +08.
> Source: `E:/@交易/@AVAVA/Keep/!_TXDL_1_024_3DHL/!_TXDL_1_024_3DHL.txt`

## 核心論點
3 日高低 + 固定停利停損；Edward 否決最佳 WF 結果

## 本質原理
最佳化不等於最可執行；回撤容忍度也是策略一部分

## 策略摘要
3DHL_TX_24M LO — TAIEX 24-min day-session long-only based on 3-day high/low pivot structure. Params stp(575) profit target, stpl(45) stop-loss. Author notes netProfit maxed at stp=710 but refused due to retracement tolerance — example of discretionary override on optimization output. Uses 3-day rolling HL range to define entry pivots. Fixed stop + fixed target architecture. Cost $500 min + 1.5%. Max 1 contract. Demonstrates discipline: not every optimal WF param is accepted; equity-curve psychology overrides raw P/L optimum.

## Edward 視角 take-away
operator-in-the-loop — 不盲從 optimizer；股本心理=隱形約束，必須建模

## 參考
- digestion_log.jsonl entry timestamp: `2026-04-14T10:45:07+08:00`
- tier: 1
