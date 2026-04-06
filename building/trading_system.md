# 量化交易系統設計哲學

## 核心原則

> 一致性 > 精確性。
> 存活率 > 報酬率。

---

## 交易憲法（邊界條件，不是建議）

```
不追漲 / 不攤平
單筆虧損上限：總資產 2%
停損設置後不移動
年度 MDD 上限：30%
```

違反任何一條 → 停下來問「發生了什麼」，不是繼續操作。

---

## 市場狀態機

市場有三種狀態，對應不同操作模式：

| 狀態 | 觸發條件 | 操作 |
|------|---------|------|
| 攻擊 | 月線+季線多頭 + ATR 低 | 高 Beta 加碼 |
| 防禦 | 月線空頭 + ATR 高 | 避險 / CTA |
| 中性 | 訊號模糊 | 等權持倉，等待清晰 |

**「不確定的時候，站回中性。」**

---

## 績效評估框架

### MAE / MFE

$$\text{MAE (long)} = \text{entry} - \min(\text{intra-trade low})$$
$$\text{MFE (long)} = \max(\text{intra-trade high}) - \text{entry}$$

$$\text{MAFE ratio} = \frac{\text{MAE}}{\text{MFE}}$$

低 MAFE ratio → 逆勢小，順勢大 → 好的風險報酬結構。

### 核心閾值

| 指標 | 目標 | 觸發重審 |
|------|------|---------|
| Profit Factor | 1.5 – 2.5 | < 1.5 |
| Expectancy | > 0 | ≤ 0 |
| 年度 MDD | < 30% | ≥ 30% |

---

## 策略矩陣

| 策略 | 核心邏輯 | 適用市況 |
|------|---------|---------|
| ORB | 開盤區間突破，捕捉早盤動能 | 趨勢日 |
| Resonance | 多週期趨勢共振入場 | 中期趨勢明確 |
| Prime K | 關鍵K棒結構判斷主力方向 | 盤整後突破 |
| Tofu | 窄幅區間來回收割 | 低波動橫盤 |

---

## 技術架構（trading_core）

從 17 個重複 repo 合併而來：

```
config/      環境變數管理
broker/      Singleton API 封裝（防多實例）
data/        OHLCV + 倉位管理
analytics/   績效指標 + MAE/MFE
strategy/    策略抽象基底
```

設計決策：所有憑證走 `.env`，不入版控。

---

## 策略核心機制（實戰驗證）

| 機制 | 說明 |
|------|------|
| **avgdis** | 通用自適應距離：`avg(max(\|Hi-C[-1]\|, \|Lo-C[-1]\|, \|Hi[-1]-Lo[-1]\|))`，clip [100,300]pts。同時驅動進場/停損/停利/追蹤出場。非固定參數，隨市場狀態調整。 |
| **Session-end entries** | 進場集中在 AM session 最後 N 分鐘（1m K線，time-gated）。偵測動量耗盡（price 二階導數）。收盤前均值回歸，非開盤追勢。 |
| **NH equity adaptive** | 追蹤策略是否正在創權益新高。NH mode: stops 收緊、倉位放鬆；Drawdown mode: 反之。系統化資金管理嵌入信號邏輯。 |
| **Daily cap** | `y+z < 2`：每日最多 1-2 筆進場，不管信號多少。結構性防過度交易。 |
| **Settlement full exit** | `LastTradeDay(d)` 無條件平倉所有部位。不跨結算。 |
| **SBF slope×kbar** | `slope = day_ATR(20) / day_len`（波動率正規化漂移率），乘以 session 開盤以來經過 bar 數。價格「飄夠遠」才進場——無指標的 momentum filter。 |
| **Reverse-entry on profit** | 獲利中遇到急反轉信號 → 翻倉（不只平倉）。同日捕捉反向行情。 |

**核心績效指標**：SQN 為主要系統品質信號（非只看 Sharpe）。
**成本模型**：手續費 0.025%/筆，最小 2.5 ticks，大台點值 200。

---

## 量化交易哲學

> "Huge bias toward inaction — top guys take a few big trades a year."

> "In efficient markets, active trading has negative EV against time-opportunity-cost baseline unless you have a structural edge."

結構性優勢 = 速度（自動化）+ 利基市場（台指期日內）+ 系統化不作為。

---

## Alternative Data 框架（財神爺）

一個用 user browsing behavior 預測股價的系統，展示 alternative data → signal 的完整流程。

**核心假說**：某些用戶的瀏覽行為能預測隔日股價漲跌。

**架構**：
1. Raw data: user browsing logs → stock code mapping
2. Per-user predictive power: avg(next-day return on days user browsed)
3. Noise filter: weight by `(10 - max(|highest gain|, |highest loss|)) / 10`（去除被漲跌幅吸引的 momentum chasers）
4. Confidence: rolling 15-65 day correlation between predicted and actual returns
5. Signal: weighted average of high-predictive-power users visiting today
6. Portfolio: top 5 stocks by expected return × confidence

**關鍵 insight**：「使用者會被漲跌幅騙進來」— 噪音過濾本身就是 edge。

**方法論原則**：
- 「驗證才是最難的部分，不要急著弄出太多假設」
- 「嘗試弄出最小的測試架構，抓大放小」
- 「找出最有價值的假設，排除最大的雜訊」
- 「可能只是運氣好」（+2% backtest → 保持懷疑）

直接對應本質三步引擎：strip noise → essential signal → minimum viable test。
