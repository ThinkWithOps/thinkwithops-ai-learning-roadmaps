# Season 14 Roadmap — Production AI Systems, Security & Governance

[← Season 14 overview](README.md) · [All seasons](../README.md)

**4 modules · 20 episodes · 77 topics · 218 subtopics · Level: Advanced**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Architecture and Reliability](#s14-module-1)
- [Module 2 — AI Security and Privacy](#s14-module-2)
- [Module 3 — Responsible AI, Governance, and Risk](#s14-module-3)
- [Module 4 — Operations, Economics, and Enterprise Architecture](#s14-module-4)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Bring everything together at production and enterprise level: system design and reliability for AI, AI-specific security, privacy, responsible AI, regulation and risk, AIOps (AI applied to operations), incident management, economics, and reference architectures and three end-to-end case studies.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S14E01 | Apply a repeatable design process to AI systems of any type (ML, LLM, RAG, agents). |
| S14E02 | Define and defend reliability for systems whose outputs are probabilistic. |
| S14E03 | Find and remove bottlenecks across the AI request path under realistic load. |
| S14E04 | Plan recovery and regional strategy for model, data and retrieval platforms. |
| S14E05 | Systematically identify threats to AI systems and prioritize defenses. |
| S14E06 | Understand the attack classes against models themselves and the limits of defenses. |
| S14E07 | Trust (or verify) the models, datasets, libraries and containers an AI system is built from. |
| S14E08 | Apply least privilege across models, tools, data and agents. |
| S14E09 | Reduce privacy risk across training, retrieval, prompts and logs. |
| S14E10 | Operationalize responsible-AI principles with measurable controls. |
| S14E11 | Understand how regulatory and standards frameworks translate into engineering obligations. |
| S14E12 | Decide whether and under what conditions an AI system may go live. |
| S14E13 | Generate trustworthy evidence automatically instead of assembling it before audits. |
| S14E14 | Understand where AI helps operations teams and where it must stay advisory. |
| S14E15 | Run incidents specific to AI: quality regressions, harmful outputs, data leaks and provider failures. |
| S14E16 | Evaluate AI initiatives on measured value and total cost of ownership. |
| S14E17 | Place every component studied in the course into one coherent enterprise architecture. |
| S14E18 | Apply the curriculum to one realistic design problem — a permission-aware knowledge assistant — and defend the architecture, evaluation, governance and operating choices. |
| S14E19 | Apply data, feature, serving, release and monitoring design to a real-time prediction system such as fraud or personalization, and justify the trade-offs. |
| S14E20 | Apply telemetry, anomaly detection, LLM assistance and safe automation to an operations use case, with explicit autonomy tiers and measurable value. |

## Prerequisites and Expected Knowledge

- **Season 4 — [Advanced Machine Learning Engineering](../season-04-advanced-ml-engineering/roadmap.md)**: S04E12, S04E14, S04E15, S04E21
- **Season 5 — [Deep Learning & Neural Networks](../season-05-deep-learning/roadmap.md)**: S05E08
- **Season 7 — [Generative AI Application Engineering](../season-07-generative-ai-engineering/roadmap.md)**: S07E04, S07E08
- **Season 8 — [RAG Engineering](../season-08-rag-engineering/roadmap.md)**: S08E19
- **Season 9 — [AI Agents, Tool Calling & MCP](../season-09-ai-agents-and-mcp/roadmap.md)**: S09E12, S09E18
- **Season 10 — [Advanced Agentic AI](../season-10-advanced-agentic-ai/roadmap.md)**: S10E04, S10E12, S10E15
- **Season 11 — [MLOps Engineering](../season-11-mlops-engineering/roadmap.md)**: S11E04, S11E20, S11E23, S11E24, S11E27
- **Season 12 — [LLMOps Engineering](../season-12-llmops-engineering/roadmap.md)**: S12E12, S12E14, S12E16, S12E18
- **Season 13 — [AI Infrastructure & Cloud Engineering](../season-13-ai-infrastructure/roadmap.md)**: S13E14, S13E15, S13E20, S13E21

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Architecture and Reliability](#s14-module-1) | S14E01–S14E04 | 4 | 1 Intermediate, 3 Advanced |
| 2 | [AI Security and Privacy](#s14-module-2) | S14E05–S14E09 | 5 | 4 Advanced, 1 Intermediate |
| 3 | [Responsible AI, Governance, and Risk](#s14-module-3) | S14E10–S14E13 | 4 | 2 Intermediate, 2 Advanced |
| 4 | [Operations, Economics, and Enterprise Architecture](#s14-module-4) | S14E14–S14E20 | 7 | 6 Advanced, 1 Intermediate |

<a id="s14-module-1"></a>

## Module 1 — Architecture and Reliability

**4 episodes (S14E01–S14E04) · 13 topics.** This module covers: Production AI System Design; Reliability Engineering for AI Systems; Scaling and Performance Engineering; Resilience at Scale.

| ID | Episode | Depth |
|---|---|---|
| S14E01 | Production AI System Design: Requirements, SLOs, and Trade-offs | Intermediate |
| S14E02 | Reliability Engineering for AI Systems: SLOs, Degradation, and Fallbacks | Advanced |
| S14E03 | Scaling and Performance Engineering: Latency Budgets and Load Testing | Advanced |
| S14E04 | Resilience at Scale: Multi-Region Architecture, Disaster Recovery, and Data Sovereignty | Advanced |

### S14E01 — Production AI System Design: Requirements, SLOs, and Trade-offs

**Depth:** Intermediate  
**Learning objective:** Apply a repeatable design process to AI systems of any type (ML, LLM, RAG, agents).  
**Prerequisites:** S11E27, S12E18  
**Expected outcome:** Produce a design with explicit requirements, SLOs and trade-offs for an AI system.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Requirements**

- Functional requirements and quality bars
- Latency, throughput, availability, cost and risk constraints
- Data and model availability at decision time

**Topic 2 — Choosing the Approach and Component Architecture**

- Rules, classical ML, LLM, RAG or agent — by requirement
- Selecting an LLM where a classifier suffices
- Components and data flows
- Build/buy and make/compose decisions

**Topic 3 — Trade-off Analysis**

- Quality vs cost vs latency vs safety
- Documenting decisions (ADRs) and failure-mode analysis up front

</details>

**Important concepts**

- *Commands / APIs / Code:* design-review template; requirement-to-component matrix
- *Mechanisms & failure scenarios:* Selecting an LLM where a classifier suffices, unbounded autonomy for a low-risk task, SLOs defined after launch.

### S14E02 — Reliability Engineering for AI Systems: SLOs, Degradation, and Fallbacks

**Depth:** Advanced  
**Learning objective:** Define and defend reliability for systems whose outputs are probabilistic.  
**Prerequisites:** S14E01, S07E08  
**Expected outcome:** Specify SLOs and degradation modes for an AI service.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — SLIs and SLOs for AI**

- Availability, latency, quality and safety indicators
- Error budgets including quality failures
- Per-segment objectives

**Topic 2 — Failure Domains**

- Model provider outages, GPU capacity loss, data pipeline failures and retrieval failures
- Dependency mapping and blast-radius reduction

**Topic 3 — Graceful Degradation and Exercising Fallbacks**

- Fallback models, cached answers, reduced features and human handoff
- Circuit breakers and load shedding
- Fallback paths that are never tested
- Communicating degraded mode to users

</details>

**Important concepts**

- *Commands / APIs / Code:* SLO definition file (illustrative), error-budget calculation
- *Mechanisms & failure scenarios:* Quality failures invisible to availability SLOs, fallback paths never exercised, cascading retries during provider outages.

### S14E03 — Scaling and Performance Engineering: Latency Budgets and Load Testing

**Depth:** Advanced  
**Learning objective:** Find and remove bottlenecks across the AI request path under realistic load.  
**Prerequisites:** S14E02, S13E14  
**Expected outcome:** Design and interpret a load test and set capacity targets for an AI service.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Latency Budgets**

- Decomposing end-to-end latency
- Tail latency and queueing effects
- Streaming and perceived latency

**Topic 2 — Load Testing AI Systems**

- Realistic workloads: prompt lengths, concurrency and burstiness
- Measuring throughput, TTFT and p95/p99

**Topic 3 — Testing Dependencies**

- Rate limits and provider quotas
- Load tests that hit production providers

**Topic 4 — Capacity Planning**

- Headroom and autoscaling policy
- Cost-performance curves
- Overload behavior and queueing collapse near saturation

</details>

**Important concepts**

- *Commands / APIs / Code:* load generator script for an LLM endpoint (illustrative), latency histogram analysis
- *Mechanisms & failure scenarios:* Benchmarks with uniform short prompts, ignoring queueing collapse near saturation, load tests hitting production providers.

### S14E04 — Resilience at Scale: Multi-Region Architecture, Disaster Recovery, and Data Sovereignty

**Depth:** Advanced  
**Learning objective:** Plan recovery and regional strategy for model, data and retrieval platforms.  
**Prerequisites:** S14E02, S13E15  
**Expected outcome:** Create a DR and regional strategy covering all AI system components.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Recovery Objectives, Backup, and Restore**

- RPO/RTO for models, indexes, feature stores and prompts
- What must be replicated: weights, data and configuration
- Backing up indexes and configuration, not only data
- Restore validation

**Topic 2 — Multi-Region Patterns**

- Active-active vs active-passive for inference
- Model availability and quota per region
- Data residency constraints

**Topic 3 — Testing and Runbooks**

- Game days and failure injection
- Provider-outage drills, runbooks and communication

</details>

**Important concepts**

- *Commands / APIs / Code:* recovery runbook outline; replication plan table
- *Mechanisms & failure scenarios:* Backups of data but not of index or configuration, secondary region lacking model capacity, data-residency violations during failover.

<a id="s14-module-2"></a>

## Module 2 — AI Security and Privacy

**5 episodes (S14E05–S14E09) · 20 topics.** This module covers: AI Threat Modeling; Adversarial ML; Model and Data Supply Chain Security; Identity, Secrets, and Access Control for AI Systems; Privacy and Data Protection in AI Systems.

| ID | Episode | Depth |
|---|---|---|
| S14E05 | AI Threat Modeling: OWASP LLM Risks, MITRE ATLAS, and Trust Boundaries | Advanced |
| S14E06 | Adversarial ML: Jailbreaks, Evasion, Data Poisoning, and Model Extraction | Advanced |
| S14E07 | Model and Data Supply Chain Security | Intermediate |
| S14E08 | Identity, Secrets, and Access Control for AI Systems | Advanced |
| S14E09 | Privacy and Data Protection in AI Systems | Advanced |

### S14E05 — AI Threat Modeling: OWASP LLM Risks, MITRE ATLAS, and Trust Boundaries

**Depth:** Advanced  
**Learning objective:** Systematically identify threats to AI systems and prioritize defenses.  
**Prerequisites:** S14E01, S09E12, S07E04  
**Expected outcome:** Produce a threat model for an AI application and a prioritized control plan.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Threat Modeling Method**

- Assets, actors, trust boundaries and data flows
- Threat-modeling approaches adapted to AI

**Topic 2 — Attack Surfaces**

- Prompts, retrieval, tools, training data and model artifacts
- Treating the model as an untrusted component

**Topic 3 — Application-Risk Catalog**

- LLM application risk categories (verify current OWASP list)
- Mapping risks to components

**Topic 4 — Adversary Tactics Catalog**

- Adversarial tactic knowledge bases (verify current ATLAS)
- Using them to plan tests

**Topic 5 — From Threats to Controls**

- Prioritization by impact and likelihood
- Layered controls and residual risk
- Security requirements in design reviews

</details>

**Important concepts**

- *Commands / APIs / Code:* threat-model worksheet over a data-flow diagram
- *Mechanisms & failure scenarios:* Treating the model as trusted, ignoring supply-chain and data threats, controls that address only prompt content.

### S14E06 — Adversarial ML: Jailbreaks, Evasion, Data Poisoning, and Model Extraction

**Depth:** Advanced  
**Learning objective:** Understand the attack classes against models themselves and the limits of defenses.  
**Prerequisites:** S14E05, S05E08  
**Expected outcome:** Classify attacks by lifecycle stage and select proportional mitigations.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Attacks at Inference**

- Adversarial examples and evasion
- Jailbreak techniques and why they transfer

**Topic 2 — Information Extraction Attacks**

- Model extraction and membership inference
- Query-based extraction and its defenses
- Privacy auditing of trained models

**Topic 3 — Attacks on Training**

- Data poisoning and backdoors
- Poisoned retrieval corpora and feedback channels

**Topic 4 — Defenses and Limits**

- Adversarial training, filtering, monitoring and rate limiting
- Provenance and data curation
- Honest limits and defense in depth

</details>

**Important concepts**

- *Commands / APIs / Code:* illustrative adversarial perturbation of a toy classifier (concept), poisoning simulation on small data
- *Mechanisms & failure scenarios:* Defenses evaluated only against known attacks, poisoning via user feedback, extraction through unrestricted API access.

### S14E07 — Model and Data Supply Chain Security

**Depth:** Intermediate  
**Learning objective:** Trust (or verify) the models, datasets, libraries and containers an AI system is built from.  
**Prerequisites:** S14E05, S13E15  
**Expected outcome:** Define an intake and verification process for external AI artifacts.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Risks**

- Unsafe serialization formats and code execution on load
- Malicious or tampered models and datasets
- Typosquatted packages and compromised images

**Topic 2 — Controls**

- Safer weight formats and scanning
- Signing, checksums and provenance attestations
- Private registries and allowlists

**Topic 3 — Intake Process**

- Review of third-party models and datasets
- SBOMs and AI bills of materials (concept)
- License and usage-term checks

</details>

**Important concepts**

- *Commands / APIs / Code:* artifact verification steps (illustrative), scanner usage (concept)
- *Mechanisms & failure scenarios:* Loading a pickled model from an unvetted source, mutable tags replaced upstream, unlicensed model in production.

### S14E08 — Identity, Secrets, and Access Control for AI Systems

**Depth:** Advanced  
**Learning objective:** Apply least privilege across models, tools, data and agents.  
**Prerequisites:** S14E05, S10E04  
**Expected outcome:** Specify an identity, secrets and authorization model for an AI system.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Identity for Workloads and Agents**

- Service identities and short-lived credentials
- User-delegated access and impersonation limits
- Tenant isolation

**Topic 2 — Secrets and Keys**

- Provider API keys, tool credentials and signing keys
- Rotation, vaulting and leak detection
- Secrets in prompts, logs and memory

**Topic 3 — Authorization Design**

- Per-tool and per-data-source policies
- Policy enforcement points

**Topic 4 — Auditing**

- Audit trails and anomaly detection
- Shared API keys across tenants and over-broad pipeline accounts

</details>

**Important concepts**

- *Commands / APIs / Code:* policy-as-code example (illustrative), secret-scanning step (concept)
- *Mechanisms & failure scenarios:* Shared API key across tenants, secrets echoed into model context, over-broad service accounts for pipelines.

### S14E09 — Privacy and Data Protection in AI Systems

**Depth:** Advanced  
**Learning objective:** Reduce privacy risk across training, retrieval, prompts and logs.  
**Prerequisites:** S12E14, S14E05  
**Expected outcome:** Create a privacy plan covering data used in training, retrieval and operation.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Privacy Risks**

- Memorization and leakage from models
- PII in training sets, indexes and traces
- Re-identification and inference attacks

**Topic 2 — Techniques**

- Minimization, anonymization and pseudonymization
- Differential privacy and federated learning at concept level
- Access control and encryption

**Topic 3 — Lifecycle Obligations**

- Consent, purpose limitation and retention
- Deletion and unlearning challenges

**Topic 4 — Documentation**

- Impact assessments
- Data deleted at the source but not from indexes or fine-tuned models

</details>

**Important concepts**

- *Commands / APIs / Code:* PII scanning pipeline sketch; retention-policy configuration (illustrative)
- *Mechanisms & failure scenarios:* Data deleted from the source but not from indexes or fine-tuned models, membership inference revealing sensitive records, over-collection "for future use".

<a id="s14-module-3"></a>

## Module 3 — Responsible AI, Governance, and Risk

**4 episodes (S14E10–S14E13) · 13 topics.** This module covers: Responsible AI in Production; AI Regulation and Frameworks; Model Risk Management and Release Governance; AI Assurance.

| ID | Episode | Depth |
|---|---|---|
| S14E10 | Responsible AI in Production: Fairness Monitoring, Transparency, and Human Oversight | Intermediate |
| S14E11 | AI Regulation and Frameworks: EU AI Act, NIST AI RMF, and ISO Standards | Intermediate |
| S14E12 | Model Risk Management and Release Governance | Advanced |
| S14E13 | AI Assurance: Audit-Ready Evidence and Continuous Compliance | Advanced |

### S14E10 — Responsible AI in Production: Fairness Monitoring, Transparency, and Human Oversight

**Depth:** Intermediate  
**Learning objective:** Operationalize responsible-AI principles with measurable controls.  
**Prerequisites:** S04E15, S04E14, S11E24  
**Expected outcome:** Define responsible-AI controls and metrics for a deployed system.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Measuring Harm**

- Slice-based performance and fairness monitoring (building on S04E15)
- Content safety and misuse monitoring for generative systems

**Topic 2 — Transparency**

- Model and system documentation, user disclosure
- Explanations appropriate to the audience (building on S04E14)
- Appeals and redress

**Topic 3 — Human Oversight**

- Where humans decide vs review vs monitor
- Avoiding automation bias
- Escalation and override

</details>

**Important concepts**

- *Commands / APIs / Code:* fairness dashboard queries (illustrative), oversight decision matrix
- *Mechanisms & failure scenarios:* Reviewers rubber-stamping model output, fairness metrics monitored only at launch, no route for affected users to contest.

### S14E11 — AI Regulation and Frameworks: EU AI Act, NIST AI RMF, and ISO Standards

**Depth:** Intermediate  
**Learning objective:** Understand how regulatory and standards frameworks translate into engineering obligations.  
**Prerequisites:** S14E10  
**Expected outcome:** Map a system's risk class to a concrete list of engineering and documentation controls.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Landscape**

- Risk-based regulation concepts
- Voluntary frameworks and management-system standards
- Sector rules (finance, health) at overview level

**Topic 2 — Roles**

- Provider, deployer and user obligations
- Shared responsibility with model vendors
- Obligations that attach to deployers

**Topic 3 — From Requirements to Engineering**

- Risk classification of a system
- Documentation, logging, testing and oversight requirements

**Topic 4 — Compliance Practice**

- Mapping controls to requirements and collecting evidence
- Keeping up with change (all legal specifics verified against primary sources at scripting time; not legal advice)

</details>

**Important concepts**

- *Commands / APIs / Code:* control-mapping table template
- *Mechanisms & failure scenarios:* Misclassifying system risk level, evidence assembled only at audit time, ignoring obligations that attach to deployers.

### S14E12 — Model Risk Management and Release Governance

**Depth:** Advanced  
**Learning objective:** Decide whether and under what conditions an AI system may go live.  
**Prerequisites:** S14E11, S11E04  
**Expected outcome:** Design a release-governance process proportional to risk.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Risk Assessment**

- Use-case risk tiering
- Model validation independent of development
- Limitations and intended-use statements

**Topic 2 — Release Governance**

- Approval workflows and stage gates
- Exceptions and risk acceptance

**Topic 3 — Inventory and Lifecycle**

- Model, prompt, agent and dataset inventories
- Shadow AI systems absent from the inventory
- Periodic review and retirement
- Third-party model risk

</details>

**Important concepts**

- *Commands / APIs / Code:* risk-tier policy table; inventory record schema
- *Mechanisms & failure scenarios:* Shadow AI systems absent from the inventory, validation done by the builders only, approvals without evidence.

### S14E13 — AI Assurance: Audit-Ready Evidence and Continuous Compliance

**Depth:** Advanced  
**Learning objective:** Generate trustworthy evidence automatically instead of assembling it before audits.  
**Prerequisites:** S14E12, S12E12  
**Expected outcome:** Specify automated evidence generation and control monitoring for AI governance.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Evidence by Design**

- What auditors ask for: lineage, evaluations, approvals and access logs
- Immutable logs and tamper evidence
- Linking evidence to releases

**Topic 2 — Continuous Control Monitoring**

- Automated checks against policy
- Control testing cadence and exceptions tracking

**Topic 3 — External and Internal Audit**

- Preparing for external review
- Findings remediation and reporting to leadership

</details>

**Important concepts**

- *Commands / APIs / Code:* evidence-collection pipeline (illustrative), control-status report
- *Mechanisms & failure scenarios:* Logs lacking the reasoning/action trace, controls documented but not enforced, evidence drift between releases.

<a id="s14-module-4"></a>

## Module 4 — Operations, Economics, and Enterprise Architecture

**7 episodes (S14E14–S14E20) · 31 topics.** This module covers: AIOps; Incident Management for AI Systems; AI Economics; Enterprise AI Reference Architecture; Case Study; Case Study; Case Study.

| ID | Episode | Depth |
|---|---|---|
| S14E14 | AIOps: Applying AI to IT Operations | Advanced |
| S14E15 | Incident Management for AI Systems | Advanced |
| S14E16 | AI Economics: Cost, ROI, and Portfolio Decisions | Intermediate |
| S14E17 | Enterprise AI Reference Architecture | Advanced |
| S14E18 | Case Study: Designing an Enterprise Knowledge Assistant (RAG and Agents) | Advanced |
| S14E19 | Case Study: Designing a Real-Time Prediction Platform (ML and MLOps) | Advanced |
| S14E20 | Case Study: Designing AI-Assisted Operations (AIOps and Agents) | Advanced |

### S14E14 — AIOps: Applying AI to IT Operations

**Depth:** Advanced  
**Learning objective:** Understand where AI helps operations teams and where it must stay advisory.  
**Prerequisites:** S04E12, S09E18, S11E20  
**Expected outcome:** Design an AIOps workflow with human oversight and quantified value.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Telemetry to Insight**

- Metrics, logs, traces and events as inputs
- Topology and change context

**Topic 2 — Anomaly Detection and Correlation**

- Baselines, seasonality and threshold tuning
- Event deduplication, grouping and noise reduction

**Topic 3 — Incident Intelligence**

- Candidate root-cause ranking vs proven cause
- LLM-assisted triage, runbook retrieval and summaries

**Topic 4 — Forecasting**

- Capacity prediction and lead time
- Seasonality, trend and uncertainty intervals
- Forecast-driven scaling decisions

**Topic 5 — Safe Automation**

- Recommendation vs execution boundary
- Risk tiers, approvals and idempotent remediation
- Measuring value: false positives, time saved and operator acceptance
- Deeper coverage of each topic in this episode is in Season 15, AI for DevOps & Intelligent Operations, starting at S15E01

</details>

**Important concepts**

- *Commands / APIs / Code:* anomaly-detection baseline on a metric series (illustrative), remediation policy gate
- *Mechanisms & failure scenarios:* Auto-remediation acting on a wrong diagnosis, correlation mistaken for causation, alert suppression hiding real incidents.

### S14E15 — Incident Management for AI Systems

**Depth:** Advanced  
**Learning objective:** Run incidents specific to AI: quality regressions, harmful outputs, data leaks and provider failures.  
**Prerequisites:** S14E02, S11E23, S12E18  
**Expected outcome:** Operate and learn from an AI-specific incident using a defined process.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — AI Incident Types**

- Quality/behavioral, safety and harmful-output, security and privacy, and cost incidents
- Severity classification beyond downtime

**Topic 2 — Detection and Response**

- Detection sources
- Containment: disable a feature, pin or roll back a model, tighten guardrails

**Topic 3 — Evidence, Communication, and Learning**

- Evidence preservation and reproduction of harmful outputs
- Disclosure obligations
- Blameless postmortems with AI-specific factors
- Turning incidents into evaluations and tests; trend analysis

</details>

**Important concepts**

- *Commands / APIs / Code:* incident runbook, postmortem template (illustrative)
- *Mechanisms & failure scenarios:* No kill switch for an AI feature, inability to reproduce a harmful output, unreported privacy incidents.

### S14E16 — AI Economics: Cost, ROI, and Portfolio Decisions

**Depth:** Intermediate  
**Learning objective:** Evaluate AI initiatives on measured value and total cost of ownership.  
**Prerequisites:** S13E21, S12E16  
**Expected outcome:** Build a defensible business case and ongoing unit-economics view for an AI feature.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Total Cost**

- Build, run, human review, governance and opportunity cost
- Token, GPU and data costs
- Hidden costs: evaluation, monitoring and rework

**Topic 2 — Value**

- Quality-adjusted outcomes: time saved, revenue and risk reduced
- Counterfactual baselines
- Adoption vs capability

**Topic 3 — Decisions**

- Prioritizing use cases
- When to stop or simplify
- Unit economics for scaling and pilots that do not survive scale

</details>

**Important concepts**

- *Commands / APIs / Code:* TCO and ROI worksheet
- *Mechanisms & failure scenarios:* Pilot economics not surviving scale, ignoring human-review cost, value claimed without a baseline.

### S14E17 — Enterprise AI Reference Architecture

**Depth:** Advanced  
**Learning objective:** Place every component studied in the course into one coherent enterprise architecture.  
**Prerequisites:** S14E13, S13E20, S10E12  
**Expected outcome:** Present and critique an enterprise AI reference architecture.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Layered Architecture**

- Experience, orchestration, model/retrieval/agent, data and platform layers
- Shared services: gateway, registry, feature and vector stores

**Topic 2 — Planes**

- Identity, security, governance and observability planes
- How planes integrate with runtime systems
- Policy decision and enforcement points

**Topic 3 — Cross-Cutting Concerns**

- Multi-tenancy and isolation
- Resilience and cost controls
- Compliance and audit

**Topic 4 — Evolution**

- Maturity roadmap and sequencing
- Standardization vs team autonomy
- Technology change management

</details>

**Important concepts**

- *Commands / APIs / Code:* layered reference diagram and capability map
- *Mechanisms & failure scenarios:* Platform sprawl, governance planes not integrated with runtime, single points of failure in shared services.

### S14E18 — Case Study: Designing an Enterprise Knowledge Assistant (RAG and Agents)

**Depth:** Advanced  
**Learning objective:** Apply the curriculum to one realistic design problem — a permission-aware knowledge assistant — and defend the architecture, evaluation, governance and operating choices.  
**Prerequisites:** S14E17, S08E19, S10E15  
**Expected outcome:** Present and defend an end-to-end design for a knowledge assistant, including the components you chose not to build.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Requirements and Risk**

- Users, content sources, quality bar and risk tier
- Permission model and data classification
- Success metrics and non-goals

**Topic 2 — Architecture**

- Ingestion, index, retrieval, generation, gateway and identity
- Where agents add value and where fixed pipelines suffice

**Topic 3 — Evaluation and Release**

- Retrieval and answer evaluation, safety tests and release gates
- Evaluation sets for retrieval and answers
- Safety and injection tests as release gates
- Canary release and feedback loops

**Topic 4 — Security and Governance**

- Permission-aware retrieval, injection defenses and audit evidence
- Permission-aware retrieval
- Injection defenses and tool permissions
- Audit evidence and approvals

**Topic 5 — Operations and Failure Scenarios**

- Freshness, incidents, degradation modes and runbooks
- Cost model and scaling

</details>

**Important concepts**

- *Commands / APIs / Code:* Design document with architecture diagram, risk register and evaluation plan (clearly labeled hypothetical)
- *Mechanisms & failure scenarios:* Stale or unowned content, permission leaks through caches, over-autonomous agents, quality regressions after embedding upgrades, cost growth with corpus size.

### S14E19 — Case Study: Designing a Real-Time Prediction Platform (ML and MLOps)

**Depth:** Advanced  
**Learning objective:** Apply data, feature, serving, release and monitoring design to a real-time prediction system such as fraud or personalization, and justify the trade-offs.  
**Prerequisites:** S14E17, S11E27, S04E21  
**Expected outcome:** Present and defend an end-to-end real-time ML platform design, including SLOs, release strategy and monitoring.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — Requirements and SLOs**

- Latency, availability, freshness and cost; risk of wrong predictions
- Latency, availability, freshness and cost targets
- Fallback policy when predictions are wrong or unavailable
- Label availability and feedback latency

**Topic 2 — Data and Feature Architecture**

- Batch and streaming features, point-in-time correctness and the feature store
- Batch and streaming feature paths
- Training-serving consistency checks
- Late and out-of-order events

**Topic 3 — Training and Release**

- Pipelines, evaluation gates, canary and shadow release, rollback
- Evaluation gates before promotion
- Canary and shadow release
- Rollback with compatible feature versions

**Topic 4 — Serving and Reliability**

- Serving pattern, fallbacks and capacity planning
- Online vs precomputed serving choice
- Fallbacks and graceful degradation
- Capacity planning and autoscaling

**Topic 5 — Monitoring and Retraining**

- Drift, delayed labels, retraining triggers and incident response
- Drift and skew monitoring
- Delayed labels and proxy metrics
- Incident response

**Topic 6 — Governance and Trade-offs**

- Fairness, documentation and what to simplify for a small team
- Fairness and documentation requirements
- Cost and team-size trade-offs
- What to simplify first

</details>

**Important concepts**

- *Commands / APIs / Code:* Design document with data-flow diagram, SLOs and retraining policy (clearly labeled hypothetical)
- *Mechanisms & failure scenarios:* Training-serving skew, stale online features, label delay hiding degradation, retraining on feedback-contaminated data, rollback blocked by incompatible feature versions.

### S14E20 — Case Study: Designing AI-Assisted Operations (AIOps and Agents)

**Depth:** Advanced  
**Learning objective:** Apply telemetry, anomaly detection, LLM assistance and safe automation to an operations use case, with explicit autonomy tiers and measurable value.  
**Prerequisites:** S14E17, S14E14, S10E15  
**Expected outcome:** Present and defend an AI-assisted operations design with safe automation boundaries and a plan to measure benefit.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Problem and Baseline**

- Current operational pain, signals available and success measures
- Baseline metrics for current operational pain
- Available signals and their quality
- Scope and success measures

**Topic 2 — Detection and Triage**

- Anomaly detection, correlation and LLM-assisted triage
- Anomaly detection and correlation choices
- Runbook retrieval and summaries
- Confidence and evidence shown to operators

**Topic 3 — Remediation and Autonomy Tiers**

- Recommendation vs execution, approvals and idempotent actions
- Approvals, idempotent actions and blast-radius limits
- Autonomy tiers and promotion criteria

**Topic 4 — Security and Governance**

- Agent identity, least privilege, audit and kill switches
- Agent identity and least privilege
- Audit trails and kill switches
- Policy-as-code gates

**Topic 5 — Measuring Value and Failure Modes**

- False positives, time saved and operator acceptance
- Staged rollout and rollback

</details>

**Important concepts**

- *Commands / APIs / Code:* Design document with autonomy-tier table and remediation policy gates (clearly labeled hypothetical)
- *Mechanisms & failure scenarios:* Auto-remediation acting on a wrong diagnosis, alert suppression hiding real incidents, correlation mistaken for causation, agent permissions drifting wider, untracked value.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s14-module-1) | Starting point of the season |
| [Module 2](#s14-module-2) | [Module 1](#s14-module-1) (S14E01) |
| [Module 3](#s14-module-3) | Within-module sequence only |
| [Module 4](#s14-module-4) | [Module 1](#s14-module-1) (S14E02); [Module 3](#s14-module-3) (S14E13) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 13 — AI Infrastructure & Cloud Engineering](../season-13-ai-infrastructure/roadmap.md)
- **Next:** [Season 15 — AI for DevOps & Intelligent Operations](../season-15-ai-for-devops/roadmap.md)
- **Draws on:** [Season 4](../season-04-advanced-ml-engineering/roadmap.md) (S04E12, S04E14, S04E15, S04E21); [Season 5](../season-05-deep-learning/roadmap.md) (S05E08); [Season 7](../season-07-generative-ai-engineering/roadmap.md) (S07E04, S07E08); [Season 8](../season-08-rag-engineering/roadmap.md) (S08E19); [Season 9](../season-09-ai-agents-and-mcp/roadmap.md) (S09E12, S09E18); [Season 10](../season-10-advanced-agentic-ai/roadmap.md) (S10E04, S10E12, S10E15); [Season 11](../season-11-mlops-engineering/roadmap.md) (S11E04, S11E20, S11E23, S11E24, S11E27); [Season 12](../season-12-llmops-engineering/roadmap.md) (S12E12, S12E14, S12E16, S12E18); [Season 13](../season-13-ai-infrastructure/roadmap.md) (S13E14, S13E15, S13E20, S13E21)
- **Required by:** [Season 15](../season-15-ai-for-devops/roadmap.md) (via S14E02, S14E08, S14E13, S14E14, S14E16, S14E17)
