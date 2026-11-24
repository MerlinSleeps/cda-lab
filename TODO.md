# TODO – Sheet 1 (deadline Thu 26.11.2026)

Legend: 🧠 = understand/decide yourself (colloquium!) · ⚙️ = code/computation, Claude can help

## Done
- [x] Repo structure, `build_context.py`, `fca_tools.py`, tests, report template
- [x] Raw data for all 32 sports (Wikipedia/Olympedia), checked against the official medal table
- [x] Top 25 fixed (no tie at the cut)
- [x] Setup on MacBook (packages installed, tests pass)
- [x] Sports chosen: 13 in three generations (since 1896 · 1964/2000 · 2020/24) → 125 concepts
- [x] `SPORTS` updated, `olympics.cxt` and `olympics_gold.cxt` rebuilt
- [x] Diagram history in `figures/` (Graphviz → additive → interactive), see `figures/README.md`
- [x] Interactive additive line diagram (`figures/05_interactive.html`) with highlighting and SVG export

## Tue 24.11. – foundations + steps 1–2
- [ ] 🧠 Justify the sport selection in the report (incl. origin vs. dominance for judo/taekwondo, what was left out)
- [ ] 🧠 Write step 1: share of crosses, nation with most sports, sport with most nations, information loss + example nation
- [ ] 🧠 Understand the derivation operators A′, B′, B″ (explanation with Claude)
- [ ] 🧠 Step 2 (a)–(c): write the formula, check by hand on the cross table, cross-check with `fca_tools` / interactive diagram
- [ ] 🧠 Explain "closed" in a sports journalist's words

## Wed 25.11. – steps 3–5
- [ ] 🧠 Understand NextClosure / lectic order
- [ ] 🧠 Hand computation on 5 sports (paper), first 3 steps with reasons; check with `next_closure(..., trace=True)`; photo into `handrechnung/`
- [ ] 🧠 Number of concepts vs. 2^|M|; context with 2^n concepts (contranominal scale); why sports data stays far below
- [ ] 🧠 Export one highlighted view per finding as SVG and include it in the report
- [ ] 🧠 Step 4: read ≥ 3 statements off the diagram (subordination, incomparable, position of the top 5)
- [ ] ⚙️ Step 5: medal twins, reducible sports (add a reducibility function)
- [ ] 🧠 Step 5: explain what reducibility means, check the shape of the reduced lattice

## Thu 26.11. – step 6 + submission
- [ ] 🧠 3–5 findings with concept (extent/intent), marked in the diagram; ≥ 1 finding the medal table cannot show
- [x] ⚙️ Gold-only variant built (`olympics_gold.cxt`, `figures/05_interactive_gold.html`)
- [ ] 🧠 Robustness: which findings survive the gold-only variant?
- [ ] 🧠 Finish the report (≤ 5 pages + appendix), source + download date included
- [ ] ⚙️ Export as PDF, check page count
- [ ] 🧠 Complete `AI_LOG.md` (TODO fields: what was checked/changed)
- [ ] 🧠 Spot-check the raw data against Wikipedia yourself
- [ ] Go through the submission checklist in the README, submit

## Colloquium preparation
- [ ] 🧠 Compute a derivation and a closure by hand on the own cross table
- [ ] 🧠 Point to the concept behind every finding in the diagram

## Open questions
- [ ] Submission time on 26.11. and submission channel (Moodle?)
- [ ] Format and content required by the general AI policy for `AI_LOG.md`
