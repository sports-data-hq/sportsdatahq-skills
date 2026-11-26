# Preview Chiefs at Bills this week

> Asked in Claude Code on 2026-11-25 with the EndzoneAPI MCP server connected. Skill: `nfl-game-preview`. Tool calls: `get_schedule`, `get_standings`, `get_game_detail`, `get_injuries`, `get_game_probabilities`, `get_team_stats`. Credits: about 33. Answers change as games are played; run it yourself for today's numbers.

**Chiefs (8-2) at Bills (9-1)** | Thu Nov 26, 8:20 PM ET (kickoff 2026-11-27 01:20Z) | Highmark Stadium, outdoors, artificial turf. Weather is not posted yet.
Week 12, 2026 season. Both teams are on 4 days' rest.

**Line:** Bills -3 (-2.5 at some books), total 46.5. Moneyline BUF -150 / KC +127. The total opened at 50.5 at most books and is now 45.5–46.5 (`get_game_detail`).
**Market view:** no-margin win probability is BUF 57.8% and KC 42.2%, from 8 books (`get_game_probabilities`). That is the market's number, not a prediction.

**Form** (`get_standings`)
- **BUF:** 9-1, streak W6, 5-0 on the road, 4-1 at home. Points 313 for / 208 against, +105.
- **KC:** 8-2, streak W3, 5-0 at home, 3-2 on the road. Points 271 for / 163 against, +108.
- The tools returned no per-game scores, so I can't list the last 5 results. Only the streaks above are available.

**Efficiency, season to date over 10 games each** (`get_team_stats`)
Only offensive EPA/play came back. Defensive EPA allowed and success rate were not available, and the game file's team stats were empty.

| | KC | BUF |
|---|---|---|
| Pass EPA/play | 0.183 | 0.166 |
| Rush EPA/play | 0.054 | 0.094 |
| Yards per attempt | 8.01 | 8.44 |
| Yards per carry | 4.88 | 4.59 |
| TDs (pass / rush) | 22 / 11 | 14 / 21 |
| INTs thrown | 4 | 9 |
| Fumbles lost | 3 | 7 |
| Sacks taken | 13 | 21 |
| Sacks / QB hits made | 19 / 52 | 23 / 84 |

**Injuries that matter** (`get_injuries`, week 12)
No game statuses (Out, Doubtful, Questionable) are posted yet. These are practice participation only.
- **KC:**
  - Mahomes (QB, knee): full.
  - Rashee Rice (WR, knee): full.
  - Trey Smith (G, concussion): full.
  - Jaylon Moore (T, ankle): did not participate.
  - Kenneth Walker III (RB, groin): limited.
  - Omarr Norman-Lott (DT, knee): limited.
- **BUF:**
  - Christian Benford (CB, groin): limited.
  - O'Cyrus Torrence (G, ankle): limited.
  - Dalton Kincaid (TE, thumb): limited.
  - Dorian Williams (LB, calf): limited.
  - T.J. Sanders (DE, shoulder): limited.
  - Spencer Brown (T), Connor McGovern (C), Greg Rousseau and Ed Oliver: full.
  - Josh Allen is not on the report.

**What to watch**
- **Pass rush:** BUF has 84 QB hits to KC's 52, and KC has taken 13 sacks to BUF's 21. Moore, KC's tackle, did not practice, which matters against that rush.
- **Ball security:** BUF has thrown 9 INTs and lost 7 fumbles, against KC's 4 and 3. Turnovers are the likeliest source of a swing.
- **Run game:** BUF has 21 rushing TDs on 320 carries and leads in rush EPA/play. KC's rush EPA/play is only 0.054, and the passing game carries its offense.
- **Total:** the 4-point drop from the opening number is worth tracking once weather is posted. It is outdoors in late November.

**Not covered:** head-to-head history, and depth-chart checks on the limited players. Say if you want either.

Data: get_schedule, get_game_detail, get_standings, get_injuries (KC, BUF), get_game_probabilities, get_team_stats (KC, BUF) | season 2026, week 12. Early-season noise isn't a concern at 10 games, but EPA excludes penalties, kneels and spikes.
