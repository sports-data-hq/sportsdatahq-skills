<div align="center">

<img src="assets/banner.png" alt="PuckAPI Skills" width="100%">

<br>
<br>

**Turn Claude into a hockey analyst.** 28 free skills covering NHL analytics,<br>market analysis, and predictive modeling. No code to install.

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-5dd5ff.svg?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-28-5dd5ff?style=flat-square)](skills/)
[![MCP Tools](https://img.shields.io/badge/MCP_tools-28-5dd5ff?style=flat-square)](https://github.com/PuckAPI/mcp)

[Quick Start](#quick-start) · [All Skills](#skills) · [How It Works](#how-it-works) · [Data](#data) · [Docs](#reference-docs)

</div>

<br>

```
You:    "Build me an expected goals model from shot data"
Claude: [loads nhl-xg-model skill → walks you through feature selection,
         spatial coordinates, shot type encoding, logistic regression baseline,
         gradient boosting upgrade, calibration, and evaluation]
```

```
You:    "How does our win probability for tonight's Sabres game differ from the market?"
Claude: [loads nhl-odds-explorer + market-vs-model → pulls the odds PuckAPI holds,
         removes the margin, shows the model vs market gap with sample sizes]
```

## Python

The official Python client is on PyPI: [puckapi](https://pypi.org/project/puckapi/).

```bash
pip install puckapi
export PUCKAPI_API_KEY=sk_live_...
```

```python
from puckapi import Client, to_dataframe

client = Client()

odds = client.get_odds(game_id="2026020080", snapshot_type="closing")
df = to_dataframe(odds, key="odds")
print(df[["bookmaker", "mlHome", "mlAway", "total"]])
print("credits left:", client.last_credits_remaining)
```

Typed errors for a bad key, no credits left, not found and rate limits, automatic retries, and `to_dataframe` for pandas.

## Quick Start

**1. Clone the skills:**

```bash
git clone https://github.com/PuckAPI/claude-sports-analytics.git
```

Or install them as a Claude Code plugin:

```
/plugin marketplace add PuckAPI/claude-sports-analytics
/plugin install puckapi-skills@puckapi
```

**2. Connect live NHL data** (optional - 500 free credits):

```bash
claude mcp add puckapi \
  --transport streamable-http \
  "https://mcp.puckapi.com/mcp?key=YOUR_API_KEY"
```

<sub>Get your free key at <a href="https://puckapi.com">puckapi.com</a>. Skills also work with your own CSV/JSON files - no API key needed.</sub>

**3. Ask Claude anything:**

```
"Analyze the Maple Leafs' season - record, Corsi, xG, special teams"
"Help me build a game prediction model"
"Pull tonight's lines and flag any movement"
"Compare McDavid and MacKinnon across every stat"
"Backtest my model over the last 3 seasons, with intervals and a per-season breakdown"
```

The `sports-skill-router` skill routes your request to the right 2-3 skills automatically.

---

## Skills

<details open>
<summary><strong>Data Exploration</strong> - 7 skills</summary>

<br>

| Skill | What It Does |
|-------|-------------|
| `nhl-game-lookup` | Find games by date, team, season. Scores, schedule, results. |
| `nhl-team-analysis` | Standings, advanced stats, strength of schedule, power rankings. |
| `nhl-player-scouting` | Player search, comparison, NHLe translation, career trajectory. |
| `nhl-goalie-analysis` | GSAA, xSV%, high-danger save rate, workload tracking. |
| `nhl-odds-explorer` | Multi-book price comparison, implied and fair probability, line movement. |
| `nl-to-query` | Translates natural language questions into structured data queries. |
| `nhl-game-preview` | Full pre-game breakdown: matchup, goalies, trends, odds, prediction. |

</details>

<details>
<summary><strong>Hockey Analytics</strong> - 2 skills</summary>

<br>

| Skill | What It Does |
|-------|-------------|
| `nhl-advanced-stats` | Corsi, Fenwick, xG, PDO, RAPM, WAR - definitions, context, proper usage. |
| `nhl-xg-model` | Build an expected goals model from scratch. Feature engineering through calibration. |

</details>

<details>
<summary><strong>Modeling Methodology</strong> - 7 skills</summary>

<br>

| Skill | What It Does |
|-------|-------------|
| `feature-engineering` | Rolling windows, lag features, leakage detection, feature catalogs. |
| `walk-forward-validation` | Temporal cross-validation. Refuses k-fold on time-series data. |
| `model-building` | LR → RF → XGBoost ladder. Hard-vote ensemble. Knows when to stop. |
| `elo-engineering` | 5 Elo variants (standard, margin, venue, recency, surface) with tuning. |
| `probability-calibration` | Platt scaling, isotonic regression, reliability diagrams, Brier decomposition. |
| `odds-market-analysis` | 4 devigging methods: power, multiplicative, Shin, worst-case. |
| `data-pipeline` | GitHub Actions automation, SQLite schema design, credit budgeting. |

</details>

<details>
<summary><strong>Markets and Evaluation</strong> - 5 skills</summary>

<br>

| Skill | What It Does |
|-------|-------------|
| `market-vs-model` | How our probability differs from the market's fair probability, with closing-line comparison. |
| `backtesting` | Walk-forward historical model evaluation with sample sizes, intervals and per-season results. |
| `nhl-daily-slate` | Tonight's slate: odds, fair probabilities and the model vs market gap for each game. |
| `prediction-tracker` | Log predictions, grade them with Brier score and calibration, compare to the closing line. |
| `visualization` | Calibration plots, gap distributions, player cards, correlation matrices. |

</details>

<details>
<summary><strong>Advanced Models</strong> - 4 skills</summary>

<br>

| Skill | What It Does |
|-------|-------------|
| `nhl-totals-model` | Game total prediction. Pace metrics, Poisson distribution, model vs market gap. |
| `nhl-player-props-research` | Player prop projections. TOI-first architecture, correlation between props. |
| `nhl-war-gar` | RAPM ridge regression, component GAR, contract surplus valuation. |
| `nhl-playoff-simulation` | Monte Carlo bracket simulation. Series win probabilities, path probabilities. |

</details>

<details>
<summary><strong>Workflow + Infrastructure</strong> - 3 skills</summary>

<br>

| Skill | What It Does |
|-------|-------------|
| `sports-skill-router` | Routes your request to the right skills automatically. Start here. |
| `nhl-research-workflow` | 4 patterns for hypothesis testing: explore, model, validate, deploy. |
| `nhl-puckapi-tools` | MCP tool router. 28 tools, credit tracking, your-own-data support. |

</details>

---

## How It Works

Skills are **markdown files, not code**. Each one teaches Claude a specific domain. When you mention a topic, Claude reads the relevant skill and gains that expertise for the conversation.

<table>
<tr>
<td width="50%">

**What each skill includes:**

- When to use / when NOT to use
- Step-by-step methodology
- Python/pandas code templates
- Anti-patterns it actively prevents
- Chaining to the next logical skill

</td>
<td width="50%">

**What skills prevent:**

- k-fold on time-series data
- Future data leakage in features
- Overfitting to small samples
- Wrong devigging methods
- Misinterpreting advanced stats

</td>
</tr>
</table>

---

## Data

| Source | Coverage |
|--------|----------|
| **[PuckAPI MCP](https://github.com/PuckAPI/mcp)** | 6.8M+ plays · 23,000+ games · 107,000+ odds records · 4,800+ players · 16 seasons (2010-11 to present) |
| **Your own files** | Every skill accepts CSV/JSON. Bring your own data, no credits needed. |

---

## Use it in

- **Claude, ChatGPT, Cursor, VS Code, Gemini CLI, Grok, Perplexity, Le Chat:** add `https://mcp.puckapi.com/mcp` as a remote MCP server. Step-by-step for each: https://puckapi.com/mcp
- **Gemini CLI:** `gemini extensions install https://github.com/PuckAPI/claude-sports-analytics`
- **Cursor:** the [SportsDataHQ plugins for Cursor](https://github.com/noahowsh/sportsdatahq-cursor-plugins)
- **Google Sheets:** `=SDHQ("puckapi","get_standings")` fills a live table: https://sportsdatahq.com/sheets

---

## Other sports

The same kind of skills pack, wired to each sport's own data API:

| Sport | Skills | Data API |
|-------|--------|----------|
| NFL and college football | [endzoneapi-mcp/skills](https://github.com/noahowsh/endzoneapi-mcp/tree/main/skills) | [EndzoneAPI](https://endzoneapi.com/skills) |
| NBA, WNBA and college basketball | [dunkapi-mcp/skills](https://github.com/noahowsh/dunkapi-mcp/tree/main/skills) | [DunkAPI](https://dunkapi.com/skills) |
| MLB and college baseball | [fastballapi-mcp/skills](https://github.com/noahowsh/fastballapi-mcp/tree/main/skills) | [FastballAPI](https://fastballapi.com/skills) |
| Soccer, 17 competitions | [strikerapi-mcp/skills](https://github.com/noahowsh/strikerapi-mcp/tree/main/skills) | [StrikerAPI](https://strikerapi.com/skills) |
| ATP and WTA tennis | [acesapi-mcp/skills](https://github.com/noahowsh/acesapi-mcp/tree/main/skills) | [AcesAPI](https://acesapi.com/skills) |
| PGA Tour and other golf tours | [birdieapi-mcp/skills](https://github.com/noahowsh/birdieapi-mcp/tree/main/skills) | [BirdieAPI](https://birdieapi.com/skills) |
| UFC, PFL and Bellator | [fighterapi-mcp/skills](https://github.com/noahowsh/fighterapi-mcp/tree/main/skills) | [FighterAPI](https://fighterapi.com/skills) |
| Cricket, every format | [yorkerapi-mcp](https://github.com/noahowsh/yorkerapi-mcp) | [YorkerAPI](https://yorkerapi.com) |

---

## Reference Docs

| Doc | Contents |
|-----|----------|
| [`hockey-glossary.md`](docs/hockey-glossary.md) | Corsi, Fenwick, xG, PDO, RAPM, WAR |
| [`market-glossary.md`](docs/market-glossary.md) | Odds formats, vig, fair probability, line movement, closing line |
| [`tool-routing.md`](docs/tool-routing.md) | Decision tree for picking the right data source |
| [`season-logic.md`](docs/season-logic.md) | NHL season IDs, game ID format, lockout handling |

---

## Contributing

Found an issue with a skill? Have a methodology improvement? PRs welcome.

Skills are markdown files in `skills/[name]/SKILL.md`. Each skill has a consistent structure - follow the existing patterns.

---

<div align="center">

**[PuckAPI MCP Server](https://github.com/PuckAPI/mcp)** · **[puckapi.com](https://puckapi.com)** · **[API Docs](https://puckapi.com/docs)** · **[Player props today](https://puckapi.com/props)**

<sub>MIT License</sub>

</div>

## Use with Codex

Add this repo as a Codex plugin marketplace, then install the plugin:

```bash
codex plugin marketplace add PuckAPI/claude-sports-analytics
```

Then open the plugin directory in Codex and install `puckapi-skills` from the `puckapi` marketplace. The plugin bundles the skills in `skills/` and the PuckAPI MCP server (https://mcp.puckapi.com/mcp). Set your key first (free at https://puckapi.com/signup):

```bash
export PUCKAPI_API_KEY=your_key
```

Codex sends it as a bearer token.

## Use with Gemini CLI

```bash
export PUCKAPI_API_KEY=your_key
gemini extensions install https://github.com/PuckAPI/claude-sports-analytics
```

The extension adds the PuckAPI MCP server (https://mcp.puckapi.com/mcp) and sends the key in the `x-api-key` header. Get a free key (500 credits a month) at https://puckapi.com/signup.
