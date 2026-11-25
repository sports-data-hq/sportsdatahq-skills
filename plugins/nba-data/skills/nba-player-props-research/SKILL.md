---
name: nba-player-props-research
description: "Use when the user asks about NBA or WNBA player prop lines as information: 'what's Luka's points line', 'how often does Jokic go over his rebounds', 'compare threes lines across books', 'how did his line move', 'what does the market imply for his PRA'. Shows lines by sportsbook, the player's record against his line with sample size and minutes context, movement and no-margin probability. Never says which side to take. Not for game previews (see nba-game-preview) or who absorbs minutes when a player sits (see nba-minutes-usage-redistribution)."
metadata:
  version: 2.0.0
  author: SportsDataHQ
---

# NBA player props research

Prop lines are the market's estimate of a player's night. This skill lays them out and checks them against what the player did, with minutes as the main context. It never recommends a side, a stake or a bet.

## Before you start
- Tools come from the DunkAPI MCP server. Lines move all day; always call, never recall.
- Markets: `player_points`, `player_rebounds`, `player_assists`, `player_threes`, `player_blocks`, `player_steals`, combos (`player_points_rebounds_assists` and others) and double/triple doubles; see the tool's `market` list.
- Player ids from `search_players(name)` (1 cr).

## Default path
1. **Resolve the player.** `search_players(name)` (1 cr).
2. **Current lines.** `get_player_props(game_id or player_id, market)` (10 cr): each book's line and prices, opening and closing.
3. **What the market implies.** `get_prop_probabilities(game_id, market, player_id)` (10 cr): average implied and no-margin over/under probability.
4. **Track record.** `get_prop_history(player_id, market)` (10 cr): line, result, over/under/push per game.
5. **Minutes context.** `get_player_games(player_id, season)` (5 cr): minutes and stats per game. Minutes explain most misses.
6. **Injuries (optional).** `get_injuries(team)` (2 cr): teammates out raise usage; the player's own status matters most.

## How to report a track record
- Hit rate = overs / (overs + unders); pushes excluded and counted.
- Split by minutes: games with 30+ minutes vs fewer. A low-minutes game (blowout, foul trouble) is a different sample.
- Show n and the window: "over in 11 of 18 (61%) this season; 9 of 12 in 30+ minute games".
- Below 10 games, say it's too small to mean much. A past hit rate is not a forecast.

## Output template
```
<Player> (<team>) | <market> | <game, date>
Lines now: <book: line (prices)> | consensus <line>
Market implies: over <x%> / under <y%> (no-margin)
Against his line: over <a>/<a+b> (<%>), <p> pushes, <season> | 30+ min: <a'>/<n'> | last 5: <O/U>
Minutes: <avg last 10>, <trend>; teammates out: <names>
Data: search_players, get_player_props, get_prop_probabilities, get_prop_history, get_player_games | season <yyyy>
```

## Rules
- Information only: no picks, leans, "value", stakes, payouts or sportsbook links.
- Every number names its tool; every rate shows n.
- No line posted yet: say so, don't borrow another market or game.
