# Sinner vs Alcaraz: head to head and who has the edge on each surface

> Asked in Claude Code on 2026-11-25 with the AcesAPI MCP server connected. Skill: `tennis-head-to-head`. Tool calls: `search_players`, `get_head_to_head`, `get_ratings`. Credits: about 13. Answers change as games are played; run it yourself for today's numbers.

# Sinner vs Alcaraz: head to head

**Alcaraz leads 10-7 in 17 meetings.** The last meeting was Sinner d. Alcaraz 7-6(5) 6-3 in the Monte-Carlo final on clay, 12 Apr 2026. Sets are 26-25 to Alcaraz, so the rivalry is very close.

| Surface | Sinner | Alcaraz | Meetings |
|---|---|---|---|
| Hard | 3 | 7 | 10 |
| Clay | 2 | 3 | 5 |
| Grass | 2 | 0 | 2 |
| Finals | 4 | 5 | 9 |

**Current strength (our Elo, with rank from the player search):**

| | Sinner | Alcaraz | Higher |
|---|---|---|---|
| Overall | 2407 | 2331 | Sinner |
| Hard | 2367 | 2265 | Sinner (+102) |
| Clay | 2209 | 2247 | Alcaraz (+38) |
| Grass | 2119 | 2135 | Alcaraz (+16) |
| Rank | 2 | 3 | Sinner |

## Who has the edge on each surface

- **Hard:** The record favours Alcaraz 7-3, but one of those wins was the Cincinnati 2025 final, where Sinner retired at 0-5. Without it the record is 6-3. The ratings point the other way, with Sinner clearly ahead. Sinner also won the most recent hard meeting, the 2025 ATP Finals final (7-6(4) 7-5, indoors). Alcaraz's wins are mostly older, with the exception of the 2025 US Open final (6-2 3-6 6-1 6-4).
- **Clay:** Alcaraz leads 3-2 and is slightly ahead on clay Elo. He won Roland Garros 2024 (semi) and 2025 (final), and Rome 2025. Sinner won Umag 2022 and Monte-Carlo 2026. This is a near coin flip with a small lean to Alcaraz, and Sinner has the latest result.
- **Grass:** Sinner leads 2-0 (Wimbledon 2022 R4 and the 2025 final). Two matches is too few to mean anything. The grass Elo has Alcaraz fractionally higher, and both sit behind Djokovic.

## Is the record informative?

Not very. It is close, so ratings should lead. It is 10-7 over 17 meetings, nowhere near the lopsided 8-1-or-better pattern that would carry signal of its own. The surface splits are small samples: 5 on clay, 2 on grass, 10 on hard. Two things also qualify the record:
- **Age:** 10 of the 17 meetings were in 2024 or earlier, and Sinner has won 3 of the last 5.
- **Retirement:** Cincinnati 2025 counts as a result but was not a full match.

**Stale rating:** Sinner's last match in the data is 12 Jul 2026, while Alcaraz played as recently as 22 Nov 2026. Sinner's Elo is therefore about four months old. It does not decay while he is absent, so it may overstate his current level, especially on hard courts.

Data: search_players, get_head_to_head, get_ratings (overall, hard, clay and grass) | ATP, matches 2021–2026. I took ranks from the search_players results rather than a separate rankings call.
