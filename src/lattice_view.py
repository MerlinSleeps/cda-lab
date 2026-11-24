"""Interactive additive line diagram of olympics.cxt -> figures/lattice.html

Additive layout: every sport m gets a vector (x_m, 1); a concept is drawn at the
sum of the vectors of its intent, so its height is the number of sports it has
and lines with the same sport added are parallel. The x-components are chosen
by generation (classic left, new right) and then tuned by a small random search
that pushes nodes apart and away from lines they do not belong to.

    python src/lattice_view.py                  # olympics.cxt -> figures/05_interactive.html
    python src/lattice_view.py olympics_gold.cxt  # -> figures/05_interactive_gold.html
"""

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fca_tools as ft  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# x-range per generation: classic -> left, new -> right
GENERATION = {
    "Athletics": 0, "Swimming": 0, "Wrestling": 0, "Fencing": 0,
    "Gymnastics": 0, "Shooting": 0,
    "Judo": 1, "Taekwondo": 1, "Triathlon": 1,
    "Breaking": 2, "Skateboarding": 2, "Sport climbing": 2, "Surfing": 2,
}
RANGE = {0: (-1.0, -0.1), 1: (-0.45, 0.45), 2: (0.1, 1.0)}
GEN_NAME = {0: "since 1896", 1: "added 1964 / 2000", 2: "added 2020 / 2024"}


def spread(x, y, gap=0.2):
    """Keep the additive left-to-right order within each level, but push
    nodes apart to at least `gap`, keeping the level centred where it was."""
    x = x.copy()
    for level in np.unique(y):
        ids = np.where(y == level)[0]
        ids = ids[np.argsort(x[ids], kind="stable")]
        xs = x[ids].copy()
        for k in range(1, len(xs)):
            xs[k] = max(xs[k], xs[k - 1] + gap)
        xs += x[ids].mean() - xs.mean()
        x[ids] = xs
    return x


def build(K, iters=6000, seed=1):
    """K: concepts.Context. Returns positions (pure additive and spread) and graph."""
    M = list(K.properties)
    G = list(K.objects)
    L = list(K.lattice)
    idx = {c: i for i, c in enumerate(L)}
    A = np.array([[m in c.intent for m in M] for c in L], dtype=float)  # concept x sport
    edges = [(idx[c], idx[d]) for c in L for d in c.lower_neighbors]
    E = np.array(edges)
    y = A.sum(axis=1)

    gen = [GENERATION.get(m, 1) for m in M]
    lo = np.array([RANGE[g][0] for g in gen])
    hi = np.array([RANGE[g][1] for g in gen])

    def score(vx):
        x = A @ vx
        dx = np.abs(x[:, None] - x[None, :])
        same = (y[:, None] == y[None, :]) & ~np.eye(len(L), dtype=bool)
        overlap = np.clip(0.35 - dx, 0, None)[same].sum()
        # node lying on an edge it is not part of
        a, b = E[:, 0], E[:, 1]
        t = (y[None, :] - y[a][:, None]) / (y[b] - y[a])[:, None]   # edges x nodes
        inside = (t > 0) & (t < 1)
        xe = x[a][:, None] + t * (x[b] - x[a])[:, None]
        near = np.clip(0.2 - np.abs(xe - x[None, :]), 0, None) * inside
        length = np.abs(x[a] - x[b]).sum()
        return 10 * overlap + 5 * near.sum() + 0.05 * length

    rng = np.random.default_rng(seed)
    vx = (lo + hi) / 2 + rng.uniform(-0.05, 0.05, len(M))
    best = score(vx)
    for k in range(iters):
        cand = vx.copy()
        j = rng.integers(len(M))
        step = 0.3 * (1 - k / iters) + 0.02
        cand[j] = np.clip(cand[j] + rng.normal(0, step), lo[j], hi[j])
        s = score(cand)
        if s < best:
            vx, best = cand, s
    x_raw = A @ vx
    x = spread(x_raw, y)

    nodes = [{
        "x": round(float(x[idx[c]]), 4), "y": int(y[idx[c]]),
        "extent": sorted(c.extent), "intent": [m for m in M if m in c.intent],
    } for c in L]
    return {"K": K, "M": M, "G": G, "L": L, "idx": idx, "nodes": nodes, "edges": edges,
            "vx": vx, "score": best, "x_raw": x_raw, "x": x, "y": y}


def label_maps(K, L, idx):
    M, G = list(K.properties), list(K.objects)
    attr = {}
    for m in M:
        ext = set(K.extension([m]))
        attr[m] = next(idx[c] for c in L if set(c.extent) == ext)
    obj = {}
    for g in G:
        intent = set(K.intension([g]))
        obj[g] = next(idx[c] for c in L if set(c.intent) == intent)
    return attr, obj


def write_html(K, out, title):
    r = build(K)
    M, G, L, idx, nodes, edges, vx = (r[k] for k in ("M", "G", "L", "idx", "nodes", "edges", "vx"))
    attr, obj = label_maps(K, L, idx)
    data = {
        "title": title,
        "sports": [{"name": m, "gen": GENERATION.get(m, 1), "concept": attr[m],
                    "vx": round(float(v), 3)} for m, v in zip(M, vx)],
        "nations": [{"name": g, "concept": obj[g]} for g in G],
        "genNames": GEN_NAME,
        "nodes": nodes,
        "edges": edges,
    }
    template = (ROOT / "src" / "lattice_template.html").read_text(encoding="utf-8")
    html = template.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False))
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}: {len(nodes)} concepts, layout score {r['score']:.2f}")


def main():
    cxt = sys.argv[1] if len(sys.argv) > 1 else "olympics.cxt"
    name = "05_interactive_gold.html" if "gold" in cxt else "05_interactive.html"
    write_html(ft.load(cxt), ROOT / "figures" / name, f"Paris 2024 – {cxt}")


if __name__ == "__main__":
    main()
