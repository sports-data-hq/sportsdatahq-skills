# Which pitchers changed their pitch mix the most last season?

> Asked in Claude Code on 2026-11-25 with the FastballAPI MCP server connected. Skill: `mlb-pitcher-skill-change`. Tool calls: `get_leaders`, `get_pitch_mix`. Credits: about 85. Answers change as games are played; run it yourself for today's numbers.

Among the eight 2026 strikeout leaders, Cam Schlittler changed his pitch mix the most. I can't rank the whole league, because the tools only pull one pitcher at a time. I checked the 8 qualified pitchers with the most strikeouts, comparing regular-season 2026 with 2025. The measure is the total usage points moved from some pitches to others.

| Pitcher | Usage moved | What changed (2025 → 2026 usage) |
|---|---|---|
| Cam Schlittler, NYY | **24.9 pts** | Cutter 13.2% → 26.0%, sinker 7.2% → 19.2%, four-seam 54.8% → 44.2%, slider 7.8% → 0.7% |
| Gavin Williams, CLE | 18.4 | Four-seam 37.4% → 27.2%, cutter 14.0% → 5.8%, sinker 6.6% → 15.2%, sweeper 19.7% → 28.4% |
| Jacob Misiorowski, MIL | 17.9 | Cutter 0% → 9.7%, four-seam 55.2% → 63.3%, slider 24.3% → 15.5%, changeup 5.9% → 1.1% |
| Logan Gilbert, SEA | 17.6 | Slider 34.9% → 24.9%, changeup 0% → 7.3%, cutter 0% → 5.1%, splitter 20.0% → 15.1% |
| Jesus Luzardo, PHI | 15.6 | Sinker 10.3% → 17.5%, sweeper 30.7% → 38.2%, four-seam 33.8% → 26.2%, slider 7.9% → 0% |
| Dylan Cease, TOR | 15.1 | Slider 41.0% → 30.1%, changeup 1.1% → 11.5%, four-seam 41.1% → 37.0% |
| Reid Detmers, LAA | about 12 | Curve 21.1% → 11.0%, changeup 0.2% → 9.2% |
| Cristopher Sanchez, PHI | about 2 | Essentially unchanged |

**Schlittler** is the clearest case. He moved from a four-seam fastball with a curve to a heavier mix of cutter and sinker. His four-seam velocity held at about 97.5 mph both years, and his curve whiff rate went from 21.8% to 44.2%. His 2026 ERA was 1.95.

**Misiorowski** went to a bigger fastball share and added a cutter. His four-seam averaged 100.1 mph in 2026 against 98.8 in 2025, and its whiff rate rose from 32.7% to 40.5%.

**Cease** is the one where the ranking could mislead. His 2026 changeup averaged 81 mph, against 76.9 in 2025. That is a big jump in speed for the same pitch.

Caveats:
- **Sample:** this covers 8 pitchers, so it isn't a league-wide ranking. Someone outside the strikeout top 8 could have changed more, such as a mid-rotation starter or a reliever.
- **Small samples:** Schlittler (1,253 pitches) and Misiorowski (1,164) threw far fewer pitches in 2025 than in 2026 (about 3,000 and 2,650). Detmers had 1,083 in 2025. Their 2025 usage figures are less stable than the others.
- **Rare pitches:** whiff rates on pitches thrown fewer than about 100 times are unreliable. That includes Schlittler's slider and Misiorowski's changeup.
- **Velocity:** the tool cuts velocities down instead of rounding, so they run about 0.5 mph under published figures. Comparisons within this data are fine.
- **Causes:** the data has no spin, movement or release point. I can show that the mix changed, but not why.

If you want a different group, I can check another set, such as the strikeout leaders ranked 9–25 or specific pitchers you name. Each pitcher-season costs 5 credits, and this run used 85.

Data: get_leaders (so, 2026), get_pitch_mix | seasons 2025, 2026 regular season
