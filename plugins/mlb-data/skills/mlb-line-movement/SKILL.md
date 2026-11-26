---
name: mlb-line-movement
description: "Use when the user asks how an MLB moneyline, run line or total moved before first pitch, in fan wording: 'how did the Dodgers line move', 'did the total drop for Yankees Red Sox', 'opening vs closing line for tonight', 'did the price change when the starter was announced', 'which book moved first', 'what are the alt run lines', 'line history for the Braves game'. Lays out snapshots by sportsbook, opening against closing, the size and timing of moves, and alternate run-line and total ladders, as information. Never says which side to take or reads who is betting. Not for player prop movement (see mlb-player-props-research), game previews (see mlb-game-preview), or fantasy and DFS questions."
metadata:
  version: 2.2.0
  author: SportsDataHQ
---

# MLB line movement

How an MLB game's moneyline, run line and total changed before first pitch, by sportsbook, and what the alternate-line ladders look like. Information about the market only. College baseball uses `league: "ncaabase"`, but alternate ladders cover MLB only; the default league is `mlb`.

## Before you start
- For anything across games, seasons or books, apply the sports-data-preflight checks first (ids from lookups, the season convention, one league, enough data).
- Tools come from the FastballAPI MCP server. Lines move all day; always call, never recall.
- Seasons are calendar years (2026). In the off-season there are no games to look at; say so and offer the last completed season's games instead.
- Snapshots are our pre-game captures: once a day, and hourly for games in the next four days. By default a capture identical to the one before it is dropped (the latest is always kept), so a long gap means the line did not move. Pre-game only.
- **Baseball moneylines carry the story.** The run line is almost always 1.5, so a run-line move often shows up as a price change (-110 to -125), not a points change. Report the price, not just the line.

## Default path (about 12 credits)
1. **Find the game.** `get_schedule(team, league)` (2 cr) for the game id and the median line, or `get_games(team, date, league)` (2 cr) for a past game.
2. **The movement.** `get_line_movement(game_id, league)` (10 cr): each sportsbook's snapshots with `captured_at`, moneyline, run line and total. Pass `provider` for one book. Use `all_snapshots: true` only when every hourly capture is needed.
3. **Opening and closing, all books.** `get_odds(game_id, league)` (5 cr): each book's opening and closing line.
4. **Alt-line ladders (when asked).** `get_alt_lines(game_id, market, snapshot_type, league: "mlb")` (10 cr): every point on each book's alternate run-line or total ladder with its price, from the 2023 season on.
5. **Starters (optional).** `get_game(game_id)` (5 cr) shows the listed starting pitchers; a late starter change often sits near a moneyline move, so line the two up by time and say "coincided with".
6. **First five innings (optional, MLB only).** `get_market_odds(game_id, market)` (10 cr): first-5 and first-inning lines as history.

## How to read a move
- **Moneyline:** move in cents. Home -140 to -165 is a change in implied probability; convert only through the tool's `*_prob` fields and say a book's implied probability includes its margin.
- **Total:** a half-run move is meaningful; a full run is large. Total moves in baseball often come with price changes on the over and under, so show both.
- **Timing:** list the capture times the move happened between. Starters are announced late in the day before; wind and roof status arrive on game day. A step at one capture differs from a drift.
- **Across books:** books moving on the same captures point to a shared repricing; one book alone, then the others, is a lead and follow. The data holds prices, not who bet, so "sharp" or "public" money cannot be claimed.
- **Steam vs drift (descriptions only):** steam is a fast move across several books within one or two captures; drift is slow. Label by the captures, with times.
- **Alt ladders:** show rows (point, price) per book around the main line; games before Nov 12 2026 have one capture shortly before the start, so opening and closing ladders match.
- **Why:** the data does not say. Use "coincided with" for a starter change or injury (`get_injuries`, MLB, 2 cr), never "caused by".

## Output template
```
<AWAY> at <HOME> | <date, first pitch ET> | <starters if known>
Open to close: home ML <open> to <close> | run line <line and price open> to <close> | total <open> to <close> (<over/under price>)
By book: <book: open -> close>, <n> books
Timeline: <captured_at: what changed>, in order returned
Pattern: <step / drift / books moved together or one lead and follow>, with the capture times
Alt ladder (closing): <book: points and prices around the main line>
Context: <starter or injury change with time, "coincided with">
Data: get_schedule, get_line_movement, get_odds, get_alt_lines | season <yyyy>
```

## Rules
- Information only: no picks, leans, "value", stakes, payouts, "sharp money" claims or sportsbook links. If the user asks what to bet, say this skill shows the market and offer the data instead.
- Two sources of "opening": the opening line from `get_odds` is the book's own first posted line, and the first snapshot in `get_line_movement` is our first capture, which can be later and different. Label which one a figure comes from, never mix them in one column, and say when a book's first capture is already after it moved.
- Describe what moved and when; do not explain why or what a bettor should do with it.
- No posted line or too few captures: say how many snapshots exist and stop; don't borrow another game.
- Every number names its tool (the Data line, plus inline where it could be doubted).
- Sequences (last 5, recent form, a run of results, a series of line changes) are quoted in the order the tool returns them, with dates and times; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.
