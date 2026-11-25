<div align="center">

# SportsDataHQ skills

**Claude skills for nine sports.** Game previews, player and team research, and each sport's standard metrics, with every number pulled live from the SportsDataHQ APIs.

Hockey · Football · Basketball · Baseball · Soccer · Tennis · Golf · UFC · Cricket

[Install](#install) · [Skills](#skills) · [How it works](#how-it-works) · [Rules](#rules-every-skill-follows) · [Other tools](#codex-cursor-gemini)

</div>

```
You:    "Preview Bills at Chiefs this Sunday"
Claude: [nfl-game-preview] records and form, EPA and success rate, injuries,
        the line and the market's no-margin probability, one page,
        every number tied to the call that produced it
```

## Install

In Claude Code, add the marketplace once, then install the sports you want:

```
/plugin marketplace add sports-data-hq/sportsdatahq-skills
/plugin install nfl-data@sportsdatahq
/plugin install sports-analytics-core@sportsdatahq
```

| Plugin | Sport | Data API (MCP server) |
|---|---|---|
| `nhl-data` | Hockey (NHL, PWHL, junior and minor leagues) | PuckAPI |
| `nfl-data` | Football (NFL, college, FCS) | EndzoneAPI |
| `nba-data` | Basketball (NBA, WNBA, college, NBL) | DunkAPI |
| `mlb-data` | Baseball (MLB, college) | FastballAPI |
| `soccer-data` | Soccer (17 leagues and cups) | StrikerAPI |
| `tennis-data` | Tennis (ATP, WTA) | AcesAPI |
| `golf-data` | Golf (PGA Tour, LPGA, LIV, DP World, Korn Ferry) | BirdieAPI |
| `mma-data` | UFC, PFL, Bellator | FighterAPI |
| `cricket-data` | Cricket (Tests, ODIs, T20s, IPL, BBL and more) | YorkerAPI |
| `sports-analytics-core` | Any sport: modeling, backtesting, calibration, Elo, charts | (uses the sport's server) |

Each sport plugin connects its API's MCP server; you sign in on the first call. Every API gives 500 free credits a month.

Just one skill: `npx skills add sports-data-hq/sportsdatahq-skills --skill nfl-game-preview`.

## Skills

**Shared:** `sports-data-preflight` (ids, season conventions, duplicates, enough data), `market-vs-model` (the market's no-margin probability beside a model's, as information), `odds-market-analysis`, `prediction-tracker`, `model-building`, `feature-engineering`, `backtesting`, `walk-forward-validation`, `probability-calibration`, `elo-engineering`, `visualization`, `data-pipeline`, `nl-to-query`, `sports-skill-router`.

| Sport | Skills |
|---|---|
| Hockey | `nhl-game-preview`, `nhl-player-props-research`, `nhl-goalie-analysis`, `nhl-daily-slate`, `nhl-advanced-stats`, `nhl-xg-model`, `nhl-war-gar`, `nhl-team-analysis`, `nhl-player-scouting`, `nhl-playoff-simulation`, `nhl-totals-model`, `nhl-game-lookup`, `nhl-odds-explorer`, `nhl-puckapi-tools`, `nhl-research-workflow` |
| Football | `nfl-game-preview`, `nfl-player-props-research`, `nfl-weekly-usage-report` |
| Basketball | `nba-game-preview`, `nba-player-props-research`, `nba-minutes-usage-redistribution` |
| Baseball | `mlb-game-preview` |
| Soccer | `soccer-match-preview`, `soccer-xg-breakdown` |
| Tennis | `tennis-match-preview` |
| Golf | `golf-tournament-preview` |
| UFC | `ufc-fight-preview` |
| Cricket | `cricket-match-preview` |

More are on the way for every sport: fourth-down and EPA work, xG and GSAx reports, regression screens, simulations. `catalog.json` lists every skill with its plugin and flags (all read-only; none move money).

## How it works

A skill is a short playbook: when to use it, the default sequence of tool calls (with their credit costs), the output format, and the rules. Claude loads it when your request matches, then calls the sport's MCP tools for live data. No code to install; nothing runs on your machine.

## Rules every skill follows

- Call the tools; never answer from memory.
- Name the tool call behind each number and the sample size behind each rate.
- State the season convention (it differs by sport).
- Say "not enough data" instead of guessing.
- Sportsbook prices are information about the market. No picks, no stake sizing, no bet links.

## Codex, Cursor, Gemini

- **Codex** reads `.agents/plugins/marketplace.json` (one plugin per sport).
- **Cursor** reads `.cursor-plugin/marketplace.json`.
- **Gemini CLI**: `gemini extensions install https://github.com/sports-data-hq/sportsdatahq-skills` adds all nine MCP servers (set each `<BRAND>_API_KEY`).

## Contributing

Each skill lives in `plugins/<plugin>/skills/<name>/` with a `SKILL.md` and `evals/evals.json` (task checks and trigger queries with near-miss negatives). Run `python scripts/validate.py` before a pull request; CI runs it and Claude Code's plugin validator.

## License

MIT
