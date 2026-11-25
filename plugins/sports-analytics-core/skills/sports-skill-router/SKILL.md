---
name: sports-skill-router
description: "Routes hockey analytics requests to the right 2-3 skills. Load this FIRST when a hockey data or analytics request comes in and you are unsure which skills to activate. Prevents loading all 28 skills when only 2-3 are needed. Also handles first-use persona detection."
metadata:
  version: 1.0.0
  author: PuckAPI
---

# Skill Dispatch Guide

When a hockey analytics request comes in, match it to a pattern below. Load those skills. Don't load everything.

**Default data tool:** `nhl-puckapi-tools` -- covers most data needs. Load it alongside the relevant strategy skill unless the request specifically needs a different tool.

---

## First-Use Persona Detection

On first interaction, identify which path the user is on:

| Signal | Persona | Start With |
|--------|---------|-----------|
| "What games are tonight?" / exploring data | **Explorer** | `nhl-game-lookup` + `nhl-puckapi-tools` |
| "Help me build a model" / "I want to predict" | **Builder** | `nhl-advanced-stats` + `feature-engineering` |
| "What are tonight's best bets?" / "Give me picks" | **Daily User** | `nhl-daily-slate` + `nhl-odds-explorer` |
| "I have a model, is it any good?" | **Validator** | `walk-forward-validation` + `probability-calibration` |
| "I'm new to hockey analytics" | **Learner** | `nhl-advanced-stats` + `nhl-research-workflow` |
| "I'm new to betting" | **New Bettor** | `odds-market-analysis` + `market-vs-model` |

---

## Request Patterns -> Skills to Load

### "Who plays tonight?" / "What's the schedule?" / "Game results"
1. `nhl-game-lookup` -- find games by date, team, season
2. `nhl-puckapi-tools` -- `get_games`, `get_schedule` endpoints

### "How are the Sabres doing?" / "Standings" / "Team stats"
1. `nhl-team-analysis` -- standings, stats, rankings, SOS
2. `nhl-puckapi-tools` -- `get_standings`, `get_team_stats`

### "Tell me about Connor McDavid" / "Player stats" / "Compare players"
1. `nhl-player-scouting` -- search, stats, comparison, NHLe
2. `nhl-puckapi-tools` -- `search_players`, `get_player_stats`

### "Who's starting in goal?" / "Goalie matchup" / "Save percentage"
1. `nhl-goalie-analysis` -- leaderboard, workload, xG-adjusted metrics
2. `nhl-puckapi-tools` -- `get_goalie_stats`

### "What are the odds?" / "Line shopping" / "Best price"
1. `nhl-odds-explorer` -- multi-book comparison, line movement
2. `nhl-puckapi-tools` -- `get_odds`, `get_line_movement`
3. For odds math/devigging: also load `odds-market-analysis`

### "Show me games where..." / "Find all teams that..." / natural language query
1. `nl-to-query` -- translate natural language to structured queries
2. `nhl-puckapi-tools` -- routes to appropriate endpoint
3. If pattern found: `nhl-research-workflow` for follow-up hypothesis testing

### "What is Corsi?" / "Explain xG" / "Hockey analytics basics"
1. `nhl-advanced-stats` -- metric definitions, formulas, context
2. `nhl-puckapi-tools` -- pull real data to demonstrate

### "How do I use Claude for sports analysis?" / "What questions should I ask?"
1. `nhl-research-workflow` -- prompt patterns, hypothesis testing, iteration
2. Load relevant data skill based on the specific question

### "How do I automate this?" / "Run daily" / "Pipeline"
1. `data-pipeline` -- GitHub Actions, scheduling, model versioning
2. Reference `nhl-puckapi-tools` for endpoint costs in automation budget

### "Help me build features" / "Feature engineering" / "What features should I use?"
1. `feature-engineering` -- rolling windows, leakage detection, shift(1)
2. `nhl-puckapi-tools` -- historical data endpoints
3. If user is new to metrics: also load `nhl-advanced-stats`

