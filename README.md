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

**Get a key (free, no card):** sign in when the first tool call asks, or create the account first: [PuckAPI](https://puckapi.com/signup?utm_source=github&utm_medium=skills&utm_campaign=nhl-data), [EndzoneAPI](https://endzoneapi.com/signup?utm_source=github&utm_medium=skills&utm_campaign=nfl-data), [DunkAPI](https://dunkapi.com/signup?utm_source=github&utm_medium=skills&utm_campaign=nba-data), [FastballAPI](https://fastballapi.com/signup?utm_source=github&utm_medium=skills&utm_campaign=mlb-data), [StrikerAPI](https://strikerapi.com/signup?utm_source=github&utm_medium=skills&utm_campaign=soccer-data), [AcesAPI](https://acesapi.com/signup?utm_source=github&utm_medium=skills&utm_campaign=tennis-data), [BirdieAPI](https://birdieapi.com/signup?utm_source=github&utm_medium=skills&utm_campaign=golf-data), [FighterAPI](https://fighterapi.com/signup?utm_source=github&utm_medium=skills&utm_campaign=mma-data), [YorkerAPI](https://yorkerapi.com/signup?utm_source=github&utm_medium=skills&utm_campaign=cricket-data). Working across sports? [One SportsDataHQ key](https://app.sportsdatahq.com/signup?utm_source=github&utm_medium=skills&utm_campaign=core) covers all nine, with 1,000 free credits a month. No key yet? The `season-pack-offline` skill answers from a free season of data first.

**See them work:** [example answers](docs/examples/README.md) from every sport on live data, each with the skill, the tools it called and the credits it used. What's new: [CHANGELOG](CHANGELOG.md). Fantasy and DFS skills also have their own repo: [sports-data-hq/fantasy-sports-skills](https://github.com/sports-data-hq/fantasy-sports-skills).

Just one skill: `npx skills add sports-data-hq/sportsdatahq-skills --skill nfl-game-preview`.

## Skills

**Shared:** `sports-data-preflight` (ids, season conventions, duplicates, enough data), `market-vs-model` (the market's no-margin probability beside a model's, as information), `odds-market-analysis`, `prediction-tracker`, `model-building`, `feature-engineering`, `backtesting`, `walk-forward-validation`, `probability-calibration`, `elo-engineering`, `visualization`, `data-pipeline`, `nl-to-query`, `sports-skill-router`.

| Sport | Skills |
|---|---|
| Hockey | `nhl-game-preview`, `nhl-player-props-research`, `nhl-goalie-analysis`, `nhl-daily-slate`, `nhl-advanced-stats`, `nhl-xg-model`, `nhl-war-gar`, `nhl-team-analysis`, `nhl-player-scouting`, `nhl-playoff-simulation`, `nhl-totals-model`, `nhl-game-lookup`, `nhl-odds-explorer`, `nhl-puckapi-tools`, `nhl-research-workflow`, `nhl-goalie-gsax-report`, `nhl-xg-report` |
| Football | `nfl-game-preview`, `nfl-player-props-research`, `nfl-weekly-usage-report`, `nfl-fourth-down-review`, `nfl-epa-leaderboards`, `nfl-qb-efficiency`, `nfl-injury-impact` |
| Basketball | `nba-game-preview`, `nba-player-props-research`, `nba-minutes-usage-redistribution`, `nba-shot-quality`, `nba-pace-efficiency-matchup` |
| Baseball | `mlb-game-preview`, `mlb-regression-candidates`, `mlb-pitcher-skill-change`, `mlb-streaming-planner`, `mlb-batter-spray-profile`, `mlb-win-prob-swings` |
| Soccer | `soccer-match-preview`, `soccer-xg-breakdown`, `soccer-season-simulation`, `soccer-team-style-profile`, `soccer-set-pieces` |
| Tennis | `tennis-match-preview`, `tennis-head-to-head`, `tennis-tournament-simulation`, `tennis-surface-form` |
| Golf | `golf-tournament-preview`, `golf-strokes-vs-field`, `golf-course-history`, `golf-finish-simulation`, `golf-leaderboard-story` |
| UFC | `ufc-fight-preview`, `ufc-elo-baseline`, `ufc-fighter-profile`, `ufc-finish-profile` |
| Cricket | `cricket-match-preview`, `cricket-phase-analysis`, `cricket-chase-win-probability`, `cricket-venue-effects`, `cricket-batter-vs-bowler` |

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
