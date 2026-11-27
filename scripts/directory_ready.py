#!/usr/bin/env python3
"""Give every plugin what the Claude directory checks for: a README that says what it does and what data it sends,
a LICENSE, an icon and a privacy policy link in plugin.json. Re-run after adding a plugin; it rewrites only these files.

    python3 scripts/directory_ready.py ICONS_DIR

ICONS_DIR holds <brand>.png (512x512) for each brand, plus sportsdatahq.png for the core plugin.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ICONS = Path(sys.argv[1])
CORE = "sports-analytics-core"


def brand_of(plugin: Path) -> tuple[str, str]:
    """(brand name, domain) from the plugin's MCP server, or SportsDataHQ for the core."""
    if plugin.name == CORE:
        return "SportsDataHQ", "sportsdatahq.com"
    servers = json.loads((plugin / ".mcp.json").read_text())["mcpServers"]
    url = next(iter(servers.values()))["url"]
    domain = url.split("//", 1)[1].split("/", 1)[0].removeprefix("mcp.")
    return json.loads((plugin / ".claude-plugin" / "plugin.json").read_text())["displayName"].split(":")[0], domain


def skill_lines(plugin: Path) -> list[str]:
    out = []
    for s in sorted((plugin / "skills").iterdir()):
        md = s / "SKILL.md"
        if not md.exists():
            continue
        desc = ""
        for line in md.read_text().splitlines():
            if line.startswith("description:"):
                desc = line.split(":", 1)[1].strip().strip('"').split(": '")[0].split(". ")[0].rstrip(".:")
                break
        out.append(f"- `{s.name}`: {desc}." if desc else f"- `{s.name}`")
    return out


for plugin in sorted((ROOT / "plugins").iterdir()):
    manifest_path = plugin / ".claude-plugin" / "plugin.json"
    m = json.loads(manifest_path.read_text())
    brand, domain = brand_of(plugin)
    privacy = "https://app.sportsdatahq.com/privacy" if plugin.name == CORE else f"https://{domain}/privacy"
    icon_src = ICONS / ("sportsdatahq.png" if plugin.name == CORE else f"{brand.lower()}.png")
    shutil.copy(icon_src, plugin / ".claude-plugin" / "icon.png")
    shutil.copy(ROOT / "LICENSE", plugin / "LICENSE")
    m["privacyPolicyUrl"] = privacy
    m["icon"] = ".claude-plugin/icon.png"
    manifest_path.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n")

    if plugin.name == CORE:
        data = ("These skills hold methods only (modelling, validation, metrics). They make no calls of their own; "
                "the numbers come from whichever SportsDataHQ sport plugin you also install.")
    else:
        data = (f"The skills call the {brand} MCP server at `mcp.{domain}`. Each call sends the tool name and its inputs "
                f"(teams, players, dates, seasons) with your {brand} API key, and returns data. Nothing from your files or "
                f"conversation is sent beyond what a tool call needs. Calls use credits on your {brand} account; "
                f"a free key at https://{domain}/signup includes monthly credits.")
    readme = "\n".join([
        f"# {m['displayName']}",
        "",
        m["description"],
        "",
        "## Skills",
        "",
        *skill_lines(plugin),
        "",
        "## Data it sends",
        "",
        data,
        "",
        f"Privacy policy: {privacy}",
        "",
        "## Install",
        "",
        "```",
        "/plugin marketplace add sports-data-hq/sportsdatahq-skills",
        f"/plugin install {plugin.name}@sportsdatahq",
        "```",
        "",
        f"More: {m['homepage']}. Licence: MIT (see LICENSE).",
        "",
    ])
    (plugin / "README.md").write_text(readme)
    print(f"{plugin.name}: {brand} ({domain})")
