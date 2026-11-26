---
name: tennis-head-to-head
description: "Use when the user asks about two tennis players' record against each other, in fan or analyst wording: 'Federer vs Murray record', 'who has the edge in the rivalry', 'how often have they met', 'has Gauff ever beaten Swiatek', 'their record on hard', 'do they split sets', 'lifetime head to head', 'does he own him'. Use this whenever two players and their past meetings come up. Load it for short fragments and follow-ups too, even with no name given, instead of answering from memory or going straight to the raw tools. Shows the record, by surface and round, every meeting's score, and sets it against current ratings and rankings with the caveat that ratings usually beat head-to-head. Not for a full match preview or prediction (see tennis-match-preview), a draw simulation (see tennis-tournament-simulation), one player's surface record (see tennis-surface-form) or rankings lists (call get_rankings)."
metadata:
  version: 2.0.0
  author: SportsDataHQ
---

# Tennis head to head

Head-to-head records are the favourite talking point and a weak predictor. This skill reports the record accurately, decides whether it can carry any signal, and puts it next to ratings, which usually matter more.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the AcesAPI MCP server (`https://mcp.acesapi.com/mcp`). Call them; never fill in a number from memory.
- Player ids from `search_players(name)` (1 cr); search the right tour. The ATP is the default; pass `league: "wta"` for women's matches. Season is the calendar year. There are no serve or return statistics in the data.
- Walkovers are listed but not counted as wins; incomplete records are not counted. Retirements count as results.

## Default path (about 15 credits)
1. **Resolve both players.** `search_players(name)` (1 cr each).
2. **The record.** `get_head_to_head(player_id, opponent_id)` (3 cr): wins each, sets won, wins by surface and in finals, and every meeting with its score and date.
3. **Current strength.** `get_ratings(surface)` (2 cr): both players' Elo overall and on the surface of interest, and `get_rankings()` (2 cr) for current ranks.
4. **Surface form (optional).** `get_surface_splits(player_id)` (3 cr) for each player on the surface at hand.

## When a head to head means something
In most large records, rankings and ratings predict the next meeting better than the head-to-head does. Only a lopsided record with many meetings carries signal of its own, for example 8-1 or better over 9 or more matches, and even then it is a reason to look at style and age, not a forecast. Give the record, then say plainly which of three cases it is: too few meetings (under 5) to mean anything; many meetings but close, so ratings should lead; or lopsided with many meetings, so it adds some signal. Also flag when the meetings are old (more than 3 years) or all on another surface.

## Output template
```
<P1> vs <P2> | head to head <a>-<b> in <n> meetings | last meeting <date, score, surface>
By surface: hard <a>-<b> | clay <a>-<b> | grass <a>-<b> | finals <a>-<b>
Current strength: Elo <P1 overall/surface> vs <P2 ...> | rank <r> vs <r>
Is the record informative? <too few / close, ratings lead / lopsided with many meetings> because <numbers>
Data: search_players, get_head_to_head, get_ratings, get_rankings | <tour>, <season>
```

## Rules
- Say the record's size and age every time.
- Never present the head to head as a prediction; the ratings are the baseline, and our model's pregame probability lives in tennis-match-preview.
- Retirements and walkovers: mention them when they distort a record.
- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.

## Example prompts
- "Sinner vs Alcaraz head to head"
- "Has Djokovic ever beaten Alcaraz on clay?"
- "Is the Swiatek vs Gauff record meaningful?"
