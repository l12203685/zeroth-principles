# TXDL_313 — TXDL_1_060_LR01

> Batch 296-314 digestion, 2026-04-14 +08.
> Source: `E:/@交易/@AVAVA/Keep/!_TXDL_1_060_LR01/!_TXDL_1_060_LR01.txt`

## 核心論點
Linear Regression 曲線趨勢基座 + 3 日波幅當風險單位

## 本質原理
趨勢基座 + 波動縮放 = 自適應風險預算

## 策略摘要
No32_TX_LinearRegCurve_60K_LO_S — TAIEX 60-min day-session using MC-default LinearRegCurve. Entry: LR curve crosses upward to rising trend AND 3-day high-expansion range reached = break-high entry long; short mirrored. Exits: (1) 3-day high range stop-loss — large expansion = larger stop, small expansion = tight stop, (2) take-profit at 2x stop-value, (3) settlement close. WF Len 26:38:6, Vol 500:1000:100, NRatio 7:19:4. Param-tight; LR as trend substrate, 3-day range as volatility-adjusted risk unit.

## Edward 視角 take-away
LR 比 MA 更 noise-robust；3 日 HL 當風險單位值得通用化

## 參考
- digestion_log.jsonl entry timestamp: `2026-04-14T10:45:17+08:00`
- tier: 1
