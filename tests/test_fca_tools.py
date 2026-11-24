"""Checks the helpers on a tiny invented context (not real Olympic data)."""

import sys
from pathlib import Path

import concepts

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import fca_tools as ft  # noqa: E402

CXT = """B

4
3

A
B
C
D
x
y
z
XX.
X.X
X..
...
"""


def ctx(tmp_path):
    p = tmp_path / "t.cxt"
    p.write_text(CXT)
    return concepts.load_cxt(str(p))


def test_derivations(tmp_path):
    K = ctx(tmp_path)
    assert ft.down(K, {"x"}) == {"A", "B", "C"}
    assert ft.up(K, {"A", "B"}) == {"x"}
    assert ft.closure(K, {"y"}) == {"x", "y"}


def test_next_closure_matches_lattice(tmp_path):
    K = ctx(tmp_path)
    mine = {frozenset(i) for i in ft.next_closure(K)}
    ref = {frozenset(c.intent) for c in K.lattice}
    assert mine == ref


def test_twins(tmp_path):
    K = ctx(tmp_path)
    assert ft.twins(K) == []
