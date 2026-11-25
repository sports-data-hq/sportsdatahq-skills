#!/usr/bin/env python3
"""Checks every skill: frontmatter, name = folder, description length and form, house rules, and that every
tool it names exists on its sport's API (scripts/tools.json, refreshed from the live tool lists)."""
import json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOLS = json.loads((ROOT / "scripts/tools.json").read_text())
SPORT_OF = {"nhl-data": "nhl", "nfl-data": "nfl", "nba-data": "nba", "mlb-data": "mlb", "soccer-data": "soccer", "tennis-data": "tennis", "golf-data": "golf", "mma-data": "mma", "cricket-data": "cricket"}
ALL_TOOLS = set().union(*TOOLS.values())
BANNED = re.compile(r"\b(kelly|bankroll|unit siz|stake siz|bet siz|best bets?|value bets?|lock of the|how much to (bet|wager))\b", re.I)
problems = []
for skill in sorted(ROOT.glob("plugins/*/skills/*/SKILL.md")):
    plugin, name = skill.parts[-4], skill.parent.name
    text = skill.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m: problems.append(f"{skill}: no frontmatter"); continue
    fm = m.group(1)
    fname = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r'^description:\s*"?(.*?)"?\s*$', fm, re.M)
    if not fname or fname.group(1).strip() != name: problems.append(f"{name}: name != folder")
    if not desc: problems.append(f"{name}: no description")
    else:
        d = desc.group(1)
        if len(d) > 1024: problems.append(f"{name}: description {len(d)} chars")
        if not re.match(r"Use (when|this skill when|before)", d): problems.append(f"{name}: description should start 'Use when'")
    if "—" in text: problems.append(f"{name}: em dash")
    for b in BANNED.finditer(text): problems.append(f"{name}: banned term '{b.group(0)}'")
    if len(text.splitlines()) > 500: problems.append(f"{name}: over 500 lines")
    sport = SPORT_OF.get(plugin)
    known = set(TOOLS[sport]) if sport else ALL_TOOLS
    for t in set(re.findall(r"`((?:get|list|search)_[a-z_]+)", text)):
        if t not in known: problems.append(f"{name}: tool {t} not on {sport or 'any'} API")
print(f"{len(list(ROOT.glob('plugins/*/skills/*/SKILL.md')))} skills checked")
for p in problems: print("PROBLEM", p)
sys.exit(1 if problems else 0)
