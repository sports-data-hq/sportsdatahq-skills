# Which Premier League teams are over- or under-performing their xG this season?

> Asked in Claude Code on 2026-11-25 with the StrikerAPI MCP server connected. Skill: `soccer-xg-breakdown`. Tool calls: `get_team_stats`, `get_standings`. Credits: about 7. Answers change as games are played; run it yourself for today's numbers.

**Over the first 11 matches, Brighton, Hull and Brentford are beating their xG. Nottingham Forest, Sunderland and Manchester United are well below theirs.** This uses our xG, which is a location-only model. It doesn't see defenders, the pass or the keeper. I took the per-match averages from `get_team_stats` and multiplied by 11 to get season totals, so they are rounded. I took the table from `get_standings`.

**Overperforming: goal difference above xG difference**

| Team | Goals for vs xG for | Goals against vs xG against | Net gap |
|---|---|---|---|
| Brighton | 26 vs 23.0 | 9 vs 16.3 | about **+10** |
| Hull | 13 vs 12.2 | 11 vs 17.7 | about **+7.5** |
| Brentford | 20 vs 18.5 | 11 vs 15.6 | about **+6** |
| Chelsea | 20 vs 15.1 | 20 vs 17.9 | about **+3** |
| Arsenal | 17 vs 18.9 | 7 vs 12.2 | about **+3** |

- Brighton's gap is mostly defence. They have conceded 9 goals from about 16 xG against, and they are also scoring about 3 more than their chances suggest.
- Hull's gap is also mostly defence. They concede 1.61 xG per match, the third-highest in the league, but have conceded only 1.0 goals per match.
- Chelsea's gap comes from attack. They have scored about 5 more than their xG, while their xG against is poor (1.63 per match).
- Arsenal are slightly under on attack (17 goals from about 19 xG). Their defence is outperforming by about 5 goals, so their top spot looks a little flattered by luck at the back.

**Underperforming: goal difference below xG difference**

| Team | Goals for vs xG for | Goals against vs xG against | Net gap |
|---|---|---|---|
| Nottingham Forest | 9 vs 19.5 | 15 vs 14.0 | about **-11.5** |
| Sunderland | 8 vs 16.4 | 17 vs 16.4 | about **-9** |
| Manchester United | 14 vs 18.9 | 23 vs 20.9 | about **-7** |
| Crystal Palace | 12 vs 16.2 | 27 vs 27.0 | about **-4** |
| Fulham | 11 vs 17.4 | 13 vs 15.8 | about **-3.5** |
| Tottenham | 12 vs 18.2 | 11 vs 14.7 | about **-2.5** |

- Forest are the biggest outlier. They average 16.5 shots per match but have scored only 0.82 goals per match, and they have failed to score in 6 of 11. They sit 17th in the table with an xG profile (1.77 for, 1.27 against) that looks like a top-half side.
- Sunderland have scored 8 goals from about 16 xG.
- Manchester United rank first in the league for shots (18.5 per match) but are 19th in the table. They are underperforming at both ends, though the defensive part is small.
- Crystal Palace's xG against is 2.45 per match, the worst in the league, and they have conceded exactly that. They are bottom because of the chances they allow, not bad luck.
- Tottenham and Fulham are under on attack by 6 or more goals each, but their defences are running somewhat hot or are about neutral.

**How much of this is luck**
- Eleven matches is a small sample. A single team's gap of 5 to 10 goals can come from luck alone. Over this stretch, Forest's and Sunderland's attacking gaps (about 10 and 8 goals) are the largest, but I haven't computed a z-score for either, because I don't have shot counts per team.
- Defensive overperformance, such as Brighton's, Hull's and Arsenal's, tends to be less persistent than good chance creation. Chance quality is the steadier signal. Treat these gaps as "results ahead of or behind the chances", not as a lasting skill.
- Manchester City, Bournemouth, Newcastle, Coventry and Liverpool are within about 3 goals of their xG in total, so they are roughly in line.
- The data covers every final match in the season. Played counts of 11 match the table, so these should all be league games.

Data: `get_team_stats`, `get_standings` | Premier League, season 2026.

I can pull `get_shot_map` for Forest or Brighton to see whether the gap comes from shot location, finishing or goalkeeping. Each call costs 10 credits.
