# Season 15 Roadmap — AI for DevOps & Intelligent Operations

[← Season 15 overview](README.md) · [All seasons](../README.md)

**8 modules · 32 episodes · 160 topics · 320 subtopics · Level: Advanced specialization**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — AI-Powered DevOps Foundations](#s15-module-1)
- [Module 2 — Intelligent Observability](#s15-module-2)
- [Module 3 — AI-Powered Incident Management](#s15-module-3)
- [Module 4 — AI SRE & Reliability Engineering](#s15-module-4)
- [Module 5 — AI DevOps Agents](#s15-module-5)
- [Module 6 — AI-Powered CI/CD](#s15-module-6)
- [Module 7 — AI Infrastructure Automation & FinOps](#s15-module-7)
- [Module 8 — Enterprise AIOps Architecture](#s15-module-8)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Apply AI, LLMs and agents to operations: observe, investigate, decide, remediate, deliver and govern, always with evidence, human control and measurable value. This is the "AI for DevOps" direction; operating AI and ML systems ("DevOps for AI") is covered in Seasons 11–14. The season assumes DevOps and SRE fundamentals (outside the AI-first curriculum) and the AI building blocks of Seasons 4 and 6–10; it reuses them by prerequisite and does not re-teach RAG, agents, MCP, evaluation, guardrails, MLOps or LLMOps. The AIOps overview is S14E14 and the integrative case study is S14E20; this season provides the depth behind both.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S15E01 | Map operational problems to AI capabilities and limits, and recognize where AI helps, where it misleads, and how far automation should go. |
| S15E02 | Choose between deterministic and AI-driven automation for an operational task using explicit criteria. |
| S15E03 | Draw the reference architecture of an AI-for-operations system and identify its dependencies and failure modes. |
| S15E04 | Use AI assistants safely in everyday operations work such as runbooks, queries, commands and change authoring. |
| S15E05 | Turn high-volume logs into understandable signals using parsing, clustering and carefully grounded language models. |
| S15E06 | Apply baselines, anomaly detection and trace analysis to service telemetry and interpret the results without false confidence. |
| S15E07 | Reduce alert noise through grouping and correlation while measuring the risk of hiding real incidents. |
| S15E08 | Build natural-language access to telemetry that is safe, verifiable and honest about its limits. |
| S15E09 | Structure AI assistance during an investigation around gathering evidence, forming hypotheses and verifying them. |
| S15E10 | Rank probable causes using topology, changes and telemetry, and communicate confidence honestly. |
| S15E11 | Produce accurate, evidence-backed incident summaries for different audiences. |
| S15E12 | Design an incident copilot that helps responders without adding risk or cognitive load. |
| S15E13 | Use AI to analyze SLIs, SLOs and error budgets and communicate reliability status accurately. |
| S15E14 | Build and evaluate early-warning signals that give useful lead time without drowning responders in false alarms. |
| S15E15 | Produce capacity forecasts and evidence-backed reliability recommendations that teams actually act on. |
| S15E16 | Design agents that diagnose common Kubernetes failures using scoped read-only tools and sound reasoning. |
| S15E17 | Build operations agents for infrastructure and cloud estates that are useful, bounded and auditable. |
| S15E18 | Compose MCP servers for operations safely and effectively. |
| S15E19 | Design the full lifecycle of a remediation that an AI proposes and a human approves. |
| S15E20 | Classify and diagnose CI failures faster, including distinguishing flaky tests from real regressions. |
| S15E21 | Use history and code structure to run fewer, better tests and read quality signals correctly. |
| S15E22 | Estimate the risk of a change before deployment and use the estimate in gates without eroding developer trust. |
| S15E23 | Apply AI to release notes, change review and progressive-delivery judgments with clear accountability. |
| S15E24 | Use AI to author, review and explain infrastructure as code safely, including AI-assisted provisioning workflows. |
| S15E25 | Find and act on cloud waste with recommendations that respect performance and risk. |
| S15E26 | Detect and explain cost anomalies and triage cloud configuration issues with AI. |
| S15E27 | Design an enterprise-scale AIOps platform that integrates data, shared AI services, operations tools and teams. |
| S15E28 | Coordinate multiple operations agents without losing control, context or accountability. |
| S15E29 | Govern operations AI with identity, tiered permissions, data handling and audit appropriate to its power over production. |
| S15E30 | Organize people and processes around AI so humans stay effective, informed and accountable. |
| S15E31 | Decide when automation may act without approval and engineer the controls that keep it safe. |
| S15E32 | Measure whether operations AI works and adopt it incrementally with evidence. |

## Prerequisites and Expected Knowledge

- **Season 4 — [Advanced Machine Learning Engineering](../season-04-advanced-ml-engineering/roadmap.md)**: S04E01, S04E02, S04E08, S04E09, S04E12, S04E13, S04E17
- **Season 6 — [LLMs & Transformer Architecture](../season-06-llms-and-transformers/roadmap.md)**: S06E21
- **Season 7 — [Generative AI Application Engineering](../season-07-generative-ai-engineering/roadmap.md)**: S07E03, S07E19
- **Season 8 — [RAG Engineering](../season-08-rag-engineering/roadmap.md)**: S08E04, S08E09, S08E13, S08E19
- **Season 9 — [AI Agents, Tool Calling & MCP](../season-09-ai-agents-and-mcp/roadmap.md)**: S09E03, S09E04, S09E06, S09E10, S09E11, S09E12, S09E16, S09E17, S09E18
- **Season 10 — [Advanced Agentic AI](../season-10-advanced-agentic-ai/roadmap.md)**: S10E01, S10E02, S10E04, S10E08, S10E13, S10E14
- **Season 11 — [MLOps Engineering](../season-11-mlops-engineering/roadmap.md)**: S11E13, S11E17
- **Season 12 — [LLMOps Engineering](../season-12-llmops-engineering/roadmap.md)**: S12E06, S12E11
- **Season 13 — [AI Infrastructure & Cloud Engineering](../season-13-ai-infrastructure/roadmap.md)**: S13E06, S13E19, S13E21
- **Season 14 — [Production AI Systems, Security & Governance](../season-14-production-ai-systems/roadmap.md)**: S14E02, S14E08, S14E13, S14E14, S14E16, S14E17

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [AI-Powered DevOps Foundations](#s15-module-1) | S15E01–S15E04 | 4 | 4 Intermediate |
| 2 | [Intelligent Observability](#s15-module-2) | S15E05–S15E08 | 4 | 4 Intermediate |
| 3 | [AI-Powered Incident Management](#s15-module-3) | S15E09–S15E12 | 4 | 3 Intermediate, 1 Advanced |
| 4 | [AI SRE & Reliability Engineering](#s15-module-4) | S15E13–S15E15 | 3 | 2 Intermediate, 1 Advanced |
| 5 | [AI DevOps Agents](#s15-module-5) | S15E16–S15E19 | 4 | 3 Advanced, 1 Intermediate |
| 6 | [AI-Powered CI/CD](#s15-module-6) | S15E20–S15E23 | 4 | 3 Intermediate, 1 Advanced |
| 7 | [AI Infrastructure Automation & FinOps](#s15-module-7) | S15E24–S15E26 | 3 | 1 Advanced, 2 Intermediate |
| 8 | [Enterprise AIOps Architecture](#s15-module-8) | S15E27–S15E32 | 6 | 4 Advanced, 2 Intermediate |

<a id="s15-module-1"></a>

## Module 1 — AI-Powered DevOps Foundations

**4 episodes (S15E01–S15E04) · 20 topics.** This module covers: AIOps Foundations; Traditional Automation vs AI-Driven Automation; AI-Powered DevOps Architecture; AI-Assisted Engineering Workflows for Operations Teams.

| ID | Episode | Depth |
|---|---|---|
| S15E01 | AIOps Foundations: What AI Can and Cannot Do for Operations | Intermediate |
| S15E02 | Traditional Automation vs AI-Driven Automation | Intermediate |
| S15E03 | AI-Powered DevOps Architecture: Telemetry, Context, Reasoning, Action, and Feedback | Intermediate |
| S15E04 | AI-Assisted Engineering Workflows for Operations Teams | Intermediate |

### S15E01 — AIOps Foundations: What AI Can and Cannot Do for Operations

**Depth:** Intermediate  
**Learning objective:** Map operational problems to AI capabilities and limits, and recognize where AI helps, where it misleads, and how far automation should go.  
**Prerequisites:** S14E14, S06E21, S04E12  
**Expected outcome:** Place an operational task on the capability map and the autonomy ladder and state how its value would be measured.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Operations Problem Space**

- Toil, alert volume, mean time to detect and recover, and cognitive load
- Where operations time goes in a typical incident and delivery cycle

**Topic 2 — A Capability Map**

- Classification, detection, forecasting, summarization, retrieval, reasoning and action
- Which capabilities suit which operational tasks

**Topic 3 — Where AI Helps and Where It Fails**

- Causality vs correlation, rare events, distribution shift and hallucination
- Confident wrong answers under pressure

**Topic 4 — The Autonomy Ladder**

- Assist, recommend, act with approval, act autonomously
- Matching rung to risk and reversibility

**Topic 5 — Measuring Value**

- MTTD, MTTR, noise ratio, toil hours and accepted recommendations
- Avoiding vanity metrics

</details>

**Important concepts**

- *Commands / APIs / Code:* Capability-to-task mapping worksheet; value-metric definitions (illustrative); no commands required
- *Mechanisms & failure scenarios:* Treating a probabilistic suggestion as fact during an incident, automating an unmeasured process, metrics that reward activity instead of reliability, over-trust after early successes.

### S15E02 — Traditional Automation vs AI-Driven Automation

**Depth:** Intermediate  
**Learning objective:** Choose between deterministic and AI-driven automation for an operational task using explicit criteria.  
**Prerequisites:** S15E01, S09E06, S10E13  
**Expected outcome:** Justify, for a given operational task, whether to use a script, a rule, an AI assistant or an agent, and design the fallback.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Deterministic Automation**

- Scripts, runbooks, rules, alerts and infrastructure as code
- Strengths: predictability, testability, auditability

**Topic 2 — AI-Driven Automation**

- Probabilistic, context-sensitive decisions
- Strengths: ambiguity, unstructured data, long-tail variation

**Topic 3 — A Decision Framework**

- Frequency, variability, risk, reversibility and cost of error
- When a rule or script is the better answer

**Topic 4 — Hybrid Patterns**

- Rules first with AI assistance, AI with deterministic fallback, AI proposing and rules validating
- Keeping the deterministic path alive

**Topic 5 — Failure Modes and Costs**

- Nondeterminism, token and latency cost, over-automation and skill atrophy
- Making AI-driven steps observable and replaceable

</details>

**Important concepts**

- *Commands / APIs / Code:* Side-by-side deterministic and AI-assisted remediation flow (illustrative); decision-matrix template
- *Mechanisms & failure scenarios:* Replacing a reliable script with an unpredictable agent, AI steps with no fallback, cost growth from invoking a model on every event, hidden coupling between rules and prompts.

### S15E03 — AI-Powered DevOps Architecture: Telemetry, Context, Reasoning, Action, and Feedback

**Depth:** Intermediate  
**Learning objective:** Draw the reference architecture of an AI-for-operations system and identify its dependencies and failure modes.  
**Prerequisites:** S15E02, S08E19, S09E18, S14E17  
**Expected outcome:** Present a layered AI-for-operations architecture with its context sources, action boundary and failure modes.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Layered Reference Architecture**

- Sources, normalization, context store, reasoning, action and feedback layers
- Control plane and data plane for operations AI

**Topic 2 — Context Engineering for Operations**

- Topology, ownership, change history, runbooks and service catalogs
- Keeping context current and queryable

**Topic 3 — Data Access Patterns**

- Tool queries against live systems, pre-indexed stores and streaming
- Trade-offs in freshness, cost and permissions

**Topic 4 — Where Classical ML and LLMs Belong**

- Detection and forecasting with ML, language tasks with LLMs, orchestration with code
- Avoiding an LLM where a statistic suffices

**Topic 5 — The AI Layer as a Dependency**

- Its own SLOs, rate limits, fallbacks and incident modes
- What happens to operations when the AI layer is down

</details>

**Important concepts**

- *Commands / APIs / Code:* Architecture diagram and data-flow table; service-catalog schema (illustrative)
- *Mechanisms & failure scenarios:* Stale topology giving wrong answers, direct production access from the reasoning layer, a single AI dependency in the incident path, context missing ownership so recommendations reach the wrong team.

### S15E04 — AI-Assisted Engineering Workflows for Operations Teams

**Depth:** Intermediate  
**Learning objective:** Use AI assistants safely in everyday operations work such as runbooks, queries, commands and change authoring.  
**Prerequisites:** S15E03, S09E16, S09E17  
**Expected outcome:** Adopt AI assistance for operations tasks with validation, review and secret-handling rules.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Runbooks and Procedures**

- Drafting, reviewing and testing procedures with AI
- Keeping runbooks accurate and executable

**Topic 2 — Query and Command Authoring**

- PromQL, LogQL, SQL and kubectl suggestions
- Validation before execution and read-only first

**Topic 3 — Change Authoring and Review**

- Explaining diffs, drafting change plans and rollback notes
- Human review of AI-authored changes

**Topic 4 — ChatOps and Knowledge Sharing**

- Assistants in chat, tickets and documentation
- Capturing tribal knowledge without leaking it

**Topic 5 — Guardrails and Measuring Effect**

- Verify before run, secrets handling and review requirements
- Time saved vs defects introduced

</details>

**Important concepts**

- *Commands / APIs / Code:* Prompt and validation wrapper for query generation (illustrative); change-summary template; instruction file for an operations repository (concept)
- *Mechanisms & failure scenarios:* Plausible but wrong queries returning misleading results, commands run without review, secrets pasted into prompts, runbooks that look complete but skip a safety step.

<a id="s15-module-2"></a>

## Module 2 — Intelligent Observability

**4 episodes (S15E05–S15E08) · 20 topics.** This module covers: AI-Powered Log Analysis; Metrics and Trace Intelligence; Alert Correlation and Noise Reduction; Natural-Language Observability and Intelligent Dashboards.

| ID | Episode | Depth |
|---|---|---|
| S15E05 | AI-Powered Log Analysis: Parsing, Templates, Clustering, and LLM Summarization | Intermediate |
| S15E06 | Metrics and Trace Intelligence: Baselines, Anomalies, and Dependency-Aware Analysis | Intermediate |
| S15E07 | Alert Correlation and Noise Reduction | Intermediate |
| S15E08 | Natural-Language Observability and Intelligent Dashboards | Intermediate |

### S15E05 — AI-Powered Log Analysis: Parsing, Templates, Clustering, and LLM Summarization

**Depth:** Intermediate  
**Learning objective:** Turn high-volume logs into understandable signals using parsing, clustering and carefully grounded language models.  
**Prerequisites:** S15E03, S04E12, S04E13, S08E04  
**Expected outcome:** Design a log-analysis pipeline that reduces volume, surfaces novelty, and produces cited summaries safely.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Logs as Data**

- Structure, volume, cost and retention
- Why raw logs overwhelm both humans and models

**Topic 2 — Parsing and Templating**

- Extracting templates from message streams (Drain-style) and normalization
- Handling variable fields, multi-line events and schema drift

**Topic 3 — Clustering and Novelty Detection**

- Embedding log templates and clustering patterns
- Detecting new and rare message types

**Topic 4 — LLM Summarization and Explanation**

- Chunking, selecting representative samples and citing source lines
- Hallucination controls and evidence links

**Topic 5 — Sensitive Data and Cost Control**

- Redacting secrets and personal data before analysis
- Sampling, tiering and budgeting model calls

</details>

**Important concepts**

- *Commands / APIs / Code:* Template-mining pass over sample logs (illustrative), embedding-and-cluster sketch in Python, log-summary prompt with citations; related project series: AIOps Season 2, Episode 3
- *Mechanisms & failure scenarios:* Over-merged templates hiding a rare error, summaries that omit the one decisive line, secrets sent to an external model, model cost growing with log volume.

### S15E06 — Metrics and Trace Intelligence: Baselines, Anomalies, and Dependency-Aware Analysis

**Depth:** Intermediate  
**Learning objective:** Apply baselines, anomaly detection and trace analysis to service telemetry and interpret the results without false confidence.  
**Prerequisites:** S15E05, S04E08, S04E12, S14E14  
**Expected outcome:** Choose and tune a detection approach for service metrics and explain an anomaly using traces and change context.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Dynamic Baselines and Seasonality**

- Learning normal behavior per service and time window
- Handling deploys, holidays and traffic shifts

**Topic 2 — Anomaly Detection for Service Metrics**

- Statistical and machine-learning detectors on SLO-relevant signals
- Choosing sensitivity against alert cost

**Topic 3 — Metric Quality**

- Cardinality, missing data and label hygiene
- Why bad telemetry produces confident nonsense

**Topic 4 — Trace Intelligence**

- Latency attribution, critical paths and service-map inference
- Finding the slow dependency

**Topic 5 — Change Correlation and Tuning**

- Linking anomalies to deployments, configuration and feature flags
- Reducing false positives with feedback

</details>

**Important concepts**

- *Commands / APIs / Code:* Baseline and residual computation on a metric series (illustrative), trace critical-path extraction sketch, change-event join; related project series: AIOps Season 2, Episodes 1–2
- *Mechanisms & failure scenarios:* Anomalies flagged at every deployment, seasonality learned from too little history, high-cardinality labels exploding cost, a slow dependency hidden by averaging.

### S15E07 — Alert Correlation and Noise Reduction

**Depth:** Intermediate  
**Learning objective:** Reduce alert noise through grouping and correlation while measuring the risk of hiding real incidents.  
**Prerequisites:** S15E06  
**Expected outcome:** Design an alert-correlation pipeline and evaluate its noise reduction against missed-incident risk.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Anatomy of Alert Fatigue**

- Duplicate, flapping, symptom and cascading alerts
- Cost to on-call engineers and to reliability

**Topic 2 — Deduplication, Grouping, and Suppression**

- Rules for fingerprints, grouping keys and maintenance windows
- When rules stop scaling

**Topic 3 — Temporal and Topology Correlation**

- Time windows, dependency graphs and shared causes
- Collapsing many alerts into one incident

**Topic 4 — Learned and LLM-Assisted Grouping**

- Embeddings, clustering and language-model summaries of alert groups
- Where learned grouping is helpful and where it is risky

**Topic 5 — Evaluating Noise Reduction**

- Noise ratio vs missed-incident risk
- Feedback loops and ownership routing

</details>

**Important concepts**

- *Commands / APIs / Code:* Alert grouping configuration (illustrative), topology-aware correlation sketch, evaluation of grouped vs raw alerts; related project series: AIOps Season 2, Episode 4
- *Mechanisms & failure scenarios:* Suppression hiding a distinct incident, stale topology causing wrong grouping, silent drops of low-severity alerts that were early warnings, unmeasured noise reduction.

### S15E08 — Natural-Language Observability and Intelligent Dashboards

**Depth:** Intermediate  
**Learning objective:** Build natural-language access to telemetry that is safe, verifiable and honest about its limits.  
**Prerequisites:** S15E06, S08E13, S07E03  
**Expected outcome:** Design a natural-language observability assistant with validation, limits and evidence display.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Natural Language to Query**

- Translating questions into PromQL, LogQL and SQL
- Few-shot patterns and schema grounding

**Topic 2 — Metric and Schema Catalogs as Context**

- Metric names, labels, units and service ownership
- Keeping the catalog accurate

**Topic 3 — Query Safety**

- Read-only access, cost and time limits, query validation
- Preventing expensive or sensitive queries

**Topic 4 — Generated Dashboards and Explanations**

- Choosing visualizations and summarizing what a panel shows
- Showing the query and evidence behind every answer

**Topic 5 — Limits and Verification**

- Wrong aggregations, missing labels and misleading time ranges
- When a human should write the query

</details>

**Important concepts**

- *Commands / APIs / Code:* Question-to-query pipeline with a validator (illustrative), query allowlist and limits configuration
- *Mechanisms & failure scenarios:* A plausible query with the wrong aggregation, an unbounded query overloading the metrics backend, generated dashboards that mislead, answers presented without the underlying query.

<a id="s15-module-3"></a>

## Module 3 — AI-Powered Incident Management

**4 episodes (S15E09–S15E12) · 20 topics.** This module covers: AI-Assisted Incident Investigation; Root-Cause Analysis; Incident Summarization, Timelines, and Handoffs; Incident Response Copilots.

| ID | Episode | Depth |
|---|---|---|
| S15E09 | AI-Assisted Incident Investigation: Evidence, Hypotheses, and Verification | Intermediate |
| S15E10 | Root-Cause Analysis: Topology, Change Context, and Ranked Hypotheses | Advanced |
| S15E11 | Incident Summarization, Timelines, and Handoffs | Intermediate |
| S15E12 | Incident Response Copilots: Roles, ChatOps, and Safe Assistance Under Pressure | Intermediate |

### S15E09 — AI-Assisted Incident Investigation: Evidence, Hypotheses, and Verification

**Depth:** Intermediate  
**Learning objective:** Structure AI assistance during an investigation around gathering evidence, forming hypotheses and verifying them.  
**Prerequisites:** S15E07, S08E09, S09E04, S14E14  
**Expected outcome:** Run an AI-assisted investigation that records evidence, hypotheses and verification, and recognize its failure modes.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Incident Lifecycle and Where AI Assists**

- Detection, triage, diagnosis, mitigation and review
- Tasks that benefit from assistance and tasks that do not

**Topic 2 — Evidence Gathering Tools**

- Logs, metrics, traces, changes and topology as tool calls
- Read-only, bounded and attributable queries

**Topic 3 — Hypothesis Generation and Ranking**

- Proposing explanations and the checks that would confirm or refute them
- Keeping alternatives alive

**Topic 4 — Operational Retrieval**

- Runbooks and past incidents as a corpus (stale documents, citations)
- Grounded recommendations

**Topic 5 — Verification and Failure Modes**

- Stopping criteria and confirmation steps
- Anchoring, fabricated evidence and plausible but wrong stories

</details>

**Important concepts**

- *Commands / APIs / Code:* Investigation loop with evidence tools (illustrative), hypothesis record template, runbook-retrieval query with citations; related project series: AIOps Season 3, Episode 3
- *Mechanisms & failure scenarios:* Anchoring on the first hypothesis, conclusions without checked evidence, retrieval of an outdated runbook, tool errors silently treated as "no data".

### S15E10 — Root-Cause Analysis: Topology, Change Context, and Ranked Hypotheses

**Depth:** Advanced  
**Learning objective:** Rank probable causes using topology, changes and telemetry, and communicate confidence honestly.  
**Prerequisites:** S15E09, S15E06, S04E17  
**Expected outcome:** Design an RCA assistant that ranks causes with evidence and calibrated confidence, and evaluate it on past incidents.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — Correlation vs Causation in Operations**

- Why co-occurring anomalies do not identify the cause
- Using causal reasoning (S04E17) and temporal ordering

**Topic 2 — Topology-Aware RCA**

- Service graphs and failure propagation
- Distinguishing source from symptom

**Topic 3 — Change-Based RCA**

- Deployment, configuration and infrastructure diffs near the onset
- Weighting recent changes appropriately

**Topic 4 — Trace and Log Causality Clues**

- Error origins, retry storms and dependency timeouts
- Combining independent signals

**Topic 5 — Statistical and LLM Reasoning Together**

- Using models to generate and explain hypotheses while statistics score them
- Communicating confidence and uncertainty

**Topic 6 — Evaluating RCA**

- Top-k accuracy, time to first correct hypothesis and calibration
- Replay on historical incidents

</details>

**Important concepts**

- *Commands / APIs / Code:* Graph-based candidate scoring (illustrative), change-correlation query, RCA evaluation harness over historical incidents; related project series: AIOps Season 3, Episode 2
- *Mechanisms & failure scenarios:* Blaming the loudest symptom, ignoring an unrelated deployment, overconfident single answers, evaluation sets that leak the answer.

### S15E11 — Incident Summarization, Timelines, and Handoffs

**Depth:** Intermediate  
**Learning objective:** Produce accurate, evidence-backed incident summaries for different audiences.  
**Prerequisites:** S15E09, S07E19  
**Expected outcome:** Design summarization that is cited, audience-appropriate and safe to circulate.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Timeline Construction**

- Merging alerts, deploys, actions and messages into one ordered record
- Clock skew and missing events

**Topic 2 — Summary Types**

- Live updates, shift handoffs, stakeholder briefs and postmortem drafts
- Different audiences need different content

**Topic 3 — Evidence-Backed Text**

- Citations, uncertainty and "unknown" as a valid statement
- Preventing invented details

**Topic 4 — Evaluation and Learning Capture**

- Measuring accuracy and usefulness of summaries
- Turning incidents into follow-up actions

</details>

**Important concepts**

- *Commands / APIs / Code:* Timeline merge across event sources (illustrative), summary prompt with required citations and an "unknown" field; related project series: AIOps Season 3, Episodes 1 and 4
- *Mechanisms & failure scenarios:* Fabricated causes in a handoff, timelines with misordered events, confidential data in stakeholder summaries, summaries that smooth over uncertainty.

### S15E12 — Incident Response Copilots: Roles, ChatOps, and Safe Assistance Under Pressure

**Depth:** Intermediate  
**Learning objective:** Design an incident copilot that helps responders without adding risk or cognitive load.  
**Prerequisites:** S15E11, S09E11, S10E13  
**Expected outcome:** Specify the roles, interfaces and safety rules of an incident copilot.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Copilot Roles**

- Scribe, investigator, communicator and runbook guide
- Scope each role to what it can do reliably

**Topic 2 — ChatOps and Paging Integrations**

- Assistants in chat channels, ticketing and paging tools
- Commands, confirmations and audit trails

**Topic 3 — Cognitive Load and Automation Bias**

- How assistants help and distract during incidents
- Designing for skepticism

**Topic 4 — Safe Assistance**

- Read-only default, confirmation for actions, bounded permissions
- Behaviour when evidence is missing or contradictory

**Topic 5 — Degradation and Adoption**

- Working when the AI is unavailable
- Building trust through transparency and feedback

</details>

**Important concepts**

- *Commands / APIs / Code:* Chat-command contract for a copilot (illustrative), confirmation flow for sensitive requests; related project series: AIOps Season 3, Episode 7
- *Mechanisms & failure scenarios:* Responders trusting a wrong suggestion under stress, copilots issuing actions without confirmation, noisy assistants distracting the incident channel, no fallback when the service is down.

<a id="s15-module-4"></a>

## Module 4 — AI SRE & Reliability Engineering

**3 episodes (S15E13–S15E15) · 14 topics.** This module covers: AI-Assisted SLO Analysis and Error-Budget Intelligence; Predictive Failure Detection and Early Warning; AI-Assisted Capacity Planning and Reliability Recommendations.

| ID | Episode | Depth |
|---|---|---|
| S15E13 | AI-Assisted SLO Analysis and Error-Budget Intelligence | Intermediate |
| S15E14 | Predictive Failure Detection and Early Warning | Advanced |
| S15E15 | AI-Assisted Capacity Planning and Reliability Recommendations | Intermediate |

### S15E13 — AI-Assisted SLO Analysis and Error-Budget Intelligence

**Depth:** Intermediate  
**Learning objective:** Use AI to analyze SLIs, SLOs and error budgets and communicate reliability status accurately.  
**Prerequisites:** S14E02, S15E06  
**Expected outcome:** Apply AI to SLO and error-budget analysis while keeping the numbers and narratives verifiable.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — SLI Selection and Discovery**

- Candidate indicators from telemetry and user journeys
- Judging whether an indicator reflects user experience

**Topic 2 — Burn-Rate Analysis**

- Multi-window, multi-burn-rate alerting
- Explaining why a budget is burning

**Topic 3 — Error-Budget Forecasting and Policy**

- Projecting budget exhaustion and its decision implications
- Supporting release and freeze decisions

**Topic 4 — Reliability Reporting**

- Narratives for engineering and business audiences
- Accuracy and traceability of generated reports

**Topic 5 — Pitfalls**

- Poor SLIs, optimizing the metric, and averaging away tail failures
- Where human judgment must stay

</details>

**Important concepts**

- *Commands / APIs / Code:* Burn-rate computation (illustrative), SLO definition file, generated reliability summary with source queries
- *Mechanisms & failure scenarios:* A well-computed SLO of the wrong indicator, budget forecasts ignoring seasonality, narratives that overstate certainty, gaming of SLO metrics.

### S15E14 — Predictive Failure Detection and Early Warning

**Depth:** Advanced  
**Learning objective:** Build and evaluate early-warning signals that give useful lead time without drowning responders in false alarms.  
**Prerequisites:** S15E06, S04E09, S04E01  
**Expected outcome:** Design and evaluate a predictive-warning system with defined lead time, precision and alert cost.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Leading Indicators**

- Signals that precede failure: saturation, error trends, retry growth
- Distinguishing predictors from symptoms

**Topic 2 — Forecasting Lead Time and Uncertainty**

- Time-series forecasting for exhaustion and degradation (S04E09)
- Prediction intervals and decision thresholds

**Topic 3 — Framing Prediction from Incident Labels**

- Defining the target from history, class imbalance (S04E01) and leakage
- Evaluating with time-based splits

**Topic 4 — Common Failure Patterns**

- Resource exhaustion, leaks, certificate and quota expiry
- Rule-based vs learned warnings

**Topic 5 — Precision, Recall, and Alert Cost**

- Choosing thresholds against on-call burden
- Drift and revalidation

</details>

**Important concepts**

- *Commands / APIs / Code:* Time-to-exhaustion forecast (illustrative), evaluation of warnings with lead-time and precision; related project series: AIOps Season 2, Episodes 5–6
- *Mechanisms & failure scenarios:* Models trained on incidents that were never labeled, warnings too late to act on, drift after infrastructure change, predictions evaluated on leaked future data.

### S15E15 — AI-Assisted Capacity Planning and Reliability Recommendations

**Depth:** Intermediate  
**Learning objective:** Produce capacity forecasts and evidence-backed reliability recommendations that teams actually act on.  
**Prerequisites:** S15E14, S04E09  
**Expected outcome:** Create capacity and reliability recommendations with forecasts, evidence and an ownership workflow.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Demand Forecasting for Services**

- Growth, seasonality and events
- Forecast error as a planning input

**Topic 2 — Headroom and Saturation**

- Utilization targets, queueing effects and bottleneck identification
- Linking capacity to SLOs

**Topic 3 — Scaling Recommendations**

- Autoscaler settings, node pools and schedule-based capacity
- Explaining each recommendation with its data

**Topic 4 — Reliability Recommendations from Evidence**

- Patterns from incidents and SLO history
- Prioritization, ownership and tracking

</details>

**Important concepts**

- *Commands / APIs / Code:* Capacity forecast with headroom calculation (illustrative), recommendation record schema with evidence links
- *Mechanisms & failure scenarios:* Forecasts that ignore planned launches, recommendations with no owner, savings that break SLOs, generic advice not tied to evidence.

<a id="s15-module-5"></a>

## Module 5 — AI DevOps Agents

**4 episodes (S15E16–S15E19) · 21 topics.** This module covers: Kubernetes Troubleshooting Agents; Infrastructure and Cloud Operations Agents; MCP-Powered DevOps Agents; Human-Approved Remediation.

| ID | Episode | Depth |
|---|---|---|
| S15E16 | Kubernetes Troubleshooting Agents | Advanced |
| S15E17 | Infrastructure and Cloud Operations Agents: Scoped Tools, Least Privilege, and Read-First Design | Advanced |
| S15E18 | MCP-Powered DevOps Agents: Connecting Observability, Clusters, Tickets, and Cloud | Intermediate |
| S15E19 | Human-Approved Remediation: Proposals, Dry Runs, Approvals, and Rollback | Advanced |

### S15E16 — Kubernetes Troubleshooting Agents

**Depth:** Advanced  
**Learning objective:** Design agents that diagnose common Kubernetes failures using scoped read-only tools and sound reasoning.  
**Prerequisites:** S15E10, S09E04, S09E11, S11E17, S13E06  
**Expected outcome:** Specify a Kubernetes troubleshooting agent, its tools, its reasoning loop and how it will be evaluated.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — The Failure Taxonomy**

- Pending, CrashLoopBackOff, OOMKilled, image pull errors, probe failures
- DNS, networking, storage and RBAC problems

**Topic 2 — Diagnostic Workflow as an Agent Loop**

- Describe, events, logs, metrics and rollout history
- Hypothesis, check, conclude

**Topic 3 — Scoped Tools and Redaction**

- Read-only wrappers over the API server and namespaces
- Removing secrets and sensitive data from tool output

**Topic 4 — Fix Proposals vs Actions**

- Manifest diffs and explanations as proposals
- Handing remediation to the approval workflow (S15E19)

**Topic 5 — Evaluation with Fault Injection**

- Reproducible failure scenarios and scoring diagnosis accuracy
- Regression testing agent changes

**Topic 6 — Failure Modes**

- Wrong cluster or namespace, misread events, hallucinated resources
- Prompt injection through logs and labels

</details>

**Important concepts**

- *Commands / APIs / Code:* `kubectl describe`, `kubectl get events`, `kubectl logs` wrapped as read-only tools (illustrative), fault-injection manifests; related project series: AIOps Season 3, Episode 5 and Season 4, Episode 3
- *Mechanisms & failure scenarios:* Diagnosing the wrong namespace, ignoring a node-level cause, agent output trusted without checking events, log content steering the agent.

### S15E17 — Infrastructure and Cloud Operations Agents: Scoped Tools, Least Privilege, and Read-First Design

**Depth:** Advanced  
**Learning objective:** Build operations agents for infrastructure and cloud estates that are useful, bounded and auditable.  
**Prerequisites:** S15E16, S09E03, S10E04, S14E08  
**Expected outcome:** Design an infrastructure and cloud operations agent with least-privilege tools and a read-first workflow.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Operations Tasks Suited to Agents**

- Inventory, configuration checks, certificate expiry, patch status
- Tasks that stay human

**Topic 2 — Cloud Operations Copilots**

- Read-only questions across AWS, Azure and Google Cloud
- Normalizing provider differences behind tools

**Topic 3 — Tool and Credential Design**

- Scoped roles, short-lived credentials and per-tool authorization
- Delegation chains and attribution (S10E04)

**Topic 4 — Query Safety and Cost**

- Limits, pagination and rate handling
- Preventing expensive or sensitive enumerations

**Topic 5 — Configuration-Management Integration**

- Idempotent playbooks as the only action surface
- Dry runs and drift checks

</details>

**Important concepts**

- *Commands / APIs / Code:* Read-only cloud query tool definition (illustrative), role-scoping policy sketch, idempotent playbook invocation; related project series: AIOps Season 4, Episode 4
- *Mechanisms & failure scenarios:* Admin credentials shared with an agent, cross-account confusion, unbounded list calls, actions outside the declared playbook set.

### S15E18 — MCP-Powered DevOps Agents: Connecting Observability, Clusters, Tickets, and Cloud

**Depth:** Intermediate  
**Learning objective:** Compose MCP servers for operations safely and effectively.  
**Prerequisites:** S09E10, S09E17, S15E17  
**Expected outcome:** Specify an MCP tool landscape for operations agents with scopes, audit and injection defenses.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — MCP Servers for Operations**

- Metrics, logs, clusters, tickets, runbooks and cloud APIs
- What belongs in a server vs in the agent

**Topic 2 — Server Design for Operations**

- Read/write separation, scopes and audit
- Per-tool authorization (S09E10)

**Topic 3 — Composing Multiple Servers**

- Context budget, tool selection and naming
- Avoiding overload from dozens of tools

**Topic 4 — Injection Through Telemetry and Tickets**

- Untrusted text in logs, alerts and tickets reaching the model
- Separating data from instructions

**Topic 5 — Registries and Testing**

- Shared server catalogs, versioning and tests
- Governance of who may add a server

</details>

**Important concepts**

- *Commands / APIs / Code:* MCP tool definitions for an observability server (illustrative), server registration concept, allowlist configuration
- *Mechanisms & failure scenarios:* A ticket body steering the agent, write tools exposed alongside read tools, tool-description bloat degrading selection, unvetted servers added by individual users.

### S15E19 — Human-Approved Remediation: Proposals, Dry Runs, Approvals, and Rollback

**Depth:** Advanced  
**Learning objective:** Design the full lifecycle of a remediation that an AI proposes and a human approves.  
**Prerequisites:** S15E17, S09E11, S10E08, S10E14  
**Expected outcome:** Specify a remediation workflow with proposals, dry runs, approvals, verification and rollback.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Remediation Lifecycle**

- Detect, propose, validate, approve, execute, verify and roll back
- Where each stage fails

**Topic 2 — Proposal Quality**

- Evidence, blast radius, alternatives and expected outcome
- Rejecting vague or unsupported proposals

**Topic 3 — Dry Runs, Diffs, and Policy Checks**

- Previewing effects and validating against policy
- Idempotency and preconditions

**Topic 4 — Approval Design**

- Who approves what, expiry, escalation and approval fatigue
- Interfaces that show evidence, not just a button

**Topic 5 — Execution, Audit, and Verification**

- Scoped execution, audit records and post-action telemetry checks
- Automatic rollback criteria

</details>

**Important concepts**

- *Commands / APIs / Code:* Remediation proposal schema, approval-gated runbook execution (illustrative), post-action verification check; related project series: AIOps Season 4, Episodes 1–5
- *Mechanisms & failure scenarios:* Approvals granted without reading evidence, an expired approval executed, success declared without verification, rollback path untested.

<a id="s15-module-6"></a>

## Module 6 — AI-Powered CI/CD

**4 episodes (S15E20–S15E23) · 19 topics.** This module covers: Pipeline Failure Analysis; Intelligent Build and Test Analysis; Deployment Risk Assessment; AI-Assisted Release Management and Progressive Delivery Decisions.

| ID | Episode | Depth |
|---|---|---|
| S15E20 | Pipeline Failure Analysis: Log Triage, Failure Classification, and Flaky Tests | Intermediate |
| S15E21 | Intelligent Build and Test Analysis: Test Selection, Impact Analysis, and Quality Signals | Intermediate |
| S15E22 | Deployment Risk Assessment | Advanced |
| S15E23 | AI-Assisted Release Management and Progressive Delivery Decisions | Intermediate |

### S15E20 — Pipeline Failure Analysis: Log Triage, Failure Classification, and Flaky Tests

**Depth:** Intermediate  
**Learning objective:** Classify and diagnose CI failures faster, including distinguishing flaky tests from real regressions.  
**Prerequisites:** S15E05, S09E16  
**Expected outcome:** Design a pipeline failure-analysis system with classification, flaky-test handling and safe fix suggestions.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — A CI Failure Taxonomy**

- Build, test, infrastructure, configuration, dependency and flaky failures
- Different failure types need different responses

**Topic 2 — Log Triage**

- Extracting the failing step and decisive lines
- Clustering failures across runs and using LLM summaries with citations

**Topic 3 — Flaky-Test Detection**

- Rerun statistics, history and quarantine policies
- Cost of ignoring vs masking flakiness

**Topic 4 — Linking Failures to Changes**

- Bisecting commits and mapping failures to owners
- Fix suggestions and the boundary of automatic pull requests

**Topic 5 — Metrics**

- Time to green, rerun rate and failure recurrence
- Avoiding gaming

</details>

**Important concepts**

- *Commands / APIs / Code:* Failure classifier over build logs (illustrative), flaky-test scoring from run history, failure-to-commit linkage
- *Mechanisms & failure scenarios:* Misclassifying an infrastructure fault as a code failure, quarantining a real regression as flaky, auto-fixes that mask the root cause, summaries ignoring the decisive log line.

### S15E21 — Intelligent Build and Test Analysis: Test Selection, Impact Analysis, and Quality Signals

**Depth:** Intermediate  
**Learning objective:** Use history and code structure to run fewer, better tests and read quality signals correctly.  
**Prerequisites:** S15E20  
**Expected outcome:** Design a test-selection and quality-analysis approach with safety nets and honest metrics.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Change-Impact Analysis**

- Dependency graphs and affected components
- Limits of static analysis

**Topic 2 — Predictive Test Selection**

- Learning from history which tests catch which changes
- Safety nets and periodic full runs

**Topic 3 — Build Duration and Cache Analysis**

- Predicting and reducing build time
- Cache invalidation patterns

**Topic 4 — Test-Quality Signals**

- Coverage, mutation testing and flakiness
- AI-generated tests: value and risks

</details>

**Important concepts**

- *Commands / APIs / Code:* Test-selection scoring from change and failure history (illustrative), coverage and mutation-score interpretation
- *Mechanisms & failure scenarios:* Selected tests miss a regression, coverage used as quality proof, generated tests that assert current buggy behavior, optimization that erodes confidence.

### S15E22 — Deployment Risk Assessment

**Depth:** Advanced  
**Learning objective:** Estimate the risk of a change before deployment and use the estimate in gates without eroding developer trust.  
**Prerequisites:** S15E21, S04E02, S11E13  
**Expected outcome:** Design a calibrated deployment-risk system and integrate it with progressive delivery.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Risk Features**

- Change size, files touched, ownership, timing, dependencies and history
- Blast radius and rollback complexity

**Topic 2 — Scoring Approaches**

- Heuristics, supervised models and LLM-assisted explanations
- Why explanations must come from the features

**Topic 3 — Calibrating Risk**

- Probability calibration (S04E02) and thresholds
- Measuring against actual incident outcomes

**Topic 4 — Using Risk in Delivery**

- Gates, canaries, approvals and change windows
- Progressive delivery integration

**Topic 5 — Trust and Feedback**

- False positives and developer experience
- Learning from incidents and near misses

</details>

**Important concepts**

- *Commands / APIs / Code:* Change-risk feature extraction (illustrative), calibration plot of scores against outcomes, gate policy configuration
- *Mechanisms & failure scenarios:* Scores that merely track change size, uncalibrated "high risk" labels, blocking low-risk work unnecessarily, no feedback from real incidents.

### S15E23 — AI-Assisted Release Management and Progressive Delivery Decisions

**Depth:** Intermediate  
**Learning objective:** Apply AI to release notes, change review and progressive-delivery judgments with clear accountability.  
**Prerequisites:** S15E22  
**Expected outcome:** Design AI-assisted release and canary decisions with verification and accountability.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Release Notes and Change Summaries**

- Generating accurate notes from commits and tickets
- Verifying against the actual diff

**Topic 2 — Change Review and Approval Assistance**

- Summarizing risk, dependencies and test evidence for approvers
- Keeping the human decision explicit

**Topic 3 — Canary Analysis and Automated Judgment**

- Comparing canary and baseline metrics
- Statistical judgment with explanations

**Topic 4 — Rollback Decision Support**

- Recommending rollback or proceed with evidence
- Avoiding premature or late rollback

**Topic 5 — Governance and Audit**

- Release calendars, conflicts and audit trail
- Who is accountable for an AI-influenced release decision

</details>

**Important concepts**

- *Commands / APIs / Code:* Canary-versus-baseline comparison (illustrative), release-note generation with diff verification, rollback recommendation record
- *Mechanisms & failure scenarios:* Release notes describing changes that were not shipped, canary judgments on too little traffic, over-trust in an automated "pass", unclear accountability.

<a id="s15-module-7"></a>

## Module 7 — AI Infrastructure Automation & FinOps

**3 episodes (S15E24–S15E26) · 15 topics.** This module covers: Terraform and IaC Assistants; Cloud Resource Optimization with AI; Cost Anomaly Detection and Intelligent Cloud Operations.

| ID | Episode | Depth |
|---|---|---|
| S15E24 | Terraform and IaC Assistants: Generation, Review, Plan Analysis, and Drift Explanation | Advanced |
| S15E25 | Cloud Resource Optimization with AI: Rightsizing, Waste Detection, and Safe Recommendations | Intermediate |
| S15E26 | Cost Anomaly Detection and Intelligent Cloud Operations | Intermediate |

### S15E24 — Terraform and IaC Assistants: Generation, Review, Plan Analysis, and Drift Explanation

**Depth:** Advanced  
**Learning objective:** Use AI to author, review and explain infrastructure as code safely, including AI-assisted provisioning workflows.  
**Prerequisites:** S15E19, S13E19, S09E16  
**Expected outcome:** Design an AI-assisted infrastructure workflow where generation is validated, plans are explained and apply requires approval.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — Where AI Helps in Infrastructure as Code**

- Drafting, refactoring, documenting and reviewing
- Tasks where a human must lead

**Topic 2 — Generation and Its Failure Modes**

- Hallucinated resources and arguments, insecure defaults and version drift
- Pinning providers and validating against schemas

**Topic 3 — Review with Static Analysis and Policy**

- Policy as code, security scanning and cost checks
- AI explanations layered over deterministic checks

**Topic 4 — Plan Analysis and Blast Radius**

- Reading plans, flagging destructive changes and explaining impact
- Human approval of plans

**Topic 5 — Drift Explanation and Remediation Proposals**

- Detecting drift, explaining its likely cause and proposing a fix
- Never auto-applying

**Topic 6 — AI-Assisted Provisioning Workflows**

- Environments, modules, approvals and a validation pipeline
- Auditing AI-authored infrastructure changes

</details>

**Important concepts**

- *Commands / APIs / Code:* `terraform fmt`, `validate`, `plan` and policy-check pipeline (illustrative), plan-summary prompt grounded in the plan JSON, provider version pinning
- *Mechanisms & failure scenarios:* Generated code referencing nonexistent arguments, public storage or open security groups from defaults, a plan summary that hides a destroy, applying AI changes without human plan review.

### S15E25 — Cloud Resource Optimization with AI: Rightsizing, Waste Detection, and Safe Recommendations

**Depth:** Intermediate  
**Learning objective:** Find and act on cloud waste with recommendations that respect performance and risk.  
**Prerequisites:** S15E15, S13E21  
**Expected outcome:** Design a cloud-optimization workflow with safe recommendations, approvals and measured results.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Utilization Data and Signal Quality**

- CPU, memory, I/O and request-level metrics
- Why peaks, seasonality and sampling matter

**Topic 2 — Rightsizing**

- Models and rules for sizing compute, storage and databases
- Performance headroom and SLO constraints

**Topic 3 — Idle and Waste Detection**

- Unattached resources, over-retention and unused capacity
- Ownership before deletion

**Topic 4 — Commitments and Purchase Recommendations**

- Reservations and savings commitments from forecast demand
- Regret of over-commitment

**Topic 5 — From Recommendation to Action**

- Approval loops, staged changes and rollback
- Measuring realized savings

</details>

**Important concepts**

- *Commands / APIs / Code:* Rightsizing recommendation computation over utilization percentiles (illustrative), waste-detection query, savings tracking record
- *Mechanisms & failure scenarios:* Rightsizing on a quiet week, deleting a resource with an unknown owner, commitments sized to a transient peak, savings claimed but not realized.

### S15E26 — Cost Anomaly Detection and Intelligent Cloud Operations

**Depth:** Intermediate  
**Learning objective:** Detect and explain cost anomalies and triage cloud configuration issues with AI.  
**Prerequisites:** S15E25, S15E06  
**Expected outcome:** Design a cost-anomaly and cloud-triage system with grounded explanations and ownership routing.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Cost Data Model**

- Tags, allocation, billing exports and shared costs
- Why allocation quality bounds everything else

**Topic 2 — Anomaly Detection on Spend**

- Seasonality, deployments and expected growth
- Alert thresholds and false positives

**Topic 3 — Explaining a Cost Change**

- Attributing change to service, team or deployment
- LLM-assisted narrative grounded in data

**Topic 4 — Cloud Configuration and Posture Triage**

- Drift, compliance findings and risk ranking
- Routing to the right owner

</details>

**Important concepts**

- *Commands / APIs / Code:* Cost-series anomaly detection (illustrative), attribution query over a billing export, finding-triage ranking; related project series: AIOps Season 3, Episode 6
- *Mechanisms & failure scenarios:* Untagged spend that cannot be attributed, alerts on every month-end, explanations that guess a cause, findings sent to no one.

<a id="s15-module-8"></a>

## Module 8 — Enterprise AIOps Architecture

**6 episodes (S15E27–S15E32) · 31 topics.** This module covers: Enterprise AIOps Reference Architecture; Orchestrating Operations Agents; Operational Governance, Security, and Permissions for Operations AI; Human-in-the-Loop Operations; Safe Autonomous Remediation; Evaluating and Adopting AIOps.

| ID | Episode | Depth |
|---|---|---|
| S15E27 | Enterprise AIOps Reference Architecture | Advanced |
| S15E28 | Orchestrating Operations Agents: Specialist Agents, Routing, and Shared Context | Advanced |
| S15E29 | Operational Governance, Security, and Permissions for Operations AI | Advanced |
| S15E30 | Human-in-the-Loop Operations: Operating Models, Trust, and Automation Bias | Intermediate |
| S15E31 | Safe Autonomous Remediation: Autonomy Tiers, Safety Budgets, and Kill Switches | Advanced |
| S15E32 | Evaluating and Adopting AIOps: Metrics, Shadow Mode, and Business Value | Intermediate |

### S15E27 — Enterprise AIOps Reference Architecture

**Depth:** Advanced  
**Learning objective:** Design an enterprise-scale AIOps platform that integrates data, shared AI services, operations tools and teams.  
**Prerequisites:** S15E03, S14E17, S12E11  
**Expected outcome:** Present and critique an enterprise AIOps reference architecture and an adoption roadmap.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Platform Layers**

- Data, context, intelligence, action and experience layers
- Boundaries between layers

**Topic 2 — The Data and Context Platform**

- Service catalog, topology, ownership and change history
- Keeping context authoritative

**Topic 3 — Shared AI Services**

- Model gateway, retrieval, evaluation and observability reused from earlier seasons
- Avoiding per-team duplication

**Topic 4 — Integration with Operations Tooling**

- Monitoring, ITSM, CI/CD and ChatOps
- Contracts and failure isolation

**Topic 5 — Multi-Tenancy, Scale, and Adoption**

- Isolation, quotas and cost attribution
- Build vs buy and phased adoption

</details>

**Important concepts**

- *Commands / APIs / Code:* Reference architecture and capability map; integration contract examples (illustrative)
- *Mechanisms & failure scenarios:* A central platform becoming an incident bottleneck, inconsistent topology across teams, unmetered model usage, tools integrated with no failure isolation.

### S15E28 — Orchestrating Operations Agents: Specialist Agents, Routing, and Shared Context

**Depth:** Advanced  
**Learning objective:** Coordinate multiple operations agents without losing control, context or accountability.  
**Prerequisites:** S10E01, S10E02, S10E08, S15E18  
**Expected outcome:** Design a multi-agent operations system with routing, shared state and conflict control.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Specialist Agents**

- Observability, Kubernetes, cloud, CI/CD and cost specialists
- Scope and tools per specialist

**Topic 2 — Routing and Supervision**

- Selecting specialists, escalation and termination
- Avoiding delegation loops

**Topic 3 — Shared Incident State and Handoff**

- A common record of evidence, hypotheses and actions
- Context passing and what to withhold

**Topic 4 — Coordination, Conflict, and Durability**

- Preventing conflicting actions on the same system
- Long-running workflows and recovery

**Topic 5 — Cost and Latency**

- Token and tool-call economics across agents
- When one agent is enough

</details>

**Important concepts**

- *Commands / APIs / Code:* Typed handoff message between specialists (illustrative), shared incident-state schema, action lock concept
- *Mechanisms & failure scenarios:* Two agents acting on the same resource, lost context at handoff, delegation loops during an incident, cost explosion from redundant investigation.

### S15E29 — Operational Governance, Security, and Permissions for Operations AI

**Depth:** Advanced  
**Learning objective:** Govern operations AI with identity, tiered permissions, data handling and audit appropriate to its power over production.  
**Prerequisites:** S14E08, S14E13, S09E12, S10E14  
**Expected outcome:** Define an identity, permission, data-handling and audit model for operations AI.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Identity and Delegation**

- Agent identities, on-behalf-of access and short-lived credentials
- Attribution of every action

**Topic 2 — Permission Tiers by Action Risk**

- Read, propose, execute-with-approval and autonomous classes
- Mapping tiers to systems and environments

**Topic 3 — Secrets and Operational Data**

- Redaction, retention and residency of telemetry sent to models
- Vendor and model data-handling terms

**Topic 4 — Threats Specific to Operations AI**

- Prompt injection through telemetry and tickets (S09E12)
- Tool abuse and privilege escalation

**Topic 5 — Audit, Evidence, and Change Management**

- Evidence for auditors, links to change records and approvals
- Compliance integration (S14E13)

</details>

**Important concepts**

- *Commands / APIs / Code:* Permission-tier policy table (illustrative), audit record schema, redaction rules
- *Mechanisms & failure scenarios:* Agents inheriting broad admin rights, operational data leaking to external models, audit logs lacking the reasoning behind an action, policy bypass through a new tool.

### S15E30 — Human-in-the-Loop Operations: Operating Models, Trust, and Automation Bias

**Depth:** Intermediate  
**Learning objective:** Organize people and processes around AI so humans stay effective, informed and accountable.  
**Prerequisites:** S15E19, S15E12  
**Expected outcome:** Specify the operating model, approval experience and training that keep humans effective alongside AI.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — On-Call Roles with AI**

- Who does what when an assistant is in the loop
- Accountability for AI-influenced decisions

**Topic 2 — Approval Experience and Escalation**

- Designing approval screens, expiry and escalation paths
- Reducing approval fatigue without reducing scrutiny

**Topic 3 — Trust Calibration and Automation Bias**

- Detecting over-reliance and under-reliance
- Training responders to challenge suggestions

**Topic 4 — Skills, Toil, and Feedback**

- Preventing skill atrophy and capturing corrections
- Using feedback to improve the system

**Topic 5 — Degraded Mode**

- Operating when the AI layer is unavailable or wrong
- Regular practice of manual procedures

</details>

**Important concepts**

- *Commands / APIs / Code:* Responsibility matrix (RACI) for AI-assisted incidents, game-day scenario with the AI layer disabled
- *Mechanisms & failure scenarios:* Rubber-stamp approvals, responders unable to operate without the assistant, feedback never reaching the system, unclear ownership of automated actions.

### S15E31 — Safe Autonomous Remediation: Autonomy Tiers, Safety Budgets, and Kill Switches

**Depth:** Advanced  
**Learning objective:** Decide when automation may act without approval and engineer the controls that keep it safe.  
**Prerequisites:** S15E19, S15E29, S10E14  
**Expected outcome:** Define autonomy tiers, safety budgets, verification and containment for safe autonomous remediation.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — Autonomy Tiers and Promotion Criteria**

- Evidence required to move an action to a higher tier
- Demotion triggers

**Topic 2 — Actions Safe to Automate**

- Idempotent, reversible and bounded actions
- Exclusion lists

**Topic 3 — Safety Budgets and Rate Limits**

- Limits on frequency, scope and blast radius per interval
- Backoff and escalation to a human

**Topic 4 — Verification and Automatic Rollback**

- Post-action telemetry checks and rollback criteria
- Preventing remediation loops

**Topic 5 — Chaos Testing Autonomous Operations**

- Fault injection against the automation itself
- Validating kill switches

**Topic 6 — Containment and Review**

- Kill switches, quarantine and incident review of autonomy failures
- Feeding lessons back into tiers

</details>

**Important concepts**

- *Commands / APIs / Code:* Autonomy-tier policy and safety-budget configuration (illustrative), kill-switch check, rollback verification; related project series: AIOps Season 4, Episodes 6–7
- *Mechanisms & failure scenarios:* A remediation loop that repeats an ineffective restart, budget limits never enforced, kill switch unreachable during the incident, autonomy promoted on a few lucky successes.

### S15E32 — Evaluating and Adopting AIOps: Metrics, Shadow Mode, and Business Value

**Depth:** Intermediate  
**Learning objective:** Measure whether operations AI works and adopt it incrementally with evidence.  
**Prerequisites:** S15E27, S12E06, S14E16  
**Expected outcome:** Build an evidence-based evaluation and adoption plan for an AIOps capability.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Operational Metrics**

- MTTD, MTTR, noise ratio, RCA accuracy, accepted recommendations and toil
- Leading and lagging indicators

**Topic 2 — Offline Replay, Shadow Mode, and Canary**

- Replaying historical incidents
- Running recommendations in shadow before acting

**Topic 3 — Evaluation Datasets from Incidents**

- Building labeled sets from postmortems
- Avoiding leakage and survivorship bias

**Topic 4 — Cost-Benefit and ROI**

- Model, platform and review cost against time saved and incidents avoided
- Counterfactual baselines (S14E16)

**Topic 5 — Adoption Roadmap and Selection Criteria**

- Phasing from assist to act
- Evaluating tools and vendors by evidence rather than demos

</details>

**Important concepts**

- *Commands / APIs / Code:* Shadow-mode comparison harness (illustrative), incident replay evaluation, ROI worksheet
- *Mechanisms & failure scenarios:* Metrics improving because incidents were reclassified, shadow results that ignore human corrections, evaluating on incidents the system already saw, benefits claimed without a baseline.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s15-module-1) | Starting point of the season |
| [Module 2](#s15-module-2) | [Module 1](#s15-module-1) (S15E03) |
| [Module 3](#s15-module-3) | [Module 2](#s15-module-2) (S15E06, S15E07) |
| [Module 4](#s15-module-4) | [Module 2](#s15-module-2) (S15E06) |
| [Module 5](#s15-module-5) | [Module 3](#s15-module-3) (S15E10) |
| [Module 6](#s15-module-6) | [Module 2](#s15-module-2) (S15E05) |
| [Module 7](#s15-module-7) | [Module 2](#s15-module-2) (S15E06); [Module 4](#s15-module-4) (S15E15); [Module 5](#s15-module-5) (S15E19) |
| [Module 8](#s15-module-8) | [Module 1](#s15-module-1) (S15E03); [Module 3](#s15-module-3) (S15E12); [Module 5](#s15-module-5) (S15E18, S15E19) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 14 — Production AI Systems, Security & Governance](../season-14-production-ai-systems/roadmap.md)
- **Next:** none — this is the final season.
- **Draws on:** [Season 4](../season-04-advanced-ml-engineering/roadmap.md) (S04E01, S04E02, S04E08, S04E09, S04E12, S04E13, S04E17); [Season 6](../season-06-llms-and-transformers/roadmap.md) (S06E21); [Season 7](../season-07-generative-ai-engineering/roadmap.md) (S07E03, S07E19); [Season 8](../season-08-rag-engineering/roadmap.md) (S08E04, S08E09, S08E13, S08E19); [Season 9](../season-09-ai-agents-and-mcp/roadmap.md) (S09E03, S09E04, S09E06, S09E10, S09E11, S09E12, S09E16, S09E17, S09E18); [Season 10](../season-10-advanced-agentic-ai/roadmap.md) (S10E01, S10E02, S10E04, S10E08, S10E13, S10E14); [Season 11](../season-11-mlops-engineering/roadmap.md) (S11E13, S11E17); [Season 12](../season-12-llmops-engineering/roadmap.md) (S12E06, S12E11); [Season 13](../season-13-ai-infrastructure/roadmap.md) (S13E06, S13E19, S13E21); [Season 14](../season-14-production-ai-systems/roadmap.md) (S14E02, S14E08, S14E13, S14E14, S14E16, S14E17)
- **Required by:** no later season lists an episode of this season as a prerequisite.
