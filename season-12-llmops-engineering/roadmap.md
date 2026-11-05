# Season 12 Roadmap — LLMOps Engineering

[← Season 12 overview](README.md) · [All seasons](../README.md)

**5 modules · 18 episodes · 65 topics · 174 subtopics · Level: Advanced**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — The LLM System Lifecycle](#s12-module-1)
- [Module 2 — Evaluation Engineering](#s12-module-2)
- [Module 3 — Observability and Quality Monitoring](#s12-module-3)
- [Module 4 — Gateways, Safety, and Compliance](#s12-module-4)
- [Module 5 — Optimization and Delivery](#s12-module-5)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Teach how LLM-based systems are versioned, evaluated, observed, secured, optimized and released at production quality. It extends Season 11 to the parts that change with generative systems: prompts as artifacts, probabilistic outputs, token economics, and multi-component systems (retrieval, tools, agents).

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S12E01 | Identify which MLOps practices carry over and which must be rethought for LLM applications. |
| S12E02 | Treat prompts as versioned, testable, deployable artifacts. |
| S12E03 | Make an LLM application reproducible despite many interacting components. |
| S12E04 | Build and maintain datasets that represent the product's real quality bar. |
| S12E05 | Score open-ended outputs reliably and know the measurement error. |
| S12E06 | Automate evaluation so every change to prompts, models, retrieval or tools is tested before release. |
| S12E07 | Learn from production usage while protecting users and privacy. |
| S12E08 | Capture enough structure to debug any request end to end. |
| S12E09 | Attribute spend and delay to features, tenants and components. |
| S12E10 | Detect quality degradation when there is no single accuracy number. |
| S12E11 | Centralize model access with consistent security, reliability and cost controls. |
| S12E12 | Verify, rather than assume, that safety controls work. |
| S12E13 | Operationalize defenses and detection for injection and misuse. |
| S12E14 | Handle sensitive data across prompts, logs, vendors and training pipelines. |
| S12E15 | Operationalize fine-tuning as a repeatable, evaluated, governed pipeline. |
| S12E16 | Reduce cost and latency across hosted and self-hosted LLMs without losing quality. |
| S12E17 | Ship changes to prompts, models, retrieval and tools with the same safety as code. |
| S12E18 | See the whole LLMOps stack operating, including how a real class of incident is detected, diagnosed and prevented. |

## Prerequisites and Expected Knowledge

- **Season 2 — [Mathematics for AI & Machine Learning](../season-02-mathematics-for-ai/roadmap.md)**: S02E14
- **Season 4 — [Advanced Machine Learning Engineering](../season-04-advanced-ml-engineering/roadmap.md)**: S04E16, S04E19
- **Season 6 — [LLMs & Transformer Architecture](../season-06-llms-and-transformers/roadmap.md)**: S06E13, S06E15, S06E17, S06E22
- **Season 7 — [Generative AI Application Engineering](../season-07-generative-ai-engineering/roadmap.md)**: S07E02, S07E08, S07E09, S07E14, S07E19, S07E20, S07E21
- **Season 8 — [RAG Engineering](../season-08-rag-engineering/roadmap.md)**: S08E15
- **Season 9 — [AI Agents, Tool Calling & MCP](../season-09-ai-agents-and-mcp/roadmap.md)**: S09E12, S09E13, S09E14
- **Season 11 — [MLOps Engineering](../season-11-mlops-engineering/roadmap.md)**: S11E04, S11E11, S11E13, S11E21, S11E27

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [The LLM System Lifecycle](#s12-module-1) | S12E01–S12E03 | 3 | 2 Intermediate, 1 Advanced |
| 2 | [Evaluation Engineering](#s12-module-2) | S12E04–S12E07 | 4 | 1 Intermediate, 3 Advanced |
| 3 | [Observability and Quality Monitoring](#s12-module-3) | S12E08–S12E10 | 3 | 2 Intermediate, 1 Advanced |
| 4 | [Gateways, Safety, and Compliance](#s12-module-4) | S12E11–S12E14 | 4 | 3 Advanced, 1 Intermediate |
| 5 | [Optimization and Delivery](#s12-module-5) | S12E15–S12E18 | 4 | 4 Advanced |

<a id="s12-module-1"></a>

## Module 1 — The LLM System Lifecycle

**3 episodes (S12E01–S12E03) · 10 topics.** This module covers: LLMOps vs MLOps; Prompt Management and Versioning; Versioning the Whole LLM System.

| ID | Episode | Depth |
|---|---|---|
| S12E01 | LLMOps vs MLOps: What Changes for Generative Systems | Intermediate |
| S12E02 | Prompt Management and Versioning | Intermediate |
| S12E03 | Versioning the Whole LLM System: Prompts, Models, Retrievers, Tools, and Config | Advanced |

### S12E01 — LLMOps vs MLOps: What Changes for Generative Systems

**Depth:** Intermediate  
**Learning objective:** Identify which MLOps practices carry over and which must be rethought for LLM applications.  
**Prerequisites:** S11E27, S07E21  
**Expected outcome:** Map an LLM application to a lifecycle and list the controls it needs.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — What Carries Over from MLOps**

- Versioning, CI/CD, monitoring and governance
- Registries, promotion and platform patterns

**Topic 2 — What Is Different**

- Prompts and configurations as primary "code"
- Open-ended outputs and subjective quality
- External model dependencies that change underneath you
- Token-based cost and latency

**Topic 3 — The LLM Application Lifecycle**

- Prototype → evaluate → harden → release → observe → improve
- Roles and ownership

**Topic 4 — Season Roadmap**

- Where each later episode fits
- Failure examples: silent provider updates and untested prompt edits

</details>

**Important concepts**

- *Commands / APIs / Code:* lifecycle diagram; comparison table
- *Mechanisms & failure scenarios:* Provider model update silently changing behavior, prompt edits shipped without tests, quality regressions invisible to infrastructure metrics.

### S12E02 — Prompt Management and Versioning

**Depth:** Intermediate  
**Learning objective:** Treat prompts as versioned, testable, deployable artifacts.  
**Prerequisites:** S12E01, S07E02  
**Expected outcome:** Design a prompt versioning and release workflow.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Prompts as Artifacts**

- Templates, variables, system prompts and few-shot sets
- Storing in code vs a prompt registry

**Topic 2 — Environments and Release Channels**

- Development, staging and production prompts
- Runtime retrieval vs build-time embedding

**Topic 3 — Change Management and Operations**

- Review and diff of prompt changes
- Linking prompt versions to evaluation results; rollback
- Caching and latency of prompt fetch
- Access control and audit

</details>

**Important concepts**

- *Commands / APIs / Code:* prompt file with metadata and version, registry fetch (concept)
- *Mechanisms & failure scenarios:* Prompt hot-edited in production without evaluation, prompt/model version mismatch, untracked prompt differences between environments.

### S12E03 — Versioning the Whole LLM System: Prompts, Models, Retrievers, Tools, and Config

**Depth:** Advanced  
**Learning objective:** Make an LLM application reproducible despite many interacting components.  
**Prerequisites:** S12E02, S11E04  
**Expected outcome:** Define a release manifest and a rollback procedure for a multi-component LLM application.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — The Bill of Materials**

- Model ID/version, prompts, retrieval config, embeddings, tools, guardrails and parameters
- Provider model aliases vs pinned versions
- Index and data versions

**Topic 2 — Release Units**

- Bundling components into a versioned release
- Compatibility between components; configuration as code

**Topic 3 — Reproduction, Rollback, and Its Limits**

- Recording versions with every trace
- Replaying a request against a past release
- Nondeterminism and provider changes
- Embedding upgrades without re-indexing

</details>

**Important concepts**

- *Commands / APIs / Code:* release manifest (YAML) with pinned components (illustrative)
- *Mechanisms & failure scenarios:* Embedding model upgraded without re-indexing, tools updated but prompts not, "latest" alias shifting behavior.

<a id="s12-module-2"></a>

## Module 2 — Evaluation Engineering

**4 episodes (S12E04–S12E07) · 14 topics.** This module covers: Evaluation Datasets and Golden Sets; Metrics, Rubrics, and LLM-as-Judge Done Right; Evaluating RAG and Agent Systems in CI; Online Evaluation and Feedback Loops.

| ID | Episode | Depth |
|---|---|---|
| S12E04 | Evaluation Datasets and Golden Sets | Intermediate |
| S12E05 | Metrics, Rubrics, and LLM-as-Judge Done Right | Advanced |
| S12E06 | Evaluating RAG and Agent Systems in CI: Regression Gates | Advanced |
| S12E07 | Online Evaluation and Feedback Loops | Advanced |

### S12E04 — Evaluation Datasets and Golden Sets

**Depth:** Intermediate  
**Learning objective:** Build and maintain datasets that represent the product's real quality bar.  
**Prerequisites:** S07E19, S04E19  
**Expected outcome:** Create a governed evaluation dataset with coverage targets and a refresh process.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Sources**

- Production sampling, expert-written cases and synthetic generation
- Edge cases, adversarial cases and safety cases

**Topic 2 — Coverage**

- Coverage by task and user segment
- Size vs statistical power

**Topic 3 — Quality and Maintenance**

- Labeling guidelines and agreement
- Avoiding contamination with few-shot examples and training data
- Versioning evaluation sets
- Refreshing with new failure cases; privacy handling of real traffic

</details>

**Important concepts**

- *Commands / APIs / Code:* evaluation set schema (JSONL) with tags and expected behavior
- *Mechanisms & failure scenarios:* Evaluation set biased toward easy cases, leakage into prompts, stale sets missing new failure modes.

### S12E05 — Metrics, Rubrics, and LLM-as-Judge Done Right

**Depth:** Advanced  
**Learning objective:** Score open-ended outputs reliably and know the measurement error.  
**Prerequisites:** S12E04, S06E22, S02E14  
**Expected outcome:** Build a judge-based metric with validated agreement and quantified uncertainty.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Metric Types**

- Deterministic checks, reference-based metrics, rubric scoring and pairwise preference
- Task-specific vs general metrics; safety and policy metrics

**Topic 2 — Judge Design**

- Prompt design, rubrics and scales
- Multiple judges and reference answers

**Topic 3 — Judge Biases and Measurement Quality**

- Verbosity, position and self-preference
- Calibration against human labels
- Inter-rater agreement and confidence intervals on scores
- Judge model versioning and drift

</details>

**Important concepts**

- *Commands / APIs / Code:* judge prompt and calibration script (illustrative)
- *Mechanisms & failure scenarios:* Judge drift when its model changes, scores that cannot distinguish versions, optimizing the judge's quirks.

### S12E06 — Evaluating RAG and Agent Systems in CI: Regression Gates

**Depth:** Advanced  
**Learning objective:** Automate evaluation so every change to prompts, models, retrieval or tools is tested before release.  
**Prerequisites:** S12E05, S08E15, S09E13  
**Expected outcome:** Design CI evaluation gates with explicit statistical handling and budgets.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Component and System Tests**

- Retrieval metrics, generation metrics, tool-call checks and trajectory checks
- Mocked vs live dependencies

**Topic 2 — Cheap vs Expensive Suites**

- Fast smoke suites vs full evaluations
- Cost and time budgets

**Topic 3 — Gating and Reporting**

- Baseline comparison and thresholds
- Handling nondeterminism (multiple runs, statistical tests)
- Results in pull requests and failure clustering
- Tracking quality trends over time

</details>

**Important concepts**

- *Commands / APIs / Code:* CI job running an evaluation suite (illustrative), threshold configuration
- *Mechanisms & failure scenarios:* Flaky gates teams learn to ignore, suites too costly to run on every change, thresholds locking in mediocre quality.

### S12E07 — Online Evaluation and Feedback Loops

**Depth:** Advanced  
**Learning objective:** Learn from production usage while protecting users and privacy.  
**Prerequisites:** S12E06, S04E16  
**Expected outcome:** Build a feedback loop that converts production signals into measured improvements.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Signals**

- Explicit feedback (ratings, edits) and implicit signals (retries, abandonment)
- Outcome-based signals

**Topic 2 — Sampling for Review**

- Human review queues and triage
- Sampling strategies: random, uncertainty-based and outlier-based
- Reviewer guidelines and agreement

**Topic 3 — Experiments**

- A/B tests and shadow comparison for prompts and models
- Sparse and delayed feedback; guardrail metrics

**Topic 4 — Closing the Loop**

- Turning failures into evaluation cases
- Ownership of triage

**Topic 5 — Privacy and Consent**

- Consent, retention and sensitive content in review queues
- Redaction before human review
- Access control for reviewers

</details>

**Important concepts**

- *Commands / APIs / Code:* feedback event schema, failure-to-eval-case workflow
- *Mechanisms & failure scenarios:* Feedback biased toward vocal users, experiments underpowered, sensitive user content stored in review queues.

<a id="s12-module-3"></a>

## Module 3 — Observability and Quality Monitoring

**3 episodes (S12E08–S12E10) · 11 topics.** This module covers: LLM Tracing; Token, Cost, and Latency Accounting; Quality Monitoring and Drift for LLM Applications.

| ID | Episode | Depth |
|---|---|---|
| S12E08 | LLM Tracing: Spans for Prompts, Retrieval, and Tools | Intermediate |
| S12E09 | Token, Cost, and Latency Accounting | Intermediate |
| S12E10 | Quality Monitoring and Drift for LLM Applications | Advanced |

### S12E08 — LLM Tracing: Spans for Prompts, Retrieval, and Tools

**Depth:** Intermediate  
**Learning objective:** Capture enough structure to debug any request end to end.  
**Prerequisites:** S12E03, S09E14  
**Expected outcome:** Instrument an LLM application with privacy-aware, versioned traces.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — What a Trace Contains and Cost Attribution**

- Request span with child spans for retrieval, model calls, tool calls and guardrails
- Inputs, outputs, parameters and versions
- Token usage and latency per span
- Cost attribution per step
- Cache-hit and retry attributes

**Topic 2 — Implementation**

- OpenTelemetry-style instrumentation and semantic conventions (verify current status)
- Context propagation across services

**Topic 3 — Sampling, Privacy, and Cost**

- Sampling strategies that keep rare failures
- Redaction, access control and retention

</details>

**Important concepts**

- *Commands / APIs / Code:* span creation around an LLM call (illustrative), attribute schema
- *Mechanisms & failure scenarios:* PII stored in traces, traces without version tags, sampling dropping the rare failures that matter.

### S12E09 — Token, Cost, and Latency Accounting

**Depth:** Intermediate  
**Learning objective:** Attribute spend and delay to features, tenants and components.  
**Prerequisites:** S12E08, S07E09  
**Expected outcome:** Produce cost and latency reports attributable to features and tenants.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Measurement**

- Input, output and cached token counts
- Cost per request, per user and per feature

**Topic 2 — Latency Decomposition**

- Queueing, time to first token, generation and tools
- Streaming vs non-streaming latency
- Percentiles and tail latency

**Topic 3 — Attribution and Budgets**

- Tags for tenant, feature and environment
- Budgets, quotas and alerts; showback/chargeback

**Topic 4 — Using the Data**

- Finding cost outliers and capacity planning
- Cost-per-success rather than cost-per-call
- Retries and price changes in accounting

</details>

**Important concepts**

- *Commands / APIs / Code:* cost tagging middleware (illustrative), usage-report query
- *Mechanisms & failure scenarios:* Untagged spend, retries double-counted or missed, price changes not reflected.

### S12E10 — Quality Monitoring and Drift for LLM Applications

**Depth:** Advanced  
**Learning objective:** Detect quality degradation when there is no single accuracy number.  
**Prerequisites:** S12E05, S11E21  
**Expected outcome:** Set up monitoring that detects LLM quality regression and triggers a response.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — What Can Drift**

- Input distribution and topic mix
- Provider model behavior
- Retrieval corpus freshness and embedding drift

**Topic 2 — Monitoring Techniques**

- Sampled automated scoring of live traffic
- Embedding-based drift of inputs and outputs

**Topic 3 — Behavioral Indicators**

- Refusal rate, length, format-failure and toxicity rates
- Baselines per use case and user segment
- Changes in citation and tool-use rates

**Topic 4 — Probes and Response**

- Canary prompts against the provider
- Alert thresholds, triage, rollback or mitigation

</details>

**Important concepts**

- *Commands / APIs / Code:* scheduled probe suite, live-traffic scoring sample (illustrative)
- *Mechanisms & failure scenarios:* Judge cost making coverage too thin, drift alarms on benign topic change, provider update unnoticed for days.

<a id="s12-module-4"></a>

## Module 4 — Gateways, Safety, and Compliance

**4 episodes (S12E11–S12E14) · 15 topics.** This module covers: LLM Gateways; Guardrails and Safety Evaluation; Prompt Injection and Abuse Defenses in Operations; Privacy, PII, and Compliance for LLM Applications.

| ID | Episode | Depth |
|---|---|---|
| S12E11 | LLM Gateways: Routing, Fallbacks, Policy, and Rate Limiting | Advanced |
| S12E12 | Guardrails and Safety Evaluation: Red-Teaming for LLM Systems | Advanced |
| S12E13 | Prompt Injection and Abuse Defenses in Operations | Advanced |
| S12E14 | Privacy, PII, and Compliance for LLM Applications | Intermediate |

### S12E11 — LLM Gateways: Routing, Fallbacks, Policy, and Rate Limiting

**Depth:** Advanced  
**Learning objective:** Centralize model access with consistent security, reliability and cost controls.  
**Prerequisites:** S07E08, S12E09  
**Expected outcome:** Design a gateway with routing, fallback and policy and state its failure modes.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Gateway Functions**

- Unified API across providers
- Authentication, quotas and budgets
- Logging and policy enforcement

**Topic 2 — Routing**

- Routing by task, cost or latency
- Caching and load balancing
- Normalized request/response schema and capability negotiation across providers
- Routing by task complexity and semantic routing
- Provider-specific features that break portability (application-side view in S07E16)

**Topic 3 — Reliability**

- Fallbacks and retries across providers
- Fallback models with incompatible output

**Topic 4 — Operating**

- Latency overhead and single-point-of-failure risk
- Streaming support
- Provider onboarding and deprecation handling

</details>

**Important concepts**

- *Commands / APIs / Code:* gateway routing configuration (illustrative)
- *Mechanisms & failure scenarios:* Fallback model producing incompatible output, gateway outage taking down all AI features, misrouted sensitive data.

### S12E12 — Guardrails and Safety Evaluation: Red-Teaming for LLM Systems

**Depth:** Advanced  
**Learning objective:** Verify, rather than assume, that safety controls work.  
**Prerequisites:** S07E20, S12E06  
**Expected outcome:** Design a red-team and safety-regression process tied to releases.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Safety Controls**

- Input and output classifiers and policy engines
- Constrained tools and layered defense

**Topic 2 — Refusal Behavior**

- Refusal quality and over-refusal
- Measuring over-refusal with benign-but-sensitive prompts
- Policy tuning by use case

**Topic 3 — Red-Teaming Programs**

- Threat scenarios: jailbreaks, harmful content, data leakage and tool abuse
- Manual and automated adversarial testing
- Severity classification and remediation
- Safety regression suites tied to releases

</details>

**Important concepts**

- *Commands / APIs / Code:* adversarial test set, attack-success-rate metric
- *Mechanisms & failure scenarios:* Guardrails tuned to benchmarks and bypassed in practice, over-refusal harming usability, safety tests not rerun after model changes.

### S12E13 — Prompt Injection and Abuse Defenses in Operations

**Depth:** Advanced  
**Learning objective:** Operationalize defenses and detection for injection and misuse.  
**Prerequisites:** S12E12, S09E12  
**Expected outcome:** Define monitoring and response procedures for injection and abuse.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Operational Defenses**

- Content provenance and trust labeling
- Tool-permission enforcement outside the model
- Egress and output controls

**Topic 2 — Detection**

- Monitoring for anomalous tool use and exfiltration patterns
- Abuse and rate-limit controls

**Topic 3 — Response**

- Incident playbooks and forensics requirements
- Containment: revoking tokens and disabling tools
- Adding regression tests after an incident

**Topic 4 — Testing and Measurement**

- Continuous adversarial testing and reporting channels
- Metrics for defense effectiveness

</details>

**Important concepts**

- *Commands / APIs / Code:* detection rules over traces (illustrative), incident playbook
- *Mechanisms & failure scenarios:* Detection reliant on the same model that was compromised, logs insufficient for forensics, tool permissions drifting wider.

### S12E14 — Privacy, PII, and Compliance for LLM Applications

**Depth:** Intermediate  
**Learning objective:** Handle sensitive data across prompts, logs, vendors and training pipelines.  
**Prerequisites:** S12E08, S07E20  
**Expected outcome:** Map and control sensitive data flows in an LLM application.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Data Flows**

- Where user data goes: prompts, traces, caches, embeddings and fine-tuning sets
- Vendor retention and training terms
- Data residency

**Topic 2 — Controls**

- Redaction, minimization and tokenization of identifiers
- Access control and encryption

**Topic 3 — Deletion and Retention**

- Propagating deletion requests to traces, indexes and caches
- Retention schedules per data class
- Verifying that deletion actually happened

**Topic 4 — Compliance Practice**

- Data-protection regulations at overview level (verify at scripting time)
- DPIAs, vendor assessments and audit evidence

</details>

**Important concepts**

- *Commands / APIs / Code:* data-flow diagram, redaction step (illustrative)
- *Mechanisms & failure scenarios:* PII persisted in embeddings and traces, deletion requests not propagated, vendor terms changing silently.

<a id="s12-module-5"></a>

## Module 5 — Optimization and Delivery

**4 episodes (S12E15–S12E18) · 15 topics.** This module covers: Fine-Tuning Pipelines for Production; Inference Optimization and Cost Engineering; CI/CD for LLM Applications; LLMOps Reference Architecture and an Incident Walkthrough.

| ID | Episode | Depth |
|---|---|---|
| S12E15 | Fine-Tuning Pipelines for Production | Advanced |
| S12E16 | Inference Optimization and Cost Engineering | Advanced |
| S12E17 | CI/CD for LLM Applications: Releases, Canaries, and Rollbacks | Advanced |
| S12E18 | LLMOps Reference Architecture and an Incident Walkthrough | Advanced |

### S12E15 — Fine-Tuning Pipelines for Production

**Depth:** Advanced  
**Learning objective:** Operationalize fine-tuning as a repeatable, evaluated, governed pipeline.  
**Prerequisites:** S07E14, S06E13, S11E11  
**Expected outcome:** Design a governed fine-tune-evaluate-deploy pipeline.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Data Pipeline**

- Collection from traces and feedback with consent
- Cleaning, deduplication, balancing and held-out sets
- Dataset versioning and lineage

**Topic 2 — Training Pipeline**

- Orchestrated training jobs and checkpoints
- Evaluation against the base model and prior versions

**Topic 3 — Registry and Promotion**

- Registering adapters and merged models
- Linking to dataset and base-model versions
- Promotion criteria and approvals

**Topic 4 — Deployment**

- Serving adapters vs merged models
- Canary release and rollback

**Topic 5 — Lifecycle**

- Cost-benefit and drift of fine-tuned models
- Base-model deprecation

</details>

**Important concepts**

- *Commands / APIs / Code:* pipeline stages (illustrative), adapter registry entry
- *Mechanisms & failure scenarios:* Training on unvetted production data, regression on untested capabilities, fine-tuned model stranded when the base is deprecated.

### S12E16 — Inference Optimization and Cost Engineering

**Depth:** Advanced  
**Learning objective:** Reduce cost and latency across hosted and self-hosted LLMs without losing quality.  
**Prerequisites:** S12E09, S06E17, S06E15  
**Expected outcome:** Produce a cost-reduction plan validated by quality measurements.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Application-Level Levers**

- Prompt compression and shorter outputs
- Caching (exact, semantic, prefix)

**Topic 2 — Model Routing and Cascades**

- Routing easy requests to smaller models
- Cascades with confidence thresholds
- Measuring cascade savings and failure rates

**Topic 3 — Serving-Level Levers and Verification**

- Batching, quantization and speculative decoding (connect to S06E17)
- Self-host vs API break-even; capacity and utilization
- Measuring quality impact of each change
- Cost-per-success tracking and avoiding premature optimization

</details>

**Important concepts**

- *Commands / APIs / Code:* break-even calculator, cascade routing sketch
- *Mechanisms & failure scenarios:* Cheap model cascades increasing total cost through retries, quantization hurting a rare but important task, cache poisoning.

### S12E17 — CI/CD for LLM Applications: Releases, Canaries, and Rollbacks

**Depth:** Advanced  
**Learning objective:** Ship changes to prompts, models, retrieval and tools with the same safety as code.  
**Prerequisites:** S12E06, S12E11, S11E13  
**Expected outcome:** Define a release pipeline with evaluation, canary and rollback for an LLM application.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Pipeline Stages and Configuration**

- Lint and unit tests, evaluation gates, safety gates, build and deploy
- Environment promotion
- Secrets and configuration management
- Config drift across environments

**Topic 2 — Progressive Delivery**

- Feature flags for prompts and models
- Canary and shadow traffic
- Automated rollback on quality or cost regression

**Topic 3 — Governance and Migration**

- Approvals for high-risk changes and release notes with evidence
- Provider model migration playbook

</details>

**Important concepts**

- *Commands / APIs / Code:* pipeline definition (illustrative), feature-flagged prompt rollout
- *Mechanisms & failure scenarios:* Provider deprecation forcing rushed migration, canary metrics too coarse to see quality loss, config drift across environments.

### S12E18 — LLMOps Reference Architecture and an Incident Walkthrough

**Depth:** Advanced  
**Learning objective:** See the whole LLMOps stack operating, including how a real class of incident is detected, diagnosed and prevented.  
**Prerequisites:** S12E17, S12E10, S12E03  
**Expected outcome:** Present an LLMOps architecture and walk a hypothetical incident through detection, diagnosis and prevention.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Reference Architecture**

- Gateway, orchestration, retrieval, tools, evaluation, tracing and governance
- Environments and release flow

**Topic 2 — Incident Walkthrough (Hypothetical)**

- A silent quality regression after a provider model update
- Detection via monitoring probes
- Diagnosis via versioned traces

**Topic 3 — Mitigation and Prevention**

- Pinning or rollback; adding evaluation cases
- Adding evaluation cases and probes
- Postmortem and ownership

**Topic 4 — Maturity and Next Steps**

- Right-sizing the stack; metrics for LLMOps health
- Bridge to infrastructure (Season 13) and production systems (Season 14)

</details>

**Important concepts**

- *Commands / APIs / Code:* architecture diagram, incident timeline (clearly labeled hypothetical)
- *Mechanisms & failure scenarios:* Overbuilt tooling nobody maintains, observability gaps masking the real cause, incident learnings not fed back into evaluation.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s12-module-1) | Starting point of the season |
| [Module 2](#s12-module-2) | Within-module sequence only |
| [Module 3](#s12-module-3) | [Module 1](#s12-module-1) (S12E03); [Module 2](#s12-module-2) (S12E05) |
| [Module 4](#s12-module-4) | [Module 2](#s12-module-2) (S12E06); [Module 3](#s12-module-3) (S12E08, S12E09) |
| [Module 5](#s12-module-5) | [Module 1](#s12-module-1) (S12E03); [Module 2](#s12-module-2) (S12E06); [Module 3](#s12-module-3) (S12E09, S12E10); [Module 4](#s12-module-4) (S12E11) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 11 — MLOps Engineering](../season-11-mlops-engineering/roadmap.md)
- **Next:** [Season 13 — AI Infrastructure & Cloud Engineering](../season-13-ai-infrastructure/roadmap.md)
- **Draws on:** [Season 2](../season-02-mathematics-for-ai/roadmap.md) (S02E14); [Season 4](../season-04-advanced-ml-engineering/roadmap.md) (S04E16, S04E19); [Season 6](../season-06-llms-and-transformers/roadmap.md) (S06E13, S06E15, S06E17, S06E22); [Season 7](../season-07-generative-ai-engineering/roadmap.md) (S07E02, S07E08, S07E09, S07E14, S07E19, S07E20, S07E21); [Season 8](../season-08-rag-engineering/roadmap.md) (S08E15); [Season 9](../season-09-ai-agents-and-mcp/roadmap.md) (S09E12, S09E13, S09E14); [Season 11](../season-11-mlops-engineering/roadmap.md) (S11E04, S11E11, S11E13, S11E21, S11E27)
- **Required by:** [Season 13](../season-13-ai-infrastructure/roadmap.md) (via S12E09, S12E12); [Season 14](../season-14-production-ai-systems/roadmap.md) (via S12E12, S12E14, S12E16, S12E18); [Season 15](../season-15-ai-for-devops/roadmap.md) (via S12E06, S12E11)
