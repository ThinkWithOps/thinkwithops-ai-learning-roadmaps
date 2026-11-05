# Season 1 Roadmap — Python for AI & ML Engineering

[← Season 1 overview](README.md) · [All seasons](../README.md)

**3 modules · 18 episodes · 77 topics · 203 subtopics · Level: Foundational → Intermediate**

## Table of Contents

- [Season Purpose and Scope](#season-purpose-and-scope)
- [Learning Objectives](#learning-objectives)
- [Prerequisites and Expected Knowledge](#prerequisites-and-expected-knowledge)
- [Module Map](#module-map)
- [Module 1 — Python Foundations for ML Engineers](#s01-module-1)
- [Module 2 — Numerical and Data Computing](#s01-module-2)
- [Module 3 — Engineering Practice for AI Projects](#s01-module-3)
- [How the Modules Connect](#how-the-modules-connect)
- [How This Season Fits the 15-Season Curriculum](#how-this-season-fits-the-15-season-curriculum)

## Season Purpose and Scope

Give learners the Python, data-handling and engineering habits that every later season assumes: how Python really runs, how numerical and tabular data is represented in memory, and how to build reproducible, tested, servable code. Linux, Git and Docker appear here only as the minimum developer environment for AI work.

Terminology: **Season → Module → Episode → Topic → Subtopic**. Each episode is one video; its topics are the video chapters and its subtopics are the detailed points explained inside each chapter. Commands and code named in the curriculum are illustrative teaching material.

## Learning Objectives

What each episode sets out to teach, in curriculum order:

| Episode | Learning objective |
|---|---|
| S01E01 | Explain what happens between typing `python train.py` and a result, so that later performance, memory and reproducibility problems have a mental model. |
| S01E02 | Choose the right built-in structure and iteration style for data-processing code and write functions that are safe to reuse. |
| S01E03 | Model datasets, transformers and models as clean components, using the same interfaces ML libraries use. |
| S01E04 | Handle failure deliberately and diagnose problems with logs and a debugger rather than print statements. |
| S01E05 | Use types and runtime validation to catch bad data and bad configuration before they corrupt a model or a service. |
| S01E06 | Understand why NumPy is fast and how shapes, strides and broadcasting determine both correctness and performance. |
| S01E07 | Manipulate tabular data correctly and efficiently, and understand what Pandas does underneath. |
| S01E08 | Turn raw, inconsistent data into a trustworthy dataset, with checks that make cleaning auditable. |
| S01E09 | Use plots to find problems in data and models, not just to decorate reports. |
| S01E10 | Extract and shape training data from relational stores correctly and understand why a query is slow. |
| S01E11 | Pick storage and interchange formats deliberately and understand how a small data pipeline moves and transforms data. |
| S01E12 | Make a project install and run identically on another machine or in CI. |
| S01E13 | Use Git as a safety net and collaboration tool, including its limits for data and models. |
| S01E14 | Build a test suite that catches bugs in data transforms and model code without being flaky. |
| S01E15 | Find the real bottleneck first, then choose threads, processes or async appropriately. |
| S01E16 | Understand HTTP request handling and expose a Python function as a validated, documented service. |
| S01E17 | Gain just enough Linux, shell and container understanding to work on remote GPU machines and read AI project setup instructions. |
| S01E18 | Move exploratory work into a maintainable codebase that other tools and people can run. |

## Prerequisites and Expected Knowledge

No episodes from other seasons are required.

Episode-level prerequisites are listed with every episode below.

## Module Map

| Module | Title | Episodes | Count | Depth mix |
|---:|---|---|---:|---|
| 1 | [Python Foundations for ML Engineers](#s01-module-1) | S01E01–S01E05 | 5 | 4 Foundational, 1 Intermediate |
| 2 | [Numerical and Data Computing](#s01-module-2) | S01E06–S01E11 | 6 | 4 Foundational, 2 Intermediate |
| 3 | [Engineering Practice for AI Projects](#s01-module-3) | S01E12–S01E18 | 7 | 3 Foundational, 4 Intermediate |

<a id="s01-module-1"></a>

## Module 1 — Python Foundations for ML Engineers

**5 episodes (S01E01–S01E05) · 21 topics.** This module covers: How Python Executes Code; Data Structures, Iteration, and Functions for ML Code; Object-Oriented Python and Dataclasses for ML Components; Errors, Context Managers, Logging, and Debugging; Type Hints, Pydantic, and Data Validation.

| ID | Episode | Depth |
|---|---|---|
| S01E01 | How Python Executes Code: Interpreter, Bytecode, Objects, and Memory | Foundational |
| S01E02 | Data Structures, Iteration, and Functions for ML Code | Foundational |
| S01E03 | Object-Oriented Python and Dataclasses for ML Components | Foundational |
| S01E04 | Errors, Context Managers, Logging, and Debugging | Foundational |
| S01E05 | Type Hints, Pydantic, and Data Validation | Intermediate |

### S01E01 — How Python Executes Code: Interpreter, Bytecode, Objects, and Memory

**Depth:** Foundational  
**Learning objective:** Explain what happens between typing `python train.py` and a result, so that later performance, memory and reproducibility problems have a mental model.  
**Prerequisites:** None  
**Expected outcome:** Trace how a script runs, predict aliasing behavior, and explain why numerical Python delegates to compiled libraries.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — From Source to Execution**

- Source code, bytecode compilation, and the CPython virtual machine loop
- Reading bytecode with `dis` to see what one line costs
- REPL, script and notebook as three execution models
- Why `__name__ == "__main__"` exists

**Topic 2 — Objects, Names, and References**

- Everything is an object: identity, type, value
- Names as references; mutable vs immutable objects
- Aliasing, copy vs deepcopy, and how aliasing bugs corrupt datasets

**Topic 3 — Memory Management**

- Reference counting and the cyclic garbage collector
- Memory growth in long loops and typical leak patterns
- Small-object allocation and why Python lists of numbers are heavy

**Topic 4 — Modules and Imports**

- What `import` really does: finder, loader, `sys.modules` cache
- `sys.path`, packages, and circular-import failures

**Topic 5 — Why This Matters for AI Work**

- Why Python loops are slow and where speed comes from (C extensions)
- The global interpreter lock, previewed
- Where interpreter overhead disappears (NumPy, PyTorch) and where it dominates

</details>

**Important concepts**

- *Commands / APIs / Code:* `python -m dis`, `sys.getrefcount`, `id()`, `gc`, `python -X importtime`
- *Mechanisms & failure scenarios:* Mutable default arguments, accidental aliasing of a shared list, circular imports, memory not released because of lingering references.

### S01E02 — Data Structures, Iteration, and Functions for ML Code

**Depth:** Foundational  
**Learning objective:** Choose the right built-in structure and iteration style for data-processing code and write functions that are safe to reuse.  
**Prerequisites:** S01E01  
**Expected outcome:** Write memory-efficient data-batching code and justify structure choices by cost.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Core Containers and Their Costs**

- Lists, tuples, dicts, sets: internal layout and complexity
- Hashing; why dictionary keys must be hashable
- `collections` (`Counter`, `defaultdict`, `deque`) and when each pays off

**Topic 2 — Iteration and Laziness**

- Iterators, iterables and the iteration protocol
- Generators and lazy evaluation; streaming large files
- Comprehensions vs loops; `itertools` batching patterns

**Topic 3 — Functions as Building Blocks**

- Arguments, keyword-only parameters, `*args/**kwargs`
- Closures and decorators (timing, caching, retry)
- Pure functions and why they simplify testing

**Topic 4 — Complexity in Practice**

- Big-O as a tool for predicting data-pipeline cost
- Sorting, searching and membership tests on real sizes
- Measuring instead of guessing (`timeit`)

</details>

**Important concepts**

- *Commands / APIs / Code:* `timeit`, `functools.lru_cache`, generator expressions, `itertools.islice`
- *Mechanisms & failure scenarios:* Exhausted generators reused twice, quadratic list membership tests, hidden state in closures, decorators breaking function metadata.

### S01E03 — Object-Oriented Python and Dataclasses for ML Components

**Depth:** Foundational  
**Learning objective:** Model datasets, transformers and models as clean components, using the same interfaces ML libraries use.  
**Prerequisites:** S01E02  
**Expected outcome:** Design a small pipeline component that fits the scikit-learn and PyTorch conventions.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Classes and Protocols**

- Instances, methods, `__init__`, `__repr__`, special methods
- Duck typing and protocols (`__len__`, `__getitem__`, `__call__`)

**Topic 2 — Dataclasses and Configuration Objects**

- `@dataclass`, defaults, frozen instances
- Config objects instead of scattered constants
- Serialization to and from dict, JSON and YAML

**Topic 3 — The Interfaces ML Code Expects**

- The scikit-learn estimator contract (`fit`, `transform`, `predict`)
- PyTorch `Dataset` and `Module` as classes with required methods

**Topic 4 — Designing Components**

- Composition vs inheritance
- Abstract base classes for swappable components
- Class-level state and shared-mutable-attribute traps

</details>

**Important concepts**

- *Commands / APIs / Code:* `dataclasses`, `abc.ABC`, `__call__`, minimal custom transformer sketch
- *Mechanisms & failure scenarios:* Deep inheritance trees, mutable class attributes shared across instances, configs mutated in place between experiments.

### S01E04 — Errors, Context Managers, Logging, and Debugging

**Depth:** Foundational  
**Learning objective:** Handle failure deliberately and diagnose problems with logs and a debugger rather than print statements.  
**Prerequisites:** S01E01  
**Expected outcome:** Instrument a data job with structured logging and locate a fault from a traceback.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Exceptions as Control Flow**

- Exception hierarchy; `try/except/else/finally`
- Raising meaningful errors and custom exception types
- Failing fast vs recovering

**Topic 2 — Context Managers and Resources**

- `with`, `__enter__/__exit__`, `contextlib.contextmanager`
- Files, locks, timers and GPU-memory scopes as examples

**Topic 3 — Logging**

- Logger hierarchy, levels, handlers and formatters
- Structured logs and correlation fields
- Keeping secrets and personal data out of logs

**Topic 4 — Debugging**

- Reading a traceback from the bottom up
- `pdb` and IDE debuggers; breakpoints and post-mortem
- Reducing a failure to a minimal reproduction

</details>

**Important concepts**

- *Commands / APIs / Code:* `logging.basicConfig`, `python -m pdb`, `traceback`, `contextlib.contextmanager`
- *Mechanisms & failure scenarios:* Swallowed exceptions via bare `except`, resource leaks without context managers, log noise that hides signal, secrets in logs.

### S01E05 — Type Hints, Pydantic, and Data Validation

**Depth:** Intermediate  
**Learning objective:** Use types and runtime validation to catch bad data and bad configuration before they corrupt a model or a service.  
**Prerequisites:** S01E03  
**Expected outcome:** Define validated schemas for config and API payloads and explain what each layer guarantees.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Static Type Hints**

- Annotations, generics, `Optional`, `Literal`, `TypedDict`
- What type checkers (mypy/pyright) prove and what they do not

**Topic 2 — Runtime Validation with Pydantic**

- Models, field constraints, coercion vs strict mode
- Custom validators and types

**Topic 3 — Settings and Configuration**

- Settings objects from environment variables and files
- Secrets handling and environment-specific overrides

**Topic 4 — Validation at AI System Boundaries**

- Request/response schemas for APIs
- Config schemas for training runs
- Validating LLM structured output (preview of Season 7)
- Typing arrays and tensors at module boundaries

</details>

**Important concepts**

- *Commands / APIs / Code:* `typing`, `pydantic.BaseModel`, `model_validate`, `mypy`
- *Mechanisms & failure scenarios:* Silent type coercion changing values, annotations that lie at runtime, schema drift between producer and consumer.

<a id="s01-module-2"></a>

## Module 2 — Numerical and Data Computing

**6 episodes (S01E06–S01E11) · 26 topics.** This module covers: NumPy Arrays; Pandas Internals; Cleaning and Validating Messy Data; Data Visualization for Diagnosis; SQL for ML Engineers; Data Formats and Pipelines.

| ID | Episode | Depth |
|---|---|---|
| S01E06 | NumPy Arrays: Memory Layout, Vectorization, and Broadcasting | Foundational |
| S01E07 | Pandas Internals: DataFrames, Indexing, Joins, and GroupBy | Foundational |
| S01E08 | Cleaning and Validating Messy Data | Foundational |
| S01E09 | Data Visualization for Diagnosis | Foundational |
| S01E10 | SQL for ML Engineers: Joins, Window Functions, and Query Plans | Intermediate |
| S01E11 | Data Formats and Pipelines: CSV, JSON, Parquet, and Arrow | Intermediate |

### S01E06 — NumPy Arrays: Memory Layout, Vectorization, and Broadcasting

**Depth:** Foundational  
**Learning objective:** Understand why NumPy is fast and how shapes, strides and broadcasting determine both correctness and performance.  
**Prerequisites:** S01E01  
**Expected outcome:** Predict output shapes, avoid unnecessary copies, and replace a Python loop with a vectorized expression.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The ndarray**

- Contiguous memory, dtype, shape and strides
- C-order vs Fortran-order and cache behavior

**Topic 2 — Views, Copies, and Indexing**

- Basic slicing returns views; fancy indexing returns copies
- Boolean masks and `np.where`
- Accidental copies doubling memory

**Topic 3 — Vectorization**

- Why vector operations replace loops
- Universal functions, reductions along axes, `keepdims`
- Integer overflow and dtype promotion rules

**Topic 4 — Broadcasting**

- The broadcasting rules step by step
- Reading shape errors
- Intermediate-array memory blow-ups

**Topic 5 — Numerical Building Blocks**

- Linear algebra routines (`@`, `solve`, `svd`) and BLAS
- Random generators and reproducibility
- `einsum` as a shape-explicit tool

</details>

**Important concepts**

- *Commands / APIs / Code:* `np.array`, `.reshape`, `.strides`, `np.einsum` (intro), `%timeit`
- *Mechanisms & failure scenarios:* Accidental copies doubling memory, integer overflow in small dtypes, silent broadcasting that produces a wrong-shaped result.

### S01E07 — Pandas Internals: DataFrames, Indexing, Joins, and GroupBy

**Depth:** Foundational  
**Learning objective:** Manipulate tabular data correctly and efficiently, and understand what Pandas does underneath.  
**Prerequisites:** S01E06  
**Expected outcome:** Build correct joins and aggregations and diagnose row-count and memory surprises.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — The DataFrame Model**

- Columns as typed arrays, index, block storage
- Series, dtypes and nullable types

**Topic 2 — Selecting and Transforming**

- `loc` vs `iloc`, boolean masks, `assign`, method chaining
- Copy-on-write and chained-assignment pitfalls

**Topic 3 — Combining Tables**

- Merge/join types and key cardinality
- Concatenation and alignment
- Detecting row-count surprises after a join

**Topic 4 — Aggregation and Time**

- GroupBy: split-apply-combine
- Pivot, melt and window functions
- Resampling time series

**Topic 5 — Scale Limits**

- Memory footprint and dtype downcasting; categorical dtype
- Chunked processing
- When to leave Pandas (columnar engines, SQL)

</details>

**Important concepts**

- *Commands / APIs / Code:* `pd.merge`, `df.groupby().agg`, `df.memory_usage(deep=True)`, `astype('category')`
- *Mechanisms & failure scenarios:* Many-to-many join exploding row counts, SettingWithCopy surprises, silent NaN introduction on merge, out-of-memory on wide frames.

### S01E08 — Cleaning and Validating Messy Data

**Depth:** Foundational  
**Learning objective:** Turn raw, inconsistent data into a trustworthy dataset, with checks that make cleaning auditable.  
**Prerequisites:** S01E07  
**Expected outcome:** Produce a documented cleaning step with explicit validation and explain the risks of each choice.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Typical Data Defects**

- Missing values and their meanings (absent vs unknown vs zero)
- Duplicates, inconsistent categories, wrong types
- Outliers vs errors

**Topic 2 — Handling Missing and Bad Values**

- Deletion vs imputation and what each does to the distribution
- Missing-indicator features
- Winsorizing, clipping and flagging

**Topic 3 — Normalizing Messy Fields**

- Parsing dates, units and encodings
- Text normalization and category consolidation

**Topic 4 — Validation and Auditability**

- Schema, range and uniqueness assertions
- Before/after distribution checks
- Why cleaning must be fit on training data only (preview of leakage)

</details>

**Important concepts**

- *Commands / APIs / Code:* `df.isna()`, `df.duplicated()`, `pd.to_datetime(errors=...)`, assertion-style validation
- *Mechanisms & failure scenarios:* Imputing with global statistics (leakage), dropping rows that bias the sample, cleaning scripts that are not repeatable.

### S01E09 — Data Visualization for Diagnosis

**Depth:** Foundational  
**Learning objective:** Use plots to find problems in data and models, not just to decorate reports.  
**Prerequisites:** S01E07  
**Expected outcome:** Select plots that expose data quality and model behavior issues.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — Choosing the Right Plot**

- Distributions: histograms, KDE, box plots
- Relationships: scatter, heatmaps, pair plots
- Time series and categorical comparisons

**Topic 2 — Matplotlib Mechanics**

- Figure/axes model and the object-oriented API
- Scales, annotations, small multiples
- Saving reproducible figures

**Topic 3 — Plots that Reveal Problems**

- Class imbalance, skew, outliers and leakage signals
- Learning curves and residual plots (preview of Season 3)
- Misleading charts and how to avoid them

</details>

**Important concepts**

- *Commands / APIs / Code:* `plt.subplots`, `sns.histplot`, `df.plot`
- *Mechanisms & failure scenarios:* Overplotting hiding structure, truncated axes exaggerating effects, aggregated plots hiding subgroup failures.

### S01E10 — SQL for ML Engineers: Joins, Window Functions, and Query Plans

**Depth:** Intermediate  
**Learning objective:** Extract and shape training data from relational stores correctly and understand why a query is slow.  
**Prerequisites:** S01E07  
**Expected outcome:** Write leakage-safe training-set queries and read a basic query plan.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Relational Thinking**

- Tables, keys, normalization vs denormalized analytics tables
- Cardinality and why it controls join behavior

**Topic 2 — Querying**

- Joins (inner, left, anti, semi)
- Aggregation, `GROUP BY`, `HAVING`, subqueries and CTEs

**Topic 3 — Window Functions**

- Ranking, running totals, `LAG/LEAD`
- Partitioning and frame definitions

**Topic 4 — Leakage-Safe Training Sets**

- Point-in-time correct feature queries
- Avoiding future data in time-based joins
- Label definition windows

**Topic 5 — How a Query Executes**

- Indexes and scans
- Reading an `EXPLAIN` plan
- Pushing work to the database vs Pandas

</details>

**Important concepts**

- *Commands / APIs / Code:* `SELECT … OVER (PARTITION BY …)`, `EXPLAIN ANALYZE`, `pandas.read_sql`, SQLite/PostgreSQL
- *Mechanisms & failure scenarios:* Join fan-out inflating labels, future data leaking into features, full-table scans in nightly jobs.

### S01E11 — Data Formats and Pipelines: CSV, JSON, Parquet, and Arrow

**Depth:** Intermediate  
**Learning objective:** Pick storage and interchange formats deliberately and understand how a small data pipeline moves and transforms data.  
**Prerequisites:** S01E07, S01E08  
**Expected outcome:** Choose a format for a workload and design a re-runnable data-prep step.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Row vs Columnar Formats**

- CSV/JSON limits: types, size, parsing cost
- Parquet: columns, row groups, compression, predicate pushdown
- Arrow as the in-memory columnar standard

**Topic 2 — Serialization and Schemas**

- JSON/YAML configs; Avro/Protobuf at overview level
- Schema evolution and compatibility
- Python pickle risks

**Topic 3 — A Small Data Pipeline**

- Extract, transform, load stages
- Idempotent, re-runnable steps

**Topic 4 — Partitioning and Incremental Processing**

- Partitioning schemes and small-file problems
- Incremental loads and watermarks
- Choosing a format for a workload

</details>

**Important concepts**

- *Commands / APIs / Code:* `df.to_parquet`, `pyarrow`, `pd.read_csv(chunksize=…)`, `json.loads`
- *Mechanisms & failure scenarios:* Type inference differences between reads, schema drift breaking downstream jobs, unsafe pickle loading, non-idempotent loads creating duplicates.

<a id="s01-module-3"></a>

## Module 3 — Engineering Practice for AI Projects

**7 episodes (S01E12–S01E18) · 30 topics.** This module covers: Environments, Dependencies, and Reproducible Python Projects; Git and Collaboration for ML Projects; Testing Python ML Code; Performance; Building APIs with FastAPI; Linux Shell, Containers, and the Developer Environment for AI Work; From Jupyter to Production.

| ID | Episode | Depth |
|---|---|---|
| S01E12 | Environments, Dependencies, and Reproducible Python Projects | Foundational |
| S01E13 | Git and Collaboration for ML Projects | Foundational |
| S01E14 | Testing Python ML Code: pytest, Fixtures, and Data Tests | Intermediate |
| S01E15 | Performance: Profiling, Concurrency, Async, and the GIL | Intermediate |
| S01E16 | Building APIs with FastAPI: Serving a Model Endpoint | Intermediate |
| S01E17 | Linux Shell, Containers, and the Developer Environment for AI Work | Foundational |
| S01E18 | From Jupyter to Production: Notebooks, Scripts, Packages, and Project Structure | Intermediate |

### S01E12 — Environments, Dependencies, and Reproducible Python Projects

**Depth:** Foundational  
**Learning objective:** Make a project install and run identically on another machine or in CI.  
**Prerequisites:** S01E01  
**Expected outcome:** Create a locked, reproducible project environment and explain its remaining sources of nondeterminism.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Isolating Environments**

- Why global installs break
- Virtual environments and interpreter versions
- Package indexes and wheels

**Topic 2 — Declaring and Locking Dependencies**

- Direct vs transitive dependencies
- Lock files and hashes
- Resolver conflicts and how to read them

**Topic 3 — ML-Specific Dependency Problems**

- CUDA-linked wheels and driver compatibility
- Pinning strategy for fast-moving ML libraries

**Topic 4 — Reproducibility Beyond Packages**

- Random seeds and nondeterminism sources
- Recording environment metadata with each run
- Handoff to containers (Season 11)

</details>

**Important concepts**

- *Commands / APIs / Code:* `python -m venv`, `pip install`/`pip freeze`, `uv`/`pip-tools` lock concept, `pyproject.toml`
- *Mechanisms & failure scenarios:* Dependency resolution conflicts, "works on my machine" from unpinned transitive packages, GPU-wheel/driver mismatch.

### S01E13 — Git and Collaboration for ML Projects

**Depth:** Foundational  
**Learning objective:** Use Git as a safety net and collaboration tool, including its limits for data and models.  
**Prerequisites:** None  
**Expected outcome:** Work safely in a shared repository and explain how large data and model files should be tracked.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Git Mental Model**

- Commits, trees, blobs and the object store
- Staging area, history, diff

**Topic 2 — Branching and Integration**

- Branches as pointers; merge vs rebase
- Conflict resolution

**Topic 3 — Collaboration Workflow**

- Pull requests and code review
- `.gitignore`, secrets in history
- Tags and release versions

**Topic 4 — Recovering from Mistakes**

- `reflog`, `restore`, `revert` vs `reset`
- Safe vs destructive history rewrites

**Topic 5 — Git for ML Artifacts**

- Why large files and notebooks fit poorly
- Pointer-based data/model versioning (DVC concept, previewed for Season 11)
- Notebook diffs and `nbstripout`

</details>

**Important concepts**

- *Commands / APIs / Code:* `git log --graph`, `git rebase`, `git reflog`, `git restore`
- *Mechanisms & failure scenarios:* Committed credentials, repository bloat from datasets, destructive history rewrites on shared branches.

### S01E14 — Testing Python ML Code: pytest, Fixtures, and Data Tests

**Depth:** Intermediate  
**Learning objective:** Build a test suite that catches bugs in data transforms and model code without being flaky.  
**Prerequisites:** S01E04  
**Expected outcome:** Write meaningful tests for a transformation and a training smoke test.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — Unit Testing Foundations**

- pytest structure, assertions, parametrization
- Fixtures and test data

**Topic 2 — Isolating Dependencies**

- Mocking external services and file systems
- Test doubles vs real dependencies

**Topic 3 — Testing Numerical and ML Code**

- Floating-point tolerances (`pytest.approx`)
- Shape, dtype and invariance tests
- Deterministic seeds; property-based testing idea

**Topic 4 — Testing Data and Pipelines**

- Data-quality assertions as tests
- Smoke tests: can the model overfit a tiny batch?

**Topic 5 — Test Strategy**

- Test pyramid for ML projects
- Speed, flakiness and CI hooks

</details>

**Important concepts**

- *Commands / APIs / Code:* `pytest -k`, `@pytest.mark.parametrize`, `pytest.approx`, `unittest.mock`
- *Mechanisms & failure scenarios:* Flaky tests from unseeded randomness, tests that pass because mocks hide the real failure, slow suites nobody runs.

### S01E15 — Performance: Profiling, Concurrency, Async, and the GIL

**Depth:** Intermediate  
**Learning objective:** Find the real bottleneck first, then choose threads, processes or async appropriately.  
**Prerequisites:** S01E02  
**Expected outcome:** Profile a slow pipeline and select an appropriate concurrency model with reasons.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — Measuring Before Optimizing**

- Wall time vs CPU time
- Profilers (`cProfile`, line profilers) and memory profilers
- Reading a flame graph

**Topic 2 — The GIL and Concurrency Models**

- What the GIL blocks and what it does not
- Threads vs processes vs `asyncio`
- I/O-bound vs CPU-bound work

**Topic 3 — Parallel Data Processing**

- Process pools, shared memory and serialization cost
- Parallel data loading and batch processing

**Topic 4 — Async and Rate Limits**

- Async calls to external APIs (preview of LLM APIs)
- Semaphores, backpressure and rate limits

</details>

**Important concepts**

- *Commands / APIs / Code:* `cProfile`, `multiprocessing`, `concurrent.futures`, `asyncio.gather`
- *Mechanisms & failure scenarios:* Threads giving no speedup on CPU-bound code, process pools copying large arrays, unbounded concurrency overwhelming an API.

### S01E16 — Building APIs with FastAPI: Serving a Model Endpoint

**Depth:** Intermediate  
**Learning objective:** Understand HTTP request handling and expose a Python function as a validated, documented service.  
**Prerequisites:** S01E05, S01E15  
**Expected outcome:** Explain and sketch a validated prediction endpoint with sensible failure behavior.

<details>
<summary>Topics and subtopics (5 topics)</summary>

**Topic 1 — HTTP for Engineers**

- Request/response cycle, methods, status codes, headers
- JSON payloads
- Authentication at overview level

**Topic 2 — FastAPI Mechanics**

- Routing, path/query parameters, dependency injection
- Sync vs async handlers

**Topic 3 — Validation and Documentation**

- Pydantic request/response models
- Automatic OpenAPI documentation and error responses

**Topic 4 — Serving a Model Responsibly**

- Loading the model once at startup (lifespan)
- Health checks, timeouts and input limits
- Latency and the cost of per-request work

**Topic 5 — Testing and Running the Service**

- `TestClient` and contract tests
- ASGI servers, workers and concurrency settings

</details>

**Important concepts**

- *Commands / APIs / Code:* `uvicorn app:app`, `@app.post`, `curl -X POST`, `TestClient`
- *Mechanisms & failure scenarios:* Model reloaded on every request, blocking calls inside async handlers, unvalidated input crashing inference.

### S01E17 — Linux Shell, Containers, and the Developer Environment for AI Work

**Depth:** Foundational  
**Learning objective:** Gain just enough Linux, shell and container understanding to work on remote GPU machines and read AI project setup instructions.  
**Prerequisites:** S01E12  
**Expected outcome:** Navigate a remote Linux box, inspect resources and run a containerized project.

<details>
<summary>Topics and subtopics (4 topics)</summary>

**Topic 1 — The Shell You Will Use**

- Filesystem layout, permissions, processes
- Pipes, redirection, environment variables

**Topic 2 — Remote Machines**

- SSH keys, config and tunnels
- Moving data (`scp`, `rsync`) and long-running sessions (`tmux`)

**Topic 3 — Inspecting a Machine**

- CPU, memory, disk and process inspection
- GPU visibility from the shell (preview of Season 13)
- Reading logs and tailing output

**Topic 4 — Containers in One Episode**

- What a container is and is not
- Images, layers, running a container, mounting data
- Why AI projects ship as images (preview of Season 11)

</details>

**Important concepts**

- *Commands / APIs / Code:* `ls -l`, `grep`, `top`/`htop`, `df -h`, `ssh`, `docker run`, `nvidia-smi` (where available)
- *Mechanisms & failure scenarios:* Permission denied on mounted volumes, out-of-disk during training, processes killed by the OOM killer, container with no GPU access.

### S01E18 — From Jupyter to Production: Notebooks, Scripts, Packages, and Project Structure

**Depth:** Intermediate  
**Learning objective:** Move exploratory work into a maintainable codebase that other tools and people can run.  
**Prerequisites:** S01E12, S01E14  
**Expected outcome:** Refactor a notebook into a tested, configurable package structure.

<details>
<summary>Topics and subtopics (3 topics)</summary>

**Topic 1 — What Notebooks Are Good and Bad At**

- Hidden state and execution-order bugs
- Reproducibility and review problems
- Where notebooks belong in the workflow

**Topic 2 — Structuring a Project**

- Source package, tests, configs, scripts
- Separating data, features, training and serving code
- Entry points and command-line interfaces

**Topic 3 — Making Work Repeatable**

- Config-driven runs and run directories
- Logging results and artifacts per run
- Connecting to Season 3 (ML workflow) and Season 11 (pipelines)

</details>

**Important concepts**

- *Commands / APIs / Code:* `jupyter nbconvert`, `python -m package`, `argparse`/`typer`, `pyproject.toml` entry points
- *Mechanisms & failure scenarios:* Out-of-order cell execution producing irreproducible results, notebooks importing each other, configuration scattered across cells.

## How the Modules Connect

Derived from the episode prerequisites: a module depends on another when one of its episodes lists an episode of that module as a prerequisite.

| Module | Builds on (within this season) |
|---|---|
| [Module 1](#s01-module-1) | Starting point of the season |
| [Module 2](#s01-module-2) | [Module 1](#s01-module-1) (S01E01) |
| [Module 3](#s01-module-3) | [Module 1](#s01-module-1) (S01E01, S01E02, S01E04, S01E05) |

## How This Season Fits the 15-Season Curriculum

- **Previous:** none — this is the first season.
- **Next:** [Season 2 — Mathematics for AI & Machine Learning](../season-02-mathematics-for-ai/roadmap.md)
- **Required by:** [Season 2](../season-02-mathematics-for-ai/roadmap.md) (via S01E06); [Season 3](../season-03-machine-learning/roadmap.md) (via S01E03, S01E08); [Season 4](../season-04-advanced-ml-engineering/roadmap.md) (via S01E10); [Season 5](../season-05-deep-learning/roadmap.md) (via S01E03, S01E11); [Season 7](../season-07-generative-ai-engineering/roadmap.md) (via S01E05, S01E15, S01E16); [Season 8](../season-08-rag-engineering/roadmap.md) (via S01E10, S01E11); [Season 9](../season-09-ai-agents-and-mcp/roadmap.md) (via S01E13, S01E14); [Season 11](../season-11-mlops-engineering/roadmap.md) (via S01E08, S01E10, S01E11, S01E12, S01E13, S01E14, S01E16, S01E17)
