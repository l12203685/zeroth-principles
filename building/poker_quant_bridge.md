# Poker → Trading 量化橋接

> Poker 是不完整資訊博弈的最佳訓練場。
> 所有在 poker 發展的量化工具，直接移植到交易。

---

## 統一數學框架

| 概念 | Poker 實作 | Trading 實作 |
|------|-----------|-------------|
| Risk of Ruin | `exp(-2 × bankroll × bb/100 / std²)` | `exp(-2 × capital × edge / drawdown_std²)` |
| Kelly Criterion | `f = win_rate + 1 - 1/odds` | `f = (b×p - q) / b`，實務半 Kelly |
| Monte Carlo | 300K hands × 1K players | 期貨策略 drawdown distribution |
| Drawdown from peak | `df - df.cummax()` | 同一視覺化 |
| EV calculation | bb/100 over large sample | 每筆交易期望值 |
| Variance management | Bankroll in buy-ins | Position sizing in ATR units |

---

## Poker 量化方法論

### Cash Game Analysis
- 核心指標：bb/100（每百手大盲贏率）+ std（標準差）
- 大樣本才有統計意義（>30K hands）
- Drawdown 視覺化：cumulative sum + cummax → max drawdown

### MTT (Multi-Table Tournament) Simulation
- ITM（入錢圈）率 18-21%
- Payout structure: quadratic weighting（FT 重賞）
- Rake 10% = long-run EV drag
- 需 500+ 錦標賽樣本才能區分 skill vs variance

### Risk of Ruin
$$RoR = \left(\frac{1 - (2p-1)}{1 + (2p-1)}\right)^u$$

- p = win probability per unit
- u = bankroll in units (buy-ins)
- RoR < 5% = acceptable risk level

---

## 跨域遷移

### Poker GTO → 交易
- **Range thinking** → 不猜單一價格，考慮所有可能情境的機率分布
- **Position** → 資訊優勢（後手行動 = 更多資訊 = 更好決策）
- **Bluff frequency** → 假突破頻率（市場也有 bluff）
- **Pot odds** → 風險報酬比（賺賠比 = pot odds）

### Poker Variance → 交易 Drawdown
- Cash game: 30K hands 可能持續虧損（純 variance）
- Trading: 100 筆交易可能持續虧損（系統仍正 EV）
- 區分 variance vs edge loss 的方法：Runs Test + 統計假設檢定

### MTT Payout → 選擇權 Payoff
- MTT: 大部分人輸光（out of money），少數人大贏（deep in the money）
- 選擇權買方：多數到期歸零，少數大賺
- 同一數學結構：fat-tail distribution, positive skew

---

## 核心洞見

> **Poker 教你的不是怎麼贏，是怎麼在不確定中存活。**

1. 短期結果無意義（variance dominates）
2. 只有大樣本下的 EV 才是真實
3. Bankroll management > Strategy selection
4. 情緒管理（tilt）= 交易中的 overtrading/revenge trading
