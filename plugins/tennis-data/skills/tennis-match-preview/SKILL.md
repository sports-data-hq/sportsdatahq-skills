---
name: tennis-match-preview
description: "Use when the user asks about a specific tennis match, in fan or analyst wording: 'Sinner vs Zverev tonight', 'break down tonight's match', 'who is favored in the final', 'how do they match up on grass', 'how does Rybakina match up with Sabalenka', 'preview the semi', 'will Fritz upset him', 'who wins this one', 'is the underdog live'. Use this whenever two players are named together for an upcoming or live match, even with no tournament given. Also use it for bare follow-ups with no name given, and load it instead of answering from memory or going straight to the raw tools. Produces a one-page report: our surface Elo and pregame win probability, surface records, form, head to head with its caveat and the market's prices. Not for only a head-to-head record (see tennis-head-to-head), one player's surface split (see tennis-surface-form), title chances (see tennis-tournament-simulation), rankings or modeling."
metadata:
  version: 2.1.0
  author: SportsDataHQ
---

# Tennis match preview

A one-page preview of one singles match from live AcesAPI calls. The ATP is the default; pass `league: "wta"` for women's matches. It goes past the ranking to what an analyst checks: surface Elo, how each player wins games, tiebreak and deciding-set record, who the player has beaten, workload and layoffs, and what the head to head says on this surface.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the AcesAPI MCP server (`https://mcp.acesapi.com/mcp`). Call them; never recall a ranking or record.
- There are no serve or return statistics in the data (no aces, holds, breaks, first-serve percentage). Do not invent them. The proxies below are counted from scores, and the answer should say they are proxies.
- Season is the calendar year. Player ids from `search_players(name)` (1 cr); search the right tour. Scores are written winner first ("7-6(2) 6-4"; the bracket is the loser's tiebreak points).
- Surface comes from our tournament reference and can be null. Retirements count as results but are not rated; walkovers count nowhere.

## Default path (about 34 credits)
1. **Find the match.** `get_schedule(days, league)` (2 cr): players, round, surface, start time, seeds and our pregame win probability (`win_prob`, model elo-tennis-pregame v1: half overall Elo, half surface Elo). Note the match and tournament ids.
2. **Ratings.** `get_ratings(surface, limit: 200, league)` (2 cr): both players' Elo on this surface; call it again without `surface` (2 cr) for overall, or read the overall and surface ratings from `get_surface_splits`. Note `last_match`.
3. **Surface records and how they win.** `get_surface_splits(player_id, season)` (3 cr each): wins, losses, games won, tiebreaks, deciding sets and 6-0 sets on this surface, for the season and, if the season is young, career.
4. **Opposition quality.** `get_player_stats(player_id, season)` (3 cr each): record by round and by opponent ranking (top 10, 11-50, 51-100).
5. **Recent form and workload.** `get_player_matches(player_id, limit: 10)` (5 cr each): dates, rounds, scores, opponents and rating before and after.
6. **Head to head.** `get_head_to_head(player_id, opponent_id)` (3 cr): wins each, by surface, in finals, every meeting with its score (in `matches`).
7. **Prices (when held).** `get_odds(match_id)` (5 cr): moneylines for Grand Slam matches from mid-2020 and ATP Masters and WTA 1000 matches from August 2024; empty elsewhere.

## Method
- **Probability from ratings:** p = 1 / (1 + 10^(-d / 400)), with d = 0.5 x overall gap + 0.5 x surface gap. The served `win_prob` wins any disagreement; use the formula for a hypothetical and to explain the number. Elo does not know the format: a favourite wins more often in best-of-five (men's Grand Slams) than in best-of-three, so say which applies.
- **Surface specialist:** surface Elo minus overall Elo. A gap of 60 or more either way says the player is better or worse on this surface than the overall rating shows. Under 30 surface matches behind the rating is thin.
- **Game dominance (serve and return proxy):** games won share = games won / (games won + games lost) on this surface. Above 60% over 20 or more matches is dominant. It is a blend of serve and return; say it is not a serve statistic.
- **Tiebreak profile:** tiebreak rate = tiebreaks / sets played (higher means serve-dominated sets); tiebreak record = won / (won + lost). Under 20 tiebreaks the record is noise; do not call it a skill.
- **Deciding sets:** record in deciding sets and the share of matches that went the distance (a proxy for fitness and clutch). Under 10 deciding sets it is anecdote.
- **Opposition quality:** record against the top 10 and 11 to 50 from `get_player_stats`. A high win rate against 51-100 opponents says little about a top-10 match. Under 5 matches in a band: not rated.
- **Fatigue and schedule:** days since the last match, matches in the last 14 days, sets and games in the last 7 days, and whether the last match went the distance. A layoff of 60 or more days is a rust and injury question (first matches back are less reliable; Elo is not decayed for inactivity); 8 or more matches in the last 17 days is heavy; say these are workload counts, not fitness readings.
- **Head to head:** by surface and recency. Under 5 meetings is weak; rankings and Elo beat head to head in most cases, and only lopsided records with many meetings carry signal. A player who lost the last meeting on this surface is a data point to quote, not a trend.
- **Market:** American price a: negative |a|/(|a|+100), positive 100/(a+100); no-margin per book = pA/(pA+pB); average the books. Compare with `win_prob` in points; 8 or more is worth one line (information only).

## Output template
```
<P1> (<rank>, Elo <overall>/<surface>) vs <P2> (...) | <tournament, round, surface, best of n> | <start>
Our pregame win probability: <P1 x%> / <P2 y%> (elo-tennis-pregame v1) | Market (when posted): <P1 %> / <P2 %> (<n> books)
Surface record (<season>): <P1 W-L, games won %, TB W-L, deciding sets> | <P2 ...>
Against the top 10 / 11-50: <P1> | <P2>
Workload: <days since last match, matches in 14 days, last match length> for each
Form (last 10, newest first): <P1 results with dates> | <P2 ...>
Head to head: <a-b> (<on this surface>, last meeting with score), with the caveat
What to watch: 2-3 bullets from the numbers
Data: get_schedule, get_ratings, get_surface_splits, get_player_stats, get_player_matches, get_head_to_head | <tour>, <season>
```

## Worked example (live calls, Nov 25, 2026; hypothetical, see below)
No ATP match was scheduled in the next 30 days (`get_schedule` returned none), so this is Sinner vs Alcaraz on hard courts, labelled hypothetical.
- Ratings: overall Sinner 2407, Alcaraz 2331 (gap 76); hard Sinner 2367, Alcaraz 2265 (gap 102). Blended gap 89 gives 62.5% Sinner (formula, not a served number).
- Hard 2026: Sinner 19-2, games won 62.2%, tiebreaks 7-1; Alcaraz 41-4, games won 59.4%, tiebreaks 20-8. Alcaraz's hard sets went to a tiebreak 25% of the time against 16% for Sinner. Sinner's sample is 21 hard matches against Alcaraz's 45.
- Workload: Alcaraz last played Nov 22 (won the Finals, three days ago) and had 8 matches since Nov 6, a heavy run. Sinner's last match was the Wimbledon final on Jul 12, 136 days ago: a rust question with no recent hard-court data.
- Head to head (`get_head_to_head`): Alcaraz leads 10-7 over 17 meetings, 7-3 on hard; Sinner won the most recent one, the Monte-Carlo final on Apr 12, 2026, 7-6(5) 6-3. Seventeen meetings is a real sample, but Elo already includes those results.
Verdict wording: "Elo makes Sinner about a 62% favourite on hard courts, Alcaraz has the better recent hard-court volume and the head-to-head lead; Sinner's layoff is the swing."

## Not enough data
- Under 20 matches on the surface in the season: use the career surface record and say which.
- Under 20 tiebreaks or 10 deciding sets: no skill claim from the record.
- Under 5 head-to-head meetings, or none on this surface: say so and lean on Elo.
- Under 5 matches against a ranking band: the band is not rated.
- A player returning from 60 or more days off, or with `last_match` more than a year ago: say the rating is stale; if a player is missing from `get_ratings`, he has under 10 rated matches or has not played in the window.
- No prices: odds exist only for Grand Slam and Masters/1000 matches in the periods above; say none are held.
- Qualifying and walkovers: counted differently; mention when they distort a record.

## When there's no match

If the two players aren't drawn to meet, don't stop to ask. Preview the matchup as it would play on the surface of the next event both are entered in (or the surface asked about): head to head, surface Elo, recent form and the workload, labelled hypothetical, with the probability computed from the formula and named as such. If a match between them is scheduled, use that. If the tour is between seasons, say so in the first line.

## Rules
- Say "our model" for the probability and "the market" for prices; never blend them. Never name a book.
- Retirements count as results but are not rated; walkovers count nowhere. Mention them when they distort a record.
- Odds are information only: no pick, stake or bet. Avoid betting idioms such as "better bet" or "safe"; say "more likely".
- Complete before writing: every step in the default path is called for both sides before the preview is written. If a call fails or returns nothing, say which section is missing rather than writing around it.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Rate limit: a "rate limit exceeded" reply is not a credit refusal. Wait a few seconds and retry that call once, one call at a time; if it still fails, name the section that is missing.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.
