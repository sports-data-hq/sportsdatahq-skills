---
name: nba-shot-quality
description: "Use when the user wants to know how good a player's or team's shots are in the NBA or WNBA: 'is Curry's shot selection good', 'how many corner threes does Boston take', 'is he over-performing his shot quality', 'shot chart for Haliburton', 'where does Denver allow shots from', 'expected points per shot'. Reports attempts, makes and expected points per shot by zone, so shooting results can be set against shot location. NBA and WNBA only (college shots carry no expected points). Not for prop lines (see nba-player-props-research), game previews (see nba-game-preview) or pace and efficiency (see nba-pace-efficiency-matchup)."
metadata:
  version: 2.1.0
  author: SportsDataHQ
---

# NBA shot quality

Shot results are noisy; shot locations are steadier. This skill compares what a player or team shot with what the shots were worth by location, from DunkAPI's located shots and our expected-points model.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the DunkAPI MCP server (`https://mcp.dunkapi.com/mcp`). Call them; never fill in a number from memory.
- `season` is named by the year it ends (2025 = 2024-25); WNBA seasons are calendar years. Player ids from `search_players(name)` (1 cr); teams accept abbreviations.
- `expected_points` is our model's value of a shot from its location and type, fitted on every shot in the league's history. It is served for the NBA and WNBA only (also NBL on this tool); college shots carry locations but no expected points yet, so say that and stop for a college request.
- Court coordinates are in feet: x 0-50 across the court, y from the basket at (25, 0).
- `get_shot_chart` takes `player_id`, `team`, `opponent: true` (the shots a team's defence allowed), `game_id`, `season` and `season_type`. Set `include_shots: true` only when you need individual shots to draw a chart.

## Default path (about 10 credits per shot profile)
1. **Resolve ids.** `search_players(name)` (1 cr) or a team abbreviation.
2. **Shot profile.** `get_shot_chart(player_id, season)` (10 cr): attempts, makes, percentage, points per shot and expected points per shot in each zone (restricted area, paint, midrange, corner three, above-the-break three, free throws).
3. **Compare.** For a team's offence `get_shot_chart(team, season)` (10 cr); for its defence add `opponent: true` (10 cr). For a league baseline, call the tool for a representative comparison the user names; do not invent a league average.
4. **One game (optional).** `get_shot_chart(game_id, player_id)` (10 cr).
5. **Draw it (optional).** Repeat with `include_shots: true` and hand the x/y rows to the visualization skill.

## Shot quality versus shot making
Shot quality is expected points per shot from the locations taken. Shot making is points per shot minus expected points per shot. A positive gap on a small sample is mostly luck; show attempts per zone and call a zone with under 50 attempts too thin. Expected points do not see defenders, the passer or shot clock, so a player taking only open looks and a player creating his own shots are not comparable on this number alone.

## Output template
```
<Player or team> | <league, season, season type> | attempts <n>
Shot quality: expected points per shot <v> | actual points per shot <v> | gap <v>
By zone (attempts, FG%, expected points per shot, actual): restricted area | paint | midrange | corner 3 | above-break 3 | free throws
Where the gap comes from: <zones with the largest gap and their attempts>
Read: 2-3 bullets with sample sizes (zones under 50 attempts flagged)
Data: search_players, get_shot_chart | <league>, season <yyyy>
```

## Rules
- NBA and WNBA only for expected points; say so for college requests.
- Report attempts beside every percentage.
- A single season's over- or under-performance against expected points is mostly noise; say how many shots it rests on.
- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.

## Example prompts
- "Is Steph Curry shooting better than his shot quality this season?"
- "Where does Denver allow shots from?"
- "How many corner threes do the Celtics take?"
