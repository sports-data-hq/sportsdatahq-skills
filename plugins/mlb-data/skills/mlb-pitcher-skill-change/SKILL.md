---
name: mlb-pitcher-skill-change
description: "Use when the user asks whether an MLB pitcher has changed, in fan or analyst wording: 'is Cole's heater down a tick', 'did Sale add a sinker', 'throwing more curveballs?', 'why are his Ks up', 'whiffs on the splitter', 'is he tipping pitches', 'lost velo or just tired', 'is the breakout real', 'did his four-seamer lose velo', 'why more strikeouts this year', 'injured or just fatigued'. Use this whenever a pitcher is named with velocity, pitch usage, whiffs, strikeouts or a slump. Also use it for bare follow-ups with no name given, and load it instead of answering from memory or going straight to the raw tools. Compares pitch usage, average and top velocity and whiff rate by pitch type across seasons or games, with pitch counts. Spin and movement are not in the data. Not for a game preview (see mlb-game-preview), league-wide luck (see mlb-regression-candidates), a hitter's batted balls (see mlb-batter-spray-profile) or the weekly schedule (see mlb-streaming-planner)."
metadata:
  version: 2.1.0
  author: SportsDataHQ
---

# MLB pitcher skill change

A pitcher's results can change for luck or for skill. Pitch-level changes (what he throws, how hard, how often it misses bats) are the evidence for skill. This skill compares them across seasons and across starts using FastballAPI pitch data.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the FastballAPI MCP server (`https://mcp.fastballapi.com/mcp`). Call them; never fill in a number from memory.
- `season` is the calendar year. Players by `search_players(name)` (1 cr). Pitch rows exist for about 98% of games in 2015-2017 and every game from 2018; check the season before comparing.
- `get_pitch_mix(pitcher_id, season)` returns each pitch type's usage, average and top velocity, whiff rate per swing and ball rate. `get_pitches(pitcher_id, season, pitch_type)` returns every pitch with count, type, velocity, location and result.
- Spin rate, movement and release point are not returned; do not discuss them.
- Velocity by game is computed from the pitch rows: average of `get_pitches` velocity per game. Say it was computed.

## Default path (about 25 credits)
1. **Resolve the pitcher.** `search_players(name)` (1 cr).
2. **Arsenal by season.** `get_pitch_mix(pitcher_id, season)` (5 cr) for this season and the one or two before: usage, average and top velocity, whiff rate per pitch type.
3. **Inside the season.** `get_pitches(pitcher_id, season, pitch_type)` (10 cr per page, up to 2,000 pitches): velocity and usage by game or month for the pitch in question, computed from the rows.
4. **Results.** `get_player(player_id)` (5 cr): strikeout and walk rates, ERA and WHIP by season, to connect pitch changes to outcomes.
5. **Injury check (optional).** `get_injuries(team)` (2 cr) if velocity dropped sharply.

## Reading the changes
A change counts when it shows in both seasons' totals and in more than a couple of starts. A velocity drop of about one mph or more on the main fastball held over several starts is worth saying out loud; a single cold-weather start is not. Usage shifts of several points mean a plan changed. Whiff rate per pitch needs swings: under about 100 swings on a pitch, say the rate is unstable. Early in a season, compare against the same pitcher's earlier seasons at the same point, since velocity rises through spring.

## Output template
```
<Pitcher, team> | <season> vs <season> | pitches <n>
By pitch type (usage % / avg velo / top velo / whiff %): <fastball, slider, changeup...> this year vs last
In-season trend for <pitch>: <velo by month or start, pitches counted> (computed from get_pitches)
Results: K% <v>, BB% <v>, ERA <v> vs last
Read: <what changed, whether it holds across starts, what the data cannot say>
Data: search_players, get_pitch_mix, get_pitches, get_player | seasons <yyyy>, <yyyy>
```

## Rules
- Do not explain a change with spin, movement or release point; they are not in the data.
- Say how many pitches or swings each figure rests on.
- Do not diagnose an injury; flag the velocity drop and the injury report separately.
- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.

## Example prompts
- "Did Skubal's fastball velocity drop this year?"
- "Is he throwing his slider more than last season?"
- "What is the whiff rate on his changeup?"
