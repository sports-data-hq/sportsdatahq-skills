# Preview South Africa vs Bangladesh

> Asked in Claude Code on 2026-11-25 with the YorkerAPI MCP server connected. Skill: `cricket-match-preview`. Tool calls: `list_teams`, `get_schedule`, `get_matches`, `get_ratings`, `get_venue`, `get_odds`. Credits: about 17. Answers change as games are played; run it yourself for today's numbers.

I'm putting together a preview of the next South Africa vs Bangladesh match, the 1st ODI on Dec 1. I have the ratings, venue, form, head to head and odds, so I'm writing it up now.

**South Africa vs Bangladesh | 1st ODI (D/N), Bangladesh tour of South Africa | Buffalo Park, KuGompo City | Dec 1, 2026, 13:30 local | XI not announced**

A Test in this series is live right now. In the 2nd Test at Centurion, Bangladesh trail by 315 runs, and the market makes South Africa about 1.01 favourites. I've previewed the next white-ball match instead, since our model serves win probability for ODIs but not Tests.

**Ratings (men's ODI):** South Africa 1685 (5th) vs Bangladesh 1570 (8th).
**Our pregame win probability:** South Africa 64.5% / Bangladesh 35.5%. South Africa also have home advantage.
**Market:** no ODI prices are posted yet, so there's no market comparison or gap to our model.

**Venue (Buffalo Park, 15 ODIs since 2003, last one Dec 2025):**
- Par is 239 for the first innings and 178 for the second. The second-innings average is pulled down by chases that fell short.
- Batting first won 9 of 15 (64.3%). The standard error is about 12 points, so that isn't a real edge.
- Toss winners won 64.3%, and 5 of 15 captains chose to field. The sample is small, so I wouldn't call the toss a factor.
- This is the all-time view. I didn't pull a recent-era split.

**Form (newest first):**
- **South Africa:**
  - W vs Australia, Sep 30, by 45 runs (D/L)? The tool lists this as an Australia win, so it was a loss for South Africa.
  - W vs Australia, Sep 27, by 32 runs
  - W vs Australia, Sep 24, by 67 runs
  - W vs Namibia, Sep 13, by 9 wickets
  - W vs Namibia, Sep 11, by 157 runs
  - Corrected record: L, W, W, W, W.
- **Bangladesh:**
  - L vs Zimbabwe, Oct 17, by 99 runs (Abu Dhabi)
  - W vs Zimbabwe, Jul 11, by 7 wickets
  - L vs Zimbabwe, Jul 9, by 13 runs
  - L vs Zimbabwe, Jul 6, by 25 runs
  - L vs Australia, Jun 14, by 1 wicket

**Head to head (all formats, newest first; the list lags and doesn't include the 1st Test of this series):**
- South Africa won the Test in Chattogram, Oct 29, 2024, by an innings and 273 runs.
- South Africa won the Test in Mirpur, Oct 21, 2024, by 7 wickets.
- South Africa won the T20I at the 2024 T20 World Cup, Jun 10, 2024, by 4 runs.
- South Africa won the ODI at the 2023 World Cup, Oct 24, 2023, by 149 runs (382/5 to 233).
- South Africa won the T20I at the 2022 T20 World Cup, Oct 27, 2022, by 104 runs.

These are five wins from five, but only one is an ODI.

**What to watch:**
- The rating gap is 115 points. That gives roughly 66% before adjustments, close to the served 64.5%.
- Bangladesh's recent ODI form is poor, with four losses in five, including three to a side rated 1415.
- South Africa's batting depth has been scoring heavily: 365, 335 and 297 in their last five ODIs. Buffalo Park's par of 239 is lower than that.

**Not covered:** player phase splits and matchups (I didn't pull them, so I can't name key batters or bowlers), and ODI odds (none posted).

Data: get_schedule, get_ratings, get_venue, get_matches, get_odds | ODI, 2026/27

I can also preview the live 2nd Test or the T20Is that start Dec 10.
