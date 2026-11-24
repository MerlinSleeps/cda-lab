"""Build the formal context olympics.cxt from raw Paris 2024 medal data.

Input (see data/raw/README.md):
    data/raw/medals_by_sport.csv   columns: nation,sport,gold,silver,bronze
    data/raw/medal_table.csv       columns: nation,gold,silver,bronze,total

Output:
    olympics.cxt        (Burmeister format, readable by concepts / ConExp)
    context stats on stdout (share of crosses, nation with most sports, ...)

Usage:
    python src/build_context.py                 # at least one medal
    python src/build_context.py --gold-only     # at least one gold (step 6)
"""

import argparse
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"

# 13 sports in three "generations" of the Olympic programme:
#   since 1896:        Athletics, Swimming, Wrestling, Fencing, Gymnastics, Shooting
#   added 1964 / 2000: Judo (Japan), Taekwondo (Korea), Triathlon
#   added 2020 / 2024: Breaking, Skateboarding, Sport climbing, Surfing
# Names must match the "sport" column in medals_by_sport.csv.
SPORTS = [
    "Athletics",
    "Swimming",
    "Wrestling",
    "Fencing",
    "Gymnastics",
    "Shooting",
    "Judo",
    "Taekwondo",
    "Triathlon",
    "Breaking",
    "Skateboarding",
    "Sport climbing",
    "Surfing",
]

N_NATIONS = 25


def top_nations(table: pd.DataFrame, n: int) -> list[str]:
    """Top n nations by total medals. Ties broken by gold, silver, bronze
    (medal-table order); a tie that is still left over at rank n is reported."""
    ranked = table.sort_values(
        ["total", "gold", "silver", "bronze"], ascending=False
    ).reset_index(drop=True)
    cut = ranked.loc[n - 1, "total"]
    tied = ranked[ranked["total"] == cut]
    if len(tied) > 1 and tied.index.max() >= n:
        print(f"Note: tie at {cut} medals around rank {n}: {', '.join(tied['nation'])}")
        print("      kept the first ones in medal-table order - state this in the report.")
    return ranked.head(n)["nation"].tolist()


def build(gold_only: bool) -> tuple[list[str], list[str], list[list[bool]]]:
    by_sport = pd.read_csv(RAW / "medals_by_sport.csv")
    table = pd.read_csv(RAW / "medal_table.csv")

    unknown = set(SPORTS) - set(by_sport["sport"])
    if unknown:
        raise SystemExit(f"Sports not found in raw data: {sorted(unknown)}")

    nations = top_nations(table, N_NATIONS)
    count = by_sport["gold"] if gold_only else by_sport[["gold", "silver", "bronze"]].sum(axis=1)
    has = set(zip(by_sport.loc[count > 0, "nation"], by_sport.loc[count > 0, "sport"]))

    rows = [[(g, m) in has for m in SPORTS] for g in nations]
    return nations, SPORTS, rows


def write_cxt(path: Path, objects, attributes, rows) -> None:
    lines = ["B", "", str(len(objects)), str(len(attributes)), ""]
    lines += objects + attributes
    lines += ["".join("X" if x else "." for x in row) for row in rows]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def report(objects, attributes, rows) -> None:
    crosses = sum(map(sum, rows))
    print(f"{len(objects)} nations x {len(attributes)} sports, "
          f"{crosses} crosses = {crosses / (len(objects) * len(attributes)):.1%}")
    per_nation = {g: sum(r) for g, r in zip(objects, rows)}
    per_sport = {m: sum(r[j] for r in rows) for j, m in enumerate(attributes)}
    best_g = max(per_nation.values())
    best_m = max(per_sport.values())
    print(f"most sports : {[g for g, v in per_nation.items() if v == best_g]} ({best_g})")
    print(f"most nations: {[m for m, v in per_sport.items() if v == best_m]} ({best_m})")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gold-only", action="store_true", help="cross = at least one gold")
    args = ap.parse_args()

    objects, attributes, rows = build(args.gold_only)
    out = ROOT / ("olympics_gold.cxt" if args.gold_only else "olympics.cxt")
    write_cxt(out, objects, attributes, rows)
    print(f"wrote {out.name}")
    report(objects, attributes, rows)


if __name__ == "__main__":
    main()
