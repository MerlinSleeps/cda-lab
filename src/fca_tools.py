"""Small FCA helpers for steps 2-5: derivation, closure, NextClosure with a
trace (to check the hand computation), lattice drawing, clarification.

    from fca_tools import load, up, down, closure
    K = load("olympics.cxt")
    down(K, {"Judo", "Wrestling"})      # {Judo, Wrestling}'  -> nations
    closure(K, {"Swimming"})            # {Swimming}''        -> sports
"""

from pathlib import Path

import concepts

ROOT = Path(__file__).resolve().parent.parent


def load(path="olympics.cxt") -> concepts.Context:
    return concepts.load_cxt(str(ROOT / path))


def up(K, objects) -> set:
    """A' : sports shared by all nations in A."""
    return set(K.intension(list(objects)))


def down(K, attributes) -> set:
    """B' : nations that have all sports in B."""
    return set(K.extension(list(attributes)))


def closure(K, attributes) -> set:
    """B'' : everything that is implied once you know B."""
    return up(K, down(K, attributes))


def next_closure(K, attributes=None, trace=False) -> list[tuple]:
    """All intents in lectic order (Ganter's NextClosure).

    attributes: optional sub-list of sports (e.g. 5 for the hand computation);
    their order in the list is the order used for the lectic order.
    trace=True prints, for every step, which attribute i is tried and why the
    candidate is accepted or rejected.
    """
    M = list(attributes) if attributes else list(K.properties)
    pos = {m: k for k, m in enumerate(M)}

    def cl(B):
        ext = down(K, B) if B else set(K.objects)
        return {m for m in M if all(m in up(K, {g}) for g in ext)}

    def fmt(S):
        return "{" + ", ".join(sorted(S, key=pos.get)) + "}"

    A = cl(set())
    intents = [A]
    step = 0
    while len(A) < len(M):
        step += 1
        for i in reversed(range(len(M))):
            m = M[i]
            if m in A:
                continue
            base = {x for x in A if pos[x] < i}
            cand = cl(base | {m})
            new = {x for x in cand - A if pos[x] < i}
            ok = not new
            if trace:
                verdict = "accept" if ok else f"reject: adds {fmt(new)} before {m}"
                print(f"step {step}: A={fmt(A)}, try i={m}: "
                      f"({fmt(base)} + {m})'' = {fmt(cand)} -> {verdict}")
            if ok:
                A = cand
                intents.append(A)
                break
    return intents


def draw(K, filename="figures/lattice", fmt="pdf"):
    """Line diagram with reduced labelling (graphviz must be installed)."""
    dot = K.lattice.graphviz(filename=str(ROOT / filename), directory=None)
    dot.format = fmt
    dot.render(cleanup=True)
    return dot


def twins(K) -> list[list[str]]:
    """Nations with identical rows ("medal twins", clarification)."""
    groups = {}
    for g in K.objects:
        groups.setdefault(frozenset(up(K, {g})), []).append(g)
    return [v for v in groups.values() if len(v) > 1]


if __name__ == "__main__":
    K = load()
    print(f"{len(K.lattice)} concepts, 2^|M| = {2 ** len(K.properties)}")
    print("medal twins:", twins(K))
