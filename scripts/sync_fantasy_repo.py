#!/usr/bin/env python3
"""Build the fantasy and DFS repo (sports-data-hq/fantasy-sports-skills) from the fantasy skills in each sport plugin.

The skills are written and reviewed here, inside their sport plugins. The fantasy repo collects them into one
plugin wired to the SportsDataHQ per-sport servers, so one account and one sign-in cover every sport.

    python3 scripts/sync_fantasy_repo.py WORKDIR [--push]
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "sports-data-hq/fantasy-sports-skills"
PLUGIN = "fantasy-sports"
MARKET = "sportsdatahq-fantasy"
SPORTS = {"nfl-data": ("nfl", "NFL"), "nba-data": ("nba", "NBA"), "mlb-data": ("mlb", "MLB"),
          "nhl-data": ("nhl", "NHL"), "soccer-data": ("soccer", "Fantasy Premier League")}
IS_FANTASY = re.compile(r"(fantasy|dfs|fpl)")
SUMMARIES = json.loads((ROOT / "scripts" / "summaries.json").read_text())
VERSION = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())["metadata"]["version"]
SIGNUP = "https://app.sportsdatahq.com/signup?utm_source=github&utm_medium=fantasy-repo&utm_campaign=fantasy-sports-skills"


def run(cmd, cwd=None, check=True):
    return subprocess.run(cmd, cwd=cwd, check=check, text=True, capture_output=True)


def collect():
    out = []
    for plugin, (sport, label) in SPORTS.items():
        for d in sorted((ROOT / "plugins" / plugin / "skills").iterdir()):
            if IS_FANTASY.search(d.name) and (d / "SKILL.md").exists():
                out.append((label, d))
    return out


def readme(skills):
    rows = "\n".join(f"| {label} | `{d.name}` | {SUMMARIES.get(d.name, '')} |" for label, d in skills)
    return f"""# Fantasy and DFS skills for Claude

{len(skills)} Claude skills for fantasy football, fantasy basketball, baseball and hockey, daily fantasy and Fantasy Premier League. They rank your players from real usage, injuries, depth charts and schedules, and use the market's per-player lines as projections, so every number comes from live data, not a guess.

```
/plugin marketplace add {REPO}
/plugin install {PLUGIN}@{MARKET}
```

Codex: `codex plugin marketplace add {REPO}`. Any agent that reads skills: `npx skills add {REPO}`.

The first tool call asks you to sign in to SportsDataHQ: one free account covers every sport here, with 1,000 credits a month and no card. [Create it now]({SIGNUP}).

## Skills

| Sport | Skill | What it does |
|---|---|---|
{rows}

## How the projections work

- **The market as a projection.** A player's prop line is the market's median for that stat. The skills turn lines into fantasy points with your league's scoring, and show the formula.
- **Usage first.** Snap share, targets, carries, minutes, plate appearances, ice time and power-play role, with the trend, because role changes before results do.
- **Schedules.** Games per team in the window, back-to-backs, and fixture difficulty for FPL.
- **What you paste.** Salaries, ADP, ownership, your league's scoring and FPL prices aren't in the data, so the skills ask for them rather than invent them.
- **Sample sizes on every rate,** and a plain "not enough data" when there isn't.

DFS skills build lineups under the cap from your salary file. They never advise on entries, contests or bankroll. Odds are used only as information.

## Example answers

