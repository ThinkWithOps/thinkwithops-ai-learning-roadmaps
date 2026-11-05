# Season 5 Roadmap — Deep Learning & Neural Networks

[← Season 5 overview](README.md) · [All seasons](../README.md)

**9 modules · 28 episodes · 118 topics · 293 subtopics · Level: Intermediate → Advanced**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Neural Network Foundations](#s05-module-1)
- [Module 2 — Training Deep Networks](#s05-module-2)
- [Module 3 — Computer Vision](#s05-module-3)
- [Module 4 — Sequences and Representation](#s05-module-4)
- [Module 5 — Applied Vision: Video and Documents](#s05-module-5)
- [Module 6 — Audio and Speech](#s05-module-6)
- [Module 7 — Generative Models](#s05-module-7)
- [Module 8 — Reinforcement Learning](#s05-module-8)
- [Module 9 — Representation Learning and Training at Scale](#s05-module-9)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Teach neural networks as trainable computational graphs: how they represent data, how backpropagation and optimizers train them, how vision (including video and document understanding), speech and audio, generative models and reinforcement learning work, and how to debug and scale training. It prepares learners directly for transformers and LLMs in Season 6.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S05E01 | Understand how stacked linear maps and nonlinearities form a universal function approximator. |
| S05E02 | Follow gradients backward through a network and understand vanishing/exploding gradients. |
| S05E03 | Pair output layers, activations and losses correctly for each task type. |
| S05E04 | Understand why initial weights and normalization layers make deep networks trainable. |
| S05E05 | Apply the optimizer theory from Season 2 to real training runs and tune the knobs that matter. |
| S05E06 | Control overfitting in high-capacity networks with several complementary techniques. |
| S05E07 | Understand every line of a standard training loop and what it costs. |
| S05E08 | Systematically find why a network is not learning. |
| S05E09 | Explain how convolution exploits image structure and how features build hierarchically. |
| S05E10 | Understand landmark architectures and reuse pretrained models effectively. |
| S05E11 | Understand how models localize and delineate objects, and how their quality is measured. |
| S05E12 | Understand sequence modeling before attention, and the limitations that motivated transformers. |
| S05E13 | Understand how networks learn dense vector representations and why embeddings are central to modern AI. |
| S05E14 | Understand how models add the time dimension to vision: motion, action recognition and tracking objects across frames. |
| S05E15 | Understand how text is located and read in images and how page layout, tables and forms become structured data. |
| S05E16 | Understand how sound becomes numbers and the representations models use for audio classification, detection and speech tasks. |
| S05E17 | Explain how speech is transcribed and generated, the trade-offs of streaming systems, and how quality and risk are measured. |
| S05E18 | Understand compression, latent spaces and probabilistic generation through autoencoders. |
| S05E19 | Understand adversarial training and why it is powerful but unstable. |
| S05E20 | Explain how a diffusion model is trained to reverse a gradual noising process and what the network actually predicts. |
| S05E21 | Explain how images are generated at inference time, how text steers generation, and why latent diffusion made it practical. |
| S05E22 | Understand how an agent learns to act from rewards: the formal problem, value functions, and the basic learning algorithms. |
| S05E23 | Understand how policies are optimized directly, why variance matters, and how PPO stabilizes learning (the algorithm behind RLHF-style training). |
| S05E24 | Understand how neural networks scale RL to hard problems and what makes RL projects succeed or fail in practice. |
| S05E25 | Understand how models learn from unlabeled data, the idea that powers foundation models. |
| S05E26 | Understand where GPU memory and time go during training and the first scaling techniques. |
| S05E27 | Keep accelerators busy and training data correct. |
| S05E28 | Run a deep-learning project with the same discipline as classical ML, adapted to expensive experiments. |

## Prerequisites and Expected Knowledge

- **Season 1 — [Python for AI & ML Engineering](../season-01-python-for-ai-ml/roadmap.md)**: S01E03, S01E11
- **Season 2 — [Mathematics for AI & Machine Learning](../season-02-mathematics-for-ai/roadmap.md)**: S02E01, S02E02, S02E03, S02E04, S02E06, S02E07, S02E08, S02E09, S02E11, S02E12, S02E13, S02E17, S02E18
- **Season 3 — [Machine Learning Foundations](../season-03-machine-learning/roadmap.md)**: S03E05, S03E12
- **Season 4 — [Advanced Machine Learning Engineering](../season-04-advanced-ml-engineering/roadmap.md)**: S04E16

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Neural Network Foundations](#s05-module-1) | S05E01–S05E03 | 3 | 1 Foundational, 2 Intermediate |
| 2 | [Training Deep Networks](#s05-module-2) | S05E04–S05E08 | 5 | 4 Intermediate, 1 Advanced |
| 3 | [Computer Vision](#s05-module-3) | S05E09–S05E11 | 3 | 2 Intermediate, 1 Advanced |
| 4 | [Sequences and Representation](#s05-module-4) | S05E12–S05E13 | 2 | 2 Intermediate |
| 5 | [Applied Vision: Video and Documents](#s05-module-5) | S05E14–S05E15 | 2 | 1 Advanced, 1 Intermediate |
| 6 | [Audio and Speech](#s05-module-6) | S05E16–S05E17 | 2 | 1 Intermediate, 1 Advanced |
| 7 | [Generative Models](#s05-module-7) | S05E18–S05E21 | 4 | 3 Advanced, 1 Intermediate |
| 8 | [Reinforcement Learning](#s05-module-8) | S05E22–S05E24 | 3 | 1 Intermediate, 2 Advanced |
| 9 | [Representation Learning and Training at Scale](#s05-module-9) | S05E25–S05E28 | 4 | 2 Advanced, 2 Intermediate |

<a id="s05-module-1"></a>

## Module 1 — Neural Network Foundations

**3 episodes (S05E01–S05E03) · 13 topics.** This module covers: From Perceptron to Multilayer Networks; Backpropagation; Loss Functions and Output Layers for Deep Learning.

| ID | Episode | Depth |
|---|---|---|
| S05E01 | From Perceptron to Multilayer Networks: Neurons, Layers, and Activations | Foundational |
| S05E02 | Backpropagation: How Networks Learn | Intermediate |
| S05E03 | Loss Functions and Output Layers for Deep Learning | Intermediate |

### S05E01 — From Perceptron to Multilayer Networks: Neurons, Layers, and Activations

**Depth:** Foundational  
**Learning objective:** Understand how stacked linear maps and nonlinearities form a universal function approximator.  
**Prerequisites:** S03E05, S02E02  
**Expected outcome:** Describe a forward pass through an MLP and justify an activation choice.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Artificial Neuron**

- Weighted sum, bias and activation
- Relationship to logistic regression
- Why one neuron is limited (XOR)

**Topic 2 — Layers and Depth**

- Dense layers as matrix multiplications
- Hidden representations and feature hierarchies
- Why depth helps: composition of simple functions

**Topic 3 — Activation Functions**

- Sigmoid, tanh, ReLU, GELU, SiLU
- Saturation and dead units
- Choosing activations

**Topic 4 — Capacity and Approximation**

- Universal approximation (what it does and does not say)
- Parameter counts and capacity

</details>

**Important concepts**

- *Commands / APIs / Code:* `torch.nn.Linear`, `nn.Sequential`, activation modules
- *Mechanisms & failure scenarios:* Dead ReLUs, saturated sigmoids stalling learning, removing nonlinearities collapsing depth to one linear layer.

### S05E02 — Backpropagation: How Networks Learn

**Depth:** Intermediate  
**Learning objective:** Follow gradients backward through a network and understand vanishing/exploding gradients.  
**Prerequisites:** S05E01, S02E06, S02E09  
**Expected outcome:** Derive and verify gradients for a small network and recognize pathological gradient flow.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Forward and Backward Pass**

- Caching activations
- Chain rule applied layer by layer

**Topic 2 — A Worked Example**

- Two-layer network by hand
- Gradients with respect to weights and inputs

**Topic 3 — Backpropagation in Matrix Form**

- Batched gradients and shapes
- Why backward costs about twice forward

**Topic 4 — Gradient Pathologies**

- Vanishing and exploding gradients
- Effect of activation and depth

**Topic 5 — Verifying Gradients**

- Checking against autograd and finite differences
- Common implementation bugs

</details>

**Important concepts**

- *Commands / APIs / Code:* manual backprop in NumPy, `loss.backward()`, `param.grad` inspection
- *Mechanisms & failure scenarios:* Gradients shrinking to zero in deep sigmoid networks, exploding updates, forgetting to detach cached values.

### S05E03 — Loss Functions and Output Layers for Deep Learning

**Depth:** Intermediate  
**Learning objective:** Pair output layers, activations and losses correctly for each task type.  
**Prerequisites:** S05E01, S02E13, S02E17  
**Expected outcome:** Choose the output layer and loss for a given task without numerical or shape mistakes.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Task-to-Loss Mapping**

- Regression: MSE, Huber
- Binary and multiclass classification: BCE and cross-entropy with logits
- Multi-label and ordinal targets

**Topic 2 — Output Layers**

- Logits vs probabilities
- Softmax and numerical stability
- Class-imbalance weighting

**Topic 3 — Specialized Losses**

- Contrastive and triplet losses
- Label smoothing

**Topic 4 — Practical Pitfalls**

- Wrong target dtype or shape; applying softmax before a logits-based loss
- Custom losses and gradient checks

</details>

**Important concepts**

- *Commands / APIs / Code:* `BCEWithLogitsLoss`, `CrossEntropyLoss`, `label_smoothing`
- *Mechanisms & failure scenarios:* Applying softmax before a loss that expects logits, wrong target dtype or shape, class-weight misconfiguration.

<a id="s05-module-2"></a>

## Module 2 — Training Deep Networks

**5 episodes (S05E04–S05E08) · 19 topics.** This module covers: Initialization and Normalization; Optimization in Practice; Regularization in Deep Learning; The PyTorch Training Loop; Debugging Training.

| ID | Episode | Depth |
|---|---|---|
| S05E04 | Initialization and Normalization: Keeping Signals Stable | Intermediate |
| S05E05 | Optimization in Practice: Batch Size, Learning-Rate Schedules, and Warmup | Intermediate |
| S05E06 | Regularization in Deep Learning: Dropout, Weight Decay, Augmentation, and Early Stopping | Intermediate |
| S05E07 | The PyTorch Training Loop: Tensors, Autograd, DataLoader, and Devices | Intermediate |
| S05E08 | Debugging Training: Loss Curves, Overfitting a Batch, NaNs, and Mixed Precision | Advanced |

### S05E04 — Initialization and Normalization: Keeping Signals Stable

**Depth:** Intermediate  
**Learning objective:** Understand why initial weights and normalization layers make deep networks trainable.  
**Prerequisites:** S05E02  
**Expected outcome:** Select initialization and normalization for an architecture and explain train/eval differences.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Initialization**

- Variance preservation, Xavier and He schemes
- Symmetry breaking and effects on early training

**Topic 2 — Normalization Layers**

- BatchNorm: statistics, train vs eval behavior
- LayerNorm, GroupNorm and RMSNorm
- Where normalization is placed

**Topic 3 — Residual Connections and Diagnosing Signal Stability**

- Skip connections and gradient flow
- Why residual networks train at depth
- Activation and gradient statistics per layer
- Batch-size sensitivity of BatchNorm

</details>

**Important concepts**

- *Commands / APIs / Code:* `nn.init.kaiming_normal_`, `nn.BatchNorm1d`, `nn.LayerNorm`, `model.eval()`
- *Mechanisms & failure scenarios:* BatchNorm in eval mode with unstable running statistics, tiny batches breaking BatchNorm, poor initialization causing early divergence.

### S05E05 — Optimization in Practice: Batch Size, Learning-Rate Schedules, and Warmup

**Depth:** Intermediate  
**Learning objective:** Apply the optimizer theory from Season 2 to real training runs and tune the knobs that matter.  
**Prerequisites:** S02E08, S05E02  
**Expected outcome:** Configure optimizer, schedule and batch settings deliberately and diagnose instabilities.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Practical Optimizers**

- SGD with momentum vs AdamW in practice
- Weight decay and decoupling

**Topic 2 — Schedules and Batch Size**

- Warmup, cosine decay and one-cycle
- Learning-rate finder idea
- Batch size, gradient accumulation and learning-rate scaling
- Large-batch training caveats

**Topic 3 — Stability and Dynamics**

- Gradient clipping
- Loss-curve shapes and what they imply
- Instabilities and recovery

</details>

**Important concepts**

- *Commands / APIs / Code:* `torch.optim.AdamW`, `OneCycleLR`, gradient accumulation loop
- *Mechanisms & failure scenarios:* Loss spikes from too-high learning rate at start, accumulation bugs scaling gradients wrongly, schedules not stepped.

### S05E06 — Regularization in Deep Learning: Dropout, Weight Decay, Augmentation, and Early Stopping

**Depth:** Intermediate  
**Learning objective:** Control overfitting in high-capacity networks with several complementary techniques.  
**Prerequisites:** S05E05, S03E12  
**Expected outcome:** Combine regularizers appropriately and verify improvement on a clean validation set.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Explicit Regularizers**

- Dropout mechanics and train/eval behavior
- L2 weight decay
- Stochastic depth and noise injection

**Topic 2 — Data-Side Regularization**

- Augmentation for images, text and tabular data
- Mixup and cutmix ideas

**Topic 3 — Stopping, Selection, and Generalization**

- Early stopping and checkpoint selection
- Validation protocol for deep models
- Double descent and why bigger models can generalize
- Memorization of noisy labels

</details>

**Important concepts**

- *Commands / APIs / Code:* `nn.Dropout`, `torchvision.transforms`, early-stopping callback
- *Mechanisms & failure scenarios:* Dropout left on at inference, augmentation leaking into validation, early stopping on a noisy metric.

### S05E07 — The PyTorch Training Loop: Tensors, Autograd, DataLoader, and Devices

**Depth:** Intermediate  
**Learning objective:** Understand every line of a standard training loop and what it costs.  
**Prerequisites:** S05E05, S01E03  
**Expected outcome:** Write and explain a complete training and evaluation loop and find an input-pipeline bottleneck.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Tensors and Modules**

- Tensors, dtypes and devices
- `nn.Module`, parameters and state dict

**Topic 2 — Data Loading**

- `Dataset` and `DataLoader` (workers, batching, collation)
- Shuffling and sampling

**Topic 3 — The Training Loop**

- Forward, loss, backward, step, `zero_grad`
- Train vs eval modes and `no_grad`
- Metrics logging

**Topic 4 — Moving to the GPU**

- Host-device transfer costs
- Pinned memory and asynchronous copy

**Topic 5 — Checkpoints and Reproducibility**

- Saving and restoring model, optimizer and RNG state
- Seeding and determinism limits

</details>

**Important concepts**

- *Commands / APIs / Code:* `model.to('cuda')`, `DataLoader(num_workers=…)`, `torch.save(state_dict)`
- *Mechanisms & failure scenarios:* Forgetting `model.eval()`, GPU idle waiting on data loading, loading a checkpoint on the wrong device.

### S05E08 — Debugging Training: Loss Curves, Overfitting a Batch, NaNs, and Mixed Precision

**Depth:** Advanced  
**Learning objective:** Systematically find why a network is not learning.  
**Prerequisites:** S05E07, S02E18  
**Expected outcome:** Apply a repeatable debugging procedure to a non-learning model.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — A Debugging Checklist**

- Overfit one small batch first
- Verify data, labels, shapes and augmentation visually
- Sanity-check the initial loss

**Topic 2 — Symptoms and Causes**

- Loss not decreasing, NaN/inf, accuracy at chance
- Train/validation divergence

**Topic 3 — Inspecting Internals**

- Gradient and activation statistics
- Hooks for layer-level inspection

**Topic 4 — Precision**

- Mixed precision (FP16/BF16) and loss scaling
- Overflow in half-precision softmax

**Topic 5 — Performance and Flakiness**

- Profiling a training step
- Nondeterminism and flaky results

</details>

**Important concepts**

- *Commands / APIs / Code:* `torch.autocast`, `GradScaler`, `torch.autograd.set_detect_anomaly`, `torch.profiler`
- *Mechanisms & failure scenarios:* Label shuffling bugs, softmax overflow in FP16, hidden data leakage producing suspiciously good results.

<a id="s05-module-3"></a>

## Module 3 — Computer Vision

**3 episodes (S05E09–S05E11) · 13 topics.** This module covers: Convolutional Neural Networks; CNN Architectures and Transfer Learning; Object Detection and Segmentation.

| ID | Episode | Depth |
|---|---|---|
| S05E09 | Convolutional Neural Networks: Convolution, Pooling, and Receptive Fields | Intermediate |
| S05E10 | CNN Architectures and Transfer Learning | Intermediate |
| S05E11 | Object Detection and Segmentation: IoU, NMS, and YOLO-Style Pipelines | Advanced |

### S05E09 — Convolutional Neural Networks: Convolution, Pooling, and Receptive Fields

**Depth:** Intermediate  
**Learning objective:** Explain how convolution exploits image structure and how features build hierarchically.  
**Prerequisites:** S05E01, S02E03  
**Expected outcome:** Compute convolution shapes and describe how a CNN builds features.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Convolution**

- Kernels, stride, padding and channels
- Weight sharing and translation equivariance
- Output-size arithmetic

**Topic 2 — Building a CNN**

- Pooling and downsampling
- Receptive fields and feature hierarchy
- Parameter count vs fully connected layers

**Topic 3 — What CNNs Learn**

- Edges → textures → parts → objects
- Feature maps and saliency (overview)

**Topic 4 — Limits and Efficiency**

- Texture bias and shift sensitivity
- Depthwise and dilated convolutions at overview level

</details>

**Important concepts**

- *Commands / APIs / Code:* `nn.Conv2d`, `nn.MaxPool2d`, feature-map visualization
- *Mechanisms & failure scenarios:* Off-by-one size mismatches, overfitting on small image sets, reliance on background shortcuts.

### S05E10 — CNN Architectures and Transfer Learning

**Depth:** Intermediate  
**Learning objective:** Understand landmark architectures and reuse pretrained models effectively.  
**Prerequisites:** S05E09  
**Expected outcome:** Choose a pretrained backbone and fine-tuning strategy for a small dataset.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Architecture Evolution**

- Deeper networks and the degradation problem
- Residual connections (ResNet)
- Efficient designs (depthwise separable, compound scaling)

**Topic 2 — Transfer Learning**

- Feature extraction vs fine-tuning
- Learning rates for pretrained vs new layers
- Domain similarity and dataset size

**Topic 3 — Practical Concerns**

- Preprocessing must match pretraining
- Class imbalance and evaluation in vision

**Topic 4 — Choosing a Backbone**

- Accuracy-latency trade-offs
- Inference cost and deployment targets

</details>

**Important concepts**

- *Commands / APIs / Code:* `torchvision.models`, freezing layers with `requires_grad_(False)`, `timm` (concept)
- *Mechanisms & failure scenarios:* Wrong normalization constants, fine-tuning destroying pretrained features with a high learning rate, catastrophic domain gap.

### S05E11 — Object Detection and Segmentation: IoU, NMS, and YOLO-Style Pipelines

**Depth:** Advanced  
**Learning objective:** Understand how models localize and delineate objects, and how their quality is measured.  
**Prerequisites:** S05E10  
**Expected outcome:** Explain a detection pipeline end to end and interpret mAP.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Detection Concepts**

- Bounding boxes, anchors vs anchor-free
- IoU and non-maximum suppression

**Topic 2 — Detector Families**

- Two-stage vs one-stage detectors
- Feature pyramids and multi-scale detection

**Topic 3 — Segmentation**

- Semantic vs instance segmentation
- Encoder-decoder (U-Net) idea and mask losses

**Topic 4 — Evaluation**

- mAP and its variants
- Small-object and class-imbalance failure cases

**Topic 5 — Deployment and Data**

- Real-time constraints and model size
- Data labeling cost for detection

</details>

**Important concepts**

- *Commands / APIs / Code:* `torchvision.ops.nms`, IoU calculation, Ultralytics-style inference (concept)
- *Mechanisms & failure scenarios:* Duplicate boxes from poor NMS thresholds, small-object misses, label noise in bounding boxes.

<a id="s05-module-4"></a>

## Module 4 — Sequences and Representation

**2 episodes (S05E12–S05E13) · 7 topics.** This module covers: Recurrent Networks; Embeddings and Representation Learning.

| ID | Episode | Depth |
|---|---|---|
| S05E12 | Recurrent Networks: RNNs, LSTMs, GRUs, and Why They Struggled | Intermediate |
| S05E13 | Embeddings and Representation Learning | Intermediate |

### S05E12 — Recurrent Networks: RNNs, LSTMs, GRUs, and Why They Struggled

**Depth:** Intermediate  
**Learning objective:** Understand sequence modeling before attention, and the limitations that motivated transformers.  
**Prerequisites:** S05E02  
**Expected outcome:** Explain how an LSTM carries information and why attention replaced it for most language work.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Recurrent Computation and Gating**

- Hidden state passed through time
- Backpropagation through time
- LSTM and GRU gating
- Bidirectional and stacked variants

**Topic 2 — Sequence-to-Sequence**

- Encoder-decoder with teacher forcing
- Exposure bias and beam search

**Topic 3 — Limits**

- Sequential computation prevents parallelism
- Fixed-size state bottleneck
- Transition to attention (Season 6)

</details>

**Important concepts**

- *Commands / APIs / Code:* `nn.LSTM`, packed sequences, gradient clipping
- *Mechanisms & failure scenarios:* Exploding gradients through time, padding handled incorrectly, forgetting early tokens on long inputs.

### S05E13 — Embeddings and Representation Learning

**Depth:** Intermediate  
**Learning objective:** Understand how networks learn dense vector representations and why embeddings are central to modern AI.  
**Prerequisites:** S05E01, S02E01  
**Expected outcome:** Explain how embeddings are learned, compared and evaluated.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Learned Embeddings**

- Embedding tables as learned lookups
- Word2vec-style objectives (skip-gram, negative sampling)
- Categorical-feature embeddings

**Topic 2 — Geometry of Embedding Spaces**

- Similarity and analogy structure
- Dimensionality and compression

**Topic 3 — Static vs Contextual Embeddings**

- Polysemy and why context matters
- From word vectors to contextual models

**Topic 4 — Using and Evaluating Embeddings**

- Nearest-neighbor search and clustering
- Probing and downstream evaluation
- Biases captured in embeddings

</details>

**Important concepts**

- *Commands / APIs / Code:* `nn.Embedding`, cosine nearest neighbors, embedding visualization
- *Mechanisms & failure scenarios:* Out-of-vocabulary items, embeddings encoding social bias, similarity thresholds not transferable across models.

<a id="s05-module-5"></a>

## Module 5 — Applied Vision: Video and Documents

**2 episodes (S05E14–S05E15) · 11 topics.** This module covers: Video Understanding and Object Tracking; OCR and Document Intelligence.

| ID | Episode | Depth |
|---|---|---|
| S05E14 | Video Understanding and Object Tracking | Advanced |
| S05E15 | OCR and Document Intelligence | Intermediate |

### S05E14 — Video Understanding and Object Tracking

**Depth:** Advanced  
**Learning objective:** Understand how models add the time dimension to vision: motion, action recognition and tracking objects across frames.  
**Prerequisites:** S05E10, S05E11, S05E12  
**Expected outcome:** Explain how video models represent time and design a detect-then-track pipeline with sensible evaluation.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — Video as Data**

- Frames, frame rate, clips and temporal sampling
- Memory and compute cost of video

**Topic 2 — Motion Representations**

- Optical flow and frame differencing
- Two-stream networks

**Topic 3 — Spatiotemporal Models**

- 3D convolutions and factorized (2+1)D designs
- Temporal pooling and recurrent aggregation
- Video transformers as a preview (Season 6)

**Topic 4 — Action Recognition**

- Clip sampling, labels and temporal localization
- Evaluation for classification and localization

**Topic 5 — Object Tracking**

- Tracking-by-detection and data association
- Kalman filtering and the Hungarian algorithm (concept)
- Re-identification and occlusion handling

**Topic 6 — Production Considerations**

- Streaming inference and latency budgets
- Privacy and consent for video

</details>

**Important concepts**

- *Commands / APIs / Code:* `torchvision.io` video reading, optical-flow call (concept), IoU-based association in Python, Kalman-filter update step (illustrative)
- *Mechanisms & failure scenarios:* Identity switches after occlusion, frame-rate or sampling mismatch between training and serving, memory blow-up from long clips, motion blur degrading detection.

### S05E15 — OCR and Document Intelligence

**Depth:** Intermediate  
**Learning objective:** Understand how text is located and read in images and how page layout, tables and forms become structured data.  
**Prerequisites:** S05E11, S05E12, S05E13  
**Expected outcome:** Design a document-extraction pipeline, choose between OCR, layout models and vision-language models, and measure its accuracy.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The OCR Pipeline**

- Preprocessing: deskew, denoise, binarize
- Text detection vs text recognition

**Topic 2 — Text Detection**

- Segmentation-based and regression-based detectors
- Handling curved and rotated text

**Topic 3 — Text Recognition**

- CNN + recurrent sequence models with CTC loss
- Decoding and language-model rescoring
- Handwriting and rare scripts

**Topic 4 — Layout and Document Understanding**

- Reading order, columns and structure
- Tables, forms and key-value extraction
- Layout-aware and vision-language document models
- Managed document-analysis services and when to use them over self-hosted models

**Topic 5 — Evaluation and Failure Modes**

- Character and word error rates, field-level accuracy
- Confidence scores and human review loops
- Connection to RAG ingestion (Season 8)

</details>

**Important concepts**

- *Commands / APIs / Code:* OCR library call and bounding-box output (illustrative), CTC loss in PyTorch (concept), layout/table extraction output schema
- *Mechanisms & failure scenarios:* Skewed or low-resolution scans, multi-column reading-order errors, tables flattened into prose, handwriting and rare scripts, confidently wrong characters.

<a id="s05-module-6"></a>

## Module 6 — Audio and Speech

**2 episodes (S05E16–S05E17) · 11 topics.** This module covers: Audio and Speech Fundamentals; Speech Recognition and Speech Synthesis.

| ID | Episode | Depth |
|---|---|---|
| S05E16 | Audio and Speech Fundamentals: Signals, Spectrograms, and Features | Intermediate |
| S05E17 | Speech Recognition and Speech Synthesis: CTC, Encoder-Decoder ASR, TTS, and Vocoders | Advanced |

### S05E16 — Audio and Speech Fundamentals: Signals, Spectrograms, and Features

**Depth:** Intermediate  
**Learning objective:** Understand how sound becomes numbers and the representations models use for audio classification, detection and speech tasks.  
**Prerequisites:** S05E09, S05E12, S02E04  
**Expected outcome:** Convert raw audio into model-ready features and choose an architecture and evaluation setup for an audio task.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Sound as a Signal**

- Sampling, Nyquist limit, bit depth and channels
- Waveform, amplitude and frequency

**Topic 2 — From Waveform to Spectrogram**

- Fourier transform intuition and the short-time Fourier transform
- Window size, hop length and the time-frequency trade-off

**Topic 3 — Perceptual Features**

- Mel scale, log-mel spectrograms and MFCCs
- Why log compression helps

**Topic 4 — Models for Audio**

- CNNs on spectrograms
- Sequence models and raw-waveform models
- Pretrained audio embeddings

**Topic 5 — Audio Tasks and Data**

- Classification, event detection, voice-activity detection, diarization and source separation
- Augmentation, speaker-aware splits and dataset pitfalls

</details>

**Important concepts**

- *Commands / APIs / Code:* `librosa` or `torchaudio` loading, STFT and mel-spectrogram computation, SpecAugment-style masking (illustrative)
- *Mechanisms & failure scenarios:* Sample-rate mismatches, clipping and normalization errors, data leakage across speakers or recording sessions, train-test mismatch in feature extraction.

### S05E17 — Speech Recognition and Speech Synthesis: CTC, Encoder-Decoder ASR, TTS, and Vocoders

**Depth:** Advanced  
**Learning objective:** Explain how speech is transcribed and generated, the trade-offs of streaming systems, and how quality and risk are measured.  
**Prerequisites:** S05E16, S05E15, S05E12  
**Expected outcome:** Choose and evaluate an ASR or TTS approach for an application and describe its failure and misuse risks.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — The Speech Recognition Problem**

- Alignment between audio frames and text
- Word error rate and its limits

**Topic 2 — CTC and Hybrid Approaches**

- CTC loss and decoding
- Language-model fusion and vocabulary adaptation

**Topic 3 — Encoder-Decoder and Large-Scale ASR**

- Attention-based sequence-to-sequence ASR (attention detailed in Season 6)
- Multilingual, weakly supervised training and its failure modes

**Topic 4 — Streaming ASR**

- Chunked and causal models
- Endpointing, latency vs accuracy

**Topic 5 — Speech Synthesis**

- Text analysis, acoustic model and vocoder pipeline
- Neural vocoders and end-to-end TTS
- Prosody, speaker control and codec-based speech models (concept)

**Topic 6 — Evaluation, Safety, and Misuse**

- MOS and automatic quality metrics
- Voice cloning, consent and watermarking

</details>

**Important concepts**

- *Commands / APIs / Code:* Whisper-style transcription call (concept), WER computation, TTS synthesis call and vocoder stage (illustrative)
- *Mechanisms & failure scenarios:* Accents, noise and domain vocabulary raising word error rate, hallucinated transcripts on silence, streaming latency vs accuracy trade-offs, unauthorized voice cloning.

<a id="s05-module-7"></a>

## Module 7 — Generative Models

**4 episodes (S05E18–S05E21) · 14 topics.** This module covers: Autoencoders and Variational Autoencoders; Generative Adversarial Networks; Diffusion Models I; Diffusion Models II.

| ID | Episode | Depth |
|---|---|---|
| S05E18 | Autoencoders and Variational Autoencoders | Advanced |
| S05E19 | Generative Adversarial Networks | Intermediate |
| S05E20 | Diffusion Models I: Noising, Denoising, and the Training Objective | Advanced |
| S05E21 | Diffusion Models II: Sampling, Guidance, Latent Diffusion, and Conditioning | Advanced |

### S05E18 — Autoencoders and Variational Autoencoders

**Depth:** Advanced  
**Learning objective:** Understand compression, latent spaces and probabilistic generation through autoencoders.  
**Prerequisites:** S05E03, S02E17  
**Expected outcome:** Explain autoencoder and VAE training objectives and their trade-offs.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Autoencoders**

- Encoder, bottleneck and decoder
- Reconstruction loss
- Denoising and sparse variants

**Topic 2 — Variational Autoencoders and the ELBO**

- Latent distributions and the reparameterization trick
- Sampling and smooth latent spaces
- Reconstruction plus KL terms
- Where the objective comes from

**Topic 3 — Uses and Limits**

- Anomaly detection and representation learning
- Blurry reconstructions and posterior collapse

</details>

**Important concepts**

- *Commands / APIs / Code:* PyTorch VAE sketch, reparameterization snippet
- *Mechanisms & failure scenarios:* KL term overpowering reconstruction, blurry samples, using reconstruction error as anomaly score without calibration.

### S05E19 — Generative Adversarial Networks

**Depth:** Intermediate  
**Learning objective:** Understand adversarial training and why it is powerful but unstable.  
**Prerequisites:** S05E18, S05E09  
**Expected outcome:** Describe GAN training and diagnose its characteristic failures.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Adversarial Game**

- Generator and discriminator objectives
- Minimax training dynamics
- Nash equilibrium intuition

**Topic 2 — Training Challenges**

- Mode collapse and vanishing gradients
- Stabilization techniques (Wasserstein, spectral norm)

**Topic 3 — Evaluation**

- FID, precision/recall for generators and their limits
- FID and Inception-based metrics: what they capture
- Precision/recall for generators and human evaluation

**Topic 4 — Where GANs Fit Today**

- Strengths: fast sampling, sharp images
- Why diffusion largely displaced them
- Misuse and provenance concerns

</details>

**Important concepts**

- *Commands / APIs / Code:* GAN training-loop sketch with alternating updates
- *Mechanisms & failure scenarios:* Discriminator overpowering the generator, mode collapse, training oscillation.

### S05E20 — Diffusion Models I: Noising, Denoising, and the Training Objective

**Depth:** Advanced  
**Learning objective:** Explain how a diffusion model is trained to reverse a gradual noising process and what the network actually predicts.  
**Prerequisites:** S05E18, S05E10, S02E17  
**Expected outcome:** Derive the intuition behind noise-prediction training and describe the denoising network and schedule choices.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — The Core Idea and the Forward Process**

- Gradually destroying data with noise and learning to reverse it
- Connection to VAEs and score matching (concept)
- Noise schedules and closed-form noising at any step
- Signal-to-noise ratio view

**Topic 2 — The Training Objective**

- Predicting noise vs predicting the clean image vs velocity
- Why a simple mean-squared loss works
- Timestep sampling and weighting

**Topic 3 — The Denoising Network**

- U-Net backbone with timestep conditioning
- Attention layers and diffusion transformers (concept)

</details>

**Important concepts**

- *Commands / APIs / Code:* Forward-noising step and noise-prediction loss in PyTorch (illustrative), noise schedule plot
- *Mechanisms & failure scenarios:* Poorly chosen noise schedules, training instability at high noise levels, memorization of training images, mismatch between training and sampling schedules.

### S05E21 — Diffusion Models II: Sampling, Guidance, Latent Diffusion, and Conditioning

**Depth:** Advanced  
**Learning objective:** Explain how images are generated at inference time, how text steers generation, and why latent diffusion made it practical.  
**Prerequisites:** S05E20, S05E13  
**Expected outcome:** Trace text-to-image generation end to end and reason about step count, guidance and conditioning trade-offs.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Core Idea and the Forward Process**

- Ancestral (DDPM) sampling vs deterministic (DDIM) sampling
- Step count vs quality; fast samplers and distillation (concept)
- Classifier guidance and classifier-free guidance
- Guidance scale trade-off between fidelity and diversity

**Topic 2 — Latent Diffusion**

- Autoencoder compression and diffusion in latent space
- Compute and memory savings

**Topic 3 — Conditioning**

- Text conditioning with embeddings and cross-attention
- Image conditioning and control signals (concept)

**Topic 4 — Evaluation and Risk**

- Evaluating generative quality and prompt alignment
- Safety, provenance and watermarking at overview level

</details>

**Important concepts**

- *Commands / APIs / Code:* `diffusers` pipeline call with scheduler and guidance scale (concept), sampler step loop (illustrative)
- *Mechanisms & failure scenarios:* Prompt-adherence failures, artifacts from too few steps, over-saturation at high guidance, safety-filter bypass, latent-decoder artifacts.

<a id="s05-module-8"></a>

## Module 8 — Reinforcement Learning

**3 episodes (S05E22–S05E24) · 16 topics.** This module covers: Reinforcement Learning Foundations; Policy Gradients, Actor-Critic, and PPO; Deep RL in Practice.

| ID | Episode | Depth |
|---|---|---|
| S05E22 | Reinforcement Learning Foundations: MDPs, Value Functions, and Q-Learning | Intermediate |
| S05E23 | Policy Gradients, Actor-Critic, and PPO | Advanced |
| S05E24 | Deep RL in Practice: DQN, Reward Design, Simulation, and Offline RL | Advanced |

### S05E22 — Reinforcement Learning Foundations: MDPs, Value Functions, and Q-Learning

**Depth:** Intermediate  
**Learning objective:** Understand how an agent learns to act from rewards: the formal problem, value functions, and the basic learning algorithms.  
**Prerequisites:** S02E11, S02E12, S02E07  
**Expected outcome:** Formalize a decision problem as an MDP and explain how Q-learning improves a policy from experience.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Reinforcement Learning Problem**

- Agent, environment, state, action and reward
- Trajectories, returns and discounting
- How RL differs from supervised learning

**Topic 2 — Markov Decision Processes**

- Transition dynamics and the Markov property
- Policies and optimality

**Topic 3 — Value Functions, Bellman Equations, and Planning**

- State-value and action-value functions
- Bellman expectation and optimality equations
- Policy evaluation, policy iteration and value iteration

**Topic 4 — Learning from Experience**

- Monte Carlo and temporal-difference learning
- Q-learning vs SARSA (off-policy vs on-policy)

**Topic 5 — Exploration vs Exploitation**

- Epsilon-greedy and optimism
- Why exploration is hard and where RL is (and is not) the right tool

</details>

**Important concepts**

- *Commands / APIs / Code:* Gym-style environment loop, tabular Q-learning update, epsilon-greedy policy (illustrative)
- *Mechanisms & failure scenarios:* Sparse rewards giving no learning signal, unstable bootstrapping, reward functions that encourage unintended behavior, exploration collapse.

### S05E23 — Policy Gradients, Actor-Critic, and PPO

**Depth:** Advanced  
**Learning objective:** Understand how policies are optimized directly, why variance matters, and how PPO stabilizes learning (the algorithm behind RLHF-style training).  
**Prerequisites:** S05E22, S02E06, S05E02  
**Expected outcome:** Derive the policy-gradient idea, explain advantage and clipping, and relate PPO to its use in language-model training.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — Why Optimize the Policy Directly**

- Parameterized stochastic policies
- Continuous and large action spaces

**Topic 2 — The Policy Gradient**

- The log-derivative trick and the policy-gradient theorem
- REINFORCE

**Topic 3 — Variance Reduction**

- Baselines and advantages
- Reward-to-go

**Topic 4 — Actor-Critic Methods**

- Learned value functions as critics
- Generalized advantage estimation

**Topic 5 — Trust Regions and PPO**

- Why large policy updates are dangerous
- PPO clipped objective and KL control

**Topic 6 — Connection to Language Models**

- Policy, reward model and KL penalty in RLHF (Season 6)
- Verifiable rewards for reasoning (concept)

</details>

**Important concepts**

- *Commands / APIs / Code:* REINFORCE loop, advantage estimation, PPO clipped objective (illustrative PyTorch)
- *Mechanisms & failure scenarios:* High-variance gradients, destructive policy updates, value-function errors misleading the actor, reward hacking, sensitivity to hyperparameters.

### S05E24 — Deep RL in Practice: DQN, Reward Design, Simulation, and Offline RL

**Depth:** Advanced  
**Learning objective:** Understand how neural networks scale RL to hard problems and what makes RL projects succeed or fail in practice.  
**Prerequisites:** S05E23, S05E07, S05E08  
**Expected outcome:** Decide when RL is appropriate, design rewards and simulators responsibly, and evaluate RL results with statistical care.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Deep Q-Networks**

- Function approximation and the deadly triad
- Experience replay and target networks

**Topic 2 — Continuous Control**

- Actor-critic variants for continuous actions (DDPG, SAC at concept level)
- Entropy regularization

**Topic 3 — Reward Design**

- Reward shaping and its dangers
- Reward hacking and specification gaming

**Topic 4 — Simulation and Sim-to-Real**

- Simulators as training environments
- Domain randomization and transfer gaps

**Topic 5 — Offline RL and Evaluation**

- Learning from logged data and distribution shift
- Off-policy evaluation (link to Season 4 causal ML)
- Reproducibility: seeds, variance and honest reporting

</details>

**Important concepts**

- *Commands / APIs / Code:* DQN replay buffer and target network update, environment wrapper with reward shaping, evaluation rollouts across seeds (illustrative)
- *Mechanisms & failure scenarios:* Reward hacking, instability from bootstrapping with function approximation, results that do not replicate across seeds, simulator-to-real gaps, off-policy evaluation with poor coverage.

<a id="s05-module-9"></a>

## Module 9 — Representation Learning and Training at Scale

**4 episodes (S05E25–S05E28) · 14 topics.** This module covers: Self-Supervised and Contrastive Learning; Efficient Training; Data Pipelines for Deep Learning; Deep Learning Project Workflow.

| ID | Episode | Depth |
|---|---|---|
| S05E25 | Self-Supervised and Contrastive Learning | Advanced |
| S05E26 | Efficient Training: GPU Memory, Checkpointing, and Data Parallelism | Advanced |
| S05E27 | Data Pipelines for Deep Learning: Datasets, Augmentation, and Throughput | Intermediate |
| S05E28 | Deep Learning Project Workflow: Baselines, Evaluation, and Reproducibility | Intermediate |

### S05E25 — Self-Supervised and Contrastive Learning

**Depth:** Advanced  
**Learning objective:** Understand how models learn from unlabeled data, the idea that powers foundation models.  
**Prerequisites:** S05E13, S05E10  
**Expected outcome:** Explain contrastive and masked objectives and why pretraining transfers.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Self-Supervision**

- Pretext tasks and the pretrain-then-fine-tune paradigm
- Label efficiency

**Topic 2 — Contrastive and Masked Objectives**

- Positive and negative pairs
- InfoNCE loss and temperature
- Masked modeling and reconstruction
- Joint-embedding predictive ideas (concept)

**Topic 3 — Foundation-Model Connection**

- CLIP-style image-text alignment
- Why scale plus self-supervision works
- Failure: shortcut learning, collapsed representations, false negatives

</details>

**Important concepts**

- *Commands / APIs / Code:* contrastive loss implementation sketch, CLIP embedding use (concept)
- *Mechanisms & failure scenarios:* Collapsed representations, false negatives in batches, augmentations destroying the signal.

### S05E26 — Efficient Training: GPU Memory, Checkpointing, and Data Parallelism

**Depth:** Advanced  
**Learning objective:** Understand where GPU memory and time go during training and the first scaling techniques.  
**Prerequisites:** S05E07, S05E08  
**Expected outcome:** Estimate training memory and choose first-line techniques to fit a model on hardware.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Memory Accounting**

- Parameters, gradients, optimizer states and activations
- Why activations dominate for large batches

**Topic 2 — Reducing Memory**

- Gradient checkpointing trade-off
- Mixed precision and 8-bit optimizers (concept)

**Topic 3 — Throughput**

- Fused kernels and compilation
- Data-loading and I/O overlap
- Profiling utilization

**Topic 4 — Multi-GPU Basics**

- Data parallelism and gradient all-reduce
- Effective batch size
- Preview of model/pipeline parallelism (Season 13)

</details>

**Important concepts**

- *Commands / APIs / Code:* `DistributedDataParallel` (concept), `torch.cuda.memory_summary()`, `nvidia-smi`
- *Mechanisms & failure scenarios:* CUDA out-of-memory from activations, stragglers in data-parallel runs, gradient mismatch from different seeds.

### S05E27 — Data Pipelines for Deep Learning: Datasets, Augmentation, and Throughput

**Depth:** Intermediate  
**Learning objective:** Keep accelerators busy and training data correct.  
**Prerequisites:** S05E07, S01E11  
**Expected outcome:** Design and measure an input pipeline that does not bottleneck training.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Dataset Design**

- Map-style vs iterable datasets
- Sharded formats for large corpora
- Deterministic shuffling and resumability

**Topic 2 — Augmentation and Preprocessing Pipelines**

- CPU vs GPU augmentation
- Caching and on-the-fly transforms
- Preventing train/validation contamination

**Topic 3 — Measuring the Pipeline**

- Data-loader bottleneck detection
- Prefetching and worker tuning
- Data validation before training

</details>

**Important concepts**

- *Commands / APIs / Code:* `DataLoader` params, WebDataset-style sharding (concept), profiler timeline
- *Mechanisms & failure scenarios:* Starved GPUs, nondeterministic shuffles across restarts, corrupted samples crashing long runs.

### S05E28 — Deep Learning Project Workflow: Baselines, Evaluation, and Reproducibility

**Depth:** Intermediate  
**Learning objective:** Run a deep-learning project with the same discipline as classical ML, adapted to expensive experiments.  
**Prerequisites:** S05E08, S05E06, S04E16  
**Expected outcome:** Plan and document a deep-learning experiment so results can be trusted and reproduced.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Starting Right**

- Baselines (classical and pretrained)
- Small-scale prototypes before big runs
- Experiment plan and budget

**Topic 2 — Evaluation**

- Per-class and per-slice analysis
- Robustness and distribution-shift checks

**Topic 3 — Statistical Noise**

- Variance across seeds
- Confidence in small improvements

**Topic 4 — Reproducibility and Hand-Off**

- Seeds, versions, configs and checkpoints
- Model cards and documentation
- Bridge to Season 6 (transformers) and Season 11 (MLOps)

</details>

**Important concepts**

- *Commands / APIs / Code:* config-driven training script, checkpoint metadata, seed utilities
- *Mechanisms & failure scenarios:* Irreproducible results from nondeterministic ops, one lucky seed reported as truth, evaluation set overlap with pretraining data.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s05-module-1) | Starting point of the season |
| [Module 2](#s05-module-2) | [Module 1](#s05-module-1) (S05E02) |
| [Module 3](#s05-module-3) | [Module 1](#s05-module-1) (S05E01) |
| [Module 4](#s05-module-4) | [Module 1](#s05-module-1) (S05E01, S05E02) |
| [Module 5](#s05-module-5) | [Module 3](#s05-module-3) (S05E10, S05E11); [Module 4](#s05-module-4) (S05E12, S05E13) |
| [Module 6](#s05-module-6) | [Module 3](#s05-module-3) (S05E09); [Module 4](#s05-module-4) (S05E12); [Module 5](#s05-module-5) (S05E15) |
| [Module 7](#s05-module-7) | [Module 1](#s05-module-1) (S05E03); [Module 3](#s05-module-3) (S05E09, S05E10); [Module 4](#s05-module-4) (S05E13) |
| [Module 8](#s05-module-8) | [Module 1](#s05-module-1) (S05E02); [Module 2](#s05-module-2) (S05E07, S05E08) |
| [Module 9](#s05-module-9) | [Module 2](#s05-module-2) (S05E06, S05E07, S05E08); [Module 3](#s05-module-3) (S05E10); [Module 4](#s05-module-4) (S05E13) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 4 — Advanced Machine Learning Engineering](../season-04-advanced-ml-engineering/roadmap.md)
- **Next:** [Season 6 — LLMs & Transformer Architecture](../season-06-llms-and-transformers/roadmap.md)
- **Draws on:** [Season 1](../season-01-python-for-ai-ml/roadmap.md) (S01E03, S01E11); [Season 2](../season-02-mathematics-for-ai/roadmap.md) (S02E01, S02E02, S02E03, S02E04, S02E06, S02E07, S02E08, S02E09, S02E11, S02E12, S02E13, S02E17, S02E18); [Season 3](../season-03-machine-learning/roadmap.md) (S03E05, S03E12); [Season 4](../season-04-advanced-ml-engineering/roadmap.md) (S04E16)
- **Required by:** [Season 6](../season-06-llms-and-transformers/roadmap.md) (via S05E04, S05E10, S05E12, S05E13, S05E23, S05E25, S05E26); [Season 7](../season-07-generative-ai-engineering/roadmap.md) (via S05E14, S05E17, S05E21); [Season 8](../season-08-rag-engineering/roadmap.md) (via S05E13, S05E15, S05E25); [Season 10](../season-10-advanced-agentic-ai/roadmap.md) (via S05E23); [Season 11](../season-11-mlops-engineering/roadmap.md) (via S05E10); [Season 13](../season-13-ai-infrastructure/roadmap.md) (via S05E26, S05E27); [Season 14](../season-14-production-ai-systems/roadmap.md) (via S05E08)
