## 期權制勝——指數期權快速上手 18 課 — 金曹 (Jin Cao)
**來源**: E:/書籍/期權制勝——指數期權快速上手18課 (201819增訂版) by 金曹 (z-lib.org).pdf  |  **消化日**: 2026-04-18  |  **模型**: sonnet-4.6

### 目錄
- 第一課 期權的基本定義（Call/Put、Strike、Expiry、Premium、Moneyness）
- 第二課 四大角色（Buyer/Seller、Call/Put 組合）
- 第三課 時間價值與內涵價值
- 第四課 Greeks 入門（Delta/Gamma/Theta/Vega/Rho）
- 第五課 隱含波動率與 IV Smile/Skew
- 第六課 Put-Call Parity 與套利
- 第七課 方向性策略（Long Call/Long Put、Protective Put）
- 第八課 中性策略（Straddle、Strangle）
- 第九課 價差策略（Bull/Bear Spread、Calendar Spread、Diagonal）
- 第十課 蝶式/鷹式（Butterfly、Iron Condor、Iron Butterfly）
- 第十一課 合成部位（Synthetic Long/Short、Conversion/Reversal）
- 第十二課 VIX 與波動率交易
- 第十三課 指數期權特性（歐式 vs 美式、現金交割）
- 第十四課 保證金機制（SPAN、Portfolio Margin）
- 第十五課 事件交易（Earnings、FOMC、Election）
- 第十六課 動態對沖（Delta Hedging、Gamma Scalping）
- 第十七課 風險管理（VaR、尾部風險、Black Swan 防護）
- 第十八課 實戰案例與進階技巧

### TL;DR (≤120字)
針對香港/中國讀者寫的指數期權（恒指期權/滬深 300 指數期權）快速入門 18 課，從基本定義到 Greeks、從策略到風控。最大特色是以恒指期權為主要案例，補足了英文教材缺乏的亞洲市場細節（如合約規格、保證金、交割時間）。作者金曹是港 ETF 與期權實戰派，內容實用而非學院派。

### 核心本質 (3-5 條)
1. **期權的四種角色本質是「風險重分配」**（本質，第 2 課） — 買方支付權利金獲得非對稱回報（有限損失 + 潛在大利）、賣方收取權利金承擔非對稱風險（有限利潤 + 潛在大損）。任何策略都是這四角色的組合，理解此本質勝過死背公式。
2. **時間價值是期權賣方的飯票**（本質，第 3、4 課） — 平均每日 θ 衰減是賣方獲利主引擎；但 θ 在臨近到期加速（gamma 爆發），賣方需動態管理。作者強調：近月期權 θ/premium 比遠月高 3-5 倍，效率更高但風險也更大。
3. **IV Skew 是市場對尾部風險的定價**（本質，第 5 課） — 股指期權 put 的 IV 永遠高於 call（保險需求不對稱），此 skew 大小反映市場恐慌程度；VIX 是 30 日 ATM IV 加權平均，但 skew 更細粒度揭示市場情緒。
4. **Iron Condor 本質是賣雙邊波動**（本質，第 10 課） — 賣 OTM call + 賣 OTM put + 買更 OTM 兩邊保護 = 壓注「指數窄幅震盪」；作者警告：看似「每月穩賺」但單一黑天鵝即可抹掉一年收益（如 2015 年 A 股熔斷、2020 年 COVID）。
5. **動態對沖的 Gamma Scalping 是 volatility 交易核心**（本質，第 16 課） — Long Gamma（買 straddle）做 delta hedge 可在震盪市中持續套利波動幅度；若實現波動率 > 隱含波動率即獲利。此邏輯是做市商與 prop shop 的主線。

### 可用戰術/策略
- **恒指期權 Iron Condor 每月**：賣當月 delta ±0.15 call/put，買外側 100 點保護；目標收權利金 0.5-1% 每月、最大虧 4-5%。
- **Calendar Spread 事件交易**：事件前賣近月買遠月 put/call，賺事件後 IV crush（近月 IV 暴跌 > 遠月）。作者給出 FOMC 前後實戰案例。
- **VIX Term Structure 套利**：VIX 期貨 contango 陡峭時做空 VXX（ETF），backwardation 時做多；歷史上年化 10-15% 但 2018 年 2 月 XIV 暴雷是極限風險提醒。
- **Protective Put Collar**：持有指數 ETF + 賣 OTM call 收權利金 + 買 OTM put 防黑天鵝；零成本 collar 可鎖定 -5% 到 +5% 的月報酬。
- **Gamma Scalping**：買 ATM straddle、每日依 delta 變化動態調整現貨倉位，賺「實現波動率 > 隱含波動率」的差；作者給出 HSBC、騰訊的實戰案例。

### 盲點 / 反例 / 適用邊界
- **偏港股指數**：作者以恒指期權為主，A 股/美股/台股細節未涵蓋；如恒指 vs S&P 500 的 skew 結構差異 30%。
- **2018 後市場結構變化**：增訂版為 2018 年，未涵蓋 0-DTE 期權（SPX daily expiration）、WallStreetBets 散戶逼空、2022 高通膨下期權市場變化。
- **保證金章節偏淺**：SPAN 與 portfolio margin 僅簡述，實務上保證金算法細節決定槓桿能開多大，專業交易者需再補。
- **Iron Condor 的 left tail 風險低估**：作者描述為「穩定月收」，但歷史上 Iron Condor 策略在 2008、2011、2015、2020 皆有爆倉紀錄；應合併尾部保險。
- **缺少數學推導**：期權定價（Black-Scholes PDE、Heston、SABR）只用白話解釋，對想進階到 quant 角色的讀者需補 Higham/Bennett。

### 與 Edward 既有知識的連結
- **對齊 ZP 自營系統選擇權模組**：作者 18 課結構可作為 ZP/options/ 的入門課程範本；Edward 可直接復用章節架構開發台指選擇權策略。
- **延伸既有 DNA**：§4 階段性完成——作者「每月穩收 0.5-1%」是現實預期，而非「月報酬 5%」的神話；這種期望管理符合 Edward 經濟自給的理性規劃。
- **衝突點**：作者推崇賣方策略穩定月收，Taleb《反脆弱》主張「賣方是撿硬幣，站在壓路機前」；Edward 需明確策略在自己的 bankroll 尺度是否屬於可承受 ruin 的區段。
- **可挖金礦**：第 12 課 VIX term structure 套利 + 第 16 課 Gamma Scalping 可直接用於 ZP 波動率交易子策略。
- **對接 Bennett《Trading Volatility》**：金曹第 16 課的 Gamma Scalping 與 Bennett Part V 完全對應；兩本書可互補——金曹教入門、Bennett 教進階數學。
