# Which quarterbacks lead in EPA per dropback this season?

> Asked in Claude Code on 2026-11-25 with the EndzoneAPI MCP server connected. Skill: `nfl-epa-leaderboards`. Tool calls: `get_player_leaders`. Credits: about 5. Answers change as games are played; run it yourself for today's numbers.

The data I pulled ranks quarterbacks by total passing EPA, not EPA per dropback. The tool's `passing_epa` column is a season sum (`aggregation: sum`), so these totals reward volume. I haven't calculated a per-dropback rate.

**Passing EPA (season total) | 2026 REG | QBs, min 8 games | unadjusted for opponent**

| # | QB | Total EPA | Games |
|---|---|---|---|
| 1 | Joe Burrow, CIN | 100.8 | 10 |
| 2 | Brock Purdy, SF | 100.1 | 10 |
| 3 | Dak Prescott, DAL | 77.7 | 11 |
| 4 | Jared Goff, DET | 75.3 | 10 |
| 5 | Trevor Lawrence, JAX | 69.0 | 10 |
| 6 | Patrick Mahomes, KC | 65.3 | 10 |
| 7 | Kirk Cousins, MIN | 51.5 | 11 |
| 8 | Josh Allen, BUF | 50.7 | 10 |
| 9 | Jordan Love, GB | 50.1 | 10 |
| 10 | C.J. Stroud, HOU | 48.3 | 10 |

Matthew Stafford (47.1), Drake Maye (39.3), Geno Smith (25.3), Bryce Young (16.3) and Bo Nix (7.7) round out the top 15.

- **Close gaps:** Burrow and Purdy are separated by 0.7 EPA, which is noise over about 10 games. Treat them as tied. The same goes for Allen, Love and Stroud, who sit within about 2.5 EPA of each other.
- **Not a rate:** a QB with fewer dropbacks could rank higher per dropback than his total suggests. Per-dropback EPA needs dropback counts per QB. I can get those from `get_plays` at 10 credits per team, or by pulling attempts and sacks to approximate them.
- **Scope:** this covers only QBs with at least 8 games, so anyone below that is left out.

Data: get_player_leaders | season 2026, stat passing_epa, position QB, min_games 8

Do you want me to build the per-dropback version for the top 6–8 QBs? It would cost about 60–80 credits.
