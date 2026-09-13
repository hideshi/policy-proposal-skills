#!/usr/bin/env python3
"""Validate SKILL.md frontmatter for Codex compatibility and catalog consistency."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills" / "ja"
ALLOWED = {"name", "description", "license", "allowed-tools", "metadata"}


def check_one(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    path = skill_dir / "SKILL.md"
    if not path.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return [f"{skill_dir.name}: invalid frontmatter"]
    body = m.group(1)
    if yaml is None:
        if not re.search(r"^name:\s*[a-z0-9-]+", body, re.M):
            errors.append(f"{skill_dir.name}: missing name")
        if "description:" not in body:
            errors.append(f"{skill_dir.name}: missing description")
        if re.search(r"^version:", body, re.M):
            errors.append(
                f"{skill_dir.name}: top-level version not allowed; use metadata.version"
            )
        return errors
    data = yaml.safe_load(body)
    if not isinstance(data, dict):
        return [f"{skill_dir.name}: frontmatter must be a mapping"]
    unexpected = set(data) - ALLOWED
    if unexpected:
        errors.append(f"{skill_dir.name}: unexpected keys {sorted(unexpected)}")
    name = data.get("name")
    if name != skill_dir.name:
        errors.append(f"{skill_dir.name}: name '{name}' != directory")
    desc = data.get("description")
    if not isinstance(desc, str) or not desc.strip():
        errors.append(f"{skill_dir.name}: empty description")
    meta = data.get("metadata")
    if meta is not None and not isinstance(meta, dict):
        errors.append(f"{skill_dir.name}: metadata must be a mapping")
    return errors


def main() -> int:
    if not SKILLS.is_dir():
        print("skills/ja not found", file=sys.stderr)
        return 2
    errs: list[str] = []
    for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        errs.extend(check_one(d))
    if errs:
        print("FAIL")
        for e in errs:
            print(f"- {e}")
        return 1
    print("PASS: skill frontmatter ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
