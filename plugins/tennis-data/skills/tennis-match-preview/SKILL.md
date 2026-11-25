---
name: tennis-match-preview
description: "Use when the user wants a tennis match preview or matchup analysis for any ATP or WTA singles match: 'preview Sinner vs Alcaraz', 'break down tonight's tennis match', 'US Open quarterfinal preview', 'Wimbledon semifinal breakdown', 'how do they match up on grass', 'who wins Swiatek vs Gauff on clay', 'tennis matchup analysis'. Produces a one-page report: our surface Elo and pregame win probability, surface records, form, head to head with its caveat, and the market's prices. Not for rankings lists or full draws (call the tools directly) or modeling (see model-building)."
metadata:
  version: 2.0.0
  author: SportsDataHQ
---

# Tennis match preview

A one-page preview of one singles match from live AcesAPI calls. The ATP is the default; pass `league: "wta"` for women's matches.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the AcesAPI MCP server (`https://mcp.acesapi.com/mcp`). Call them; never recall a ranking or record.
- There are no serve or return statistics in the data (no aces, holds, breaks). Do not invent them; analyse from results, ratings and games won.
- Season is the calendar year. Player ids from `search_players(name)` (1 cr); search the right tour.

## Default path (about 17 credits)
1. **Find the match.** `get_schedule(days)` (2 cr): players, round, start time, and our pregame win probability (model elo-tennis-pregame: half overall Elo, half surface Elo).
2. **Ratings.** `get_ratings(surface)` (2 cr): both players' Elo on this surface and overall.
3. **Surface records.** `get_surface_splits(player_id)` (3 cr) for both: wins, losses, games won share, tiebreaks, deciding sets on this surface.
4. **Recent form.** `get_player_matches(player_id, season)` (5 cr) for both: last 10 results with opponents.
5. **Head to head.** `get_head_to_head(player_id, opponent_id)` (3 cr). Caveat: in large records rankings beat head-to-head in most cases; only lopsided records with many meetings carry signal.
6. **Prices (when held).** `get_odds(match_id)` (5 cr): moneylines for Grand Slam and Masters/1000 matches; empty elsewhere.

## Output template
```
<P1> (<rank>, Elo <overall>/<surface>) vs <P2> (...) | <tournament, round, surface> | <start>
Our pregame win probability: <P1 x%> / <P2 y%> (elo-tennis-pregame v1)
Market (when posted): <P1 implied %> / <P2 %>
Surface record: <P1 W-L, games won %> | <P2 ...>
Form (last 10): <P1 W-L, notable wins> | <P2 ...>
Head to head: <a-b> (<on this surface>), with the caveat
What to watch: 2-3 bullets from the numbers
Data: get_schedule, get_ratings, get_surface_splits, get_player_matches, get_head_to_head | <tour>, <season>
```

## Rules
- Say "our model" for the probability and "the market" for prices; never blend them.
- Retirements count as results but are not rated; walkovers count nowhere. Mention them when they distort a record.
- Odds are information only: no pick, stake or bet.
