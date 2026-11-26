# Preview tonight's Jets at Bruins game

> Asked in Claude Code on 2026-11-25 with the PuckAPI MCP server connected. Skill: `nhl-game-preview`. Tool calls: `get_schedule`, `get_standings`, `get_goalie_stats`, `get_game_probabilities`, `get_odds`, `get_head_to_head`. Credits: about 39. Answers change as games are played; run it yourself for today's numbers.

## Game Preview: Jets @ Bruins
Wed Nov 25, 2026 | TD Garden | 7:00 PM ET (00:00 UTC) | 2026-27 season

### Matchup Context
Source: `get_standings`, `get_schedule`.

| | Record (W-L-OTL) | GP | Pts% | Rank |
|---|---|---|---|---|
| WPG | 12-9-4, 28 pts | 25 | .560 | 15th overall, 15th in Central |
| BOS | 15-7-1, 31 pts | 23 | .674 | 10th overall, 3rd in Atlantic |

- **Ranks:** the standings tool returns league rank, so I derived division rank from the table. WPG sits 15th overall and BOS 10th.
- **Last-10 form:** not returned.
- **Rest:** the schedule tool doesn't give days of rest for either team, so there is not enough data to say whether either team is on a back-to-back.

### Goalie Matchup
Source: `get_goalie_stats`. Neither tool confirms tonight's starter, so check team news.

| Goalie | GP | Record | SV% | GAA | GSAx | Last-10 SV% | Rest |
|---|---|---|---|---|---|---|---|
| WPG Stuart Skinner | 18 | 8-5-4 | .887 | 3.24 | +2.8 | .911 (trending down) | 2 days |
| WPG Nico Daws | 4 | 2-2-0 | .872 | 2.78 | -2.1 | .928 | 5 days |
| WPG Clay Stevenson | 5 | 1-3-0 | .870 | 3.61 | -1.8 | .916 | 5 days |
| BOS Jeremy Swayman | 17 | 11-5-1 | .905 | 2.65 | +7.8 | .922 (trending down) | 3 days |
| BOS Michael DiPietro | 7 | 4-2-0 | .923 | 2.15 | +5.6 | .949 | 5 days |

Skinner and Swayman have the most starts for their teams. The sample for DiPietro, Daws and Stevenson is small (4 to 7 games).

### Key Stats
Source: `get_standings`. Corsi%, Fenwick% and expected goals are 5v5 only. Expected goals are season totals.

| Metric | WPG | BOS |
|---|---|---|
| Goals for per game | 3.16 | 3.61 |
| Goals against per game | 3.36 | 2.65 |
| Goal differential | -5 | +22 |
| Corsi% | 47.0 | 49.8 |
| Fenwick% | 47.3 | 50.6 |
| xGF | 47.6 | 50.4 |
| xGA | 55.1 | 47.0 |

- **Defense:** Winnipeg's xGA of 55.1 is among the higher figures in the league table. Boston's goals against per game is 0.71 lower.
- **Goal differential:** the gap between the teams is 27 goals, on a similar number of games played.

### Odds Snapshot
Source: `get_odds`, `get_game_probabilities`. Eight books, closing prices.

- **Moneyline:** BOS about -155 to -170, WPG +129 to +145.
- **Puck line:** BOS -1.5 at about +145 to +153, WPG +1.5 at about -172 to -184.
- **Total:** 6.5, with both sides at about -105 to -115.
- **Market fair probability:** WPG 40.3%, BOS 59.7%.
- **Puck line fair probability:** BOS -1.5 38.9%, WPG +1.5 61.1%.
- **Total fair probability:** over 49.9%, under 50.1%.
- **Book disagreement:** the Winnipeg price runs from +129 (MyBookie) to +145 (BetOnline), a spread of 16 cents. That is a wider range than the 5-cent threshold, and Winnipeg's implied probability ranges from 40.8% to 43.7% across books. DraftKings, Pinnacle and Bovada sit near +140 to +142.
- **Movement:** the DraftKings first-posted line was BOS -148 and the closing line was BOS -170. Several other books moved little, and I'm reporting the current lines only.

### Model vs Market Gap
No model probability supplied. The `get_predictions` tool isn't available in this session.

### Head-to-Head
Source: `get_head_to_head`. These are the last 10 of 38 all-time meetings, where BOS leads 24-14 all-time. The 10-game sample is too small to read a trend, though BOS won 7 of the 10.

| Date | Venue | Winner | Score |
|---|---|---|---|
| 2026-10-02 | WPG | BOS | 4-3 |
| 2026-03-19 | BOS | BOS | 6-1 |
| 2025-12-11 | WPG | BOS | 6-3 |
| 2025-01-30 | BOS | WPG | 6-2 |
| 2024-12-10 | WPG | WPG | 8-1 |
| 2024-01-22 | BOS | BOS | 4-1 |
| 2023-12-22 | WPG | WPG | 5-1 |
| 2023-03-16 | WPG | BOS | 3-0 |
| 2022-12-22 | BOS | BOS | 3-2 |
| 2022-03-18 | WPG | BOS | 4-2 |

**Sources:** `get_schedule` (WPG), `get_standings`, `get_goalie_stats` (WPG, BOS), `get_game_probabilities`, `get_odds`, `get_head_to_head`, all for game 2026020386 and season 20262027. I skipped `get_team_stats` because the standings call already returned the same 5v5 fields. In total I used 39 credits.