### "How do I validate my model?" / "Is k-fold okay?" / "Cross-validation"
1. `walk-forward-validation` -- temporal CV, anti-leakage, significance testing
2. If user has a model: `probability-calibration` for probability verification

### "Help me build a prediction model" / "Train a model" / "XGBoost"
1. `model-building` -- model selection, training, evaluation
2. `walk-forward-validation` -- correct evaluation method
3. `feature-engineering` -- if features aren't built yet

### "Build an Elo rating system" / "Rating system" / "Team ratings"
1. `elo-engineering` -- 5 variants, tuning, carryover
2. `nhl-puckapi-tools` -- `get_games` for historical results

### "Are my probabilities calibrated?" / "Platt scaling" / "Brier score"
1. `probability-calibration` -- reliability diagrams, scaling methods
2. If model outputs available: proceed directly
3. If not: route to `model-building` first

### "How do I devig odds?" / "Implied probability" / "Shin method"
1. `odds-market-analysis` -- conversion, devigging, no-vig lines
2. `nhl-puckapi-tools` -- `get_odds` for real numbers to work with

### "Should I bet this game?" / "Where's the edge?" / "Expected value"
1. `market-vs-model` -- EV calculation, Kelly sizing, CLV
2. `nhl-odds-explorer` -- current market odds
3. `probability-calibration` -- verify model probabilities first
4. Requires: user must have a calibrated model

### "Backtest my model" / "Historical performance" / "Is my edge real?"
1. `backtesting` -- walk-forward backtest, strategy simulation
2. `nhl-puckapi-tools` -- historical odds (heavy credits)
3. If model health check: backtesting includes model audit

### "Build an xG model" / "Expected goals from scratch" / "Shot quality model"
1. `nhl-xg-model` -- full xG pipeline from play-by-play
2. If user needs basics first: `nhl-advanced-stats` for xG concept

### "Over/under prediction" / "Totals model" / "Will this game go over?"
1. `nhl-totals-model` -- pace, goalie matchup quality, under bias
2. `nhl-puckapi-tools` -- `get_odds` for totals lines

### "Player props" / "Will McDavid score?" / "SOG prop" / "DFS"
1. `nhl-player-props-research` -- TOI projection, per-60 rates, matchup adjustment
2. `nhl-player-scouting` -- player data
3. `nhl-puckapi-tools` -- `get_player_stats`

### "Build WAR" / "Player value" / "Contract analysis" / "RAPM"
1. `nhl-war-gar` -- RAPM ridge regression, component GAR
2. `nhl-player-scouting` -- player data for context

### "Playoff odds" / "Will they make the playoffs?" / "Season simulation"
1. `nhl-playoff-simulation` -- Monte Carlo, bracket simulation
2. `elo-engineering` -- if rating system needed as input
3. `nhl-puckapi-tools` -- remaining schedule

### "Preview tonight's game" / "Sabres vs Leafs preview"
1. `nhl-game-preview` -- compound skill, loads data internally
2. `nhl-puckapi-tools` -- multiple endpoints (~34 credits)

### "Tonight's card" / "Full slate" / "All games tonight"
1. `nhl-daily-slate` -- slate analysis, edge rankings
2. Requires: user's model for edge calculations
3. Heavy credits: ~10 credits per game on slate

### "Track my bets" / "Am I profitable?" / "CLV" / "Log this bet"
1. `prediction-tracker` -- prediction logging, CLV, significance
2. If performance declining: route to `backtesting` for audit

### "Make a chart" / "Visualize" / "Calibration plot" / "Player card"
1. `visualization` -- chart type selection, code generation
2. Requires output from another skill (calibration, backtest, preview, etc.)

---

## When to Load Docs

- Unknown hockey term -> `docs/hockey-glossary.md`
- Unknown betting term -> `docs/betting-glossary.md`
- Need to pick a data tool -> `docs/tool-routing.md`
- Date/season confusion -> `docs/season-logic.md`

## When NOT to Use This Guide

Single-skill requests don't need sports-skill-router. If someone says "devig these odds: +150 / -180" -> just load `odds-market-analysis`.
