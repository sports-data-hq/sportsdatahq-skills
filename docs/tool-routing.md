# Data Tool Routing Guide

When you need data, pick the tool for your sport. Always call the tool; do not answer from memory.

## Core skills: your sport's SportsDataHQ MCP server

The core skills work with any sport. Call your sport's SportsDataHQ MCP tools.

| Sport | Server | Example play-level tool |
|-------|--------|-------------------------|
| Hockey | PuckAPI | `get_shot_map` |
| Football | EndzoneAPI | `get_plays` |
| Basketball | DunkAPI | `get_shot_chart` |
| Baseball | FastballAPI | `get_pitches` |
| Soccer | StrikerAPI | `get_events` |
| Tennis | AcesAPI | `get_match` |
| Golf | BirdieAPI | `get_leaderboard` |
| UFC | FighterAPI | `get_fight` |
| Cricket | YorkerAPI | `get_deliveries` |

Market tools follow the same pattern across servers: `get_odds`, `get_line_movement`, `get_game_probabilities` (average implied and fair probability across books), `get_prop_probabilities`, `get_prop_backtest` where offered. Check the server's tool list before assuming a tool exists.

## Hockey: PuckAPI MCP server (`nhl-puckapi-tools`)

Use for all hockey data unless the user brings their own file.

| Data need | Tool | Credits |
|-----------|------|---------|
| Team list | `list_teams` | 1 |
| Upcoming schedule | `get_schedule` | 2 |
| Player search | `search_players` | 2 |
| Standings | `get_standings` | 2 |
| Game scores, results | `get_games` | 5 |
| Model win probability per game | `get_predictions` | 5 |
| Market fair probability per game | `get_game_probabilities` | 5 |
| Player bio and season context | `get_player_stats` | 5 |
| Skater leaderboard | `get_skater_season_stats` | 5 |
| Player game log | `get_player_game_log` | 5 |
| Team season stats | `get_team_stats` | 5 |
| Goalie leaderboard | `get_goalie_stats` | 5 |
| Single game detail (odds, goalies) | `get_game_detail` | 10 |
| Head-to-head history | `get_head_to_head` | 10 |
| Play-by-play | `get_plays` | 10 |
| Shot locations | `get_shot_map` | 10 |
| Shifts | `get_shifts` | 10 |
| Time by game situation | `get_situation_time` | 10 |
| Current odds | `get_odds` | 10 |
| Player prop lines, history, movement | `get_player_props`, `get_prop_history`, `get_prop_movement` | 10 each |
| Period and regulation markets | `get_market_odds` | 10 |
| Alternate lines | `get_alt_lines` | 10 |
| Prop fair probability | `get_prop_probabilities` | 10 |
| Line movement history | `get_line_movement` | 25 |
| Prop hit rates against the market | `get_prop_backtest` | 25 |
| Player projections (paid plans) | `get_prop_projections` | 25 |

## Your own data

When a user provides a CSV, JSON or database:
1. Work with the file directly. No MCP calls needed.
2. Verify required columns exist before proceeding.
3. Check date formats (ISO 8601 preferred).
4. No credits are used.

## Decision tree

```
Need hockey data?            -> nhl-puckapi-tools
Need another sport's data?   -> that sport's SportsDataHQ MCP server
User has their own file?     -> work with the file, no credits
Need odds for a backtest?    -> get_odds or get_market_odds, report sample size
Need line movement?          -> get_line_movement (most expensive, call once per game)
```
