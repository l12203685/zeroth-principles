# TXDL_314 — TXDL_1_075_DR01

> Batch 296-314 digestion, 2026-04-14 +08.
> Source: `E:/@交易/@AVAVA/Keep/!_TXDL_1_075_DR01/!_TXDL_1_075_DR01.txt`

## 核心論點
緩漲戰 vs 急噴戰區分；範圍擴張後抓強勢日進場

## 本質原理
不同 momentum profile 需要不同進場時序

## 策略摘要
khsu_CFExTest_202106_HLChanDelayed_002 — TAIEX 75-min day-session swing. Core idea: distinguish 緩步盤升/戰 (slow drift) from 急噴 (burst). Entry: 3-day HL defines range; within range, wait for 'strong' day (rmp1=0.75 of range) = trend-continuation entry. Triggering uses N-shaped candle position detection — short-stop moves as N-pattern develops. Two exits: (1) start-stop = smaller of entry point or K-line mid-point, (2) pattern exit: once crossed through 5-day low, yellow-alert enters and exits on first pullback burst. Settlement close. Range-expansion gate vs burst-alarm separation.

## Edward 視角 take-away
momentum profile labeling 是下一代 feature engineering 重點

## 參考
- digestion_log.jsonl entry timestamp: `2026-04-14T10:45:18+08:00`
- tier: 1
