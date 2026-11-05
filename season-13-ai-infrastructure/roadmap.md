# Season 13 Roadmap — AI Infrastructure & Cloud Engineering

[← Season 13 overview](README.md) · [All seasons](../README.md)

**5 modules · 22 episodes · 86 topics · 227 subtopics · Level: Advanced**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Compute, Memory, and Networking for AI](#s13-module-1)
- [Module 2 — Containers and Kubernetes for AI](#s13-module-2)
- [Module 3 — Distributed Training Infrastructure](#s13-module-3)
- [Module 4 — Inference Infrastructure](#s13-module-4)
- [Module 5 — Cloud, Platform, and Operations](#s13-module-5)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Teach the infrastructure that AI workloads actually run on: GPU hardware and interconnects, containers and Kubernetes configured for accelerators, distributed training and inference systems, cloud AI services, infrastructure as code, multi-tenant AI platforms, FinOps and GPU observability. DevOps, cloud and Kubernetes topics appear only as they serve AI/ML engineering; fundamentals were introduced in Seasons 1 and 11.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S13E01 | Understand why GPUs suit deep learning and what limits their performance. |
| S13E02 | Use simple arithmetic to predict model memory needs and token throughput. |
| S13E03 | Understand how GPUs communicate within and across nodes and why that governs scaling. |
| S13E04 | Compare hardware options on the criteria that determine cost and feasibility. |
| S13E05 | Understand how a container gets access to a GPU and why version mismatches break it. |
| S13E06 | Understand the Kubernetes mechanisms that matter when running AI workloads at scale. |
| S13E07 | Understand how accelerators are exposed to pods and how to share them safely. |
| S13E08 | Run many training and batch jobs fairly and efficiently on shared GPU capacity. |
| S13E09 | Understand how training scales across GPUs by replicating or sharding model state, and what memory and communication cost each choice has. |
| S13E10 | Understand how a model too large for one GPU is split across devices and how strategies are combined to match topology. |
| S13E11 | Keep long-running training jobs fed, durable and recoverable. |
| S13E12 | Understand the scheduling and memory mechanisms inside modern serving engines. |
| S13E13 | Serve models that exceed one GPU and understand architectures that separate inference phases. |
| S13E14 | Scale inference capacity on the right signals without wasting GPUs or violating latency SLOs. |
| S13E15 | Move large model files to where they are needed quickly, safely and reproducibly. |
| S13E16 | Navigate managed AI offerings across major clouds and decide when to use them. |
| S13E17 | Understand the common architecture of managed generative-AI platforms by mapping the capabilities of Amazon Bedrock, Azure AI Foundry with Azure OpenAI, and Google Vertex AI onto one reference model, and decide when managed services are the right choice. |
| S13E18 | Connect AI services securely using private networking and least-privilege identity. |
| S13E19 | Provision and change AI infrastructure repeatably and reviewably. |
| S13E20 | Turn infrastructure into a platform that many teams can use safely. |
| S13E21 | Understand and reduce the cost of AI infrastructure without harming delivery. |
| S13E22 | Monitor the health and efficiency of AI infrastructure and diagnose bottlenecks. |

## Prerequisites and Expected Knowledge

- **Season 3 — [Machine Learning Foundations](../season-03-machine-learning/roadmap.md)**: S03E06, S03E11
- **Season 5 — [Deep Learning & Neural Networks](../season-05-deep-learning/roadmap.md)**: S05E26, S05E27
- **Season 6 — [LLMs & Transformer Architecture](../season-06-llms-and-transformers/roadmap.md)**: S06E06, S06E10, S06E14, S06E15, S06E19, S06E23
- **Season 7 — [Generative AI Application Engineering](../season-07-generative-ai-engineering/roadmap.md)**: S07E06
- **Season 8 — [RAG Engineering](../season-08-rag-engineering/roadmap.md)**: S08E19
- **Season 10 — [Advanced Agentic AI](../season-10-advanced-agentic-ai/roadmap.md)**: S10E12
- **Season 11 — [MLOps Engineering](../season-11-mlops-engineering/roadmap.md)**: S11E04, S11E05, S11E17, S11E20, S11E25, S11E26
- **Season 12 — [LLMOps Engineering](../season-12-llmops-engineering/roadmap.md)**: S12E09, S12E12

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Compute, Memory, and Networking for AI](#s13-module-1) | S13E01–S13E04 | 4 | 3 Intermediate, 1 Advanced |
| 2 | [Containers and Kubernetes for AI](#s13-module-2) | S13E05–S13E08 | 4 | 1 Intermediate, 3 Advanced |
| 3 | [Distributed Training Infrastructure](#s13-module-3) | S13E09–S13E11 | 3 | 3 Advanced |
| 4 | [Inference Infrastructure](#s13-module-4) | S13E12–S13E15 | 4 | 3 Advanced, 1 Intermediate |
| 5 | [Cloud, Platform, and Operations](#s13-module-5) | S13E16–S13E22 | 7 | 4 Intermediate, 3 Advanced |

<a id="s13-module-1"></a>

## Module 1 — Compute, Memory, and Networking for AI

**4 episodes (S13E01–S13E04) · 15 topics.** This module covers: GPU Architecture for AI Workloads; Memory, Bandwidth, and Why LLM Inference Is Memory-Bound; Interconnects and Networking; AI Accelerators and Choosing Hardware.

| ID | Episode | Depth |
|---|---|---|
| S13E01 | GPU Architecture for AI Workloads | Intermediate |
| S13E02 | Memory, Bandwidth, and Why LLM Inference Is Memory-Bound | Intermediate |
| S13E03 | Interconnects and Networking: PCIe, NVLink, InfiniBand, and RDMA | Advanced |
| S13E04 | AI Accelerators and Choosing Hardware | Intermediate |

### S13E01 — GPU Architecture for AI Workloads

**Depth:** Intermediate  
**Learning objective:** Understand why GPUs suit deep learning and what limits their performance.  
**Prerequisites:** S05E26, S06E14  
**Expected outcome:** Classify an operation as compute- or memory-bound and explain GPU utilization numbers.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — From CPU to GPU: Architecture and Execution Model**

- Throughput-oriented design
- Streaming multiprocessors, cores and tensor cores
- Threads, warps and kernels
- Kernel launch overhead

**Topic 2 — Memory Hierarchy**

- Registers, shared memory, caches and HBM
- Host-device transfers

**Topic 3 — Performance Concepts**

- FLOPs vs bandwidth: the roofline idea
- Compute-bound vs memory-bound operations
- Utilization, occupancy, power and thermal throttling

</details>

**Important concepts**

- *Commands / APIs / Code:* `nvidia-smi`, `nvidia-smi dmon` output interpretation (illustrative), tiny CUDA-aware PyTorch benchmark
- *Mechanisms & failure scenarios:* Low utilization from small kernels, data transfer bottlenecks, thermal or power throttling.

### S13E02 — Memory, Bandwidth, and Why LLM Inference Is Memory-Bound

**Depth:** Intermediate  
**Learning objective:** Use simple arithmetic to predict model memory needs and token throughput.  
**Prerequisites:** S13E01, S06E15  
**Expected outcome:** Size hardware for a model and workload from first principles.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Memory Budgeting**

- Weights, KV cache, activations and framework overhead
- Precision and parameter-count math

**Topic 2 — Throughput Math**

- Bytes per token vs bandwidth
- Batching and arithmetic intensity
- Estimating tokens per second

**Topic 3 — Capacity Planning**

- Concurrency limits from KV-cache size
- Multi-GPU needs
- Cost per million tokens estimation

**Topic 4 — Common Errors**

- Out-of-memory at long contexts despite fitting weights
- Optimistic throughput that ignores bandwidth and fragmentation

</details>

**Important concepts**

- *Commands / APIs / Code:* memory and throughput calculator in Python
- *Mechanisms & failure scenarios:* OOM at long contexts despite fitting weights, optimistic throughput ignoring bandwidth, ignoring fragmentation.

### S13E03 — Interconnects and Networking: PCIe, NVLink, InfiniBand, and RDMA

**Depth:** Advanced  
**Learning objective:** Understand how GPUs communicate within and across nodes and why that governs scaling.  
**Prerequisites:** S13E01, S03E06  
**Expected outcome:** Explain how collective operations use the network and diagnose communication bottlenecks.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Intra-Node Links**

- PCIe vs NVLink/NVSwitch
- Topology awareness and peer-to-peer transfers

**Topic 2 — Inter-Node Networks**

- Ethernet vs InfiniBand; RDMA and RoCE
- Bandwidth, latency and congestion

**Topic 3 — Collective Communication**

- All-reduce, all-gather and reduce-scatter
- Ring and tree algorithms and their costs

**Topic 4 — Practical Implications**

- Communication cost in training and inference
- Network topology and job placement

**Topic 5 — Diagnosing Slow Collectives**

- One slow link stalling a job
- Mismatched NCCL settings

</details>

**Important concepts**

- *Commands / APIs / Code:* `nvidia-smi topo -m` (illustrative), NCCL test usage (concept)
- *Mechanisms & failure scenarios:* Cross-switch placement slowing all-reduce, mismatched NCCL settings, one slow link stalling a job.

### S13E04 — AI Accelerators and Choosing Hardware

**Depth:** Intermediate  
**Learning objective:** Compare hardware options on the criteria that determine cost and feasibility.  
**Prerequisites:** S13E02  
**Expected outcome:** Justify a hardware choice using memory, bandwidth and software considerations.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Landscape**

- GPUs, TPUs, cloud-vendor accelerators and CPUs for inference
- Software ecosystem and portability

**Topic 2 — Selection Criteria**

- Memory capacity and bandwidth, interconnect and precision support
- Training vs inference needs

**Topic 3 — Procurement and Decision Process**

- On-demand, reserved, spot and on-premises
- Availability and quotas
- Benchmarking your own workload
- Price-performance and avoiding lock-in

</details>

**Important concepts**

- *Commands / APIs / Code:* hardware comparison worksheet
- *Mechanisms & failure scenarios:* Benchmarks unlike your workload, software stack unsupported on chosen accelerator, quota delays.

<a id="s13-module-2"></a>

## Module 2 — Containers and Kubernetes for AI

**4 episodes (S13E05–S13E08) · 15 topics.** This module covers: GPU Containers; Kubernetes Architecture for AI Platform Operators; GPUs on Kubernetes; Batch and Training Scheduling.

| ID | Episode | Depth |
|---|---|---|
| S13E05 | GPU Containers: Drivers, CUDA Compatibility, and the Container Runtime | Intermediate |
| S13E06 | Kubernetes Architecture for AI Platform Operators | Advanced |
| S13E07 | GPUs on Kubernetes: Device Plugins, MIG, Time-Slicing, and Sharing | Advanced |
| S13E08 | Batch and Training Scheduling: Queues, Gang Scheduling, and Ray | Advanced |

### S13E05 — GPU Containers: Drivers, CUDA Compatibility, and the Container Runtime

**Depth:** Intermediate  
**Learning objective:** Understand how a container gets access to a GPU and why version mismatches break it.  
**Prerequisites:** S11E05  
**Expected outcome:** Diagnose "GPU not found in container" systematically.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — The GPU Software Stack and Runtime Integration**

- Kernel driver, user-space libraries, CUDA toolkit and framework
- What the image provides vs what the host provides
- Container toolkit and runtime hooks
- Device exposure into the container

**Topic 2 — Compatibility**

- Driver vs CUDA runtime versions
- Base images, wheels and multi-architecture images

**Topic 3 — Troubleshooting**

- Verifying GPU visibility in a container
- Silent CPU fallback and common errors
- Security considerations for device access

</details>

**Important concepts**

- *Commands / APIs / Code:* `docker run --gpus all … nvidia-smi` (illustrative), `torch.cuda.is_available()`
- *Mechanisms & failure scenarios:* Image CUDA newer than host driver supports, missing runtime hook, silently falling back to CPU.

### S13E06 — Kubernetes Architecture for AI Platform Operators

**Depth:** Advanced  
**Learning objective:** Understand the Kubernetes mechanisms that matter when running AI workloads at scale.  
**Prerequisites:** S11E17  
**Expected outcome:** Explain how a pod requesting GPUs is scheduled, started and kept healthy.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Control Plane and Reconciliation**

- API server, etcd, scheduler, controllers and kubelet
- Declarative desired state

**Topic 2 — Custom Resources and Operators**

- Why AI frameworks use operators
- Training-job custom resources (concept)
- Operator reconciliation and failure behavior

**Topic 3 — Scheduling and Resources**

- Requests, limits, QoS and eviction
- Affinity, taints and tolerations
- Priority and preemption

**Topic 4 — Storage**

- CSI volumes for datasets and checkpoints
- Slow checkpoint volumes

**Topic 5 — Networking**

- CNI and pod networking; high-performance networking options
- Services and ingress for inference endpoints

</details>

**Important concepts**

- *Commands / APIs / Code:* `kubectl describe node`, scheduling events (illustrative)
- *Mechanisms & failure scenarios:* Pods evicted under memory pressure, unschedulable pods due to taints, slow checkpoint volumes.

### S13E07 — GPUs on Kubernetes: Device Plugins, MIG, Time-Slicing, and Sharing

**Depth:** Advanced  
**Learning objective:** Understand how accelerators are exposed to pods and how to share them safely.  
**Prerequisites:** S13E06, S13E05  
**Expected outcome:** Choose a GPU sharing model for a workload mix and describe its trade-offs.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Exposing GPUs**

- Device plugin framework and extended resources
- Node labels and discovery
- Operators that install drivers and runtimes

**Topic 2 — Sharing Models and Dynamic Allocation**

- Whole GPU, MIG partitions, time-slicing and MPS
- Isolation, performance and fault-containment differences
- Dynamic resource allocation (concept)

**Topic 3 — Operations**

- Health checks and failed GPUs
- Monitoring utilization per pod
- Upgrades and drain procedures

</details>

**Important concepts**

- *Commands / APIs / Code:* pod spec with `nvidia.com/gpu` resource (illustrative), MIG profile listing (concept)
- *Mechanisms & failure scenarios:* Time-sliced jobs interfering, MIG fragmentation leaving capacity unusable, driver upgrades breaking nodes.

### S13E08 — Batch and Training Scheduling: Queues, Gang Scheduling, and Ray

**Depth:** Advanced  
**Learning objective:** Run many training and batch jobs fairly and efficiently on shared GPU capacity.  
**Prerequisites:** S13E07  
**Expected outcome:** Design a scheduling policy for a shared GPU cluster.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Scheduling Problem**

- Gang scheduling for multi-pod jobs
- Fair-share quotas, priorities and preemption

**Topic 2 — Queueing Systems**

- Kubernetes batch queueing and scheduler extensions (concept)
- Quotas, cohorts and borrowing of idle capacity
- Preemption policies

**Topic 3 — Distributed Compute Frameworks**

- Ray-style clusters and operators
- Job lifecycle and retries

**Topic 4 — Efficiency**

- Bin-packing and fragmentation
- Backfill and elastic jobs
- Cost-aware scheduling with spot capacity; deadlock and starvation

</details>

**Important concepts**

- *Commands / APIs / Code:* job queue and quota definitions (illustrative), Ray cluster spec (concept)
- *Mechanisms & failure scenarios:* Deadlock from partially scheduled jobs, starvation of small jobs, preemption losing hours of work without checkpoints.

<a id="s13-module-3"></a>

## Module 3 — Distributed Training Infrastructure

**3 episodes (S13E09–S13E11) · 14 topics.** This module covers: Distributed Training I; Distributed Training II; Training Infrastructure.

| ID | Episode | Depth |
|---|---|---|
| S13E09 | Distributed Training I: Data Parallelism and Sharded Training | Advanced |
| S13E10 | Distributed Training II: Tensor, Pipeline, Sequence, and Expert Parallelism | Advanced |
| S13E11 | Training Infrastructure: Storage, Checkpointing, and Fault Tolerance | Advanced |

### S13E09 — Distributed Training I: Data Parallelism and Sharded Training

**Depth:** Advanced  
**Learning objective:** Understand how training scales across GPUs by replicating or sharding model state, and what memory and communication cost each choice has.  
**Prerequisites:** S13E03, S06E10  
**Expected outcome:** Choose between replicated and sharded data parallelism for a model and cluster and predict its scaling efficiency.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Data Parallelism**

- Replicated models and gradient all-reduce
- Effective batch size and learning-rate scaling

**Topic 2 — Overlapping Communication and Compute**

- Gradient bucketing and overlap
- Scaling efficiency and how to measure it

**Topic 3 — Sharded Data Parallelism**

- ZeRO stages and FSDP
- What is sharded: optimizer state, gradients, parameters

**Topic 4 — Memory vs Communication Trade-offs**

- All-gather and reduce-scatter patterns
- Offloading and activation checkpointing

**Topic 5 — Launching and Debugging**

- Process groups, ranks and rendezvous
- Hangs, stragglers and mismatched collectives

</details>

**Important concepts**

- *Commands / APIs / Code:* `torchrun` launch, DDP and FSDP wrapping (concept), scaling-efficiency calculation
- *Mechanisms & failure scenarios:* Communication overhead erasing gains, stragglers slowing synchronous training, mismatched seeds or data shards, optimizer-state memory dominating, batch-size and learning-rate scaling errors.

### S13E10 — Distributed Training II: Tensor, Pipeline, Sequence, and Expert Parallelism

**Depth:** Advanced  
**Learning objective:** Understand how a model too large for one GPU is split across devices and how strategies are combined to match topology.  
**Prerequisites:** S13E09, S06E06, S06E19  
**Expected outcome:** Propose a parallelism layout for a given model and cluster topology and predict its bottleneck.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Tensor Parallelism**

- Splitting matrix multiplications across GPUs
- Per-layer communication and why it needs fast links

**Topic 2 — Pipeline Parallelism**

- Stage partitioning and micro-batching
- Pipeline bubbles and schedules

**Topic 3 — Sequence and Context Parallelism**

- Splitting long sequences across devices
- Ring-style attention and its communication pattern (concept)
- When context parallelism is needed

**Topic 4 — Expert Parallelism**

- Placing experts and all-to-all communication (link to S06E19)
- Load imbalance and capacity factors
- Combining expert parallelism with data and tensor parallelism

**Topic 5 — Combining Strategies**

- 3D and hybrid layouts
- Matching strategy to topology
- Measuring and reporting model-FLOPs utilization

</details>

**Important concepts**

- *Commands / APIs / Code:* Parallelism layout configuration (illustrative), pipeline-bubble calculation, communication-volume estimate per strategy
- *Mechanisms & failure scenarios:* Pipeline bubbles wasting GPUs, tensor parallelism across slow links, expert load imbalance, activation memory imbalance across stages, silent numerical differences between layouts.

### S13E11 — Training Infrastructure: Storage, Checkpointing, and Fault Tolerance

**Depth:** Advanced  
**Learning objective:** Keep long-running training jobs fed, durable and recoverable.  
**Prerequisites:** S13E09, S05E27  
**Expected outcome:** Design storage, checkpoint and recovery policy for a multi-day training job.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Data and Storage**

- Object storage vs parallel file systems vs local NVMe
- Sharded datasets and streaming loaders
- Throughput requirements per GPU

**Topic 2 — Checkpointing**

- What to save: weights, optimizer, data position and RNG state
- Frequency vs overhead
- Asynchronous and sharded checkpoints; verifying and restoring

**Topic 3 — Failure Handling**

- Node and GPU failures, stragglers
- Elastic training and automatic restart

**Topic 4 — Silent Failures**

- Corrupt checkpoints discovered late
- Silent data corruption detection (concept)
- I/O stalls starving GPUs

</details>

**Important concepts**

- *Commands / APIs / Code:* checkpoint save/restore sketch, restart policy configuration (illustrative)
- *Mechanisms & failure scenarios:* Corrupt checkpoint discovered after days, data loader nondeterminism on resume, I/O stalls starving GPUs.

<a id="s13-module-4"></a>

## Module 4 — Inference Infrastructure

**4 episodes (S13E12–S13E15) · 14 topics.** This module covers: High-Throughput LLM Inference Engines; Distributed Inference; Autoscaling AI Workloads; Model Artifacts.

| ID | Episode | Depth |
|---|---|---|
| S13E12 | High-Throughput LLM Inference Engines: Continuous Batching and Paged KV Cache | Advanced |
| S13E13 | Distributed Inference: Multi-GPU Serving, Disaggregated Prefill/Decode, and Speculative Decoding | Advanced |
| S13E14 | Autoscaling AI Workloads: Signals, Cold Starts, and Capacity | Advanced |
| S13E15 | Model Artifacts: Storage, Registries, and Distribution | Intermediate |

### S13E12 — High-Throughput LLM Inference Engines: Continuous Batching and Paged KV Cache

**Depth:** Advanced  
**Learning objective:** Understand the scheduling and memory mechanisms inside modern serving engines.  
**Prerequisites:** S06E15, S13E02  
**Expected outcome:** Tune an inference engine against throughput and latency targets.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Why Static Batching Fails**

- Variable-length requests
- GPU idle time and head-of-line blocking

**Topic 2 — Continuous Batching**

- Iteration-level scheduling
- Admission control

**Topic 3 — Memory Management**

- Paged KV cache and block allocation
- Prefix caching
- Preemption and swapping under pressure

**Topic 4 — Scheduling Prefill and Decode**

- Chunked prefill
- Long prompts blocking decode

**Topic 5 — Tuning and Measurement**

- Throughput vs latency measurement
- Tensor-parallel serving
- Batch size vs tail latency

</details>

**Important concepts**

- *Commands / APIs / Code:* launching an inference engine server with parallelism flags (illustrative), load-test run (concept)
- *Mechanisms & failure scenarios:* KV-cache exhaustion causing preemption storms, long prompts blocking decode, over-aggressive batch size hurting tail latency.

### S13E13 — Distributed Inference: Multi-GPU Serving, Disaggregated Prefill/Decode, and Speculative Decoding

**Depth:** Advanced  
**Learning objective:** Serve models that exceed one GPU and understand architectures that separate inference phases.  
**Prerequisites:** S13E12, S13E09  
**Expected outcome:** Decide when disaggregation or speculation is worthwhile and what operational risks they add.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Multi-GPU and Multi-Node Serving**

- Tensor and pipeline parallel inference
- Expert placement for MoE models
- Communication cost per token

**Topic 2 — Disaggregation**

- Separating prefill and decode pools
- KV-cache transfer cost and when it helps

**Topic 3 — Speculative Decoding, Routing, and Failure**

- Draft-and-verify mechanism and acceptance rate
- When it slows low-acceptance workloads
- Request routing and cache-aware load balancing
- Behavior when a node drops

</details>

**Important concepts**

- *Commands / APIs / Code:* multi-GPU serving launch (illustrative), acceptance-rate calculation
- *Mechanisms & failure scenarios:* Interconnect-bound decode, KV transfer overhead exceeding benefits, speculative decoding slowing low-acceptance workloads.

### S13E14 — Autoscaling AI Workloads: Signals, Cold Starts, and Capacity

**Depth:** Advanced  
**Learning objective:** Scale inference capacity on the right signals without wasting GPUs or violating latency SLOs.  
**Prerequisites:** S13E12, S13E06  
**Expected outcome:** Design an autoscaling policy with quantified cold-start behavior.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Scaling Signals**

- Why CPU/GPU utilization are poor signals for LLMs
- Queue depth, concurrent requests, KV-cache usage and tokens/s

**Topic 2 — Autoscaling Mechanics**

- Horizontal pod autoscaling and event-driven scaling
- Custom metrics pipelines
- Node provisioning latency and flapping

**Topic 3 — Cold Starts and Strategies**

- Image pull and model load time
- Warm pools and pre-loading weights
- Scale-to-zero trade-offs
- Overload protection and graceful degradation

</details>

**Important concepts**

- *Commands / APIs / Code:* autoscaler configuration on a custom metric (illustrative)
- *Mechanisms & failure scenarios:* Scale-up too slow for traffic spikes, flapping, minutes-long cold starts.

### S13E15 — Model Artifacts: Storage, Registries, and Distribution

**Depth:** Intermediate  
**Learning objective:** Move large model files to where they are needed quickly, safely and reproducibly.  
**Prerequisites:** S11E04, S13E14  
**Expected outcome:** Plan model artifact storage and distribution to meet start-up time and security goals.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Artifact Management**

- Weight formats and sizes
- Object storage layouts, versioning and registries

**Topic 2 — Distribution**

- Pre-pulling to nodes and caching layers
- Fast loading techniques (memory-mapped, streaming)
- Bandwidth and egress cost

**Topic 3 — Integrity and Security**

- Checksums, signatures and safe serialization
- Access control for proprietary weights and provenance records

</details>

**Important concepts**

- *Commands / APIs / Code:* model sync to object storage and node cache (illustrative), checksum verification
- *Mechanisms & failure scenarios:* Cold nodes pulling hundreds of GB simultaneously, corrupted download loading silently, unsafe pickle files executed on load.

<a id="s13-module-5"></a>

## Module 5 — Cloud, Platform, and Operations

**7 episodes (S13E16–S13E22) · 28 topics.** This module covers: Cloud AI Services Landscape; Managed Generative AI Platforms; Cloud Networking and Identity for AI Workloads; Infrastructure as Code for AI Platforms; AI Platform Engineering; AI FinOps; Observability for AI Infrastructure.

| ID | Episode | Depth |
|---|---|---|
| S13E16 | Cloud AI Services Landscape: Managed Models, Platforms, and Their Trade-offs | Intermediate |
| S13E17 | Managed Generative AI Platforms: One Architecture Across Bedrock, Azure AI Foundry, and Vertex AI | Advanced |
| S13E18 | Cloud Networking and Identity for AI Workloads | Intermediate |
| S13E19 | Infrastructure as Code for AI Platforms | Advanced |
| S13E20 | AI Platform Engineering: Multi-Tenancy, Self-Service, and Golden Paths | Advanced |
| S13E21 | AI FinOps: GPU Cost, Utilization, and Capacity Economics | Intermediate |
| S13E22 | Observability for AI Infrastructure: GPU, Cluster, and Serving Metrics | Intermediate |

### S13E16 — Cloud AI Services Landscape: Managed Models, Platforms, and Their Trade-offs

**Depth:** Intermediate  
**Learning objective:** Navigate managed AI offerings across major clouds and decide when to use them.  
**Prerequisites:** S06E23, S07E06  
**Expected outcome:** Compare managed AI services against self-hosting for a given workload.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Service Categories**

- Hosted foundation-model services and model catalogs
- Managed training and serving platforms
- Managed retrieval, guardrails and agent features
- Examples of each category from Amazon Bedrock, Azure AI Foundry with Azure OpenAI, and Google Vertex AI (architecture mapping in S13E17)

**Topic 2 — Capacity and Limits**

- On-demand vs provisioned throughput
- Quotas, throttling and regional availability
- Model versions and deprecations

**Topic 3 — Decision Factors**

- Data residency and private connectivity
- Lock-in, portability and cost models
- Deciding between managed generative-AI services and self-managed stacks

</details>

**Important concepts**

- *Commands / APIs / Code:* provider-neutral capability comparison table (product behavior verified at scripting time)
- *Mechanisms & failure scenarios:* Quota exhaustion during launch, region lacking the needed model, deprecation breaking a pipeline.

### S13E17 — Managed Generative AI Platforms: One Architecture Across Bedrock, Azure AI Foundry, and Vertex AI

**Depth:** Advanced  
**Learning objective:** Understand the common architecture of managed generative-AI platforms by mapping the capabilities of Amazon Bedrock, Azure AI Foundry with Azure OpenAI, and Google Vertex AI onto one reference model, and decide when managed services are the right choice.  
**Prerequisites:** S13E16, S08E19, S10E12, S11E26, S12E12  
**Expected outcome:** Map any managed generative-AI platform capability to the reference architecture, compare platforms on architecture rather than branding, and make a justified managed vs self-managed decision.

<details>
<summary>Topics and subtopics (7 topics)</summary>

**Topic 1 — The Reference Architecture**

- Control plane vs data plane; model catalog and deployments
- Inference modes: on-demand vs provisioned throughput; quotas, regions and throttling
- Where managed platforms sit relative to gateways, RAG and agents built earlier in the curriculum

**Topic 2 — Platform Mapping**

- A capability-by-capability table, not three tutorials
- Amazon Bedrock: model access, Agents, Knowledge Bases, Guardrails
- Azure AI Foundry and Azure OpenAI: model catalog and deployments, Azure AI Search, content safety
- Google Vertex AI: Model Garden and Gemini, Agent Builder, Vector Search

**Topic 3 — Managed Retrieval and Knowledge Services**

- Managed ingestion, chunking, embedding and vector or search stores
- What is configurable and what is fixed; evaluating retrieval quality in managed pipelines (link to S08E15)

**Topic 4 — Managed Agents and Guardrails**

- Managed agent orchestration, tool and function integration, memory and session state
- Managed guardrails and content safety: policy configuration and its limits

**Topic 5 — Evaluation, Monitoring, and Cost**

- Built-in evaluation and monitoring vs your own evaluation (link to S12E04–E07)
- Cost model: token pricing, provisioned capacity and hidden costs

**Topic 6 — Networking, Identity, and Data Residency**

- Private connectivity, identity and access, encryption and audit logging
- Data residency and customer-data handling terms

**Topic 7 — Portability and the Managed vs Self-Managed Decision**

- Lock-in sources and portability strategies
- Decision framework by team size, compliance, customization and scale
- How to read vendor claims; all product behavior is version-sensitive and verified at scripting time

</details>

**Important concepts**

- *Commands / APIs / Code:* Provider-neutral deployment and invocation definitions (illustrative; product-specific syntax verified at scripting time), capability-mapping matrix, quota and throughput calculation
- *Mechanisms & failure scenarios:* Quota or throttling limits hit at launch, hidden idle provisioned-throughput cost, model or feature unavailable in the required region, proprietary agent or knowledge-base formats creating lock-in, guardrail defaults mismatched to the use case, private-networking misconfiguration exposing endpoints.

### S13E18 — Cloud Networking and Identity for AI Workloads

**Depth:** Intermediate  
**Learning objective:** Connect AI services securely using private networking and least-privilege identity.  
**Prerequisites:** S13E16, S03E11  
**Expected outcome:** Design the network and identity layout for a private AI workload.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Networking**

- VPCs, subnets, routing and security groups
- Private endpoints for model and storage services
- Egress control and DNS

**Topic 2 — Identity**

- IAM roles for workloads, no static keys
- Cross-account access and federation
- Secrets and key management

**Topic 3 — Patterns and Auditing**

- Private inference endpoints
- Data access boundaries for training
- Auditing access; DNS leaks bypassing private links

</details>

**Important concepts**

- *Commands / APIs / Code:* role policy and private-endpoint configuration (illustrative)
- *Mechanisms & failure scenarios:* Public endpoints exposing models, over-broad roles on training jobs, DNS leaks bypassing private links.

### S13E19 — Infrastructure as Code for AI Platforms

**Depth:** Advanced  
**Learning objective:** Provision and change AI infrastructure repeatably and reviewably.  
**Prerequisites:** S13E18, S13E06  
**Expected outcome:** Describe an IaC-managed AI platform with review, policy and cost controls.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — IaC Fundamentals for AI**

- Declarative state, plan/apply and drift
- Modules and environments

**Topic 2 — State Management**

- State storage and locking
- State corruption and recovery

**Topic 3 — AI-Specific Infrastructure**

- GPU node pools, quotas, storage, registries and endpoints
- Cost and capacity guardrails in code
- Cluster add-ons as code (GitOps)

**Topic 4 — Governance and Review**

- Policy as code and secrets handling
- Review of plans that create expensive resources
- Drift remediation

</details>

**Important concepts**

- *Commands / APIs / Code:* `terraform plan/apply` workflow (illustrative), module for a GPU node pool (concept)
- *Mechanisms & failure scenarios:* Unreviewed apply creating expensive GPU nodes, state corruption, drift from console changes.

### S13E20 — AI Platform Engineering: Multi-Tenancy, Self-Service, and Golden Paths

**Depth:** Advanced  
**Learning objective:** Turn infrastructure into a platform that many teams can use safely.  
**Prerequisites:** S13E08, S11E25  
**Expected outcome:** Design a multi-tenant AI platform with isolation, quotas and a self-service path.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Platform Product Thinking**

- Users, workflows and interfaces
- Self-service training, deployment and model access
- Golden paths and templates

**Topic 2 — Multi-Tenancy**

- Namespaces, quotas, network and data isolation
- Fair sharing of GPUs and model endpoints
- Per-tenant cost attribution

**Topic 3 — Reliability and Adoption**

- SLOs for the platform
- Support model and documentation
- Measuring adoption and developer experience

</details>

**Important concepts**

- *Commands / APIs / Code:* tenant onboarding workflow (illustrative), quota definitions
- *Mechanisms & failure scenarios:* Noisy-neighbor jobs, snowflake team setups, platform features nobody uses.

### S13E21 — AI FinOps: GPU Cost, Utilization, and Capacity Economics

**Depth:** Intermediate  
**Learning objective:** Understand and reduce the cost of AI infrastructure without harming delivery.  
**Prerequisites:** S13E20, S12E09  
**Expected outcome:** Build a cost model and optimization plan for an AI platform.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Cost Structure**

- GPU hours, storage, egress and managed-service fees
- Utilization vs allocation
- Idle and fragmented capacity
- Scope: this episode covers GPU and AI-infrastructure cost; general cloud cost optimization and cost anomaly detection with AI are covered in S15E25 and S15E26

**Topic 2 — Levers**

- Rightsizing and sharing
- Spot/preemptible, reservations and committed use
- Scheduling and autoscaling for utilization

**Topic 3 — Governance**

- Tagging, showback and chargeback
- Budgets and anomaly alerts

**Topic 4 — Unit Economics**

- Cost per training run and per million tokens
- Cost per successful task
- Benchmarking self-hosting against API pricing

</details>

**Important concepts**

- *Commands / APIs / Code:* utilization vs cost report (illustrative), unit-cost calculation
- *Mechanisms & failure scenarios:* GPUs reserved but idle, spot interruptions without checkpoints, unattributed spend.

### S13E22 — Observability for AI Infrastructure: GPU, Cluster, and Serving Metrics

**Depth:** Intermediate  
**Learning objective:** Monitor the health and efficiency of AI infrastructure and diagnose bottlenecks.  
**Prerequisites:** S13E12, S11E20  
**Expected outcome:** Define dashboards and alerts that reveal both infrastructure health and serving efficiency.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Signals**

- GPU utilization, memory, power, temperature and error counters
- Cluster, node and pod metrics
- Serving metrics: tokens/s, queue depth, TTFT and KV-cache usage

**Topic 2 — Pipelines and Dashboards**

- Exporters and metric collection
- Dashboards by persona (platform, ML, finance)
- Logs and traces from training and serving

**Topic 3 — Alerting and Diagnosis**

- Symptom-based alerts and SLOs
- Detecting failing GPUs and stragglers
- Correlating infrastructure and application metrics

**Topic 4 — Misleading Signals**

- High utilization with useless work
- Silent GPU errors and alerts on resource use instead of user impact

</details>

**Important concepts**

- *Commands / APIs / Code:* GPU metrics exporter query examples (illustrative), PromQL for queue depth (concept)
- *Mechanisms & failure scenarios:* High "utilization" with useless work, silent GPU errors, alerts on resource use instead of user impact.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s13-module-1) | Starting point of the season |
| [Module 2](#s13-module-2) | Within-module sequence only |
| [Module 3](#s13-module-3) | [Module 1](#s13-module-1) (S13E03) |
| [Module 4](#s13-module-4) | [Module 1](#s13-module-1) (S13E02); [Module 2](#s13-module-2) (S13E06); [Module 3](#s13-module-3) (S13E09) |
| [Module 5](#s13-module-5) | [Module 2](#s13-module-2) (S13E06, S13E08); [Module 4](#s13-module-4) (S13E12) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 12 — LLMOps Engineering](../season-12-llmops-engineering/roadmap.md)
- **Next:** [Season 14 — Production AI Systems, Security & Governance](../season-14-production-ai-systems/roadmap.md)
- **Draws on:** [Season 3](../season-03-machine-learning/roadmap.md) (S03E06, S03E11); [Season 5](../season-05-deep-learning/roadmap.md) (S05E26, S05E27); [Season 6](../season-06-llms-and-transformers/roadmap.md) (S06E06, S06E10, S06E14, S06E15, S06E19, S06E23); [Season 7](../season-07-generative-ai-engineering/roadmap.md) (S07E06); [Season 8](../season-08-rag-engineering/roadmap.md) (S08E19); [Season 10](../season-10-advanced-agentic-ai/roadmap.md) (S10E12); [Season 11](../season-11-mlops-engineering/roadmap.md) (S11E04, S11E05, S11E17, S11E20, S11E25, S11E26); [Season 12](../season-12-llmops-engineering/roadmap.md) (S12E09, S12E12)
- **Required by:** [Season 14](../season-14-production-ai-systems/roadmap.md) (via S13E14, S13E15, S13E20, S13E21); [Season 15](../season-15-ai-for-devops/roadmap.md) (via S13E06, S13E19, S13E21)
