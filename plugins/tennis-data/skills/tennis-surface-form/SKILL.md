---
name: tennis-surface-form
description: "Use when the user asks how a tennis player does on each surface, in fan or analyst wording: 'is Ruud a clay specialist', 'Djokovic on grass lately', 'how is she on hard courts', 'best clay player right now', 'is he any good indoors', 'surface record for Medvedev', 'grass court form', 'does he live on clay', 'her record on hardcourt', 'which surface suits him'. Use this whenever one player or a surface is the subject and no opponent is named. Also use it for bare follow-ups with no name given, and load it instead of answering from memory or going straight to the raw tools. Compares record, sets and tiebreaks and our Elo by surface and by season, with matches counted. Not for a match preview (see tennis-match-preview), two players' history (see tennis-head-to-head), a draw simulation (see tennis-tournament-simulation) or serve statistics such as aces, which are not held."
metadata:
  version: 2.0.0
  author: SportsDataHQ
---

# Tennis surface form

Surface matters in tennis, and small records mislead. This skill sets a player's results and our Elo by surface side by side, with matches counted, from AcesAPI.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the AcesAPI MCP server (`https://mcp.acesapi.com/mcp`). Call them; never fill in a number from memory.
- Seasons are calendar years (2025). ATP is the default; pass `league: "wta"` for the WTA. Players from `search_players(name)` (1 cr).
- `get_surface_splits(player_id, season, by_season)` (3 cr) returns wins, losses, win rate, sets, share of games won, tiebreaks, deciding sets and 6-0 sets by surface (hard, clay, grass, carpet), plus the current surface ratings. Surface comes from our tournament reference and is null where unknown.
- Ratings are ours (Elo from results, overall and per surface), not a ranking. Retirements count as wins and losses but are not rated; walkovers count nowhere.
- There are no serve statistics (aces, break points); do not discuss serve or return.

## Default path (about 10 to 20 credits)
1. **Resolve the player.** `search_players(name)` (1 cr).
2. **Career and recent splits.** `get_surface_splits(player_id)` (3 cr) for the career, then `get_surface_splits(player_id, season, by_season: true)` (3 cr) for the recent seasons.
3. **Rating by surface.** The splits carry the current surface ratings; for the field, `get_ratings(surface, limit)` (2 cr) to place him on that surface.
4. **Recent matches (optional).** `get_player_matches(player_id, surface, season)` (5 cr) for the actual results behind a surface, with opponents and rating before and after.
5. **Season context (optional).** `get_player_stats(player_id, season)` (3 cr) for record by round and opponent ranking.

## Reading it
A win rate on under 20 matches on a surface is thin; grass seasons are only a few weeks, so say so. Compare a player's surface rating with his overall rating before calling him a specialist, and check that a clay record is not just the draws he got (opponent ranking from `get_player_stats`). Do not extend a surface record to a tournament forecast.

## Output template
```
<Player> | <tour> | career and <season range>
By surface (matches, win rate, sets won %, tiebreaks, deciding sets): hard | clay | grass | carpet
Our Elo: overall <v> | hard <v> | clay <v> | grass <v> (rank on <surface>: <n> of <m>)
By season: <the surface that moved most and by how much, with matches>
Read: 2-3 bullets with matches counted, thin surfaces flagged
Data: search_players, get_surface_splits[, get_ratings, get_player_matches] | <tour>, <seasons>
```

## Rules
- Report matches beside every win rate; flag surfaces under 20 matches.
- Elo is ours and is not the official ranking.
- Do not discuss serve or return statistics.
- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links.

## Example prompts
- "Is Alcaraz better on clay or grass?"
- "Sinner surface splits for 2025"
- "Who is rated highest on grass right now?"
