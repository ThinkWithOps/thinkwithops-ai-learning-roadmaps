"""S01E01 solution - References, aliasing and mutable defaults

Try the exercise first: ../exercises/s01e01_exercise.py
"""
import copy


def add_tag(tag, tags=None):
    # ``None`` as the default means a fresh list is built on every call,
    # so no state survives between calls.
    new_tags = [] if tags is None else list(tags)   # list(...) copies: input stays untouched
    new_tags.append(tag)
    return new_tags


def snapshot(config):
    # deepcopy duplicates nested containers too; copy.copy would share the inner lists.
    return copy.deepcopy(config)


def check():
    original = ["a"]
    assert add_tag("b", original) == ["a", "b"], "wrong result"
    assert original == ["a"], "input list was modified"
    assert add_tag("x") == ["x"]
    assert add_tag("x") == ["x"], "state leaked between calls"

    cfg = {"model": {"layers": [4, 2]}}
    duplicate = snapshot(cfg)
    duplicate["model"]["layers"].append(9)
    assert cfg == {"model": {"layers": [4, 2]}}, "nested data was shared"
    assert duplicate == {"model": {"layers": [4, 2, 9]}}


if __name__ == "__main__":
    check()
    print("All checks passed")
