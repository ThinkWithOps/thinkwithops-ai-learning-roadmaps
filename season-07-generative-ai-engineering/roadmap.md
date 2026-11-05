# Season 7 Roadmap — Generative AI Application Engineering

[← Season 7 overview](README.md) · [All seasons](../README.md)

**5 modules · 21 episodes · 93 topics · 233 subtopics · Level: Intermediate**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Working with LLMs Programmatically](#s07-module-1)
- [Module 2 — Application Architecture and Reliability](#s07-module-2)
- [Module 3 — Multimodal, Customization, and Model Choice](#s07-module-3)
- [Module 4 — Generative Media Engineering](#s07-module-4)
- [Module 5 — Quality, Safety, and Productization](#s07-module-5)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Teach how to build dependable applications on top of LLMs: API mechanics, prompting, structured output, context management, application architecture, reliability, cost, multimodal and voice, image/video/audio generation engineering, customization choices, evaluation and guardrails. Framework and vendor specifics are treated as interchangeable examples of durable patterns.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S07E01 | Understand every part of a chat-completion style request and response, and what each costs. |
| S07E02 | Apply prompting techniques with an understanding of why they work and when they fail. |
| S07E03 | Get machine-readable output from a probabilistic model and handle the cases where it breaks. |
| S07E04 | Recognize why instructions and data share one channel and design prompts that limit damage. |
| S07E05 | Decide what goes into a prompt on each turn and manage conversation state within limits. |
| S07E06 | Understand the components of a production GenAI app and where each concern belongs. |
| S07E07 | Deliver token-by-token responses and handle concurrent LLM calls efficiently. |
| S07E08 | Make an application resilient to the failure modes of external model APIs. |
| S07E09 | Reduce cost and latency without silently degrading answers. |
| S07E10 | Evaluate LLM frameworks by the patterns they encapsulate rather than by brand. |
| S07E11 | Build features that accept images, documents and audio, understanding their cost and failure modes. |
| S07E12 | Understand the architecture and latency constraints of conversational voice systems. |
| S07E13 | Decide how to add knowledge, behavior or style to a model with the least cost and risk. |
| S07E14 | Run a small, disciplined fine-tuning project end to end. |
| S07E15 | Run models locally or self-hosted and understand the practical constraints. |
| S07E16 | Compare the major model providers and open-weight families by the capabilities that matter to an application, and design provider-portable integrations with routing, fallback and cost control. |
| S07E17 | Build and operate image-generation features: understand the pipeline stages, control generation, customize models, evaluate output and serve it within cost and safety limits. |
| S07E18 | Understand how video, music and speech are generated, what drives their cost and failure modes, and how to build asynchronous generation services responsibly. |
| S07E19 | Build a small but trustworthy evaluation loop for an LLM feature before scaling it with Season 12. |
| S07E20 | Apply layered safety controls around a model and understand their cost and limits. |
| S07E21 | Combine the season's components into one coherent, production-ready design. |

## Prerequisites and Expected Knowledge

- **Season 1 — [Python for AI & ML Engineering](../season-01-python-for-ai-ml/roadmap.md)**: S01E05, S01E15, S01E16
- **Season 5 — [Deep Learning & Neural Networks](../season-05-deep-learning/roadmap.md)**: S05E14, S05E17, S05E21
- **Season 6 — [LLMs & Transformer Architecture](../season-06-llms-and-transformers/roadmap.md)**: S06E02, S06E13, S06E15, S06E16, S06E17, S06E20, S06E22, S06E23, S06E24

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Working with LLMs Programmatically](#s07-module-1) | S07E01–S07E05 | 5 | 1 Foundational, 4 Intermediate |
| 2 | [Application Architecture and Reliability](#s07-module-2) | S07E06–S07E10 | 5 | 5 Intermediate |
| 3 | [Multimodal, Customization, and Model Choice](#s07-module-3) | S07E11–S07E16 | 6 | 4 Intermediate, 2 Advanced |
| 4 | [Generative Media Engineering](#s07-module-4) | S07E17–S07E18 | 2 | 1 Intermediate, 1 Advanced |
| 5 | [Quality, Safety, and Productization](#s07-module-5) | S07E19–S07E21 | 3 | 3 Intermediate |

<a id="s07-module-1"></a>

## Module 1 — Working with LLMs Programmatically

**5 episodes (S07E01–S07E05) · 22 topics.** This module covers: Anatomy of an LLM API Call; Prompt Engineering Mechanisms; Structured Outputs; Prompt Injection and Safe Prompt Design; Context Management.

| ID | Episode | Depth |
|---|---|---|
| S07E01 | Anatomy of an LLM API Call: Messages, Tokens, Parameters, and Streaming | Foundational |
| S07E02 | Prompt Engineering Mechanisms: Instructions, Examples, and Reasoning | Intermediate |
| S07E03 | Structured Outputs: JSON Schemas, Validation, and Repair | Intermediate |
| S07E04 | Prompt Injection and Safe Prompt Design | Intermediate |
| S07E05 | Context Management: Windows, Memory, Summarization, and Token Budgets | Intermediate |

### S07E01 — Anatomy of an LLM API Call: Messages, Tokens, Parameters, and Streaming

**Depth:** Foundational  
**Learning objective:** Understand every part of a chat-completion style request and response, and what each costs.  
**Prerequisites:** S06E02, S06E16, S01E16  
**Expected outcome:** Make, inspect and cost a basic LLM call and interpret its metadata.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Request**

- Roles: system, user, assistant, tool
- Model selection and parameters (temperature, max tokens, stop)
- Token accounting for input and output

**Topic 2 — The Response**

- Choices, finish reasons and usage metadata
- Truncation and refusals

**Topic 3 — Streaming**

- Event streams and partial tokens
- Assembling streamed responses and handling mid-stream errors

**Topic 4 — Provider API Differences**

- Message and role conventions across providers
- Tool-call schema and streaming-event differences
- Usage metadata, caching fields and error semantics
- Capability comparison across providers is in S07E16

**Topic 5 — Calling It from Code**

- SDK vs raw HTTP
- Authentication and key handling
- Errors, rate-limit and quota responses; timeouts and retries (preview of S07E08)

</details>

**Important concepts**

- *Commands / APIs / Code:* HTTP `POST` chat-completion request with `curl`, Python SDK call, streaming iterator
- *Mechanisms & failure scenarios:* Truncated output from `max_tokens`, leaked API keys, mistaking finish reasons for success.

### S07E02 — Prompt Engineering Mechanisms: Instructions, Examples, and Reasoning

**Depth:** Intermediate  
**Learning objective:** Apply prompting techniques with an understanding of why they work and when they fail.  
**Prerequisites:** S07E01, S06E20  
**Expected outcome:** Write, test and version a prompt and explain its expected failure modes.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Instruction Design**

- Role, task, constraints and output format
- Specificity vs over-constraint
- System vs user message responsibilities

**Topic 2 — In-Context Learning**

- Few-shot examples and their selection
- Order and format sensitivity

**Topic 3 — Reasoning Prompts**

- Chain-of-thought and when to request it
- Decomposition and self-checking prompts

**Topic 4 — Prompts as Software**

- Templating and versioning
- Testing prompts against a fixed set

**Topic 5 — Failure Modes**

- Instructions ignored in long context
- Prompts tuned to one model failing on another
- Avoiding tool-specific folklore

</details>

**Important concepts**

- *Commands / APIs / Code:* prompt templates with variables, side-by-side prompt comparison harness
- *Mechanisms & failure scenarios:* Sensitivity to example order, instructions ignored in long context, prompts tuned to one model failing on another.

### S07E03 — Structured Outputs: JSON Schemas, Validation, and Repair

**Depth:** Intermediate  
**Learning objective:** Get machine-readable output from a probabilistic model and handle the cases where it breaks.  
**Prerequisites:** S07E01, S01E05  
**Expected outcome:** Build an extraction step that returns validated structured data with bounded repair.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Getting Structure**

- Prompt-only JSON vs JSON mode vs schema-constrained decoding
- Tool-call arguments as structured output
- Enumerations and constrained fields

**Topic 2 — Validation**

- Pydantic validation of model output (link to S01E05)
- Handling refusals and partial output

**Topic 3 — Repair and Retry**

- Bounded retry and repair loops
- Feeding validation errors back to the model

**Topic 4 — Schema Design**

- Simple, unambiguous schemas
- Nested vs flat; optional fields
- Evolving schemas safely and semantic (not just syntactic) validation

</details>

**Important concepts**

- *Commands / APIs / Code:* `response_format` / schema parameters (concept), `model_validate_json`
- *Mechanisms & failure scenarios:* Syntactically valid but semantically wrong JSON, truncated JSON, schema constraints degrading answer quality.

### S07E04 — Prompt Injection and Safe Prompt Design

**Depth:** Intermediate  
**Learning objective:** Recognize why instructions and data share one channel and design prompts that limit damage.  
**Prerequisites:** S07E02  
**Expected outcome:** Explain injection mechanics and apply layered mitigations proportional to risk.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Problem**

- Direct and indirect prompt injection
- Why models cannot reliably separate instructions from data

**Topic 2 — Realistic Attack Examples**

- Documents, web pages and emails carrying instructions
- Data exfiltration through generated links

**Topic 3 — Design Defenses**

- Delimiting and labeling untrusted content
- Least privilege for any action the model can trigger
- Output validation and confirmation steps

**Topic 4 — Limits and Testing**

- No prompt-only defense is sufficient
- Defense in depth (preview of S09E12 and S14E05)
- Testing with adversarial inputs

</details>

**Important concepts**

- *Commands / APIs / Code:* delimiter templates, adversarial test cases, output filter sketch
- *Mechanisms & failure scenarios:* Document text overriding system instructions, data exfiltration through generated links, overreliance on "ignore malicious instructions" text.

### S07E05 — Context Management: Windows, Memory, Summarization, and Token Budgets

**Depth:** Intermediate  
**Learning objective:** Decide what goes into a prompt on each turn and manage conversation state within limits.  
**Prerequisites:** S07E01, S06E15  
**Expected outcome:** Implement a context policy that keeps cost bounded and quality stable.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Context Budget**

- Window size, input/output split and cost
- Position and attention effects
- Token counting before sending

**Topic 2 — Conversation State**

- Stateless APIs and history replay
- Storing state outside the model

**Topic 3 — Truncation and Summarization**

- Sliding windows and rolling summaries
- Summaries drifting from facts

**Topic 4 — Context Hygiene**

- Removing stale or conflicting content
- Prompt-caching-friendly ordering (link to S07E09)
- Context poisoning

</details>

**Important concepts**

- *Commands / APIs / Code:* token-budget manager, rolling summary function
- *Mechanisms & failure scenarios:* Silent truncation of key instructions, summaries drifting from facts, growing history raising cost every turn.

<a id="s07-module-2"></a>

## Module 2 — Application Architecture and Reliability

**5 episodes (S07E06–S07E10) · 21 topics.** This module covers: GenAI Application Architecture; Streaming, Async, and Real-Time Backends; Reliability Patterns; Caching and Cost Control; Orchestration Frameworks.

| ID | Episode | Depth |
|---|---|---|
| S07E06 | GenAI Application Architecture: Gateway, Orchestration, State, and Tools | Intermediate |
| S07E07 | Streaming, Async, and Real-Time Backends | Intermediate |
| S07E08 | Reliability Patterns: Retries, Timeouts, Fallbacks, and Rate Limits | Intermediate |
| S07E09 | Caching and Cost Control: Prompt Caching, Semantic Caching, and Batching | Intermediate |
| S07E10 | Orchestration Frameworks: What They Abstract and When Not to Use Them | Intermediate |

### S07E06 — GenAI Application Architecture: Gateway, Orchestration, State, and Tools

**Depth:** Intermediate  
**Learning objective:** Understand the components of a production GenAI app and where each concern belongs.  
**Prerequisites:** S07E01, S01E16  
**Expected outcome:** Draw and justify a layered GenAI application architecture.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Layers**

- Client, API/backend, orchestration, model access, data stores
- Where prompts, configuration and secrets live

**Topic 2 — Request Flows**

- Synchronous request vs background jobs
- Choosing synchronous, streaming or asynchronous flows

**Topic 3 — State and Storage**

- Conversations, user data and caches
- Tenancy and data isolation

**Topic 4 — Cross-Cutting Concerns**

- Authentication and authorization
- Logging and tracing hooks
- Feature flags and model routing

**Topic 5 — Reference Patterns and Failure Boundaries**

- Chat assistant, document processor and copilot patterns
- Where failures should be contained

</details>

**Important concepts**

- *Commands / APIs / Code:* architecture sketch, FastAPI service skeleton calling an LLM
- *Mechanisms & failure scenarios:* Prompt logic scattered across the codebase, user data leaking across tenants, long calls blocking workers.

### S07E07 — Streaming, Async, and Real-Time Backends

**Depth:** Intermediate  
**Learning objective:** Deliver token-by-token responses and handle concurrent LLM calls efficiently.  
**Prerequisites:** S07E06, S01E15  
**Expected outcome:** Build a streaming endpoint with cancellation and bounded concurrency.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Streaming Protocols**

- Server-sent events vs WebSockets
- Chunked responses and backpressure
- Client rendering and cancellation

**Topic 2 — Async Python for LLM Calls**

- `asyncio` and concurrent requests
- Connection pooling and timeouts
- Semaphores and rate limiting

**Topic 3 — Cancellation and Cleanup**

- Disconnected clients leaving generation running
- Propagating cancellation to upstream calls

**Topic 4 — Long-Running Work**

- Background jobs and queues
- Polling vs callbacks vs push
- Progress reporting and resumability

</details>

**Important concepts**

- *Commands / APIs / Code:* FastAPI `StreamingResponse`, `asyncio.gather`, `asyncio.Semaphore`
- *Mechanisms & failure scenarios:* Disconnected clients leaving generation running, event-loop blocking, unbounded concurrency hitting rate limits.

### S07E08 — Reliability Patterns: Retries, Timeouts, Fallbacks, and Rate Limits

**Depth:** Intermediate  
**Learning objective:** Make an application resilient to the failure modes of external model APIs.  
**Prerequisites:** S07E07  
**Expected outcome:** Design retry, timeout and fallback policy for an LLM-dependent feature.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Failure Types**

- Rate limits, timeouts, 5xx errors and content filters
- Latency variance and tail latency
- Partial and malformed responses

**Topic 2 — Resilience Mechanisms**

- Exponential backoff with jitter
- Circuit breakers and bulkheads
- Idempotency for side-effecting calls

**Topic 3 — Fallbacks and Degradation**

- Secondary models and providers
- Cached or simplified responses
- Honest user-facing errors

**Topic 4 — Testing Failure Paths**

- Fault injection against model APIs
- Retry storms and fallback format mismatches

</details>

**Important concepts**

- *Commands / APIs / Code:* retry decorator with jitter, fallback chain, `tenacity` (concept)
- *Mechanisms & failure scenarios:* Retry storms amplifying outages, duplicate actions from retried tool calls, fallback model with different output format.

### S07E09 — Caching and Cost Control: Prompt Caching, Semantic Caching, and Batching

**Depth:** Intermediate  
**Learning objective:** Reduce cost and latency without silently degrading answers.  
**Prerequisites:** S07E05, S07E08  
**Expected outcome:** Build a cost model for a feature and choose safe optimizations.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Where Cost Comes From**

- Input vs output tokens
- Context-length growth and model tier choice

**Topic 2 — Prompt Caching**

- Provider prefix caching and prompt design for cache hits
- Provider prefix-caching mechanics: what counts as a cacheable prefix
- Prompt design for cache hits: static content first, dynamic content last
- Cache lifetime and pricing effects

**Topic 3 — Semantic and Exact Caching**

- Correctness risks of near-match caches
- Invalidation and cross-user isolation

**Topic 4 — Other Levers**

- Batch APIs and off-peak jobs
- Model routing by difficulty
- Output length control

**Topic 5 — Budgets and Monitoring**

- Per-feature cost models
- Spend limits, alerts and unbounded-loop protection

</details>

**Important concepts**

- *Commands / APIs / Code:* cost calculator, semantic-cache lookup sketch, batch job submission (concept)
- *Mechanisms & failure scenarios:* Semantic cache returning a near-but-wrong answer, cache keys leaking across users, cost spikes from unbounded loops.

### S07E10 — Orchestration Frameworks: What They Abstract and When Not to Use Them

**Depth:** Intermediate  
**Learning objective:** Evaluate LLM frameworks by the patterns they encapsulate rather than by brand.  
**Prerequisites:** S07E06  
**Expected outcome:** Make and defend a build-versus-framework decision.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Common Abstractions**

- Chains and pipelines, prompt templates, output parsers
- Retrievers, tools, memory and provider adapters

**Topic 2 — Trade-offs**

- Speed of prototyping vs transparency and debuggability
- Version churn and lock-in
- Hidden prompts inside abstractions

**Topic 3 — Decision Framework**

- Thin SDK plus own orchestration vs a framework
- Observability hooks required and migration paths

</details>

**Important concepts**

- *Commands / APIs / Code:* same task implemented with raw SDK and a framework (concept comparison)
- *Mechanisms & failure scenarios:* Hidden prompts inside abstractions, breaking changes between versions, hard-to-trace failures.

<a id="s07-module-3"></a>

## Module 3 — Multimodal, Customization, and Model Choice

**6 episodes (S07E11–S07E16) · 25 topics.** This module covers: Multimodal Applications; Real-Time Voice AI Architecture; Prompting vs RAG vs Fine-Tuning; Fine-Tuning in Practice; Open Models and Local Inference; Foundation Model Providers and Their APIs.

| ID | Episode | Depth |
|---|---|---|
| S07E11 | Multimodal Applications: Vision, Documents, and Audio Inputs | Intermediate |
| S07E12 | Real-Time Voice AI Architecture: Streaming, Turn-Taking, and Latency Budgets | Advanced |
| S07E13 | Prompting vs RAG vs Fine-Tuning: Choosing the Right Customization | Intermediate |
| S07E14 | Fine-Tuning in Practice: Data Preparation, Training, and Evaluation | Advanced |
| S07E15 | Open Models and Local Inference: Runtimes, Formats, and Hardware | Intermediate |
| S07E16 | Foundation Model Providers and Their APIs: OpenAI, Anthropic, Google, and Open-Weight Families | Intermediate |

### S07E11 — Multimodal Applications: Vision, Documents, and Audio Inputs

**Depth:** Intermediate  
**Learning objective:** Build features that accept images, documents and audio, understanding their cost and failure modes.  
**Prerequisites:** S07E03, S06E24  
**Expected outcome:** Design a multimodal extraction pipeline with validation and fallback.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Vision and Document Understanding**

- Image input formats, resolution and token cost
- OCR vs vision-model reading
- Structured extraction from forms and invoices

**Topic 2 — Audio**

- Transcription and diarization pipelines
- Audio-native models vs cascaded pipelines
- Privacy and consent

**Topic 3 — Production Concerns**

- Preprocessing, size limits and content safety
- Injected instructions inside images and audio

**Topic 4 — Evaluating Extraction**

- Field-level accuracy and confidence thresholds
- Fallback when confidence is low

</details>

**Important concepts**

- *Commands / APIs / Code:* image-input request payload (concept), transcription API call (concept)
- *Mechanisms & failure scenarios:* Misread numbers in tables, resolution loss, injected instructions inside images.

### S07E12 — Real-Time Voice AI Architecture: Streaming, Turn-Taking, and Latency Budgets

**Depth:** Advanced  
**Learning objective:** Understand the architecture and latency constraints of conversational voice systems.  
**Prerequisites:** S07E07, S07E11  
**Expected outcome:** Produce a latency budget and architecture for a voice agent.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Pipeline vs Speech-Native**

- ASR → LLM → TTS cascade
- End-to-end speech models
- Control, cost and latency trade-offs

**Topic 2 — Streaming and Transport**

- WebRTC and WebSocket audio transport
- Jitter, buffering and codecs

**Topic 3 — Turn-Taking**

- Voice activity detection and end-of-speech detection
- Barge-in and interruption handling

**Topic 4 — Latency Budget**

- Per-stage budgets and streaming overlap
- Network and region effects

**Topic 5 — Failure Handling and Privacy**

- Echo, noise and mis-detected end of speech
- Consent, recording and retention

</details>

**Important concepts**

- *Commands / APIs / Code:* latency-budget worksheet, streaming-pipeline diagram
- *Mechanisms & failure scenarios:* Awkward silences from sequential stages, echo/feedback loops, mis-detected end of speech.

### S07E13 — Prompting vs RAG vs Fine-Tuning: Choosing the Right Customization

**Depth:** Intermediate  
**Learning objective:** Decide how to add knowledge, behavior or style to a model with the least cost and risk.  
**Prerequisites:** S07E02, S06E13  
**Expected outcome:** Select a customization strategy with an explicit justification.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — What Each Technique Changes**

- Prompting: behavior in context
- Retrieval: knowledge at inference time
- Fine-tuning: behavior and style in weights

**Topic 2 — Decision Criteria**

- Freshness, data volume, privacy, latency and cost
- Failure modes of each

**Topic 3 — A Practical Process**

- Start with prompts and evals; add retrieval for knowledge gaps
- Fine-tune only with evidence and data

</details>

**Important concepts**

- *Commands / APIs / Code:* decision matrix worksheet
- *Mechanisms & failure scenarios:* Fine-tuning to inject facts that retrieval would handle better, retrieval for tasks that are really style problems.

### S07E14 — Fine-Tuning in Practice: Data Preparation, Training, and Evaluation

**Depth:** Advanced  
**Learning objective:** Run a small, disciplined fine-tuning project end to end.  
**Prerequisites:** S07E13, S06E13  
**Expected outcome:** Plan a fine-tuning run with data, metrics and rollback.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Data**

- Collecting and cleaning examples
- Format, balance, deduplication and held-out set
- Privacy and licensing

**Topic 2 — Training Options**

- Hosted fine-tuning APIs vs open-model training
- Full vs adapter-based tuning

**Topic 3 — Hyperparameters and Cost**

- Hyperparameters that matter
- Cost and time estimation

**Topic 4 — Evaluation**

- Before/after comparison on a fixed eval set
- Regression and safety checks

**Topic 5 — Deployment**

- Versioning and rollback
- Contamination between train and eval data

</details>

**Important concepts**

- *Commands / APIs / Code:* JSONL training file, `trl`/provider fine-tune job (concept), eval comparison script
- *Mechanisms & failure scenarios:* Overfitting to a narrow style, contamination between train and eval data, improved target metric with hidden regressions.

### S07E15 — Open Models and Local Inference: Runtimes, Formats, and Hardware

**Depth:** Intermediate  
**Learning objective:** Run models locally or self-hosted and understand the practical constraints.  
**Prerequisites:** S06E17, S06E23  
**Expected outcome:** Estimate hardware needs for a model and run it behind a standard API.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Runtimes and Formats**

- Transformers, llama.cpp-style runtimes and Ollama-style tools
- Quantized formats and memory requirements

**Topic 2 — Hardware Reality**

- VRAM vs RAM vs unified memory
- Tokens-per-second expectations; CPU vs GPU inference

**Topic 3 — Serving Locally and When It Makes Sense**

- OpenAI-compatible local endpoints
- Chat-template and tokenizer pitfalls
- Privacy, offline use and cost at volume
- Quality gap vs frontier hosted models and operational burden

</details>

**Important concepts**

- *Commands / APIs / Code:* `ollama run`, `llama.cpp` server (concept), `curl` to a local endpoint
- *Mechanisms & failure scenarios:* Model not fitting in memory, slow CPU-only inference, version-specific chat templates breaking output.

### S07E16 — Foundation Model Providers and Their APIs: OpenAI, Anthropic, Google, and Open-Weight Families

**Depth:** Intermediate  
**Learning objective:** Compare the major model providers and open-weight families by the capabilities that matter to an application, and design provider-portable integrations with routing, fallback and cost control.  
**Prerequisites:** S06E23, S07E01, S07E08, S07E09  
**Expected outcome:** Select models and providers for a use case from capability and constraint evidence, and design an application-side integration layer that can route, fall back and control cost without rewriting application code.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The Provider and Model-Family Landscape**

- Closed-model providers: OpenAI (GPT and reasoning models; ChatGPT the consumer product vs the API), Anthropic (Claude), Google (Gemini)
- Model tiers, context lengths, modalities and deployment channels (direct API, cloud platforms, local)
- Why names, versions and capabilities change quickly and how to track them

**Topic 2 — Open-Weight Families**

- Llama, Qwen, Gemma and Mistral: sizes, specializations and typical strengths
- Licenses and usage terms; what "open-weight" does and does not allow
- Hosting options: self-hosted, managed endpoints and local runtimes (link to S07E15)

**Topic 3 — Mapping API Capabilities**

- Messages, roles and system prompts across providers
- Tool and function calling, structured output and streaming events as comparable capabilities
- Prompt caching, batch processing, reasoning controls and multimodal inputs
- Rate-limit, quota and error semantics

**Topic 4 — Multi-Provider Integration**

- Provider abstraction layers and normalized request/response schemas
- Routing by task, difficulty, latency and cost; fallback chains and retries
- Cost optimization: model tiering, caching, batching and output limits
- What cannot be abstracted away: provider-specific features that break portability

**Topic 5 — Reading Provider Claims**

- Benchmarks vs evaluation on your own task (link to S06E22 and S07E19)
- Deprecation, version pinning and migration planning
- Data handling, retention and regional availability terms

</details>

**Important concepts**

- *Commands / APIs / Code:* Provider-neutral request builders showing equivalent calls across providers (illustrative), capability matrix template, routing and fallback configuration sketch, per-request cost calculator
- *Mechanisms & failure scenarios:* Code coupled to one provider's schema, model deprecations breaking production, fallback models with incompatible tool or structured-output behavior, quality regressions hidden by model-name aliases, benchmark claims used instead of task evaluation, licence or data-handling terms overlooked.

<a id="s07-module-4"></a>

## Module 4 — Generative Media Engineering

**2 episodes (S07E17–S07E18) · 13 topics.** This module covers: Image Generation Engineering; Video and Audio Generation Engineering.

| ID | Episode | Depth |
|---|---|---|
| S07E17 | Image Generation Engineering: Pipelines, Control, Customization, and Serving | Intermediate |
| S07E18 | Video and Audio Generation Engineering | Advanced |

### S07E17 — Image Generation Engineering: Pipelines, Control, Customization, and Serving

**Depth:** Intermediate  
**Learning objective:** Build and operate image-generation features: understand the pipeline stages, control generation, customize models, evaluate output and serve it within cost and safety limits.  
**Prerequisites:** S05E21, S07E06, S07E09  
**Expected outcome:** Design an image-generation service with defined controls, evaluation, safety measures and capacity plan.

<details>
<summary>Topics and subtopics (7 topics)</summary>

**Topic 1 — Pipeline Anatomy**

- Text encoder, denoising network, scheduler and decoder
- Where time and memory go per stage

**Topic 2 — Controlling Generation**

- Prompts, negative prompts, seeds and guidance scale
- Image-to-image, inpainting and outpainting

**Topic 3 — Structural Control and Customization**

- Control signals (edges, depth, pose) via control networks and adapters (concept)
- Low-rank adapters and subject/style customization, and their data requirements

**Topic 4 — Editing and Enhancement Workflows**

- Upscaling and refinement passes
- Composition of multi-step workflows

**Topic 5 — Evaluation**

- Prompt-alignment and aesthetic metrics, and the limits of automated scores
- Human evaluation protocols

**Topic 6 — Serving**

- GPU memory, batching and latency per image
- Job queues, caching of results and cost per image

**Topic 7 — Safety, Provenance, and Rights**

- Input and output safety filters
- Watermarking and content credentials
- Licensing and consent for training data and likenesses

</details>

**Important concepts**

- *Commands / APIs / Code:* `diffusers` text-to-image, image-to-image and inpainting calls (illustrative), seed and guidance settings, GPU memory monitoring, queue-based job submission
- *Mechanisms & failure scenarios:* Prompt-adherence failures, anatomical and text artifacts, non-reproducible outputs, GPU out-of-memory under concurrent requests, safety-filter bypass, training-data and licensing disputes.

### S07E18 — Video and Audio Generation Engineering

**Depth:** Advanced  
**Learning objective:** Understand how video, music and speech are generated, what drives their cost and failure modes, and how to build asynchronous generation services responsibly.  
**Prerequisites:** S07E17, S05E17, S05E14  
**Expected outcome:** Choose and integrate video or audio generation capabilities with realistic cost, latency, quality and policy controls.

<details>
<summary>Topics and subtopics (6 topics)</summary>

**Topic 1 — Video Generation Approaches**

- Diffusion over spatiotemporal latents and video transformers (concept)
- Text-to-video, image-to-video and video-to-video

**Topic 2 — Temporal Consistency and Control**

- Identity and motion consistency, camera and keyframe control
- Failure modes: flicker, drift and implausible physics

**Topic 3 — Cost and Latency**

- Why video is orders of magnitude heavier than images
- Resolution, duration and step-count trade-offs

**Topic 4 — Music and Speech Generation**

- Codec-token language models and diffusion for audio
- Text-to-speech product engineering; voice consent and verification

**Topic 5 — Asynchronous Service Design**

- Job queues, status polling and webhooks
- Storage, delivery and retention of large media outputs

**Topic 6 — Safety, Detection, and Rights**

- Deepfake risk and misuse policies
- Watermarking, provenance and detection limits
- Licensing and rights management

</details>

**Important concepts**

- *Commands / APIs / Code:* Asynchronous generation job API pattern (submit, poll, webhook), video-latent size estimation, audio duration/cost calculator (illustrative)
- *Mechanisms & failure scenarios:* Temporal flicker and identity drift, physics and motion errors, long generation times and high cost per second, lip-sync mismatch, voice cloning without consent, deepfake misuse.

<a id="s07-module-5"></a>

## Module 5 — Quality, Safety, and Productization

**3 episodes (S07E19–S07E21) · 12 topics.** This module covers: Evaluating GenAI Applications; Guardrails; Building a Production GenAI Service.

| ID | Episode | Depth |
|---|---|---|
| S07E19 | Evaluating GenAI Applications: Datasets, Rubrics, and LLM Judges | Intermediate |
| S07E20 | Guardrails: Input and Output Filtering, Moderation, and PII Handling | Intermediate |
| S07E21 | Building a Production GenAI Service: End-to-End Blueprint | Intermediate |

### S07E19 — Evaluating GenAI Applications: Datasets, Rubrics, and LLM Judges

**Depth:** Intermediate  
**Learning objective:** Build a small but trustworthy evaluation loop for an LLM feature before scaling it with Season 12.  
**Prerequisites:** S06E22, S07E02  
**Expected outcome:** Create an eval set and automated scoring that can gate prompt or model changes.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Evaluation Sets**

- Collecting representative and edge-case examples
- Golden answers vs rubrics
- Size and coverage

**Topic 2 — Scoring**

- Exact match and programmatic checks
- LLM judges: prompt design and bias checks
- Human spot-checks

**Topic 3 — Using Evals in Development**

- Prompt and model comparison runs
- Regression gates and tracking results over time

**Topic 4 — Pitfalls**

- Judge sharing the generator's blind spots
- Eval set drift from real traffic and optimizing to the eval set

</details>

**Important concepts**

- *Commands / APIs / Code:* evaluation loop over JSONL, rubric prompt, results table
- *Mechanisms & failure scenarios:* Judge sharing the generator's blind spots, eval set drift from real traffic, optimizing to the eval set.

### S07E20 — Guardrails: Input and Output Filtering, Moderation, and PII Handling

**Depth:** Intermediate  
**Learning objective:** Apply layered safety controls around a model and understand their cost and limits.  
**Prerequisites:** S07E04, S07E03  
**Expected outcome:** Design guardrail layers appropriate to an application's risk.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Control Points**

- Input validation and policy checks
- Output moderation and schema enforcement
- Tool-permission checks

**Topic 2 — Sensitive Data**

- PII detection and redaction
- Data retention and logging policy
- Provider data-handling terms

**Topic 3 — Operating Guardrails**

- False-positive/false-negative trade-offs
- Latency and cost added
- Monitoring guardrail triggers

**Topic 4 — Testing Guardrails**

- Bypass attempts and encoding tricks
- Measuring over-blocking

</details>

**Important concepts**

- *Commands / APIs / Code:* moderation endpoint call (concept), regex/NER-based redactor sketch
- *Mechanisms & failure scenarios:* Over-blocking harming usability, PII retained in logs, guardrail bypass through encoding tricks.

### S07E21 — Building a Production GenAI Service: End-to-End Blueprint

**Depth:** Intermediate  
**Learning objective:** Combine the season's components into one coherent, production-ready design.  
**Prerequisites:** S07E19, S07E20, S07E09  
**Expected outcome:** Produce a launch-ready design for a GenAI feature and defend its trade-offs.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Requirements to Design**

- Use case, quality bar, latency, cost and risk
- Data flow and component selection
- Build/buy decisions

**Topic 2 — Putting It Together**

- API, orchestration, validation, guardrails and caching
- Observability hooks and feedback capture

**Topic 3 — Deployment and Configuration**

- Environments, secrets and configuration management
- Deployment topology for LLM backends (containers, serverless)
- Configuration rollout and feature flags

**Topic 4 — Readiness Review and Handoff**

- Evaluation, security and failure-mode checklist
- Launch plan: shadow, canary and rollback
- Handoff to RAG (Season 8) and LLMOps (Season 12)

</details>

**Important concepts**

- *Commands / APIs / Code:* reference architecture diagram, readiness checklist
- *Mechanisms & failure scenarios:* No rollback plan for a bad prompt change, missing feedback capture, unmonitored cost growth.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s07-module-1) | Starting point of the season |
| [Module 2](#s07-module-2) | [Module 1](#s07-module-1) (S07E01, S07E05) |
| [Module 3](#s07-module-3) | [Module 1](#s07-module-1) (S07E01, S07E02, S07E03); [Module 2](#s07-module-2) (S07E07, S07E08, S07E09) |
| [Module 4](#s07-module-4) | [Module 2](#s07-module-2) (S07E06, S07E09) |
| [Module 5](#s07-module-5) | [Module 1](#s07-module-1) (S07E02, S07E03, S07E04); [Module 2](#s07-module-2) (S07E09) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 6 — LLMs & Transformer Architecture](../season-06-llms-and-transformers/roadmap.md)
- **Next:** [Season 8 — RAG Engineering](../season-08-rag-engineering/roadmap.md)
- **Draws on:** [Season 1](../season-01-python-for-ai-ml/roadmap.md) (S01E05, S01E15, S01E16); [Season 5](../season-05-deep-learning/roadmap.md) (S05E14, S05E17, S05E21); [Season 6](../season-06-llms-and-transformers/roadmap.md) (S06E02, S06E13, S06E15, S06E16, S06E17, S06E20, S06E22, S06E23, S06E24)
- **Required by:** [Season 8](../season-08-rag-engineering/roadmap.md) (via S07E03, S07E04, S07E09, S07E13, S07E19); [Season 9](../season-09-ai-agents-and-mcp/roadmap.md) (via S07E03, S07E04, S07E05, S07E10, S07E19); [Season 10](../season-10-advanced-agentic-ai/roadmap.md) (via S07E09); [Season 12](../season-12-llmops-engineering/roadmap.md) (via S07E02, S07E08, S07E09, S07E14, S07E19, S07E20, S07E21); [Season 13](../season-13-ai-infrastructure/roadmap.md) (via S07E06); [Season 14](../season-14-production-ai-systems/roadmap.md) (via S07E04, S07E08); [Season 15](../season-15-ai-for-devops/roadmap.md) (via S07E03, S07E19)
