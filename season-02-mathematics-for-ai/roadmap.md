# Season 2 Roadmap — Mathematics for AI & Machine Learning

[← Season 2 overview](README.md) · [All seasons](../README.md)

**5 modules · 18 episodes · 68 topics · 184 subtopics · Level: Foundational → Intermediate**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Linear Algebra: The Language of Data](#s02-module-1)
- [Module 2 — Calculus and Optimization: How Models Learn](#s02-module-2)
- [Module 3 — Probability: Reasoning Under Uncertainty](#s02-module-3)
- [Module 4 — Statistics: Evidence and Experiments](#s02-module-4)
- [Module 5 — Information Theory and Numerical Computing](#s02-module-5)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Teach only the mathematics that later seasons use, visually and with code, always tied to an ML consequence ("why does this matter when a model trains?"). Proofs are replaced by geometric and numerical intuition; correctness is preserved.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S02E01 | See a vector as both a list of numbers and a point or direction, and understand the dot product as the basic similarity operation behind embeddings and attention. |
| S02E02 | Understand matrices as functions that move space, and matrix multiplication as composition, so neural network layers become geometry. |
| S02E03 | Reason fluently about tensor shapes, axes and batched operations as used in deep learning frameworks. |
| S02E04 | Understand the directions along which a matrix acts simply, and how that yields dimensionality reduction and compression. |
| S02E05 | Choose distance and size measures deliberately and recognize when a problem is numerically fragile. |
| S02E06 | Understand the gradient as the direction of steepest increase and the chain rule as the mechanism behind backpropagation. |
| S02E07 | Explain how repeatedly stepping downhill trains a model and why step size decides success or failure. |
| S02E08 | Understand why modern optimizers add momentum and per-parameter scaling, and what convexity does and does not guarantee. |
| S02E09 | Understand how frameworks compute exact gradients automatically, and what memory and compute that costs. |
| S02E10 | Build the vocabulary of probability needed to read ML papers and understand model outputs as distributions. |
| S02E11 | Update beliefs with evidence and understand classifiers such as Naive Bayes and the base-rate trap. |
| S02E12 | Summarize distributions and understand why averages of many samples behave predictably. |
| S02E13 | Derive common loss functions from probabilistic assumptions, connecting statistics to training. |
| S02E14 | Quantify uncertainty about a metric computed on a finite sample. |
| S02E15 | Use hypothesis tests correctly to evaluate model changes and online experiments. |
| S02E16 | Recognize when data supports a prediction but not a causal claim, and common ways data misleads. |
| S02E17 | Understand information measures that define the losses used for classification and language models. |
| S02E18 | Understand how finite-precision arithmetic affects training and inference, motivating mixed precision and quantization. |

## Prerequisites and Expected Knowledge

- **Season 1 — [Python for AI & ML Engineering](../season-01-python-for-ai-ml/roadmap.md)**: S01E06

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Linear Algebra: The Language of Data](#s02-module-1) | S02E01–S02E05 | 5 | 3 Foundational, 2 Intermediate |
| 2 | [Calculus and Optimization: How Models Learn](#s02-module-2) | S02E06–S02E09 | 4 | 2 Foundational, 2 Intermediate |
| 3 | [Probability: Reasoning Under Uncertainty](#s02-module-3) | S02E10–S02E13 | 4 | 3 Foundational, 1 Intermediate |
| 4 | [Statistics: Evidence and Experiments](#s02-module-4) | S02E14–S02E16 | 3 | 3 Intermediate |
| 5 | [Information Theory and Numerical Computing](#s02-module-5) | S02E17–S02E18 | 2 | 2 Intermediate |

<a id="s02-module-1"></a>

## Module 1 — Linear Algebra: The Language of Data

**5 episodes (S02E01–S02E05) · 19 topics.** This module covers: Vectors, Dot Products, and the Geometry of Similarity; Matrices as Transformations and Matrix Multiplication; Tensors, Shapes, and Batched Computation; Eigenvectors, SVD, and PCA Intuition; Norms, Distance Metrics, and Numerical Conditioning.

| ID | Episode | Depth |
|---|---|---|
| S02E01 | Vectors, Dot Products, and the Geometry of Similarity | Foundational |
| S02E02 | Matrices as Transformations and Matrix Multiplication | Foundational |
| S02E03 | Tensors, Shapes, and Batched Computation | Foundational |
| S02E04 | Eigenvectors, SVD, and PCA Intuition | Intermediate |
| S02E05 | Norms, Distance Metrics, and Numerical Conditioning | Intermediate |

### S02E01 — Vectors, Dot Products, and the Geometry of Similarity

**Depth:** Foundational  
**Learning objective:** See a vector as both a list of numbers and a point or direction, and understand the dot product as the basic similarity operation behind embeddings and attention.  
**Prerequisites:** S01E06  
**Expected outcome:** Compute and interpret dot products and cosine similarity and explain when each is appropriate.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Vectors**

- Data points, features and embeddings as vectors
- Vector addition, scaling and linear combinations
- Span, basis and linear independence, intuitively

**Topic 2 — Dot Product and Angle**

- Algebraic and geometric definitions
- Projection and decomposition of a vector
- Cosine similarity vs raw dot product

**Topic 3 — Why ML Cares**

- Similarity search and recommendation scoring
- A single neuron as a dot product plus bias
- Attention scores as dot products (preview of Season 6)

**Topic 4 — High-Dimensional Geometry**

- Concentration of distances in high dimensions
- Near-orthogonality of random vectors
- Consequences for nearest-neighbor search

</details>

**Important concepts**

- *Commands / APIs / Code:* `np.dot`, `np.linalg.norm`, cosine similarity in NumPy
- *Mechanisms & failure scenarios:* Comparing unnormalized vectors, dot-product scores dominated by magnitude, distance concentration in very high dimensions.

### S02E02 — Matrices as Transformations and Matrix Multiplication

**Depth:** Foundational  
**Learning objective:** Understand matrices as functions that move space, and matrix multiplication as composition, so neural network layers become geometry.  
**Prerequisites:** S02E01  
**Expected outcome:** Visualize a layer's weight matrix as a transformation and reason about shapes and cost.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Matrix as a Transformation**

- Rotation, scaling, shear, projection
- Columns as where basis vectors land
- Linear vs affine maps

**Topic 2 — Matrix Multiplication**

- Row-by-column rule and the composition view
- Shapes and what is allowed; cost in operations and memory

**Topic 3 — Rank, Inverses, and Linear Systems**

- Solving linear systems; inverse and determinant
- Rank, null space and singular matrices
- Why solvers beat explicit inverses

**Topic 4 — Application: Least Squares**

- Normal equation for linear regression
- Geometry of projection onto a column space

</details>

**Important concepts**

- *Commands / APIs / Code:* `A @ B`, `np.linalg.solve`, `np.linalg.inv`
- *Mechanisms & failure scenarios:* Shape mismatches, singular or ill-conditioned matrices producing unstable solutions, confusing element-wise and matrix products.

### S02E03 — Tensors, Shapes, and Batched Computation

**Depth:** Foundational  
**Learning objective:** Reason fluently about tensor shapes, axes and batched operations as used in deep learning frameworks.  
**Prerequisites:** S02E02, S01E06  
**Expected outcome:** Annotate and debug tensor shapes through a small model's forward pass.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — From Scalars to Tensors**

- Rank, shape and axes
- Batch, channel, sequence and feature dimensions
- Images, text and time series as tensors

**Topic 2 — Operations on Tensors**

- Reshape, transpose, permute
- Reductions and `keepdims`

**Topic 3 — Batched Computation and Shape Discipline**

- Batched matmul and `einsum` notation
- Broadcasting math revisited
- Reading and annotating shapes in model code
- Memory layout, views and contiguity

</details>

**Important concepts**

- *Commands / APIs / Code:* `torch.einsum`, `tensor.shape`, `.permute`, `.view`
- *Mechanisms & failure scenarios:* Wrong axis reductions that still run, silent broadcasting, transposed batch/sequence dimensions.

### S02E04 — Eigenvectors, SVD, and PCA Intuition

**Depth:** Intermediate  
**Learning objective:** Understand the directions along which a matrix acts simply, and how that yields dimensionality reduction and compression.  
**Prerequisites:** S02E02, S02E01  
**Expected outcome:** Explain what PCA and SVD compute and when low-rank structure helps.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Eigenvectors and Eigenvalues**

- Directions that only stretch
- Symmetric matrices and the spectral theorem
- Covariance matrices as the main ML example

**Topic 2 — Singular Value Decomposition**

- Decomposing any matrix into rotation, scaling, rotation
- Singular values and rank
- Computing SVD in practice

**Topic 3 — Low-Rank Approximation**

- Best rank-k approximation (Eckart–Young idea)
- Compression and denoising
- Connection to LoRA-style adapters (preview of Season 6)

**Topic 4 — PCA**

- Variance maximization and principal components
- Explained variance and choosing components
- PCA via eigendecomposition vs SVD

**Topic 5 — Limits and Pitfalls**

- Linearity, scale sensitivity
- Low-variance but predictive directions
- Components are not causes

</details>

**Important concepts**

- *Commands / APIs / Code:* `np.linalg.eig`, `np.linalg.svd`, `sklearn.decomposition.PCA`
- *Mechanisms & failure scenarios:* PCA on unscaled features, discarding low-variance but predictive directions, misreading components as causes.

### S02E05 — Norms, Distance Metrics, and Numerical Conditioning

**Depth:** Intermediate  
**Learning objective:** Choose distance and size measures deliberately and recognize when a problem is numerically fragile.  
**Prerequisites:** S02E01, S02E02  
**Expected outcome:** Select a metric and diagnose an ill-conditioned problem.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Norms**

- L1, L2, L∞ and their geometry
- Frobenius norm for matrices
- Regularization as a norm penalty (preview)

**Topic 2 — Distance and Similarity Measures**

- Euclidean, Manhattan, cosine, Mahalanobis
- Choosing a metric for a task and for how embeddings were trained
- Effects of feature scaling

**Topic 3 — Conditioning**

- Condition number and sensitivity
- Multicollinearity and unstable regression
- Why normalization helps training

</details>

**Important concepts**

- *Commands / APIs / Code:* `np.linalg.norm(ord=…)`, `np.linalg.cond`, `scipy.spatial.distance`
- *Mechanisms & failure scenarios:* Distance dominated by one large-scale feature, near-singular design matrices, metric mismatch with how embeddings were trained.

<a id="s02-module-2"></a>

## Module 2 — Calculus and Optimization: How Models Learn

**4 episodes (S02E06–S02E09) · 16 topics.** This module covers: Derivatives, Gradients, and the Chain Rule; Gradient Descent; Convexity, Momentum, and Adaptive Optimizers; Automatic Differentiation and Computational Graphs.

| ID | Episode | Depth |
|---|---|---|
| S02E06 | Derivatives, Gradients, and the Chain Rule | Foundational |
| S02E07 | Gradient Descent: Loss Surfaces, Learning Rates, and Convergence | Foundational |
| S02E08 | Convexity, Momentum, and Adaptive Optimizers | Intermediate |
| S02E09 | Automatic Differentiation and Computational Graphs | Intermediate |

### S02E06 — Derivatives, Gradients, and the Chain Rule

**Depth:** Foundational  
**Learning objective:** Understand the gradient as the direction of steepest increase and the chain rule as the mechanism behind backpropagation.  
**Prerequisites:** S02E01  
**Expected outcome:** Compute gradients of simple composite functions and explain chain-rule flow.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Derivatives**

- Slope, rate of change and numerical approximation
- Partial derivatives and the gradient vector
- Gradient direction and magnitude

**Topic 2 — The Chain Rule**

- Composite functions and local derivatives
- A tiny network differentiated by hand

**Topic 3 — Jacobians and Hessians**

- Vector-valued functions and the Jacobian
- Curvature and what the Hessian tells us
- Why only first-order methods are used at scale

**Topic 4 — Checking Gradients**

- Finite-difference gradient checks
- Step size and numerical error
- Common sign and shape mistakes

</details>

**Important concepts**

- *Commands / APIs / Code:* finite differences in Python, `torch.autograd.grad`
- *Mechanisms & failure scenarios:* Wrong sign conventions, numerical gradients that disagree with analytic gradients, gradients that vanish through saturating functions.

### S02E07 — Gradient Descent: Loss Surfaces, Learning Rates, and Convergence

**Depth:** Foundational  
**Learning objective:** Explain how repeatedly stepping downhill trains a model and why step size decides success or failure.  
**Prerequisites:** S02E06  
**Expected outcome:** Implement and tune gradient descent and diagnose divergence or stagnation from the loss curve.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Algorithm**

- Loss as a function of parameters
- Update rule and learning rate

**Topic 2 — Dynamics**

- Convergence, oscillation, divergence
- Learning rate too high vs too low
- Plateaus, saddle points and local minima

**Topic 3 — Stochastic and Mini-Batch Descent**

- Batch, stochastic and mini-batch variants
- Gradient noise and why it can help
- Epochs, iterations and stopping criteria

**Topic 4 — A Worked Example**

- Fitting a line by gradient descent
- Visualizing the path on a loss surface

</details>

**Important concepts**

- *Commands / APIs / Code:* NumPy gradient descent loop, loss-curve plot
- *Mechanisms & failure scenarios:* Divergence from a large learning rate, extremely slow progress from a tiny one, noisy gradients from small batches.

### S02E08 — Convexity, Momentum, and Adaptive Optimizers

**Depth:** Intermediate  
**Learning objective:** Understand why modern optimizers add momentum and per-parameter scaling, and what convexity does and does not guarantee.  
**Prerequisites:** S02E07  
**Expected outcome:** Compare optimizers on a loss surface and justify a choice and schedule.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Convex vs Non-Convex**

- Convex functions and guaranteed minima
- Why deep learning is non-convex but still trainable
- Ill-conditioned valleys

**Topic 2 — Momentum**

- Momentum as accumulated velocity
- Nesterov acceleration

**Topic 3 — Adaptive Optimizers**

- RMSProp and Adam: first- and second-moment estimates
- Bias correction
- Weight decay and the AdamW distinction

**Topic 4 — Schedules and Stabilization**

- Learning-rate decay, warmup and cosine schedules
- Gradient clipping
- Choosing an optimizer in practice

</details>

**Important concepts**

- *Commands / APIs / Code:* `torch.optim.SGD/Adam/AdamW`, `lr_scheduler`, `clip_grad_norm_`
- *Mechanisms & failure scenarios:* Adam's generalization differences from SGD, exploding gradients, wrong weight-decay implementation.

### S02E09 — Automatic Differentiation and Computational Graphs

**Depth:** Intermediate  
**Learning objective:** Understand how frameworks compute exact gradients automatically, and what memory and compute that costs.  
**Prerequisites:** S02E06, S02E03  
**Expected outcome:** Trace a backward pass on a small graph and explain training memory behavior.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Computational Graphs**

- Operations as nodes, tensors as edges
- Forward evaluation and graph recording
- Static vs dynamic graphs

**Topic 2 — Reverse-Mode Differentiation**

- Backward pass: propagating gradients
- Forward vs reverse mode and why reverse wins for many parameters

**Topic 3 — Costs**

- Activation memory held for backward
- Gradient accumulation and `zero_grad`

**Topic 4 — Controls and Pitfalls**

- Detaching, no-grad regions and checkpointing
- In-place operations that break autograd
- Higher-order derivatives (overview)

</details>

**Important concepts**

- *Commands / APIs / Code:* `loss.backward()`, `requires_grad`, `torch.no_grad()`, `torch.utils.checkpoint`
- *Mechanisms & failure scenarios:* Forgetting to zero gradients, graph retained across iterations leaking memory, in-place operations breaking autograd.

<a id="s02-module-3"></a>

## Module 3 — Probability: Reasoning Under Uncertainty

**4 episodes (S02E10–S02E13) · 15 topics.** This module covers: Probability Basics, Random Variables, and Distributions; Conditional Probability and Bayes' Rule; Expectation, Variance, Covariance, and the Central Limit Theorem; Maximum Likelihood and Why Loss Functions Look the Way They Do.

| ID | Episode | Depth |
|---|---|---|
| S02E10 | Probability Basics, Random Variables, and Distributions | Foundational |
| S02E11 | Conditional Probability and Bayes' Rule | Foundational |
| S02E12 | Expectation, Variance, Covariance, and the Central Limit Theorem | Foundational |
| S02E13 | Maximum Likelihood and Why Loss Functions Look the Way They Do | Intermediate |

### S02E10 — Probability Basics, Random Variables, and Distributions

**Depth:** Foundational  
**Learning objective:** Build the vocabulary of probability needed to read ML papers and understand model outputs as distributions.  
**Prerequisites:** S01E06  
**Expected outcome:** Identify suitable distributions for data and interpret a model's probabilistic output.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Probability Fundamentals**

- Sample spaces, events and axioms
- Discrete vs continuous random variables
- PMF, PDF and CDF

**Topic 2 — Key Distributions**

- Bernoulli, binomial and categorical
- Normal distribution and why it appears everywhere
- Uniform, exponential and Poisson

**Topic 3 — Joint and Marginal Distributions**

- Joint, marginal and conditional views
- Multivariate normal as a worked example

**Topic 4 — Sampling**

- Drawing from distributions and reproducible seeds
- Softmax outputs as categorical distributions

</details>

**Important concepts**

- *Commands / APIs / Code:* `np.random.default_rng`, `scipy.stats`, histogram of samples
- *Mechanisms & failure scenarios:* Treating a density as a probability, assuming normality of heavy-tailed data, unseeded random sampling.

### S02E11 — Conditional Probability and Bayes' Rule

**Depth:** Foundational  
**Learning objective:** Update beliefs with evidence and understand classifiers such as Naive Bayes and the base-rate trap.  
**Prerequisites:** S02E10  
**Expected outcome:** Apply Bayes' rule to a screening/classification scenario and explain why precision depends on prevalence.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Conditional Probability**

- Joint, marginal and conditional probability
- Independence and conditional independence
- The chain rule of probability

**Topic 2 — Bayes' Rule**

- Prior, likelihood and posterior
- Base-rate neglect with a screening-test example
- Sequential updating

**Topic 3 — Bayes in ML**

- Naive Bayes classifier and smoothing
- Language modeling as conditional probability
- Probabilistic view of classification

</details>

**Important concepts**

- *Commands / APIs / Code:* worked Bayes calculation in Python, `sklearn.naive_bayes`
- *Mechanisms & failure scenarios:* Ignoring class prevalence, assuming independence that does not hold, zero-probability events without smoothing.

### S02E12 — Expectation, Variance, Covariance, and the Central Limit Theorem

**Depth:** Foundational  
**Learning objective:** Summarize distributions and understand why averages of many samples behave predictably.  
**Prerequisites:** S02E10  
**Expected outcome:** Explain sampling noise and estimate quantities by simulation.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Summaries of a Distribution**

- Expected value, variance and standard deviation
- Linearity of expectation

**Topic 2 — Covariance and Correlation**

- Covariance matrices (link to PCA)
- Correlation vs dependence

**Topic 3 — Limit Theorems**

- Law of large numbers
- Central limit theorem and its conditions
- Why mini-batch gradients are noisy but unbiased

**Topic 4 — Monte Carlo Estimation**

- Estimating quantities by sampling
- Standard error and sample size
- Heavy tails where the CLT disappoints

</details>

**Important concepts**

- *Commands / APIs / Code:* `np.cov`, simulation of sample means, Monte Carlo estimate in Python
- *Mechanisms & failure scenarios:* Averages of heavy-tailed data not converging quickly, correlation mistaken for dependence, small-sample overconfidence.

### S02E13 — Maximum Likelihood and Why Loss Functions Look the Way They Do

**Depth:** Intermediate  
**Learning objective:** Derive common loss functions from probabilistic assumptions, connecting statistics to training.  
**Prerequisites:** S02E11, S02E12  
**Expected outcome:** Justify the loss function for a given prediction task from its noise assumptions.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Likelihood**

- Likelihood vs probability
- Maximum likelihood estimation
- Log-likelihood and why logs are used

**Topic 2 — Losses as Negative Log-Likelihood**

- Gaussian noise gives mean squared error
- Bernoulli and categorical give cross-entropy

**Topic 3 — Regularization as a Prior**

- MAP estimation
- L2 as a Gaussian prior; L1 as a Laplace prior

**Topic 4 — Interpretation**

- Calibration and probabilistic predictions
- When the assumed distribution is wrong
- Link to language-model training

</details>

**Important concepts**

- *Commands / APIs / Code:* manual MLE for a coin and a Gaussian, `torch.nn.CrossEntropyLoss`
- *Mechanisms & failure scenarios:* MSE on classification, outliers dominating squared loss, probabilities that are not calibrated.

<a id="s02-module-4"></a>

## Module 4 — Statistics: Evidence and Experiments

**3 episodes (S02E14–S02E16) · 11 topics.** This module covers: Sampling, Estimation, and Confidence Intervals; Hypothesis Testing, p-Values, and A/B Testing for ML; Correlation, Causation, Bias, and Statistical Traps.

| ID | Episode | Depth |
|---|---|---|
| S02E14 | Sampling, Estimation, and Confidence Intervals | Intermediate |
| S02E15 | Hypothesis Testing, p-Values, and A/B Testing for ML | Intermediate |
| S02E16 | Correlation, Causation, Bias, and Statistical Traps | Intermediate |

### S02E14 — Sampling, Estimation, and Confidence Intervals

**Depth:** Intermediate  
**Learning objective:** Quantify uncertainty about a metric computed on a finite sample.  
**Prerequisites:** S02E12  
**Expected outcome:** Attach a defensible interval to a model metric and judge whether a difference is meaningful.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Populations and Samples**

- Sampling bias and representativeness
- Estimators, bias and variance
- Standard error

**Topic 2 — Confidence Intervals**

- Meaning (and common misreadings) of a CI
- Analytic intervals and the bootstrap

**Topic 3 — Evaluating Models with Uncertainty**

- Intervals for accuracy, F1 and AUC
- How big must the evaluation set be?
- Paired comparisons on the same examples
- Reporting results honestly

</details>

**Important concepts**

- *Commands / APIs / Code:* bootstrap resampling in NumPy, `scipy.stats.bootstrap`
- *Mechanisms & failure scenarios:* Reading a CI as probability of the parameter, tiny test sets, repeated peeking at a test set.

### S02E15 — Hypothesis Testing, p-Values, and A/B Testing for ML

**Depth:** Intermediate  
**Learning objective:** Use hypothesis tests correctly to evaluate model changes and online experiments.  
**Prerequisites:** S02E14  
**Expected outcome:** Design a basic A/B test for a model change and interpret its result.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Logic of Testing**

- Null and alternative hypotheses
- p-values, significance, Type I and II errors, power
- Effect size

**Topic 2 — Common Tests**

- t-test, chi-square, ANOVA and F-test (overview), nonparametric alternatives
- Paired tests for model comparison

**Topic 3 — Multiple Comparisons**

- Why many metrics create false positives
- Bonferroni and false-discovery-rate corrections

**Topic 4 — Experiments for ML Systems**

- A/B test design: randomization, duration, metrics
- Novelty effects and interference

**Topic 5 — Interpreting Results**

- Statistical vs practical significance
- Peeking, early stopping and p-hacking

</details>

**Important concepts**

- *Commands / APIs / Code:* `scipy.stats.ttest_rel`, `statsmodels`, power calculation
- *Mechanisms & failure scenarios:* p-hacking, stopping tests early, multiple-metric false positives, unbalanced traffic splits.

### S02E16 — Correlation, Causation, Bias, and Statistical Traps

**Depth:** Intermediate  
**Learning objective:** Recognize when data supports a prediction but not a causal claim, and common ways data misleads.  
**Prerequisites:** S02E14  
**Expected outcome:** Spot confounding and selection effects in an ML dataset.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Correlation vs Causation**

- Confounders, colliders and mediators
- Simple causal diagrams (DAGs)
- Spurious correlation

**Topic 2 — Classic Traps**

- Simpson's paradox
- Selection and survivorship bias
- Data dredging

**Topic 3 — Implications for ML**

- Models learning shortcuts
- Distribution shift and why causal structure matters
- Limits of observational data and the bridge to causal inference (Season 4)

</details>

**Important concepts**

- *Commands / APIs / Code:* group-wise vs aggregate comparison in Pandas, simple confounder simulation
- *Mechanisms & failure scenarios:* Shortcut features that collapse in deployment, aggregated metrics hiding subgroup failure.

<a id="s02-module-5"></a>

## Module 5 — Information Theory and Numerical Computing

**2 episodes (S02E17–S02E18) · 7 topics.** This module covers: Entropy, Cross-Entropy, and KL Divergence; Numerical Precision.

| ID | Episode | Depth |
|---|---|---|
| S02E17 | Entropy, Cross-Entropy, and KL Divergence | Intermediate |
| S02E18 | Numerical Precision: Floating Point, Overflow, and Stable Softmax | Intermediate |

### S02E17 — Entropy, Cross-Entropy, and KL Divergence

**Depth:** Intermediate  
**Learning objective:** Understand information measures that define the losses used for classification and language models.  
**Prerequisites:** S02E13  
**Expected outcome:** Compute entropy, cross-entropy and KL for small distributions and interpret perplexity.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Entropy**

- Information content and surprise
- Entropy as uncertainty; bits vs nats

**Topic 2 — Cross-Entropy, KL Divergence, and Mutual Information**

- Cross-entropy as expected surprise under the wrong model
- Link to maximum likelihood
- Definition and asymmetry of KL
- Mutual information as shared information

**Topic 3 — Uses in AI**

- Classification loss and perplexity
- KL penalties in RLHF/DPO and VAEs (previews)
- Distillation with soft targets

</details>

**Important concepts**

- *Commands / APIs / Code:* `scipy.stats.entropy`, `torch.nn.functional.kl_div`, perplexity calculation
- *Mechanisms & failure scenarios:* log of zero, KL direction confusion, comparing perplexities across different tokenizers.

### S02E18 — Numerical Precision: Floating Point, Overflow, and Stable Softmax

**Depth:** Intermediate  
**Learning objective:** Understand how finite-precision arithmetic affects training and inference, motivating mixed precision and quantization.  
**Prerequisites:** S02E17, S02E08  
**Expected outcome:** Explain and fix a NaN-from-softmax failure and choose precisions with understanding.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Floating-Point Representation**

- Sign, exponent, mantissa
- FP32, FP16, BF16, INT8 trade-offs
- Rounding error and accumulation

**Topic 2 — Stability Techniques**

- Overflow/underflow and the log-sum-exp trick
- Stable softmax and cross-entropy

**Topic 3 — Mixed Precision**

- Why lower precision speeds up and where it breaks
- Loss scaling
- Quantization error preview (Season 6)

**Topic 4 — Nondeterminism**

- Parallel reductions and non-associativity
- Different results across hardware

</details>

**Important concepts**

- *Commands / APIs / Code:* `np.finfo`, naive vs stable softmax, `torch.autocast`
- *Mechanisms & failure scenarios:* NaN losses from overflow, silent precision loss when summing small values, different results across hardware.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s02-module-1) | Starting point of the season |
| [Module 2](#s02-module-2) | [Module 1](#s02-module-1) (S02E01, S02E03) |
| [Module 3](#s02-module-3) | Within-module sequence only |
| [Module 4](#s02-module-4) | [Module 3](#s02-module-3) (S02E12) |
| [Module 5](#s02-module-5) | [Module 2](#s02-module-2) (S02E08); [Module 3](#s02-module-3) (S02E13) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 1 — Python for AI & ML Engineering](../season-01-python-for-ai-ml/roadmap.md)
- **Next:** [Season 3 — Machine Learning Foundations](../season-03-machine-learning/roadmap.md)
- **Draws on:** [Season 1](../season-01-python-for-ai-ml/roadmap.md) (S01E06)
- **Required by:** [Season 3](../season-03-machine-learning/roadmap.md) (via S02E02, S02E04, S02E05, S02E07, S02E11, S02E13, S02E14, S02E17); [Season 4](../season-04-advanced-ml-engineering/roadmap.md) (via S02E04, S02E13, S02E15, S02E16); [Season 5](../season-05-deep-learning/roadmap.md) (via S02E01, S02E02, S02E03, S02E04, S02E06, S02E07, S02E08, S02E09, S02E11, S02E12, S02E13, S02E17, S02E18); [Season 6](../season-06-llms-and-transformers/roadmap.md) (via S02E03, S02E04, S02E10, S02E14, S02E17, S02E18); [Season 8](../season-08-rag-engineering/roadmap.md) (via S02E05); [Season 11](../season-11-mlops-engineering/roadmap.md) (via S02E14); [Season 12](../season-12-llmops-engineering/roadmap.md) (via S02E14)
