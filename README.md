# CDA Lab – Sheet 1: Beyond the Medal Table

Conceptual Data Analysis – Python Lab, Knowledge & Data Engineering, Universität Kassel (WiSe 26/27).
Deadline Sheet 1: **26.11.2026**

> Which nations share the same sporting strengths at Paris 2024,
> and what do these groups reveal that a single ranking cannot?

## Structure

```
data/raw/            raw medal data + source/download date (README there)
src/build_context.py raw CSV -> olympics.cxt (+ --gold-only for step 6)
src/fca_tools.py     derivation, closure, NextClosure trace, lattice, twins
src/lattice_view.py  interactive additive line diagram (HTML), highlight sports/nations, SVG export
src/make_figures.py  regenerates the diagram history 01-05 in figures/
figures/             line diagram(s)
handrechnung/        photo/scan of the NextClosure hand computation (step 3)
report.md            the report (max. 5 pages + appendix)
AI_LOG.md            AI usage log (general AI policy)
olympics.cxt         generated formal context (submitted)
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Drawing lattices also needs the Graphviz program itself (not just the Python package):
macOS `brew install graphviz`, Windows `winget install Graphviz.Graphviz` (then reopen the terminal).

## Workflow

```bash
python src/build_context.py              # -> olympics.cxt + stats for step 1
python src/build_context.py --gold-only  # -> olympics_gold.cxt for step 6
python src/fca_tools.py                  # number of concepts, medal twins
python src/make_figures.py               # -> all diagrams in figures/ (see figures/README.md)
python -m pytest -q                      # helper self-test
```

In Python / a notebook:

```python
import sys; sys.path.insert(0, "src")
import fca_tools as ft
K = ft.load()
ft.down(K, {"Judo", "Wrestling"})   # 2(a)
ft.closure(K, {"Swimming"})         # 2(b)
ft.next_closure(K, ["Swimming", "Judo", "Wrestling", "Boxing", "Rowing"], trace=True)  # check step 3
ft.draw(K)                          # Graphviz diagram (see also make_figures.py)
```

## Submission checklist

- [ ] `report.md` (or exported PDF), ≤ 5 pages + appendix
- [ ] `olympics.cxt`
- [ ] `src/build_context.py`
- [ ] line diagram(s) in `figures/`
- [ ] hand computation (step 3) in `handrechnung/`
- [ ] `AI_LOG.md`
- [ ] data source + download date in report and `data/raw/README.md`
