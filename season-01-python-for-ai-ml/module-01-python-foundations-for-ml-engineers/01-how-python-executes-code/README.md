# S01E01 — How Python Executes Code: Interpreter, Bytecode, Objects, and Memory

[← Module](../README.md) · [Season roadmap](../../roadmap.md#s01-module-1)

**Season 1:** Python for AI & ML Engineering
**Module 1:** Python Foundations for ML Engineers
**Depth:** Foundational
**Learning objective:** Explain what happens between typing `python train.py` and a result, so that later performance, memory and reproducibility problems have a mental model.

## What this example shows

One runnable script that walks through seven small experiments: reading the bytecode of a function, aliasing versus copying, reference counting and the cycle collector, the mutable-default-argument trap, how heavy a list of numbers is, the `sys.modules` import cache, and why a Python loop is slower than a C-backed builtin.

## Curriculum topics and the code that covers them

| Topic | What the code demonstrates | Where |
|---|---|---|
| 1. From Source to Execution | Bytecode of a one-line function via `dis`; the `if __name__ == "__main__"` guard that runs the demo | section 1 |
| 2. Objects, Names, and References | Aliasing, `copy` vs `deepcopy`, and the mutable default argument bug | sections 2 and 4 |
| 3. Memory Management | `sys.getrefcount`, a reference cycle freed by `gc.collect()`, list-of-ints vs `array` memory | sections 3 and 5 |
| 4. Modules and Imports | The `sys.modules` cache and `sys.path` | section 6 |
| 5. Why This Matters for AI Work | Python loop vs `sum()` timing: interpreter overhead disappears inside compiled code | section 7 |

Not demonstrated in code: the GIL (previewed only) and `python -X importtime`.

## Narration alignment

This code was written before the episode narration existed. It is mapped here to the approved narration (chapters and beats) of this episode. The demo script is organized in numbered sections, referred to below as "section N". Rows marked "partly" are only partly demonstrated by the code; rows marked "conceptual only" have no practical demonstration.

| Chapter | Beats | Curriculum topic | Practical files / sections |
|---|---|---|---|
| 1. From Source to Execution | 1.1 | From Source to Execution | conceptual only (the opening scenario, a function whose second call remembers the first, is not run here; the mechanism behind it is demonstrated in section 4, see beat 2.5) |
| 1. From Source to Execution | 1.2 | From Source to Execution | conceptual only (the CPython scope note and the train.py example are not run as code) |
| 1. From Source to Execution | 1.3-1.4 | From Source to Execution | `s01e01_execution_and_memory.py` (section 1, partly: the bytecode listing shows what compilation produces; the pyc cache and the virtual machine loop are not demonstrated) |
| 1. From Source to Execution | 1.5 | From Source to Execution | `s01e01_execution_and_memory.py` (section 1: bytecode of a one-line function listed with the dis module) |
| 1. From Source to Execution | 1.6 | From Source to Execution | conceptual only (REPL, script and notebook are not demonstrated in code) |
| 1. From Source to Execution | 1.7 | From Source to Execution | `s01e01_execution_and_memory.py` (partly: the main guard at the bottom of the file runs the demo; the effect of importing the file is not demonstrated; 1.7 also leads into chapter 2) |
| 2. Objects, Names, and References | 2.1-2.2 | Objects, Names, and References | `s01e01_execution_and_memory.py` (section 2, partly: object identity with the is operator and a change made through a shared name; id() and rebinding an immutable value are not demonstrated) |
| 2. Objects, Names, and References | 2.3 | Objects, Names, and References | `s01e01_execution_and_memory.py` (section 2: alias and original are the same list and a change shows through both names; the narration's raw and clean example uses the same pattern with different names) |
| 2. Objects, Names, and References | 2.4 | Objects, Names, and References | `s01e01_execution_and_memory.py` (section 2: shallow copy and deep copy of nested lists), `exercises/s01e01_exercise.py` and `solutions/s01e01_solution.py` (the deepcopy snapshot task) |
| 2. Objects, Names, and References | 2.5 | Objects, Names, and References | `s01e01_execution_and_memory.py` (section 4: mutable default argument and the None-default fix), `exercises/s01e01_exercise.py` and `solutions/s01e01_solution.py` (the add_tag task) |
| 2. Objects, Names, and References | 2.6 | Objects, Names, and References | conceptual only (2.6 is a transition into memory management) |
| 3. Memory Management | 3.1 | Memory Management | `s01e01_execution_and_memory.py` (section 3: reference count and sys.getrefcount) |
| 3. Memory Management | 3.2 | Memory Management | `s01e01_execution_and_memory.py` (section 3: a reference cycle, a weak reference and gc.collect) |
| 3. Memory Management | 3.3 | Memory Management | conceptual only (memory growth and lingering references are not demonstrated in code) |
| 3. Memory Management | 3.4 | Memory Management | `s01e01_execution_and_memory.py` (section 5, partly: the size of integer objects inside a list; the small-object allocator is not demonstrated) |
| 3. Memory Management | 3.5 | Memory Management | `s01e01_execution_and_memory.py` (section 5: list of integers vs a compact array; 3.5 also leads into chapter 4) |
| 4. Modules and Imports | 4.1 | Modules and Imports | `s01e01_execution_and_memory.py` (section 6, partly: the sys.modules cache; finders, the loader and -X importtime are not demonstrated) |
| 4. Modules and Imports | 4.2 | Modules and Imports | `s01e01_execution_and_memory.py` (section 6, partly: sys.path is inspected; search order and shadowing are not demonstrated) |
| 4. Modules and Imports | 4.3-4.4 | Modules and Imports | conceptual only (circular imports are not demonstrated in code; 4.4 is a transition) |
| 5. Why This Matters for AI Work | 5.1 | Why This Matters for AI Work | `s01e01_execution_and_memory.py` (section 7: Python loop vs the sum builtin) |
| 5. Why This Matters for AI Work | 5.2 | Why This Matters for AI Work | conceptual only (NumPy and PyTorch are not used in the code) |
| 5. Why This Matters for AI Work | 5.3 | Why This Matters for AI Work | conceptual only (many tiny calls versus one large call are not demonstrated; section 7 shows only the Python loop and the builtin) |
| 5. Why This Matters for AI Work | 5.4 | Why This Matters for AI Work | conceptual only (the global interpreter lock is previewed in the narration, not in code) |
| 5. Why This Matters for AI Work | 5.5 | Why This Matters for AI Work | conceptual only (closing summary) |

<!-- practical:narration {"beats":{"1.1":"c7b0078f14b3","1.2":"3d650de94179","1.3":"3f6dd7732ccc","1.4":"b001590606eb","1.5":"962266021677","1.6":"478878cfcbe3","1.7":"7e1acedf53d6","2.1":"c125b4f3d952","2.2":"c03046e9659e","2.3":"a4e1f4a76322","2.4":"b7e0867a9c4f","2.5":"cea6c3133ba7","2.6":"ef56cf15917a","3.1":"a8d52f1994b0","3.2":"b6d0a0a2cba6","3.3":"2522db213459","3.4":"db89fa516c71","3.5":"ad8ef4562974","4.1":"596845489dbc","4.2":"2464b9263356","4.3":"b8f11bb426a4","4.4":"60368ad7ccf9","5.1":"f631d75f4ed8","5.2":"6d98cda33854","5.3":"ec04fada4c54","5.4":"cbbf1a54d727","5.5":"f85fc921c48d"},"episode":"S01E01","narration_sha256":"f5839f316e83ebf0cd031291cc4b199aedaeb542a5753311c9006c52e4fa6b5a"} -->

## Files

<!-- practical:files:start -->
| File | Type | How to run |
|---|---|---|
| [exercises/s01e01_exercise.py](exercises/s01e01_exercise.py) | Python | `python exercises/s01e01_exercise.py` |
| [s01e01_execution_and_memory.py](s01e01_execution_and_memory.py) | Python | `python s01e01_execution_and_memory.py` |
| [solutions/s01e01_solution.py](solutions/s01e01_solution.py) | Python | `python solutions/s01e01_solution.py` |
<!-- practical:files:end -->

The `exercises/` and `solutions/` folders hold an optional practice task on aliasing and mutable defaults. Try the exercise first, then compare with the solution.

## Prerequisites and setup

None (curriculum prerequisites: none). Python 3.8+; standard library only.

## How to run

```bash
python s01e01_execution_and_memory.py       # the demonstration
python exercises/s01e01_exercise.py         # prints "Not solved yet" until you implement it
python solutions/s01e01_solution.py         # prints "All checks passed"
```

Bytecode instruction names, memory sizes and timings differ between Python versions and machines. The aliasing, refcount, garbage-collection and default-argument lines are deterministic.

## Expected outcome

Trace how a script runs, predict aliasing behavior, and explain why numerical Python delegates to compiled libraries.
