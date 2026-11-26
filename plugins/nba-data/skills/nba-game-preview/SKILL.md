---
name: nba-game-preview
description: "Use when the user wants a preview of one NBA, WNBA or college basketball game: 'preview Celtics vs Knicks', 'break down tonight's Lakers game', 'who's out for the Nuggets', 'pace and efficiency matchup for this game', 'what's the line on Bucks Heat'. Produces a one-page report: records, ratings, pace and efficiency (offensive, defensive, net rating, four factors), injuries, the line and what it implies. Not for player props (see nba-player-props-research), minutes when a star sits (see nba-minutes-usage-redistribution) or modeling (see model-building)."
metadata:
  version: 2.0.0
  author: SportsDataHQ
---

# NBA game preview

A one-page preview of a single game from live DunkAPI calls. Basketball means the NBA unless the user names the WNBA (`league: "wnba"`), men's or women's college (`ncaam`, `ncaaw`) or the NBL.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the DunkAPI MCP server (`https://mcp.dunkapi.com/mcp`). Call them; never fill in a number from memory.
- `season` is the year the season ends (2026 = 2025-26). WNBA seasons are calendar years.
- Teams accept abbreviations; `list_teams` (1 cr) if unsure.

## Default path (about 21 credits)
1. **Find the game.** `get_schedule(team)` (2 cr): game id, tip time and today's line.
2. **Team efficiency.** `get_team_stats(season, team)` (5 cr) for both teams: pace, offensive, defensive and net rating per 100 possessions, the four factors (eFG%, turnover %, offensive rebound %, free throw rate), three-point rate. Pass `before: <date>` for point-in-time numbers on a past game.
3. **Strength.** `get_ratings(season)` (2 cr): our Elo ratings for both teams. `get_standings(season)` (2 cr) for records.
4. **Injuries.** `get_injuries(team)` (2 cr) for each team: out, day-to-day, expected return.
5. **What the market implies.** `get_game_probabilities(game_id)` (5 cr): average implied and no-margin win probability, spread and total. The market's view, not ours.
6. **After the game (optional).** `get_game(game_id)` (5 cr) for box scores and every book's closing line.

## Output template
```
<AWAY> (<record>) at <HOME> (<record>) | <date, tip ET>
Line: <spread> / total <total> | Market: <home no-margin win %> | Elo: <away> vs <home>
Pace: <away> vs <home> possessions per 48 (league rank)
Efficiency: ORtg / DRtg / Net for both, last <n> games and season
Four factors edge: where one team clearly leads (eFG%, TOV%, OREB%, FT rate)
Injuries: <player: status, expected return>
What to watch: 2-4 bullets tied to the numbers
Data: get_schedule, get_team_stats, get_ratings, get_injuries, get_game_probabilities | season <yyyy>
```

## Rules
- Ratings per 100 possessions need a sample: show games played. Early season (first 15 games) is noisy; say so.
- Every number names its tool; the Data line lists them with the season.
- Odds are information about the market: no side, no stake, no bet.
- If a star's status is unknown (not on the report yet), say that rather than assuming he plays.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.