---
name: mlb-player-props-research
description: "Use when the user asks about MLB player prop lines as information: 'Skenes strikeout line tonight', 'how often does Judge go over his total bases', 'compare hits lines across books', 'did his K prop move', 'what's the home run price for Ohtani', 'is the outs recorded line high for this starter'. Shows lines by sportsbook, the player's record against his line with sample size, the pitcher's or batter's recent workload and matchup context, and line movement. Covers strikeouts, outs, hits, home runs, total bases and RBI. Never says which side to take. Not for game previews (see mlb-game-preview), pitch-mix changes (see mlb-pitcher-skill-change) or general odds math (see odds-market-analysis)."
metadata:
  version: 2.2.0
  author: SportsDataHQ
---

# MLB player props research

A prop line is the market's estimate of one player's game. This skill lays it out and checks it against what the player did, with workload (pitch counts, innings, plate appearances) as the main context. It never recommends a side, a stake or a bet.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, enough data).
- Tools come from the FastballAPI MCP server. Lines move all day and starters get scratched; always call, never recall.
- Seasons are calendar years.

## Default path
1. **Resolve the player and game.** `search_players(name)` (1 cr); `get_schedule()` (2 cr) for the game and probable starters.
2. **Lines now.** `get_player_props(game_id, market)` (10 cr before first pitch, 20 after), or `player_id` with `from_date` for one player across games. Markets: `pitcher_strikeouts`, `pitcher_outs`, `batter_hits`, `batter_home_runs`, `batter_total_bases`, `batter_rbis`. Lines are held from May 2023.
3. **Track record.** `get_prop_history(player_id, market)` (10 cr per 25 games covered): closing line, what he recorded and over/under per game, plus the over rate.
4. **Workload.** `get_player_games(player_id, season)` (5 cr): for pitchers, innings, pitches and strikeouts per start; for batters, plate appearances and batting order spot. Short starts and low lineup spots explain most unders.
5. **Matchup (pitchers).** `get_pitch_mix(pitcher_id, season)` (5 cr) for arsenal and whiff rate, and the opponent's strikeout rate from `get_team_stats(team, season)` (5 cr).
6. **Movement (optional).** `get_prop_movement` (10 cr).

## How to report a record
- Hit rate = overs / (overs + unders); pushes excluded and counted.
- Pitchers: split by pitch count (90+ pitches vs fewer); a short outing is a different sample. Batters: split by lineup spot.
- Show n and the window ("over in 9 of 15 starts, 60%; 8 of 10 when he threw 90+ pitches").
- Below 10 games, say it's too small to mean much. A past hit rate is not a forecast.

## Output template
```
<Player> (<team>) | <market> | <game, date>
Lines now: <book: line (prices)> | consensus <line>
Against his line: over <a>/<a+b> (<%>), <p> pushes, <season> | 90+ pitches / top-of-order: <a'>/<n'> | last 5: <O/U>
Workload: <avg pitches or PA, last 5>; matchup: opponent K% <x>, his whiff% <y>
Data: search_players, get_player_props, get_prop_history, get_player_games, get_pitch_mix | season <yyyy>
```

## When no line is posted

Off-season, or the book hasn't posted yet: don't stop to ask. Give the player's record against his line over his last completed season (`get_prop_history` with that season's dates), his current form from game logs, and say lines aren't up yet. Never invent a line.

## The analyst layer

Go one step past the raw hit rate:
- **Across books:** the highest and lowest line or price on offer and the spread between them.
- **Over time:** the hit rate this season and last season separately, each with n.
- **Context split:** the same rate in the games that look like tonight's (minutes or workload for the player, home/away, favourite/underdog).
State each with its sample size; skip a split with fewer than 8 games and say why.

## Rules
- Information only: no picks, leans, "value", stakes, payouts or sportsbook links.
- Every number names its tool; every rate shows n.
- No line posted, or the starter is not confirmed: say so; don't borrow another game or market.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.