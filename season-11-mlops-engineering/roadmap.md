# Season 11 Roadmap — MLOps Engineering

[← Season 11 overview](README.md) · [All seasons](../README.md)

**5 modules · 27 episodes · 104 topics · 275 subtopics · Level: Intermediate → Advanced**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — The ML Lifecycle and Reproducibility](#s11-module-1)
- [Module 2 — Data and Feature Systems](#s11-module-2)
- [Module 3 — Training Pipelines and CI/CD/CT](#s11-module-3)
- [Module 4 — Model Serving](#s11-module-4)
- [Module 5 — Monitoring, Governance, and Platforms](#s11-module-5)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Teach how machine learning systems are built, shipped and kept healthy: reproducibility, data and feature management, pipelines, CI/CD/CT for ML, distributed and streaming data systems, model serving (including edge and on-device), monitoring and drift, governance, managed ML platforms and platform design. Docker, Kubernetes, CI/CD and cloud appear as supporting infrastructure for ML, not as standalone courses.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S11E01 | Understand why ML systems fail in production differently from ordinary software and what MLOps adds. |
| S11E02 | Make any trained model traceable to the exact data and code that produced it. |
| S11E03 | Record parameters, metrics, artifacts and environment so experiments are comparable and reproducible. |
| S11E04 | Manage model versions as controlled artifacts with a promotion workflow. |
| S11E05 | Package training and serving environments so results do not depend on a machine. |
| S11E06 | Build reliable, re-runnable data workflows for ML. |
| S11E07 | Stop bad data before it trains or serves a model. |
| S11E08 | Understand how large datasets are processed across machines, why shuffles and skew dominate cost, and how table formats make data lakes reliable for ML. |
| S11E09 | Understand how event streams carry data to ML systems, how time and ordering are handled, and how real-time features stay consistent with training data. |
| S11E10 | Understand why features are managed centrally and how training-serving skew is prevented. |
| S11E11 | Turn experiments into reproducible, parameterized, cacheable pipelines. |
| S11E12 | Define what "continuous integration" means when the artifact is a model. |
| S11E13 | Release models safely and recover quickly. |
| S11E14 | Decide when and how a model retrains itself without creating new risks. |
| S11E15 | Choose the right serving mode for latency, throughput and freshness needs. |
| S11E16 | Understand what dedicated serving platforms provide and when to use them. |
| S11E17 | Learn the Kubernetes concepts an ML engineer needs to run training and serving, without becoming a cluster administrator. |
| S11E18 | Reduce latency and cost of non-LLM models through export and runtime optimization. |
| S11E19 | Understand how models are adapted to run on phones, embedded devices and gateways, and how constraints change architecture and model choice. |
| S11E20 | Define what to measure so degradation is caught before users report it. |
| S11E21 | Detect and diagnose changes in data and relationships that degrade models. |
| S11E22 | Manage models across many remote devices: safe updates, telemetry under limited connectivity, and learning from distributed data without centralizing it. |
| S11E23 | Debug and resolve production ML incidents methodically. |
| S11E24 | Provide the evidence trail that regulated or high-risk ML systems require. |
| S11E25 | Decide how an organization provides MLOps capabilities to many teams. |
| S11E26 | Understand how cloud-managed ML platforms are structured, what they provide for each stage of the ML lifecycle, and how to decide between managed and self-managed infrastructure, using Amazon SageMaker, Google Vertex AI and Azure Machine Learning as examples of common patterns. |
| S11E27 | Integrate the season into a complete system design and walk through a change from commit to monitored production. |

## Prerequisites and Expected Knowledge

- **Season 1 — [Python for AI & ML Engineering](../season-01-python-for-ai-ml/roadmap.md)**: S01E08, S01E10, S01E11, S01E12, S01E13, S01E14, S01E16, S01E17
- **Season 2 — [Mathematics for AI & Machine Learning](../season-02-mathematics-for-ai/roadmap.md)**: S02E14
- **Season 3 — [Machine Learning Foundations](../season-03-machine-learning/roadmap.md)**: S03E18
- **Season 4 — [Advanced Machine Learning Engineering](../season-04-advanced-ml-engineering/roadmap.md)**: S04E03, S04E04, S04E15, S04E16, S04E21
- **Season 5 — [Deep Learning & Neural Networks](../season-05-deep-learning/roadmap.md)**: S05E10
- **Season 6 — [LLMs & Transformer Architecture](../season-06-llms-and-transformers/roadmap.md)**: S06E17

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [The ML Lifecycle and Reproducibility](#s11-module-1) | S11E01–S11E05 | 5 | 1 Foundational, 4 Intermediate |
| 2 | [Data and Feature Systems](#s11-module-2) | S11E06–S11E10 | 5 | 3 Intermediate, 2 Advanced |
| 3 | [Training Pipelines and CI/CD/CT](#s11-module-3) | S11E11–S11E14 | 4 | 3 Advanced, 1 Intermediate |
| 4 | [Model Serving](#s11-module-4) | S11E15–S11E19 | 5 | 2 Intermediate, 3 Advanced |
| 5 | [Monitoring, Governance, and Platforms](#s11-module-5) | S11E20–S11E27 | 8 | 2 Intermediate, 6 Advanced |

<a id="s11-module-1"></a>

## Module 1 — The ML Lifecycle and Reproducibility

**5 episodes (S11E01–S11E05) · 17 topics.** This module covers: The MLOps Lifecycle and Maturity Levels; Data Versioning and Lineage; Experiment Tracking; Model Registry, Versioning, and Promotion; Reproducible ML Environments.

| ID | Episode | Depth |
|---|---|---|
| S11E01 | The MLOps Lifecycle and Maturity Levels | Foundational |
| S11E02 | Data Versioning and Lineage | Intermediate |
| S11E03 | Experiment Tracking | Intermediate |
| S11E04 | Model Registry, Versioning, and Promotion | Intermediate |
| S11E05 | Reproducible ML Environments: Containers, Dependencies, and Hardware | Intermediate |

### S11E01 — The MLOps Lifecycle and Maturity Levels

**Depth:** Foundational  
**Learning objective:** Understand why ML systems fail in production differently from ordinary software and what MLOps adds.  
**Prerequisites:** S04E21, S03E18  
**Expected outcome:** Map a project to the lifecycle and identify its next automation step.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Why ML Is Different**

- Code, data and model as three moving parts
- Hidden technical debt in ML systems
- Training-serving gap and silent failures

**Topic 2 — The Lifecycle**

- Data, experimentation, training, validation, deployment, monitoring and retraining
- Roles: data scientist, ML engineer, platform, SRE

**Topic 3 — Maturity and Season Roadmap**

- Manual → automated pipeline → continuous training
- What to automate first
- Where each later episode fits
- Handoffs and ownership

</details>

**Important concepts**

- *Commands / APIs / Code:* lifecycle diagram; maturity checklist
- *Mechanisms & failure scenarios:* A model that cannot be reproduced, notebooks as production, no one owning a degraded model.

### S11E02 — Data Versioning and Lineage

**Depth:** Intermediate  
**Learning objective:** Make any trained model traceable to the exact data and code that produced it.  
**Prerequisites:** S01E13, S01E11  
**Expected outcome:** Design dataset versioning that ties every model to its data.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Why Version Data**

- Reproducibility and rollback
- Lineage as an audit requirement

**Topic 2 — Mechanisms**

- Content-addressed storage and pointer files (DVC-style)
- Table formats with time travel (lakehouse-style)
- Dataset manifests and hashes

**Topic 3 — Practice and Sensitive Data**

- Linking a dataset version to a training run
- Storage cost and retention
- Deletion requests and lineage
- Access control on datasets

</details>

**Important concepts**

- *Commands / APIs / Code:* `dvc add`, `dvc push`, `dvc repro` (concept), dataset hash manifest
- *Mechanisms & failure scenarios:* Unversioned data mutated in place, huge copies filling storage, lineage broken by manual file edits.

### S11E03 — Experiment Tracking

**Depth:** Intermediate  
**Learning objective:** Record parameters, metrics, artifacts and environment so experiments are comparable and reproducible.  
**Prerequisites:** S11E02, S04E03  
**Expected outcome:** Instrument training so any result can be traced and reproduced.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — What to Record**

- Parameters, metrics and artifacts
- Code commit, data version and environment

**Topic 2 — Tracking Architecture**

- Client, tracking server, artifact store and backend store
- Local vs remote tracking; access control

**Topic 3 — Using the Record and Pitfalls**

- Comparing and querying runs
- Reproducing a past run
- Metric overload and cherry-picking
- Metrics logged from different splits

</details>

**Important concepts**

- *Commands / APIs / Code:* `mlflow.start_run`, `log_param`, `log_metric`, `log_artifact` (concept)
- *Mechanisms & failure scenarios:* Missing commit hash making runs irreproducible, metrics logged from different splits, tracking server as single point of failure.

### S11E04 — Model Registry, Versioning, and Promotion

**Depth:** Intermediate  
**Learning objective:** Manage model versions as controlled artifacts with a promotion workflow.  
**Prerequisites:** S11E03  
**Expected outcome:** Design a promotion workflow with gates, approvals and rollback.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Registry Concepts**

- Model artifacts, signatures and metadata
- Versions and aliases/stages
- Lineage to runs and data

**Topic 2 — Promotion Workflow**

- Validation gates before promotion
- Approvals and audit; rollback

**Topic 3 — Integration**

- Serving systems pulling by alias
- Compatibility of model and feature versions

**Topic 4 — Documentation in the Registry**

- Model cards and intended-use statements
- Linking documentation to specific versions
- Risk labels and approval state in the registry

</details>

**Important concepts**

- *Commands / APIs / Code:* `register_model`, alias assignment, model loading by URI (concept)
- *Mechanisms & failure scenarios:* Deploying an unvalidated version, mutable aliases changing production unexpectedly, registry/serving version mismatch.

### S11E05 — Reproducible ML Environments: Containers, Dependencies, and Hardware

**Depth:** Intermediate  
**Learning objective:** Package training and serving environments so results do not depend on a machine.  
**Prerequisites:** S01E12, S01E17  
**Expected outcome:** Build a reproducible, GPU-capable image and explain its remaining nondeterminism.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Containers for ML**

- Images, layers and build caching
- Image size and dependency pinning

**Topic 2 — GPU Base Images**

- CUDA base images and driver/runtime compatibility
- Pinning CUDA and framework versions together
- Minimal runtime images for serving

**Topic 3 — Reproducibility Limits**

- Seeds, nondeterministic kernels and library versions
- Hardware differences; recording environment fingerprints

**Topic 4 — Build and Distribution**

- Multi-stage builds, registries and tags
- Training vs serving images
- Scanning and provenance (link to S14E07)

</details>

**Important concepts**

- *Commands / APIs / Code:* `docker build`, `docker run --gpus all`, Dockerfile for training (illustrative)
- *Mechanisms & failure scenarios:* Driver/CUDA mismatch, "latest" tags changing behavior, enormous images slowing deployment.

<a id="s11-module-2"></a>

## Module 2 — Data and Feature Systems

**5 episodes (S11E06–S11E10) · 22 topics.** This module covers: Data Pipelines and Orchestration; Data Validation and Data Contracts; Distributed Data Processing for ML; Streaming Systems for ML; Feature Stores.

| ID | Episode | Depth |
|---|---|---|
| S11E06 | Data Pipelines and Orchestration | Intermediate |
| S11E07 | Data Validation and Data Contracts | Intermediate |
| S11E08 | Distributed Data Processing for ML: Partitions, Shuffles, and Lakehouse Tables | Intermediate |
| S11E09 | Streaming Systems for ML: Event Logs, Event Time, and Real-Time Features | Advanced |
| S11E10 | Feature Stores: Offline/Online Consistency and Point-in-Time Correctness | Advanced |

### S11E06 — Data Pipelines and Orchestration

**Depth:** Intermediate  
**Learning objective:** Build reliable, re-runnable data workflows for ML.  
**Prerequisites:** S01E11, S11E02  
**Expected outcome:** Design an idempotent, observable data pipeline with defined backfill behavior.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Pipeline Concepts, Idempotency and Backfills**

- DAGs, tasks, dependencies and schedules
- Batch vs streaming ingestion
- Idempotent tasks and late data
- Backfill strategies

**Topic 2 — Orchestrators**

- Scheduler, workers and metadata database (Airflow-style)
- Retries, SLAs and alerting
- Sensors and event triggers

**Topic 3 — Reliability**

- Partitioned processing and failure isolation
- Cost and resource management

</details>

**Important concepts**

- *Commands / APIs / Code:* DAG definition (illustrative), backfill command (concept)
- *Mechanisms & failure scenarios:* Non-idempotent tasks duplicating data after a retry, silent upstream delays, backfills overwhelming sources.

### S11E07 — Data Validation and Data Contracts

**Depth:** Intermediate  
**Learning objective:** Stop bad data before it trains or serves a model.  
**Prerequisites:** S11E06, S01E08  
**Expected outcome:** Add validation gates and a data contract to an ML pipeline.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — What to Validate and Expectation Suites**

- Schema, ranges, null rates, distributions and freshness
- Training data vs serving data checks
- Writing and versioning data tests
- Where checks run: ingestion, pre-training and pre-serving
- Choosing thresholds from historical data

**Topic 2 — Contracts**

- Producer/consumer agreements and ownership
- Breaking vs compatible changes

**Topic 3 — Handling Failures**

- Fail, quarantine or alert
- Dead-letter data and reprocessing

</details>

**Important concepts**

- *Commands / APIs / Code:* validation expectations (Great Expectations-style, concept), schema check in a pipeline
- *Mechanisms & failure scenarios:* Checks too lax to catch drift, upstream schema change silently breaking features, alert fatigue.

### S11E08 — Distributed Data Processing for ML: Partitions, Shuffles, and Lakehouse Tables

**Depth:** Intermediate  
**Learning objective:** Understand how large datasets are processed across machines, why shuffles and skew dominate cost, and how table formats make data lakes reliable for ML.  
**Prerequisites:** S11E06, S01E11, S01E10  
**Expected outcome:** Reason about the cost of a distributed data job, spot skew and shuffle problems, and choose storage formats for ML data at scale.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Why Distribute**

- When a single machine stops being enough
- Data parallelism over partitions

**Topic 2 — Execution Model**

- Lazy evaluation, DAGs of stages and tasks
- Narrow vs wide transformations and the shuffle

**Topic 3 — Performance Problems**

- Data skew and stragglers
- Partition sizing, spill to disk and memory pressure
- Reading query plans

**Topic 4 — Lakehouse Table Formats**

- ACID tables over object storage
- Snapshots, time travel and schema evolution
- Compaction and small-file management

**Topic 5 — ML Workloads on Distributed Engines**

- Feature computation and training-set generation at scale
- Point-in-time joins over large tables
- Cost control and handoff to training

</details>

**Important concepts**

- *Commands / APIs / Code:* Spark-style DataFrame job and `explain()` plan (illustrative), repartition and salting for skew, Delta/Iceberg-style table time-travel query (concept)
- *Mechanisms & failure scenarios:* Skewed keys causing straggler tasks, small-file explosions, out-of-memory in shuffles, non-reproducible reads of mutable tables, expensive wide joins.

### S11E09 — Streaming Systems for ML: Event Logs, Event Time, and Real-Time Features

**Depth:** Advanced  
**Learning objective:** Understand how event streams carry data to ML systems, how time and ordering are handled, and how real-time features stay consistent with training data.  
**Prerequisites:** S11E08, S11E06  
**Expected outcome:** Design a streaming pipeline for real-time features with correct time semantics and defined delivery guarantees.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — The Log Abstraction**

- Topics, partitions and offsets
- Retention, compaction and replay

**Topic 2 — Producers and Consumers**

- Consumer groups and partition assignment
- Ordering guarantees and keys
- Consumer lag as a health signal

**Topic 3 — Time in Streams**

- Event time vs processing time
- Watermarks, late data and out-of-order events

**Topic 4 — Stream Processing**

- Windows (tumbling, sliding, session) and stateful aggregation
- State stores and checkpointing

**Topic 5 — Delivery Semantics**

- At-most-once, at-least-once and exactly-once claims
- Idempotent sinks and deduplication

**Topic 6 — Real-Time Features for ML**

- Online feature computation and freshness
- Keeping batch and streaming logic consistent
- Backpressure, scaling and failure recovery

</details>

**Important concepts**

- *Commands / APIs / Code:* Producer and consumer-group sketch (Kafka-style concept), windowed aggregation with watermark (illustrative), replay from an offset
- *Mechanisms & failure scenarios:* Late and out-of-order events producing wrong aggregates, consumer lag, duplicate processing under at-least-once delivery, training-serving skew between batch and stream feature logic, hot partitions.

### S11E10 — Feature Stores: Offline/Online Consistency and Point-in-Time Correctness

**Depth:** Advanced  
**Learning objective:** Understand why features are managed centrally and how training-serving skew is prevented.  
**Prerequisites:** S11E06, S11E09, S04E04  
**Expected outcome:** Decide whether a feature store is warranted and design for point-in-time correctness.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Problem**

- Duplicate feature logic in training and serving
- Skew and leakage; reuse across models

**Topic 2 — Architecture**

- Feature definitions, offline store, online store and registry
- Materialization and freshness

**Topic 3 — Point-in-Time Correctness**

- Point-in-time joins and label timestamps
- Backfills and versioning

**Topic 4 — Streaming and Online Features**

- Streaming ingestion into the online store (link to S11E09)
- Latency, cost and consistency

**Topic 5 — When a Feature Store Is Overkill**

- Decision criteria and lighter alternatives
- Decision criteria: number of models, team size and need for online features
- Lighter alternatives: shared feature libraries and materialized tables
- Migration path as needs grow

</details>

**Important concepts**

- *Commands / APIs / Code:* feature view definition and `get_historical_features` / `get_online_features` (Feast-style concept)
- *Mechanisms & failure scenarios:* Stale online features, joins leaking future data, features changed without versioning.

<a id="s11-module-3"></a>

## Module 3 — Training Pipelines and CI/CD/CT

**4 episodes (S11E11–S11E14) · 13 topics.** This module covers: Training Pipelines and ML Workflow Orchestration; CI for ML; CD for ML; Continuous Training.

| ID | Episode | Depth |
|---|---|---|
| S11E11 | Training Pipelines and ML Workflow Orchestration | Advanced |
| S11E12 | CI for ML: Testing Data, Code, and Models | Intermediate |
| S11E13 | CD for ML: Deployment Strategies, Canary, Shadow, and Rollback | Advanced |
| S11E14 | Continuous Training: Triggers, Retraining Policies, and Safe Automation | Advanced |

### S11E11 — Training Pipelines and ML Workflow Orchestration

**Depth:** Advanced  
**Learning objective:** Turn experiments into reproducible, parameterized, cacheable pipelines.  
**Prerequisites:** S11E06, S11E04, S11E05  
**Expected outcome:** Specify a parameterized, cacheable training pipeline with clear failure behavior.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Pipeline Design**

- Steps: ingest, validate, featurize, train, evaluate, register
- Artifacts and caching between steps
- Parameterization and configuration

**Topic 2 — Execution Platforms**

- Kubernetes-based pipeline engines (Kubeflow/Argo-style) and general orchestrators
- Resource requests, GPUs and retries

**Topic 3 — Triggers**

- Schedule, event and data-change triggers
- Dependency-aware triggering of downstream steps
- Avoiding trigger storms

**Topic 4 — Reliability**

- Idempotent steps and step-level caching
- Failure recovery and resumption
- Cached steps masking changed inputs; cost control

</details>

**Important concepts**

- *Commands / APIs / Code:* pipeline definition (illustrative), parameterized run submission (concept)
- *Mechanisms & failure scenarios:* Cached steps masking changed inputs, GPU jobs stuck pending, non-deterministic steps breaking reproducibility.

### S11E12 — CI for ML: Testing Data, Code, and Models

**Depth:** Intermediate  
**Learning objective:** Define what "continuous integration" means when the artifact is a model.  
**Prerequisites:** S01E14, S11E11  
**Expected outcome:** Design a CI pipeline for an ML repository with meaningful automated gates.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Layers of Testing**

- Code unit tests, data tests and training smoke tests
- Overfit-a-tiny-batch and reproducibility checks
- Test ownership across data and model code

**Topic 2 — Model Behavior Tests**

- Invariance, directional and slice tests
- Performance and fairness thresholds

**Topic 3 — The CI Pipeline, Gates, and Reporting**

- Triggers, runners and caching
- Time and cost budgets for ML tests
- Baseline comparison and regression thresholds
- Blocking vs advisory checks; results in pull requests

</details>

**Important concepts**

- *Commands / APIs / Code:* pytest model tests, CI workflow file (illustrative), baseline-comparison script
- *Mechanisms & failure scenarios:* Flaky model tests from randomness, CI too slow so it's bypassed, thresholds that do not reflect user impact.

### S11E13 — CD for ML: Deployment Strategies, Canary, Shadow, and Rollback

**Depth:** Advanced  
**Learning objective:** Release models safely and recover quickly.  
**Prerequisites:** S11E12, S04E16  
**Expected outcome:** Choose and implement a release strategy with explicit rollback criteria.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Release Strategies and Batch Releases**

- Blue-green, canary, shadow and A/B
- Traffic splitting and metrics comparison
- Releasing batch-scored models safely
- Double-running old and new models and backfilling
- Reconciling downstream consumers of batch outputs

**Topic 2 — Promotion Automation**

- Registry-driven deployment
- Config as code and GitOps for model releases

**Topic 3 — Rollback**

- What must roll back together (model, features, code)
- Automated rollback triggers; canaries lacking ground truth

</details>

**Important concepts**

- *Commands / APIs / Code:* canary traffic split (illustrative), rollback procedure
- *Mechanisms & failure scenarios:* Canary lacking ground truth, rollback blocked by schema changes, serving version incompatible with feature version.

### S11E14 — Continuous Training: Triggers, Retraining Policies, and Safe Automation

**Depth:** Advanced  
**Learning objective:** Decide when and how a model retrains itself without creating new risks.  
**Prerequisites:** S11E13, S11E07  
**Expected outcome:** Define a retraining policy with triggers, gates and fallbacks.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Triggers**

- Scheduled, drift-triggered, performance-triggered and data-volume triggers
- Label delay and its implications

**Topic 2 — Automated Retraining Pipeline**

- Training on fresh data windows
- Champion/challenger evaluation against the production baseline

**Topic 3 — Promotion Policy and Risks**

- Human approval vs automatic promotion
- Cost-benefit of retraining frequency
- Feedback loops and poisoned data
- Training on model-influenced labels; silent degradation from automation

</details>

**Important concepts**

- *Commands / APIs / Code:* trigger rules configuration (concept), champion/challenger comparison
- *Mechanisms & failure scenarios:* Auto-retraining on corrupted data, challenger beating champion on stale validation, retraining cost exceeding value.

<a id="s11-module-4"></a>

## Module 4 — Model Serving

**5 episodes (S11E15–S11E19) · 18 topics.** This module covers: Model Serving Patterns; Model Serving Platforms; Kubernetes for ML Workloads; Model Optimization for Serving; Edge and On-Device Inference.

| ID | Episode | Depth |
|---|---|---|
| S11E15 | Model Serving Patterns: Batch, Online, and Streaming Inference | Intermediate |
| S11E16 | Model Serving Platforms: KServe, Triton, and BentoML Patterns | Advanced |
| S11E17 | Kubernetes for ML Workloads: Jobs, Deployments, Storage, and Scheduling | Intermediate |
| S11E18 | Model Optimization for Serving: ONNX, Compilation, and Quantization | Advanced |
| S11E19 | Edge and On-Device Inference: Constraints, Compression, and Runtimes | Advanced |

### S11E15 — Model Serving Patterns: Batch, Online, and Streaming Inference

**Depth:** Intermediate  
**Learning objective:** Choose the right serving mode for latency, throughput and freshness needs.  
**Prerequisites:** S11E10, S01E16  
**Expected outcome:** Select a serving pattern and justify it with latency and freshness requirements.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Patterns**

- Batch scoring, real-time APIs, streaming inference
- Precompute vs compute-on-request

**Topic 2 — Performance**

- Latency vs throughput, batching and concurrency
- Cold starts and model loading

**Topic 3 — Integration and Resilience**

- Feature access at inference time
- Input validation and schema enforcement
- Fallback predictions and timeouts
- Caching predictions

</details>

**Important concepts**

- *Commands / APIs / Code:* batch scoring job, online API with FastAPI (link to S01E16)
- *Mechanisms & failure scenarios:* Online feature fetches dominating latency, batch results stale by the time of use, cold-start spikes.

### S11E16 — Model Serving Platforms: KServe, Triton, and BentoML Patterns

**Depth:** Advanced  
**Learning objective:** Understand what dedicated serving platforms provide and when to use them.  
**Prerequisites:** S11E15, S11E13  
**Expected outcome:** Pick between a custom service and a serving platform for a workload.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Platform Capabilities**

- Model repositories and multi-framework serving
- Dynamic batching, concurrency and versioning

**Topic 2 — Inference Graphs**

- Pre- and post-processing pipelines
- Ensembles and multi-model serving

**Topic 3 — Kubernetes-Native Serving and Choosing**

- Inference services as custom resources
- Autoscaling, scale-to-zero and canary rollouts; GPU sharing
- Custom API vs platform
- Operational burden, observability and metrics

</details>

**Important concepts**

- *Commands / APIs / Code:* inference-service manifest (illustrative), Triton model repository layout (concept)
- *Mechanisms & failure scenarios:* Cold start from scale-to-zero, batching delay violating latency SLOs, model repository drift from registry.

### S11E17 — Kubernetes for ML Workloads: Jobs, Deployments, Storage, and Scheduling

**Depth:** Intermediate  
**Learning objective:** Learn the Kubernetes concepts an ML engineer needs to run training and serving, without becoming a cluster administrator.  
**Prerequisites:** S01E17, S11E05  
**Expected outcome:** Read and write basic manifests for an ML job and a model server and diagnose common failures.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Core Objects**

- Pods, Deployments, Services, Jobs and CronJobs
- ConfigMaps and Secrets
- Resource requests and limits

**Topic 2 — Storage, Scheduling, and Health for ML**

- Persistent volumes for datasets and checkpoints
- Node selectors, taints and tolerations for GPU nodes
- Probes and graceful shutdown for model servers

**Topic 3 — Debugging**

- Reading pod status and events
- OOMKilled, Pending and CrashLoopBackOff; logs and exec

</details>

**Important concepts**

- *Commands / APIs / Code:* `kubectl get/describe/logs`, Job manifest requesting a GPU (illustrative)
- *Mechanisms & failure scenarios:* Pods Pending for lack of GPU capacity, OOM kills of large models, readiness probe passing before the model is loaded.

### S11E18 — Model Optimization for Serving: ONNX, Compilation, and Quantization

**Depth:** Advanced  
**Learning objective:** Reduce latency and cost of non-LLM models through export and runtime optimization.  
**Prerequisites:** S11E15, S06E17  
**Expected outcome:** Export and optimize a model with measured, validated speedups.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Portable Formats**

- ONNX export and operator support
- Safe vs unsafe serialization (pickle)

**Topic 2 — Runtime Optimization**

- Graph optimization and operator fusion
- Hardware-specific compilers and runtimes

**Topic 3 — Quantization for Classical and Vision Models**

- Post-training and quantization-aware approaches
- Calibration data and accuracy checks for vision models
- INT8 on CPUs and GPUs and supported operators

**Topic 4 — Validation**

- Numerical parity tests
- Benchmarking methodology (warm-up, batching)
- Accuracy vs latency trade-offs

</details>

**Important concepts**

- *Commands / APIs / Code:* `torch.onnx.export`, ONNX Runtime session (concept), benchmark harness
- *Mechanisms & failure scenarios:* Unsupported operators, silent numerical divergence after export, benchmarks that ignore batching and warm-up.

### S11E19 — Edge and On-Device Inference: Constraints, Compression, and Runtimes

**Depth:** Advanced  
**Learning objective:** Understand how models are adapted to run on phones, embedded devices and gateways, and how constraints change architecture and model choice.  
**Prerequisites:** S11E18, S06E17, S05E10  
**Expected outcome:** Select a model, compression approach and runtime for an edge target and verify it against latency, memory and energy budgets.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Why and When Edge**

- Latency, privacy, connectivity and cost drivers
- Cloud, edge and hybrid splits

**Topic 2 — Device Constraints**

- Memory, compute, power and thermal limits
- CPUs, GPUs and NPUs/DSPs on devices

**Topic 3 — Making Models Small**

- Quantization, pruning and distillation for edge
- Efficient architectures for mobile
- Small language and vision models on device

**Topic 4 — Runtimes and Deployment Formats**

- Mobile and embedded inference runtimes (concept)
- Operator support and delegates to accelerators

**Topic 5 — Measuring on Real Hardware**

- Benchmarking latency, memory and energy
- Simulators vs physical devices

</details>

**Important concepts**

- *Commands / APIs / Code:* Model export and quantization for an edge runtime (illustrative), on-device benchmark harness, latency/energy measurement approach
- *Mechanisms & failure scenarios:* Models that fit but run too slowly or hot, unsupported operators on target accelerators, accuracy drop after aggressive quantization, differing preprocessing on device, thermal throttling.

<a id="s11-module-5"></a>

## Module 5 — Monitoring, Governance, and Platforms

**8 episodes (S11E20–S11E27) · 34 topics.** This module covers: Monitoring ML Systems; Drift Detection and Training-Serving Skew; Operating Edge AI Fleets; Observability and Incident Response for ML Systems; Model Governance; ML Platform Patterns; Managed ML Platforms; End-to-End MLOps Reference Architecture.

| ID | Episode | Depth |
|---|---|---|
| S11E20 | Monitoring ML Systems: Service, Data, and Model Metrics | Intermediate |
| S11E21 | Drift Detection and Training-Serving Skew | Advanced |
| S11E22 | Operating Edge AI Fleets: Updates, Monitoring, and Federated Learning | Advanced |
| S11E23 | Observability and Incident Response for ML Systems | Advanced |
| S11E24 | Model Governance: Lineage, Documentation, and Audit | Intermediate |
| S11E25 | ML Platform Patterns: Build vs Buy, Self-Service, and Team Topologies | Advanced |
| S11E26 | Managed ML Platforms: Architecture, Capabilities, and Managed vs Self-Managed Trade-offs | Advanced |
| S11E27 | End-to-End MLOps Reference Architecture | Advanced |

### S11E20 — Monitoring ML Systems: Service, Data, and Model Metrics

**Depth:** Intermediate  
**Learning objective:** Define what to measure so degradation is caught before users report it.  
**Prerequisites:** S11E15  
**Expected outcome:** Define a monitoring plan covering service, data and model signals.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Three Layers**

- Service health: latency, errors and saturation
- Data health: schema, freshness and distributions
- Model health: prediction distributions and accuracy when labels arrive

**Topic 2 — Delayed Ground Truth**

- Proxy metrics and label delay
- Sampling and human labeling for monitoring

**Topic 3 — Dashboards and Alerts**

- SLOs for ML services
- Alert thresholds, noise and runbooks

</details>

**Important concepts**

- *Commands / APIs / Code:* Prometheus-style metrics from a model server (concept), prediction-logging schema
- *Mechanisms & failure scenarios:* Healthy service returning garbage, no labels so no accuracy signal, alert fatigue.

### S11E21 — Drift Detection and Training-Serving Skew

**Depth:** Advanced  
**Learning objective:** Detect and diagnose changes in data and relationships that degrade models.  
**Prerequisites:** S11E20, S02E14  
**Expected outcome:** Implement drift checks and a decision procedure for responding to them.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Kinds of Change**

- Covariate shift, label shift and concept drift
- Training-serving skew vs drift
- Seasonality vs real drift

**Topic 2 — Detection Statistics**

- PSI, KS test and divergence measures
- Windowing and reference choice

**Topic 3 — Multivariate and Embedding Drift**

- Drift in feature interactions and embeddings
- Why univariate tests miss joint changes
- Domain-classifier drift detection

**Topic 4 — Response**

- Diagnosis: data, feature or model
- Retrain, roll back or accept
- Avoiding alarms on benign shifts

</details>

**Important concepts**

- *Commands / APIs / Code:* PSI and KS computation, drift report (concept)
- *Mechanisms & failure scenarios:* Statistical significance without practical impact, drift on irrelevant features triggering retrains, drift hidden in feature interactions.

### S11E22 — Operating Edge AI Fleets: Updates, Monitoring, and Federated Learning

**Depth:** Advanced  
**Learning objective:** Manage models across many remote devices: safe updates, telemetry under limited connectivity, and learning from distributed data without centralizing it.  
**Prerequisites:** S11E19, S11E13, S11E20, S11E21  
**Expected outcome:** Design an update, monitoring and (where appropriate) federated-learning strategy for an edge fleet.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Fleet Model Management**

- Device registries and model versions per device
- Compatibility between model, runtime and hardware

**Topic 2 — Safe Updates**

- Over-the-air rollouts, staged deployment and rollback
- Delta updates and bandwidth limits

**Topic 3 — Monitoring Under Constraints**

- Sparse and delayed telemetry
- On-device quality and drift signals

**Topic 4 — Federated and On-Device Learning**

- Federated averaging and its assumptions
- Non-IID data, communication cost and privacy protections (concept)

**Topic 5 — Security of Edge Models**

- Model theft and tampering
- Secure boot, signing and attestation at overview level

</details>

**Important concepts**

- *Commands / APIs / Code:* Staged OTA rollout configuration (illustrative), on-device telemetry schema, federated averaging round (concept)
- *Mechanisms & failure scenarios:* Bricked devices from a bad update, devices stuck on old model versions, telemetry too sparse to detect drift, biased federated clients, privacy leakage from model updates.

### S11E23 — Observability and Incident Response for ML Systems

**Depth:** Advanced  
**Learning objective:** Debug and resolve production ML incidents methodically.  
**Prerequisites:** S11E21, S11E13  
**Expected outcome:** Run an ML incident from alert to postmortem with versioned evidence.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Telemetry**

- Logs, traces and metrics with model and data version tags
- Prediction and input logging with privacy controls

**Topic 2 — Reproducing Problems**

- Reproducing a bad prediction from versioned evidence
- Capturing inputs, features and model version per request
- Recomputing features at the prediction timestamp

**Topic 3 — Incident Process**

- Severity, roles and communication
- Triage: data, features, model, infrastructure
- Mitigation: fallback, rollback, disable

**Topic 4 — Learning**

- Blameless postmortems
- Adding tests and monitors after incidents; runbooks

</details>

**Important concepts**

- *Commands / APIs / Code:* trace/log correlation by model version, runbook template
- *Mechanisms & failure scenarios:* Cannot tell which model version served a request, logs lacking inputs, fixes without regression tests.

### S11E24 — Model Governance: Lineage, Documentation, and Audit

**Depth:** Intermediate  
**Learning objective:** Provide the evidence trail that regulated or high-risk ML systems require.  
**Prerequisites:** S11E04, S04E15  
**Expected outcome:** Produce governance artifacts and a traceable release record.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Documentation**

- Model cards, dataset documentation and intended use
- Risk classification and change logs

**Topic 2 — Lineage and Audit**

- End-to-end traceability from prediction to data
- Approvals, retention and access control

**Topic 3 — Process**

- Review boards and release criteria
- Third-party and open-model due diligence
- Link to responsible AI (Season 14)

</details>

**Important concepts**

- *Commands / APIs / Code:* model-card template, audit-record schema
- *Mechanisms & failure scenarios:* Documentation drifting from the deployed model, missing approval evidence, unclear intended-use boundaries.

### S11E25 — ML Platform Patterns: Build vs Buy, Self-Service, and Team Topologies

**Depth:** Advanced  
**Learning objective:** Decide how an organization provides MLOps capabilities to many teams.  
**Prerequisites:** S11E24, S11E16  
**Expected outcome:** Make a reasoned build/buy decision for an ML platform.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Platform Capabilities**

- Experimentation, pipelines, registry, serving and monitoring as a product
- Self-service and golden paths

**Topic 2 — Multi-Tenancy**

- Isolation, quotas and cost attribution
- Fair sharing of GPUs and pipeline capacity
- Per-team environments and access boundaries

**Topic 3 — Build vs Buy vs Compose**

- Managed cloud ML platforms vs open-source stacks
- Integration and lock-in
- Team size and maturity

**Topic 4 — Adoption**

- Platform as product: users, metrics and support
- Standardization vs flexibility

</details>

**Important concepts**

- *Commands / APIs / Code:* capability matrix, decision worksheet
- *Mechanisms & failure scenarios:* Platform nobody adopts, over-standardization blocking research, hidden operational load of self-hosting.

### S11E26 — Managed ML Platforms: Architecture, Capabilities, and Managed vs Self-Managed Trade-offs

**Depth:** Advanced  
**Learning objective:** Understand how cloud-managed ML platforms are structured, what they provide for each stage of the ML lifecycle, and how to decide between managed and self-managed infrastructure, using Amazon SageMaker, Google Vertex AI and Azure Machine Learning as examples of common patterns.  
**Prerequisites:** S11E03, S11E04, S11E10, S11E16, S11E21, S11E25  
**Expected outcome:** Map the stages of the ML lifecycle to managed platform capabilities, compare platforms on architecture rather than branding, and make a justified managed vs self-managed decision.

<details>
<summary>Topics and subtopics (7 topics)</summary>

**Topic 1 — Managed Platform Architecture**

- Control plane vs data plane and the resource model (workspaces or projects, compute targets, storage, identity, networking)
- Common abstractions across SageMaker, Vertex AI and Azure Machine Learning
- Where managed platforms sit relative to the open-source stack from earlier episodes

**Topic 2 — Training Jobs**

- The job abstraction: container or script, data location, compute and hyperparameters
- Managed clusters, spot or preemptible capacity and distributed training support
- Managed hyperparameter tuning and pipeline orchestration
- Failure modes: quota limits, start-up latency, data egress cost and environment drift

**Topic 3 — Experiment Tracking and Model Registry**

- Managed tracking and lineage
- Registry versions, stages and approval workflows
- Integration with CI/CD and portability through open formats and tracking APIs

**Topic 4 — Feature Stores and Data Integration**

- Managed offline and online stores and ties to warehouses and lakes
- Point-in-time correctness and freshness guarantees
- Limits and lock-in risks

**Topic 5 — Model Deployment**

- Endpoint types: real-time, serverless, asynchronous and batch
- Autoscaling, traffic splitting, multi-model hosting and GPU endpoints
- Cold starts, pricing models and deployment safety

**Topic 6 — Model Monitoring and Governance**

- Data-quality, drift and model-quality monitoring
- Explainability and bias reports as platform features
- Audit logs, access control and private networking

**Topic 7 — Managed vs Self-Managed**

- Decision factors: team size, compliance, customization, scale and cost model
- Cost behavior: idle capacity, premiums over raw compute and egress
- Portability strategies: containers, open model formats, open tracking and orchestration standards
- Hybrid designs and how to read vendor claims (all product behavior is version-sensitive and verified at scripting time)

</details>

**Important concepts**

- *Commands / APIs / Code:* Provider-neutral training-job and endpoint definitions (illustrative; product-specific syntax verified at scripting time), capability comparison matrix
- *Mechanisms & failure scenarios:* Quota exhaustion at launch, hidden idle endpoint cost, platform features that do not integrate with existing CI/CD, lock-in through proprietary pipeline formats, monitoring defaults that do not match the use case, region or model availability gaps.

### S11E27 — End-to-End MLOps Reference Architecture

**Depth:** Advanced  
**Learning objective:** Integrate the season into a complete system design and walk through a change from commit to monitored production.  
**Prerequisites:** S11E25, S11E23, S11E14  
**Expected outcome:** Present and defend an end-to-end MLOps architecture sized to a given organization.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Architecture**

- Data, features, training, registry, serving and monitoring
- CI/CD/CT flows
- Governance and security touchpoints

**Topic 2 — Walkthrough: A Code Change**

- Where each gate acts, from commit to monitored production
- Tests, evaluation gate, registry promotion and canary in sequence
- Evidence generated at each stage

**Topic 3 — Walkthrough: A Data Change and a Drift-Triggered Retrain**

- What gets versioned and what rolls back
- Data validation → retrain → champion/challenger → promotion
- Failure paths: bad data, failed gate and canary regression

**Topic 4 — Trade-offs and Next Steps**

- Right-sizing for team and scale
- Failure scenarios and recovery
- Bridge to LLMOps (Season 12) and AI infrastructure (Season 13)

</details>

**Important concepts**

- *Commands / APIs / Code:* architecture diagram and trace of a release through the system
- *Mechanisms & failure scenarios:* Gates configured but not enforced, lineage gaps at integration points, over-engineered pipelines for small teams.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s11-module-1) | Starting point of the season |
| [Module 2](#s11-module-2) | [Module 1](#s11-module-1) (S11E02) |
| [Module 3](#s11-module-3) | [Module 1](#s11-module-1) (S11E04, S11E05); [Module 2](#s11-module-2) (S11E06, S11E07) |
| [Module 4](#s11-module-4) | [Module 1](#s11-module-1) (S11E05); [Module 2](#s11-module-2) (S11E10); [Module 3](#s11-module-3) (S11E13) |
| [Module 5](#s11-module-5) | [Module 1](#s11-module-1) (S11E03, S11E04); [Module 2](#s11-module-2) (S11E10); [Module 3](#s11-module-3) (S11E13, S11E14); [Module 4](#s11-module-4) (S11E15, S11E16, S11E19) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 10 — Advanced Agentic AI](../season-10-advanced-agentic-ai/roadmap.md)
- **Next:** [Season 12 — LLMOps Engineering](../season-12-llmops-engineering/roadmap.md)
- **Draws on:** [Season 1](../season-01-python-for-ai-ml/roadmap.md) (S01E08, S01E10, S01E11, S01E12, S01E13, S01E14, S01E16, S01E17); [Season 2](../season-02-mathematics-for-ai/roadmap.md) (S02E14); [Season 3](../season-03-machine-learning/roadmap.md) (S03E18); [Season 4](../season-04-advanced-ml-engineering/roadmap.md) (S04E03, S04E04, S04E15, S04E16, S04E21); [Season 5](../season-05-deep-learning/roadmap.md) (S05E10); [Season 6](../season-06-llms-and-transformers/roadmap.md) (S06E17)
- **Required by:** [Season 12](../season-12-llmops-engineering/roadmap.md) (via S11E04, S11E11, S11E13, S11E21, S11E27); [Season 13](../season-13-ai-infrastructure/roadmap.md) (via S11E04, S11E05, S11E17, S11E20, S11E25, S11E26); [Season 14](../season-14-production-ai-systems/roadmap.md) (via S11E04, S11E20, S11E23, S11E24, S11E27); [Season 15](../season-15-ai-for-devops/roadmap.md) (via S11E13, S11E17)
