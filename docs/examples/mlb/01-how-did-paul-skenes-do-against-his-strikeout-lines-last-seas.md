# How did Paul Skenes do against his strikeout lines last season?

> Asked in Claude Code on 2026-11-25 with the FastballAPI MCP server connected. Skill: `mlb-player-props-research`. Tool calls: `search_players`, `get_prop_history`. Credits: about 21. Answers change as games are played; run it yourself for today's numbers.

Skenes was almost exactly even against his strikeout lines in 2026: **15 overs and 16 unders in 31 starts (48.4% over), with no pushes.** The line was the median across books, and the data comes from `get_prop_history`.

| | Overs | Unders | Over rate |
|---|---|---|---|
| Season | 15 | 16 | 48.4% |
| Apr 1 – Jun 20 | 10 | 5 | 67% (n=15) |
| Jun 26 – Sep 24 | 5 | 11 | 31% (n=16) |

- **Line vs. result:** The average closing line was 6.5, and he averaged 6.4 strikeouts. The line was close to his actual output.
- **Early season:** He went over in 10 of his first 15 starts after a rough April start. His highs came during that stretch and just after it: 10 on May 12, 10 on May 28 and 10 on Jun 14. Another 11 came on Jul 25.
- **Late season:** From Jun 26 on, the unders piled up. He went under in 11 of 16, including 2 strikeouts on Sep 6 against a 6.5 line and 4 on Aug 25 against a 5.5 line. The books lowered the line to 5.5 for four of his last five starts. He went over in his last two (7 on Sep 18, 8 on Sep 24).
- **Near misses:** Four of the unders missed by half a strikeout (6 on Apr 7, 6 on Apr 13, 7 on Jun 26, 7 on Jul 31). Three of the overs cleared by only 0.5 (7 on Apr 24, 7 on May 17, 7 on Jun 3).

I didn't pull pitch counts, so I can't say whether the late-season unders were short outings. I also didn't check opponents. If you want either, `get_player_games` would show innings and pitches per start. Past hit rates don't predict future results.

Data: search_players, get_prop_history | season 2026 (regular season only; the query had no postseason games).
