---
name: nba-minutes-usage-redistribution
description: "Use when an NBA or WNBA player is out or limited and the user asks who benefits: 'Embiid is out, who gets the minutes', 'who starts if Tatum sits', 'how did the Knicks do without Brunson', 'usage bump with the starter out', 'how does usage change without Luka', 'fantasy pickup with the injury'. Compares minutes, shots and usage per teammate in games the player missed against games he played, with sample sizes. Not for prop lines (see nba-player-props-research) or a game preview (see nba-game-preview)."
metadata:
  version: 2.1.0
  author: SportsDataHQ
---

# NBA minutes and usage redistribution

When a player sits, his minutes and shots go somewhere. The best evidence is what actually happened in the games he already missed this season. This skill builds that comparison.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the DunkAPI MCP server. `season` is the year the season ends (2026 = 2025-26).
- Player ids from `search_players(name)` (1 cr).

## Default path (one team, about 30 credits)
1. **Who's out.** `get_injuries(team)` (2 cr): status and expected return.
2. **His games.** `get_player_games(player_id, season)` (5 cr): which games he played and missed (team games minus his games).
3. **The team's games.** `list_games(season, team)` (2 cr): every game id and date, so you can split "with" and "without".
4. **Teammates' logs.** `get_player_games(player_id, season)` (5 cr each), one call per teammate, for the 4-6 players most likely affected (same position, the next starters).
5. **Shot share (optional).** `get_plays(game_id, shots_only: true)` (10 cr) on a few "without" games for field goal attempts per teammate.

## Method
- For each teammate: minutes, points, field goal attempts and assists per game **with** vs **without** the player. Usage proxy = (FGA + 0.44 x FTA + TOV) per minute; true usage needs team totals, so call it a proxy.
- Show n for both sides: "without Embiid: 9 games; with: 14".
- Under 4 "without" games, the comparison is anecdotal; say so and fall back to the rotation (who starts, who's next at his position).
- Starters' minutes also depend on blowouts and back-to-backs; mention outliers.

## Output template
```
<Team> without <player> (<season>): <n_without> games without, <n_with> with
<teammate>: minutes <with> -> <without> (<+/->), FGA <with> -> <without>, pts <with> -> <without>
...
Biggest beneficiaries: <names> (evidence: <n_without> games)
Likely starter: <name> (from recent lineups / position)
Data: get_injuries, get_player_games, list_games | season <yyyy>
```

## Rules
- Every rate has its game count. Tiny samples are flagged, not dressed up.
- Name the tool behind each number.
- Fantasy and usage only: no betting language.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.