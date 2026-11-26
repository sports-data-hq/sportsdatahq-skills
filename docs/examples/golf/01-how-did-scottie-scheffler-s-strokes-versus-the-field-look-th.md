# How did Scottie Scheffler's strokes versus the field look this season?

> Asked in Claude Code on 2026-11-25 with the BirdieAPI MCP server connected. Skill: `golf-strokes-vs-field`. Tool calls: `search_players`, `get_player_stats`, `get_leaders`. Credits: about 11. Answers change as games are played; run it yourself for today's numbers.

**Scottie Scheffler | PGA Tour, 2026 season | 78 rounds, 20 starts**

- **Strokes vs field per round:** raw **+2.35**, field-strength adjusted **+3.46**. The adjusted figure ranks **1st** among players with at least 40 rounds.
- **By hole type** (score-based, raw): par 3 +0.50, par 4 +2.11, par 5 +0.84. Most of his edge comes on par 4s. Hole-type splits are noisier than the total.
- **Results:** 3 wins, 13 top-10s, 19 top-25s, 19 cuts made in 20 starts. Average finish was 6.7 and scoring average 67.86.
- **Scoring:** 4.82 birdies and 1.83 bogeys or worse per round.

**Read**
- The adjusted gap to second place is large. Rory McIlroy is 2nd at +2.64 adjusted over 54 rounds. Fitzpatrick is 3rd at +2.39 over 78 rounds.
- Over 78 rounds the sample is solid, above the 40-round threshold, but not huge.
- The raw figure (+2.35) is well below the adjusted one (+3.46). That is because of how the data adjusts for field strength. I didn't pull round-by-round results, so I can't say which events drove it.

I didn't pull recent form (last five starts) or the decay-weighted rating, which would show whether he's trending up or down late in the season. I can pull those if you want.

*Data: search_players, get_player_stats, get_leaders | PGA Tour, 2026*
