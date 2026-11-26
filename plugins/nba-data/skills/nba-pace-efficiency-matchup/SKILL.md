---
name: nba-pace-efficiency-matchup
description: "Use when the user asks about tempo or how two NBA or WNBA teams' styles match up, in fan or analyst wording: 'is this going to be a track meet', 'pace of Pacers vs Thunder', 'whose offense beats whose defense', 'net rating edge', 'four factors for this game', 'slow grind or shootout', 'does the total fit the pace'. Use this whenever tempo, pace or team efficiency is compared. Load it for short fragments and follow-ups too, even with no name given, instead of answering from memory or going straight to the raw tools. Lines up pace, offensive and defensive rating per 100 possessions and the four factors for both teams, plus our ratings and the posted total as market information. Not for a full game preview (see nba-game-preview), player lines (see nba-player-props-research), minutes when a player sits (see nba-minutes-usage-redistribution) or shot locations (see nba-shot-quality)."
metadata:
  version: 2.0.0
  author: SportsDataHQ
---

# NBA pace and efficiency matchup

Pace sets how many possessions a game has; efficiency sets what each is worth. This skill lays the two teams side by side and says where each side's strength meets the other's weakness, from DunkAPI team stats.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the DunkAPI MCP server (`https://mcp.dunkapi.com/mcp`). Call them; never fill in a number from memory.
- `season` is named by the year it ends (2025 = 2024-25); WNBA seasons are calendar years. Player ids from `search_players(name)` (1 cr); teams accept abbreviations.
- `get_team_stats` returns pace, offensive, defensive and net rating per 100 possessions, the four factors (eFG%, turnover %, offensive rebound %, free throw rate) and three-point rate, computed from every box score, with `season_type` for regular season or postseason.
- Ratings from `get_ratings` are our Elo, not a ranking; do not call them efficiency.

## Default path (about 12 credits)
1. **Find the game.** `get_schedule(team)` (2 cr): game id, start time and today's lines.
2. **Team numbers.** `get_team_stats(team, season)` (5 cr) for both teams, or once without `team` (5 cr) for the whole league to place each team in the distribution.
3. **Strength.** `get_ratings(season)` (2 cr): our Elo for both.
4. **Availability (optional).** `get_injuries(team)` (2 cr): efficiency is season to date, so a missing starter changes it.
5. **Market (optional).** `get_game_probabilities(game_id)` (5 cr): the posted total and the market's win probability, reported as the market's view.

## How to line them up
Report each team's pace and efficiency, then read both ways: a team's offence against the other's defence on each of the four factors. A rough expected pace is the average of the two teams' paces; label it a rule of thumb, not a model output. Early in a season (under about 15 games) the numbers are noisy; say so.

## Output template
```
<Away> at <Home> | <date> | season <yyyy>, games <n> and <n>
Pace (possessions per 48): <away> vs <home> | rule-of-thumb average <v>
Offence / defence / net rating: <away> | <home>
Four factors, offence vs the other's defence: eFG% | turnover % | offensive rebound % | free throw rate
Matchup edges: 2-3 bullets with the numbers
Market (if asked): total <t>, market win probability <%> (information only)
Data: get_schedule, get_team_stats, get_ratings[, get_game_probabilities] | season <yyyy>
```

## Rules
- Season-to-date numbers do not include tonight's injuries; check them or say they were not checked.
- Pace differences of one or two possessions are within noise; say so.
- The posted total is the market's number; do not present it as ours.
- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.

## Example prompts
- "Is Celtics vs Knicks a fast game?"
- "Compare the Thunder and Nuggets offence against defence"
- "Which team has the better net rating, Cavs or Pacers?"
