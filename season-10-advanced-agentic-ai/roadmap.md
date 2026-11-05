# Season 10 Roadmap — Advanced Agentic AI

[← Season 10 overview](README.md) · [All seasons](../README.md)

**4 modules · 15 episodes · 58 topics · 154 subtopics · Level: Advanced**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Multi-Agent Systems](#s10-module-1)
- [Module 2 — Reasoning, Memory, and Learning](#s10-module-2)
- [Module 3 — Reliability and Economics](#s10-module-3)
- [Module 4 — Agent Systems in the Enterprise](#s10-module-4)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Cover the engineering of agent systems beyond one loop: multi-agent coordination and protocols, identity and trust, advanced planning and learning, durable long-running execution, evaluation at scale, cost economics, and enterprise governance. Assumes Season 9.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S10E01 | Decide when multiple agents beat one, and choose a coordination topology. |
| S10E02 | Design the interfaces between agents so collaboration is reliable and debuggable. |
| S10E03 | Understand how independently built agents interoperate across organizational boundaries. |
| S10E04 | Make clear who an agent is acting as, with what authority, and how far that authority extends. |
| S10E05 | Use deliberate reasoning and search where simple loops fail, understanding cost and benefit. |
| S10E06 | Build persistent memory that stays accurate, relevant and safe over long horizons. |
| S10E07 | Improve agents over time using feedback loops without destabilizing them. |
| S10E08 | Run agent tasks that last minutes to days without losing progress or repeating side effects. |
| S10E09 | Build evaluation infrastructure that keeps pace with changing prompts, tools and models. |
| S10E10 | Predict and control what an agent costs and how long it takes. |
| S10E11 | Combine retrieval, tools and reasoning to answer multi-step questions over enterprise knowledge. |
| S10E12 | Understand the shared platform services an organization needs to run many agents. |
| S10E13 | Understand when visual and low-code workflow automation is the right execution model for AI, how such workflows integrate APIs, models, tools and humans, and how to operate them reliably and under governance. |
| S10E14 | Match the level of autonomy to risk and produce evidence that controls work. |
| S10E15 | Integrate multi-agent coordination, protocols, memory, durability, evaluation and governance into one architecture. |

## Prerequisites and Expected Knowledge

- **Season 5 — [Deep Learning & Neural Networks](../season-05-deep-learning/roadmap.md)**: S05E23
- **Season 6 — [LLMs & Transformer Architecture](../season-06-llms-and-transformers/roadmap.md)**: S06E12, S06E20
- **Season 7 — [Generative AI Application Engineering](../season-07-generative-ai-engineering/roadmap.md)**: S07E09
- **Season 8 — [RAG Engineering](../season-08-rag-engineering/roadmap.md)**: S08E11, S08E18
- **Season 9 — [AI Agents, Tool Calling & MCP](../season-09-ai-agents-and-mcp/roadmap.md)**: S09E05, S09E06, S09E07, S09E08, S09E09, S09E11, S09E13, S09E14, S09E18

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Multi-Agent Systems](#s10-module-1) | S10E01–S10E04 | 4 | 1 Intermediate, 3 Advanced |
| 2 | [Reasoning, Memory, and Learning](#s10-module-2) | S10E05–S10E07 | 3 | 3 Advanced |
| 3 | [Reliability and Economics](#s10-module-3) | S10E08–S10E10 | 3 | 2 Advanced, 1 Intermediate |
| 4 | [Agent Systems in the Enterprise](#s10-module-4) | S10E11–S10E15 | 5 | 3 Advanced, 2 Intermediate |

<a id="s10-module-1"></a>

## Module 1 — Multi-Agent Systems

**4 episodes (S10E01–S10E04) · 14 topics.** This module covers: Multi-Agent Patterns; Agent Communication, Shared State, and Message Contracts; Agent-to-Agent Protocols; Agent Identity, Delegation, and Trust Boundaries.

| ID | Episode | Depth |
|---|---|---|
| S10E01 | Multi-Agent Patterns: Supervisor, Peer, and Hierarchical Designs | Intermediate |
| S10E02 | Agent Communication, Shared State, and Message Contracts | Advanced |
| S10E03 | Agent-to-Agent Protocols: Discovery, Task Lifecycle, and Streaming | Advanced |
| S10E04 | Agent Identity, Delegation, and Trust Boundaries | Advanced |

### S10E01 — Multi-Agent Patterns: Supervisor, Peer, and Hierarchical Designs

**Depth:** Intermediate  
**Learning objective:** Decide when multiple agents beat one, and choose a coordination topology.  
**Prerequisites:** S09E06, S09E18  
**Expected outcome:** Select and justify a multi-agent topology and bound its failure modes.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Why Multiple Agents**

- Specialization, context isolation and parallelism
- Costs: coordination overhead and error compounding
- When one agent with more tools is better

**Topic 2 — Topologies and Collaboration Patterns**

- Supervisor/worker, peer-to-peer, hierarchical and pipeline
- Handoffs and routing
- Debate, critic and reviewer patterns
- Role design and prompt boundaries

**Topic 3 — Failure Modes**

- Miscommunication and lost context at handoffs
- Cascading errors, runaway cost, deadlock and termination

</details>

**Important concepts**

- *Commands / APIs / Code:* supervisor-worker skeleton with typed handoff messages (concept)
- *Mechanisms & failure scenarios:* Agents endlessly delegating to each other, contradictory outputs, unclear ownership of the final answer.

### S10E02 — Agent Communication, Shared State, and Message Contracts

**Depth:** Advanced  
**Learning objective:** Design the interfaces between agents so collaboration is reliable and debuggable.  
**Prerequisites:** S10E01, S09E05  
**Expected outcome:** Specify message contracts and shared-state rules for a multi-agent system.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Communication Styles**

- Direct messaging, shared memory/blackboard and event bus
- Synchronous vs asynchronous collaboration

**Topic 2 — Message Contracts**

- Typed task and result schemas; natural language vs structured messages
- Versioning and validation

**Topic 3 — Context Passing and State Consistency**

- What to share and what to withhold
- Summaries and artifact references
- Concurrent updates and conflicts
- Partial failure, timeouts and idempotent task handling

</details>

**Important concepts**

- *Commands / APIs / Code:* Pydantic message schemas for tasks and results, queue-based agent messaging (concept)
- *Mechanisms & failure scenarios:* Free-text handoffs losing constraints, race conditions on shared state, silent schema drift between agents.

### S10E03 — Agent-to-Agent Protocols: Discovery, Task Lifecycle, and Streaming

**Depth:** Advanced  
**Learning objective:** Understand how independently built agents interoperate across organizational boundaries.  
**Prerequisites:** S10E02, S09E09  
**Expected outcome:** Explain A2A-style interoperability and how it differs from tool protocols such as MCP.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Why Protocols, Discovery and Capabilities**

- Interoperability beyond a single framework
- Relationship to MCP (agent-to-tool vs agent-to-agent)
- Agent cards and capability advertisement
- Opaque agents

**Topic 2 — Task Lifecycle**

- Task creation, states and artifacts
- Streaming, long-running tasks and notifications

**Topic 3 — Operational Concerns**

- Authentication between agents
- Versioning and compatibility
- Partial results and failure semantics

</details>

**Important concepts**

- *Commands / APIs / Code:* protocol message examples (illustrative; verify against current specification)
- *Mechanisms & failure scenarios:* Capability claims that do not match behavior, task state divergence, unauthenticated remote agents.

### S10E04 — Agent Identity, Delegation, and Trust Boundaries

**Depth:** Advanced  
**Learning objective:** Make clear who an agent is acting as, with what authority, and how far that authority extends.  
**Prerequisites:** S10E03, S09E11  
**Expected outcome:** Design an identity and delegation model for agents with traceable, narrowing authority.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Identity**

- Workload identity for agents
- Short-lived, scoped credentials

**Topic 2 — Delegation**

- On-behalf-of delegation vs the agent's own authority
- Token exchange concepts

**Topic 3 — Delegation Chains**

- Authority narrowing across hops
- Attribution in audit logs

**Topic 4 — Trust Models**

- Trusted vs untrusted agents and tools
- Cross-tenant and cross-organization agents

**Topic 5 — Revocation and Containment**

- Revoking access mid-task
- Limiting blast radius

</details>

**Important concepts**

- *Commands / APIs / Code:* token-exchange flow sketch, delegation-chain audit record
- *Mechanisms & failure scenarios:* Privilege accumulating across hops, shared credentials hiding who acted, long-lived tokens in agent memory.

<a id="s10-module-2"></a>

## Module 2 — Reasoning, Memory, and Learning

**3 episodes (S10E05–S10E07) · 10 topics.** This module covers: Advanced Planning and Reasoning for Agents; Long-Term Memory Systems and Knowledge Graphs for Agents; Learning from Feedback.

| ID | Episode | Depth |
|---|---|---|
| S10E05 | Advanced Planning and Reasoning for Agents: Search and Test-Time Compute | Advanced |
| S10E06 | Long-Term Memory Systems and Knowledge Graphs for Agents | Advanced |
| S10E07 | Learning from Feedback: Reflection, Preference Data, and Agent Fine-Tuning | Advanced |

### S10E05 — Advanced Planning and Reasoning for Agents: Search and Test-Time Compute

**Depth:** Advanced  
**Learning objective:** Use deliberate reasoning and search where simple loops fail, understanding cost and benefit.  
**Prerequisites:** S06E20, S09E07  
**Expected outcome:** Decide when planning search is worth its cost and how to verify candidate plans.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Search over Plans with Verifiers**

- Tree and graph search over actions or thoughts
- Sampling multiple trajectories and selection
- Verifier- and reward-guided selection
- Best-of-n and its cost

**Topic 2 — Reasoning Models in Agents**

- Where reasoning models help planning
- Budgeting reasoning tokens; combining fast and slow models

**Topic 3 — Limits**

- Combinatorial cost
- Unreliable self-evaluation
- Environments that do not allow backtracking

</details>

**Important concepts**

- *Commands / APIs / Code:* best-of-n with verifier (concept), plan-search sketch
- *Mechanisms & failure scenarios:* Search spending large budgets on unverifiable steps, irreversible actions explored in the real environment.

### S10E06 — Long-Term Memory Systems and Knowledge Graphs for Agents

**Depth:** Advanced  
**Learning objective:** Build persistent memory that stays accurate, relevant and safe over long horizons.  
**Prerequisites:** S09E05, S08E11  
**Expected outcome:** Design a long-term memory subsystem with provenance, update and deletion rules.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Memory Architectures**

- Episodic logs, semantic stores and entity/relationship graphs
- Consolidation and summarization

**Topic 2 — Retrieval Policies**

- Recency, relevance and importance scoring
- Hybrid retrieval over episodic and semantic memory
- Context-budget-aware recall

**Topic 3 — Maintenance**

- Updating, versioning and invalidating memories
- Conflict resolution and provenance
- Forgetting and retention rules

**Topic 4 — Risks and Evaluation**

- Memory poisoning, contamination and cross-user leakage
- Evaluating memory quality

</details>

**Important concepts**

- *Commands / APIs / Code:* memory consolidation job (concept), provenance-tagged memory record
- *Mechanisms & failure scenarios:* Outdated facts overriding new ones, injected memories persisting across sessions, graph drift from extraction errors.

### S10E07 — Learning from Feedback: Reflection, Preference Data, and Agent Fine-Tuning

**Depth:** Advanced  
**Learning objective:** Improve agents over time using feedback loops without destabilizing them.  
**Prerequisites:** S09E13, S06E12, S05E23  
**Expected outcome:** Plan a safe improvement loop for an agent using logged trajectories and evaluations.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Feedback Sources and Prompt and Tool Refinement**

- Explicit ratings, implicit signals and outcome verification
- Bias and noise in feedback
- Prompt and tool-description refinement from failures
- Few-shot memory of successful trajectories

**Topic 2 — Training-Based Improvement**

- Fine-tuning for tool use
- Reinforcement learning with verifiable rewards (concept; builds on S05E23)

**Topic 3 — Safe Iteration**

- Regression testing before rollout
- Reward hacking and training on one's own flawed successes
- Versioned releases and rollback

</details>

**Important concepts**

- *Commands / APIs / Code:* trajectory dataset curation script, evaluation gate (concept)
- *Mechanisms & failure scenarios:* Training on its own flawed successes, optimizing for proxy rewards, regressions on rare tasks.

<a id="s10-module-3"></a>

## Module 3 — Reliability and Economics

**3 episodes (S10E08–S10E10) · 13 topics.** This module covers: Durable Execution; Agent Evaluation at Scale; Cost, Latency, and Token Economics of Agents.

| ID | Episode | Depth |
|---|---|---|
| S10E08 | Durable Execution: Long-Running Agents, Checkpointing, and Recovery | Advanced |
| S10E09 | Agent Evaluation at Scale: Simulation, Benchmarks, and Regression Suites | Advanced |
| S10E10 | Cost, Latency, and Token Economics of Agents | Intermediate |

### S10E08 — Durable Execution: Long-Running Agents, Checkpointing, and Recovery

**Depth:** Advanced  
**Learning objective:** Run agent tasks that last minutes to days without losing progress or repeating side effects.  
**Prerequisites:** S09E06, S10E02  
**Expected outcome:** Design resumable, idempotent agent workflows with explicit failure semantics.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Why Durability**

- Process crashes, deploys, timeouts and approvals in the middle of a task
- Workflow engines and event-sourced state

**Topic 2 — Deterministic Orchestration**

- Replay of workflow history
- Isolating non-deterministic model calls

**Topic 3 — Checkpointing and Resume**

- Checkpoint contents and storage
- Resuming with stale context

**Topic 4 — Side Effects**

- Idempotency keys and exactly-once effect patterns
- Retries, compensation and sagas

**Topic 5 — Human Waits and Scheduling**

- Pausing for approvals; timers and external events
- Cancellation and cleanup

</details>

**Important concepts**

- *Commands / APIs / Code:* checkpoint store interface, idempotency-key pattern (concept)
- *Mechanisms & failure scenarios:* Duplicate emails/payments after a retry, resumed run using stale context, orphaned resources after cancellation.

### S10E09 — Agent Evaluation at Scale: Simulation, Benchmarks, and Regression Suites

**Depth:** Advanced  
**Learning objective:** Build evaluation infrastructure that keeps pace with changing prompts, tools and models.  
**Prerequisites:** S09E13, S10E08  
**Expected outcome:** Specify an evaluation pipeline that gates agent releases with statistical care.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Environments**

- Simulated users and mocked backends
- Replay of recorded production traces
- Sandboxes for write actions

**Topic 2 — Benchmarks and Metrics**

- Public agent benchmarks and their limits
- Custom task suites with graded success

**Topic 3 — Statistics**

- Multi-run variance and confidence intervals
- Reliability metrics such as pass-at-k vs pass-to-the-k
- Sample sizes needed to detect a regression

**Topic 4 — Continuous Evaluation**

- CI gates on agent changes
- Production sampling and shadow comparison
- Safety and policy test suites

</details>

**Important concepts**

- *Commands / APIs / Code:* simulated-user harness, regression-suite runner (concept)
- *Mechanisms & failure scenarios:* Simulators unlike real users, benchmark overfitting, flaky evaluations ignored.

### S10E10 — Cost, Latency, and Token Economics of Agents

**Depth:** Intermediate  
**Learning objective:** Predict and control what an agent costs and how long it takes.  
**Prerequisites:** S10E01, S07E09  
**Expected outcome:** Model the cost of an agent workflow and apply optimizations without hurting task success.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Where Cost Accumulates**

- Context growth across steps
- Tool results and retrieval bloat
- Reasoning tokens and retries

**Topic 2 — Optimization**

- Model routing (small for easy steps, large for hard ones)
- Context compaction and caching
- Parallel tool calls

**Topic 3 — Budgets and Metrics**

- Cost per successful task as the metric
- Spend limits, early stopping and alerts

**Topic 4 — Latency**

- Latency budgets and streaming progress
- Parallel vs sequential tool calls
- Perceived latency for long-running tasks

</details>

**Important concepts**

- *Commands / APIs / Code:* per-run cost accounting, budget guard (concept)
- *Mechanisms & failure scenarios:* Quadratic cost from replaying full history, retries hiding true cost, cheap models causing expensive loops.

<a id="s10-module-4"></a>

## Module 4 — Agent Systems in the Enterprise

**5 episodes (S10E11–S10E15) · 21 topics.** This module covers: Agentic RAG and Enterprise Knowledge Agents; Agent Platforms and Runtime Architecture; AI Workflow Automation and Enterprise Integration Patterns; Governing Autonomous Agents; Capstone.

| ID | Episode | Depth |
|---|---|---|
| S10E11 | Agentic RAG and Enterprise Knowledge Agents | Advanced |
| S10E12 | Agent Platforms and Runtime Architecture | Intermediate |
| S10E13 | AI Workflow Automation and Enterprise Integration Patterns | Intermediate |
| S10E14 | Governing Autonomous Agents: Policy, Risk Tiers, and Audit | Advanced |
| S10E15 | Capstone: Designing an Enterprise Multi-Agent System | Advanced |

### S10E11 — Agentic RAG and Enterprise Knowledge Agents

**Depth:** Advanced  
**Learning objective:** Combine retrieval, tools and reasoning to answer multi-step questions over enterprise knowledge.  
**Prerequisites:** S08E11, S09E18, S08E18  
**Expected outcome:** Design an agentic retrieval system with evidence tracking and permission enforcement.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Agentic Retrieval and Multi-Source Routing**

- Agent decides what and when to retrieve
- Iterative evidence gathering and synthesis
- Documents, SQL and APIs
- Mixing sources of different trust levels

**Topic 2 — Evidence and Citations**

- Evidence ledgers across steps
- Citation tracking

**Topic 3 — Safety and Quality**

- Permission-aware retrieval inside agents
- Evaluating multi-hop answers
- Latency vs depth; when fixed pipelines suffice

</details>

**Important concepts**

- *Commands / APIs / Code:* retrieval-as-tool definition, evidence-ledger structure
- *Mechanisms & failure scenarios:* Agent over-searching, mixing sources of different trust levels, unverifiable synthesized claims.

### S10E12 — Agent Platforms and Runtime Architecture

**Depth:** Intermediate  
**Learning objective:** Understand the shared platform services an organization needs to run many agents.  
**Prerequisites:** S10E04, S09E14  
**Expected outcome:** Sketch an internal agent platform and justify its components.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Platform Components**

- Agent registry, tool/MCP registry and policy engine
- Gateway for model access, quotas and logging

**Topic 2 — Runtime and Developer Experience**

- Sandboxing, scheduling and queues
- Environments: development, staging and production
- Templates and golden paths
- Versioning agents, tools and prompts together

**Topic 3 — Operations**

- Multi-tenancy and isolation
- Observability, cost attribution and incident handling
- Governance hooks (link to S10E14)

</details>

**Important concepts**

- *Commands / APIs / Code:* registry entry schema, policy-check call (concept)
- *Mechanisms & failure scenarios:* Shadow agents outside governance, tool sprawl, no attribution of cost to teams.

### S10E13 — AI Workflow Automation and Enterprise Integration Patterns

**Depth:** Intermediate  
**Learning objective:** Understand when visual and low-code workflow automation is the right execution model for AI, how such workflows integrate APIs, models, tools and humans, and how to operate them reliably and under governance.  
**Prerequisites:** S09E06, S09E08, S09E11, S10E08  
**Expected outcome:** Choose between workflow tools, code orchestration and agents for an integration problem, and design a workflow with defined triggers, error handling, approvals and governance.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — Workflow Automation vs Code Orchestration vs Agents**

- Visual and low-code workflow platforms (n8n as the worked example)
- Where each model fits: deterministic integration, durable code workflows, autonomous agents
- Building blocks: triggers, nodes, credentials, executions

**Topic 2 — Triggers and Integration Surfaces**

- Webhooks, schedules, queues and polling
- External API integrations: authentication, pagination, rate limits (link to S09E03)
- Data mapping between systems

**Topic 3 — AI, Tool, and MCP Nodes**

- Model calls, structured outputs and tool calling inside workflows
- MCP servers as workflow tools; agent nodes vs fixed paths
- Prompt and model versioning in a workflow context

**Topic 4 — Reliability and Error Handling**

- Retries, timeouts, idempotency and dead-letter handling
- Error workflows, alerting and execution logs
- Cost and rate control for AI nodes

**Topic 5 — Human-in-the-Loop Automation**

- Approval and review steps, escalation and timeout behavior
- Safe defaults when no human responds (link to S09E11)

**Topic 6 — Governance and Operations**

- Environments, versioning and promotion of workflows
- Secrets and credential management; access control
- Shadow automation, audit and when to graduate a workflow to code

</details>

**Important concepts**

- *Commands / APIs / Code:* Webhook-triggered workflow definition (n8n-style, illustrative), retry and error-workflow policy, human-approval step configuration concept, credential handling pattern
- *Mechanisms & failure scenarios:* Duplicate side effects from retried nodes, secrets in workflow definitions, silent failures with no error workflow, uncontrolled shadow automation, approvals that time out into unsafe defaults, workflows too complex to review or version, unbounded AI-node cost.

### S10E14 — Governing Autonomous Agents: Policy, Risk Tiers, and Audit

**Depth:** Advanced  
**Learning objective:** Match the level of autonomy to risk and produce evidence that controls work.  
**Prerequisites:** S10E12, S09E11  
**Expected outcome:** Define an autonomy and governance framework with measurable controls.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Risk Classification**

- Impact and reversibility of actions
- Data sensitivity and regulatory context

**Topic 2 — Autonomy Tiers**

- Suggest, approve, act-with-limits, autonomous
- Moving between tiers with evidence

**Topic 3 — Controls**

- Policy enforcement points
- Approval workflows and break-glass
- Kill switches and rate limits

**Topic 4 — Assurance**

- Audit logs with reasoning and action traces
- Periodic review and incident reporting
- Alignment with frameworks (verified at scripting time)

</details>

**Important concepts**

- *Commands / APIs / Code:* risk-tier policy table, audit record schema
- *Mechanisms & failure scenarios:* Autonomy raised without evidence, audit logs missing the reasoning chain, controls bypassed by new tools.

### S10E15 — Capstone: Designing an Enterprise Multi-Agent System

**Depth:** Advanced  
**Learning objective:** Integrate multi-agent coordination, protocols, memory, durability, evaluation and governance into one architecture.  
**Prerequisites:** S10E14, S10E09, S10E08, S10E11  
**Expected outcome:** Present and defend an end-to-end enterprise multi-agent design, including where not to use agents.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Problem and Decomposition**

- Choosing a realistic enterprise workflow
- Agent roles, tools and data sources
- Autonomy tiers per role

**Topic 2 — Coordination and Protocols**

- Orchestration, protocols and identity
- Agent roles and message contracts in the design
- Choosing synchronous vs asynchronous coordination

**Topic 3 — Durability, Memory, and Observability**

- Durable execution and memory design
- Tracing across agents

**Topic 4 — Evaluation, Cost, and Guardrails**

- Evaluation strategy and cost envelope
- Guardrails and governance

**Topic 5 — Readiness and Operations**

- Launch gates and staged rollout
- Incident scenarios and runbooks
- Where not to use agents; handoff to MLOps, LLMOps and infrastructure seasons

</details>

**Important concepts**

- *Commands / APIs / Code:* architecture diagram and readiness checklist
- *Mechanisms & failure scenarios:* Complexity exceeding the value delivered, cascading agent failures, governance added only after launch.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s10-module-1) | Starting point of the season |
| [Module 2](#s10-module-2) | Within-module sequence only |
| [Module 3](#s10-module-3) | [Module 1](#s10-module-1) (S10E01, S10E02) |
| [Module 4](#s10-module-4) | [Module 1](#s10-module-1) (S10E04); [Module 3](#s10-module-3) (S10E08, S10E09) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 9 — AI Agents, Tool Calling & MCP](../season-09-ai-agents-and-mcp/roadmap.md)
- **Next:** [Season 11 — MLOps Engineering](../season-11-mlops-engineering/roadmap.md)
- **Draws on:** [Season 5](../season-05-deep-learning/roadmap.md) (S05E23); [Season 6](../season-06-llms-and-transformers/roadmap.md) (S06E12, S06E20); [Season 7](../season-07-generative-ai-engineering/roadmap.md) (S07E09); [Season 8](../season-08-rag-engineering/roadmap.md) (S08E11, S08E18); [Season 9](../season-09-ai-agents-and-mcp/roadmap.md) (S09E05, S09E06, S09E07, S09E08, S09E09, S09E11, S09E13, S09E14, S09E18)
- **Required by:** [Season 13](../season-13-ai-infrastructure/roadmap.md) (via S10E12); [Season 14](../season-14-production-ai-systems/roadmap.md) (via S10E04, S10E12, S10E15); [Season 15](../season-15-ai-for-devops/roadmap.md) (via S10E01, S10E02, S10E04, S10E08, S10E13, S10E14)
