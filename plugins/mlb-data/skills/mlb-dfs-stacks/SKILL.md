---
name: mlb-dfs-stacks
description: "Use when someone has an MLB daily fantasy slate: 'build my MLB DraftKings lineup', 'best stacks tonight', 'which team has the highest implied total', 'who do I pair with this pitcher', 'one-off hitters to fill out the stack', 'cheap pitcher plays', '5-3 stack', 'Coors stack', 'salary file for tonight, make a lineup'. Ranks teams by the market's implied run total, projects hitters and starting pitchers from prop medians in fantasy points and builds lineups under the cap from the user's salary file. Also for bare follow-ups with no names: load this skill first, then ask for what is missing, rather than answering from memory. Not for entry fees, contest choice or how much to play, which it will not advise; not for a week of pitching matchups (see mlb-streaming-planner), season-long waivers (see mlb-fantasy-waivers) or prop research."
metadata:
  version: 1.0.0
  author: SportsDataHQ
---

# MLB DFS stacks and lineup builder

MLB DFS is stack-driven: runs come in clusters, so hitters from one lineup share an outcome. Team choice starts with the market's expected runs for each side. This skill derives the implied team totals, projects each hitter and starter from the market's medians, and builds under the cap. Batting orders and probable pitchers are not in the data, so they come from the user's file.

## Before you start
- For anything across games, seasons or players, apply the sports-data-preflight checks first (ids from search, the season convention, one league, enough data).
- Tools come from the FastballAPI MCP server. `season` is the calendar year. Player ids come from `search_players(name)` (1 cr).
- Required from the user: the salary file with positions and, if available, batting order and the opposing starter; the cap, the roster slots and the scoring (DraftKings classic is usually 2 P, C, 1B, 2B, 3B, SS, 3 OF at 50,000). Confirm what the site uses.
- Batting orders and probable pitchers are not in the data. Never state a lineup spot or a starter unless the user's file or message gives it; ask them to paste lineups once posted.
- Park factors and weather are not in the data; do not quote them.

## Default path (a slate of 6 to 12 games is 80 to 200 credits; ask before pulling more than 100)
1. **The slate.** `get_schedule(days: 1)` (2 cr): games, the median total, moneylines and run line.
2. **Cost check.** `get_player_props(game_id, estimate_only: true)` (free) per game; let the user trim.
3. **Team totals.** Derived from the schedule (no extra call): see the method.
4. **Hitter and pitcher lines.** `get_player_props(game_id)` (10 cr per game): hits, home runs, total bases, RBI, pitcher strikeouts and pitcher outs for every player posted.
5. **Skill context.** `get_player(player_id, season)` (5 cr) for a starter's WHIP and a hitter's walk rate, and `get_player_games(player_id, season, limit: 20)` (5 cr) for runs and walks per game, only for players you are considering; `get_injuries(team)` (2 cr).

## Projection method
Implied team totals (derive, do not look up):
- Take the median moneylines from `get_schedule`, convert each to implied probability, divide by their sum to remove the margin (fair win probability p for the home side).
- Expected margin = 10 x (p - 0.5) runs (rule of thumb: about 10 percentage points of win probability per run; say it is approximate).
- Home team total = total / 2 + margin / 2; away team total = total / 2 - margin / 2. Rank teams by implied total. Say these are the market's numbers, not ours.
Hitter points (DraftKings-style: single 3, double 5, triple 8, home run 10, RBI 2, run 2, walk 2, stolen base 5; confirm the site):
- points = 3 x H + 2 x (TB - H) + 1 x HR + 2 x RBI + 2 x (R + BB), using the median line for hits (H), total bases (TB), home runs (HR) and RBI. The total-bases term gives a single 3, double 5 and home run 9, plus 1 for the HR; triples are rare and ignored.
- R + BB per game: average of the last 20 games (n shown), since there is no line for them; stolen bases are left out and said so.
- Hitters with no line (not posted for most lineup spots 6 to 9): estimate from lineup-spot plate appearances only if the user gave the order; otherwise mark 'no line' and exclude from the optimizer unless the user wants them.
Starting pitcher points (DraftKings-style: out 0.75, strikeout 2, win 4, earned run -2, hit or walk allowed -0.6):
- 0.75 x outs line + 2 x strikeouts line - 2 x ER - 0.6 x (hits + walks allowed).
- ER = opponent implied team total x outs / 27 (the starter's share of innings; bullpen runs excluded); hits + walks = season WHIP x outs / 3.
- Win points are left out of the number; report the team's fair win probability beside it.
Lineup construction:
- Fix the stack first: the user's requested shape (for example 5-3, 4-2-2) from the top implied totals, taking hitters adjacent in the batting order where the user gave it, and a pitcher not facing the stacked team. Then fill remaining slots to maximize projected points under the cap (exact solve with a short script, or greedy then pairwise swaps; say which).
- Show used salary, remaining salary, projected total. Correlation is a structural choice, not something measured here.

## Output template
```
Slate: <games>, cap <$>, scoring <site>
Implied totals (market): <team: runs> top 6
Lineup 1: salary <used>/<cap>, projected <pts>
P <name> $<s> <pts> (opp implied <r>, win prob <p>) | P ... | C ... | 1B ... | ... | OF x3
Stack: <team> x<n> (order: <as given by you / not given>)
No line / excluded: <names>
Data: get_schedule, get_player_props, get_player, get_player_games, get_injuries | season <yyyy>
```

## When there is no game or no line
If there is no salary file, say lineups cannot be built and offer the implied-total ranking and projections for named players. If props are not posted yet, rank teams by implied total only and say hitters are not projected. If a game has no total, skip the team. On a no-game day or the offseason, say so.

## Rules
- The salary file, the cap, the roster slots and the scoring system come from the user. If any is missing, ask for it; never use remembered salaries or prices.
- Build lineups under the cap the user gives. Do not advise on entry fees, which contest to enter or how much to play, and do not call any player a lock. Projections are estimates, not promises.
- Odds and prices are information about the market only: no picks, leans, stakes, payouts or sportsbook links. A prop line is used here only as the market's median projection of a player's stat.
- Ownership is not in the data. Use it only if the user pastes it, and say it came from them.

- Every number names its tool (the Data line, plus inline where it could be doubted) and every rate shows its sample size and season convention.
- Do not add names, roles, injuries or storylines from memory; if a tool did not return it, leave it out.
- If a tool returns too little, say "not enough data" and stop; do not estimate or borrow another sample.
- Sequences (last 5, recent form, a run of results) are quoted in the order the tool returns them, with dates; never retell them from memory. Lists in the answer must match the tool rows.
- Out of credits: if a call is refused for credits, pass on the API's message as it comes (it says when free credits refill and how to add more), and stop; don't retry or switch tools to get around it.
