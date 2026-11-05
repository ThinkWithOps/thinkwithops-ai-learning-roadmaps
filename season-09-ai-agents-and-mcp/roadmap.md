# Season 9 Roadmap — AI Agents, Tool Calling & MCP

[← Season 9 overview](README.md) · [All seasons](../README.md)

**4 modules · 18 episodes · 78 topics · 199 subtopics · Level: Intermediate → Advanced**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Tool Use Foundations](#s09-module-1)
- [Module 2 — Agent Loops, State, and Orchestration](#s09-module-2)
- [Module 3 — Model Context Protocol (MCP)](#s09-module-3)
- [Module 4 — Safety, Evaluation, and Production](#s09-module-4)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Teach single-agent systems as engineered control loops around an LLM: tool calling mechanics, planning and state, workflow vs autonomy, the Model Context Protocol, and the safety, evaluation and observability needed to run agents in production. Multi-agent and long-horizon systems follow in Season 10.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S09E01 | Define an agent precisely and distinguish it from chatbots and fixed workflows. |
| S09E02 | Understand how a model "calls" a tool and who actually executes it. |
| S09E03 | Design tools that models can use reliably and that cannot cause unbounded damage. |
| S09E04 | Understand how agents interleave reasoning with action and how to bound them. |
| S09E05 | Decide what an agent remembers, where it is stored, and how it is recalled. |
| S09E06 | Choose between deterministic orchestration and model-driven control, and combine them. |
| S09E07 | Use critique and verification loops to improve agent reliability, and know their limits. |
| S09E08 | Understand the problem MCP standardizes and the roles in its architecture. |
| S09E09 | Follow an MCP session from initialization to tool invocation and understand authorization. |
| S09E10 | Implement an MCP server and apply security practices appropriate for tools that act on real systems. |
| S09E11 | Contain what an agent can do, whatever the model decides. |
| S09E12 | Understand why tool-using agents are especially exposed to injected instructions and how to limit the blast radius. |
| S09E13 | Measure agent quality beyond the final answer. |
| S09E14 | Make multi-step agent behavior inspectable and reproducible. |
| S09E15 | Understand how coding agents work internally — how they build context from a repository, execute tools and are held within permissions — and how computer-use agents differ. |
| S09E16 | Understand how coding agents are used inside a software-delivery process: how work is decomposed, verified, reviewed and measured, and where human judgment stays essential. |
| S09E17 | Understand how coding agents are customized and connected to the engineering environment, and how to do so safely and maintainably. |
| S09E18 | Combine tools, memory, safety, evaluation and observability into a production-ready agent design. |

## Prerequisites and Expected Knowledge

- **Season 1 — [Python for AI & ML Engineering](../season-01-python-for-ai-ml/roadmap.md)**: S01E13, S01E14
- **Season 6 — [LLMs & Transformer Architecture](../season-06-llms-and-transformers/roadmap.md)**: S06E20
- **Season 7 — [Generative AI Application Engineering](../season-07-generative-ai-engineering/roadmap.md)**: S07E03, S07E04, S07E05, S07E10, S07E19
- **Season 8 — [RAG Engineering](../season-08-rag-engineering/roadmap.md)**: S08E06

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Tool Use Foundations](#s09-module-1) | S09E01–S09E03 | 3 | 1 Foundational, 2 Intermediate |
| 2 | [Agent Loops, State, and Orchestration](#s09-module-2) | S09E04–S09E07 | 4 | 3 Intermediate, 1 Advanced |
| 3 | [Model Context Protocol (MCP)](#s09-module-3) | S09E08–S09E10 | 3 | 1 Intermediate, 2 Advanced |
| 4 | [Safety, Evaluation, and Production](#s09-module-4) | S09E11–S09E18 | 8 | 5 Advanced, 3 Intermediate |

<a id="s09-module-1"></a>

## Module 1 — Tool Use Foundations

**3 episodes (S09E01–S09E03) · 14 topics.** This module covers: What an Agent Is; Function Calling Mechanics; Tool Design.

| ID | Episode | Depth |
|---|---|---|
| S09E01 | What an Agent Is: LLM, Tools, and a Loop | Foundational |
| S09E02 | Function Calling Mechanics: Tool Schemas and the Execution Boundary | Intermediate |
| S09E03 | Tool Design: Interfaces, Errors, Idempotency, and Permissions | Intermediate |

### S09E01 — What an Agent Is: LLM, Tools, and a Loop

**Depth:** Foundational  
**Learning objective:** Define an agent precisely and distinguish it from chatbots and fixed workflows.  
**Prerequisites:** S07E03, S07E10  
**Expected outcome:** Explain an agent's control loop and choose between agent and workflow for a use case.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Anatomy and Levels of Autonomy**

- Model, instructions, tools, state and loop
- Perceive → decide → act → observe
- Predefined paths vs model-chosen paths
- Autonomy as a spectrum

**Topic 2 — A Minimal Agent**

- Walk through one tool-using task
- Stopping conditions

**Topic 3 — Costs and Risks**

- When extra autonomy helps and when it hurts
- Cost, latency and reliability implications
- Compounding errors across steps

</details>

**Important concepts**

- *Commands / APIs / Code:* minimal while-loop agent with one tool (concept)
- *Mechanisms & failure scenarios:* Infinite loops, tool misuse, wrong stopping decisions, compounding errors across steps.

### S09E02 — Function Calling Mechanics: Tool Schemas and the Execution Boundary

**Depth:** Intermediate  
**Learning objective:** Understand how a model "calls" a tool and who actually executes it.  
**Prerequisites:** S09E01, S07E03  
**Expected outcome:** Implement a safe tool-call loop with validation and error handling.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Protocol**

- Tool definitions as JSON schemas
- Model emits a tool call; application executes; result returned

**Topic 2 — The Execution Boundary**

- The model proposes, your code disposes
- Argument validation and authorization

**Topic 3 — Parallel and Sequential Calls**

- Parallel tool calls and result ordering
- Dependent calls and error propagation

**Topic 4 — Tool-Choice Control**

- Auto, required and forced tool use
- Tool description quality and selection accuracy
- Tool-call schema differences across OpenAI, Anthropic and Gemini
- Parallel-call and tool-choice semantics by provider

**Topic 5 — Costs and Failure Modes**

- Token cost of many tool definitions
- Hallucinated arguments and nonexistent tools
- Timeouts and partial failures

</details>

**Important concepts**

- *Commands / APIs / Code:* tools parameter and `tool_calls` handling loop (concept), argument validation with Pydantic
- *Mechanisms & failure scenarios:* Hallucinated arguments, calling nonexistent tools, executing unvalidated model output.

### S09E03 — Tool Design: Interfaces, Errors, Idempotency, and Permissions

**Depth:** Intermediate  
**Learning objective:** Design tools that models can use reliably and that cannot cause unbounded damage.  
**Prerequisites:** S09E02, S01E14  
**Expected outcome:** Specify a tool contract that is safe, testable and model-friendly.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — Interface Design**

- Narrow, well-named tools with clear descriptions
- Inputs the model can actually supply

**Topic 2 — Outputs and Errors**

- Output shaping: concise, structured, informative
- Error messages that let the model recover without leaking secrets

**Topic 3 — Safety Properties**

- Idempotency and dry-run modes
- Read vs write separation
- Scoped credentials and rate limits

**Topic 4 — External API Integration in Tools**

- Authentication flows: API keys, OAuth and delegated tokens
- Pagination, rate limits, retries and idempotency keys
- Webhooks and asynchronous callbacks
- Mapping API errors to model-friendly messages

**Topic 5 — Testing Tools**

- Tool-level unit tests
- Simulating model misuse

**Topic 6 — Evolving Tool Contracts**

- Versioning and deprecation
- Retries duplicating side effects

</details>

**Important concepts**

- *Commands / APIs / Code:* tool wrapper with validation, error-to-model message formatting
- *Mechanisms & failure scenarios:* Ambiguous tools chosen wrongly, retries duplicating side effects, error messages that leak secrets or give the model no recovery path.

<a id="s09-module-2"></a>

## Module 2 — Agent Loops, State, and Orchestration

**4 episodes (S09E04–S09E07) · 18 topics.** This module covers: Reasoning and Acting; Agent State and Memory; Workflow Orchestration vs Autonomous Agents; Planning, Reflection, and Self-Correction.

| ID | Episode | Depth |
|---|---|---|
| S09E04 | Reasoning and Acting: The ReAct Loop, Planning, and Stopping | Intermediate |
| S09E05 | Agent State and Memory: Short-Term, Long-Term, and Retrieval | Intermediate |
| S09E06 | Workflow Orchestration vs Autonomous Agents: Graphs and State Machines | Intermediate |
| S09E07 | Planning, Reflection, and Self-Correction | Advanced |

### S09E04 — Reasoning and Acting: The ReAct Loop, Planning, and Stopping

**Depth:** Intermediate  
**Learning objective:** Understand how agents interleave reasoning with action and how to bound them.  
**Prerequisites:** S09E02, S06E20  
**Expected outcome:** Implement bounded agent control with explicit stopping and recovery rules.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Reasoning and Acting**

- Thought/action/observation cycle
- Native tool calling vs text-parsed actions

**Topic 2 — Planning Styles**

- Plan-then-execute vs adaptive planning
- Re-planning after failure

**Topic 3 — Control**

- Step limits, token budgets and timeouts
- Stopping criteria and success checks

**Topic 4 — Handling Failure**

- Tool failures and dead ends
- Repeating the same failing call

**Topic 5 — Failure Modes of the Loop**

- Drift from the goal and premature completion
- Error accumulation over long trajectories and cost growth

</details>

**Important concepts**

- *Commands / APIs / Code:* agent loop with max-steps and budget guard (concept)
- *Mechanisms & failure scenarios:* Repeating the same failing call, hallucinating tool results, claiming success without verification.

### S09E05 — Agent State and Memory: Short-Term, Long-Term, and Retrieval

**Depth:** Intermediate  
**Learning objective:** Decide what an agent remembers, where it is stored, and how it is recalled.  
**Prerequisites:** S09E04, S08E06, S07E05  
**Expected outcome:** Design an agent memory layer with explicit write, recall and forgetting policies.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Kinds of Memory**

- Working memory (context), episodic, semantic and procedural
- Scratchpads and structured state

**Topic 2 — Implementation**

- Summarization and compaction
- Vector and key-value memory stores

**Topic 3 — Recall**

- Retrieving relevant memories
- Recency, relevance and importance scoring

**Topic 4 — Write Policy**

- What to store, when, and with what provenance
- Salience scoring and deduplication of memories
- User-visible memory controls

**Topic 5 — Risks**

- Memory poisoning and stale facts
- Privacy, retention and deletion

</details>

**Important concepts**

- *Commands / APIs / Code:* memory read/write interface, summarization step
- *Mechanisms & failure scenarios:* Wrong memories retrieved and trusted, sensitive data stored indefinitely, memory growth degrading performance.

### S09E06 — Workflow Orchestration vs Autonomous Agents: Graphs and State Machines

**Depth:** Intermediate  
**Learning objective:** Choose between deterministic orchestration and model-driven control, and combine them.  
**Prerequisites:** S09E04, S09E05  
**Expected outcome:** Select and justify an orchestration style for a task and design its state model.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Orchestrated Workflows**

- Directed graphs, state machines and conditional edges
- Patterns: routing, parallelization, prompt chaining, evaluator-optimizer

**Topic 2 — Autonomous Control**

- Where model discretion adds value
- Guardrails around autonomy

**Topic 3 — Hybrid Designs**

- A bounded agent inside a workflow
- Choosing the boundary

**Topic 4 — State and Persistence**

- Typed shared state and checkpoints
- Resumability after failure

**Topic 5 — Human Checkpoints and Testing**

- Human-approval nodes
- Testing nondeterministic branches; unbounded loops in graphs

</details>

**Important concepts**

- *Commands / APIs / Code:* graph-based orchestration library concepts (framework-neutral), state schema design
- *Mechanisms & failure scenarios:* State schema drift, nondeterministic branches hard to test, unbounded loops in graphs.

### S09E07 — Planning, Reflection, and Self-Correction

**Depth:** Advanced  
**Learning objective:** Use critique and verification loops to improve agent reliability, and know their limits.  
**Prerequisites:** S09E06  
**Expected outcome:** Add verification loops that are grounded in external checks and measure their effect.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Planning Patterns**

- Task decomposition and plan revision
- Plan verification before execution

**Topic 2 — Reflection**

- Self-critique and reviser loops
- Why self-review without ground truth is weak

**Topic 3 — Verification, Cost, and Benefit**

- Tests, validators and retrieval as verification
- Grounding critique in checkable facts
- Added latency and tokens
- Measuring improvement and when to stop refining

</details>

**Important concepts**

- *Commands / APIs / Code:* generate–critique–revise loop with an external check (concept)
- *Mechanisms & failure scenarios:* Self-reinforcing errors, critique that rubber-stamps, verification cost exceeding value.

<a id="s09-module-3"></a>

## Module 3 — Model Context Protocol (MCP)

**3 episodes (S09E08–S09E10) · 12 topics.** This module covers: MCP Architecture; MCP Protocol Internals; Building and Hardening MCP Servers.

| ID | Episode | Depth |
|---|---|---|
| S09E08 | MCP Architecture: Hosts, Clients, Servers, and Capabilities | Intermediate |
| S09E09 | MCP Protocol Internals: Messages, Transports, and Authorization | Advanced |
| S09E10 | Building and Hardening MCP Servers | Advanced |

### S09E08 — MCP Architecture: Hosts, Clients, Servers, and Capabilities

**Depth:** Intermediate  
**Learning objective:** Understand the problem MCP standardizes and the roles in its architecture.  
**Prerequisites:** S09E02  
**Expected outcome:** Draw an MCP architecture and explain what each role is responsible for.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — The Integration Problem**

- N×M tool integrations
- A standard protocol for context and tools

**Topic 2 — Roles and Primitives**

- Host, client and server
- Tools, resources and prompts

**Topic 3 — MCP in Context and Deployment Shapes**

- Versus function calling and agent frameworks
- What MCP is and is not
- Local vs remote servers
- Trust boundaries between host, client and server
- Versioning and specification revisions

</details>

**Important concepts**

- *Commands / APIs / Code:* MCP server/client message flow (concept), inspector tool usage (concept)
- *Mechanisms & failure scenarios:* Overtrusting third-party servers, capability mismatch between client and server, version incompatibilities.

### S09E09 — MCP Protocol Internals: Messages, Transports, and Authorization

**Depth:** Advanced  
**Learning objective:** Follow an MCP session from initialization to tool invocation and understand authorization.  
**Prerequisites:** S09E08  
**Expected outcome:** Trace an MCP tool call end to end and describe how remote servers are authorized.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Messages**

- JSON-RPC structure
- Requests, responses, notifications and errors

**Topic 2 — Session Lifecycle**

- Initialization and capability negotiation
- Tool listing, invocation and results

**Topic 3 — Transports**

- stdio and HTTP-based transports
- Streaming, cancellation and progress

**Topic 4 — Authorization**

- OAuth-based flow for remote servers (overview)
- Consent, token handling and audience binding

**Topic 5 — Compatibility**

- Specification revision tracking
- Session and statelessness considerations

</details>

**Important concepts**

- *Commands / APIs / Code:* raw JSON-RPC messages for an initialize/list/call exchange (illustrative; verify against current spec)
- *Mechanisms & failure scenarios:* Broken session negotiation, unhandled cancellation, tokens issued for the wrong audience.

### S09E10 — Building and Hardening MCP Servers

**Depth:** Advanced  
**Learning objective:** Implement an MCP server and apply security practices appropriate for tools that act on real systems.  
**Prerequisites:** S09E09, S09E03  
**Expected outcome:** Specify a hardened MCP server design with scoped permissions and auditing.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Building and Testing a Server**

- Exposing tools and resources with schemas
- Error handling and logging
- Using a client or inspector
- Contract tests for tool behavior

**Topic 2 — Security**

- Scopes and per-tool authorization
- Token audience validation; avoiding token passthrough
- Local vs remote risk

**Topic 3 — Operating**

- Registration, discovery and trust
- Auditing, revocation and tracking specification changes

**Topic 4 — Enterprise Integration Patterns**

- MCP registries and gateways for shared servers
- MCP inside coding agents (S09E17) and workflow tools (S10E13)
- Governance of server catalogs and credentials

</details>

**Important concepts**

- *Commands / APIs / Code:* server SDK usage (concept), per-tool authorization check
- *Mechanisms & failure scenarios:* Over-broad scopes, server executing arbitrary commands from model input, missing audit trails.

<a id="s09-module-4"></a>

## Module 4 — Safety, Evaluation, and Production

**8 episodes (S09E11–S09E18) · 34 topics.** This module covers: Agent Safety; Prompt Injection in Agents; Evaluating Agents; Observability and Debugging for Agents; AI Coding Agents; Agentic Software Development Workflows; Extending Coding Agents; Designing a Production Single Agent.

| ID | Episode | Depth |
|---|---|---|
| S09E11 | Agent Safety: Permissions, Sandboxing, and Human Approval | Advanced |
| S09E12 | Prompt Injection in Agents: Confused Deputy and Exfiltration | Advanced |
| S09E13 | Evaluating Agents: Trajectories, Tool-Call Correctness, and Task Success | Advanced |
| S09E14 | Observability and Debugging for Agents | Intermediate |
| S09E15 | AI Coding Agents: Architecture, Repository Context, Tool Execution, and Permissions | Advanced |
| S09E16 | Agentic Software Development Workflows | Intermediate |
| S09E17 | Extending Coding Agents: Instruction Files, Hooks, Sub-Agents, and MCP | Intermediate |
| S09E18 | Designing a Production Single Agent: End-to-End Blueprint | Advanced |

### S09E11 — Agent Safety: Permissions, Sandboxing, and Human Approval

**Depth:** Advanced  
**Learning objective:** Contain what an agent can do, whatever the model decides.  
**Prerequisites:** S09E03, S09E06  
**Expected outcome:** Define a permission and approval model that bounds worst-case agent behavior.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Least Privilege**

- Scoped identities and credentials per agent and task
- Allowlists, deny rules and read-only defaults

**Topic 2 — Isolation and Separation of Privilege**

- Sandboxed code execution and network egress limits
- Resource limits and timeouts
- Privileged executors behind policy checks

**Topic 3 — Human in the Loop, Audit, and Rollback**

- Risk-tiered approvals
- Approval fatigue and good defaults
- Audit trails and reversible actions
- Approval patterns in coding agents and automation tools (see S09E17 and S10E13)
- Safe defaults when no human responds

</details>

**Important concepts**

- *Commands / APIs / Code:* approval-gate wrapper, container/sandbox run (concept), policy table
- *Mechanisms & failure scenarios:* Agent with production credentials, approvals rubber-stamped, sandbox escapes via mounted secrets.

### S09E12 — Prompt Injection in Agents: Confused Deputy and Exfiltration

**Depth:** Advanced  
**Learning objective:** Understand why tool-using agents are especially exposed to injected instructions and how to limit the blast radius.  
**Prerequisites:** S09E11, S07E04  
**Expected outcome:** Perform a basic threat model of an agent and apply architectural mitigations.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Attack Paths and the Confused Deputy**

- Indirect injection via web pages, files, emails and tool results
- Data exfiltration channels (links, tool calls, markdown)
- Acting with the user's authority on an attacker's behalf
- Capability combinations that create exfiltration paths

**Topic 2 — Design Principles**

- Untrusted data cannot authorize actions
- Separating data-reading and action-taking capabilities
- Egress control and output sanitization

**Topic 3 — Testing and Monitoring**

- Adversarial test suites
- Detection signals and incident response

</details>

**Important concepts**

- *Commands / APIs / Code:* injection test corpus (concept), egress allowlist
- *Mechanisms & failure scenarios:* Agent forwarding private data after reading a malicious page, tool chains combining read and send capabilities, over-trusting model-based detectors.

### S09E13 — Evaluating Agents: Trajectories, Tool-Call Correctness, and Task Success

**Depth:** Advanced  
**Learning objective:** Measure agent quality beyond the final answer.  
**Prerequisites:** S09E04, S07E19  
**Expected outcome:** Build an agent evaluation harness with trajectory-level metrics.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — What to Measure**

- Task success, tool-call accuracy and step efficiency
- Cost, latency and safety violations

**Topic 2 — Environments**

- Deterministic mocked tools and sandboxes
- Scenario suites

**Topic 3 — Methods**

- Trajectory-level scoring
- LLM judges on trajectories and their limits

**Topic 4 — Statistics**

- Variance across runs
- Confidence intervals for pass rates

**Topic 5 — Using Evaluation**

- Regression testing prompts, tools and models
- Failure clustering and production sampling

</details>

**Important concepts**

- *Commands / APIs / Code:* scenario runner with mocked tools, trajectory scoring script
- *Mechanisms & failure scenarios:* Non-deterministic tests masking regressions, judges rewarding confident but wrong trajectories, evals not covering tool failures.

### S09E14 — Observability and Debugging for Agents

**Depth:** Intermediate  
**Learning objective:** Make multi-step agent behavior inspectable and reproducible.  
**Prerequisites:** S09E13  
**Expected outcome:** Instrument an agent so any failed run can be diagnosed and replayed.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Tracing**

- Spans per model call and tool call
- Capturing prompts, tool arguments and results

**Topic 2 — Debugging**

- Replaying trajectories
- Diffing runs across versions
- Finding where a run first went wrong

**Topic 3 — Operational Signals and Privacy-Aware Logging**

- Cost, latency and loop metrics
- Alerting on anomalous behavior
- Redaction and retention
- Secrets in traces

</details>

**Important concepts**

- *Commands / APIs / Code:* OpenTelemetry-style span instrumentation (concept), trace replay tool
- *Mechanisms & failure scenarios:* Missing context making failures unreproducible, secrets in traces, overwhelming trace volume.

### S09E15 — AI Coding Agents: Architecture, Repository Context, Tool Execution, and Permissions

**Depth:** Advanced  
**Learning objective:** Understand how coding agents work internally — how they build context from a repository, execute tools and are held within permissions — and how computer-use agents differ.  
**Prerequisites:** S09E11, S09E12  
**Expected outcome:** Explain a coding agent's architecture end to end, reason about its context and permission design, and identify its main risks and controls.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — Coding Agent Architecture**

- Model, tools, context and permissions inside an agent loop
- Interactive vs unattended modes
- Claude Code and OpenAI Codex as two instances of the pattern

**Topic 2 — Repository Understanding**

- Indexing and search: text search, symbol and AST search, embeddings
- Building a repository map and selecting relevant files
- Reading code vs reading tests, configuration and history

**Topic 3 — Context Management**

- Context window budgeting and compaction in long sessions
- Persistent instructions vs session memory (extension covered in S09E17)

**Topic 4 — Tool Execution and Permissions**

- File editing, shell, test and search tools
- Approval modes, allowlists and sandboxing (builds on S09E11)

**Topic 5 — Verification and Failure Modes**

- Tests, linters and type checks as feedback
- Plausible patches that pass weak tests; insecure code and hallucinated dependencies
- Prompt injection through repository content

**Topic 6 — Computer-Use Agents**

- Screenshot-and-action loops
- Browser/DOM vs pixel control; reliability and latency limits

</details>

**Important concepts**

- *Commands / APIs / Code:* Agent loop sketch with a file-search tool and a permission check (illustrative), test-runner tool wrapper, approval-mode configuration concept
- *Mechanisms & failure scenarios:* Wrong files selected into context, stale context across long sessions, destructive shell commands, plausible patches that pass weak tests, hallucinated dependencies, prompt injection through repository content, unreviewed autonomy.

### S09E16 — Agentic Software Development Workflows

**Depth:** Intermediate  
**Learning objective:** Understand how coding agents are used inside a software-delivery process: how work is decomposed, verified, reviewed and measured, and where human judgment stays essential.  
**Prerequisites:** S09E15, S09E11, S01E13, S01E14  
**Expected outcome:** Design a bounded, reviewable agent-assisted development workflow with explicit verification gates and measure whether it improves delivery quality.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — From Request to Change**

- Specifying work for an agent: scope, acceptance criteria and constraints
- Task decomposition and sizing for reliable agent output
- Plan-first vs act-first modes

**Topic 2 — Verification Loops**

- Tests, linters, type checks and build as the agent's feedback
- Test-driven prompting and reviewing the tests themselves
- Plausible-but-wrong patches and why green checks are not proof

**Topic 3 — Source Control, CI, and Review**

- Branch and pull-request workflows for agent-authored changes
- CI integration and required checks
- Reviewing agent-written code: diff size limits, risk-based review, human approval

**Topic 4 — Failure Modes and Controls**

- Runaway edits, context loss, hallucinated dependencies, secret exposure
- Scoped permissions and sandboxes for unattended runs (link to S09E11)

**Topic 5 — Measuring Effect**

- Metrics: accepted-change rate, rework, cycle time, defect escape and cost per accepted change
- Avoiding vanity measures
- Claude Code, OpenAI Codex and open coding models (for example Qwen Coder) as instances of one workflow pattern

</details>

**Important concepts**

- *Commands / APIs / Code:* Task specification template, test-and-lint verification loop, pull-request review checklist (illustrative); agent-assisted change flow expressed as a pipeline
- *Mechanisms & failure scenarios:* Plausible patches that pass weak tests, runaway edits across many files, context lost in long sessions, hallucinated dependencies, secrets exposed in prompts or commits, reviewers rubber-stamping large agent-authored diffs, productivity claims without measurement.

### S09E17 — Extending Coding Agents: Instruction Files, Hooks, Sub-Agents, and MCP

**Depth:** Intermediate  
**Learning objective:** Understand how coding agents are customized and connected to the engineering environment, and how to do so safely and maintainably.  
**Prerequisites:** S09E15, S09E16, S09E10, S09E11  
**Expected outcome:** Configure and govern a coding agent's instructions, permissions, automation hooks, sub-agents and MCP connections with explicit trust boundaries.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Instruction and Context Files**

- Project instruction files (CLAUDE.md/AGENTS.md-style): purpose, hierarchy and scope
- What belongs in them, what does not, and why context budget matters
- Keeping instructions current and non-conflicting

**Topic 2 — Permissions and Trust**

- Permission modes, allowlists and denylists
- Sandboxing, network access and approval policies
- Shared team configuration vs personal settings

**Topic 3 — Hooks and Automation**

- Events around tool calls (before and after) and what they can enforce
- Formatting, linting, policy checks and notifications as hooks
- Risks: side effects, performance and privilege

**Topic 4 — Sub-Agents, Skills, and Reusable Commands**

- Delegation for context isolation and parallel work
- Reusable commands and skills as packaged workflows
- When delegation helps and when it only adds cost

**Topic 5 — MCP as the Extension Mechanism**

- Connecting repositories, tickets, documentation, databases and cloud APIs
- Least-privilege MCP servers and per-tool authorization (link to S09E10)
- Auditing, secrets handling and governance of shared configuration

</details>

**Important concepts**

- *Commands / APIs / Code:* Example instruction file structure, hook configuration concept, MCP server registration concept, permission allowlist (illustrative)
- *Mechanisms & failure scenarios:* Bloated instruction files wasting context, conflicting instructions, hooks with side effects or privilege escalation, over-broad MCP servers exposing production systems, secrets in shared configuration, sub-agents multiplying cost without benefit.

### S09E18 — Designing a Production Single Agent: End-to-End Blueprint

**Depth:** Advanced  
**Learning objective:** Combine tools, memory, safety, evaluation and observability into a production-ready agent design.  
**Prerequisites:** S09E14, S09E13, S09E10, S09E05  
**Expected outcome:** Produce a defensible design and launch plan for a production agent.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Requirements and Scope**

- Task boundaries and autonomy level
- Tool inventory and permissions
- Success metrics and cost envelope

**Topic 2 — Architecture**

- Orchestration, state, memory and tools via MCP
- Approval and fallback paths
- Evaluation and tracing built in

**Topic 3 — Launch**

- Shadow mode, staged autonomy and rollback
- Kill switches

**Topic 4 — Operate and Hand Off**

- Runbooks and ownership
- Bridge to multi-agent systems (Season 10)

</details>

**Important concepts**

- *Commands / APIs / Code:* reference architecture and launch checklist
- *Mechanisms & failure scenarios:* Over-broad autonomy at launch, no kill switch, quality unmeasured after release.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s09-module-1) | Starting point of the season |
| [Module 2](#s09-module-2) | [Module 1](#s09-module-1) (S09E02) |
| [Module 3](#s09-module-3) | [Module 1](#s09-module-1) (S09E02, S09E03) |
| [Module 4](#s09-module-4) | [Module 1](#s09-module-1) (S09E03); [Module 2](#s09-module-2) (S09E04, S09E05, S09E06); [Module 3](#s09-module-3) (S09E10) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 8 — RAG Engineering](../season-08-rag-engineering/roadmap.md)
- **Next:** [Season 10 — Advanced Agentic AI](../season-10-advanced-agentic-ai/roadmap.md)
- **Draws on:** [Season 1](../season-01-python-for-ai-ml/roadmap.md) (S01E13, S01E14); [Season 6](../season-06-llms-and-transformers/roadmap.md) (S06E20); [Season 7](../season-07-generative-ai-engineering/roadmap.md) (S07E03, S07E04, S07E05, S07E10, S07E19); [Season 8](../season-08-rag-engineering/roadmap.md) (S08E06)
- **Required by:** [Season 10](../season-10-advanced-agentic-ai/roadmap.md) (via S09E05, S09E06, S09E07, S09E08, S09E09, S09E11, S09E13, S09E14, S09E18); [Season 12](../season-12-llmops-engineering/roadmap.md) (via S09E12, S09E13, S09E14); [Season 14](../season-14-production-ai-systems/roadmap.md) (via S09E12, S09E18); [Season 15](../season-15-ai-for-devops/roadmap.md) (via S09E03, S09E04, S09E06, S09E10, S09E11, S09E12, S09E16, S09E17, S09E18)
