#!/usr/bin/env python3
"""Regenerates catalog.json from every plugins/*/skills/*/SKILL.md. Run after adding or renaming a skill."""
import json, glob, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
rows = []
for f in sorted(ROOT.glob("plugins/*/skills/*/SKILL.md")):
    plugin, name = f.parts[-4], f.parent.name
    d = re.search(r'^description:\s*"?(.*?)"?\s*$', f.read_text().split("---")[1], re.M).group(1)
    rows.append({"name": name, "plugin": plugin, "description": d, "reads_live_data": plugin != "sports-analytics-core" or name in ("sports-data-preflight", "market-vs-model", "odds-market-analysis"), "writes": False, "moves_money": False})
(ROOT / "catalog.json").write_text(json.dumps({"generated_from": "plugins/*/skills/*/SKILL.md", "skills": rows}, indent=1))
print(len(rows), "skills in catalog.json")
