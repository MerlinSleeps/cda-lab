# Raw data

**Source:** English Wikipedia, per-sport medal tables in
[List of 2024 Summer Olympics medal winners](https://en.wikipedia.org/wiki/List_of_2024_Summer_Olympics_medal_winners)
(Volleyball, missing there in the extract, from
[Olympedia](https://www.olympedia.org/editions/63/sports/VVO) / [Beach](https://www.olympedia.org/editions/63/sports/VBV));
overall table: [2024 Summer Olympics medal table](https://en.wikipedia.org/wiki/2024_Summer_Olympics_medal_table)
**Download date:** 24.11.2026

## Files

`medals_by_sport.csv` – `sport,nation,gold,silver,bronze`, one row per nation and sport with ≥ 1 medal, all 32 sports.
Wikipedia groups disciplines into sports: *Canoeing* = slalom + sprint, *Cycling* = BMX + mountain bike + road + track,
*Gymnastics* = artistic + rhythmic + trampoline, *Volleyball* = indoor + beach, *Basketball* = 5×5 + 3×3.

`medal_table.csv` – `nation,gold,silver,bronze,total`, summed from `medals_by_sport.csv`.

## Checks

- Column sums: 329 gold, 330 silver, 385 bronze = official totals.
- Per nation, the sum over all sports equals the official medal table for all 29 nations with ≥ 8 medals.
- Includes the CAS decision on the women's floor exercise (bronze moved from USA to Romania).
- Top 25 by total medals has no tie at the cut: ranks 23–25 have 9 medals (Romania, Denmark, Cuba), the next nations have 8.
