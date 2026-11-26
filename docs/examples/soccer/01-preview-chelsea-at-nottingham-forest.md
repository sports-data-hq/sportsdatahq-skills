# Preview Chelsea at Nottingham Forest

> Asked in Claude Code on 2026-11-25 with the StrikerAPI MCP server connected. Skill: `soccer-match-preview`. Tool calls: `get_schedule`, `get_standings`, `get_ratings`, `get_team_stats`, `get_head_to_head`, `get_game_probabilities`. Credits: about 23. Answers change as games are played; run it yourself for today's numbers.

**Nottingham Forest (17th, 9 pts) vs Chelsea (8th, 16 pts) | Premier League 2026-27 | Fri 27 Nov, 20:00 UTC (3pm EST), The City Ground**

**Line (median of 10 books):** home +155 / draw +242 / away +169, total 2.5. Implied: 39.2% / 29.3% / 37.2%.
**Market (no-margin):** Forest 37.4% / draw 27.6% / Chelsea 35.0%.
Our Elo-based pregame model has Forest 41.2% / draw 27.9% / Chelsea 30.9%.

**Elo:** Forest 1485.4 vs Chelsea 1509.3. Chelsea are 24 points ahead, and Forest's home advantage in the ratings is 60 points. That is why both the model and the market lean slightly to Forest despite the table.

**Table and form** (latest first, as the table returns it)
- **Forest:** P11, 2W 3D 6L, GF 9, GA 15, GD -6. Form LWLDL. Home 1-1-3, away 1-2-3.
- **Chelsea:** P11, 5W 1D 5L, GF 20, GA 20, GD 0. Form LLWLW. Home 3-1-2, away 2-0-3.

**Per match this season (11 games each)**

| | Goals for | Goals against | xG for | xG against | Shots for / against | Possession |
|---|---|---|---|---|---|---|
| Forest | 0.82 | 1.36 | 1.77 | 1.27 | 16.5 / 10.9 | 45.4% |
| Chelsea | 1.82 | 1.82 | 1.37 | 1.63 | 13.5 / 13.0 | 50.5% |

- Forest have scored about 0.95 per match fewer than our xG says they should. They have failed to score in 6 of 11 and kept 1 clean sheet.
- Chelsea have scored about 0.45 per match more than our xG, and conceded about 0.19 more than our xG against. Our xG doesn't see defenders, so treat it as a rough guide.

**Head to head** (8 meetings in our data since 2023): Forest 2 wins, Chelsea 3, 3 draws. Goals were 10 for Forest and 12 for Chelsea. This is weak evidence. The most recent results, newest first:
- 2026-05-04: Chelsea 1–3 Forest
- 2025-10-18: Forest 0–3 Chelsea
- 2025-05-25: Forest 0–1 Chelsea
- 2024-10-06: Chelsea 1–1 Forest
- 2024-05-11: Forest 2–3 Chelsea

**Lineups:** not announced yet. Team sheets usually come out about an hour before kickoff, so I didn't call `get_lineups`.

**What to watch**
- **Forest's finishing against their chances:** Forest create more than they score from (1.77 xG vs 0.82 goals). If that gap closes, they are better than 17th. Eleven matches is a small sample, though.
- **Chelsea's defence:** they concede 1.82 a match and 13 shots, with 5.5 on target. Forest's shot volume of 16.5 a match tests that.
- **Goals:** the 2.5 line is a lean to the over, at 54% over / 46% under after removing the margin. Chelsea's goals for and against both average 1.82. Forest's goals are low, at 0.82 for and 1.36 against.
- **Form:** Forest are winless in their last four, and Chelsea have lost three of their last five.

**Data:** get_schedule, get_standings, get_ratings, get_team_stats (both clubs), get_head_to_head, get_game_probabilities | Premier League, season 2026
