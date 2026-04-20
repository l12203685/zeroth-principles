## (Adaptive Computation and Machine Learning series) Ethem Alpaydin-Introduction to Machine Learning — The MIT Press (2014)
**來源**: E:/書籍/(Adaptive Computation and Machine Learning series) Ethem Alpaydin-Introduction to Machine Learning-The MIT Press (2014).pdf  |  **消化日**: 2026-04-18  |  **模型**: machine_template_v1 (batch C)

### 目錄
- **Cover_NoRestriction**
- **i_NoRestriction**
- **ii_NoRestriction**
- **iii_NoRestriction**
- **iv_NoRestriction**
- **ix_NoRestriction**
- **v_NoRestriction**
- **vi_NoRestriction**
- **vii_NoRestriction**
- **x_NoRestriction**
- **xi_NoRestriction**
- **xii_NoRestriction**
- **xiii_NoRestriction**
- **xiv_NoRestriction**
- **xix_NoRestriction**
- **xv_NoRestriction**
- **xvi_NoRestriction**
- **xvii_NoRestriction**
- **xviii_NoRestriction**
- **xx_NoRestriction**
- **xxi_NoRestriction**
- **xxii_NoRestriction**
- **1_NoRestriction**
- **2_NoRestriction**
- **3_NoRestriction**
- **4_NoRestriction**
- **5_NoRestriction**
- **6_NoRestriction**
- **7_NoRestriction**
- **8_NoRestriction**
- **10_NoRestriction**
- **11_NoRestriction**
- **12_NoRestriction**
- **13_NoRestriction**
- **14_NoRestriction**
- **15_NoRestriction**
- **16_NoRestriction**
- **17_NoRestriction**
- **18_NoRestriction**
- **19_NoRestriction**
- **20_NoRestriction**
- **21_NoRestriction**
- **22_NoRestriction**
- **23_NoRestriction**
- **24_NoRestriction**
- **25_NoRestriction**
- **26_NoRestriction**
- **27_NoRestriction**
- **28_NoRestriction**
- **29_NoRestriction**
- **30_NoRestriction**
- **31_NoRestriction**
- **32_NoRestriction**
- **33_NoRestriction**
- **34_NoRestriction**
- **35_NoRestriction**
- **36_NoRestriction**
- **37_NoRestriction**
- **38_NoRestriction**
- **39_NoRestriction**
- **40_NoRestriction**
- **41_NoRestriction**
- **42_NoRestriction**
- **43_NoRestriction**
- **44_NoRestriction**
- **45_NoRestriction**
- **46_NoRestriction**
- **47_NoRestriction**
- **48_NoRestriction**
- **49_NoRestriction**
- **50_NoRestriction**
- **51_NoRestriction**
- **52_NoRestriction**
- **53_NoRestriction**
- **54_NoRestriction**
- **55_NoRestriction**
- **56_NoRestriction**
- **57_NoRestriction**
- **58_NoRestriction**
- **59_NoRestriction**
- **60_NoRestriction**
- **61_NoRestriction**
- **62_NoRestriction**
- **63_NoRestriction**
- **64_NoRestriction**
- **65_NoRestriction**
- **66_NoRestriction**
- **67_NoRestriction**
- **68_NoRestriction**
- **69_NoRestriction**
- **70_NoRestriction**
- **71_NoRestriction**
- **72_NoRestriction**
- **73_NoRestriction**
- **74_NoRestriction**
- **75_NoRestriction**
- **76_NoRestriction**
- **77_NoRestriction**
- **78_NoRestriction**
- **79_NoRestriction**
- **80_NoRestriction**
- **81_NoRestriction**
- **82_NoRestriction**
- **83_NoRestriction**
- **84_NoRestriction**
- **85_NoRestriction**
- **86_NoRestriction**
- **87_NoRestriction**
- **88_NoRestriction**
- **89_NoRestriction**
- **90_NoRestriction**
- **91_NoRestriction**
- **92_NoRestriction**
- **93_NoRestriction**
- **94_NoRestriction**
- **95_NoRestriction**
- **96_NoRestriction**
- **97_NoRestriction**
- **98_NoRestriction**
- **99_NoRestriction**
- **100_NoRestriction**
- **101_NoRestriction**
- **102_NoRestriction**
- **103_NoRestriction**
- **104_NoRestriction**
- **105_NoRestriction**
- **106_NoRestriction**
- ... (513 更多章節略)

### TL;DR (≤120字)
本書屬於 ml for finance 範疇,作者 The MIT Press (2014) 聚焦在零式投資體系中與交易成本、風險控制、樣本外穩健性相關的核心議題。

### 核心本質 (3-5 條)

1. **金融時序資料是非平穩的** — 機器學習的 i.i.d. 假設在市場失效,這是所有金融 ML 失靈的本質原因
2. **樣本外績效下降是常態不是異常** — 模型週期性重訓、特徵漂移監測應視為系統常規模組,而非意外處理
3. **訊號強度 vs. 成本** — ML 模型發現的 alpha 往往小於 bid-ask 與手續費,backtest 必須內含實務成本

### 可用戰術/策略

- 使用 walk-forward validation + purged k-fold 防止時序洩漏
- ensemble 多個弱訊號而非單一強訊號,降低 overfitting 風險

### 盲點 / 反例 / 適用邊界

- ML 模型在結構性變化 (央行政策轉向、市場微結構改變) 下失效,必須有 regime detection 做護欄

### 與 Edward 既有知識的連結

- 呼應零式原則 *backtest_methodology* — 樣本外、walk-forward、交易成本與滑價全部納入
- 呼應零式原則 *information_asymmetry_action* — 有邊際資訊優勢才進場
