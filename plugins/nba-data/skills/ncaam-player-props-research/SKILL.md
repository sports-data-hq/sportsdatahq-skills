---
name: ncaam-player-props-research
description: "Use when the user asks about men's college basketball player prop lines or how a player did against his line: 'Boozer points line', 'how many rebounds is Dybantsa set at', 'did the Flagg points number move', 'has he cleared 18 lately', 'who has the best line on the Kansas guard', 'college prop history for Johni Broome'. Shows each book's line and price, the player's record against his line with sample size and minutes, movement and no-margin probability, for men's Division I only. Never says which side to take. Women's college basketball has no prop market in these tools and it says so. Not for game previews (see ncaam-game-preview), NBA or WNBA props (see nba-player-props-research), bracket research (see ncaam-bracket-research) or building a model."
metadata:
  version: 2.2.0
  author: SportsDataHQ
---

# College basketball player props research

Prop lines are the market's estimate of a player's night. This skill lays them out for men's Division I basketball (`league: "ncaam"`) and checks them against what the player did, with minutes as the main context. It never recommends a side, a stake or a bet.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the DunkAPI MCP server. Lines move all day; always call, never recall. Pass `league: "ncaam"` on every call.
- Coverage: men's college prop lines start with the 2023-24 season and cover only the games the data holds; women's college basketball has no prop market. A smaller school's game may have no props at all; say "no prop lines for this game" and stop rather than borrowing another game.
- `season` is the year the season ends (2027 = 2026-27). Player ids from `search_players(name, league)` (1 cr); many college players share names, so confirm school and class before using an id.
- Markets are the points, rebounds, assists, threes, blocks and steals families and combos; the `market` list on the tool is the authority.

## Default path
1. **Resolve the player.** `search_players(name, league: "ncaam")` (1 cr).
2. **Current lines.** `get_player_props(game_id or player_id, market, league)` (10 cr): each book's line and prices, opening and closing.
3. **What the market implies.** `get_prop_probabilities(game_id, market, player_id, league)` (10 cr): average implied and no-margin over/under probability.
4. **Track record.** `get_prop_history(player_id, market, league)` (10 cr): line, result, over/under/push per game.
5. **Minutes context.** `get_player_games(player_id, season, league)` (5 cr): minutes and stats per game. College minutes swing with blowouts, foul trouble and short benches.
6. **Movement (optional).** `get_prop_movement(game_id, player_id, market, league)` (10 cr).
7. **The base rate (optional).** `get_prop_backtest(market, ..., league: "ncaam")` (25 cr) for how often a kind of prop hit. Report its sample size, interval and per-season split, and never present a past rate as a pick.

There is no injury report for college in these tools. If a teammate's absence matters, say it cannot be checked here.

## How to report a track record
- Hit rate = overs / (overs + unders); pushes excluded and counted.
- Split by minutes: games with 30+ minutes vs fewer. A game with 18 minutes in a blowout is a different sample.
- Show n and the window: "over in 9 of 15 (60%) this season; 7 of 9 in 30+ minute games".
- Below 10 games, say it is too small to mean much. Freshmen and transfers in November often have under 8 games; say that. A past hit rate is not a forecast.

## Output template
```
<Player> (<school>) | <market> | <game, date> | men's college
Lines now: <book: line (prices)> | consensus <line>
Market implies: over <x%> / under <y%> (no-margin)
Against his line: over <a>/<a+b> (<%>), <p> pushes, <season> | 30+ min: <a'>/<n'> | last 5: <O/U with dates>
Minutes: <avg last 10>, <trend>; teammate status: not available for college
Data: search_players, get_player_props, get_prop_probabilities, get_prop_history, get_player_games | league ncaam, season <yyyy>
```

## When no line is posted

Early in the day, a small-school game, or the book hasn't posted: don't stop to ask. Give the player's record against his line over his last completed season (`get_prop_history` with that season's dates), his current form from game logs, and say lines aren't up. Never invent a line.

## The analyst layer

Go one step past the raw hit rate:
- **Across books:** the highest and lowest line or price on offer and the spread between them.
- **Over time:** the hit rate this season and last season separately, each with n.
- **Context split:** the same rate in games that look like tonight's (minutes, home/away, favourite/underdog).
State each with its sample size; skip a split with fewer than 8 games and say why.

## Rules
- Information only: no picks, leans, "value", stakes, payouts, "sharp money" claims or sportsbook links. If the user asks what to bet, say this skill shows the market and offer the data instead.
- Every number names its tool ; every rate shows n.
- Women's college basketball: no props. Say so and offer a game preview instead.
- Sequences (last 5, recent form, a run of results, a series of line changes) are quoted in the order the tool returns them, with dates and times; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.
