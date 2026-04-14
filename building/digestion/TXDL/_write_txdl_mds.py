"""Generate per-strategy TXDL_NNN.md files from batch 296-314 digestion log.
B2 pipeline — Edward-view take-aways added. 2026-04-14."""
from __future__ import annotations

import json
from pathlib import Path

ZP_DIR = Path("C:/Users/admin/ZP/building/digestion/TXDL")
LOG = Path("C:/Users/admin/workspace/digital-immortality/results/digestion_log.jsonl")

# Take-away per strategy (Edward / zeroth-principles lens)
TAKEAWAYS: dict[str, tuple[str, str, str]] = {
    # slug -> (core_thesis, essence_principle, edward_takeaway)
    "TXDL_1_017_Transformer01": (
        "一支策略同時跑 swing + day-trade，結算窗內做反手",
        "單一 edge 難以覆蓋全週期；多模式協作=釋放自由度而非疊加風險",
        "Transformer 思路可移植到我的 shadow-live — 主 swing + 輔 day 保趨勢；結算後 2 天 mean-reversion 窗是 TXF 特殊結構性窗口"
    ),
    "TXDL_1_020_DCC01": (
        "DonChian 通道 + 長 EMA 只抓最強勢突破",
        "通道=波動自適應，長 EMA=趨勢基座，兩者過濾小雜訊",
        "把 DCC 當 feature，不必當主策略；長 EMA(320) on 20-min = 約 6 天 — 合理中期尺度"
    ),
    "TXDL_1_020_WeekTrade01": (
        "只在週四、週五進場做 1 週持倉，週末強制平倉",
        "週末留倉心理成本 > 邊際 Sharpe；心理可持續性也是 edge",
        "風險=心理續航力被低估；週沖 template 值得 port 進 trading_core 當 low-stress 套餐"
    ),
    "TXDL_1_022_VHF01": (
        "VHF 判別 trending vs choppy；兩種進場、四種出場",
        "Regime detection > signal timing；對 regime 誤判=策略結構性死亡",
        "VHF 是 DNA_v18 提過的 regime filter；值得獨立抽成 module 給其他策略用"
    ),
    "TXDL_1_023_ASI01": (
        "ASI 擺動指數穿越均線為主軸 + Guava 極值 7% 反手",
        "指標穿越是 trigger，固定 7% 才是極值 guard — 兩者互補",
        "ASI 非主流但 Wilder 家族；用於 TXF 表現可接受，當 diversifier 而非主軸"
    ),
    "TXDL_1_023_ASI02": (
        "拿掉 WF，用固定參數證明結構本身有 edge",
        "不是所有參數都該 WF；過 WF=over-fit 風險；結構比參數重要",
        "v2 哲學 = 穩定性 > peak PF；每個主策略都該有 no-WF 基線驗證"
    ),
    "TXDL_1_023_ASI03": (
        "ASI 同一指標衍生 3 版 WF/非WF/偏好版",
        "一個 signal source 可以多版擴散；diversification 不一定要換指標",
        "三版可 ensemble — 權重不等，非對稱結構抗單一 alpha 衰退"
    ),
    "TXDL_1_024_3DHL": (
        "3 日高低 + 固定停利停損；Edward 否決最佳 WF 結果",
        "最佳化不等於最可執行；回撤容忍度也是策略一部分",
        "operator-in-the-loop — 不盲從 optimizer；股本心理=隱形約束，必須建模"
    ),
    "TXDL_1_025_3GP01": (
        "前兩日收紅/黑 K 體 + 關價突破",
        "形態（body）+ 價格（breakout）組合濾網比單一強度高",
        "body pattern 濾網值得 port 進 ZP pattern library；可量化為 feature"
    ),
    "TXDL_1_029_MA+ATR01": (
        "ATR 穩定時順勢突破；ATR 爆發時逆勢撿便宜",
        "波動 regime 不同=邏輯必須切換；單一 style 無法適應雙 regime",
        "vol-regime switching 是 shadow-live 必備；ATR 可當 regime label 輸入模型"
    ),
    "TXDL_1_030_CT01": (
        "無腦跳空進場 + over-heat filter 救命",
        "minimalism=edge — 當複雜策略在特殊 regime 崩潰，簡單常存活",
        "AV 反轉月崩盤倖存者；simplicity budget 當作 portfolio 一部分非零"
    ),
    "TXDL_1_030_MA+CT01": (
        "KC 擴張後的回檔才進場 pyramid",
        "不是第一次突破最好，第二次（經確認）的勝率更高",
        "pullback re-entry 是進階耐心題；我易 FOMO 追首破，需寫入自律 rule"
    ),
    "TXDL_1_030_MTM01": (
        "動量指標雙進場 + 五出場 stack",
        "exit 多樣化=每種失敗模式都有對應 kill-switch",
        "exit stack 比 entry 值得投資；把 5-exit 拆成通用 exit module"
    ),
    "TXDL_1_030_RSI01": (
        "RSI cross + 閾值 boost/floor 非對稱進場",
        "RSI 不對稱閾值回映市場買賣力量的不對稱性",
        "對稱並非預設；不對稱閾值=反映 TXF 多頭偏多結構，可量化"
    ),
    "TXDL_1_032_KC01": (
        "Keltner 上軌失守 + 小紅 K + 破昨高=放空",
        "指標失效 + 形態 + 價格 三重確認才反手",
        "三重確認門檻=低訊號率但高準度；交易次數少但品質高適合低頻 live"
    ),
    "TXDL_1_050_Gap01": (
        "昨日與前日 close 夾住今日開盤=gap-between 進場",
        "gap 相對位置比 gap 絕對值更重要；夾帶=結構性訊號",
        "gap-between 是 TXF 特色；港股、美股未必成立 — 不可移植假設"
    ),
    "TXDL_1_060_BB01": (
        "布林突破 + 第一根高點 + ATR 約束 + 季線避免陷阱",
        "指標+時序+量能+關鍵均線 四層疊加",
        "BB 策略通常過擬合；此版用季線 context 是聰明處 — 可學"
    ),
    "TXDL_1_060_LR01": (
        "Linear Regression 曲線趨勢基座 + 3 日波幅當風險單位",
        "趨勢基座 + 波動縮放 = 自適應風險預算",
        "LR 比 MA 更 noise-robust；3 日 HL 當風險單位值得通用化"
    ),
    "TXDL_1_075_DR01": (
        "緩漲戰 vs 急噴戰區分；範圍擴張後抓強勢日進場",
        "不同 momentum profile 需要不同進場時序",
        "momentum profile labeling 是下一代 feature engineering 重點"
    ),
}


