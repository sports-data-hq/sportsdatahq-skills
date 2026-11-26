# Fantasy: should I start Bijan Robinson or Jahmyr Gibbs this week in PPR?

> Asked in Claude Code on 2026-11-25 with the EndzoneAPI MCP server connected. Skill: `nfl-fantasy-start-sit`. Tool calls: `search_players`, `get_schedule`, `get_prop_probabilities`, `get_injuries`, `get_player_stats`. Credits: about 38. Answers change as games are played; run it yourself for today's numbers.

**Start Gibbs.** The market projects him about 7 points ahead of Robinson in PPR, which is a clear gap. I assumed full PPR because you didn't give your scoring.

**Week 12 start/sit (full PPR)**

| | Gibbs (DET vs CHI) | Robinson (ATL at MIN) |
|---|---|---|
| Game | Thu Nov 26, total 55.5, CHI -1.5 | Sun Nov 29, total 41.5, MIN favored by 7 |
| Rush yards | 92.5 | 75.5 |
| Receiving yards | 35.5 | 19.5 |
| Receptions | 4.5 | 2.5 |
| Anytime-TD probability | 0.665 (fair) | no fair price, 0.57 (implied, margin in) |
| Projection | about 23.9 pts | about 16.4–17.1 pts |

- **Formula:** 0.1 × rush yards + 0.1 × receiving yards + 1 × receptions + 6 × expected TDs, where expected TDs = -ln(1 - p).
- **Gibbs:** 9.25 + 3.55 + 4.5 + 6 × 1.09 = about 23.9.
- **Robinson's touchdown number is weaker.** Books don't post both sides of his anytime-TD market, so there's no margin-free probability. The implied 0.57 gives the 17.1 end. Discounting it by the margin Gibbs's market carried gives the 16.4 end. Either way he's well behind.
- **The two numbers are rough.** Prop medians run slightly low for everyone, so don't read them as exact forecasts.

**Last 5 games (PPR points, in the order the tool returned them):**
- **Gibbs:** Wk 7: 17.3, Wk 8: 24.8, Wk 9: 13.4, Wk 10: 44.2, Wk 11: 27.8. Range 13.4–44.2.
- **Robinson:** Wk 6: 7.3, Wk 7: 17.2, Wk 8: 7.6, Wk 9: 26.7, Wk 10: 17.7. Range 7.3–26.7.
- Gibbs has the higher floor and ceiling. His 13.4-point low is above Robinson's 7.3-point low.
- Gibbs has scored 13 TDs in 10 games this season. Robinson has scored 7.

**Health:**
- **Gibbs:** he's not on Detroit's Week 12 report. It lists no one at RB.
- **Robinson:** Atlanta's Week 12 report isn't out yet. Check it before Sunday.
- **Timing:** Gibbs plays Thursday, so check Detroit's inactives before kickoff.

**What I didn't pull:** snap share. I skipped `get_snap_counts`, so I'm not claiming a trend either way. It wouldn't change the call at this margin.

Data: `get_schedule`, `get_prop_probabilities`, `get_injuries`, `get_player_stats` | season 2026, week 12.

If you're on half PPR or standard, the gap shrinks a little because Gibbs's edge includes more receptions. He'd still be ahead.