Real runs on live data: [start/sit](https://github.com/sports-data-hq/sportsdatahq-skills/blob/main/docs/examples/nfl/04-fantasy-should-i-start-bijan-robinson-or-jahmyr-gibbs-this-w.md), [NFL waivers](https://github.com/sports-data-hq/sportsdatahq-skills/blob/main/docs/examples/nfl/05-best-waiver-wire-pickups-this-week-for-fantasy-football.md), [NBA streaming](https://github.com/sports-data-hq/sportsdatahq-skills/blob/main/docs/examples/nba/04-which-players-should-i-stream-this-week-in-fantasy-basketbal.md), [FPL captain](https://github.com/sports-data-hq/sportsdatahq-skills/blob/main/docs/examples/soccer/04-fpl-captain-this-gameweek-haaland-salah-palmer-or-saka-defau.md).

## More

- Every sport's full analysis skills (previews, props research, ratings, models): [sports-data-hq/sportsdatahq-skills](https://github.com/sports-data-hq/sportsdatahq-skills).
- These skills are synced from that repo, so please open issues and pull requests there.

MIT licensed. Data from the SportsDataHQ APIs, used under their terms.
"""


def main():
    work = Path(sys.argv[1]).resolve()
    push = "--push" in sys.argv
    dest = work / REPO.split("/")[1]
    exists = run(["gh", "repo", "view", REPO], check=False).returncode == 0
    if dest.exists():
        shutil.rmtree(dest)
    if exists:
        run(["gh", "repo", "clone", REPO, str(dest), "--", "-q"])
    else:
        dest.mkdir(parents=True)
        run(["git", "init", "-q", "-b", "main"], cwd=dest)
    for p in ("plugins", ".claude-plugin", ".agents"):
        if (dest / p).exists():
            shutil.rmtree(dest / p)
    skills = collect()
    pdir = dest / "plugins" / PLUGIN
    for label, d in skills:
        shutil.copytree(d, pdir / "skills" / d.name)
    shutil.copytree(ROOT / "plugins" / "sports-analytics-core", dest / "plugins" / "sports-analytics-core")
    (pdir / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (pdir / ".claude-plugin" / "plugin.json").write_text(json.dumps({
        "name": PLUGIN, "displayName": "SportsDataHQ: fantasy and DFS", "version": VERSION,
        "description": "Fantasy and DFS skills for the NFL, NBA, MLB, NHL and Fantasy Premier League: start/sit, waivers, draft boards, trade value, streaming and salary-cap lineups from live usage, injuries, schedules and the market's per-player lines.",
        "author": {"name": "SportsDataHQ", "url": "https://sportsdatahq.com"},
        "homepage": f"https://github.com/{REPO}", "repository": f"https://github.com/{REPO}", "license": "MIT",
        "keywords": ["fantasy-football", "fantasy-basketball", "dfs", "fpl", "fantasy-baseball", "fantasy-hockey", "sports-data"],
    }, indent=2) + "\n")
    (pdir / ".mcp.json").write_text(json.dumps({"mcpServers": {
        f"sportsdatahq-{sport}": {"type": "http", "url": f"https://mcp.sportsdatahq.com/mcp/{sport}"}
        for sport, _ in SPORTS.values()}}, indent=2) + "\n")
    market = {"name": MARKET, "owner": {"name": "SportsDataHQ", "url": "https://sportsdatahq.com"},
              "metadata": {"description": "Fantasy and DFS skills for Claude, on live sports data.", "version": VERSION},
              "plugins": [{"name": PLUGIN, "source": f"./plugins/{PLUGIN}", "version": VERSION,
                           "description": "Fantasy and DFS skills for the NFL, NBA, MLB, NHL and FPL."},
                          {"name": "sports-analytics-core", "source": "./plugins/sports-analytics-core", "version": VERSION,
                           "description": "Models, backtests, calibration and charts for any sport."}]}
    (dest / ".claude-plugin").mkdir(exist_ok=True)
    (dest / ".claude-plugin" / "marketplace.json").write_text(json.dumps(market, indent=2) + "\n")
    codex = {"name": MARKET, "interface": {"displayName": "SportsDataHQ fantasy and DFS"}, "plugins": [
        {"name": n, "source": {"source": "local", "path": f"./plugins/{n}"},
         "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": "Developer Tools"}
        for n in (PLUGIN, "sports-analytics-core")]}
    (dest / ".agents" / "plugins").mkdir(parents=True, exist_ok=True)
    (dest / ".agents" / "plugins" / "marketplace.json").write_text(json.dumps(codex, indent=2) + "\n")
    (dest / "README.md").write_text(readme(skills))
    shutil.copy(ROOT / "LICENSE", dest / "LICENSE")
    run(["git", "add", "-A"], cwd=dest)
    stat = run(["git", "diff", "--cached", "--shortstat"], cwd=dest).stdout.strip()
    print(f"{REPO}: {len(skills)} skills; {stat or 'no change'}")
    if not push or not stat:
        return
    run(["git", "commit", "-q", "-m", f"Sync fantasy and DFS skills ({VERSION})"], cwd=dest)
    if not exists:
        run(["gh", "repo", "create", REPO, "--public", "--source", str(dest), "--push", "--description",
             f"{len(skills)} Claude skills for fantasy football, basketball, baseball and hockey, DFS lineups and Fantasy Premier League, on live sports data."])
        for t in ["claude-skills", "fantasy-football", "dfs", "fpl", "fantasy-basketball", "fantasy-baseball", "fantasy-hockey", "mcp", "claude-code", "sports-data"]:
            run(["gh", "repo", "edit", REPO, "--add-topic", t])
    else:
        run(["git", "push", "-q"], cwd=dest)
    print(f"pushed https://github.com/{REPO}")


if __name__ == "__main__":
    main()
