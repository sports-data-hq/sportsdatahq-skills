# Changelog

What changed in the SportsDataHQ skills, newest first. Every sport's own repo carries the same skills, synced from here.

## 2.1.1 (2026-11-26)

Fewer, sharper skills: 83, down from 89. Each one was kept only if it fires on the questions it's for and does something the plain tool calls don't.
- Removed `nhl-game-lookup`, `nhl-team-analysis`, `nl-to-query` and `sports-skill-router`: finding games, reading standings and routing questions are things Claude already does well with the tools.
- `nhl-goalie-analysis` is now part of `nhl-goalie-gsax-report` (workload, back-to-backs, rolling form, tandems), and `ufc-finish-profile` is part of `ufc-fighter-profile`.
- `nhl-advanced-stats` explains the metrics; `golf-tournament-preview` leaves single-player course history to `golf-course-history`; `cricket-venue-effects` answers "what's par here" and "does the toss matter".

## 2.1.0 (2026-11-26)

**Fantasy and DFS: 13 new skills.** Built on usage, injuries, depth charts, schedules and the market's per-player lines as projections; anything we don't hold (salaries, ADP, ownership, FPL prices) you paste in.
- NFL: `nfl-fantasy-start-sit`, `nfl-fantasy-waivers`, `nfl-fantasy-draft-board`, `nfl-fantasy-trade-value`, `nfl-dfs-lineup`.
- NBA: `nba-fantasy-streaming`, `nba-dfs-lineup`. MLB: `mlb-dfs-stacks`, `mlb-fantasy-waivers`. NHL: `nhl-fantasy-streamers`, `nhl-dfs-lineup`.
- Soccer: `soccer-fpl-transfers`, `soccer-fpl-captain`.
DFS skills build lineups under the cap from your salary file; they never advise on entries, contests or bankroll.

**Skills that fire when you ask.** Every description was rewritten and tested in Claude Code with each sport's MCP server connected, tuned on part of each skill's eval questions and scored on the rest. Every skill now ships evals: 10 questions it should answer, 10 near-misses it should leave alone, and 3 graded tasks.

**New skills**
- `soccer-player-props-research`: scorer, shots, shots on target, assists and card prices by sportsbook, the market's probability and the player's record against them.
- `mlb-player-props-research`: strikeouts, outs, hits, home runs, total bases and RBI lines, with the record against the line and workload.
- `ufc-card-preview`: a whole card on one page, with records, our Elo and the market's probability for every bout.
- `season-pack-offline`: answers from the free season pack when no API key or MCP server is set up yet.

**Better answers**
- Previews answer when a game isn't scheduled: the next meeting, the latest meeting and last season, or a labelled hypothetical, instead of stopping to ask.
- Props skills go past the raw hit rate: the spread across books, this season and last season separately, and a split for games like tonight's.
- Deeper UFC card, soccer xG, cricket, golf and tennis previews, each with a method section, a worked example and "not enough data" thresholds.
- Sequences such as the last five games are quoted in the order the tools return them, with dates.
- When a call is refused for credits, skills pass on the API's message and stop.

**Fixes from an audit against the live API**
- NFL advanced stats use the `tracking_*` and `charting_*` sources.
- NHL seasons are 8-digit ids (`20252026`).
- Search tools take `query` in hockey, football, golf and UFC; `get_pitch_mix` takes `pitcher_id`; playoff games are `game_type: playoff`.
- `nfl-game-preview` covers the NFL; there is no college parameter.

**Free season packs.** Each sport's repo now has the last completed season as CSV, with a Colab notebook that goes from the pack to the live API.

## 2.0.0 (2026-11-24)

One marketplace for nine sports: a plugin per sport (hockey, football, basketball, baseball, soccer, tennis, golf, UFC, cricket) and a shared analytics core. Game previews for every sport; NFL and NBA prop research and usage; soccer xG; a shared data preflight. Odds became information only across every skill.

## 1.x (2026-09 to 2026-11)

The hockey skills for PuckAPI: 28 skills for xG, goalies, player value, totals and research workflows; Codex and Gemini CLI support; the Claude Code plugin.
