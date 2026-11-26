---
name: mlb-win-prob-swings
description: "Use when the user wants to know what decided a played MLB game, in fan or analyst wording: 'what flipped last night's game', 'the big moment in Game 7', 'key at-bat of the night', 'who was the hero', 'how did they come back', 'biggest play of the series', 'show me the win probability graph', 'when was it over', 'the biggest momentum shift', 'win probability graph of the game', 'when did they actually win it', 'the play that changed it'. Use this whenever a finished game's turning points are the subject. Also use it for bare follow-ups with no name given, and load it instead of answering from memory or going straight to the raw tools. Orders a game's plate appearances by change in our home win probability and run value, with the base-out state. Not for a game preview (see mlb-game-preview), pitch trends (see mlb-pitcher-skill-change), luck screens (see mlb-regression-candidates), batted-ball profiles (see mlb-batter-spray-profile) or line movement."
metadata:
  version: 2.0.0
  author: SportsDataHQ
---

# MLB win probability swings

A box score says who won; the plate-appearance log says when. This skill ranks one game's plate appearances by how far they moved our win probability.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the FastballAPI MCP server (`https://mcp.fastballapi.com/mcp`). Call them; never fill in a number from memory.
- `season` is the calendar year. Game ids from `get_games(date or team, season)` (2 cr) or `get_schedule` (2 cr).
- `get_plate_appearances(game_id)` (10 cr) returns the game in order with the base-out state before, the result, runs, the home team's win probability after the plate appearance (our model: inning, outs, runners, score, team ratings and the two starters) and our run value (RE24). Up to 1,000 rows a page.
- Win probability is the home team's. A swing is the change from the previous plate appearance's value to this one's, computed here; the first plate appearance has no prior value in the rows, so do not compute its swing. Say the swings are computed.
- Not available for college baseball (no win probability). Leverage index is not returned; do not name it.

## Default path (about 10 to 20 credits)
1. **Find the game.** `get_games(...)` (2 cr) for the game id.
2. **Pull it.** `get_plate_appearances(game_id)` (10 cr); page with `offset` if rows are cut.
3. **Compute swings.** For each plate appearance: win probability after minus the previous row's. Express from the winner's side. Rank by absolute swing.
4. **Name the turning points.** The top 3 to 5 swings with inning, outs, runners, score, batter, pitcher and result as returned, plus the largest RE24 plays for comparison.
5. **Context (optional).** `get_game(game_id)` (5 cr) for the box score and final score.

## Reading it
Win probability comes from a model, so a swing is the model's reading, not a fact about effort or clutch. Late-game swings are larger because fewer outs remain; compare plays within the game, not across games. Do not rank players as clutch from one game.

## Output template
```
<Away> at <Home> | <date> | final <score> | plate appearances read <n>
Biggest swings (winner's side): 1) <inning, outs, runners, score, batter vs pitcher, result>: <before> to <after> (<swing>), RE24 <v>
  2) ...  3) ...
When the game turned: <the stretch where the favourite changed, if it did>
Read: 2-3 bullets, swings stated as computed from get_plate_appearances
Data: get_games, get_plate_appearances[, get_game] | season <yyyy>, game <id>
```

## Rules
- Say win probability is the home team's and is our model's.
- Do not call anyone clutch from one game.
- Do not mention leverage index; it is not returned.
- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.

## Example prompts
- "What was the biggest swing in the Dodgers game last night?"
- "Turning point of Game 7"
- "Win probability chart for the Cubs game"
