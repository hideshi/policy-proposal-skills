#!/usr/bin/env python3
"""Lightweight structural checks for a challenges/<slug> directory."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "challenge.md",
    "variables.md",
    "sources-index.md",
    "findings.md",
    "options.md",
    "claim-evidence.md",
]


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "usage: check_challenge_artifacts.py /path/to/challenges/<slug>",
            file=sys.stderr,
        )
        return 2
    root = Path(sys.argv[1]).resolve()
    errs: list[str] = []
    warns: list[str] = []
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    for name in REQUIRED_FILES:
        if not (root / name).exists():
            errs.append(f"missing {name}")

    src_index = root / "sources-index.md"
    if src_index.exists():
        body = src_index.read_text(encoding="utf-8")
        for block in re.split(r"^###\s+", body, flags=re.M):
            stripped = block.strip()
            if not stripped.startswith("SRC-"):
                continue
            sid_m = re.match(r"(SRC-\d+)", stripped)
            if not sid_m:
                continue
            sid = sid_m.group(1)
            if "sha256:" not in block.lower() and "sha256：" not in block:
                errs.append(f"{sid}: sha256 field missing")
            path_m = re.search(r"ローカルパス[:：]\s*(\S+)", block)
            if path_m:
                rel = path_m.group(1).strip()
                if rel and rel not in {"sources/", "sources"} and not rel.endswith("/"):
                    fp = root / rel
                    if not fp.exists():
                        errs.append(f"{sid}: missing file {rel}")

    findings = root / "findings.md"
    if findings.exists():
        fb = findings.read_text(encoding="utf-8")
        if re.search(r"^###\s+F-\d+", fb, re.M):
            if "locator:" not in fb and "locator：" not in fb:
                errs.append("findings.md: locator field not found")
            elif re.search(r"locator[:：]\s*$", fb, re.M):
                warns.append("findings.md: empty locator placeholder present")

    options = root / "options.md"
    if options.exists():
        ob = options.read_text(encoding="utf-8")
        if "OPT-現状維持" not in ob and "現状維持" not in ob:
            warns.append("options.md: 現状維持案 not found")
        if re.search(r"有力|推奨", ob) and "決定主体" not in ob:
            errs.append("options.md: ranking language without 評価設定")

    if errs:
        print("FAIL")
        for e in errs:
            print(f"- {e}")
        for w in warns:
            print(f"WARN: {w}")
        return 1
    print("PASS: challenge artifacts structurally ok")
    for w in warns:
        print(f"WARN: {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
