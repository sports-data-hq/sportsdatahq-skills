---
name: mlb-fantasy-waivers
description: "Use when a fantasy baseball manager is looking for pickups or deciding on a drop: 'best hitters on the wire', 'who is getting everyday at-bats', 'call-up worth adding', 'is his hot streak real', 'drop candidate', 'platoon bat available', 'who is hitting leadoff now', 'catcher or shortstop to add', 'pitcher to stash'. Ranks players by plate appearances per game over the last two weeks, quality of contact and strikeouts, role and injury status. Also for bare follow-ups with no names: load this skill first, then ask for what is missing, rather than answering from memory. Not for starting-pitcher streaming around a schedule (see mlb-streaming-planner), luck screens (see mlb-regression-candidates), pitch changes (see mlb-pitcher-skill-change), DFS lineups or trades. Cannot see roster percentage."
metadata:
  version: 1.0.0
  author: SportsDataHQ
---

# MLB fantasy waiver report

Waivers in baseball are won on playing time first: a hitter with four plate appearances a game and a decent bat beats a better bat who sits against lefties. This skill ranks the user's candidates by plate appearances, then by quality, and flags small samples.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the FastballAPI MCP server. `season` is the calendar year. Player ids come from `search_players(name)` (1 cr).
- Roster percentage and who is available are not in the data. Ask the user for the names or their free-agent list; otherwise report league-wide risers and say availability is unchecked.
- Probable starters and batting orders are not in the data; lineup spot comes from the game logs only (when a player has batted at the top, say so from the logs).
- Saves and holds are not tracked; relief roles cannot be ranked.

## Default path (about 30 to 60 credits)
1. **Find risers.** `get_leaders(stat: ops, season, min_pa: 40, limit: 40)` (5 cr) and `get_leaders(stat: re24 ...)` (5 cr) give season quality; for pitchers `get_leaders(stat: k_per_9, min_ip: 20)` (5 cr).
2. **Candidates' games.** `get_player_games(player_id, season, limit: 15)` (5 cr each), for the user's names or the top 5 to 8 of the lists: plate appearances and batting lines per game, newest first.
3. **Quality of contact (top 3).** `get_plate_appearances(batter_id, season, limit: 100)` (10 cr): results and batted ball types over the last games.
4. **Health.** `get_injuries(team)` (2 cr).
5. **Schedule.** `get_schedule(team, days: 7)` (2 cr): games the player's team has this week.

## Projection method
- Playing time first: plate appearances per team game over the last 14 days (n games shown). Under 3.2 per game is a part-time role; 4.0 or more is an everyday spot. A player who has not started 4 of the last 5 team games is part-time unless injured.
- Role evidence: games started, the batting positions in the log, and whether he sat against particular opponents (the log shows the opponent; do not state handedness unless the tool gives it).
- Quality: OPS and strikeout rate over the last 14 days and for the season; show both and flag a sample under 40 plate appearances. A hot two weeks on 45 plate appearances is noise; a role change plus a steady bat is signal.
- Contact: share of balls in play that were line drives or fly balls over the last 100 plate appearances from `get_plate_appearances`, if pulled, as a tiebreak only.
- Rank: playing time, then season quality, then the recent change; list drop candidates among the user's players using the same test.
- Pitchers: report innings per start and strikeouts per 9 over the last 5 starts; do not name who starts next week.

## Output template
```
Waiver report (<season>)
1. <player> (<team>, <pos>): PA/gm <x> over last <n> gms | last-14 OPS <a>, season OPS <b> (PA <p>) | K% <k> | role: <started x of last y>
2. ...
Drop candidates among yours: <player: why>
Health: <player: status>
Team games this week: <team: n>
Availability: <checked / unchecked>
Data: get_leaders, get_player_games, get_plate_appearances, get_injuries, get_schedule | season <yyyy>
```

## When there is no game or no line
Early in the season (under 20 team games) say samples are small and lean on last season's role. If a player has played fewer than 5 games recently, say not enough data. In the offseason, rank on last season's final-month role and say there is no current game log.

## Rules
- Fantasy rankings and advice only: no betting language. A prop line is used here only as the market's median projection of a player's stat.
- The user's scoring and roster settings come from the user; if unstated, say which default you used and show the formula so they can swap it.

- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size and season convention.
- Do not add names, roles, injuries or storylines from memory; if a tool did not return it, leave it out.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.
