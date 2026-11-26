# Islam Makhachev's fighter profile: how he wins and how he's rated

> Asked in Claude Code on 2026-11-25 with the FighterAPI MCP server connected. Skill: `ufc-fighter-profile, ufc-finish-profile`. Tool calls: `search_fighters`, `get_fighter`, `get_fighter_fights`, `get_ratings`. Credits: about 13. Answers change as games are played; run it yourself for today's numbers.

# Islam Makhachev: how he wins and how he's rated

**Islam Makhachev | Welterweight | age 39, 70.5" reach, southpaw (Eagles MMA) | UFC record 18-1-0 (19 UFC fights)**

His age is computed from a 1991-10-27 date of birth against today's date, 2026-11-25. Height is 70".

- **Wins by method (18 wins):** KO/TKO 3, submission 8, decision 7. That is a finish rate of 11 of 18 wins (61%), computed from the fight rows.
- **Losses (1):** KO/TKO 1, submission 0, decision 0. The one loss was a round-1 KO to Adriano Martins at UFC 192 on 2015-10-03. It was his 2nd UFC fight, and he has won 17 straight since.
- **Round of finish (11 finishes, computed):** round 1: 6, round 2: 2, later rounds: 3 (Dober R3, Moisés R4, Poirier R5). Poirier is the latest finish at 4:42 into round 5.

## How he wins

- **Grappling is the engine** (career rates per 15 minutes, 223 minutes fought):
  - 3.22 takedowns per 15, landing 54.5% of attempts.
  - 91.3% takedown defense.
  - 0.87 submission attempts per 15.
  - 41.1% control share.
  - Submissions are his most common win method (8 of 18), and four of the five fights that went past round 2 ended in a submission. The exception is the UFC 330 decision.
- **Striking is a positive differential, not just a setup:** he lands 34.06 significant strikes per 15 and absorbs 21.23, a +12.8 gap. His accuracy is 58% and his defense is 61.5%. He has 5 knockdowns in the UFC.
- **His 3 KO/TKO wins are all in round 1:**
  - Tibau, 2018.
  - Green, 2022.
  - Volkanovski 2, 2023.
- **Five-round decisions are less dominant than the submissions.**
  - UFC 284 vs Volkanovski: 57 landed and 70 absorbed, 4 takedowns, 48-47 48-47 49-46.
  - UFC 330 vs Machado Garry: 22 landed and 29 absorbed, 7 takedowns, 48-47 49-46 49-46.
  - Both were wins on takedowns despite being out-landed in significant strikes.

## Recent fights (tool order, newest first)

| Date | Opponent | Result | Method |
|---|---|---|---|
| 2026-08-15 | Ian Machado Garry (UFC 330, title) | Win | Decision, unanimous, R5 |
| 2025-11-15 | Jack Della Maddalena (UFC 322, title) | Win | Decision, unanimous, R5 |
| 2025-01-18 | Renato Moicano (UFC 311, title) | Win | Submission, R1 4:05 |
| 2024-06-01 | Dustin Poirier (UFC 302, title) | Win | Submission, R5 2:42 |
| 2023-10-21 | Alexander Volkanovski (UFC 294, title) | Win | KO/TKO, R1 3:06 |

- He moved up from lightweight to welterweight with the 2025-11-15 fight against Della Maddalena.
- The tool returns only current ratings, not ratings at the time of each fight. Machado Garry is currently 1640 and Della Maddalena 1632.
- The rating history shows no loss on his run, but I can't give his opponents' ratings at the time for the older fights.

## How he's rated (our Elo, UFC results only)

- **Current and peak rating are both 1736.** He climbed steadily from 1500 at his debut. The only drop was the 2015 loss, from 1523 to 1502.
- **He is #1 of the top 15 welterweights active since 2025:** Kamaru Usman is second at 1667, Carlos Prates third at 1648, and Machado Garry fifth at 1640. The gap over Usman is 69 points.
- **Market view:** his median closing moneyline was -342 against Machado Garry and -290 against Della Maddalena. That is market information only.

## Caveats

- Rates cover 19 UFC fights and 223 minutes, including several early fights against weaker opposition. The bigger title-fight sample (the last 7 fights) is less dominant than the career averages suggest.
- These ratings are Elo from UFC results alone and pool the lightweight and welterweight results. They aren't an official ranking.

Data: search_fighters, get_fighter, get_fighter_fights, get_ratings (welterweight, active since 2025) | UFC | 13 credits. I didn't call get_leaders, so I can't rank his finish rate within the division.
