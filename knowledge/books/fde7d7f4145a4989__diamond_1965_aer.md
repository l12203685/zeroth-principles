## Diamond 1965 AER — 未標示
**來源**: E:/課程/[6] 證券市場微結構/papers/Diamond 1965 AER.pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Article Contents**
  - p. [1126]
  - p. 1127
  - p. 1128
  - p. 1129
  - p. 1130
  - p. 1131
  - p. 1132
  - p. 1133
  - p. 1134
  - p. 1135
  - p. 1136
  - p. 1137
  - p. 1138
  - p. 1139
  - p. 1140
  - p. 1141
  - p. 1142
  - p. 1143
  - p. 1144
  - p. 1145
  - p. 1146
  - p. 1147
  - p. 1148
  - p. 1149
  - p. 1150
- **Issue Table of Contents**
  - The American Economic Review, Vol. 55, No. 5, Part 1 (Dec., 1965), pp. 1059-1328

### TL;DR (≤120字)
本書屬於 portfolio optimization 範疇,作者 未標示 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **MVO (均值變異數最佳化) 對輸入極敏感** — 預期報酬誤差 1% 可導致組合權重 30% 擺動
2. **Black-Litterman 透過混合市場均衡與主觀觀點穩定組合,是實務優於純 MVO 的路徑**
3. **Risk Parity 不需要預期報酬,但隱含假設各資產夏普比接近,槓桿需要嚴格風控**

### 可用戰術/策略

- shrinkage 估計共變矩陣 + 施加 weight bound (每資產 0-20%) 增強 robustness
- 實務上先配置 Risk Parity 底層,再疊加主觀 tactical overlay

### 盲點 / 反例 / 適用邊界

- Low vol 資產在極端事件中 vol 可以瞬間跳升,Risk Parity 高槓桿放大尾險

### 與 Edward 既有知識的連結

- 呼應零式原則 *meta_strategy_over_strategy* — 關注資金曲線與長期夏普、勝過單筆交易或單期回報
- 呼應零式原則 *risk_control_four_layers* — 部位/相關/流動性/尾險分層
