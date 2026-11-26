---
name: nba-dfs-lineup
description: "Use when someone has an NBA daily fantasy slate and wants lineups built: 'build my NBA DraftKings lineup', 'salary file for tonight, make a lineup', 'FanDuel lineup under the cap', 'value plays tonight', 'who is the cheap play with the starter out', 'stars and scrubs build', 'project the slate in fantasy points', 'late swap options'. Builds lineups under the cap from the user's salary file using the market's per-player projection (points, rebounds, assists, threes, steals, blocks medians as fantasy points). Also for bare follow-ups with no names: load this skill first, then ask for what is missing, rather than answering from memory. Not for entry fees, contest choice or how much to play, which it will not advise, and not for weekly streaming (see nba-fantasy-streaming) or prop research (see nba-player-props-research)."
metadata:
  version: 1.0.0
  author: SportsDataHQ
---

# NBA DFS lineup builder

NBA DFS is a cap puzzle where the edge is minutes. The market's median for each stat already prices the injury news and the matchup, so it is the projection input; the salary file comes from the user. This skill turns medians into points, finds cheap players whose minutes just rose, and builds lineups under the cap.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the DunkAPI MCP server. `season` is the year the season ends (2026 = 2025-26). Player ids come from `search_players(name)` (1 cr).
- Required from the user: the salary file (name, position, team, salary), the cap, the roster slots and the scoring. DraftKings classic is usually PG, SG, SF, PF, C, G, F, UTIL at 50,000; FanDuel differs. Confirm what the site uses.
- Late scratches happen; the data is as of the last pull. Tell the user to recheck the injury list near tip-off.

## Default path (a slate of 4 to 10 games is 50 to 120 credits; ask before pulling more than 100)
1. **Slate.** Parse the pasted file; `get_schedule(days: 1)` (2 cr) for game ids, totals and spreads.
2. **Cost check.** `get_player_props(game_id, estimate_only: true)` (free) per game; give the user the total and let them trim the slate.
3. **Projections.** `get_prop_probabilities(game_id)` (10 cr per game): fair probabilities by line for points, rebounds, assists, threes, steals and blocks for every player; `get_player_props(game_id)` (10 cr) for the line numbers.
4. **Availability.** `get_injuries()` (2 cr): drop players listed out; flag day-to-day.
5. **Turnovers and no-line players.** `get_player_games(player_id, season, limit: 10)` (5 cr each, only for the players you are considering): turnovers per game and a fallback projection.

## Projection method
Projection per player, each stat from the market's median line:
- fantasy points = 1 x points + 0.5 x threes made + 1.25 x rebounds + 1.5 x assists + 2 x steals + 2 x blocks - 0.5 x turnovers (DraftKings-style; the user's site and scoring decide, so confirm), plus 1.5 for a double-double and 3 for a triple-double when the site pays them.
- Turnovers have no line: use the average of the last 10 games (n shown) and say so.
- Double-double and triple-double bonus: add the bonus only when the market posts a double-double line and its fair probability is above 0.5, scaled by that probability (bonus x probability); say it is approximate.
- Players with no line (deep bench, a player whose line is not up yet): last-10 average per minute times the minutes expected (average of the last 5 games, up only if a rotation player ahead is out), marked 'no market line'.
Lineup construction:
- Maximize the sum of projected points under the cap with the roster slots (exact solve with a short script if code is available; otherwise greedy by points per $1,000 then pairwise swaps, and say which).
- Show used salary, remaining salary and projected total; flag value plays as points per $1,000 against the slate median.
- Minutes sanity check: a projection above 40 minutes of production is a data issue; flag it.
- For several lineups, change one or two players and show the points given up for each change.

## Output template
```
Slate: <games>, cap <$>, scoring <site>
Lineup 1: salary <used>/<cap>, projected <pts>
PG ... | SG ... | SF ... | PF ... | C ... | G ... | F ... | UTIL ...
Value plays (points per $1,000): <name: x>, why: <teammate out / minutes up, n games>
Watch: <players day-to-day or no line>
Data: get_schedule, get_prop_probabilities, get_injuries, get_player_games | season <yyyy>
```

## When there is no game or no line
If there is no salary file, say lineups cannot be built and offer a projection table for named players. If lines are not posted yet (early in the day), project from the last-10 averages and mark the table provisional. If the slate has two games or fewer, say the pool is thin. On a no-game day, say so.

## Rules
- The salary file, the cap, the roster slots and the scoring system come from the user. If any is missing, ask for it; never use remembered salaries or prices.
- Build lineups under the cap the user gives. Do not advise on entry fees, which contest to enter or how much to play, and do not call any player a lock. Projections are estimates, not promises.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links. A prop line is used here only as the market's median projection of a player's stat.
- Ownership is not in the data. Use it only if the user pastes it, and say it came from them.

- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size and season convention.
- Do not add names, roles, injuries or storylines from memory; if a tool did not return it, leave it out.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.
