#!/usr/bin/env python3
"""Copy shared rules and templates into each skill so every skill is self-contained.

Each SKILL.md lists what it needs in its frontmatter metadata:
  shared: "anti-slop,evidence-rule"   -> copied to references/<name>.md
  templates: "break-report"           -> copied to assets/<name>.md

Run with --check to fail (exit 1) when any copy is missing or differs from its source.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
TEMPLATES = ROOT / "templates"
SKILLS = ROOT / "skills"

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def read_list(frontmatter: str, key: str) -> list[str]:
    match = re.search(rf'^\s+{key}:\s*"([^"]*)"\s*$', frontmatter, re.M)
    if not match:
        return []
    return [item.strip() for item in match.group(1).split(",") if item.strip()]


def plan(skill_dir: Path) -> list[tuple[Path, Path]]:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        raise ValueError(f"{skill_dir.name}: SKILL.md has no frontmatter")
    frontmatter = match.group(1)
    pairs = []
    for name in read_list(frontmatter, "shared"):
        pairs.append((SHARED / f"{name}.md", skill_dir / "references" / f"{name}.md"))
    for name in read_list(frontmatter, "templates"):
        pairs.append((TEMPLATES / f"{name}.md", skill_dir / "assets" / f"{name}.md"))
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify only, do not write")
    args = parser.parse_args()

    problems = []
    copied = 0
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        for source, target in plan(skill_dir):
            if not source.exists():
                problems.append(f"{skill_dir.name}: missing source {source.relative_to(ROOT)}")
                continue
            same = target.exists() and target.read_bytes() == source.read_bytes()
            if args.check:
                if not same:
                    problems.append(f"{skill_dir.name}: {target.relative_to(ROOT)} is missing or out of date")
            elif not same:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
                copied += 1

    for line in problems:
        print(f"ERROR {line}")
    if problems:
        print("Run: python scripts/sync_shared.py")
        return 1
    print("check passed" if args.check else f"synced, {copied} file(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
