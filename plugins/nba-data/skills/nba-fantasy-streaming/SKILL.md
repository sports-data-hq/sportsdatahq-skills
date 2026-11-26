---
name: nba-fantasy-streaming
description: "Use when a fantasy basketball manager is planning a week or a pickup: 'who do I stream tonight', 'which teams play four games this week', 'back-to-backs this week', 'best waiver adds with the injury', 'who gets the minutes now', 'light slate tonight', 'pickup for rebounds and assists', 'fill my open spot', 'streamer for the weekend'. Also for bare follow-ups with no names: load this skill first, then ask for what is missing, rather than answering from memory. Builds the week from games per team, back-to-backs, opponent pace and defense, injuries and each candidate's recent minutes and per-minute production. Not for one team's minutes shift when a named star sits (see nba-minutes-usage-redistribution), DFS salary lineups (see nba-dfs-lineup), trades or prop lines (see nba-player-props-research)."
metadata:
  version: 1.0.0
  author: SportsDataHQ
---

# NBA fantasy streaming and schedule planner

Fantasy basketball is mostly a volume game: more games, more minutes. Streaming picks are decided by games played that week, who is playing a back-to-back, whether the opponent is fast and porous, and whether a teammate's injury raised the candidate's minutes. This skill lays that out for the week and ranks the candidates the user names or the data surfaces.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the DunkAPI MCP server. `season` is the year the season ends (2026 = 2025-26). Player ids come from `search_players(name)` (1 cr).
- League category or points scoring comes from the user; if unstated, report per-game counting stats and say the ranking is not category-specific.
- Who is available (roster percentage) and rest decisions are not in the data. Ask the user to paste the free-agent names; otherwise list who is trending and say availability is unchecked.
- Teams rest players on back-to-backs; the injury report is the only availability source here.

## Default path (about 30 to 60 credits)
1. **The week.** `get_schedule(days: 7)` (2 cr): count games per team, mark back-to-backs (consecutive dates), home or away, and the median total as the market's expected pace of scoring.
2. **Opponents.** `get_team_stats(season)` (5 cr): pace, offensive and defensive rating per 100 possessions for the teams on the schedule.
3. **Injuries.** `get_injuries()` (2 cr, or per team): who is out or day-to-day on the teams involved.
4. **Candidates.** `search_players(name)` (1 cr), then `get_player_games(player_id, season, limit: 10)` (5 cr each): minutes, points, rebounds, assists, threes, steals, blocks, turnovers for the last 10 games.
5. **Role change (optional).** `get_leaders(stat, season)` (5 cr) to find who produces per game on a team missing a starter.

## Projection method
- Games: candidates are ranked first by games in the window. A 4-game player beats a 3-game player of similar per-game value; show the games.
- Per-game level = average over the last 10 games of the user's stats (n shown). Per-minute = that divided by average minutes; projected level = per-minute x expected minutes, where expected minutes = average of the last 5 games, adjusted up only when a rotation player ahead of him is Out (use the games he has already missed this season if the log shows them, with n; otherwise say the minutes bump is unconfirmed).
- Weekly value = games x projected level. Show the arithmetic.
- Matchup adjustment is light: note a high-pace opponent (more possessions) or a poor defensive rating as a plus and say it moves a stat line a few percent at most. Do not scale the numbers by it.
- Back-to-backs: flag the risk of rest for veterans and of a minutes cut in the second game; say that the data cannot predict a rest day.
- Under 5 games of the new role: mark the minutes as unconfirmed.

## Output template
```
Week of <date> | games per team: <team: n (B2B, home/away)>
Candidates (last 10 games, n shown):
1. <player> (<team>): <g> games | <min>/gm | <stats per gm> | weekly <games x level>
2. ...
Injuries driving it: <player: status> -> <who inherits minutes, evidence n>
Opponent pace / defense: <team: pace, def rating>
Availability: <checked against your list / unchecked>
Data: get_schedule, get_team_stats, get_injuries, get_player_games | season <yyyy>
```

## When there is no game or no line
If the schedule shows a light slate (few or no games), say it and rank on games in the next 7 days instead. In the offseason there are no games to stream; offer last season's role-based list and say it is stale. Under 5 games played for a candidate, call it 'not enough data'.

## Rules
- Fantasy rankings and advice only: no betting language. A prop line is used here only as the market's median projection of a player's stat.
- The user's scoring and roster settings come from the user; if unstated, say which default you used and show the formula so they can swap it.

- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size and season convention.
- Do not add names, roles, injuries or storylines from memory; if a tool did not return it, leave it out.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.
