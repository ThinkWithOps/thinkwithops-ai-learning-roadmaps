# Season 4 Roadmap — Advanced Machine Learning Engineering

[← Season 4 overview](README.md) · [All seasons](../README.md)

**6 modules · 21 episodes · 88 topics · 227 subtopics · Level: Intermediate → Advanced**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Reliable Predictions on Hard Data](#s04-module-1)
- [Module 2 — Advanced Tabular Modeling](#s04-module-2)
- [Module 3 — Time Series and Forecasting](#s04-module-3)
- [Module 4 — Recommendation and Ranking Systems](#s04-module-4)
- [Module 5 — Specialized Problems and Responsible ML](#s04-module-5)
- [Module 6 — Experimentation, Causality, Automation, and System Design](#s04-module-6)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Move from "I can fit a model" to "I can deliver a trustworthy model on messy real problems": imbalance, uncertainty, time, ranking, anomalies, causal questions, automation (AutoML), explainability, fairness and system design. This is the ML-engineer core before deep learning.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S04E01 | Handle rare-event problems (fraud, failure, churn) without fooling yourself about performance. |
| S04E02 | Make model scores mean what they say and communicate how uncertain a prediction is. |
| S04E03 | Run search efficiently at scale and keep experiments comparable and reproducible. |
| S04E04 | Create powerful features from relational and temporal data while keeping them point-in-time correct. |
| S04E05 | Reduce features for robustness and cost, and systematically detect leakage. |
| S04E06 | Understand how modern boosting libraries differ internally and tune them with intent. |
| S04E07 | Combine models for accuracy gains while weighing complexity and serving cost. |
| S04E08 | Understand what makes temporal data different and evaluate forecasts without peeking at the future. |
| S04E09 | Choose among statistical, tree-based and neural forecasting approaches for a given problem. |
| S04E10 | Understand how systems predict preferences from interaction data. |
| S04E11 | Understand multi-stage recommendation and search architectures and how ranking quality is measured. |
| S04E12 | Detect rare or novel behavior with limited labels and manage false-positive cost. |
| S04E13 | Understand pre-transformer text techniques that remain strong baselines and underlie retrieval. |
| S04E14 | Explain individual and global model behavior and understand the limits of post-hoc explanations. |
| S04E15 | Measure and reduce unfair model behavior and understand why fairness criteria conflict. |
| S04E16 | Validate model changes in the real world safely and statistically soundly. |
| S04E17 | Reason about cause and effect from data, know what observational data can and cannot support, and choose an identification strategy. |
| S04E18 | Estimate who benefits from an action, use causal ML for targeting decisions, and evaluate policies from logged data. |
| S04E19 | Improve performance by improving data, and spend labeling effort where it counts. |
| S04E20 | Understand what automated machine learning automates, how each automated stage works internally, and where its limits and risks lie, so AutoML can be used as an engineering tool rather than a black box. |
| S04E21 | Combine requirements, data, modeling, evaluation and serving constraints into a coherent design for a tabular or ranking system. |

## Prerequisites and Expected Knowledge

- **Season 1 — [Python for AI & ML Engineering](../season-01-python-for-ai-ml/roadmap.md)**: S01E10
- **Season 2 — [Mathematics for AI & Machine Learning](../season-02-mathematics-for-ai/roadmap.md)**: S02E04, S02E13, S02E15, S02E16
- **Season 3 — [Machine Learning Foundations](../season-03-machine-learning/roadmap.md)**: S03E02, S03E03, S03E05, S03E06, S03E08, S03E09, S03E10, S03E11, S03E13, S03E14, S03E15, S03E16

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Reliable Predictions on Hard Data](#s04-module-1) | S04E01–S04E03 | 3 | 3 Intermediate |
| 2 | [Advanced Tabular Modeling](#s04-module-2) | S04E04–S04E07 | 4 | 3 Intermediate, 1 Advanced |
| 3 | [Time Series and Forecasting](#s04-module-3) | S04E08–S04E09 | 2 | 2 Intermediate |
| 4 | [Recommendation and Ranking Systems](#s04-module-4) | S04E10–S04E11 | 2 | 1 Intermediate, 1 Advanced |
| 5 | [Specialized Problems and Responsible ML](#s04-module-5) | S04E12–S04E15 | 4 | 4 Intermediate |
| 6 | [Experimentation, Causality, Automation, and System Design](#s04-module-6) | S04E16–S04E21 | 6 | 3 Intermediate, 3 Advanced |

<a id="s04-module-1"></a>

## Module 1 — Reliable Predictions on Hard Data

**3 episodes (S04E01–S04E03) · 13 topics.** This module covers: Imbalanced Data; Probability Calibration and Uncertainty; Hyperparameter Optimization and Experiment Discipline.

| ID | Episode | Depth |
|---|---|---|
| S04E01 | Imbalanced Data: Resampling, Class Weights, and Cost-Sensitive Learning | Intermediate |
| S04E02 | Probability Calibration and Uncertainty | Intermediate |
| S04E03 | Hyperparameter Optimization and Experiment Discipline | Intermediate |

### S04E01 — Imbalanced Data: Resampling, Class Weights, and Cost-Sensitive Learning

**Depth:** Intermediate  
**Learning objective:** Handle rare-event problems (fraud, failure, churn) without fooling yourself about performance.  
**Prerequisites:** S03E11, S03E15  
**Expected outcome:** Choose and validate an imbalance strategy and report metrics at the real prevalence.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Why Imbalance Breaks Models**

- Accuracy paradox and gradient dominance by the majority class
- Base rates and prevalence shift

**Topic 2 — Metrics That Survive Imbalance**

- PR-AUC, recall at fixed precision, cost-weighted metrics
- Why ROC-AUC can look good when positives are rare
- Choosing the operating point from business cost

**Topic 3 — Remedies**

- Class weights and cost-sensitive loss
- Oversampling, undersampling, SMOTE and their risks

**Topic 4 — Thresholds vs Resampling**

- Moving the decision threshold
- When each approach is appropriate

**Topic 5 — Doing It Safely**

- Resampling only inside training folds
- Calibration after resampling
- Evaluating at the true production base rate

</details>

**Important concepts**

- *Commands / APIs / Code:* `class_weight='balanced'`, `imbalanced-learn` pipelines, `precision_recall_curve`
- *Mechanisms & failure scenarios:* Synthetic samples leaking across folds, probabilities distorted by resampling, test set rebalanced and overstating results.

### S04E02 — Probability Calibration and Uncertainty

**Depth:** Intermediate  
**Learning objective:** Make model scores mean what they say and communicate how uncertain a prediction is.  
**Prerequisites:** S03E11, S02E13  
**Expected outcome:** Diagnose and fix poor calibration and set confidence-based decision rules.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Measuring Calibration**

- Reliability diagrams, Brier score, expected calibration error
- Why trees and boosted models are often miscalibrated

**Topic 2 — Calibration Methods**

- Platt scaling, isotonic regression, temperature scaling
- Calibrating on held-out data

**Topic 3 — Types of Uncertainty**

- Aleatoric vs epistemic uncertainty
- Ensembles and dropout as practical uncertainty estimates

**Topic 4 — Intervals and Guarantees**

- Quantile regression and prediction intervals
- Conformal prediction at concept level

**Topic 5 — Using Uncertainty**

- Abstention and human-review thresholds
- Risk-aware decisions and monitoring calibration over time

</details>

**Important concepts**

- *Commands / APIs / Code:* `CalibratedClassifierCV`, `calibration_curve`, quantile objectives in LightGBM
- *Mechanisms & failure scenarios:* Calibrating on training data, calibration decaying under drift, intervals with wrong coverage.

### S04E03 — Hyperparameter Optimization and Experiment Discipline

**Depth:** Intermediate  
**Learning objective:** Run search efficiently at scale and keep experiments comparable and reproducible.  
**Prerequisites:** S03E13  
**Expected outcome:** Design a bounded, reproducible tuning study and judge whether a gain is real.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Efficient Search**

- Bayesian optimization and tree-structured Parzen estimators
- Pruning and early termination

**Topic 2 — Multi-Objective Tuning**

- Accuracy vs latency vs cost trade-offs
- Pareto fronts

**Topic 3 — Experiment Hygiene and Tooling**

- Fixed splits, seeds and logged configurations
- Variance across seeds; comparing runs fairly
- Study, trial and objective abstraction
- Logging parameters, metrics and artifacts (preview of MLflow in Season 11)

</details>

**Important concepts**

- *Commands / APIs / Code:* `optuna.create_study`, `trial.suggest_*`, pruning callbacks
- *Mechanisms & failure scenarios:* Winners that are seed luck, search on a leaky split, endless tuning with no baseline gain.

<a id="s04-module-2"></a>

## Module 2 — Advanced Tabular Modeling

**4 episodes (S04E04–S04E07) · 17 topics.** This module covers: Advanced Feature Engineering; Feature Selection and Leakage Audits; Gradient Boosting Internals; Ensembling.

| ID | Episode | Depth |
|---|---|---|
| S04E04 | Advanced Feature Engineering: Aggregations, Time Features, and Leakage-Safe Encoding | Intermediate |
| S04E05 | Feature Selection and Leakage Audits | Intermediate |
| S04E06 | Gradient Boosting Internals: Histogram Splits, Leaf-Wise Growth, and Regularization | Advanced |
| S04E07 | Ensembling: Stacking, Blending, and Model Combination | Intermediate |

### S04E04 — Advanced Feature Engineering: Aggregations, Time Features, and Leakage-Safe Encoding

**Depth:** Intermediate  
**Learning objective:** Create powerful features from relational and temporal data while keeping them point-in-time correct.  
**Prerequisites:** S03E14, S01E10  
**Expected outcome:** Design features that are predictive, leakage-free, and servable.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Relational and Aggregate Features**

- Group statistics, counts and ratios
- Entity-level history features

**Topic 2 — Temporal Features**

- Rolling and expanding windows
- Lag features, recency and seasonality encodings

**Topic 3 — Leakage-Safe Encoding**

- Out-of-fold target encoding
- Time-aware feature computation

**Topic 4 — Learned Representations of Categories**

- Embeddings for high-cardinality categoricals
- When learned representations beat hand-built features

**Topic 5 — Production Considerations**

- Offline vs online feature computation
- Training-serving consistency and feature ownership (preview of feature stores)

</details>

**Important concepts**

- *Commands / APIs / Code:* `groupby().rolling`, `TargetEncoder` with CV, point-in-time joins in SQL
- *Mechanisms & failure scenarios:* Window features using future rows, target encoding leaking labels, features impossible to compute at serving time.

### S04E05 — Feature Selection and Leakage Audits

**Depth:** Intermediate  
**Learning objective:** Reduce features for robustness and cost, and systematically detect leakage.  
**Prerequisites:** S04E04, S03E08  
**Expected outcome:** Produce a defensible feature set and an audit trail.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Selection Methods and Their Stability**

- Filter, wrapper and embedded methods
- Mutual information and permutation importance
- Selection variance across resamples
- Correlated and redundant features

**Topic 2 — Leakage Audits**

- Suspiciously strong features and ablation tests
- Time-travel checks and dependency review
- Shadow-feature and null-importance tests

**Topic 3 — Cost vs Benefit**

- Feature cost, latency and maintenance
- Documenting selection decisions

</details>

**Important concepts**

- *Commands / APIs / Code:* `SelectFromModel`, `permutation_importance`, `mutual_info_classif`
- *Mechanisms & failure scenarios:* Selecting features on the full dataset, importance biased by cardinality, removing a feature that matters for a subgroup.

### S04E06 — Gradient Boosting Internals: Histogram Splits, Leaf-Wise Growth, and Regularization

**Depth:** Advanced  
**Learning objective:** Understand how modern boosting libraries differ internally and tune them with intent.  
**Prerequisites:** S03E09  
**Expected outcome:** Explain library differences and tune boosted models from first principles.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Second-Order Boosting**

- Gradients and Hessians in the objective
- Shrinkage and tree-complexity penalties
- Custom objectives and metrics

**Topic 2 — Split Finding**

- Exact vs histogram-based splits
- Sparsity-aware handling of missing values

**Topic 3 — Tree Growth Strategies**

- Level-wise vs leaf-wise growth
- Effects on overfitting and speed

**Topic 4 — Categorical Handling**

- Native categorical splits
- Ordered boosting and target-statistic leakage (CatBoost idea)

**Topic 5 — Tuning, Constraints and Failure**

- Learning rate vs number of trees
- Monotonic constraints
- GPU training and determinism

</details>

**Important concepts**

- *Commands / APIs / Code:* XGBoost/LightGBM/CatBoost params, `monotone_constraints`, custom eval metric
- *Mechanisms & failure scenarios:* Leaf-wise trees overfitting small data, categorical encoding leakage, results differing between CPU and GPU.

### S04E07 — Ensembling: Stacking, Blending, and Model Combination

**Depth:** Intermediate  
**Learning objective:** Combine models for accuracy gains while weighing complexity and serving cost.  
**Prerequisites:** S04E06, S03E08  
**Expected outcome:** Build a leak-free stack and decide whether its gain justifies its cost.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Why Ensembles Help**

- Error diversity and correlation
- Averaging, voting and weighted blending
- Diminishing returns

**Topic 2 — Stacking**

- Out-of-fold predictions as meta-features
- Meta-learner choice and leakage

**Topic 3 — Blending and Selection**

- Holdout blending
- Greedy ensemble selection

**Topic 4 — Cost and Maintenance**

- Latency and memory for ensembles
- Distillation of an ensemble into one model
- When a single model is the better engineering decision

</details>

**Important concepts**

- *Commands / APIs / Code:* `StackingClassifier`, `VotingClassifier`, out-of-fold prediction loop
- *Mechanisms & failure scenarios:* Stacking leakage inflating validation, correlated base models adding nothing, ensemble too slow to serve.

<a id="s04-module-3"></a>

## Module 3 — Time Series and Forecasting

**2 episodes (S04E08–S04E09) · 7 topics.** This module covers: Time-Series Fundamentals; Forecasting Models.

| ID | Episode | Depth |
|---|---|---|
| S04E08 | Time-Series Fundamentals: Stationarity, Seasonality, and Backtesting | Intermediate |
| S04E09 | Forecasting Models: ARIMA, Gradient Boosting, and Deep Approaches | Intermediate |

### S04E08 — Time-Series Fundamentals: Stationarity, Seasonality, and Backtesting

**Depth:** Intermediate  
**Learning objective:** Understand what makes temporal data different and evaluate forecasts without peeking at the future.  
**Prerequisites:** S03E03, S03E10  
**Expected outcome:** Decompose a series, set baselines, and backtest properly.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Structure of a Time Series**

- Trend, seasonality, noise and level shifts
- Decomposition

**Topic 2 — Stationarity and Dependence**

- Stationarity, differencing and unit-root intuition
- Autocorrelation and partial autocorrelation

**Topic 3 — Baselines and Backtesting**

- Naive and seasonal-naive forecasts
- Moving averages and exponential smoothing
- Rolling-origin evaluation
- Forecast metrics (MAE, MASE, sMAPE) and horizon-specific accuracy
- Handling holidays and regime changes

</details>

**Important concepts**

- *Commands / APIs / Code:* `statsmodels` decomposition, `TimeSeriesSplit`, ACF/PACF plots
- *Mechanisms & failure scenarios:* Random shuffling of time data, tuning on future periods, ignoring holidays and regime changes.

### S04E09 — Forecasting Models: ARIMA, Gradient Boosting, and Deep Approaches

**Depth:** Intermediate  
**Learning objective:** Choose among statistical, tree-based and neural forecasting approaches for a given problem.  
**Prerequisites:** S04E08, S04E06  
**Expected outcome:** Select and justify a forecasting approach and produce honest intervals.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Statistical Models**

- ARIMA/SARIMA intuition
- Exponential-smoothing families and exogenous regressors

**Topic 2 — Machine-Learning Forecasting**

- Lag and rolling features with boosting
- Direct vs recursive multi-step forecasting

**Topic 3 — Global Models Across Many Series**

- Pooling related series
- Cold-start series and hierarchies
- Hierarchical forecasting and reconciliation

**Topic 4 — Probabilistic and Neural Forecasts**

- Prediction intervals and quantile forecasts
- Sequence models at overview level (links to Season 5)
- When deep models are not worth it

</details>

**Important concepts**

- *Commands / APIs / Code:* `statsmodels.tsa.SARIMAX`, lag-feature construction, quantile objectives
- *Mechanisms & failure scenarios:* Error compounding in recursive forecasts, leakage via future covariates, forecasts failing at structural breaks.

<a id="s04-module-4"></a>

## Module 4 — Recommendation and Ranking Systems

**2 episodes (S04E10–S04E11) · 9 topics.** This module covers: Recommender Foundations; Ranking Systems.

| ID | Episode | Depth |
|---|---|---|
| S04E10 | Recommender Foundations: Collaborative Filtering and Matrix Factorization | Intermediate |
| S04E11 | Ranking Systems: Candidate Generation, Rankers, and Evaluation | Advanced |

### S04E10 — Recommender Foundations: Collaborative Filtering and Matrix Factorization

**Depth:** Intermediate  
**Learning objective:** Understand how systems predict preferences from interaction data.  
**Prerequisites:** S02E04, S03E13  
**Expected outcome:** Explain and sketch a factorization-based recommender and its failure modes.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Problem Setup**

- Explicit vs implicit feedback
- User-item matrices and sparsity
- Content-based vs collaborative approaches

**Topic 2 — Neighborhood Methods**

- User-based and item-based collaborative filtering
- Similarity choices and scaling

**Topic 3 — Matrix Factorization**

- Latent factors and dot-product scoring
- ALS and SGD training, regularization
- Connection to embeddings

**Topic 4 — Hard Cases**

- Cold start for users and items
- Popularity bias and hybrid strategies

</details>

**Important concepts**

- *Commands / APIs / Code:* `implicit` ALS, SVD-based recommenders, item-item similarity
- *Mechanisms & failure scenarios:* Cold-start items never shown, popularity feedback loops, treating missing interactions as negatives.

### S04E11 — Ranking Systems: Candidate Generation, Rankers, and Evaluation

**Depth:** Advanced  
**Learning objective:** Understand multi-stage recommendation and search architectures and how ranking quality is measured.  
**Prerequisites:** S04E10, S04E06  
**Expected outcome:** Describe a production ranking pipeline and evaluate it with appropriate metrics.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Multi-Stage Architecture**

- Candidate generation, ranking and re-ranking
- Business rules and diversity

**Topic 2 — Retrieval Models**

- Two-tower models and in-batch negatives
- Approximate nearest-neighbor retrieval for candidates

**Topic 3 — Learning to Rank**

- Pointwise, pairwise and listwise objectives
- Features for rankers

**Topic 4 — Evaluation**

- Precision@K, Recall@K, NDCG and MAP
- Offline vs online metrics

**Topic 5 — Feedback Loops and Bias**

- Position bias in click logs
- Exposure bias and popularity feedback

</details>

**Important concepts**

- *Commands / APIs / Code:* `lightgbm` `lambdarank` objective, NDCG computation, two-tower sketch
- *Mechanisms & failure scenarios:* Offline metrics improving while online engagement falls, position bias in click logs, candidate stage dropping relevant items.

<a id="s04-module-5"></a>

## Module 5 — Specialized Problems and Responsible ML

**4 episodes (S04E12–S04E15) · 14 topics.** This module covers: Anomaly and Fraud Detection; Classical NLP; Model Explainability; Fairness, Bias, and Responsible ML.

| ID | Episode | Depth |
|---|---|---|
| S04E12 | Anomaly and Fraud Detection | Intermediate |
| S04E13 | Classical NLP: Text Representation, TF-IDF, and Text Classification | Intermediate |
| S04E14 | Model Explainability: SHAP, LIME, and Partial Dependence | Intermediate |
| S04E15 | Fairness, Bias, and Responsible ML | Intermediate |

### S04E12 — Anomaly and Fraud Detection

**Depth:** Intermediate  
**Learning objective:** Detect rare or novel behavior with limited labels and manage false-positive cost.  
**Prerequisites:** S04E01, S03E16  
**Expected outcome:** Choose an anomaly-detection approach and tune it to an operational budget.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Approaches**

- Statistical thresholds and robust baselines
- Isolation forest, one-class models and density methods

**Topic 2 — Reconstruction-Based Detection**

- Autoencoder reconstruction error (preview of Season 5)
- Calibrating scores into alerts

**Topic 3 — Fraud-Style Systems**

- Supervised vs unsupervised vs semi-supervised
- Graph and behavioral features
- Delayed and noisy labels

**Topic 4 — Operations**

- Threshold tuning against analyst capacity
- Concept drift and adversaries who adapt
- Feedback from investigations

</details>

**Important concepts**

- *Commands / APIs / Code:* `IsolationForest`, `OneClassSVM`, rolling z-score baselines
- *Mechanisms & failure scenarios:* Alert flood from poorly set thresholds, labels reflecting only caught fraud, adversarial adaptation.

### S04E13 — Classical NLP: Text Representation, TF-IDF, and Text Classification

**Depth:** Intermediate  
**Learning objective:** Understand pre-transformer text techniques that remain strong baselines and underlie retrieval.  
**Prerequisites:** S03E05, S03E06  
**Expected outcome:** Build a TF-IDF classifier baseline and explain when it beats heavier models.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Text as Features and TF-IDF**

- Tokenization, normalization, stop-words and n-grams
- Bag of words and sparse high-dimensional representations
- Term and document frequency; the weighting idea
- Cosine similarity for retrieval and deduplication

**Topic 2 — Classical Tasks**

- Linear models for text classification
- Topic models (LDA) at overview level

**Topic 3 — Strengths, Limits, and Bridges**

- Strong baselines and interpretability
- Vocabulary mismatch and polysemy
- Bridge to embeddings (Season 5) and BM25 (Season 8)

</details>

**Important concepts**

- *Commands / APIs / Code:* `TfidfVectorizer`, `LogisticRegression` on sparse matrices, cosine similarity
- *Mechanisms & failure scenarios:* Vocabulary leakage across splits, domain-specific stop-words removing signal, out-of-vocabulary terms at inference.

### S04E14 — Model Explainability: SHAP, LIME, and Partial Dependence

**Depth:** Intermediate  
**Learning objective:** Explain individual and global model behavior and understand the limits of post-hoc explanations.  
**Prerequisites:** S04E06, S03E08  
**Expected outcome:** Produce and critically read explanations and state what they cannot prove.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Global Explanations**

- Permutation importance, partial dependence and ICE
- Surrogate models

**Topic 2 — Local Explanations**

- LIME intuition
- Reading local attributions

**Topic 3 — Shapley Values**

- The Shapley idea and its fairness axioms
- TreeSHAP and additivity
- Summary and force plots

**Topic 4 — Using Explanations Responsibly**

- Debugging models and spotting leakage
- Correlated-feature pitfalls
- Explanations vs causality; regulatory and stakeholder needs

</details>

**Important concepts**

- *Commands / APIs / Code:* `shap.TreeExplainer`, `PartialDependenceDisplay`, `lime.lime_tabular`
- *Mechanisms & failure scenarios:* Correlated features splitting credit misleadingly, explanations that are unstable, treating attribution as causation.

### S04E15 — Fairness, Bias, and Responsible ML

**Depth:** Intermediate  
**Learning objective:** Measure and reduce unfair model behavior and understand why fairness criteria conflict.  
**Prerequisites:** S04E14, S03E11  
**Expected outcome:** Audit a model by subgroup and explain the trade-offs in a mitigation choice.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Where Bias Comes From**

- Sampling, labeling, measurement and historical bias
- Proxy variables and feedback loops

**Topic 2 — Measuring Fairness and Its Trade-offs**

- Group metrics: demographic parity, equalized odds, calibration by group
- Slice-based evaluation and small subgroups
- Why fairness definitions conflict
- Choosing a criterion for a context

**Topic 3 — Mitigation and Documentation**

- Pre-, in- and post-processing mitigation
- Dataset sheets and model cards
- Connecting to Season 14 governance

</details>

**Important concepts**

- *Commands / APIs / Code:* group-wise metrics in Pandas, `fairlearn` metrics (concept)
- *Mechanisms & failure scenarios:* Removing a sensitive attribute while proxies remain, optimizing one fairness metric and breaking another, small subgroup sample sizes.

<a id="s04-module-6"></a>

## Module 6 — Experimentation, Causality, Automation, and System Design

**6 episodes (S04E16–S04E21) · 28 topics.** This module covers: Offline vs Online Evaluation; Causal Inference Foundations; Uplift Modeling and Causal ML; Data-Centric ML; AutoML; ML System Design.

| ID | Episode | Depth |
|---|---|---|
| S04E16 | Offline vs Online Evaluation: A/B Tests, Shadow Mode, and Experiment Design | Intermediate |
| S04E17 | Causal Inference Foundations: Confounding, Adjustment, and Quasi-Experiments | Intermediate |
| S04E18 | Uplift Modeling and Causal ML: Heterogeneous Effects and Off-Policy Evaluation | Advanced |
| S04E19 | Data-Centric ML: Label Noise, Active Learning, and Weak Supervision | Advanced |
| S04E20 | AutoML: Automated Feature Engineering, Model Selection, Hyperparameter Optimization, and Neural Architecture Search | Intermediate |
| S04E21 | ML System Design: From Problem to Production Blueprint | Advanced |

### S04E16 — Offline vs Online Evaluation: A/B Tests, Shadow Mode, and Experiment Design

**Depth:** Intermediate  
**Learning objective:** Validate model changes in the real world safely and statistically soundly.  
**Prerequisites:** S02E15, S04E11  
**Expected outcome:** Design a safe rollout plan and decide ship/no-ship from experiment evidence.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Offline Evaluation Limits**

- Distribution mismatch and counterfactual problems
- Metrics that predict business value; guardrail metrics

**Topic 2 — Online Experiments**

- A/B tests and interleaving; sample size and duration
- Interference and network effects

**Topic 3 — Safe Rollout and Decisions**

- Shadow deployment and canary release
- Ramp-up and rollback criteria
- Interpreting conflicting metrics
- Long-term effects and holdouts

</details>

**Important concepts**

- *Commands / APIs / Code:* power analysis, experiment assignment hashing, guardrail checks
- *Mechanisms & failure scenarios:* Peeking at results, sample-ratio mismatch, offline gains that vanish online.

### S04E17 — Causal Inference Foundations: Confounding, Adjustment, and Quasi-Experiments

**Depth:** Intermediate  
**Learning objective:** Reason about cause and effect from data, know what observational data can and cannot support, and choose an identification strategy.  
**Prerequisites:** S02E16, S02E15, S04E16  
**Expected outcome:** Frame a causal question, draw a DAG, select an adjustment strategy and state the assumptions behind the estimate.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Causal Questions and Potential Outcomes**

- Treatment, outcome and the fundamental problem of causal inference
- Average treatment effect and the potential-outcomes framework
- Why prediction accuracy does not answer causal questions

**Topic 2 — Causal Graphs**

- DAGs, confounders, mediators and colliders
- Backdoor criterion and what to adjust for (and not)

**Topic 3 — Randomization and Its Substitutes**

- Why randomization identifies causal effects
- Observational adjustment: regression, matching, propensity scores, inverse-probability weighting

**Topic 4 — Quasi-Experimental Designs**

- Difference-in-differences and parallel trends
- Instrumental variables and regression discontinuity at concept level

**Topic 5 — Assumptions and Sensitivity**

- Overlap, ignorability and consistency
- Sensitivity analysis for unmeasured confounding
- Reporting causal claims honestly

</details>

**Important concepts**

- *Commands / APIs / Code:* `statsmodels` regression adjustment, propensity-score weighting (illustrative), difference-in-differences setup
- *Mechanisms & failure scenarios:* Adjusting for a collider and creating bias, unmeasured confounders, propensity weights exploding on poor overlap, parallel-trends assumption violated.

### S04E18 — Uplift Modeling and Causal ML: Heterogeneous Effects and Off-Policy Evaluation

**Depth:** Advanced  
**Learning objective:** Estimate who benefits from an action, use causal ML for targeting decisions, and evaluate policies from logged data.  
**Prerequisites:** S04E17, S04E11, S04E16  
**Expected outcome:** Choose an approach for heterogeneous-effect estimation and evaluate a targeting policy without deploying it blindly.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Heterogeneous Treatment Effects**

- Conditional average treatment effect (CATE)
- Why "who responds" differs from "who converts"

**Topic 2 — Estimators**

- Meta-learners (S-, T- and X-learner)
- Causal forests and double machine learning at concept level

**Topic 3 — Evaluating Uplift**

- Uplift and Qini curves
- Why you need randomized data to validate

**Topic 4 — Policies and Bandits**

- Targeting policies and budget constraints
- Contextual bandits as online experimentation
- Off-policy evaluation with logged data (inverse propensity scoring, doubly robust)

**Topic 5 — Practice and Pitfalls**

- When causal ML is worth its complexity
- Interference, long-term effects and monitoring policies

</details>

**Important concepts**

- *Commands / APIs / Code:* Meta-learner sketch (T-/S-/X-learner), uplift curve and Qini computation, inverse-propensity-weighted policy value (illustrative)
- *Mechanisms & failure scenarios:* Targeting models that predict outcome rather than effect, uplift estimated on non-randomized data, off-policy estimates with huge variance from low overlap.

### S04E19 — Data-Centric ML: Label Noise, Active Learning, and Weak Supervision

**Depth:** Advanced  
**Learning objective:** Improve performance by improving data, and spend labeling effort where it counts.  
**Prerequisites:** S03E02, S04E02  
**Expected outcome:** Plan a data-improvement loop and prioritize labeling.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Finding Data Problems**

- Label-noise detection and the confident-learning idea
- Duplicates and near-duplicates
- Slice discovery

**Topic 2 — Smarter Labeling**

- Active learning: uncertainty and diversity sampling
- Annotation guidelines and agreement

**Topic 3 — Weak Supervision and Synthetic Data**

- Labeling functions and label models
- Synthetic data and its risks

**Topic 4 — Data Operations**

- Dataset versioning and dataset cards
- Data flywheels with production feedback
- Cost-benefit of more data vs better data

</details>

**Important concepts**

- *Commands / APIs / Code:* `cleanlab` concept, uncertainty sampling loop, labeling-function sketch
- *Mechanisms & failure scenarios:* Active learning biasing the sample, weak labels correlated with each other, label guidelines drifting.

### S04E20 — AutoML: Automated Feature Engineering, Model Selection, Hyperparameter Optimization, and Neural Architecture Search

**Depth:** Intermediate  
**Learning objective:** Understand what automated machine learning automates, how each automated stage works internally, and where its limits and risks lie, so AutoML can be used as an engineering tool rather than a black box.  
**Prerequisites:** S04E03, S04E04, S04E07, S03E13  
**Expected outcome:** Explain how each automated stage works, set up a bounded AutoML search, audit its output, and decide when AutoML is appropriate.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — What AutoML Automates**

- The ML pipeline stages that can be searched: features, algorithm, hyperparameters, ensembling, architecture
- Levels of automation, from tuning one model to full pipeline search
- Where AutoML helps: baselines, prototyping and small teams

**Topic 2 — Automated Feature Engineering**

- Transformation search and feature synthesis from relational data
- Automated encoding, scaling and imputation choices
- Feature explosion, selection and the leakage risk of synthesized features

**Topic 3 — Automated Model Selection and Hyperparameter Optimization**

- The combined algorithm selection and hyperparameter (CASH) problem
- Bayesian optimization, successive halving and Hyperband as budget allocators
- Meta-learning and warm starts from past tasks
- Automatic ensembling of the best candidates and time budgets

**Topic 4 — Neural Architecture Search**

- Search spaces: cells, operations and connectivity
- Search strategies: reinforcement learning, evolutionary and differentiable search
- Weight sharing and one-shot methods to cut cost
- Hardware-aware search and why most teams reuse published architectures

**Topic 5 — Limitations and Trade-offs**

- Compute cost and diminishing returns
- Overfitting the validation set through massive search
- Reproducibility, interpretability and governance of automatically built pipelines
- What cannot be automated: problem framing, label quality, data leakage and deployment constraints

**Topic 6 — AutoML in an Engineering Workflow**

- Using AutoML as a baseline generator and for search-space discovery
- Auditing the produced pipeline before trusting it
- Logging searches in experiment tracking and registering results (preview of Season 11)
- When not to use AutoML

</details>

**Important concepts**

- *Commands / APIs / Code:* Tool-agnostic AutoML search with a time budget and a leaderboard (illustrative), successive-halving budget-schedule calculation, search-space definition for hyperparameters and pipeline steps
- *Mechanisms & failure scenarios:* Leakage introduced by synthesized features, overfitting to the validation set after thousands of trials, non-reproducible pipelines, search budget spent on a badly framed problem, opaque final models that cannot be explained or maintained.

### S04E21 — ML System Design: From Problem to Production Blueprint

**Depth:** Advanced  
**Learning objective:** Combine requirements, data, modeling, evaluation and serving constraints into a coherent design for a tabular or ranking system.  
**Prerequisites:** S04E16, S04E11, S04E12, S04E17, S04E20  
**Expected outcome:** Produce a structured design document for an ML system and defend its trade-offs.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Requirements and Constraints**

- Success metric, latency, cost, freshness and risk
- Batch vs real-time; build vs buy
- Data availability at decision time

**Topic 2 — Blueprint**

- Data pipeline, features, training, evaluation and serving
- Monitoring and retraining triggers
- Fallbacks and human-in-the-loop

**Topic 3 — Case Study: Fraud Scoring**

- Imbalance, delayed labels, thresholds and analyst capacity
- Imbalance, delayed labels, thresholds and analyst capacity
- Feature freshness and graph features
- Monitoring for adversaries who adapt

**Topic 4 — Case Study: Demand Forecasting**

- Hierarchies, intermittent demand and backtesting
- Hierarchies, intermittent demand and backtesting
- Promotion and holiday effects
- Forecast reconciliation and inventory decisions

**Topic 5 — Case Study: Product Ranking**

- Two-stage architecture, feedback loops and online evaluation
- What changes at scale; bridge to Season 11 (MLOps)

</details>

**Important concepts**

- *Commands / APIs / Code:* design-review template; no commands required
- *Mechanisms & failure scenarios:* Features unavailable at serving, no feedback loop, overbuilt architecture for the real latency need.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s04-module-1) | Starting point of the season |
| [Module 2](#s04-module-2) | Within-module sequence only |
| [Module 3](#s04-module-3) | [Module 2](#s04-module-2) (S04E06) |
| [Module 4](#s04-module-4) | [Module 2](#s04-module-2) (S04E06) |
| [Module 5](#s04-module-5) | [Module 1](#s04-module-1) (S04E01); [Module 2](#s04-module-2) (S04E06) |
| [Module 6](#s04-module-6) | [Module 1](#s04-module-1) (S04E02, S04E03); [Module 2](#s04-module-2) (S04E04, S04E07); [Module 4](#s04-module-4) (S04E11); [Module 5](#s04-module-5) (S04E12) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 3 — Machine Learning Foundations](../season-03-machine-learning/roadmap.md)
- **Next:** [Season 5 — Deep Learning & Neural Networks](../season-05-deep-learning/roadmap.md)
- **Draws on:** [Season 1](../season-01-python-for-ai-ml/roadmap.md) (S01E10); [Season 2](../season-02-mathematics-for-ai/roadmap.md) (S02E04, S02E13, S02E15, S02E16); [Season 3](../season-03-machine-learning/roadmap.md) (S03E02, S03E03, S03E05, S03E06, S03E08, S03E09, S03E10, S03E11, S03E13, S03E14, S03E15, S03E16)
- **Required by:** [Season 5](../season-05-deep-learning/roadmap.md) (via S04E16); [Season 6](../season-06-llms-and-transformers/roadmap.md) (via S04E02, S04E13); [Season 8](../season-08-rag-engineering/roadmap.md) (via S04E11); [Season 11](../season-11-mlops-engineering/roadmap.md) (via S04E03, S04E04, S04E15, S04E16, S04E21); [Season 12](../season-12-llmops-engineering/roadmap.md) (via S04E16, S04E19); [Season 14](../season-14-production-ai-systems/roadmap.md) (via S04E12, S04E14, S04E15, S04E21); [Season 15](../season-15-ai-for-devops/roadmap.md) (via S04E01, S04E02, S04E08, S04E09, S04E12, S04E13, S04E17)
