# Raw data

**Source:** _TODO (e.g. Wikipedia "<Sport> at the 2024 Summer Olympics – Medal table", or olympics.com results)_
**Download date:** _TODO_

`build_context.py` expects two CSV files here:

`medal_table.csv` – overall medal table (all sports), used to pick the top 25 nations

```
nation,gold,silver,bronze,total
United States,40,44,42,126
...
```

`medals_by_sport.csv` – one row per nation and sport with at least one medal

```
nation,sport,gold,silver,bronze
United States,Swimming,8,13,7
...
```

Use the same spelling of nation and sport names in both files.
Sport names must match the `SPORTS` list in `src/build_context.py`.
