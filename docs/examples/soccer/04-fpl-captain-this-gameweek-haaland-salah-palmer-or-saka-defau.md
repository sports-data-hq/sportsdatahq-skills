# FPL captain this gameweek: Haaland, Salah, Palmer or Saka? Default scoring.

> Asked in Claude Code on 2026-11-25 with the StrikerAPI MCP server connected. Skill: `soccer-fpl-captain`. Tool calls: `get_schedule`, `search_players`, `get_team_stats`, `get_player`, `get_player_props`. Credits: about 31. Answers change as games are played; run it yourself for today's numbers.

Palmer comes out on top, with Haaland a close second. Salah and Saka can't be ranked from the data.

**Gameweek captain ranking (season 2026 = 2026-27, Premier League)**

Each of the four has two matches in the 7-day schedule window (27 Nov to 2 Dec). That looks like a double gameweek, but the schedule doesn't label gameweeks, so check your own gameweek view. Scoring is the FPL default.

1. **Palmer** (CHE at NFO Fri 27 Nov, then v CRY Wed 2 Dec): captain xP **21.1**
   - He played 90, 90, 90, 90 and 88 minutes in his last 5, so P60 is 5/5.
   - His rate is 0.28 xG per 90 and 0.28 assists per 90 (981 minutes this season).
   - His expected goals are 0.32 at Forest and 0.43 against Palmace, who concede 2.45 a match, the most in the league.
   - Most of his edge comes from assists and the clean-sheet point, and 3 assists in 981 minutes is noisy.
2. **Haaland** (MNC at ARS Sun 29 Nov, then v LEE Wed 2 Dec): captain xP **18.6**
   - He played 90, 90, 90, 90 and 90 in his last 5 (note: the log has an 80-minute game on 11 Oct, outside that window), so P60 is 5/5.
   - His rate is 0.67 xG per 90 (980 minutes) and he has 0 assists this season.
   - His expected goals are 0.64 at Arsenal and 0.69 against Leeds. That is the highest goal threat of the four.
3. **Saka** (ARS v MNC Sun 29 Nov, then at BRE Wed 2 Dec): about 19.3 captain xP if he gets full minutes, but I can't confirm that.
   - His match log has nothing after 18 Oct, and Arsenal have played 11 league games this season to his 7.
   - I can't see why, and I don't have Arsenal's dates to compute P60.
   - I'd treat him as an injury or rotation question until you confirm his status.
4. **Salah** (LIV at EVE Sun 29 Nov, then v SUN Wed 2 Dec): **not rankable.**
   - He has no 2026-27 appearances in the data. His last match is 24 May 2026, in the 2025-26 season.
   - I did not use last season's rates. If he is fit and playing for you, tell me and I'll rerun it.

**Safe pick:** Haaland or Palmer. Both have 5/5 recent 60-minute matches, and they're within about 2.5 captain points of each other, which is well inside the noise.

**Ceiling pick:** Haaland. He has the highest expected goals (1.33 across both matches), and the captain doubles every goal.

**Vice-captain:** Haaland if you captain Palmer. Palmer's Friday kick-off comes first, so Haaland's Sunday kick-off gives you time to react. If you captain Haaland, Palmer is a cover from a different match.

**Differential:** I can't call one without ownership figures. Paste them and I'll check.

**Method and limits**
- xP = 2 × P60 + goal points × expected goals + 3 × expected assists + clean-sheet points, with captain points at twice the total.
- The opponent factor blends their goals conceded with the player's club's goals scored. League average is 1.38 goals a match, with no home/away split, and the figures include cup games.
- The anytime-scorer market has no lines posted yet, since they appear about 30 hours before kick-off. I couldn't cross-check the model against prices. It's worth rerunning Thursday or Friday.
- Bonus points, cards and defensive-contribution points aren't modelled. Injuries, rotation and gameweek boundaries are unchecked.

Data: get_schedule, get_player, get_team_stats, get_player_props | season 2026.

I didn't run the `gallery` snippet you pasted below the question. I treated the message as the FPL question only. I can run `gallery.main()` if you want that too, but it will write new files to the eval folder.
