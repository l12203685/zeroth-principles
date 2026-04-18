# Hands-On Machine Learning with Scikit-Learn and TensorFlow — Aurélien Géron

### 目錄
1. 核心本質 — ML 是「從資料學習」的工程紀律，不是魔法
2. 可用戰術 — 專案流程、特徵工程、交叉驗證、集成法
3. 盲點/反例 — ML 在金融資料上的失敗模式
4. 與 Edward 既有知識的連結

### TL;DR
Géron (O'Reilly 2017, Part I Scikit-Learn + Part II TensorFlow，共 16 章) 把機器學習當作**可重複的專案工程**在教：Chapter 1-2 奠定「端到端 ML 專案」八階段流水線（framing→data→explore→prepare→short-list→fine-tune→deploy），Chapter 3-8 涵蓋經典監督式（SVM、Tree、Ensemble、Dimensionality reduction），Part II (Ch 9-16) 切入深度學習（CNN、RNN、Autoencoder、RL）。全書最深刻的反覆訓誡只有三句：**先做 test set 分割再探索資料**（避免 data snooping bias，Ch 2）、**始終監控 overfit**（bias/variance tradeoff，Ch 4）、**用 ensemble 打破單模型極限**（Ch 7 voting/bagging/boosting/stacking）。工程紀律優先於演算法新穎度，這點對投資策略程式化至關重要。

### 核心本質
1. **Data snooping bias 比 overfitting 更隱蔽（Ch 2 Create a Test Set）**：Géron 寫「your brain is an amazing pattern detection system, which means that it is highly prone to overfitting」——人腦先看到 test set 內的 pattern 會污染模型選擇。他的工程解法是用 instance identifier hash（latitude\*1000+longitude）而非 random split，確保新資料進來時舊 test set 不被污染。這是單次回測與長期 live trading 表現不對稱的根源：quant 團隊把 sample 內 feature engineering 做爛，實質上是訓練者自己記得 test 分布。
2. **Stratified sampling vs. random sampling（Ch 2 Figure 2-10）**：Géron 用 California housing 示範——median income 決定房價，隨機抽樣會讓 test set 的 income 分布偏斜 >12%，strat sampling 讓比例誤差 <0.5%。映射到金融：回測若未按 regime（高/低波動、牛/熊）分層抽樣，樣本外績效的信賴區間會嚴重低估。
3. **Bias-Variance Tradeoff 與正則化（Ch 4 Gradient Descent / Regularized Models）**：Ridge/Lasso/ElasticNet 不是「提高準確度」的工具，是「限制模型複雜度」的手段。Géron 強調 learning curves 是診斷的王道——training error 平坦 + validation error 高 = high bias；兩條之間有大 gap = high variance。
4. **Ensemble 的核心假設是「弱相關」（Ch 7 Voting Classifiers / Random Forests / Gradient Boosting）**：Law of large numbers 只有在多分類器犯獨立錯誤時才會生效；若所有模型都用同樣資料同樣特徵，ensemble 等同單模型。Random Forest 靠 bootstrap 抽樣 + 特徵子集 + Extra-Trees 的 random split 強制 decorrelation，Gradient Boosting 則靠「對殘差訓練下一棵樹」讓每一層正交。
5. **Curse of Dimensionality 的幾何詮釋（Ch 8）**：Géron 用「1,000,000-d hypercube 內兩隨機點的平均距離 ≈ 408」這個反直覺事實，說明高維空間內所有點都「邊緣化」——ML 模型在高維的外插非常不可靠。這給所有聲稱用 100+ factor 來預測股價的模型敲警鐘。

### 可用戰術
1. **端到端 ML Project Checklist（Appendix B）**：把任何策略回測當作 ML 專案走 8 steps: Frame the Problem → Get the Data → Explore → Prepare → Short-list Models → Fine-tune → Present Solution → Launch/Monitor/Maintain。這正是我 ZP 的 `B2/backtest` 應該套用的骨架。
2. **Sklearn Pipeline + GridSearchCV（Ch 2）**：把「缺失值補齊 → 特徵縮放 → 特徵衍生 → 模型」封裝成 Pipeline object，搭配 GridSearchCV 做 hyperparameter tuning，自動化交叉驗證。產線化策略時可直接沿用。
3. **Early stopping + warm_start（Ch 7）**：Gradient Boosting 用 `warm_start=True` 加逐輪 validation error 監測，連續 5 輪不降就停。回測時用在參數（如 momentum window）上可避免過度調參。
4. **StratifiedShuffleSplit 替代 KFold（Ch 2-3）**：處理類別不平衡（如「爆倉事件」佔 <1% 的情況）時強制類別比例保留，分類器不會只學到 majority class。
5. **PCA / Kernel PCA 當特徵壓縮而非降噪（Ch 8）**：保留 95% variance 的 PCA 可把 100 維壓到 10 維，加速訓練且降低 overfit 風險；但若目標是預測 tail event，PCA 會把關鍵的 tail feature 壓掉，要配合 inverse_transform 檢查重建誤差。

### 盲點/反例
1. **California housing 是 IID 資料，金融時間序列不是**：Géron 全書用 Bay Area 房價等靜態截面資料（Ch 2-8），沒處理 autocorrelation、non-stationarity、structural break。財經 ML 若直接把 train_test_split 套到時間序列會造成未來洩漏；應改用 time-based split（如 sklearn 的 TimeSeriesSplit）或 Lopez de Prado 的 Purged K-Fold + Embargo。
2. **Random Forest 在 low SNR 的金融資料上常不如 OLS**：Ch 7 的例子都是強訊號 dataset（MNIST 手寫數字）。股市 daily return 的信噪比 <1:100，RF 容易用 spurious split 過度擬合。實證：Gu, Kelly & Xiu (RFS 2020) 指出 neural net > tree > linear 在預測 US equity return 時只差 ~0.3% R²。
3. **Deep Learning 需要大量資料和算力（Ch 13-14 CNN/RNN）**：Géron 自己在 Caution 段落寫「Deep Learning is best suited for... provided you have enough data, computing power, and patience」——金融時間序列每天 252 筆，30 年 ~7500 筆，LSTM 在這麼少樣本上過擬合是常態。RNN 對 regime shift 也缺乏自動重訓機制。
4. **2017 年出版，Scikit-Learn 0.19 API 與 TF 1.x**：部分語法（如 `tf.Session()`）已在 TF 2.0+ 廢棄；sklearn 0.23+ 改用 HistGradientBoostingRegressor，速度比書中 GradientBoostingRegressor 快 10x。讀者須同步看書配合最新官方 docs。
5. **Ensemble 假設無法延伸到決策相關（crisis）**：Ch 7 的多樣性假設在 2008/2020 這類所有因子同向崩潰時失效，這時 ensemble 只會放大錯誤。

### 與 Edward 既有知識的連結
- **對照 Round 1 Kelly-Xiu《Financial Machine Learning》**：Kelly-Xiu 是「金融專用」的 ML 書，處理 non-stationarity / low SNR；Géron 是「通用 ML 工程」的教科書。兩本配合看才完整：Géron 教工具與流程，Kelly-Xiu 教金融場域的特殊限制與修正。
- **對照 Lantz《Machine Learning with R》（Round 1）**：Lantz 教 R tidyverse 框架下的 ML，Géron 教 Python/sklearn；程式語言選擇差異，概念重疊度 70%。ZP 專案若走 Python，Géron 是首選參考。
- **對照 ZP/strategies/ml_signals 架構**：我目前的 ML signal pipeline 缺乏 Appendix B Project Checklist 的「Launch/Monitor/Maintain」階段——上線後 feature drift、concept drift 的重新訓練觸發條件沒寫清楚。應補上 PSI（Population Stability Index）或 KS-test 做 monitor。
- **對照 DNA §8 的 Zero-6 個性（Conscientiousness 高）**：Géron 的 Project Checklist 八階段流程與 Zero-6 「系統化、可重複、可追溯」本能完全契合；用他的 framework 當作 quant dev 團隊 onboarding 教材會比《新 HFT》那類 trading-focused 書更結構化。
- **對照 Poker 的機率估計**：Géron Ch 3 教 confusion matrix / precision-recall / ROC-AUC，本質上就是 poker 裡區分「sklansky group」vs.「實戰 value bet」的精準度問題。high recall low precision = 看到 AA 都進場但也看錯 5-4 offsuit；high precision low recall = 只進 AA KK 但錯過大量 +EV 邊際場。回測策略也一樣，勝率 vs. 期望值的權衡。
