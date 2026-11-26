---
name: nba-line-movement
description: "Use when the user asks how an NBA, WNBA or college basketball spread, total or moneyline moved, in fan wording: 'how did the Lakers line move', 'did the total drop', 'opening vs closing line for Celtics Knicks', 'which book moved first', 'what are the alt spreads', 'did the spread shift after the injury news', 'line history for tonight'. Lays out snapshots by sportsbook, opening against closing, the size and direction of each move, whether books moved together or one drifted alone, and the alt-line ladder. Explains moves as information about the market and never says which side to take or what it means for a bet. Not for player prop movement (see nba-player-props-research), game previews (see nba-game-preview) or odds math in general (see odds-market-analysis)."
metadata:
  version: 2.2.0
  author: SportsDataHQ
---

# NBA line movement

How a game's spread, total and moneyline changed before tip-off, by sportsbook, and what the alternate-line ladders look like. Information about the market only. Basketball means the NBA unless the user names the WNBA (`wnba`), men's or women's college (`ncaam`, `ncaaw`) or the NBL (`nbl`); pass `league` on every call.

## Before you start
- For anything across games, seasons or books, apply the sports-data-preflight checks first (ids from lookups, the season convention, one league, enough data).
- Tools come from the DunkAPI MCP server. Lines move all day; always call, never recall.
- Snapshots are our pre-game captures: once a day, and hourly for games in the next four days. By default a capture identical to the one before it is dropped (the latest is always kept), so a long gap means the line did not move, not that data is missing. Pre-game only; nothing after tip-off.
- `season` is the year the season ends (2027 = 2026-27). Alt-line coverage: the NBA, WNBA and men's college from 2023-24 (not women's college).

## Default path (about 12 credits)
1. **Find the game.** `get_schedule(team, league)` (2 cr) for the game id, or `list_games(team, date, league)` (2 cr) for a past one.
2. **The movement.** `get_line_movement(game_id, league)` (10 cr): each sportsbook's snapshots with `captured_at`, moneyline, spread and total. Pass `provider` for one book. Use `all_snapshots: true` only when the user needs every hourly capture.
3. **Opening and closing, all books.** `get_odds(game_id, league)` (5 cr): each book's opening and closing line, for a clean before and after.
4. **Alt-line ladders (when asked).** `get_alt_lines(game_id, market, snapshot_type, league)` (10 cr): every point on each book's alternate spread or total ladder with price, closing by default, `opening` for the first. For the main line use `get_odds`.
5. **Period lines (NBA, optional).** `get_market_odds(game_id, market)` (10 cr): first half, first quarter and quarter-total lines as history, opening and closing by book.

## How to read a move
- **Size:** closing minus opening, in points for a spread or total. A half-point is small; two or more is a large move for a pro game. Say the numbers, not just "big".
- **Direction:** a spread move toward the favourite means the favourite became more expensive; say "the home spread went from -3.5 to -5.5", not "money came in".
- **Timing:** list the capture times the move happened between. A move at one capture after hours of quiet is a step; many small moves are a drift.
- **Across books:** books that moved together on the same capture times point to one cause that all of them priced; one book alone moving and then the others following is the pattern usually called a lead and follow. Describe the timing you can see and never assert who bet what: the data holds prices, not who placed bets, so "sharp" or "public" money cannot be read from it.
- **Steam vs drift (descriptions only):** steam is a fast move of a full point or more across several books within one or two captures; drift is a slow change over many captures. Label by what the captures show, with the times.
- **Price vs line:** a spread can stay at -4.5 while the price goes from -110 to -120. Report both the line and the price, since the implied probability moved even though the line did not.
- **Moneyline moves** are in American odds; convert to implied probability only through the tool's `*_prob` fields, and say a book's implied probability includes its margin.
- **Reasons:** an injury, rest or lineup report may have preceded a move, but the data does not say why. If an injury report exists (`get_injuries`, NBA and WNBA only, 2 cr), line it up in time and say "coincided with", never "caused by". College has no injury data in these tools.
- **Alt ladders:** show the ladder as rows (point, price) per book and where books differ at the same point. Games before Nov 12 2026 have one capture shortly before the start, so opening and closing ladders are the same; say so.

## Output template
```
<AWAY> at <HOME> | <date, tip> | <league>
Open to close: spread <home open> to <home close> (<+/- x>) | total <open> to <close> (<+/- x>) | home ML <open> to <close>
By book: <book: open -> close for spread and total>, <n> books
Timeline: <captured_at: what changed>, in order returned
Pattern: <step / drift / books moved together or one lead and follow>, with the capture times
Alt ladder (closing): <book: points and prices around the main line>
Context: <injury report entries with times, NBA and WNBA only, "coincided with">
Data: get_schedule, get_line_movement, get_odds, get_alt_lines | league <x>, season <yyyy>
```

## Rules
- Information only: no picks, leans, "value", stakes, payouts, "sharp money" claims or sportsbook links. If the user asks what to bet, say this skill shows the market and offer the data instead.
- Two sources of "opening": the opening line from `get_odds` is the book's own first posted line, and the first snapshot in `get_line_movement` is our first capture, which can be later and different. Label which one a figure comes from, never mix them in one column, and say when a book's first capture is already after it moved.
- Describe what moved and when; do not explain why a move happened or what a bettor should do with it.
- If the game has too few captures (a game more than four days away has one a day), say how many snapshots exist.
- Not enough data: a game with no posted line has no movement; say so and don't borrow another game.
- Every number names its tool (the Data line, plus inline where it could be doubted).
- Sequences (last 5, recent form, a run of results, a series of line changes) are quoted in the order the tool returns them, with dates and times; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.
