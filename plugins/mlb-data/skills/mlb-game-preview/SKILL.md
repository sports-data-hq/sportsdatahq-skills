---
name: mlb-game-preview
description: "Use when the user wants a preview of one MLB or college baseball game: 'preview Yankees vs Red Sox', 'break down tonight's Dodgers game', 'how does this pitcher match up', 'what's the run line and total', 'who's hot for the Mets series'. Produces a one-page report: records and run differential, team offense and run prevention, our Elo ratings, the starters' arsenals when known, the line and what it implies. Not for regression screens or pitcher skill changes (other mlb- skills) or model building (see model-building)."
metadata:
  version: 2.0.0
  author: SportsDataHQ
---

# MLB game preview

A one-page preview of a single game from live FastballAPI calls. Baseball means MLB unless the user names college baseball (`league: "ncaabase"`).

## Before you start
- Tools come from the FastballAPI MCP server (`https://mcp.fastballapi.com/mcp`). Call them; never recall a number.
- `season` is the calendar year. Teams accept abbreviations (`list_teams`, 1 cr).
- Probable starters are not in the schedule. If the user names them, profile them; otherwise say the starters are not confirmed in the data.

## Default path (about 21 credits, plus 10 per starter)
1. **Find the game.** `get_schedule(team)` (2 cr): game id, first pitch, median moneyline, run line and total.
2. **Records and run differential.** `get_standings(season)` (2 cr): wins, losses, run differential, Pythagorean record.
3. **Offense and run prevention.** `get_team_stats(season, team)` (5 cr) for both: runs per game for and against, OBP/SLG/OPS, K%, BB%, HR, and the same allowed.
4. **Strength.** `get_ratings(season)` (2 cr): our Elo for both teams.
5. **Starters (when named).** `search_players(name)` (1 cr), then `get_pitch_mix(pitcher_id, season)` (5 cr): usage, velocity and whiff rate per pitch type; `get_player(player_id)` (5 cr) for the season line.
6. **Injuries.** `get_injuries(team)` (2 cr).
7. **Every book's line (optional).** `get_odds(game_id)` (5 cr).

## Output template
```
<AWAY> (<W-L>, RD <+/->) at <HOME> (<W-L>, RD <+/->) | <date, first pitch ET>
Line: <ML away/home>, run line <+/-1.5>, total <t> (median of books)
Elo: <away> vs <home>
Offense (season): R/G, OPS, K%, BB% for both | Run prevention: RA/G, opp OPS
Starters: <name: pitch mix headline, velo, whiff%> or "not confirmed in the data"
Injuries: <player: status>
What to watch: 2-4 bullets tied to the numbers
Data: get_schedule, get_standings, get_team_stats, get_ratings, get_pitch_mix | season <yyyy>
```

## Rules
- Early season (under ~20 games) team rates are noisy; say so. Pitcher rates need 30+ innings before they mean much.
- Every number names its tool; the Data line has the season.
- Odds are information about the market: no side, stake or bet.
