# Season 8 Roadmap — RAG Engineering

[← Season 8 overview](README.md) · [All seasons](../README.md)

**4 modules · 19 episodes · 79 topics · 202 subtopics · Level: Intermediate → Advanced**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Building the Knowledge Index](#s08-module-1)
- [Module 2 — Retrieval Engineering](#s08-module-2)
- [Module 3 — Generation, Context, and Advanced Patterns](#s08-module-3)
- [Module 4 — Evaluation, Production, and Security](#s08-module-4)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Teach retrieval-augmented generation as an information-retrieval system with a language model at the end: ingestion, chunking, embeddings, indexes, hybrid retrieval, reranking, grounded generation, evaluation, debugging, security and production operation. Vector-database and framework products are examples of patterns, not the subject.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S08E01 | Understand the problem RAG solves and trace a question through every pipeline stage. |
| S08E02 | Turn messy real-world documents into clean, structured text without losing meaning. |
| S08E03 | Choose chunk boundaries that make retrieval precise and answers complete. |
| S08E04 | Choose and use embedding models deliberately and understand what they can and cannot represent. |
| S08E05 | Understand approximate nearest-neighbor indexes and their recall/latency/memory trade-offs. |
| S08E06 | Understand what a vector database adds beyond an index and how to choose and operate one. |
| S08E07 | Understand how retrieval strategies work and how engineers select and troubleshoot them. |
| S08E08 | Improve precision with a second-stage ranker and bridge the gap between how users ask and how documents are written. |
| S08E09 | Turn retrieved chunks into a prompt that produces faithful, attributable answers. |
| S08E10 | Decide what information to give the model and in what form, including when to skip retrieval altogether. |
| S08E11 | Recognize when basic RAG is insufficient and apply hierarchical, multi-representation and corrective retrieval patterns to specific failure modes. |
| S08E12 | Understand when relationship-centric retrieval over a knowledge graph beats vector search, how such indexes are built, and what they cost. |
| S08E13 | Answer questions over databases and tables safely and accurately. |
| S08E14 | Extend RAG to non-text content and specialized corpora. |
| S08E15 | Measure retrieval and generation separately so improvements are targeted and provable. |
| S08E16 | Locate the stage responsible for a bad answer and fix the root cause. |
| S08E17 | Operate RAG at scale within latency, cost and freshness requirements. |
| S08E18 | Prevent data leakage and manipulation through the retrieval layer. |
| S08E19 | Assemble the season's concepts into a full architecture with ownership, evaluation and operations. |

## Prerequisites and Expected Knowledge

- **Season 1 — [Python for AI & ML Engineering](../season-01-python-for-ai-ml/roadmap.md)**: S01E10, S01E11
- **Season 2 — [Mathematics for AI & Machine Learning](../season-02-mathematics-for-ai/roadmap.md)**: S02E05
- **Season 4 — [Advanced Machine Learning Engineering](../season-04-advanced-ml-engineering/roadmap.md)**: S04E11
- **Season 5 — [Deep Learning & Neural Networks](../season-05-deep-learning/roadmap.md)**: S05E13, S05E15, S05E25
- **Season 6 — [LLMs & Transformer Architecture](../season-06-llms-and-transformers/roadmap.md)**: S06E02, S06E07, S06E15
- **Season 7 — [Generative AI Application Engineering](../season-07-generative-ai-engineering/roadmap.md)**: S07E03, S07E04, S07E09, S07E13, S07E19

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Building the Knowledge Index](#s08-module-1) | S08E01–S08E04 | 4 | 1 Foundational, 3 Intermediate |
| 2 | [Retrieval Engineering](#s08-module-2) | S08E05–S08E08 | 4 | 1 Advanced, 3 Intermediate |
| 3 | [Generation, Context, and Advanced Patterns](#s08-module-3) | S08E09–S08E14 | 6 | 3 Intermediate, 3 Advanced |
| 4 | [Evaluation, Production, and Security](#s08-module-4) | S08E15–S08E19 | 5 | 1 Intermediate, 4 Advanced |

<a id="s08-module-1"></a>

## Module 1 — Building the Knowledge Index

**4 episodes (S08E01–S08E04) · 17 topics.** This module covers: Why RAG Exists and the Anatomy of a RAG Pipeline; Document Ingestion and Parsing; Chunking Strategies and Metadata Design; Embedding Models.

| ID | Episode | Depth |
|---|---|---|
| S08E01 | Why RAG Exists and the Anatomy of a RAG Pipeline | Foundational |
| S08E02 | Document Ingestion and Parsing: PDFs, HTML, Tables, and OCR | Intermediate |
| S08E03 | Chunking Strategies and Metadata Design | Intermediate |
| S08E04 | Embedding Models: Selection, Dimensions, and Domain Fit | Intermediate |

### S08E01 — Why RAG Exists and the Anatomy of a RAG Pipeline

**Depth:** Foundational  
**Learning objective:** Understand the problem RAG solves and trace a question through every pipeline stage.  
**Prerequisites:** S07E13, S05E13  
**Expected outcome:** Describe a complete RAG pipeline and name the failure points at each stage.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Problem RAG Solves**

- Knowledge cutoffs, private data and hallucination
- Why not just put everything in the prompt
- RAG vs fine-tuning (link to S07E13)

**Topic 2 — The Pipeline**

- Ingestion → chunking → embedding → indexing
- Query → retrieval → context assembly → generation

**Topic 3 — Where Each Stage Fails**

- Not in the corpus, not retrieved, retrieved but ignored, generation errors
- Stale indexes

**Topic 4 — A Minimal Working System**

- End-to-end data flow
- What to measure first
- Roadmap of the season

</details>

**Important concepts**

- *Commands / APIs / Code:* minimal RAG loop in Python (embed, search, prompt, generate)
- *Mechanisms & failure scenarios:* Retrieval returning irrelevant text that the model then trusts, answers with no supporting evidence, stale indexes.

### S08E02 — Document Ingestion and Parsing: PDFs, HTML, Tables, and OCR

**Depth:** Intermediate  
**Learning objective:** Turn messy real-world documents into clean, structured text without losing meaning.  
**Prerequisites:** S08E01, S01E11, S05E15  
**Expected outcome:** Design an ingestion step that preserves structure and records provenance.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Sources and Formats**

- PDFs, Office documents, HTML, wikis, tickets and databases
- Text-based vs scanned documents
- Connectors and incremental sync

**Topic 2 — Extraction Quality**

- Layout, reading order, headers and footers
- OCR and vision-model extraction (link to S05E15)

**Topic 3 — Tables, Lists, and Images**

- Tables and their serialization
- Code blocks, figures and captions

**Topic 4 — Cleaning and Deduplication**

- Boilerplate removal and near-duplicate detection
- Versioned documents

**Topic 5 — Metadata and Validation**

- Capturing source, section, date and permissions
- Ingestion validation and failure handling

</details>

**Important concepts**

- *Commands / APIs / Code:* PDF/HTML parsing libraries (concept), OCR invocation, metadata schema
- *Mechanisms & failure scenarios:* Columns merged into nonsense, tables flattened losing structure, silently skipped scanned pages.

### S08E03 — Chunking Strategies and Metadata Design

**Depth:** Intermediate  
**Learning objective:** Choose chunk boundaries that make retrieval precise and answers complete.  
**Prerequisites:** S08E02, S06E02  
**Expected outcome:** Select and justify a chunking strategy using retrieval experiments.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Chunking Approaches**

- Fixed-size, recursive, sentence/paragraph and semantic chunking
- Structure-aware chunking (headings, code, tables)
- Overlap and its costs

**Topic 2 — Trade-offs**

- Small chunks: precision vs lost context
- Large chunks: recall vs noise and cost

**Topic 3 — Metadata and Index Evolution**

- Fields that enable filtering and citations
- Contextual headers prepended to chunks
- Re-chunking and index versioning
- Measuring chunking with retrieval experiments

</details>

**Important concepts**

- *Commands / APIs / Code:* text splitters (concept), chunk-size experiment harness
- *Mechanisms & failure scenarios:* Answers split across chunks, headings lost from context, chunk sizes exceeding embedding-model limits.

### S08E04 — Embedding Models: Selection, Dimensions, and Domain Fit

**Depth:** Intermediate  
**Learning objective:** Choose and use embedding models deliberately and understand what they can and cannot represent.  
**Prerequisites:** S06E07, S05E25  
**Expected outcome:** Compare embedding models on a task-specific retrieval test set.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — How Embedding Models Work**

- Encoder-based text embeddings and contrastive training
- Pooling and normalization

**Topic 2 — Query vs Document Embeddings**

- Asymmetric and instruction-prefixed models
- Similarity metrics

**Topic 3 — Choosing a Model**

- Dimensions, context length and multilingual support
- Benchmarks and why to test on your data
- Cost, latency, hosted vs self-hosted

**Topic 4 — Operating Embeddings**

- Re-embedding when models change
- Domain adaptation and fine-tuning (concept)

**Topic 5 — Known Weaknesses**

- Negation, numbers and exact identifiers
- Mixing embeddings from different models; truncation of long chunks

</details>

**Important concepts**

- *Commands / APIs / Code:* `SentenceTransformer.encode`, embeddings API call (concept), cosine similarity
- *Mechanisms & failure scenarios:* Mixing embeddings from different models in one index, truncation of long chunks, poor handling of codes and IDs.

<a id="s08-module-2"></a>

## Module 2 — Retrieval Engineering

**4 episodes (S08E05–S08E08) · 17 topics.** This module covers: Vector Search Internals; Vector Databases in Practice; Dense, Sparse, and Hybrid Retrieval; Reranking and Query Transformation.

| ID | Episode | Depth |
|---|---|---|
| S08E05 | Vector Search Internals: Flat, HNSW, IVF, and Quantization | Advanced |
| S08E06 | Vector Databases in Practice: Filtering, Updates, and Operations | Intermediate |
| S08E07 | Dense, Sparse, and Hybrid Retrieval | Intermediate |
| S08E08 | Reranking and Query Transformation | Intermediate |

### S08E05 — Vector Search Internals: Flat, HNSW, IVF, and Quantization

**Depth:** Advanced  
**Learning objective:** Understand approximate nearest-neighbor indexes and their recall/latency/memory trade-offs.  
**Prerequisites:** S08E04, S02E05  
**Expected outcome:** Select and tune an ANN index to meet recall and latency targets.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Exact vs Approximate Search**

- Brute-force cost
- Why exactness is traded for speed
- Recall as the key quality measure

**Topic 2 — Graph Indexes (HNSW)**

- Navigable small-world graphs and layers
- `M`, `efConstruction` and `efSearch`

**Topic 3 — Inverted-File Indexes (IVF)**

- Clustering, probes and recall trade-offs
- Training the coarse quantizer on representative data
- Combining IVF with product quantization

**Topic 4 — Compression**

- Product quantization and scalar quantization
- Memory vs recall

**Topic 5 — Operating Indexes**

- Build time, memory and update cost
- Filtered search complications
- Tuning for a recall target

</details>

**Important concepts**

- *Commands / APIs / Code:* `faiss` index types (concept), `hnswlib` parameters, recall measurement against brute force
- *Mechanisms & failure scenarios:* Low recall from too-small `efSearch`, memory blow-up at scale, index degradation after many updates.

### S08E06 — Vector Databases in Practice: Filtering, Updates, and Operations

**Depth:** Intermediate  
**Learning objective:** Understand what a vector database adds beyond an index and how to choose and operate one.  
**Prerequisites:** S08E05  
**Expected outcome:** Choose a vector store for a workload and describe how to keep it correct and fresh.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — What a Vector Database Provides**

- Storage, indexing, metadata filtering and persistence
- Collections, shards and replicas
- Libraries vs embedded vs managed services

**Topic 2 — Filtering and Consistency**

- Pre-filter vs post-filter vs filtered ANN
- Upserts, deletes and freshness

**Topic 3 — Multi-Tenancy and Access**

- Tenant isolation and access control
- Tenant isolation: namespaces, partitions or separate collections
- Per-tenant quotas and noisy-neighbor effects

**Topic 4 — Selection and Operations**

- Scale, latency, cost and hybrid-search support
- Backup, migration and re-indexing
- Using existing databases with vector extensions
- Managed search and vector services as deployment options (architecture mapping in S13E17)

</details>

**Important concepts**

- *Commands / APIs / Code:* collection create/upsert/query (concept across products), pgvector query
- *Mechanisms & failure scenarios:* Filters removing most candidates and hurting recall, stale vectors after document updates, noisy-neighbor tenants.

### S08E07 — Dense, Sparse, and Hybrid Retrieval

**Depth:** Intermediate  
**Learning objective:** Understand how retrieval strategies work and how engineers select and troubleshoot them.  
**Prerequisites:** S08E04, S08E06  
**Expected outcome:** Explain and compare retrieval strategies and diagnose common retrieval failures.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Dense Retrieval**

- Embeddings and semantic similarity
- Vector indexing
- Approximate nearest-neighbor search
- Limitations and failure cases

**Topic 2 — Sparse Retrieval**

- Inverted indexes
- BM25 scoring: term frequency, inverse document frequency, length normalization
- Keyword matching
- Exact identifier retrieval

**Topic 3 — Hybrid Retrieval**

- Dense and sparse result fusion
- Reciprocal Rank Fusion
- Ranking tradeoffs
- Latency and relevance

**Topic 4 — Choosing and Diagnosing**

- Query types that favor each approach
- Diagnosing retrieval failures by comparing dense, sparse and hybrid results
- Tuning fusion weights with enough labeled queries

</details>

**Important concepts**

- *Commands / APIs / Code:* BM25 scoring with a search engine or `rank_bm25` (concept), RRF formula in Python, side-by-side retrieval comparison
- *Mechanisms & failure scenarios:* Dense search missing exact part numbers, BM25 missing paraphrases, fusion weights tuned on too little data.

### S08E08 — Reranking and Query Transformation

**Depth:** Intermediate  
**Learning objective:** Improve precision with a second-stage ranker and bridge the gap between how users ask and how documents are written.  
**Prerequisites:** S08E07  
**Expected outcome:** Design a two-stage retrieval pipeline and justify each added stage with measurements.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Reranking**

- Bi-encoder vs cross-encoder
- Retrieve-then-rerank latency/quality trade-off
- LLM-based rerankers

**Topic 2 — Query Rewriting and Expansion**

- Rewriting conversational queries
- Multi-query and decomposition

**Topic 3 — HyDE and Related Techniques**

- Hypothetical-document embeddings
- When generation-assisted retrieval helps or drifts

**Topic 4 — Routing and Cost**

- Choosing an index or tool per query
- Skipping retrieval when unnecessary
- Latency and cost accounting

</details>

**Important concepts**

- *Commands / APIs / Code:* cross-encoder reranking (concept), multi-query generation prompt
- *Mechanisms & failure scenarios:* Reranker latency breaking the budget, query rewrites drifting from user intent, over-expansion retrieving noise.

<a id="s08-module-3"></a>

## Module 3 — Generation, Context, and Advanced Patterns

**6 episodes (S08E09–S08E14) · 24 topics.** This module covers: Context Assembly and Grounded Generation with Citations; Context Engineering and Long-Context vs Retrieval; Structure-Aware and Corrective RAG; GraphRAG and Knowledge-Graph Retrieval; Structured and Text-to-SQL Retrieval; Multimodal and Domain-Specific RAG.

| ID | Episode | Depth |
|---|---|---|
| S08E09 | Context Assembly and Grounded Generation with Citations | Intermediate |
| S08E10 | Context Engineering and Long-Context vs Retrieval | Intermediate |
| S08E11 | Structure-Aware and Corrective RAG: Parent-Child, Multi-Vector, and Iterative Retrieval | Advanced |
| S08E12 | GraphRAG and Knowledge-Graph Retrieval | Advanced |
| S08E13 | Structured and Text-to-SQL Retrieval | Intermediate |
| S08E14 | Multimodal and Domain-Specific RAG: Images, Tables, and Code | Advanced |

### S08E09 — Context Assembly and Grounded Generation with Citations

**Depth:** Intermediate  
**Learning objective:** Turn retrieved chunks into a prompt that produces faithful, attributable answers.  
**Prerequisites:** S08E07, S07E03  
**Expected outcome:** Build a prompt and validation step that yields cited, grounded answers or an honest refusal.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Assembling Context**

- Selecting and ordering chunks within a token budget
- Deduplication and merging adjacent chunks
- Position effects on use of context

**Topic 2 — Grounded Prompting**

- Instructions to answer only from sources
- Abstaining when evidence is insufficient

**Topic 3 — Citations and Failure Handling**

- Citation formats
- Verifying that cited passages support claims
- Conflicting sources and out-of-scope questions
- Model ignoring context in favor of prior knowledge

</details>

**Important concepts**

- *Commands / APIs / Code:* context-builder with token budget, citation-checking step
- *Mechanisms & failure scenarios:* Fabricated or mismatched citations, model ignoring context in favor of prior knowledge, important evidence pushed out of the window.

### S08E10 — Context Engineering and Long-Context vs Retrieval

**Depth:** Intermediate  
**Learning objective:** Decide what information to give the model and in what form, including when to skip retrieval altogether.  
**Prerequisites:** S08E09, S06E15  
**Expected outcome:** Choose between long-context, retrieval and hybrid designs with a cost/quality argument.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Context as a Budget**

- Cost, latency and quality per token
- Dynamic context construction per query

**Topic 2 — Compression**

- Summarization and extractive compression
- What compression loses

**Topic 3 — Long Context vs RAG**

- When the whole corpus fits
- Attention degradation and cost
- Hybrid approaches with caching

**Topic 4 — Context Risks**

- Injection through retrieved content
- Context contamination and conflicting instructions
- Auditing exactly what was in context

</details>

**Important concepts**

- *Commands / APIs / Code:* context-size/cost calculator, compression prompt sketch
- *Mechanisms & failure scenarios:* Lost-in-the-middle failures, cost explosion from stuffing contexts, retrieved text overriding instructions.

### S08E11 — Structure-Aware and Corrective RAG: Parent-Child, Multi-Vector, and Iterative Retrieval

**Depth:** Advanced  
**Learning objective:** Recognize when basic RAG is insufficient and apply hierarchical, multi-representation and corrective retrieval patterns to specific failure modes.  
**Prerequisites:** S08E08, S08E09  
**Expected outcome:** Match advanced retrieval patterns to concrete failure modes and justify their complexity.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Hierarchical Retrieval**

- Parent-child chunks and small-to-big retrieval
- Window expansion around hits

**Topic 2 — Multiple Representations**

- Summaries, hypothetical questions and multi-vector indexing
- Late-interaction retrieval at concept level

**Topic 3 — Corrective and Adaptive Retrieval**

- Retrieval-quality grading and re-retrieval
- Query reformulation on failure

**Topic 4 — Multi-Hop and Iterative Retrieval**

- Decomposing questions and chaining retrieval steps
- Step limits and stopping conditions

**Topic 5 — When Added Complexity Is Not Worth It**

- Measuring gain vs latency and cost
- Simplifying back to basics

</details>

**Important concepts**

- *Commands / APIs / Code:* Parent-child index structure and window expansion (illustrative), retrieval-quality grader prompt, iterative retrieval loop with a step limit
- *Mechanisms & failure scenarios:* Multi-hop loops that never converge, graders rejecting good evidence, summaries replacing details that matter, higher latency for marginal gains.

### S08E12 — GraphRAG and Knowledge-Graph Retrieval

**Depth:** Advanced  
**Learning objective:** Understand when relationship-centric retrieval over a knowledge graph beats vector search, how such indexes are built, and what they cost.  
**Prerequisites:** S08E11, S08E07  
**Expected outcome:** Decide when a graph index is warranted and describe its construction, querying and maintenance.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Why Graphs**

- Questions about relationships and global themes
- Limits of chunk-level vector retrieval

**Topic 2 — Building the Graph**

- Entity and relation extraction with LLMs
- Entity resolution and schema design

**Topic 3 — Graph Indexing and Summaries**

- Community detection and hierarchical summaries
- Local vs global query modes

**Topic 4 — Querying**

- Neighborhood expansion and graph traversal
- Combining graph and vector retrieval

**Topic 5 — Cost, Quality, and Maintenance**

- Indexing cost and update strategies
- Evaluating extraction quality and answer benefit

</details>

**Important concepts**

- *Commands / APIs / Code:* Entity/relation extraction prompt with schema validation (illustrative), graph query for neighborhood expansion, community summary generation (concept)
- *Mechanisms & failure scenarios:* Extraction errors propagating into the graph, duplicate or unresolved entities, expensive global indexing for modest gains, stale graphs after document updates.

### S08E13 — Structured and Text-to-SQL Retrieval

**Depth:** Intermediate  
**Learning objective:** Answer questions over databases and tables safely and accurately.  
**Prerequisites:** S08E09, S01E10  
**Expected outcome:** Design a safe text-to-SQL component with validation and evaluation.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — When Documents Aren't Enough**

- Structured data and aggregates
- The text-to-SQL pipeline: schema linking, generation, execution

**Topic 2 — Context for SQL Generation**

- Schema documentation, semantic layers and curated views
- Example queries and column descriptions

**Topic 3 — Safety**

- Read-only access and query sandboxes
- Query validation and cost limits
- Row-level permissions

**Topic 4 — Quality**

- Ambiguity and error recovery
- Execution-based evaluation
- Combining SQL and document retrieval

</details>

**Important concepts**

- *Commands / APIs / Code:* schema-in-prompt template, SQL validation with a parser (concept), read-only DB role
- *Mechanisms & failure scenarios:* Plausible but wrong joins, unbounded scans, access to tables the user may not see.

### S08E14 — Multimodal and Domain-Specific RAG: Images, Tables, and Code

**Depth:** Advanced  
**Learning objective:** Extend RAG to non-text content and specialized corpora.  
**Prerequisites:** S08E03, S08E07  
**Expected outcome:** Adapt ingestion and retrieval to non-text and specialized domains.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Multimodal Retrieval**

- Image and chart indexing: captions vs multimodal embeddings
- Mixed-modality context

**Topic 2 — Tables and Structured Content**

- Table retrieval and serialization
- Numeric reasoning over retrieved tables

**Topic 3 — Code, Technical Corpora, and Domain Concerns**

- Code-aware chunking and symbol indexes
- Documentation versions and deprecated content
- Legal, medical and financial caution
- Terminology, abbreviations and citation requirements

</details>

**Important concepts**

- *Commands / APIs / Code:* multimodal embedding call (concept), code chunker by AST (concept)
- *Mechanisms & failure scenarios:* Chart values hallucinated from captions, outdated API docs retrieved, domain jargon missing from embeddings.

<a id="s08-module-4"></a>

## Module 4 — Evaluation, Production, and Security

**5 episodes (S08E15–S08E19) · 21 topics.** This module covers: RAG Evaluation; Debugging RAG Failures; Production RAG; RAG Security and Access Control; Enterprise RAG Reference Architecture.

| ID | Episode | Depth |
|---|---|---|
| S08E15 | RAG Evaluation: Retrieval Metrics, Faithfulness, and Answer Quality | Intermediate |
| S08E16 | Debugging RAG Failures: A Systematic Diagnosis Method | Advanced |
| S08E17 | Production RAG: Latency, Caching, Freshness, and Incremental Indexing | Advanced |
| S08E18 | RAG Security and Access Control | Advanced |
| S08E19 | Enterprise RAG Reference Architecture | Advanced |

### S08E15 — RAG Evaluation: Retrieval Metrics, Faithfulness, and Answer Quality

**Depth:** Intermediate  
**Learning objective:** Measure retrieval and generation separately so improvements are targeted and provable.  
**Prerequisites:** S08E09, S07E19, S04E11  
**Expected outcome:** Build a two-level RAG evaluation harness and use it to compare pipeline changes.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Retrieval Metrics**

- Recall@K, precision@K, MRR and NDCG
- Building labeled query-document sets

**Topic 2 — Synthetic Evaluation Data**

- Synthetic query generation and its biases
- Validating synthetic sets against real queries
- Coverage gaps in generated questions

**Topic 3 — Generation Metrics**

- Faithfulness/groundedness, answer relevance and completeness
- Citation accuracy

**Topic 4 — Judges**

- LLM judges and calibration against humans
- Judge prompts for faithfulness and relevance
- Calibration against human labels
- Judge cost and drift

**Topic 5 — Evaluation Practice**

- Component vs end-to-end evaluation
- Regression suites in CI
- Online feedback and error taxonomies

</details>

**Important concepts**

- *Commands / APIs / Code:* retrieval metric calculation, judge prompt for faithfulness, evaluation dataset JSONL
- *Mechanisms & failure scenarios:* Judge scoring fluent but unsupported answers highly, test queries unlike real traffic, optimizing retrieval metrics that do not move answer quality.

### S08E16 — Debugging RAG Failures: A Systematic Diagnosis Method

**Depth:** Advanced  
**Learning objective:** Locate the stage responsible for a bad answer and fix the root cause.  
**Prerequisites:** S08E15, S08E08  
**Expected outcome:** Diagnose a failing RAG answer to a specific pipeline stage and choose a targeted fix.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Failure Taxonomy**

- Not in corpus, not retrieved, ranked low, retrieved but ignored, generation error
- Ingestion/parsing errors; permission and freshness errors

**Topic 2 — Diagnostic Procedure**

- Inspect the query, retrieved chunks, scores and final prompt
- Replay with controlled variations

**Topic 3 — Tracing Every Stage**

- What to log per stage (link to S12E08)
- Replaying a request against stored retrieval state
- Linking traces to index and prompt versions

**Topic 4 — Fix Selection**

- Match fix to failure class
- Avoid prompt patches for retrieval problems
- Regression-protect each fix

</details>

**Important concepts**

- *Commands / APIs / Code:* retrieval-debug report script, trace inspection (concept)
- *Mechanisms & failure scenarios:* Fixing the prompt when the right chunk was never retrieved, chunking changes that fix one query and break ten.

### S08E17 — Production RAG: Latency, Caching, Freshness, and Incremental Indexing

**Depth:** Advanced  
**Learning objective:** Operate RAG at scale within latency, cost and freshness requirements.  
**Prerequisites:** S08E15, S08E06, S07E09  
**Expected outcome:** Design the operational plan for a RAG system including freshness and cost controls.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Latency and Cost**

- Per-stage latency budget
- Batch embedding and index build costs

**Topic 2 — Caching**

- Embeddings, retrieval results, prompts and answers
- Invalidation risks

**Topic 3 — Freshness**

- Incremental ingestion and change detection
- Deletions and document versioning
- Backfills and re-embedding migrations

**Topic 4 — Scaling and Reliability**

- Index sharding and replication
- Degraded modes when a component fails

**Topic 5 — Production Monitoring**

- Monitoring retrieval quality in production
- Alerting on freshness and failure rates

</details>

**Important concepts**

- *Commands / APIs / Code:* change-detection job sketch, cache key design, latency breakdown tracing
- *Mechanisms & failure scenarios:* Deleted documents still retrievable, stale caches serving old answers, reindexing causing downtime.

### S08E18 — RAG Security and Access Control

**Depth:** Advanced  
**Learning objective:** Prevent data leakage and manipulation through the retrieval layer.  
**Prerequisites:** S08E06, S07E04  
**Expected outcome:** Design permission-aware retrieval and describe its main residual risks.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Access Control**

- Document-level and row-level permissions
- Filtering at retrieval vs at generation
- Multi-tenant isolation

**Topic 2 — Attacks**

- Indirect prompt injection via documents
- Corpus poisoning and embedding attacks
- Data exfiltration through answers and citations

**Topic 3 — Controls**

- Permission-aware indexing and query-time identity
- Sanitization and content-trust levels

**Topic 4 — Auditing**

- Audit logging and monitoring
- Cached answers crossing permission boundaries

</details>

**Important concepts**

- *Commands / APIs / Code:* ACL metadata filters, retrieval with user-identity filter (concept)
- *Mechanisms & failure scenarios:* Cached answers crossing permission boundaries, poisoned documents steering outputs, ACL changes not propagating to the index.

### S08E19 — Enterprise RAG Reference Architecture

**Depth:** Advanced  
**Learning objective:** Assemble the season's concepts into a full architecture with ownership, evaluation and operations.  
**Prerequisites:** S08E17, S08E18, S08E15  
**Expected outcome:** Present a defensible enterprise RAG architecture with operations and governance.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Architecture**

- Sources, ingestion, index, retrieval, generation and gateway
- Identity and tenancy boundaries

**Topic 2 — Lifecycle**

- Content owners, quality gates and SLAs
- Versioning of chunking, embeddings and prompts

**Topic 3 — Evaluation, Operations, and Trade-offs**

- Build vs managed services
- Cost model and scaling
- Bridge to agents (Season 9) and LLMOps (Season 12)
- Evaluation in CI and in production
- Observability and feedback loops

</details>

**Important concepts**

- *Commands / APIs / Code:* reference diagram, runbook outline
- *Mechanisms & failure scenarios:* No owner for stale content, quality regressions after embedding upgrades, cost growth with corpus size.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s08-module-1) | Starting point of the season |
| [Module 2](#s08-module-2) | [Module 1](#s08-module-1) (S08E04) |
| [Module 3](#s08-module-3) | [Module 1](#s08-module-1) (S08E03); [Module 2](#s08-module-2) (S08E07, S08E08) |
| [Module 4](#s08-module-4) | [Module 2](#s08-module-2) (S08E06, S08E08); [Module 3](#s08-module-3) (S08E09) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** [Season 7 — Generative AI Application Engineering](../season-07-generative-ai-engineering/roadmap.md)
- **Next:** [Season 9 — AI Agents, Tool Calling & MCP](../season-09-ai-agents-and-mcp/roadmap.md)
- **Draws on:** [Season 1](../season-01-python-for-ai-ml/roadmap.md) (S01E10, S01E11); [Season 2](../season-02-mathematics-for-ai/roadmap.md) (S02E05); [Season 4](../season-04-advanced-ml-engineering/roadmap.md) (S04E11); [Season 5](../season-05-deep-learning/roadmap.md) (S05E13, S05E15, S05E25); [Season 6](../season-06-llms-and-transformers/roadmap.md) (S06E02, S06E07, S06E15); [Season 7](../season-07-generative-ai-engineering/roadmap.md) (S07E03, S07E04, S07E09, S07E13, S07E19)
- **Required by:** [Season 9](../season-09-ai-agents-and-mcp/roadmap.md) (via S08E06); [Season 10](../season-10-advanced-agentic-ai/roadmap.md) (via S08E11, S08E18); [Season 12](../season-12-llmops-engineering/roadmap.md) (via S08E15); [Season 13](../season-13-ai-infrastructure/roadmap.md) (via S08E19); [Season 14](../season-14-production-ai-systems/roadmap.md) (via S08E19); [Season 15](../season-15-ai-for-devops/roadmap.md) (via S08E04, S08E09, S08E13, S08E19)
