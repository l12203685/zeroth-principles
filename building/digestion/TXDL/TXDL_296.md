# TXDL_296 — TXDL_1_017_Transformer01

> Batch 296-314 digestion, 2026-04-14 +08.
> Source: `E:/@交易/@AVAVA/Keep/!_TXDL_1_017_Transformer01/!_TXDL_1_017_Transformer01.txt`

## 核心論點
一支策略同時跑 swing + day-trade，結算窗內做反手

## 本質原理
單一 edge 難以覆蓋全週期；多模式協作=釋放自由度而非疊加風險

## 策略摘要
$@LV@$__tx_TransFormer_17K_(DT)LT — TAIEX 17-min day-session hybrid day-trade + swing ('Transformer/Swingman'). Main logic: weekly midpoint ((highw(1)+loww(1))/2) defines medium-term bias; swing entry 3+ days after settlement, day-trade counter-weekly on mild pullback, auto-convert day-trade to swing if EOD profit reached. Post-settlement 2-day window reserved for counter-trend swing (institutions often close at settlement). Uses 三關價 (three-pivot) + weekly midpoint for stops that walk forward; no profit target — rides to settlement. WF TD param 3:11:1. Core essence: protect entry capital, let trend run till settlement.

## Edward 視角 take-away
Transformer 思路可移植到我的 shadow-live — 主 swing + 輔 day 保趨勢；結算後 2 天 mean-reversion 窗是 TXF 特殊結構性窗口

## 參考
- digestion_log.jsonl entry timestamp: `2026-04-14T10:45:00+08:00`
- tier: 1
