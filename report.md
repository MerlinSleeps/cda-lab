# Beyond the Medal Table – Paris 2024 through Formal Concept Analysis

_Merlin Moller · Conceptual Data Analysis – Python Lab, Sheet 1 · Universität Kassel_

**Question.** Which nations share the same sporting strengths at Paris 2024, and what do these groups reveal that a single ranking cannot?

**Data.** Source: _TODO_, downloaded _TODO_. Tools: Python `concepts`, Graphviz.

## 1. From results to a cross table

- K = (G, M, I): G = 25 nations with the most medals, M = _n_ sports, g I m ⇔ g won ≥ 1 medal in m
- Chosen sports and why; sports left out and why
- Share of crosses: _TODO_ · nation with most sports: _TODO_ · sport with most nations: _TODO_
- What is lost by turning counts into crosses; one nation where it matters

## 2. Asking the data questions

| | Question | Formula | Answer |
|---|---|---|---|
| (a) | Medals in both judo and wrestling | {Judo, Wrestling}′ | |
| (b) | Sports where every swimming nation has a medal | {Swimming}″ | |
| (c) | Nations that medal in every sport g medals in | {g}″ | |

"Closed" in a sports journalist's words: _TODO_

## 3. Finding all strength profiles

- Number of concepts of K vs. 2^|M|
- NextClosure by hand on five sports (appendix A): intents in lectic order, first three steps explained
- Context with n attributes and 2^n concepts: _TODO_; why sports data stays far below

## 4. Reading the picture

![Concept lattice](figures/lattice.pdf)

1. _Statement – how it is read off the diagram_
2. _…_
3. _…_

## 5. Removing what is redundant

- Medal twins (clarification): _TODO_
- Reducible sports and what that means: _TODO_
- Reduced context has a lattice of the same shape: _TODO_

## 6. Your answer

| # | Finding | Concept (extent / intent) | Survives gold-only? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

At least one finding the medal table cannot show: _TODO_

---

## Appendix

A. NextClosure hand computation (`handrechnung/`)
B. Cross table `olympics.cxt`
C. Gold-only lattice
