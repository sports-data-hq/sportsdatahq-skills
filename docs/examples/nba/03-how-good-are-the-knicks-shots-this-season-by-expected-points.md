# How good are the Knicks' shots this season, by expected points per shot and zone?

> Asked in Claude Code on 2026-11-25 with the DunkAPI MCP server connected. Skill: `nba-shot-quality`. Tool calls: `get_shot_chart`. Credits: about 10. Answers change as games are played; run it yourself for today's numbers.

**Knicks shot quality, 2026-27 regular season (through today, 2026-11-25)**

NYK | NBA, season 2027 | 1,496 field-goal attempts, plus 349 free throws

**Shot quality:** expected points per shot is **1.052**. Actual points per shot is **1.051**, so the gap is about 0.00. The Knicks are scoring almost exactly what their shot locations are worth.

| Zone | Attempts | Share | FG% | Actual pts/shot | Expected pts/shot | Gap |
|---|---|---|---|---|---|---|
| Restricted area | 415 | 27.7% | 60.2% | 1.205 | 1.240 | -0.035 |
| Paint (non-restricted) | 227 | 15.2% | 37.9% | 0.758 | 0.837 | -0.079 |
| Midrange | 171 | 11.4% | 42.1% | 0.842 | 0.807 | +0.035 |
| Corner 3 | 190 | 12.7% | 33.2% | 0.995 | 1.141 | -0.146 |
| Above-the-break 3 | 493 | 33.0% | 38.3% | 1.150 | 1.044 | +0.106 |
| Free throws | 349 | n/a | 80.2% | 0.802 | n/a | n/a |

**Where the gap comes from:** two zones offset each other. Above-the-break threes are running about 0.11 points per shot above expectation, which is about 52 points over 493 shots. Corner threes are running about 0.15 below, which is about 28 points over 190 shots. The paint and restricted area are each a little under expectation.

**Read:**
- **Location quality is mixed.** The restricted area (1.24) and corner threes (1.14) are the most valuable zones, and together they make up only about 40% of the attempts. About 33% of attempts are above-the-break threes, which are worth 1.04 each. Midrange and the non-restricted paint are the lowest-value looks, and they make up about 27% of attempts.
- **The three-point splits are probably noise.** They rest on 190 corner and 493 above-the-break attempts. The corner number is thin, and a corner percentage of 33% is likely to move toward the Knicks' usual level. The above-the-break surplus (38.3% where the model expects about 34.8%) could also fade.
- **The overall match is the steadier finding.** It rests on 1,496 shots, but it is still only about 6 weeks of data. Expected points don't account for defenders, shot clock or who created the shot.

I didn't pull a league average, so I can't say where 1.052 ranks. I can pull a comparison team if you name one, at 10 credits each.

Data: `get_shot_chart` (team NYK) | NBA, season 2027, regular season. The overall figures are my sums from the zone rows: attempts times expected points, divided by 1,496.

**About the gallery snippet:** I haven't run it. `gallery.main()` would spawn `claude -p` subprocesses for the Knicks and FPL requests. Those use API credits and write files into `~/sportsdatahq-skills/docs/examples/` and its README. The snippet's "keep numbering after existing files" comment isn't implemented. `gallery.py` numbers files from 01 per sport, so the new NBA page would overwrite `nba/01-…` only if the slug matches. The slugs differ, but the numbering would collide in order. Do you want me to run it, with numbering fixed to continue after the existing files?
