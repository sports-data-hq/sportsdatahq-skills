# FastballAPI: baseball skills

Baseball analysis skills on FastballAPI: game previews, player and team research, and the community's standard metrics, with every number pulled live from the FastballAPI MCP server.

## Skills

- `mlb-batter-spray-profile`: Use when the user asks where or how an MLB hitter hits the ball, in fan or analyst wording.
- `mlb-dfs-stacks`: Use when someone has an MLB daily fantasy slate.
- `mlb-fantasy-waivers`: Use when a fantasy baseball manager is looking for pickups or deciding on a drop.
- `mlb-game-preview`: Use when the user wants an MLB game preview or a college baseball game breakdown.
- `mlb-line-movement`: Use when the user asks how an MLB moneyline, run line or total moved before first pitch, in fan wording.
- `mlb-pitcher-skill-change`: Use when the user asks whether an MLB pitcher has changed, in fan or analyst wording.
- `mlb-player-props-research`: Use when the user asks about MLB player prop lines as information.
- `mlb-regression-candidates`: Use when the user asks whether MLB numbers are real, lucky or due to change, in fan or analyst wording.
- `mlb-streaming-planner`: Use when the user is planning an MLB or fantasy baseball week around the schedule, in fan or analyst wording.
- `mlb-win-prob-swings`: Use when the user wants to know what decided a played MLB game, in fan or analyst wording.

## Data it sends

The skills call the FastballAPI MCP server at `mcp.fastballapi.com`. Each call sends the tool name and its inputs (teams, players, dates, seasons) with your FastballAPI API key, and returns data. Nothing from your files or conversation is sent beyond what a tool call needs. Calls use credits on your FastballAPI account; a free key at https://fastballapi.com/signup includes monthly credits.

Privacy policy: https://fastballapi.com/privacy

## Install

```
/plugin marketplace add sports-data-hq/sportsdatahq-skills
/plugin install mlb-data@sportsdatahq
```

More: https://fastballapi.com/skills. Licence: MIT (see LICENSE).
