---
name: mlb-batter-spray-profile
description: "Use when the user asks where or how an MLB hitter hits the ball, in fan or analyst wording: 'Tatis spray chart', 'does Seager go oppo', 'is he a pull hitter', 'too many ground balls?', 'fly ball guy?', 'where do his hits go', 'line drive rate for Freeman', 'batted ball mix'. Use this whenever a named hitter and batted-ball direction or type come up. Load it for short fragments and follow-ups too, even with no name given, instead of answering from memory or going straight to the raw tools. Reports balls in play by trajectory and by field (left, center, right) with hit rates and counts, for a season or the postseason. Not for a game preview (see mlb-game-preview), luck screens (see mlb-regression-candidates), a pitcher's pitch mix (see mlb-pitcher-skill-change), exit velocity leaders or prop prices."
metadata:
  version: 2.2.0
  author: SportsDataHQ
---

# MLB batter spray profile

Where a batter puts the ball in play, and what happens when he does. This skill reads FastballAPI's spray chart: balls in play by trajectory and by field, with hit rates and counts.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the FastballAPI MCP server (`https://mcp.fastballapi.com/mcp`). Call them; never fill in a number from memory.
- `season` is the calendar year. Batters from `search_players(name)` (1 cr).
- `get_spray_chart(batter_id, season, season_type)` (10 cr) returns balls in play by trajectory (ground ball, line drive, fly ball, pop-up) and by field (left, center, right), with hit rates. It counts the regular season and postseason together unless `season_type` is `regular` or `postseason`; `get_player`'s batting line is the regular season only, so pass `regular` when comparing the two.
- Fields are left, center and right field. Pull or opposite field needs the batter's handedness: use it only if a tool returns it, otherwise say "left field", not "pull".
- `include_balls: true` adds each ball's x/y (up to 3,000) for drawing; skip it unless a chart is asked for.
- Not available for college baseball. Exit velocity and launch angle are not described by the tool; do not discuss them.

## Default path (about 15 to 25 credits)
1. **Resolve the batter.** `search_players(name)` (1 cr).
2. **The chart.** `get_spray_chart(batter_id, season, season_type: "regular")` (10 cr): balls in play by trajectory and by field with hit rates.
3. **Compare.** The same call for the previous season (10 cr), or `season_type: "postseason"` if asked.
4. **Results and context (optional).** `get_player(player_id)` (5 cr) for the season batting line and handedness if returned; `get_plate_appearances(batter_id, season, result)` (10 cr per page) when the user wants specific outcomes, such as home runs.

## Reading it
A trajectory or field share on under 100 balls in play is unstable; say so. Hit rate by field depends on defenders and shifts we do not see. Compare a batter with himself across seasons before comparing him with others, and do not call a profile a skill change from one season.

## Output template
```
<Batter, team> | <season, season type> | balls in play <n>
Trajectory: ground ball <%> | line drive <%> | fly ball <%> | pop-up <%> (hit rate on each)
Field: left <%> | center <%> | right <%> (hit rate on each)
Vs <prior season>: <largest shifts, with balls in play>
Read: 2-3 bullets with sample sizes
Data: search_players, get_spray_chart[, get_player] | season <yyyy>, <season type>
```

## Rules
- Do not use pull or opposite-field wording unless handedness was returned.
- Say whether the chart is regular season, postseason or both.
- Do not discuss exit velocity, launch angle or shifts.
- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.

## Example prompts
- "Where does Aaron Judge hit the ball?"
- "Is Freddie Freeman a ground ball hitter?"
- "Spray chart for Shohei Ohtani in 2025"
