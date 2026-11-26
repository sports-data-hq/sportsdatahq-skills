# Which goalies are saving the most goals above expected this season?

> Asked in Claude Code on 2026-11-25 with the PuckAPI MCP server connected. Skill: `nhl-goalie-gsax-report`. Tool calls: `get_goalie_stats`. Credits: about 5. Answers change as games are played; run it yourself for today's numbers.

**NHL goalie leaderboard by GSAX | 2026-27 season, snapshot 2026-11-25 | top 10 shown (minimum 10 games)**

| Goalie | Team | GP | GSAX | Save % | High-danger save % | Last 10 save % | Trend |
|---|---|---|---|---|---|---|---|
| Jesper Wallstedt | MIN | 22 | 19.5 | .924 | .916 | .953 | stable |
| Linus Ullmark | OTT | 13 | 13.6 | .941 | .913 | .958 | stable |
| Jacob Fowler | MTL | 15 | 12.2 | .918 | .887 | .946 | stable |
| Daniil Tarasov | DET | 10 | 9.7 | .927 | .938 | .952 | stable |
| Joel Hofer | STL | 17 | 9.5 | .919 | .882 | .946 | stable |
| Ilya Sorokin | NYI | 16 | 9.0 | .917 | .875 | .936 | down |
| Juuse Saros | NSH | 17 | 9.0 | .916 | .894 | .950 | stable |
| Jake Oettinger | DAL | 18 | 8.9 | .909 | .898 | .926 | down |
| Jeremy Swayman | BOS | 17 | 7.8 | .905 | .885 | .922 | down |
| Pyotr Kochetkov | CAR | 15 | 6.5 | .911 | .934 | .941 | stable |

**What the numbers say**
- Wallstedt leads by a wide margin. He has 19.5 GSAX over 22 games, the largest sample in the top group. That is about 6 goals more than Ullmark in second.
- Ullmark has the best raw save percentage (.941) and a 1.44 GAA in 13 games. His GSAX is lower than Wallstedt's mostly because he has played fewer games.
- Tarasov has only 10 games, the minimum for this list. Treat his 9.7 GSAX as an early read, since GSAX settles slowly and differences between goalies are small under about 25 games.
- Sorokin, Oettinger and Swayman are flagged "down" on the recent-form trend. Their season GSAX is still strong.
- I only pulled the top 10 by GSAX, so I haven't shown the bottom of the board. The tool also returned no expected-goals-against column, so I can't show that here.

Data: `get_goalie_stats` | season 2026-27, NHL, min games 10
