---
name: mlb-regression-candidates
description: "Use when the user asks whether MLB numbers are real, lucky or due to change, in fan or analyst wording: 'is his hot start fake', 'will .340 hold', 'buy low guys', 'who is due to come back down', 'overperforming his BABIP', 'is that ERA a mirage', 'sell high now?', 'fluky first month'. Use this whenever results are being questioned against underlying rates. Load it for short fragments and follow-ups too, even with no name given, instead of answering from memory or going straight to the raw tools. Compares results against steadier rates (BABIP computed from plate appearances, strikeout and walk rates, home runs per plate appearance) with sample sizes. Not for a pitcher's pitch-level changes (see mlb-pitcher-skill-change), game previews (see mlb-game-preview), where a hitter hits it (see mlb-batter-spray-profile) or the weekly schedule (see mlb-streaming-planner)."
metadata:
  version: 2.0.0
  author: SportsDataHQ
---

# MLB regression candidates

Results move faster than skills. This skill flags hitters and pitchers whose results sit far from the rates that stabilise sooner, using only fields FastballAPI returns, and says what each flag does and does not show.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the FastballAPI MCP server (`https://mcp.fastballapi.com/mcp`). Call them; never fill in a number from memory.
- `season` is the calendar year. Teams accept abbreviations (`list_teams`, 1 cr); players by `search_players(name)` (1 cr).
- The API does not return xwOBA, exit velocity, launch angle or FIP. Do not quote them. Plate appearances carry the result, the batted-ball trajectory and location, run value and our win probability; the metrics below are computed from those and labelled as computed.
- Leaders are qualified players (3.1 plate appearances per team game, or 1 inning per team game for pitchers); `min_pa` and `min_ip` override the floor.
- Batting average on balls in play (BABIP) is computed here as (hits - home runs) / (at-bats - strikeouts - home runs + sacrifice flies) from the plate-appearance results. State the formula and that it was computed.

## Default path (about 25 to 45 credits)
1. **Build the pool.** `get_leaders(stat: "avg" or "ops" or "era" or "whip", season, limit, min_pa or min_ip)` (5 cr per stat): the extremes by results.
2. **Steadier rates.** `get_leaders(stat: "k_pct")` and `get_leaders(stat: "bb_pct")` (5 cr each) for hitters, and `k_per_9`, `bb_per_9` for pitchers, to see whether the underlying skill matches the result.
3. **Player lines.** `get_player(player_id)` (5 cr): season-by-season batting and pitching, so a career baseline is visible.
4. **BABIP and home-run rate.** `get_plate_appearances(batter_id or pitcher_id, season)` (10 cr per page): count results and batted balls and compute BABIP and home runs per plate appearance. Paginate with `offset`.
5. **Context.** Compare to the player's own prior seasons from step 3, not to a league figure you recall.

## What counts as a flag
A hitter is a regression candidate when his results are well above his own multi-season level while strikeout and walk rates are unchanged and BABIP is far above his career figure. A pitcher is one when ERA is well below what his strikeout, walk and home-run rates and his BABIP against would imply. Say which rate each flag leans on. A high BABIP is not always luck: speed and contact quality hold some of it, so compare with the player's own history first. Early in a season (under about 150 plate appearances for a hitter, 40 innings for a pitcher) say the sample is too small to flag anyone.

## Output template
```
<Player, team> | <season> | PA <n> or IP <n>
Result: <AVG/OPS or ERA/WHIP> vs own prior seasons: <values>
Underlying: K% <v>, BB% <v>, home runs per PA <v> | BABIP (computed) <v> vs career <v>
Flag: <what moves back and which rate says so> or "no flag, rates support the result"
Data: get_leaders, get_player, get_plate_appearances | season <yyyy> (BABIP and home-run rate computed from plate appearances)
```

## Rules
- Never cite xwOBA, FIP, exit velocity or launch angle; say they are not in the data if asked.
- Name every computed metric as computed and give its formula.
- Regression means a likely drift, not a prediction of a number.
- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links.

## Example prompts
- "Which hitters are getting lucky this season?"
- "Is his .340 average sustainable?"
- "Whose ERA is out of line with his strikeout and walk rates?"
