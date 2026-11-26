#!/usr/bin/env python3
"""Copy each sport's plugin (plus the analytics core) into that sport's own public repo.

The skills are written and reviewed once, here. Each sport repo (dunkapi-mcp and so on) is a front door: it carries
its sport's skills and installs on its own (`/plugin marketplace add sports-data-hq/dunkapi-mcp`), but never edits
them. Run after any skill change:

    python3 scripts/sync_sport_repos.py WORKDIR [--push] [--only nba,nhl]

Without --push it prepares each repo in WORKDIR and prints the diff stat, nothing leaves the machine.
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE = "sports-analytics-core"
SPORT_DIR = {"nhl-data": "nhl", "nfl-data": "nfl", "nba-data": "nba", "mlb-data": "mlb", "soccer-data": "soccer",
             "tennis-data": "tennis", "golf-data": "golf", "mma-data": "mma", "cricket-data": "cricket"}

# plugin -> (repo, marketplace name, brand, domain, sport words, repo description lead, topics)
SPORTS = {
    "nhl-data": ("PuckAPI/mcp", "puckapi", "PuckAPI", "puckapi.com", "hockey",
                 "PuckAPI: NHL and minor-league hockey data for AI agents", ["nhl", "hockey", "expected-goals"]),
    "nfl-data": ("sports-data-hq/endzoneapi-mcp", "endzoneapi", "EndzoneAPI", "endzoneapi.com", "football",
                 "EndzoneAPI: NFL and college football data for AI agents", ["nfl", "football", "epa"]),
    "nba-data": ("sports-data-hq/dunkapi-mcp", "dunkapi", "DunkAPI", "dunkapi.com", "basketball",
                 "DunkAPI: NBA, WNBA and college basketball data for AI agents", ["nba", "basketball", "shot-chart"]),
    "mlb-data": ("sports-data-hq/fastballapi-mcp", "fastballapi", "FastballAPI", "fastballapi.com", "baseball",
                 "FastballAPI: MLB and college baseball data for AI agents", ["mlb", "baseball", "statcast"]),
    "soccer-data": ("sports-data-hq/strikerapi-mcp", "strikerapi", "StrikerAPI", "strikerapi.com", "soccer",
                    "StrikerAPI: soccer data for 17 leagues for AI agents", ["soccer", "football-data", "xg"]),
    "tennis-data": ("sports-data-hq/acesapi-mcp", "acesapi", "AcesAPI", "acesapi.com", "tennis",
                    "AcesAPI: ATP and WTA tennis data for AI agents", ["tennis", "atp", "wta"]),
    "golf-data": ("sports-data-hq/birdieapi-mcp", "birdieapi", "BirdieAPI", "birdieapi.com", "golf",
                  "BirdieAPI: PGA Tour and five more tours' golf data for AI agents", ["golf", "pga-tour", "strokes-gained"]),
    "mma-data": ("sports-data-hq/fighterapi-mcp", "fighterapi", "FighterAPI", "fighterapi.com", "UFC",
                 "FighterAPI: UFC fight data for AI agents", ["ufc", "mma", "fight-data"]),
    "cricket-data": ("sports-data-hq/yorkerapi-mcp", "yorkerapi", "YorkerAPI", "yorkerapi.com", "cricket",
                     "YorkerAPI: ball-by-ball cricket data for AI agents", ["cricket", "ipl", "ball-by-ball"]),
}

CATALOG = {s["name"]: s for s in json.loads((ROOT / "catalog.json").read_text())["skills"]}
SUMMARIES = json.loads((ROOT / "scripts" / "summaries.json").read_text())


def short(desc: str) -> str:
    """The catalog descriptions are trigger specs; the README wants what the skill does, in one line."""
    t = re.sub(r"^Use (this )?when (the user |someone )?(asks|wants|needs)( to| for| about)? ?", "", desc)
    t = t.split(":")[0].split(". ")[0].strip().rstrip(".")
    return (t[0].upper() + t[1:]) if t else t


def skills_of(plugin: str) -> list[str]:
    return sorted(p.parent.name for p in (ROOT / "plugins" / plugin / "skills").glob("*/SKILL.md"))


def manifests(plugin: str, market: str) -> dict[str, dict]:
    """The three marketplace files, each filtered to this sport and the core and renamed to the sport repo's market."""
    out = {}
    for rel in (".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json", ".cursor-plugin/marketplace.json"):
        src = ROOT / rel
        if not src.exists():
            continue
        m = json.loads(src.read_text())
        m["name"] = market
        m["plugins"] = [p for p in m["plugins"] if p["name"] in (plugin, CORE)]
        out[rel] = m
    return out


