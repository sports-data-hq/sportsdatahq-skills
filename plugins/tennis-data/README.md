# AcesAPI: tennis skills

Tennis analysis skills on AcesAPI: game previews, player and team research, and the community's standard metrics, with every number pulled live from the AcesAPI MCP server.

## Skills

- `tennis-head-to-head`: Use when the user asks about two tennis players' record against each other, in fan or analyst wording.
- `tennis-match-preview`: Use when the user asks about a specific tennis match, in fan or analyst wording.
- `tennis-surface-form`: Use when the user asks how a tennis player does on each surface, in fan or analyst wording.
- `tennis-tournament-simulation`: Use when the user wants title or round chances for a tennis tournament from the draw, in fan or analyst wording.

## Data it sends

The skills call the AcesAPI MCP server at `mcp.acesapi.com`. Each call sends the tool name and its inputs (teams, players, dates, seasons) with your AcesAPI API key, and returns data. Nothing from your files or conversation is sent beyond what a tool call needs. Calls use credits on your AcesAPI account; a free key at https://acesapi.com/signup includes monthly credits.

Privacy policy: https://acesapi.com/privacy

## Install

```
/plugin marketplace add sports-data-hq/sportsdatahq-skills
/plugin install tennis-data@sportsdatahq
```

More: https://acesapi.com/skills. Licence: MIT (see LICENSE).
