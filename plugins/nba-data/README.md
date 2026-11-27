# DunkAPI: basketball skills

Basketball analysis skills on DunkAPI: game previews, player and team research, and the community's standard metrics, with every number pulled live from the DunkAPI MCP server.

## Skills

- `nba-dfs-lineup`: Use when someone has an NBA daily fantasy slate and wants lineups built.
- `nba-fantasy-streaming`: Use when a fantasy basketball manager is planning a week or a pickup.
- `nba-game-preview`: Use when the user wants a preview of one NBA or WNBA game.
- `nba-line-movement`: Use when the user asks how an NBA, WNBA or college basketball spread, total or moneyline moved, in fan wording.
- `nba-minutes-usage-redistribution`: Use when an NBA or WNBA player is out or limited and the user asks who benefits.
- `nba-pace-efficiency-matchup`: Use when the user asks about tempo or how two NBA or WNBA teams' styles match up, in fan or analyst wording.
- `nba-player-props-research`: Use when the user asks about NBA or WNBA player prop lines or how a player did against his line, in fan or analyst wording.
- `nba-shot-quality`: Use when the user wants to know how good a player's or team's shots are in the NBA or WNBA.
- `ncaam-bracket-research`: Use when the user asks about the NCAA tournament, March Madness or a conference tournament field as information.
- `ncaam-game-preview`: Use when the user wants a preview of one college basketball game, men's or women's (any university or school team, not the NBA).
- `ncaam-player-props-research`: Use when the user asks about men's college basketball player prop lines or how a player did against his line.

## Data it sends

The skills call the DunkAPI MCP server at `mcp.dunkapi.com`. Each call sends the tool name and its inputs (teams, players, dates, seasons) with your DunkAPI API key, and returns data. Nothing from your files or conversation is sent beyond what a tool call needs. Calls use credits on your DunkAPI account; a free key at https://dunkapi.com/signup includes monthly credits.

Privacy policy: https://dunkapi.com/privacy

## Install

```
/plugin marketplace add sports-data-hq/sportsdatahq-skills
/plugin install nba-data@sportsdatahq
```

More: https://dunkapi.com/skills. Licence: MIT (see LICENSE).
