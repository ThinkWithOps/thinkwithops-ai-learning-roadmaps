"""S01E01 - How Python Executes Code: Interpreter, Bytecode, Objects, and Memory

Demonstrates, in runnable form:
  1. Source -> bytecode -> CPython VM (``dis``)
  2. Names as references, aliasing, copy vs deepcopy
  3. Reference counting and the cyclic garbage collector
  4. The mutable-default-argument trap
  5. Why Python lists of numbers are heavy
  6. The ``sys.modules`` import cache
  7. Why Python loops are slow compared with C-backed builtins

Run:  python s01e01_execution_and_memory.py
Only the standard library is needed.  Bytecode, sizes and timings differ
between Python versions and machines; see the expected output at the end.
"""
import copy
import dis
import gc
import sys
import timeit
import weakref
from array import array


def section(title: str) -> None:
    print(f"\n=== {title} ===")


def add_scaled(x, scale):
    return x * scale + 1


def show_bytecode() -> None:
    section("1. Bytecode: what one line costs")
    instructions = list(dis.get_instructions(add_scaled))
    print(f"add_scaled compiles to {len(instructions)} bytecode instructions:")
    for ins in instructions:
        print(f"  {ins.opname:<16} {ins.argrepr}")


def show_aliasing() -> None:
    section("2. Names are references: aliasing, copy, deepcopy")
    original = [[1, 2], [3, 4]]
    alias = original                   # same object, two names
    shallow = copy.copy(original)      # new outer list, SAME inner lists
    deep = copy.deepcopy(original)     # fully independent
    print("alias is original  :", alias is original)
    print("shallow is original:", shallow is original, "| inner shared:", shallow[0] is original[0])
    original[0].append(99)             # mutate through the original name
    print("alias   sees change:", alias[0])
    print("shallow sees change:", shallow[0], "<- shared inner list")
    print("deep    sees change:", deep[0], "<- independent")


class Node:
    def __init__(self):
        self.other = None


def show_refcount_and_gc() -> None:
    section("3. Reference counting and the cycle collector")
    a = Node()
    print("refcount of a (name + getrefcount argument):", sys.getrefcount(a))
    b = a  # noqa: F841 - adds a second reference on purpose
    print("after b = a:", sys.getrefcount(a))

    # Build a reference cycle; reference counting alone can never free it.
    gc.disable()
    x, y = Node(), Node()
    x.other, y.other = y, x
    probe = weakref.ref(x)             # weak references do not keep objects alive
    del x, y
    print("cycle still alive after del:", probe() is not None)
    gc.collect()
    print("cycle freed after gc.collect():", probe() is None)
    gc.enable()


def append_buggy(item, bucket=[]):     # noqa: B006 - the bug is the lesson
    bucket.append(item)
    return bucket


def append_safe(item, bucket=None):
    if bucket is None:                 # create a fresh list per call
        bucket = []
    bucket.append(item)
    return bucket


def show_mutable_default() -> None:
    section("4. Mutable default argument trap")
    append_buggy(1)
    print("buggy second call:", append_buggy(2), "<- remembers the first call")
    append_safe(1)
    print("safe  second call:", append_safe(2))


def show_memory_weight() -> None:
    section("5. Why lists of numbers are heavy")
    n = 100_000
    as_list = list(range(n))
    as_array = array("q", range(n))    # contiguous 8-byte integers
    list_bytes = sys.getsizeof(as_list) + sum(sys.getsizeof(v) for v in as_list)
    array_bytes = sys.getsizeof(as_array)
    print(f"list of {n:,} ints   : ~{list_bytes / 1e6:.1f} MB (pointers + int objects)")
    print(f"array('q') same data: ~{array_bytes / 1e6:.1f} MB")
    print(f"ratio               : ~{list_bytes / array_bytes:.1f}x")


def show_import_cache() -> None:
    section("6. import and the sys.modules cache")
    import json
    first = sys.modules["json"]
    import json as json_again          # second import is a dict lookup
    print("json in sys.modules :", "json" in sys.modules)
    print("same module object  :", json is json_again is first)
    print("sys.path entries    :", len(sys.path) > 0, "(first entry is the script's folder)")


def show_loop_overhead() -> None:
    section("7. Interpreter overhead: Python loop vs C-backed builtin")
    data = list(range(200_000))

    def python_loop():
        total = 0
        for value in data:
            total += value
        return total

    loop_time = timeit.timeit(python_loop, number=20)
    builtin_time = timeit.timeit(lambda: sum(data), number=20)
    assert python_loop() == sum(data)
    print(f"python loop: {loop_time:.3f}s   sum(): {builtin_time:.3f}s   (timings vary)")
    print("Takeaway: the same work is faster when the loop runs inside compiled code.")


if __name__ == "__main__":      # runs only when executed, not when imported
    show_bytecode()
    show_aliasing()
    show_refcount_and_gc()
    show_mutable_default()
    show_memory_weight()
    show_import_cache()
    show_loop_overhead()
