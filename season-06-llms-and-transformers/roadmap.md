# Season 6 Roadmap — LLMs & Transformer Architecture

[← Season 6 overview](README.md) · [All seasons](../README.md)

**4 modules · 24 episodes · 101 topics · 257 subtopics · Level: Intermediate → Advanced**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Transformer Architecture](#s06-module-1)
- [Module 2 — Training and Adapting LLMs](#s06-module-2)
- [Module 3 — Inference and Efficiency](#s06-module-3)
- [Module 4 — Model Behavior and Selection](#s06-module-4)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Make large language models legible: what a transformer computes, how models are pretrained, aligned and fine-tuned, how inference really works (prefill, decode, KV cache), and how to reason about model behavior, limits and selection. It is the conceptual foundation for Seasons 7–12.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S06E01 | Understand the language-modeling objective and the specific limitations that attention solves. |
| S06E02 | Understand how text becomes integer IDs and how tokenizer behavior affects cost, quality and bugs. |
| S06E03 | Understand how a transformer knows token identity and order. |
| S06E04 | Compute scaled dot-product attention step by step and interpret what it does. |
| S06E05 | Understand why attention is split across heads and how masking controls information flow. |
| S06E06 | Assemble a complete block and understand each component's role in trainability and capacity. |
| S06E07 | Match transformer family to task and understand why decoder-only models dominate today's LLMs. |
| S06E08 | Understand how the transformer was adapted to images and how vision backbones are chosen and pretrained today. |
| S06E09 | Understand how base models are trained and what pretraining does and doesn't provide. |
| S06E10 | Understand, at concept level, how models too big for one GPU are trained. |
| S06E11 | Understand how a base model becomes an assistant that follows instructions. |
| S06E12 | Understand how human preferences shape model behavior and the trade-offs among methods. |
| S06E13 | Fine-tune large models with small trainable adapters and understand the memory arithmetic. |
| S06E14 | Trace exactly what happens between a prompt and the generated tokens. |
| S06E15 | Understand the main memory cost of serving LLMs and why long contexts are expensive. |
| S06E16 | Control generation behavior by manipulating the next-token distribution. |
| S06E17 | Shrink and speed up models and understand what quality is lost. |
| S06E18 | Understand the engineering changes that make attention faster and cheaper, and how context windows are extended. |
| S06E19 | Understand sparse expert models and state-space and hybrid architectures, and what they change for training and serving. |
| S06E20 | Understand how models "think" with extra tokens and when that is worth the cost. |
| S06E21 | Understand why LLMs produce confident falsehoods and which mitigations actually work. |
| S06E22 | Read benchmark claims critically and design task-specific evaluations. |
| S06E23 | Select a model deployment option using capability, cost, latency, privacy and operational burden. |
| S06E24 | Understand how images and audio are turned into tokens a language model can use. |

## Prerequisites and Expected Knowledge

- **Season 2 — [Mathematics for AI & Machine Learning](../season-02-mathematics-for-ai/roadmap.md)**: S02E03, S02E04, S02E10, S02E14, S02E17, S02E18
- **Season 4 — [Advanced Machine Learning Engineering](../season-04-advanced-ml-engineering/roadmap.md)**: S04E02, S04E13
- **Season 5 — [Deep Learning & Neural Networks](../season-05-deep-learning/roadmap.md)**: S05E04, S05E10, S05E12, S05E13, S05E23, S05E25, S05E26

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Transformer Architecture](#s06-module-1) | S06E01–S06E08 | 8 | 7 Intermediate, 1 Advanced |
| 2 | [Training and Adapting LLMs](#s06-module-2) | S06E09–S06E13 | 5 | 3 Intermediate, 2 Advanced |
| 3 | [Inference and Efficiency](#s06-module-3) | S06E14–S06E19 | 6 | 4 Intermediate, 2 Advanced |
| 4 | [Model Behavior and Selection](#s06-module-4) | S06E20–S06E24 | 5 | 5 Intermediate |

<a id="s06-module-1"></a>

## Module 1 — Transformer Architecture

**8 episodes (S06E01–S06E08) · 34 topics.** This module covers: Language Modeling and Why Attention Replaced Recurrence; Tokenization; Embeddings and Positional Information; Attention; Multi-Head Attention and Masks; The Transformer Block; Encoder, Decoder, and Encoder-Decoder Models; Vision Transformers and Modern Vision Backbones.

| ID | Episode | Depth |
|---|---|---|
| S06E01 | Language Modeling and Why Attention Replaced Recurrence | Intermediate |
| S06E02 | Tokenization: BPE, Vocabularies, and Special Tokens | Intermediate |
| S06E03 | Embeddings and Positional Information: Absolute, Relative, and Rotary | Advanced |
| S06E04 | Attention: Queries, Keys, Values, and Context Mixing | Intermediate |
| S06E05 | Multi-Head Attention and Masks | Intermediate |
| S06E06 | The Transformer Block: Residuals, Normalization, and Feed-Forward Layers | Intermediate |
| S06E07 | Encoder, Decoder, and Encoder-Decoder Models: BERT, GPT, and T5 | Intermediate |
| S06E08 | Vision Transformers and Modern Vision Backbones | Intermediate |

### S06E01 — Language Modeling and Why Attention Replaced Recurrence

**Depth:** Intermediate  
**Learning objective:** Understand the language-modeling objective and the specific limitations that attention solves.  
**Prerequisites:** S05E12, S02E17  
**Expected outcome:** State what a language model predicts and why attention became the dominant mechanism.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Language Modeling**

- Next-token probability and the chain rule of language
- Perplexity as a measure

**Topic 2 — From n-grams to Neural Language Models**

- Count-based models and sparsity
- Neural LMs with learned embeddings

**Topic 3 — The Bottleneck Before Attention**

- Fixed-size hidden state and sequential computation
- Long-range dependency problems
- Encoder-decoder with attention as the bridge

**Topic 4 — The Transformer Idea**

- Direct connections between all positions
- Parallelism across the sequence
- Cost: attention scales with sequence length squared

</details>

**Important concepts**

- *Commands / APIs / Code:* n-gram counting sketch, perplexity computation
- *Mechanisms & failure scenarios:* Sparse n-gram counts, recurrent models forgetting distant context, quadratic attention cost on long inputs.

### S06E02 — Tokenization: BPE, Vocabularies, and Special Tokens

**Depth:** Intermediate  
**Learning objective:** Understand how text becomes integer IDs and how tokenizer behavior affects cost, quality and bugs.  
**Prerequisites:** S04E13  
**Expected outcome:** Predict how a string tokenizes, estimate cost, and explain tokenizer-related failures.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Why Subwords**

- Word-level, character-level and byte-level trade-offs
- Out-of-vocabulary problems

**Topic 2 — Byte-Pair Encoding**

- The merge algorithm worked step by step
- Byte-level BPE and related methods

**Topic 3 — Vocabulary and Special Tokens**

- Vocabulary size trade-offs
- BOS/EOS, padding, role and tool markers

**Topic 4 — Chat Templates**

- How conversations become token sequences
- Template mismatch as a silent failure

**Topic 5 — Consequences**

- Token counts, context limits and pricing
- Multilingual, code and number handling
- "Glitch" tokens and tokenizer mismatches

</details>

**Important concepts**

- *Commands / APIs / Code:* `AutoTokenizer.from_pretrained`, `tokenizer.encode/decode`, token counting with `tiktoken` (concept)
- *Mechanisms & failure scenarios:* Using the wrong tokenizer for a model, truncation cutting mid-structure, poor performance on rare scripts.

### S06E03 — Embeddings and Positional Information: Absolute, Relative, and Rotary

**Depth:** Advanced  
**Learning objective:** Understand how a transformer knows token identity and order.  
**Prerequisites:** S06E02, S05E13  
**Expected outcome:** Explain how order enters a transformer and why context extension is nontrivial.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Token Embeddings**

- Embedding matrix and weight tying
- Dimension and what it stores

**Topic 2 — Why Position Must Be Injected**

- Attention alone is order-blind
- Permutation equivariance

**Topic 3 — Position Encoding Methods**

- Sinusoidal and learned absolute positions
- Relative encodings and ALiBi
- Rotary embeddings (RoPE): rotating query/key pairs

**Topic 4 — Context Length Implications**

- Extrapolation beyond training length
- Position interpolation and scaling tricks (concept)
- Long-context quality degradation

</details>

**Important concepts**

- *Commands / APIs / Code:* embedding lookup, sinusoidal position code, RoPE rotation illustration
- *Mechanisms & failure scenarios:* Models failing beyond trained context length, position bias ("lost in the middle"), mis-scaled rotary parameters.

### S06E04 — Attention: Queries, Keys, Values, and Context Mixing

**Depth:** Intermediate  
**Learning objective:** Compute scaled dot-product attention step by step and interpret what it does.  
**Prerequisites:** S06E03, S02E03  
**Expected outcome:** Implement attention from scratch and explain its cost.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Attention as Soft Lookup**

- Query, key and value intuition
- Content-based retrieval inside a network

**Topic 2 — The Computation**

- Linear projections to Q, K, V
- Scores, softmax and weighted sum
- Why scale by √d

**Topic 3 — Masks and Generation**

- Causal masks and information leakage
- Causal masks and information leakage during training
- Why masking lets the whole sequence train in parallel
- Padding masks vs causal masks

**Topic 4 — Interpretation**

- What attention weights do and do not explain
- Attention maps are not explanations
- Head specialization examples and caveats

**Topic 5 — Cost**

- Compute and memory scaling with sequence length
- Matrix form and batching
- Why this motivates efficient variants

</details>

**Important concepts**

- *Commands / APIs / Code:* `softmax(QK^T/√d)V` in PyTorch, `scaled_dot_product_attention`
- *Mechanisms & failure scenarios:* Forgetting the causal mask (information leakage), softmax saturation without scaling, overinterpreting attention maps.

### S06E05 — Multi-Head Attention and Masks

**Depth:** Intermediate  
**Learning objective:** Understand why attention is split across heads and how masking controls information flow.  
**Prerequisites:** S06E04  
**Expected outcome:** Implement multi-head attention and reason about each mask type.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Multiple Heads**

- Subspaces and parallel attention patterns
- Concatenation and output projection
- Head specialization (and its limits)

**Topic 2 — Masks**

- Padding masks, causal masks and bidirectional attention
- Attention biases

**Topic 3 — Cross-Attention and Implementation**

- Encoder-decoder interaction
- Use in multimodal and diffusion models
- Tensor shapes through multi-head attention
- Common implementation bugs

</details>

**Important concepts**

- *Commands / APIs / Code:* `nn.MultiheadAttention`, shape-annotated implementation
- *Mechanisms & failure scenarios:* Wrong head reshape producing silent errors, padding tokens attended to, mask dtype issues.

### S06E06 — The Transformer Block: Residuals, Normalization, and Feed-Forward Layers

**Depth:** Intermediate  
**Learning objective:** Assemble a complete block and understand each component's role in trainability and capacity.  
**Prerequisites:** S06E05, S05E04  
**Expected outcome:** Compute parameters and FLOPs of a transformer from its configuration.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Block Anatomy**

- Attention sublayer and feed-forward sublayer
- Residual connections and the residual-stream view

**Topic 2 — Normalization Placement**

- Pre-norm vs post-norm and training stability
- RMSNorm

**Topic 3 — Feed-Forward Networks**

- Expansion and projection; gated variants (SwiGLU)
- Where most parameters live

**Topic 4 — Stacking Blocks**

- Depth, width and parameter counts
- Computing FLOPs per token

**Topic 5 — Stability and Outliers**

- Activation outliers and their effect on quantization
- Training stability considerations

</details>

**Important concepts**

- *Commands / APIs / Code:* parameter-count calculation, block implementation sketch
- *Mechanisms & failure scenarios:* Post-norm instability at depth, activation outliers harming quantization, miscounted parameters.

### S06E07 — Encoder, Decoder, and Encoder-Decoder Models: BERT, GPT, and T5

**Depth:** Intermediate  
**Learning objective:** Match transformer family to task and understand why decoder-only models dominate today's LLMs.  
**Prerequisites:** S06E06  
**Expected outcome:** Choose the right architecture family for a task and explain the trade-offs.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Three Architectures**

- Encoder-only (BERT-style), decoder-only (GPT-style), encoder-decoder (T5-style)
- Masking and objective differences

**Topic 2 — Why Decoder-Only Won for LLMs**

- Unified generation interface
- Scaling behavior and in-context learning

**Topic 3 — Using and Choosing Each Family**

- Encoders for embeddings, classification and reranking
- Decoder-only for chat and generation
- Cost, latency and quality trade-offs for an application
- Worked examples: a classifier, a retriever and a chat assistant
- Fine-tuning vs prompting by architecture

</details>

**Important concepts**

- *Commands / APIs / Code:* Hugging Face `AutoModelFor*` classes, pipeline task names
- *Mechanisms & failure scenarios:* Using a generative model where a small encoder would be cheaper and better, misusing mask types.

### S06E08 — Vision Transformers and Modern Vision Backbones

**Depth:** Intermediate  
**Learning objective:** Understand how the transformer was adapted to images and how vision backbones are chosen and pretrained today.  
**Prerequisites:** S06E06, S06E07, S05E10  
**Expected outcome:** Explain patch embedding and ViT behavior, and choose between CNN, ViT and hierarchical backbones for a task.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Images as Token Sequences**

- Patch embedding and position embeddings
- The class token and pooling

**Topic 2 — The ViT Architecture**

- Encoder-only transformer applied to patches
- Differences from CNNs: weaker inductive bias, global receptive field from layer one

**Topic 3 — Data, Scale, and Pretraining**

- Why ViTs need large-scale pretraining or strong augmentation
- Supervised, contrastive and self-supervised pretraining (DINO-style, masked autoencoding)

**Topic 4 — Hierarchical and Hybrid Designs**

- Windowed attention (Swin-style) and convolution hybrids
- Handling high resolution and dense prediction

**Topic 5 — Foundation Vision Models**

- Promptable segmentation and open-vocabulary detection (concept)
- Choosing a backbone: accuracy, latency and data size

</details>

**Important concepts**

- *Commands / APIs / Code:* `timm`/Hugging Face ViT loading and patch-embedding shape walkthrough (illustrative)
- *Mechanisms & failure scenarios:* Insufficient data for training ViTs from scratch, resolution changes breaking position embeddings, quadratic cost at high resolution, domain shift.

<a id="s06-module-2"></a>

## Module 2 — Training and Adapting LLMs

**5 episodes (S06E09–S06E13) · 24 topics.** This module covers: Pretraining; Training at Scale; Instruction Tuning and Supervised Fine-Tuning; Preference Optimization; Parameter-Efficient Fine-Tuning.

| ID | Episode | Depth |
|---|---|---|
| S06E09 | Pretraining: Objectives, Data, and Scaling Laws | Intermediate |
| S06E10 | Training at Scale: Parallelism, Memory, and Stability | Advanced |
| S06E11 | Instruction Tuning and Supervised Fine-Tuning | Intermediate |
| S06E12 | Preference Optimization: RLHF, Reward Models, and DPO | Advanced |
| S06E13 | Parameter-Efficient Fine-Tuning: LoRA and QLoRA | Intermediate |

### S06E09 — Pretraining: Objectives, Data, and Scaling Laws

**Depth:** Intermediate  
**Learning objective:** Understand how base models are trained and what pretraining does and doesn't provide.  
**Prerequisites:** S06E06, S05E25  
**Expected outcome:** Explain what pretraining produces and estimate the compute implied by a model's size and data.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Objectives**

- Next-token prediction and masked language modeling
- What the loss does and does not teach

**Topic 2 — Training Data**

- Sources, filtering and quality classifiers
- Deduplication and data mixtures

**Topic 3 — Scale**

- Parameters, tokens and compute
- Scaling laws and compute-optimal training
- Emergent behavior debates

**Topic 4 — What a Base Model Is**

- Capabilities and gaps before alignment
- Knowledge cutoff

**Topic 5 — Contamination and Memorization**

- Benchmark contamination
- Memorized private data and copyright concerns

</details>

**Important concepts**

- *Commands / APIs / Code:* scaling-law back-of-envelope calculation, data dedup concept
- *Mechanisms & failure scenarios:* Benchmark contamination, memorized private data, data quality dominating model quality.

### S06E10 — Training at Scale: Parallelism, Memory, and Stability

**Depth:** Advanced  
**Learning objective:** Understand, at concept level, how models too big for one GPU are trained.  
**Prerequisites:** S05E26, S06E09  
**Expected outcome:** Estimate training memory and choose among parallelism strategies conceptually.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Memory and Compute Budget**

- Parameters, gradients, optimizer state and activations
- Mixed precision and activation checkpointing
- Throughput and model-FLOPs utilization

**Topic 2 — Data Parallelism and Sharding**

- Replicated models and gradient all-reduce
- ZeRO/FSDP sharding idea

**Topic 3 — Model Parallelism**

- Tensor, pipeline and sequence parallelism
- Communication costs

**Topic 4 — Stability and Operations**

- Loss spikes, restarts and checkpoint cadence
- Hardware failures in long runs

**Topic 5 — Who Should Pretrain**

- Why most teams fine-tune rather than pretrain
- Cost reasoning

</details>

**Important concepts**

- *Commands / APIs / Code:* memory-estimate formula, FSDP/DeepSpeed config (concept)
- *Mechanisms & failure scenarios:* Communication-bound scaling, silent data corruption, divergence after a bad batch.

### S06E11 — Instruction Tuning and Supervised Fine-Tuning

**Depth:** Intermediate  
**Learning objective:** Understand how a base model becomes an assistant that follows instructions.  
**Prerequisites:** S06E09, S06E02  
**Expected outcome:** Explain an SFT pipeline and identify data and template pitfalls.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Supervised Fine-Tuning**

- Instruction-response data
- Loss masking on assistant tokens
- Chat templates and special tokens

**Topic 2 — Data Quality**

- Quality vs quantity
- Synthetic data and distillation from stronger models
- Format and style overfitting

**Topic 3 — Evaluation and Risks**

- Regression on base capabilities
- Catastrophic forgetting
- Held-out evaluation sets

**Topic 4 — Training Mechanics**

- Learning rates, epochs and packing
- Full fine-tuning vs adapters

</details>

**Important concepts**

- *Commands / APIs / Code:* `trl` SFTTrainer (concept), chat-template application
- *Mechanisms & failure scenarios:* Training on prompt tokens, template mismatch at inference, narrow data causing capability loss.

### S06E12 — Preference Optimization: RLHF, Reward Models, and DPO

**Depth:** Advanced  
**Learning objective:** Understand how human preferences shape model behavior and the trade-offs among methods.  
**Prerequisites:** S06E11, S02E17, S05E23  
**Expected outcome:** Compare RLHF and DPO and explain failure modes such as reward hacking.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Preference Data and Reward Models**

- Pairwise comparisons and the Bradley–Terry model
- Reward model training

**Topic 2 — RLHF Pipeline**

- Policy optimization with a KL constraint
- PPO in the language-model setting (builds on S05E23)
- Cost and instability

**Topic 3 — Direct Preference Optimization**

- Deriving DPO from the RLHF objective
- Related direct objectives and trade-offs

**Topic 4 — Verifiable Rewards**

- Reinforcement learning for reasoning with checkable outcomes (concept)
- Rule-based vs learned rewards

**Topic 5 — Failure Modes and Evaluation**

- Reward hacking, sycophancy and verbosity bias
- Safety implications and release risk

</details>

**Important concepts**

- *Commands / APIs / Code:* DPO loss formula walkthrough, `trl` DPOTrainer (concept)
- *Mechanisms & failure scenarios:* Over-optimization of the reward proxy, sycophancy, verbose-answer bias.

### S06E13 — Parameter-Efficient Fine-Tuning: LoRA and QLoRA

**Depth:** Intermediate  
**Learning objective:** Fine-tune large models with small trainable adapters and understand the memory arithmetic.  
**Prerequisites:** S06E11, S02E04  
**Expected outcome:** Configure a LoRA/QLoRA run conceptually and justify fine-tuning versus alternatives.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — LoRA**

- Low-rank updates (link to SVD)
- Rank, alpha and target modules
- Parameter and memory savings

**Topic 2 — QLoRA**

- Quantized base weights with trainable adapters
- Paged optimizers (concept)

**Topic 3 — Configuring a Run**

- Learning rate, rank and data size interactions
- Merging adapters vs serving them separately

**Topic 4 — Serving Adapters**

- Multi-adapter serving and routing
- Merging adapters vs keeping them separate
- Memory and latency overhead of adapter serving

**Topic 5 — Deciding to Fine-Tune**

- Prompting vs retrieval vs fine-tuning
- Evaluation before and after

</details>

**Important concepts**

- *Commands / APIs / Code:* `peft.LoraConfig`, `get_peft_model`, `bitsandbytes` 4-bit loading (concept)
- *Mechanisms & failure scenarios:* Underfitting from too-low rank, adapter/base version mismatch, forgetting caused by aggressive learning rates.

<a id="s06-module-3"></a>

## Module 3 — Inference and Efficiency

**6 episodes (S06E14–S06E19) · 25 topics.** This module covers: LLM Inference Step by Step; The KV Cache and Context Windows; Decoding Strategies; Quantization, Pruning, and Distillation; Efficient Attention; Mixture of Experts and Alternatives to Dense Transformers.

| ID | Episode | Depth |
|---|---|---|
| S06E14 | LLM Inference Step by Step: Prefill and Decode | Intermediate |
| S06E15 | The KV Cache and Context Windows | Intermediate |
| S06E16 | Decoding Strategies: Temperature, Top-k, Top-p, and Structured Decoding | Intermediate |
| S06E17 | Quantization, Pruning, and Distillation | Intermediate |
| S06E18 | Efficient Attention: FlashAttention, Grouped-Query Attention, and Long-Context Techniques | Advanced |
| S06E19 | Mixture of Experts and Alternatives to Dense Transformers | Advanced |

### S06E14 — LLM Inference Step by Step: Prefill and Decode

**Depth:** Intermediate  
**Learning objective:** Trace exactly what happens between a prompt and the generated tokens.  
**Prerequisites:** S06E06  
**Expected outcome:** Explain TTFT, per-token latency, and why generation speed is bounded by memory bandwidth.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — The Two Phases**

- Prefill: processing the prompt in parallel
- Decode: one token at a time
- Time to first token vs inter-token latency

**Topic 2 — From Logits to Tokens**

- Final projection, logits and softmax
- Sampling vs greedy and stopping conditions

**Topic 3 — Memory-Bound Decode and Its Implications**

- Weights read per generated token
- Arithmetic intensity
- Batching to amortize weight reads
- Throughput vs latency

</details>

**Important concepts**

- *Commands / APIs / Code:* manual generation loop with a small model, `generate()` parameters
- *Mechanisms & failure scenarios:* Quadratic recomputation without caching, runaway generation without stop conditions, latency dominated by the decode phase.

### S06E15 — The KV Cache and Context Windows

**Depth:** Intermediate  
**Learning objective:** Understand the main memory cost of serving LLMs and why long contexts are expensive.  
**Prerequisites:** S06E14, S06E04  
**Expected outcome:** Calculate KV-cache size for a model and workload and explain long-context trade-offs.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — What the Cache Stores**

- Keys and values per layer and head
- Why recomputation is avoided

**Topic 2 — Cache Size**

- The size formula and worked examples
- Growth with sequence length and batch size

**Topic 3 — Management**

- Paged allocation and fragmentation
- Eviction, offloading and prefix sharing

**Topic 4 — Compression**

- Quantized KV caches
- Grouped-query attention's effect

**Topic 5 — Long-Context Reality**

- Cost and latency of long prompts
- Quality degradation in the middle of context
- Context windows vs retrieval

</details>

**Important concepts**

- *Commands / APIs / Code:* KV-cache memory calculation, `use_cache` generation flag
- *Mechanisms & failure scenarios:* Out-of-memory from many concurrent long sequences, cache fragmentation, stale cache after prompt change.

### S06E16 — Decoding Strategies: Temperature, Top-k, Top-p, and Structured Decoding

**Depth:** Intermediate  
**Learning objective:** Control generation behavior by manipulating the next-token distribution.  
**Prerequisites:** S06E14, S02E10  
**Expected outcome:** Select decoding settings for a task and explain their effect on the distribution.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Sampling Controls**

- Greedy and beam search
- Temperature scaling
- Top-k and top-p (nucleus) sampling

**Topic 2 — Penalties and Constraints**

- Repetition and presence penalties
- Logit bias and stop sequences

**Topic 3 — Structured Decoding and Choosing Settings**

- Grammar- and schema-constrained decoding
- Effects on answer quality
- Determinism vs creativity
- Reproducibility limits (seeds, nondeterministic kernels)

</details>

**Important concepts**

- *Commands / APIs / Code:* `generate(temperature=…, top_p=…)`, logits processor sketch
- *Mechanisms & failure scenarios:* High temperature increasing hallucination, repetition loops at temperature zero, constrained decoding truncating answers.

### S06E17 — Quantization, Pruning, and Distillation

**Depth:** Intermediate  
**Learning objective:** Shrink and speed up models and understand what quality is lost.  
**Prerequisites:** S06E14, S02E18  
**Expected outcome:** Choose a compression approach and validate it against task-level quality.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Number Formats**

- FP16, BF16, FP8, INT8 and INT4
- Per-tensor, per-channel and group-wise scaling

**Topic 2 — Quantization Methods**

- Post-training quantization vs quantization-aware training
- Weight-only vs weight-and-activation quantization
- Outliers and calibration data

**Topic 3 — Other Compression**

- Pruning and sparsity
- Distillation into smaller models

**Topic 4 — Evaluating Trade-offs**

- Accuracy degradation on tasks, not just perplexity
- Hardware and runtime support
- Cost and latency gains

</details>

**Important concepts**

- *Commands / APIs / Code:* GGUF/AWQ/GPTQ loading (concept), `bitsandbytes` configs
- *Mechanisms & failure scenarios:* Outlier activations breaking INT8, quality collapse on specific tasks, no real speedup on unsupported hardware.

### S06E18 — Efficient Attention: FlashAttention, Grouped-Query Attention, and Long-Context Techniques

**Depth:** Advanced  
**Learning objective:** Understand the engineering changes that make attention faster and cheaper, and how context windows are extended.  
**Prerequisites:** S06E15, S06E06  
**Expected outcome:** Explain why FlashAttention and GQA help, how sparse and long-context techniques trade quality for cost, and when each matters.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Attention Bottleneck**

- Compute vs memory traffic in standard attention
- The quadratic attention matrix

**Topic 2 — IO-Aware Attention**

- Tiling and online softmax (FlashAttention idea)
- Why exact attention can be faster and use less memory

**Topic 3 — Sharing Keys and Values**

- Multi-query and grouped-query attention
- Impact on KV-cache size and decode speed

**Topic 4 — Sparse and Windowed Attention**

- Sliding-window and global-token patterns
- Quality-cost trade-offs

**Topic 5 — Extending Context**

- Position-scaling methods and continued training
- Ring and sequence-parallel attention (concept)
- Evaluating long-context quality honestly

</details>

**Important concepts**

- *Commands / APIs / Code:* `scaled_dot_product_attention` backends, GQA head-sharing shape illustration, KV-cache size comparison across MHA/MQA/GQA
- *Mechanisms & failure scenarios:* Memory-bound attention despite fewer FLOPs, accuracy loss from aggressive sparsity, long-context quality degradation, mis-scaled position parameters.

### S06E19 — Mixture of Experts and Alternatives to Dense Transformers

**Depth:** Advanced  
**Learning objective:** Understand sparse expert models and state-space and hybrid architectures, and what they change for training and serving.  
**Prerequisites:** S06E18, S06E06, S06E10  
**Expected outcome:** Explain how MoE and state-space models differ from dense transformers and reason about their serving implications.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Why Sparse Computation**

- Decoupling parameter count from per-token compute
- Active vs total parameters

**Topic 2 — Mixture of Experts**

- Routers, top-k gating and expert capacity
- Load-balancing losses and routing collapse

**Topic 3 — Training and Serving MoE**

- Expert parallelism and all-to-all communication
- Memory footprint and batching effects

**Topic 4 — State-Space Models and Hybrids**

- Recurrent formulations with constant-size state
- Selective state-space models (Mamba-style) at concept level
- Hybrid attention/SSM designs

**Topic 5 — Choosing Architectures**

- What each design is good and bad at
- Why dense transformers still dominate and how to evaluate claims

</details>

**Important concepts**

- *Commands / APIs / Code:* Top-k router sketch with load-balancing loss (illustrative), active vs total parameter calculation
- *Mechanisms & failure scenarios:* Expert load imbalance and routing collapse, serving memory dominated by total parameters, communication overhead for expert parallelism, quality gaps on retrieval-heavy tasks for some recurrent alternatives.

<a id="s06-module-4"></a>

## Module 4 — Model Behavior and Selection

**5 episodes (S06E20–S06E24) · 18 topics.** This module covers: Reasoning Models and Test-Time Compute; Hallucinations, Calibration, and Model Limitations; Evaluating LLMs; Choosing Models; Multimodal LLMs.

| ID | Episode | Depth |
|---|---|---|
| S06E20 | Reasoning Models and Test-Time Compute | Intermediate |
| S06E21 | Hallucinations, Calibration, and Model Limitations | Intermediate |
| S06E22 | Evaluating LLMs: Benchmarks, Contamination, and LLM-as-Judge | Intermediate |
| S06E23 | Choosing Models: Open-Weight, Hosted APIs, and Local Inference | Intermediate |
| S06E24 | Multimodal LLMs: Vision-Language and Audio Models | Intermediate |

### S06E20 — Reasoning Models and Test-Time Compute

**Depth:** Intermediate  
**Learning objective:** Understand how models "think" with extra tokens and when that is worth the cost.  
**Prerequisites:** S06E12, S06E16  
**Expected outcome:** Decide when to use reasoning-style models and budget their cost.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Chain-of-Thought and Beyond**

- Intermediate reasoning tokens
- Self-consistency and search over samples

**Topic 2 — Reasoning-Trained Models and Compute Trade-offs**

- Reinforcement learning on verifiable rewards (concept)
- Long reasoning traces
- Token cost and latency of reasoning
- Budget controls

**Topic 3 — Limits**

- Faithfulness of reasoning traces
- Overthinking and loops
- Evaluation difficulties

</details>

**Important concepts**

- *Commands / APIs / Code:* reasoning-effort parameters in APIs (concept), self-consistency voting sketch
- *Mechanisms & failure scenarios:* Plausible but wrong reasoning, runaway token usage, reasoning traces that do not reflect actual computation.

### S06E21 — Hallucinations, Calibration, and Model Limitations

**Depth:** Intermediate  
**Learning objective:** Understand why LLMs produce confident falsehoods and which mitigations actually work.  
**Prerequisites:** S06E16, S04E02  
**Expected outcome:** Classify hallucination types and select mitigations proportionate to risk.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Why Hallucination Happens**

- Training objective vs truthfulness
- Knowledge gaps and long-tail facts

**Topic 2 — Types of Failure**

- Fabricated facts and citations
- Prompt-induced and context-induced errors, sycophancy

**Topic 3 — Detecting and Mitigating Hallucination**

- Factuality evaluation
- Uncertainty signals and self-consistency
- Retrieval grounding, constrained outputs and abstention
- Human review and guardrails
- Honest limits: no method eliminates hallucination

</details>

**Important concepts**

- *Commands / APIs / Code:* logprob inspection, self-consistency check
- *Mechanisms & failure scenarios:* Fabricated citations, sycophantic agreement with false premises, overconfident numerical answers.

### S06E22 — Evaluating LLMs: Benchmarks, Contamination, and LLM-as-Judge

**Depth:** Intermediate  
**Learning objective:** Read benchmark claims critically and design task-specific evaluations.  
**Prerequisites:** S06E21, S02E14  
**Expected outcome:** Critique a benchmark claim and outline a defensible task-level evaluation.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Benchmarks**

- Knowledge, reasoning, code and safety benchmarks
- Saturation and contamination

**Topic 2 — Evaluation Methods and LLM-as-Judge**

- Automatic metrics vs human evaluation
- Pairwise comparison and Elo-style ranking
- Strengths and known biases
- Calibrating against humans

**Topic 3 — Task-Specific Evals**

- Building a representative evaluation set
- Statistical confidence on small sets
- Regression testing across model versions

</details>

**Important concepts**

- *Commands / APIs / Code:* evaluation harness usage (concept), judge-prompt template
- *Mechanisms & failure scenarios:* Judge favoring longer answers, leaderboard overfitting, evaluation set too small to detect change.

### S06E23 — Choosing Models: Open-Weight, Hosted APIs, and Local Inference

**Depth:** Intermediate  
**Learning objective:** Select a model deployment option using capability, cost, latency, privacy and operational burden.  
**Prerequisites:** S06E22, S06E17  
**Expected outcome:** Produce a justified model-selection decision for an application.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Options**

- Hosted APIs, open-weight models and local runtimes
- Licenses and usage terms
- Model sizes and hardware requirements

**Topic 2 — Provider and Model Families as Examples**

- Closed-model providers as examples: OpenAI GPT family, Anthropic Claude, Google Gemini (tiers, modalities, context length)
- Open-weight families as examples: Llama, Qwen, Gemma, Mistral (sizes, licenses, hosting)
- Reading provider comparisons: benchmarks vs your own evaluation
- Detailed API capability comparison and multi-provider integration are in S07E16

**Topic 3 — Selection Criteria**

- Quality on your task vs general benchmarks
- Latency, throughput and cost per token
- Data privacy and residency

**Topic 4 — Operating Considerations**

- Versioning and deprecation
- Vendor lock-in and portability
- Fallback strategy

**Topic 5 — A Decision Process**

- Shortlisting, evaluating on your data, and documenting the choice
- Shortlisting by hard constraints (license, data location, hardware)
- Evaluating shortlisted models on your own data
- Documenting the decision and the triggers for revisiting it

</details>

**Important concepts**

- *Commands / APIs / Code:* OpenAI-compatible local endpoint (concept), model-card review
- *Mechanisms & failure scenarios:* Model deprecation breaking prompts, license restrictions overlooked, underestimating hosting cost.

### S06E24 — Multimodal LLMs: Vision-Language and Audio Models

**Depth:** Intermediate  
**Learning objective:** Understand how images and audio are turned into tokens a language model can use.  
**Prerequisites:** S06E07, S06E08, S05E25  
**Expected outcome:** Describe how a multimodal model ingests images and when pipelines beat native models.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Vision-Language Models**

- Vision encoder, projector and language model
- Image tokens and resolution cost

**Topic 2 — Training Stages**

- Alignment pretraining and visual instruction tuning
- Alignment pretraining on image-text pairs
- Visual instruction tuning
- Which components are frozen or trained at each stage

**Topic 3 — Audio and Video**

- Speech encoders and speech-native models
- Streaming and frame sampling
- Native multimodal vs pipeline approaches

**Topic 4 — Capabilities and Limits**

- OCR, charts and spatial-reasoning weaknesses
- Hallucination in images
- Cost and latency of multimodal inputs

</details>

**Important concepts**

- *Commands / APIs / Code:* multimodal API request structure (concept), image token estimate
- *Mechanisms & failure scenarios:* Resolution downscaling losing detail, misread charts, prompt injection inside images.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s06-module-1) | Starting point of the season |
| [Module 2](#s06-module-2) | [Module 1](#s06-module-1) (S06E02, S06E06) |
| [Module 3](#s06-module-3) | [Module 1](#s06-module-1) (S06E04, S06E06); [Module 2](#s06-module-2) (S06E10) |
| [Module 4](#s06-module-4) | [Module 1](#s06-module-1) (S06E07, S06E08); [Module 2](#s06-module-2) (S06E12); [Module 3](#s06-module-3) (S06E16, S06E17) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 5 — Deep Learning & Neural Networks](../season-05-deep-learning/roadmap.md)
- **Next:** [Season 7 — Generative AI Application Engineering](../season-07-generative-ai-engineering/roadmap.md)
- **Draws on:** [Season 2](../season-02-mathematics-for-ai/roadmap.md) (S02E03, S02E04, S02E10, S02E14, S02E17, S02E18); [Season 4](../season-04-advanced-ml-engineering/roadmap.md) (S04E02, S04E13); [Season 5](../season-05-deep-learning/roadmap.md) (S05E04, S05E10, S05E12, S05E13, S05E23, S05E25, S05E26)
- **Required by:** [Season 7](../season-07-generative-ai-engineering/roadmap.md) (via S06E02, S06E13, S06E15, S06E16, S06E17, S06E20, S06E22, S06E23, S06E24); [Season 8](../season-08-rag-engineering/roadmap.md) (via S06E02, S06E07, S06E15); [Season 9](../season-09-ai-agents-and-mcp/roadmap.md) (via S06E20); [Season 10](../season-10-advanced-agentic-ai/roadmap.md) (via S06E12, S06E20); [Season 11](../season-11-mlops-engineering/roadmap.md) (via S06E17); [Season 12](../season-12-llmops-engineering/roadmap.md) (via S06E13, S06E15, S06E17, S06E22); [Season 13](../season-13-ai-infrastructure/roadmap.md) (via S06E06, S06E10, S06E14, S06E15, S06E19, S06E23); [Season 15](../season-15-ai-for-devops/roadmap.md) (via S06E21)
