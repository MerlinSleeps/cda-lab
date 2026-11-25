# TODO – Sheet 1 (submission: Moodle, Thu 26.11.2026 00:00)

Legend: 🧠 = understand/decide yourself (colloquium!) · ⚙️ = code/computation, Claude can help

## Now – before submission
1. - [ ] 🧠 **Clean up the hand computation** and replace the photos in `handrechnung/` (keep the file names `hand_01…`, `hand_02…`, `hand_03…`):
   - [ ] Start: write `∅″ = ∅ → intent 1`
   - [ ] Step 1: replace the "Ath ≤ Surf" notes by `✗ Ath new < 5` (≤ means something else in the lattice)
   - [ ] Step 2, line i = 1: `({Swim} ∩ ∅) ∪ {Ath} = {Ath}, {Ath}″ = {Ath} → ✓ nothing new < 1` (instead of {Ath, Swim}″)
   - [ ] Step 4, i = 4: `✗ Swim new < 4`
   - [ ] A = {1,3}: i = 5 and i = 4 `✗ (2 new)`; i = 2: `{1,2}″ = {1,2}` (no 3!) `✓`
   - [ ] A = {1,2,4}: i = 5 `✗ (3 new < 5)`, i = 3 `✓`
   - [ ] A = {1,2,3}: i = 5 `✗ (4 new < 5)`, i = 4 `✓ (only 5 new, 5 > 4)`, then `A = M → stop`
   - [ ] List of the 10 intents with extent sizes (25, 14, 19, 4, 5, 12, 3, 5, 4, 2)
2. - [ ] 🧠 Final read of `report.md` (main text is exactly 5 pages – do not make it longer), own wording where wanted
3. - [ ] ⚙️ Re-export: `python src/export_report.py` (needs `pip install markdown playwright` + `playwright install chromium`), check: main text ≤ 5 pages
4. - [ ] 🧠 `AI_LOG.md`: fill the two `_…_` fields (own spot-checks of the data, own final edits)
5. - [ ] 🧠 Spot-check 2–3 rows of the raw data against Wikipedia (e.g. Japan judo, Kenya athletics)
6. - [ ] Submit in Moodle: `report.pdf`, `olympics.cxt`, `src/build_context.py`, `figures/` (diagrams), `handrechnung/` (photos), `AI_LOG.md`

## Colloquium preparation
- [ ] 🧠 Compute a derivation and a closure by hand on the own cross table (e.g. {Breaking}″, {Ukraine}″)
- [ ] 🧠 Explain NextClosure on the sub-context: candidate ((A ∩ {1..i−1}) ∪ {i})″, accept/reject, binary-counting picture
- [ ] 🧠 Read μ(m) and γ(g) in the diagram; show a subordination (Breaking → Athletics) and an incomparable pair (Judo/Taekwondo)
- [ ] 🧠 Point to the concept behind every finding F1–F4, and explain the gold-only result

## Open questions
- [ ] Format and content required by the general AI policy for `AI_LOG.md`

## Done
- [x] Repo, `build_context.py`, `fca_tools.py`, tests; setup on MacBook
- [x] Raw data for all 32 sports, checked against the official medal table; top 25 without tie
- [x] Sports chosen: 13 in three generations and different cultural origins → 125 concepts
- [x] Diagram history 01–05, interactive diagram, findings figures 06–11, gold-only lattice
- [x] Step 1: context, choice of sports, shape of the table, meaning and loss of a cross
- [x] Step 2: (a)–(c) by hand, corrected; "closed" for a journalist
- [x] Step 3: 125 vs. 2^13, hand computation (10 intents), contranominal scale
- [x] Step 4: diagram, μ/γ explained, three statements
- [x] Step 5: twins, no reducible sport, 6 reducible nations, isomorphic reduced lattice, core insight
- [x] Step 6: findings F1–F4 with gold check, limitations, what the medal table cannot show
- [x] Report draft revised after my review (6 points), PDF exported
- [x] `AI_LOG.md` completed with my decisions and corrections
