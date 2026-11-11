#!/usr/bin/env python3
"""Validate every skill against the Agent Skills format and this repo's own rules.

Checks:
- frontmatter exists with name and description
- name: 1-64 chars, lowercase letters, digits, single hyphens, matches folder
- description: 1-1024 chars, no ": " (strict YAML)
- SKILL.md body under 500 lines
- every relative link in SKILL.md points to a file that exists
- no em dash in SKILL.md, or in shared rules outside inline code examples
- SKILL.md has a "Done when" section
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
LINK_RE = re.compile(r"\]\(([^)#\s]+)\)")
EM_DASH = chr(0x2014)
INLINE_CODE = re.compile(r"`[^`\n]*`")


def field(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"^{key}:\s*(.+)$", frontmatter, re.M)
    return match.group(1).strip().strip('"') if match else None


def check_skill(skill_dir: Path) -> list[str]:
    errors = []
    path = skill_dir / "SKILL.md"
    if not path.exists():
        return [f"{skill_dir.name}: SKILL.md missing"]
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        return [f"{skill_dir.name}: no frontmatter"]
    frontmatter, body = match.group(1), text[match.end():]

    name = field(frontmatter, "name")
    description = field(frontmatter, "description")
    if not name:
        errors.append(f"{skill_dir.name}: name missing")
    else:
        if len(name) > 64 or not NAME_RE.match(name):
            errors.append(f"{skill_dir.name}: invalid name '{name}'")
        if name != skill_dir.name:
            errors.append(f"{skill_dir.name}: name '{name}' does not match folder")
    if not description:
        errors.append(f"{skill_dir.name}: description missing")
    elif len(description) > 1024:
        errors.append(f"{skill_dir.name}: description is {len(description)} chars (max 1024)")
    elif ": " in description or " #" in description:
        errors.append(f"{skill_dir.name}: description has ': ' or ' #', which breaks strict YAML (reword it)")

    lines = body.count("\n")
    if lines >= 500:
        errors.append(f"{skill_dir.name}: body is {lines} lines (max 499)")
    if "## Done when" not in body:
        errors.append(f"{skill_dir.name}: no 'Done when' section")
    if EM_DASH in text:
        errors.append(f"{skill_dir.name}: em dash found in SKILL.md")

    for target in LINK_RE.findall(body):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (skill_dir / target).exists():
            errors.append(f"{skill_dir.name}: broken link {target}")
    return errors


def main() -> int:
    errors = []
    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for skill_dir in skill_dirs:
        errors.extend(check_skill(skill_dir))
    for rule in sorted((ROOT / "shared").glob("*.md")):
        if EM_DASH in INLINE_CODE.sub("", rule.read_text(encoding="utf-8")):
            errors.append(f"shared/{rule.name}: em dash found outside inline code")
    for line in errors:
        print(f"ERROR {line}")
    print(f"{len(skill_dirs)} skills checked, {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