def readme_section(plugin: str, repo: str, market: str, brand: str, sport: str) -> str:
    own, core = skills_of(plugin), skills_of(CORE)
    rows = "\n".join(f"| `{n}` | {SUMMARIES.get(n) or short(CATALOG[n]['description'])} |" for n in own)
    return f"""## Skills

{len(own)} Claude skills for {sport} ship in this repo, plus {len(core)} analytics skills for models, backtests, calibration and comparing a model with the market. Every number in an answer comes from a live {brand} tool call, and odds are information only: no stakes, no picks.

Claude Code:

```
/plugin marketplace add {repo}
/plugin install {plugin}@{market}
/plugin install {CORE}@{market}
```

Codex: `codex plugin marketplace add {repo}`. Any agent that reads skills: `npx skills add {repo}`.

| Skill | What it does |
|---|---|
{rows}

The analytics skills: {", ".join(f"`{n}`" for n in core)}.

Real answers on live data, with the credits each used: [example answers](https://github.com/sports-data-hq/sportsdatahq-skills/tree/main/docs/examples/{SPORT_DIR[plugin]}).

All nine sports' skills live in [sports-data-hq/sportsdatahq-skills](https://github.com/sports-data-hq/sportsdatahq-skills). The copies here are synced from there, so please open issues and pull requests there.

"""


def replace_section(readme: str, new: str) -> str:
    m = re.search(r"^## Skills\n.*?(?=^## )", readme, flags=re.S | re.M)
    if m:
        return readme[: m.start()] + new + readme[m.end():]
    m = re.search(r"^## ", readme, flags=re.M)  # no section yet: put it before the first heading after the intro
    return readme[: m.start()] + new + readme[m.start():] if m else readme + "\n" + new


def run(cmd, cwd=None, check=True):
    return subprocess.run(cmd, cwd=cwd, check=check, text=True, capture_output=True)


def main():
    work = Path(sys.argv[1]).resolve()
    push = "--push" in sys.argv
    only = None
    if "--only" in sys.argv:
        only = {f"{s}-data" for s in sys.argv[sys.argv.index("--only") + 1].split(",")}
    work.mkdir(parents=True, exist_ok=True)
    for plugin, (repo, market, brand, domain, sport, lead, topics) in SPORTS.items():
        if only and plugin not in only:
            continue
        dest = work / repo.split("/")[1]
        if dest.exists():
            shutil.rmtree(dest)
        run(["gh", "repo", "clone", repo, str(dest), "--", "-q", "--depth", "1"])
        if (dest / "plugins").exists():
            shutil.rmtree(dest / "plugins")
        for p in (plugin, CORE):
            shutil.copytree(ROOT / "plugins" / p, dest / "plugins" / p)
        for rel, m in manifests(plugin, market).items():
            (dest / rel).parent.mkdir(parents=True, exist_ok=True)
            (dest / rel).write_text(json.dumps(m, indent=2) + "\n")
        readme = dest / "README.md"
        readme.write_text(replace_section(readme.read_text(), readme_section(plugin, repo, market, brand, sport)))
        n = len(skills_of(plugin))
        desc = f"{lead}. Remote MCP server, REST API and {n} Claude skills, plus {len(skills_of(CORE))} analytics skills."
        run(["git", "add", "-A"], cwd=dest)
        stat = run(["git", "diff", "--cached", "--shortstat"], cwd=dest).stdout.strip()
        print(f"{repo}: {stat or 'no change'}")
        if push and stat:
            run(["git", "commit", "-q", "-m", f"Ship the {sport} skills in this repo\n\nSynced from sports-data-hq/sportsdatahq-skills: the {plugin} plugin and {CORE}, with marketplace files for Claude Code, Codex and Cursor, and a README skills section."], cwd=dest)
            run(["git", "push", "-q"], cwd=dest)
        if push:
            run(["gh", "repo", "edit", repo, "--description", desc,
                 *[a for t in ["claude-skills", "agent-skills", "mcp", "claude-code", "sports-data", *topics] for a in ("--add-topic", t)]])
            print(f"  description: {desc}")


if __name__ == "__main__":
    main()
