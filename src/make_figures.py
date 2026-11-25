"""Regenerate the whole diagram history in figures/ (see figures/README.md).

    python src/make_figures.py

01  Graphviz, first placeholder selection of 14 broad sports (269 concepts)
02  Graphviz, final selection of 13 sports
03  Additive layout, pure (matplotlib) - shows why nodes collide
04  Additive layout, spread per level (matplotlib) - static version for the report
05  Interactive additive diagram (HTML), full and gold-only
06-10 Findings, highlighted (F1-F4, gold check) · 11 panel of F1-F4
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


NEW = {"Breaking", "Skateboarding", "Sport climbing", "Surfing"}


def highlight_figure(K, name, title, strong, light=lambda n: False, ax=None):
    """Static additive diagram; `strong`/`light` are predicates on a node dict
    (keys 'extent', 'intent'). Nation labels are shown only on marked concepts."""
    r = lv.build(K)
    x, y, nodes = r["x"], r["y"], r["nodes"]
    attr, obj = lv.label_maps(K, r["L"], r["idx"])
    S = [strong(n) for n in nodes]
    Lg = [light(n) and not S[i] for i, n in enumerate(nodes)]
    own = ax is None
    if own:
        fig, ax = plt.subplots(figsize=(16, 9))
    for a, b in r["edges"]:
        hot = S[a] and S[b]
        warm = (S[a] or Lg[a]) and (S[b] or Lg[b])
        ax.plot([x[a], x[b]], [-y[a], -y[b]], zorder=1,
                color="#d9a400" if hot else ("#9fc3e8" if warm else "#e2e0da"),
                lw=2.2 if hot else (1.2 if warm else 0.6))
    col = ["#d9a400" if s else ("#9fc3e8" if l else "white") for s, l in zip(S, Lg)]
    edge = ["#a07800" if s else ("#5b8fc4" if l else "#b5b2aa") for s, l in zip(S, Lg)]
    ax.scatter(x, -y, s=30, c=col, edgecolors=edge, lw=0.9, zorder=2)
    stack = {}
    for m, i in attr.items():
        k = stack.get(i, 0)
        stack[i] = k + 1
        ax.text(x[i] + 0.01, -y[i] + 0.18 + 0.24 * k, m, fontsize=8, rotation=30,
                color=GEN_COLOR[lv.GENERATION.get(m, 1)], fontweight="bold", ha="left", va="bottom")
    by_concept = {}
    for g, i in obj.items():
        by_concept.setdefault(i, []).append(g)
    for i, gs in by_concept.items():
        if S[i] or Lg[i]:
            ax.text(x[i] + 0.01, -y[i] - 0.15, ", ".join(gs), fontsize=7.5, rotation=-30,
                    ha="left", va="top", fontweight="bold" if S[i] else "normal")
    ax.set_title(title, fontsize=11)
    ax.axis("off")
    if own:
        fig.tight_layout()
        fig.savefig(FIG / f"{name}.png", dpi=150)
        fig.savefig(FIG / f"{name}.pdf")
        plt.close(fig)
        print(f"wrote figures/{name}.png/.pdf")


def findings(K, KG):
    sub = lambda B: (lambda n: set(B) <= set(n["intent"]))
    sup = lambda A: (lambda n: set(A) <= set(n["extent"]))
    specs = [
        ("06_finding_new_sports",
         "F1: every concept with a new sport (gold) lies below Athletics (blue)",
         K, lambda n: bool(NEW & set(n["intent"])), sub(["Athletics"])),
        ("07_finding_judo_wrestling",
         "F2: {Judo, Wrestling}′ = {China, Japan, Uzbekistan}",
         K, sub(["Judo", "Wrestling"]), lambda n: False),
        ("08_finding_twins",
         "F3: Iran, Denmark, Cuba share one row {Wrestling, Taekwondo}; marked: γ(Iran) and above",
         K, sup(["Iran"]), lambda n: False),
        ("09_finding_japan",
         "F4: γ(Japan) (gold) is not below γ(United States) (blue): {Japan}″ = {Japan}, the US lacks only judo",
         K, lambda n: n["extent"] == ["Japan"], lambda n: n["extent"] == ["United States"]),
        ("10_gold_new_sports",
         "Gold only: concepts with a new sport (gold), below Athletics (blue)",
         KG, lambda n: bool(NEW & set(n["intent"])), sub(["Athletics"])),
    ]
    for name, title, ctx, strong, light in specs:
        highlight_figure(ctx, name, title, strong, light)
    fig, axs = plt.subplots(2, 2, figsize=(16, 10))
    for ax, (name, title, ctx, strong, light) in zip(axs.flat, specs[:4]):
        highlight_figure(ctx, name, title, strong, light, ax=ax)
    fig.tight_layout()
    fig.savefig(FIG / "11_findings_panel.png", dpi=170)
    fig.savefig(FIG / "11_findings_panel.pdf")
    plt.close(fig)
    print("wrote figures/11_findings_panel.png/.pdf")


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
    KG = context(bc.SPORTS, gold_only=True)
    lv.write_html(KG, FIG / "05_interactive_gold.html",
                  "Paris 2024 – olympics_gold.cxt (gold only)")
    matplotlib_diagram(KG, "04_additive_spread_gold", False,
                       "Gold only: additive layout, spread per level (47 concepts)")
    findings(K, KG)


if __name__ == "__main__":
    main()
