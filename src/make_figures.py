"""Regenerate the whole diagram history in figures/ (see figures/README.md).

    python src/make_figures.py

01  Graphviz, first placeholder selection of 14 broad sports (269 concepts)
02  Graphviz, final selection of 13 sports
03  Additive layout, pure (matplotlib) - shows why nodes collide
04  Additive layout, spread per level (matplotlib) - static version for the report
05  Interactive additive diagram (HTML), full and gold-only
"""

import sys
from pathlib import Path

import concepts
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_context as bc  # noqa: E402
import fca_tools as ft  # noqa: E402
import lattice_view as lv  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "figures"

PLACEHOLDER_14 = [
    "Athletics", "Swimming", "Cycling", "Rowing", "Canoeing", "Gymnastics", "Judo",
    "Wrestling", "Boxing", "Fencing", "Shooting", "Weightlifting", "Taekwondo", "Sailing",
]
GEN_COLOR = {0: "#2f6db5", 1: "#c2410c", 2: "#0f8a6a"}


def context(sports, gold_only=False):
    objects, attributes, rows = bc.build(gold_only, sports)
    return concepts.Context(objects, attributes, [tuple(r) for r in rows])


def graphviz(K, name):
    dot = K.lattice.graphviz(filename=str(FIG / name), directory=None)
    dot.format = "pdf"
    dot.render(cleanup=True)
    print(f"wrote figures/{name}.pdf: {len(K.lattice)} concepts")


def matplotlib_diagram(K, name, use_raw, title):
    r = lv.build(K)
    x = r["x_raw"] if use_raw else r["x"]
    y = r["y"]
    attr, obj = lv.label_maps(K, r["L"], r["idx"])
    fig, ax = plt.subplots(figsize=(16, 9))
    for a, b in r["edges"]:
        ax.plot([x[a], x[b]], [-y[a], -y[b]], color="#bdbab2", lw=0.7, zorder=1)
    ax.scatter(x, -y, s=28, facecolor="white", edgecolor="#6b6860", lw=0.9, zorder=2)
    stack = {}
    for m, i in attr.items():
        k = stack.get(i, 0)
        stack[i] = k + 1
        ax.text(x[i] + 0.01, -y[i] + 0.18 + 0.22 * k, m, fontsize=7.5, rotation=30,
                color=GEN_COLOR[lv.GENERATION.get(m, 1)], fontweight="bold", ha="left", va="bottom")
    by_concept = {}
    for g, i in obj.items():
        by_concept.setdefault(i, []).append(g)
    for i, gs in by_concept.items():
        ax.text(x[i] + 0.01, -y[i] - 0.15, ", ".join(gs), fontsize=7, rotation=-30,
                ha="left", va="top")
    ax.set_title(title, fontsize=11)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(FIG / f"{name}.pdf")
    fig.savefig(FIG / f"{name}.png", dpi=150)
    plt.close(fig)
    print(f"wrote figures/{name}.pdf/.png")


def main():
    FIG.mkdir(exist_ok=True)
    graphviz(context(PLACEHOLDER_14), "01_graphviz_placeholder14")
    K = context(bc.SPORTS)
    graphviz(K, "02_graphviz_final13")
    matplotlib_diagram(K, "03_additive_pure", True,
                       "Additive layout (pure): concept = sum of its sports' vectors")
    matplotlib_diagram(K, "04_additive_spread", False,
                       "Additive layout, spread per level (classic sports left, new sports right)")
    lv.write_html(K, FIG / "05_interactive.html", "Paris 2024 – olympics.cxt")
    lv.write_html(context(bc.SPORTS, gold_only=True), FIG / "05_interactive_gold.html",
                  "Paris 2024 – olympics_gold.cxt (gold only)")


if __name__ == "__main__":
    main()
