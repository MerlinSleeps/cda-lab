# AI Log – Sheet 1

Tool: Claude (Anthropic), chat in claude.ai

| Date | What I asked | What the AI produced | What I did with it / checked |
|---|---|---|---|
| 17.11.2026 | Overview of sheet 1 and a work plan | Summary of the six steps, suggested sports and tools | Used as orientation |
| 24.11.2026 | Set up a repository for the lab | Folder structure, README, `build_context.py` (CSV → .cxt), `fca_tools.py` (derivation, closure, NextClosure trace, lattice, twins), tests, report template | _TODO: reviewed / changed …_ |
| 24.11.2026 | Collect per-sport medal data | Extracted the per-sport medal tables from Wikipedia with a web-fetch tool into `data/raw/medals_by_sport.csv`; checked: per-nation sums = official table, column sums = 329/330/385 | _TODO: spot-checked …_ |
| 24.11.2026 | Readable line diagram with highlighting | `lattice_view.py` + `lattice_template.html`: additive layout (one vector per sport, tuned by random search, then spaced per level), interactive HTML with B′/B″ and A′/A″ display and SVG export | _TODO: checked …_ |
