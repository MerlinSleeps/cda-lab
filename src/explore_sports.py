"""Explore candidate sport selections before fixing SPORTS in build_context.py.

    python src/explore_sports.py                  # sports overview + nation profiles
    python src/explore_sports.py Judo Wrestling Swimming ...   # evaluate one selection
"""

import sys
from pathlib import Path

import pandas as pd

RAW = Path(__file__).resolve().parent.parent / "data" / "raw"

by_sport = pd.read_csv(RAW / "medals_by_sport.csv")
table = pd.read_csv(RAW / "medal_table.csv")
TOP = table.sort_values(["total", "gold", "silver", "bronze"], ascending=False).head(25)["nation"].tolist()
r = by_sport[by_sport["nation"].isin(TOP)].copy()
r["total"] = r[["gold", "silver", "bronze"]].sum(axis=1)
HAS = set(zip(r["nation"], r["sport"]))


def n_concepts(sports) -> int:
    """Number of concepts = number of distinct intersections of nation rows (plus M)."""
    intents = {frozenset(sports)}
    for g in TOP:
        row = frozenset(s for s in sports if (g, s) in HAS)
        intents |= {row & i for i in intents}
    return len(intents)


def evaluate(sports) -> None:
    crosses = sum((g, s) in HAS for g in TOP for s in sports)
    print(f"|M|={len(sports)}  concepts={n_concepts(sports)}  "
          f"density={crosses / (25 * len(sports)):.0%}  2^|M|={2 ** len(sports)}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        evaluate(sys.argv[1:])
        sys.exit()

    overview = r.groupby("sport").agg(
        nations=("nation", "nunique"),
        gold_nations=("gold", lambda s: (s > 0).sum()),
        medals=("total", "sum"),
    ).sort_values("nations", ascending=False)
    print(overview.to_string(), "\n")

    pool = overview.index[overview["nations"] >= 4]
    ext = {s: {g for g in TOP if (g, s) in HAS} for s in pool}
    print("Inclusions (every nation with a medal in s1 also has one in s2):")
    for a in pool:
        sup = [b for b in pool if b != a and ext[a] <= ext[b]]
        if sup:
            print(f"  {a} ({len(ext[a])}) -> {', '.join(sup)}")
    print()
    for g in TOP:
        sports = sorted(s for s in pool if (g, s) in HAS)
        print(f"{g:15s} {len(sports):2d}: {', '.join(sports)}")
