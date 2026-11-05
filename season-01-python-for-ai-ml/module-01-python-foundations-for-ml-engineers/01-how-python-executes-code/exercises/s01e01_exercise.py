"""S01E01 exercise - References, aliasing and mutable defaults

PROBLEM
  A teammate's data-prep code corrupts datasets through aliasing.  Fix it.

  1. ``add_tag(tag, tags=None)``
     Return a list containing ``tag`` appended to ``tags``.
     - It must NOT modify the list passed in.
     - Calling ``add_tag("a")`` twice must give ``["a"]`` both times
       (no state may survive between calls).

  2. ``snapshot(config)``
     ``config`` is a nested dict such as ``{"model": {"layers": [4, 2]}}``.
     Return an independent copy: changing the copy (even nested values) must
     never change the original.

EXAMPLES
  add_tag("b", ["a"])  -> ["a", "b"]   (input list stays ["a"])
  add_tag("x")         -> ["x"]
  copy = snapshot(cfg); copy["model"]["layers"].append(9)  # cfg is unchanged

RUN     python s01e01_exercise.py
SOLVED  when it prints "All checks passed".
Compare with ../solutions/s01e01_solution.py only after you have tried.
"""


def add_tag(tag, tags=None):
    # TODO: implement
    raise NotImplementedError


def snapshot(config):
    # TODO: implement
    raise NotImplementedError


def check():
    original = ["a"]
    assert add_tag("b", original) == ["a", "b"], "wrong result"
    assert original == ["a"], "input list was modified"
    assert add_tag("x") == ["x"]
    assert add_tag("x") == ["x"], "state leaked between calls"

    cfg = {"model": {"layers": [4, 2]}}
    copy = snapshot(cfg)
    copy["model"]["layers"].append(9)
    assert cfg == {"model": {"layers": [4, 2]}}, "nested data was shared"
    assert copy == {"model": {"layers": [4, 2, 9]}}


if __name__ == "__main__":
    try:
        check()
        print("All checks passed")
    except NotImplementedError:
        print("Not solved yet: replace the TODO bodies with your code.")
    except AssertionError as err:
        print("Check failed:", err)
        raise SystemExit(1)
