---
name: tennis-tournament-simulation
description: "Use when the user wants title or round chances for a tennis tournament from the draw, in fan or analyst wording: 'who wins the French Open', 'Sinner's chance to win Wimbledon', 'how deep is Gauff's section', 'who is in the toughest quarter', 'chance of an early upset', 'will a top seed go out in round one', 'simulate the Miami draw', 'odds to reach the semis', 'who wins the Slam', 'upset odds in round one', 'chance he goes deep'. Use this whenever a whole tournament or a player's path through it is the subject. Also use it for bare follow-ups with no name given, and load it instead of answering from memory or going straight to the raw tools. Simulates the draw with our surface Elo ratings, states the method and reports round-by-round probabilities. Not for one match (see tennis-match-preview), a head-to-head record (see tennis-head-to-head), a finished tournament's results (call get_tournament) or best surface for a player (see tennis-surface-form)."
metadata:
  version: 2.1.0
  author: SportsDataHQ
---

# Tennis tournament simulation

A bracket turns match probabilities into title chances, and draw luck matters. This skill simulates a tournament's draw from our Elo ratings, shows round-by-round probabilities and the toughest paths, and states exactly how it did it. It is our model, not the market's.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the AcesAPI MCP server (`https://mcp.acesapi.com/mcp`). Call them; never fill in a number from memory.
- Player ids from `search_players(name)` (1 cr); search the right tour. The ATP is the default; pass `league: "wta"` for women's matches. Season is the calendar year. There are no serve or return statistics in the data.
- Tournament ids look like "188-2025" (Wimbledon 2025), from `list_tournaments(season)` (1 cr). The draw must exist: `get_tournament` returns matches by round, with seeds. If the draw has not been published, say so and stop; do not make up a bracket.
- Ratings (`get_ratings`) are Elo from results, overall and by surface, for players with 10 or more rated matches. Players without a rating are a gap; say who was missing and what you did (exclude, or assume an average, stating it).
- Run the simulation with code execution or a short script if you have it. If you cannot run code, say so and give the draw and ratings only; do not write made-up probabilities.

## Default path (about 6 to 10 credits)
1. **Find the edition.** `list_tournaments(season)` (1 cr): id, surface and dates.
2. **The draw.** `get_tournament(tournament_id)` (2 cr): first-round pairings, seeds, and any results so far. If rounds are already played, keep their results fixed.
3. **Ratings.** `get_ratings(surface, limit: 500)` (2 cr): surface Elo for the field; add overall Elo from `get_ratings()` (2 cr) if blending.
4. **Simulate.** For a match, P(A wins) = 1 / (1 + 10^(-(Elo_A - Elo_B) / 400)), using the surface rating (or an equal blend of surface and overall, said so). Play every round at random 10,000 times or more, carrying winners forward.
5. **Report.** Probability of reaching each round and winning, the toughest quarter by average opponent rating, and the likeliest early upsets.

## Method statement (always include)
State: ratings are our Elo as of the latest rated match, the surface rating is used (or a stated blend), ratings do not change inside the simulation, best-of-five versus best-of-three is not modelled separately, injuries, withdrawals and fatigue are not modelled, and retirements are not simulated. The match formula assumes the usual 400-point Elo scale; check it against a recent rated match's pregame probability from `get_match` (2 cr) and report if it differs.

## Output template
```
<Tournament> <season> | <surface> | draw size <n> | simulations <k>
Method: surface Elo, 400-point logistic, ratings fixed, no injuries
Title: <player %> ...
Reach the final / semifinal: <player %> ...
Draw luck: <player: path difficulty, strongest likely opponents by round>
Upset watch (round 1): <match: underdog %>
Missing ratings: <names, how handled>
Data: list_tournaments, get_tournament, get_ratings | <tour>, <season>
```

## Rules
- Say "our simulation"; if prices are shown they are the market's, from `get_odds`, and never blended.
- Probabilities under 1% are shown as "under 1%".
- Keep played results fixed when the tournament is under way.
- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.

## Example prompts
- "Simulate the US Open men's draw"
- "What is Sinner's chance of reaching the Wimbledon final?"
- "How tough is Alcaraz's quarter?"
