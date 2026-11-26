---
name: ncaam-game-preview
description: "Use when the user wants a preview of one college basketball game, men's or women's (any university or school team, not the NBA): 'preview Duke vs UNC', 'break down tonight's Kansas game', 'what's the line on Gonzaga', 'how good is South Carolina women's team tonight', 'who has the edge in the Illinois game', 'is tonight's Houston game a mismatch', 'is this a mismatch', 'women's hoops preview UConn vs Texas'. Produces a one-page report: records, our Elo, pace and efficiency, the four factors, venue and neutral-site flag, and the market line with its no-margin probability. College has no injury report in these tools, so it says so instead of guessing. Not for NBA or WNBA previews (see nba-game-preview), tournament or bracket research across many teams (see ncaam-bracket-research), player props (see ncaam-player-props-research), line movement (see nba-line-movement) or football."
metadata:
  version: 2.2.0
  author: SportsDataHQ
---

# College basketball game preview

A one-page preview of a single Division I game from live DunkAPI calls. Men's games use `league: "ncaam"`, women's use `league: "ncaaw"`. Pass it on every call; the default is the NBA.

## Before you start
- For anything across games, seasons or teams, apply the sports-data-preflight checks first (ids from lookups, the season convention, one league, enough data).
- Tools come from the DunkAPI MCP server. Call them; never fill in a number from memory.
- `season` is the year the season ends (2027 = 2026-27). Early in November a team has played two or three games, so say how few.
- Teams accept abbreviations; `list_teams(league)` (1 cr) if unsure. Many schools share a mascot name or a city, so confirm the school from the `team` field before using an id.
- No injury report: `get_injuries` covers the NBA and WNBA only. State "no injury data for college in these tools" and do not infer absences from a box score or a headline.

## Default path (about 16 credits)
1. **Find the game.** `get_schedule(team, league)` (2 cr): game id, tip time, venue, neutral-site and conference flags, and the median line across books. For a past game use `list_games(team, season, status: "final", league)` (2 cr).
2. **Team efficiency.** `get_team_stats(team, season, league)` (5 cr) once per team: games played, pace, offensive, defensive and net rating per 100 possessions, the four factors (eFG%, turnover %, offensive rebound %, free throw rate), three-point rate. Pass `before: <date>` for point-in-time numbers on a past game.
3. **Strength.** `get_ratings(season, league)` (2 cr): our Elo for both teams and the national rank out of the field. A 100-point gap is about a 64% favourite on a neutral floor; add home advantage for a true home game.
4. **What the market implies.** `get_game_probabilities(game_id, league)` (5 cr): average implied and no-margin win probability, spread and total. The market's view, not ours.
5. **After the game (optional).** `get_game(game_id, league)` (5 cr): team box score, players, and every book's closing line.

## How to read the numbers
- **Schedule strength matters more here than in the pros.** A 6-0 start against low-rated teams is not a 6-0 start against ranked ones. Use the Elo rating and the rank, not the record, to compare the two sides, and say which opponents the record was built against only if you pulled them.
- **Early-season ratings regress a quarter of the way to the mean between seasons.** Before about 10 games they lean on last year's team, so rosters that turned over (transfers) will be off. Say so for any team with under 10 games.
- **Neutral site:** if `neutral_site` is true, drop home advantage when you compare the Elo gap with the line.
- **Gap between our Elo and the market:** show both as separate numbers and label the market's as the market's. A gap is information, not a pick.

## Output template
```
<AWAY> (<record>) at <HOME> (<record>) | <date, tip ET> | <venue>, <neutral / home> | <men's / women's>
Line: <spread> / total <total> | Market: <home no-margin win %> | Elo: <away> <n> (rank <r>) vs <home> <n> (rank <r>)
Pace: <away> vs <home> possessions per 40 (games played <g> each)
Efficiency: ORtg / DRtg / Net for both
Four factors edge: where one team clearly leads (eFG%, TOV%, OREB%, FT rate)
Injuries: no injury data for college in these tools
What to watch: 2-4 bullets tied to the numbers
Data: get_schedule, get_team_stats, get_ratings, get_game_probabilities | league <ncaam/ncaaw>, season <yyyy>
```

## When there's no game

If the game the user names isn't scheduled (off-season, not booked, already played), don't stop to ask. Do the most useful real version and say which one in the first line:
1. The next scheduled meeting of those two sides, if `get_schedule` (filtered by team) has one.
2. Otherwise their most recent meeting and where each side finished last season, from the last completed season's data.
3. For a matchup that can't happen soon, the ratings matchup labelled as hypothetical.
Answer first; offer the alternative in one closing line, never as a question before answering.

## Rules
- Pass `league` on every call; a women's question answered with men's data is the commonest error.
- Rates need a sample: show games played. Under 10 games, say the ratings are early.
- No prop lines exist for women's college basketball; if asked, say so.
- Every number names its tool (the Data line, plus inline where it could be doubted).
- Odds are information about the market: no side, no stake, no bet.
- Sequences (last 5, recent form, a run of results, a series of line changes) are quoted in the order the tool returns them, with dates and times; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.
