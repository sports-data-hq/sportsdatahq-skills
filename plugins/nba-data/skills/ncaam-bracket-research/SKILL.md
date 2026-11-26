---
name: ncaam-bracket-research
description: "Use when the user asks about the NCAA tournament, March Madness or a conference tournament field as information: 'tell me about the 12 seed in my bracket', 'how good is Gonzaga really', 'which teams are highest rated going into March', 'efficiency profile of the Sweet 16 teams', 'compare two teams in the first round', 'how did a team's season go', 'ratings for the women's tournament teams'. Builds team profiles from our Elo, net rating, pace, four factors, record and tournament results already played, men's or women's. It does not pick winners, fill brackets or advise pools; it lays out the evidence. Not for a single game preview (see ncaam-game-preview), player props (see ncaam-player-props-research), line movement (see nba-line-movement) or pro basketball."
metadata:
  version: 2.2.0
  author: SportsDataHQ
---

# College basketball bracket research

Profiles of the teams in a tournament or bracket question: how strong each is, how it plays and how it got there. The tools hold ratings, team stats, standings and game results for Division I men's (`ncaam`) and women's (`ncaaw`) basketball. Pass `league` on every call.

This skill gives information about teams. It does not choose winners, fill in a bracket, rank "upset picks" or give pool strategy. If asked for those, say the tools show the evidence and offer the profile instead.

## Before you start
- For anything across games, seasons or teams, apply the sports-data-preflight checks first (ids from lookups, the season convention, one league, enough data).
- Tools come from the DunkAPI MCP server. Call them; never fill in a number from memory.
- `season` is the year the season ends (2026 = 2025-26). The tournament is in the spring of that year; a question in November about "this March" means `season` is next calendar year and no games exist yet.
- **Seeds and bracket positions are not in the data.** There is no seed, region or bracket tool. If the user gives seeds or a bracket, use them as given and label them "your bracket"; never state a seed from memory. Show rating rank, which the data does hold.
- Postseason games carry `season_type: "postseason"` on `list_games`, which includes conference tournaments and the NCAA tournament; a game's `neutral_site` flag and `venue` help tell which. A round label is not provided, so describe games by date and opponent.

## Default path (about 10 credits plus 5 per team profiled)
1. **Strength across the field.** `get_ratings(season, league, limit)` (2 cr): our Elo, best first, with rank across every team the data holds. The list is the whole division, not the tournament field (the field is not in the data), so call it "the highest rated teams", never "the highest rated teams in the field". Each rating is as of that team's last game, so a deep run is already in it: for a team's strength going into the tournament, say the rating includes the tournament games and use `get_team_stats(before: <date>)` for point-in-time efficiency. 1500 is average; a 100-point gap is about a 64% favourite on a neutral floor.
2. **Each team named.** `get_team_stats(team, season, league)` (5 cr): games, record, pace, offensive, defensive and net rating per 100 possessions, the four factors, three-point rate and attempts per game.
3. **Standings and conference.** `get_standings(season, league)` (2 cr): record, conference record, home and away splits, average margin, last 10. Conference names can be null for some teams; say so.
4. **How the season went.** `list_games(team, season, league)` (2 cr): results with scores, to show close wins, losses and the postseason path. Note the number of games and who the neutral-site games were against.
5. **One team's style (optional).** `get_plays(team, season, shots_only: true, league)` (10 cr) only when the user asks where the team scores from; the `expected_points` field is NBA and WNBA only, so college shot locations show volume and make rate, not expected value.

## How to compare two teams
- Compare **net rating** and **Elo** together. If they disagree, say which one a team leads and why that might be (opponent strength, blowout margins).
- **Pace** tells which team controls possessions. A slow team against a fast team is a style gap, not a verdict.
- **Four factors:** where one side leads by a wide margin (eFG%, turnover %, offensive rebound %, free throw rate).
- **Three-point reliance:** high three-point rate with a low make rate is volatile. State both numbers and the attempts per game; a single-game outcome from such a team has a wide spread.
- **Single elimination is high variance.** A 100-point Elo gap is a 64% favourite on a neutral floor; a 200-point gap is about 76%. Quote the figure, and that the underdog wins the rest of the time.

## Output template
```
<TEAM> (<record>) | <conference> | rank <r> of <n> | Elo <n> | <men's / women's>
Efficiency: ORtg <x> / DRtg <x> / Net <x> over <g> games | pace <x> | eFG% <x> / opp eFG% <x>
Four factors: TOV% <x>, OREB% <x>, FT rate <x> | three-point rate <x>, make <x%>
Season path: <close results, postseason games played with dates and opponents>
Compared with <TEAM B>: <the 2-3 gaps that are large, with numbers>
Neutral-floor Elo gap: <n> points (about <x%> for the higher rated, not a prediction)
Data: get_ratings, get_team_stats, get_standings, list_games | league <ncaam/ncaaw>, season <yyyy>
```

## When the field isn't set

If no tournament games exist yet for that season, don't stop to ask. Give the highest-rated teams from `get_ratings` for the most recent complete season (or the current one with its games played shown) and say the field and seeds aren't in the data. Answer first; offer a profile of any team in one closing line.

## Rules
- Pass `league` on every call; a women's question answered with men's data is the commonest error.
- No seeds, no regions, no round labels from memory; the data does not hold them.
- No winner picks, no "sleeper" or "upset special" lists, no pool or bracket-filling advice, no odds-based recommendation. Market prices, if shown, come from `get_game_probabilities` and are labelled as the market's.
- Show games played beside every rate; under 10 games, say the ratings are early.
- Every number names its tool (the Data line, plus inline where it could be doubted).
- Sequences (last 5, recent form, a run of results, a series of line changes) are quoted in the order the tool returns them, with dates and times; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.
