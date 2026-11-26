# Cole Palmer anytime scorer price and his record

> Asked in Claude Code on 2026-11-25 with the StrikerAPI MCP server connected. Skill: `soccer-player-props-research`. Tool calls: `search_players`, `get_schedule`, `get_player_props`, `get_prop_history`. Credits: about 23. Answers change as games are played; run it yourself for today's numbers.

No anytime scorer price is up yet for Cole Palmer's next match. I haven't invented one.

**Cole Palmer (Chelsea) | anytime goalscorer | Nottingham Forest v Chelsea, Fri 27 Nov 2026**
- **Prices now:** none. `get_player_props` returned no lines for this game. Lines are captured from about 30 hours before kick-off (15:00 and 20:00 UTC, and again in the last 75 minutes), so try again on Thursday or Friday.
- **Match context (`get_schedule`):** Forest are slight favourites, with the three-way line at about 39% Forest, 29% draw and 37% Chelsea. The total is 2.5 goals.
- **Typical closing price (`get_prop_history`):** his closes since August 2025 mostly sit between +125 and +310, with a few near evens. The last six games ran from +140 to +210. The tool gives no no-margin probability, because books mostly post only the Yes price.

**Record against the anytime price (`get_prop_history`, Aug 2025 to 21 Nov 2026)**
- **All priced games:** he scored in 11 of 37 graded games (30%). Two more games were voids because he wasn't in the squad or on the pitch. He averaged 0.4 goals per game.
- **2025-26:** 8 of 26 (31%). That included a hat-trick on 7 Feb 2026.
- **2026-27 so far:** 3 of 11 (27%). In order, the 11 games were:

| Date | Scored |
|---|---|
| 24 Aug | 1 |
| 30 Aug | 1 |
| 6 Sep | 0 |
| 12 Sep | 0 |
| 18 Sep | 0 |
| 10 Oct | 0 |
| 17 Oct | 0 |
| 24 Oct | 0 |
| 31 Oct | 1 |
| 8 Nov | 0 |
| 21 Nov | 0 |

- **Not checked:** I didn't pull his starts versus sub appearances, goals per 90 or penalty duties (`get_player_games`), or Chelsea's lineup. A 27% rate over 11 games is a small sample, and a past hit rate isn't a forecast.

Data: `search_players`, `get_schedule`, `get_player_props`, `get_prop_history`.
