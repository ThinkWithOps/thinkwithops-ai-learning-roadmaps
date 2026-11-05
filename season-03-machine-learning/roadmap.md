# Season 3 Roadmap — Machine Learning Foundations

[← Season 3 overview](README.md) · [All seasons](../README.md)

**5 modules · 18 episodes · 65 topics · 178 subtopics · Level: Foundational → Intermediate**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Framing the Problem and the Data](#s03-module-1)
- [Module 2 — Core Supervised Learning Algorithms](#s03-module-2)
- [Module 3 — Evaluating Models](#s03-module-3)
- [Module 4 — Features and Pipelines](#s03-module-4)
- [Module 5 — Unsupervised Learning and the Full Workflow](#s03-module-5)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Teach classical supervised and unsupervised learning as mechanisms: what each algorithm optimizes, how it fails, and how to evaluate it honestly. Everything here is the base for deep learning, LLMs and MLOps.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S03E01 | Distinguish rule-based software from learned systems and frame a business problem as an ML task with a defensible objective. |
| S03E02 | Understand how data defects, label noise and leakage silently destroy models before any algorithm runs. |
| S03E03 | Evaluate generalization honestly using appropriate data splits for the problem structure. |
| S03E04 | Understand linear regression as least-squares optimization and know when its assumptions break. |
| S03E05 | Understand how a linear model produces probabilities and how decision thresholds turn them into actions. |
| S03E06 | Compare three non-tree classical models by their assumptions, geometry and cost, to know when each is the right tool. |
| S03E07 | Understand how a tree is grown greedily and why unpruned trees memorize. |
| S03E08 | Understand why averaging many decorrelated trees reduces variance. |
| S03E09 | Understand boosting as sequential error correction and why it dominates tabular problems. |
| S03E10 | Match training losses and evaluation metrics to the business cost of errors for numeric predictions. |
| S03E11 | Evaluate classifiers under class imbalance and unequal error costs. |
| S03E12 | Diagnose whether a model needs more data, more capacity, or more regularization. |
| S03E13 | Control model complexity and search hyperparameters systematically without leaking validation information. |
| S03E14 | Transform raw columns into model-ready features while understanding the effect on each algorithm family. |
| S03E15 | Package preprocessing and model into one object that is safe to cross-validate and deploy. |
| S03E16 | Group unlabeled data and judge whether the groups mean anything. |
| S03E17 | Compress and visualize high-dimensional data without misreading the picture. |
| S03E18 | Run a complete, disciplined modeling cycle and use error analysis to decide what to do next. |

## Prerequisites and Expected Knowledge

- **Season 1 — [Python for AI & ML Engineering](../season-01-python-for-ai-ml/roadmap.md)**: S01E03, S01E08
- **Season 2 — [Mathematics for AI & Machine Learning](../season-02-mathematics-for-ai/roadmap.md)**: S02E02, S02E04, S02E05, S02E07, S02E11, S02E13, S02E14, S02E17

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Framing the Problem and the Data](#s03-module-1) | S03E01–S03E03 | 3 | 3 Foundational |
| 2 | [Core Supervised Learning Algorithms](#s03-module-2) | S03E04–S03E09 | 6 | 3 Foundational, 3 Intermediate |
| 3 | [Evaluating Models](#s03-module-3) | S03E10–S03E13 | 4 | 2 Foundational, 2 Intermediate |
| 4 | [Features and Pipelines](#s03-module-4) | S03E14–S03E15 | 2 | 1 Foundational, 1 Intermediate |
| 5 | [Unsupervised Learning and the Full Workflow](#s03-module-5) | S03E16–S03E18 | 3 | 3 Intermediate |

<a id="s03-module-1"></a>

## Module 1 — Framing the Problem and the Data

**3 episodes (S03E01–S03E03) · 12 topics.** This module covers: What Machine Learning Is; Data Collection, Labeling Quality, and Leakage; Train/Validation/Test Splits and Cross-Validation.

| ID | Episode | Depth |
|---|---|---|
| S03E01 | What Machine Learning Is: Learning from Data, Problem Framing, and the Lifecycle | Foundational |
| S03E02 | Data Collection, Labeling Quality, and Leakage | Foundational |
| S03E03 | Train/Validation/Test Splits and Cross-Validation | Foundational |

### S03E01 — What Machine Learning Is: Learning from Data, Problem Framing, and the Lifecycle

**Depth:** Foundational  
**Learning objective:** Distinguish rule-based software from learned systems and frame a business problem as an ML task with a defensible objective.  
**Prerequisites:** None  
**Expected outcome:** Translate a vague business goal into a well-posed ML problem with a metric and decision.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — AI, Machine Learning, and Deep Learning**

- Rules vs learned functions
- Training vs inference
- What "learning" means: fitting parameters to minimize a loss

**Topic 2 — Learning Paradigms**

- Supervised, unsupervised and self-supervised learning
- Reinforcement learning at overview level (full treatment in Season 5)
- Where each paradigm appears in later seasons

**Topic 3 — Framing a Problem**

- Target, features, prediction horizon and the decision the prediction drives
- Regression, classification, ranking, clustering, generation
- Choosing a success metric tied to cost of errors

**Topic 4 — The ML Lifecycle and When Not to Use ML**

- Data → model → evaluation → deployment → monitoring
- Where Seasons 3–14 fit in that lifecycle
- Cases where rules or simple statistics are better

</details>

**Important concepts**

- *Commands / APIs / Code:* minimal `fit`/`predict` illustration with scikit-learn
- *Mechanisms & failure scenarios:* Wrong target definition, optimizing a proxy metric, solving a problem that rules solve better.

### S03E02 — Data Collection, Labeling Quality, and Leakage

**Depth:** Foundational  
**Learning objective:** Understand how data defects, label noise and leakage silently destroy models before any algorithm runs.  
**Prerequisites:** S01E08, S03E01  
**Expected outcome:** Audit a dataset for leakage and label problems and write down what could mislead a model.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Where Data Comes From**

- Collection methods and sampling bias
- Dataset documentation and datasheets

**Topic 2 — Labels**

- Label sources, ambiguity and inter-annotator agreement
- Label noise and its effect on models

**Topic 3 — Data Leakage**

- Target leakage, train-test contamination, temporal leakage
- Leakage through preprocessing and duplicates
- Detecting leakage from suspiciously good performance

**Topic 4 — Exploratory Data Analysis**

- Distributions, missingness, correlations
- Class balance and subgroup coverage

**Topic 5 — Data Quality Checks Before Modeling**

- Schema, range and duplicate checks
- Documenting what could mislead a model

</details>

**Important concepts**

- *Commands / APIs / Code:* `df.describe()`, `df.corr()`, duplicate checks, label-agreement computation
- *Mechanisms & failure scenarios:* A feature computed after the outcome, near-duplicate rows across splits, labels that encode the labeler's bias.

### S03E03 — Train/Validation/Test Splits and Cross-Validation

**Depth:** Foundational  
**Learning objective:** Evaluate generalization honestly using appropriate data splits for the problem structure.  
**Prerequisites:** S03E02, S02E14  
**Expected outcome:** Choose a split strategy that mirrors production and explain what each score really measures.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Why Splits Exist**

- Training, validation and test roles
- Optimistic bias from reusing data
- The test set as a one-time check

**Topic 2 — Split Strategies**

- Random, stratified and grouped splits
- Time-based splits for temporal data

**Topic 3 — Cross-Validation and Discipline**

- k-fold, repeated and nested cross-validation
- Variance of estimates across folds
- Fitting preprocessing on training folds only
- Leakage via hyperparameter search

</details>

**Important concepts**

- *Commands / APIs / Code:* `train_test_split(stratify=…)`, `KFold`, `GroupKFold`, `TimeSeriesSplit`, `cross_val_score`
- *Mechanisms & failure scenarios:* Same user in train and test, random split on time series, tuning against the test set.

<a id="s03-module-2"></a>

## Module 2 — Core Supervised Learning Algorithms

**6 episodes (S03E04–S03E09) · 23 topics.** This module covers: Linear Regression; Logistic Regression and Classification; k-Nearest Neighbors, Naive Bayes, and Support Vector Machines; Decision Trees; Bagging and Random Forests; Gradient Boosting.

| ID | Episode | Depth |
|---|---|---|
| S03E04 | Linear Regression: Fitting, Assumptions, and Diagnostics | Foundational |
| S03E05 | Logistic Regression and Classification | Foundational |
| S03E06 | k-Nearest Neighbors, Naive Bayes, and Support Vector Machines | Intermediate |
| S03E07 | Decision Trees: Splits, Impurity, and Overfitting | Foundational |
| S03E08 | Bagging and Random Forests | Intermediate |
| S03E09 | Gradient Boosting: XGBoost and LightGBM | Intermediate |

### S03E04 — Linear Regression: Fitting, Assumptions, and Diagnostics

**Depth:** Foundational  
**Learning objective:** Understand linear regression as least-squares optimization and know when its assumptions break.  
**Prerequisites:** S02E02, S02E07, S02E13, S03E03  
**Expected outcome:** Fit, diagnose, and interpret a regression model and say when not to trust it.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Model**

- Weights, bias and the prediction function
- Loss: squared error and its geometry

**Topic 2 — Fitting the Model**

- Normal equation vs gradient descent
- Feature scaling's effect on optimization
- Computational cost and when each is used

**Topic 3 — Assumptions**

- Linearity, independence, constant variance, normal errors
- What breaks when each assumption fails

**Topic 4 — Diagnostics**

- Residual plots, influential points and leverage
- Multicollinearity and unstable coefficients

**Topic 5 — Extensions and Interpretation**

- Polynomial and interaction features
- Ridge and lasso as overview (full treatment in S03E13)
- Interpreting coefficients carefully

</details>

**Important concepts**

- *Commands / APIs / Code:* `LinearRegression`, `Ridge`, `statsmodels.OLS` summary, residual plot
- *Mechanisms & failure scenarios:* Extrapolation beyond data, outliers dominating the fit, unstable coefficients from correlated features.

### S03E05 — Logistic Regression and Classification

**Depth:** Foundational  
**Learning objective:** Understand how a linear model produces probabilities and how decision thresholds turn them into actions.  
**Prerequisites:** S03E04, S02E17  
**Expected outcome:** Explain how a logistic model computes a probability and tune its threshold for a use case.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — From Linear to Logistic**

- Sigmoid and log-odds
- Cross-entropy loss and its gradient
- Multiclass: softmax and one-vs-rest

**Topic 2 — Decision Boundaries**

- Linear boundaries and feature transformations
- Probability output vs hard label

**Topic 3 — Training Behavior and Practical Use**

- Regularization and convergence
- Separable data and diverging weights
- Interpretability and calibration properties
- Thresholds and operating points

</details>

**Important concepts**

- *Commands / APIs / Code:* `LogisticRegression(C=…)`, `predict_proba`, decision boundary plot
- *Mechanisms & failure scenarios:* Perfect separation causing diverging weights, poorly calibrated probabilities, threshold left at 0.5 by default.

### S03E06 — k-Nearest Neighbors, Naive Bayes, and Support Vector Machines

**Depth:** Intermediate  
**Learning objective:** Compare three non-tree classical models by their assumptions, geometry and cost, to know when each is the right tool.  
**Prerequisites:** S03E05, S02E11, S02E05  
**Expected outcome:** Choose among these models for a given data size, dimensionality and latency need.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — k-Nearest Neighbors**

- Distance-based prediction and the choice of k
- Curse of dimensionality
- Inference cost vs training cost

**Topic 2 — Naive Bayes**

- Conditional independence assumption
- Smoothing and text classification
- Why it works despite a wrong assumption

**Topic 3 — Support Vector Machines**

- Margins and support vectors
- Kernels as implicit feature maps (intuition)
- Scaling limits

**Topic 4 — Choosing Among Them**

- Data size, dimensionality and latency trade-offs
- Rules of thumb: small data and few features favor SVM or Naive Bayes
- local nonlinear structure favors kNN
- Inference latency and memory footprint of each model
- Scaling behavior as data grows

</details>

**Important concepts**

- *Commands / APIs / Code:* `KNeighborsClassifier`, `MultinomialNB`, `SVC(kernel=…)`
- *Mechanisms & failure scenarios:* kNN slowing at inference, unscaled features ruining distance, SVM training time blowing up on large data.

### S03E07 — Decision Trees: Splits, Impurity, and Overfitting

**Depth:** Foundational  
**Learning objective:** Understand how a tree is grown greedily and why unpruned trees memorize.  
**Prerequisites:** S03E03, S02E17  
**Expected outcome:** Trace a split decision and tune tree complexity against validation error.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — How a Tree Splits**

- Gini impurity, entropy, variance reduction
- Greedy search over thresholds

**Topic 2 — Complexity Control and Data Handling**

- Depth, minimum samples and cost-complexity pruning
- High-variance behavior and overfitting
- Categorical and missing values
- No scaling needed; axis-aligned boundaries

**Topic 3 — Strengths and Weaknesses**

- Interpretability and its limits
- Instability to small data changes
- Importance bias toward high-cardinality features

</details>

**Important concepts**

- *Commands / APIs / Code:* `DecisionTreeClassifier`, `plot_tree`, `max_depth`/`ccp_alpha`
- *Mechanisms & failure scenarios:* Deep trees memorizing noise, biased importance toward high-cardinality features, brittle splits.

### S03E08 — Bagging and Random Forests

**Depth:** Intermediate  
**Learning objective:** Understand why averaging many decorrelated trees reduces variance.  
**Prerequisites:** S03E07  
**Expected outcome:** Explain bagging's variance reduction and tune a forest sensibly.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Bagging**

- Bootstrap sampling
- Variance reduction by averaging
- Out-of-bag error

**Topic 2 — Random Forests**

- Feature subsampling and decorrelation
- Hyperparameters that matter
- Permutation vs impurity importance

**Topic 3 — Behavior in Practice**

- Parallel training and prediction cost
- Probability estimates and calibration
- Extrapolation failure on regression

</details>

**Important concepts**

- *Commands / APIs / Code:* `RandomForestClassifier(oob_score=True)`, `permutation_importance`
- *Mechanisms & failure scenarios:* Correlated features distorting importance, large forests inflating latency and memory, extrapolation failure on regression.

### S03E09 — Gradient Boosting: XGBoost and LightGBM

**Depth:** Intermediate  
**Learning objective:** Understand boosting as sequential error correction and why it dominates tabular problems.  
**Prerequisites:** S03E07, S03E08, S02E07  
**Expected outcome:** Train and regularize a boosted model and explain why each hyperparameter changes behavior.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Boosting Idea**

- Weak learners and residual fitting
- AdaBoost intuition

**Topic 2 — Gradient Boosting**

- Gradient boosting as gradient descent in function space
- Shrinkage and the number of trees

**Topic 3 — Practical Systems**

- Histogram-based splits and speed
- Handling categoricals and missing values (XGBoost, LightGBM)

**Topic 4 — Regularization and Tuning**

- Subsampling, tree complexity penalties, early stopping
- Key hyperparameters and their interactions

**Topic 5 — Boosting vs Alternatives**

- Boosting vs forests vs neural nets on tabular data
- Overfitting signals via validation curves

</details>

**Important concepts**

- *Commands / APIs / Code:* `xgboost.XGBClassifier`, `lightgbm.LGBMClassifier`, `early_stopping_rounds`
- *Mechanisms & failure scenarios:* Overfitting from too many rounds, leakage through target-correlated features, tuned model failing under drift.

<a id="s03-module-3"></a>

## Module 3 — Evaluating Models

**4 episodes (S03E10–S03E13) · 13 topics.** This module covers: Loss Functions and Regression Metrics; Classification Metrics; Bias, Variance, Overfitting, and Learning Curves; Regularization and Hyperparameter Tuning.

| ID | Episode | Depth |
|---|---|---|
| S03E10 | Loss Functions and Regression Metrics | Foundational |
| S03E11 | Classification Metrics: Confusion Matrix, Precision/Recall, ROC, and Thresholds | Foundational |
| S03E12 | Bias, Variance, Overfitting, and Learning Curves | Intermediate |
| S03E13 | Regularization and Hyperparameter Tuning | Intermediate |

### S03E10 — Loss Functions and Regression Metrics

**Depth:** Foundational  
**Learning objective:** Match training losses and evaluation metrics to the business cost of errors for numeric predictions.  
**Prerequisites:** S03E04, S02E13  
**Expected outcome:** Select a regression loss and metric and compare against a meaningful baseline.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Common Losses**

- MSE, MAE, Huber
- Sensitivity to outliers
- Quantile loss for prediction intervals

**Topic 2 — Evaluation Metrics**

- RMSE, MAE, R², MAPE and their pitfalls
- Baselines: mean, median, last value

**Topic 3 — Reading Errors**

- Residual analysis by subgroup
- Prediction intervals
- Business-cost-aware metrics

</details>

**Important concepts**

- *Commands / APIs / Code:* `sklearn.metrics`, `mean_absolute_error`, `HuberRegressor`
- *Mechanisms & failure scenarios:* MAPE blowing up near zero, R² high but useless, averaging hiding large errors on important segments.

### S03E11 — Classification Metrics: Confusion Matrix, Precision/Recall, ROC, and Thresholds

**Depth:** Foundational  
**Learning objective:** Evaluate classifiers under class imbalance and unequal error costs.  
**Prerequisites:** S03E05, S03E03  
**Expected outcome:** Choose metrics and a threshold that fit the cost structure of a real decision.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Confusion Matrix and Derived Metrics**

- TP/FP/FN/TN
- Precision, recall, F1, specificity
- Accuracy's failure on imbalanced data

**Topic 2 — Curves**

- ROC and AUC; precision-recall curves
- When PR is more informative than ROC

**Topic 3 — Thresholds, Multiclass, and Segments**

- Threshold selection with costs
- Operating points
- Macro, micro and weighted averaging
- Metrics per segment

</details>

**Important concepts**

- *Commands / APIs / Code:* `confusion_matrix`, `precision_recall_curve`, `roc_auc_score`, `classification_report`
- *Mechanisms & failure scenarios:* 99% accuracy with a useless model, optimizing AUC when only top-k matters, threshold set on test data.

### S03E12 — Bias, Variance, Overfitting, and Learning Curves

**Depth:** Intermediate  
**Learning objective:** Diagnose whether a model needs more data, more capacity, or more regularization.  
**Prerequisites:** S03E03, S03E07  
**Expected outcome:** Read curves and choose the next experiment based on diagnosis rather than guesswork.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Trade-off**

- Bias and variance decomposition
- Underfitting vs overfitting symptoms
- Model capacity

**Topic 2 — Diagnostic Tools**

- Learning curves (data size)
- Validation curves (hyperparameters)
- Train vs validation gap

**Topic 3 — Remedies**

- More data, simpler or richer model, regularization, features
- Irreducible error and noise ceilings

**Topic 4 — Modern Nuance**

- Double descent preview (Season 5)
- Error analysis as the next-experiment engine

</details>

**Important concepts**

- *Commands / APIs / Code:* `learning_curve`, `validation_curve`, plotting train/validation scores
- *Mechanisms & failure scenarios:* Adding data to a high-bias model, adding capacity to a noisy-label problem, reading noisy curves as trends.

### S03E13 — Regularization and Hyperparameter Tuning

**Depth:** Intermediate  
**Learning objective:** Control model complexity and search hyperparameters systematically without leaking validation information.  
**Prerequisites:** S03E12, S02E05  
**Expected outcome:** Run a tuning job whose reported score is an honest estimate.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Regularization**

- L1 (sparsity) and L2 (shrinkage); elastic net
- Early stopping as regularization

**Topic 2 — Search Strategies and Efficient Search**

- Grid vs random vs Bayesian search
- Search spaces and scales (log-uniform)
- Budget allocation and successive halving
- Parallel trials and reproducibility

**Topic 3 — Honest Tuning**

- Nested cross-validation
- Tuning variance and overfitting the validation set

</details>

**Important concepts**

- *Commands / APIs / Code:* `GridSearchCV`, `RandomizedSearchCV`, `Lasso`, `Ridge`, Optuna concept
- *Mechanisms & failure scenarios:* Over-tuning to a small validation set, wasted compute on irrelevant parameters, inconsistent seeds across trials.

<a id="s03-module-4"></a>

## Module 4 — Features and Pipelines

**2 episodes (S03E14–S03E15) · 7 topics.** This module covers: Feature Engineering; scikit-learn Pipelines and Preventing Leakage.

| ID | Episode | Depth |
|---|---|---|
| S03E14 | Feature Engineering: Encoding, Scaling, and Missing Values | Foundational |
| S03E15 | scikit-learn Pipelines and Preventing Leakage | Intermediate |

### S03E14 — Feature Engineering: Encoding, Scaling, and Missing Values

**Depth:** Foundational  
**Learning objective:** Transform raw columns into model-ready features while understanding the effect on each algorithm family.  
**Prerequisites:** S03E02, S03E05  
**Expected outcome:** Build appropriate feature transforms and explain the leakage risks of each.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Numeric Features**

- Standardization, normalization, log transforms
- Binning and interactions
- Which models need scaling

**Topic 2 — Categorical Features**

- One-hot, ordinal, target and frequency encoding
- High-cardinality handling
- Leakage risks of target encoding

**Topic 3 — Missing Data**

- Imputation strategies and missing-indicator features
- Missing completely at random, at random and not at random
- Imputation (mean, median, model-based) and variance shrinkage
- Why the "missing" pattern can itself be predictive

**Topic 4 — Dates and Derived Features**

- Date/time feature extraction
- Ratios, aggregates and domain features
- Feature selection overview

</details>

**Important concepts**

- *Commands / APIs / Code:* `StandardScaler`, `OneHotEncoder`, `SimpleImputer`, `ColumnTransformer`
- *Mechanisms & failure scenarios:* Encoding fit on all data, unseen categories at inference, scaling leakage across folds.

### S03E15 — scikit-learn Pipelines and Preventing Leakage

**Depth:** Intermediate  
**Learning objective:** Package preprocessing and model into one object that is safe to cross-validate and deploy.  
**Prerequisites:** S03E14, S01E03  
**Expected outcome:** Build a leakage-safe pipeline that can be saved and reused.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Pipeline Mechanics**

- Transformers, estimators and the `fit`/`transform` contract
- `Pipeline` and `ColumnTransformer`
- Parameter naming and search through pipelines

**Topic 2 — Leakage Prevention**

- Fitting steps inside each fold
- Custom transformers

**Topic 3 — The Pipeline as a Deployable Unit**

- Serialization of a fitted pipeline
- Training-serving consistency and schema checks at inference
- Versioning the pipeline with the model

</details>

**Important concepts**

- *Commands / APIs / Code:* `Pipeline`, `make_pipeline`, `joblib.dump`, `set_params`
- *Mechanisms & failure scenarios:* Preprocessing done outside CV, pickled pipeline loaded under a different library version, column order mismatch at inference.

<a id="s03-module-5"></a>

## Module 5 — Unsupervised Learning and the Full Workflow

**3 episodes (S03E16–S03E18) · 10 topics.** This module covers: Clustering; Dimensionality Reduction; An End-to-End ML Workflow and Systematic Error Analysis.

| ID | Episode | Depth |
|---|---|---|
| S03E16 | Clustering: k-Means, Hierarchical, and Density-Based Methods | Intermediate |
| S03E17 | Dimensionality Reduction: PCA, t-SNE, and UMAP | Intermediate |
| S03E18 | An End-to-End ML Workflow and Systematic Error Analysis | Intermediate |

### S03E16 — Clustering: k-Means, Hierarchical, and Density-Based Methods

**Depth:** Intermediate  
**Learning objective:** Group unlabeled data and judge whether the groups mean anything.  
**Prerequisites:** S02E05, S03E14  
**Expected outcome:** Pick and validate a clustering approach for a dataset.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — k-Means**

- Centroid algorithm and objective
- Initialization sensitivity (k-means++) and choosing k
- Assumptions: spherical, similar-sized clusters

**Topic 2 — Other Clustering Families**

- Hierarchical clustering and dendrograms
- DBSCAN and noise handling
- Gaussian mixtures and the EM idea
- Soft assignment

**Topic 3 — Evaluating Without Labels**

- Silhouette and internal measures
- Stability checks and business usefulness of segments

</details>

**Important concepts**

- *Commands / APIs / Code:* `KMeans`, `DBSCAN`, `silhouette_score`, `AgglomerativeClustering`
- *Mechanisms & failure scenarios:* k-means on unscaled features, non-convex clusters, clusters that are artifacts of the metric.

### S03E17 — Dimensionality Reduction: PCA, t-SNE, and UMAP

**Depth:** Intermediate  
**Learning objective:** Compress and visualize high-dimensional data without misreading the picture.  
**Prerequisites:** S02E04, S03E16  
**Expected outcome:** Use PCA and visualization tools correctly and state their limitations.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — PCA in Practice**

- Choosing components and reconstruction error
- PCA as preprocessing and for decorrelation

**Topic 2 — Nonlinear Visualization**

- t-SNE and UMAP ideas
- Perplexity and neighbor parameters
- What distances in the plot do and do not mean

**Topic 3 — Use Cases and Limits**

- Embedding visualization
- Noise reduction vs information loss
- Leakage by fitting reducers on all data

</details>

**Important concepts**

- *Commands / APIs / Code:* `PCA(n_components=0.95)`, `TSNE`, `umap.UMAP`
- *Mechanisms & failure scenarios:* Interpreting t-SNE cluster sizes/distances literally, PCA before scaling, leakage by fitting reducers on all data.

### S03E18 — An End-to-End ML Workflow and Systematic Error Analysis

**Depth:** Intermediate  
**Learning objective:** Run a complete, disciplined modeling cycle and use error analysis to decide what to do next.  
**Prerequisites:** S03E09, S03E11, S03E15  
**Expected outcome:** Execute and document an end-to-end tabular ML cycle and justify next steps from errors.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Workflow**

- Baseline → features → model → tuning → final evaluation
- Simple models first; complexity only when justified

**Topic 2 — Recording Work**

- Experiment logs and decision records
- Reproducible seeds and splits

**Topic 3 — Error Analysis**

- Slicing errors by segment and feature ranges
- Inspecting worst predictions
- Label noise vs model limitations

**Topic 4 — Ready for Production?**

- Metrics, cost, latency and fairness checklist
- Documentation and handoff
- Bridge to Season 4 (advanced engineering) and Season 11 (MLOps)

</details>

**Important concepts**

- *Commands / APIs / Code:* baseline `DummyClassifier`, error slicing in Pandas, `joblib` model artifact
- *Mechanisms & failure scenarios:* Jumping to complex models before a baseline, tuning without error analysis, shipping an average that hides a failing segment.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s03-module-1) | Starting point of the season |
| [Module 2](#s03-module-2) | [Module 1](#s03-module-1) (S03E03) |
| [Module 3](#s03-module-3) | [Module 1](#s03-module-1) (S03E03); [Module 2](#s03-module-2) (S03E04, S03E05, S03E07) |
| [Module 4](#s03-module-4) | [Module 1](#s03-module-1) (S03E02); [Module 2](#s03-module-2) (S03E05) |
| [Module 5](#s03-module-5) | [Module 2](#s03-module-2) (S03E09); [Module 3](#s03-module-3) (S03E11); [Module 4](#s03-module-4) (S03E14, S03E15) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 2 — Mathematics for AI & Machine Learning](../season-02-mathematics-for-ai/roadmap.md)
- **Next:** [Season 4 — Advanced Machine Learning Engineering](../season-04-advanced-ml-engineering/roadmap.md)
- **Draws on:** [Season 1](../season-01-python-for-ai-ml/roadmap.md) (S01E03, S01E08); [Season 2](../season-02-mathematics-for-ai/roadmap.md) (S02E02, S02E04, S02E05, S02E07, S02E11, S02E13, S02E14, S02E17)
- **Required by:** [Season 4](../season-04-advanced-ml-engineering/roadmap.md) (via S03E02, S03E03, S03E05, S03E06, S03E08, S03E09, S03E10, S03E11, S03E13, S03E14, S03E15, S03E16); [Season 5](../season-05-deep-learning/roadmap.md) (via S03E05, S03E12); [Season 11](../season-11-mlops-engineering/roadmap.md) (via S03E18); [Season 13](../season-13-ai-infrastructure/roadmap.md) (via S03E06, S03E11)
