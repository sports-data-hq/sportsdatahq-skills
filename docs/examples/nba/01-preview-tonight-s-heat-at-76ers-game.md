# Preview tonight's Heat at 76ers game

> Asked in Claude Code on 2026-11-25 with the DunkAPI MCP server connected. Skill: `nba-game-preview`. Tool calls: `get_schedule`, `get_team_stats`, `get_ratings`, `get_standings`, `get_injuries`, `list_games`. Credits: about 26. Answers change as games are played; run it yourself for today's numbers.

This isn't a preview anymore. The Heat–76ers game is already final. It was a 22:00 UTC tip (5 pm ET) at Xfinity Mobile Arena on 2026-11-25.

**Final: 76ers 111, Heat 104** (`list_games`, game id 401909317)

Neither team has a game on the schedule tonight. Their next games are on Nov 27: MIA at NY and PHI at IND. They don't meet again in the next 30 days.

**How the teams came in** (`get_standings`, which already counts today's game; `get_team_stats`, which is one game behind for both teams, so these are pre-game figures)

| | PHI | MIA |
|---|---|---|
| Record before today | 14-4 | 10-6 |
| Pace | 101.4 | 104.9 |
| Offensive rating | 113.7 | 115.1 |
| Defensive rating | 111.9 | 113.9 |
| Net rating | +1.8 | +1.2 |
| eFG% | .535 | .558 |
| Turnover % | 11.8 | 13.7 |
| Offensive rebound % | 22.5 | 24.6 |
| Three-point rate | .389 | .457 |

- Net ratings are over 18 games for PHI and 16 for MIA, so they are still fairly noisy.
- **Elo** (`get_ratings`): PHI is 10th at 1559.7 and MIA is 12th at 1551.4, so the ratings had them close.
- **Standings after the game** (`get_standings`): PHI is 15-4 and MIA is 10-7.
- **Injuries** (`get_injuries`, current report, not necessarily as of tip):
  - MIA: Giannis Antetokounmpo is day-to-day with a groin injury, listed to return Nov 25. I can't tell from this whether he played.
  - PHI: Joel Embiid is day-to-day with an illness, listed to return Nov 27. Ariel Hukporti is out with an Achilles injury.
  - Whether Embiid played is not something I can confirm, and it matters for reading the 7-point result.

There was no posted line or market probability for this game in the schedule data, so I have no market view to show.

I haven't pulled the box score yet. `get_game` for 401909317 (5 credits) would show who played, the shooting splits and the closing lines. I can run that next.

Data: get_schedule, list_games, get_team_stats, get_ratings, get_standings, get_injuries | season 2027 (2026-27)