def slug_from_path(p: str) -> str:
    # E:/@交易/@AVAVA/Keep/!_TXDL_1_017_Transformer01/!_TXDL_1_017_Transformer01.txt
    # -> TXDL_1_017_Transformer01
    part = p.rsplit("/", 2)[-2].lstrip("!").lstrip("_")
    return part


def main() -> None:
    ZP_DIR.mkdir(parents=True, exist_ok=True)
    # load all log entries
    lines = LOG.read_text(encoding="utf-8").splitlines()
    entries = [json.loads(ln) for ln in lines if ln.strip()]
    # filter batch 296-314 — last 19 entries produced by this run
    batch = [e for e in entries if e.get("timestamp", "").startswith("2026-04-14T10:45")]
    if len(batch) != 19:
        # fallback: last 19
        batch = entries[-19:]
    start_num = 296
    written = 0
    for i, e in enumerate(batch):
        num = start_num + i
        slug = slug_from_path(e["path"])
        key = slug
        thesis, essence, takeaway = TAKEAWAYS.get(
            key,
            ("(未補)", "(未補)", "(未補)"),
        )
        content = f"""# TXDL_{num:03d} — {slug}

> Batch 296-314 digestion, 2026-04-14 +08.
> Source: `{e['path']}`

## 核心論點
{thesis}

## 本質原理
{essence}

## 策略摘要
{e['summary']}

## Edward 視角 take-away
{takeaway}

## 參考
- digestion_log.jsonl entry timestamp: `{e['timestamp']}`
- tier: {e['tier']}
"""
        out = ZP_DIR / f"TXDL_{num:03d}.md"
        out.write_text(content, encoding="utf-8")
        written += 1
    print(f"Wrote {written} TXDL_*.md files to {ZP_DIR}")


if __name__ == "__main__":
    main()
