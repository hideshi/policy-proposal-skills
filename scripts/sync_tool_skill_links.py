#!/usr/bin/env python3
"""Create/refresh tool adapter symlinks into skills/ja.

Canonical skills live in skills/ja/<name>/SKILL.md.
Adapters (do not edit skill bodies here):
  .agents/skills/  — Codex, Antigravity, Cursor
  .claude/skills/  — Claude Code (Cursor also reads)
  .cursor/skills/  — Cursor
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "skills" / "ja"
ADAPTERS = [
    ROOT / ".agents" / "skills",
    ROOT / ".claude" / "skills",
    ROOT / ".cursor" / "skills",
]
# from <adapter>/<name> to skills/ja/<name>
REL = Path("../../skills/ja")


def main() -> int:
    if not CANON.is_dir():
        print(f"missing {CANON}", file=sys.stderr)
        return 2
    skills = sorted(p for p in CANON.iterdir() if p.is_dir() and (p / "SKILL.md").exists())
    if not skills:
        print("no skills found", file=sys.stderr)
        return 1
    for adapter in ADAPTERS:
        adapter.mkdir(parents=True, exist_ok=True)
        # remove stale symlinks
        for child in list(adapter.iterdir()):
            if child.is_symlink() and child.name not in {s.name for s in skills}:
                child.unlink()
                print(f"removed stale {child.relative_to(ROOT)}")
        for sk in skills:
            link = adapter / sk.name
            target = REL / sk.name
            if link.is_symlink() or link.exists():
                if link.is_symlink():
                    if link.readlink() == target:
                        continue
                    link.unlink()
                else:
                    print(f"refusing to overwrite non-symlink {link}", file=sys.stderr)
                    return 3
            link.symlink_to(target)
            print(f"link {link.relative_to(ROOT)} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
