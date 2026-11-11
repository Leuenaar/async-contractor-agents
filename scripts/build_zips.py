#!/usr/bin/env python3
"""Build one upload-ready zip per skill in dist/, for claude.ai Customize > Skills > Upload."""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"


def main() -> int:
    DIST.mkdir(exist_ok=True)
    count = 0
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        target = DIST / f"{skill_dir.name}.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
            for file in sorted(skill_dir.rglob("*")):
                if file.is_file():
                    archive.write(file, Path(skill_dir.name) / file.relative_to(skill_dir))
        count += 1
    print(f"{count} zip(s) written to {DIST.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
