# Who has the best course history at Augusta among active players?

> Asked in Claude Code on 2026-11-25 with the BirdieAPI MCP server connected. Skill: `golf-course-history`. Tool calls: `list_tournaments`, `get_ratings`, `get_course_history`, `search_players`. Credits: about 44. Answers change as games are played; run it yourself for today's numbers.

I checked a shortlist of 9 active players' Masters records and Scottie Scheffler has the best Augusta history. The shortlist was the top of our ratings plus the well-known Augusta names. I didn't pull the whole field, so Koepka, Scott, Fleetwood, Schauffele, Åberg and Woods aren't covered.

**Scheffler at the Masters** (2020 to 2026, 7 starts, 28 rounds)
- Finishes, newest first: 2 (2026), 4 (2025), 1 (2024), T10 (2023), 1 (2022), T18 (2021), T19 (Nov 2020).
- He has 2 wins, 5 top 10s and 7 cuts made in 7 starts.
- His average finish is 7.9.
- He gains +2.78 strokes per round on the field at Augusta. His overall rating is +3.31, so Augusta is slightly below his usual level, not above it.

**How the others compare**

| Player | Starts | Wins / top 10s | Missed cuts | Avg finish | Strokes vs field per round |
|---|---|---|---|---|---|
| Scheffler | 7 | 2 / 5 | 0 | 7.9 | +2.78 |
| Spieth | 13 | 1 / 6 | 2 | 10.8 | +1.73 |
| Rahm | 10 | 1 / 5 | 0 | 17.7 | +1.73 |
| McIlroy | 18 | 2 / 9 | 3 | 12.4 | +1.42 |
| Matsuyama | 15 | 1 / 3 | 1 | 19.3 | +1.25 |
| Reed | 13 | 1 / 5 | 2 | 17.5 | +1.14 |
| Cantlay | 10 | 0 / 1 | 2 | 24.5 | +0.42 |
| DeChambeau | 10 | 0 / 2 | 3 | 25.6 | +0.02 |

- **Spieth** is the best of the rest by average finish. His 2015 win was 18 under (+4.82 strokes per round), and he has 3 other top-3 finishes.
- **McIlroy** won in both 2025 and 2026, at +3.43 and +3.55 strokes per round. His 18-start record is weaker (+1.42), since 3 of his 4 worst Masters came before 2022.
- **Rahm** has the same +1.73 as Spieth, but his last three starts were T14, T45 and T38.
- **Cantlay and DeChambeau** have poor Augusta records for how good they are in general.

**Caveats**
- Scheffler's 28 rounds are a smaller sample than McIlroy's or Spieth's.
- Course history carries less weight than current form. On current form Scheffler is also first, at +3.31, ahead of McIlroy at +2.39.

Data: get_course_history for the Masters (tournament 401811941), get_ratings, search_players, list_tournaments | PGA Tour, 2009 to 2026. The November 2020 Masters is filed under the 2021 season.
