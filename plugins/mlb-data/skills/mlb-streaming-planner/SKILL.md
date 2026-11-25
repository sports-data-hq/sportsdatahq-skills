---
name: mlb-streaming-planner
description: "Use when the user wants to plan a baseball week around schedules: 'who has the most games this week', 'who should I stream', 'which teams play at home this week', 'easy offences to pitch against', 'two-start week planning', 'which bullpen games are coming'. Builds a week view from the schedule, opponents' offence and run prevention, recent form of named players, injuries and the market's total. Not for lucky or unlucky results (see mlb-regression-candidates), a pitcher's pitch changes (see mlb-pitcher-skill-change) or one game's preview (see mlb-game-preview)."
metadata:
  version: 2.0.0
  author: SportsDataHQ
---

# MLB streaming planner

Streaming is a scheduling problem: who plays how often, against whom, and where. This skill assembles the week from FastballAPI schedules and opponent numbers. It does not know probable starters or fantasy scoring, and says so.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the FastballAPI MCP server (`https://mcp.fastballapi.com/mcp`). Call them; never fill in a number from memory.
- `season` is the calendar year. The schedule covers the next 1 to 30 days.
- Probable starters are not in the data. Do not name who will pitch. If the user names a pitcher, profile him; otherwise show teams and opponents only. Two-start weeks cannot be confirmed from the data; say a team plays enough games for one and leave it there.
- Fantasy scoring is not in the data. Report baseball numbers and let the user apply their league's scoring.
- Opponent strength is season to date; early in a season (under about 20 games) it is noisy.

## Default path (about 15 to 30 credits)
1. **The week.** `get_schedule(days: 7)` (2 cr), or with `team` for one club: games per team, home or away, opponents, and the median run line and total.
2. **Opponent offence.** `get_team_stats(season)` (5 cr, once for the league if the tool returns every team, otherwise per opponent): runs per game, OPS, K% and BB% for and against.
3. **Named players.** `search_players(name)` (1 cr), then `get_player_games(player_id, season, limit: 10)` (5 cr): the last starts or games.
4. **Availability.** `get_injuries(team)` (2 cr) for the teams involved.
5. **Market context (optional).** The schedule's total is the market's expected scoring; report it as such.

## Reading the week
Rank opponents by what the user wants (strikeout rate for pitching, runs per game for hitting) and show the values. Home park matters; the schedule's venue tells you home or away but park effects are not in the data, so do not quote them. Totals are the market's view of scoring, not a forecast from us.

## Output template
```
Week of <date> | games per team: <team: n (home/away)>
Opponent offence (season): <team: R/G, OPS, K%, BB%> sorted by <chosen measure>
Player recent form (if named): <name: last 10 games line, innings or PA counted>
Injuries: <player: status>
Market totals this week: <game: total> (information only)
Read: 2-3 bullets with the numbers; probable starters not in the data
Data: get_schedule, get_team_stats, get_player_games, get_injuries | season <yyyy>
```

## Rules
- Never claim who is starting; the data has no probable starters.
- Do not apply any fantasy scoring system that the user did not state.
- Opponent numbers are season to date, not matchup-specific; say so.
- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links.

## Example prompts
- "Which teams play the most games this week?"
- "Which offences are easiest to pitch against right now?"
- "How has he pitched in his last 5 starts?"
