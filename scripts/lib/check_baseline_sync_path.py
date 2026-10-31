#!/usr/bin/env python3
"""Reject managed baseline paths that leave a physical repository root."""

from __future__ import annotations

import argparse
from pathlib import Path
import stat
import sys


def is_indirect_path(path: Path) -> bool:
    try:
        metadata = path.lstat()
    except FileNotFoundError:
        return False
    return (
        stat.S_ISLNK(metadata.st_mode)
        or bool(getattr(metadata, "st_file_attributes", 0) & 0x400)  # Windows reparse point, including junctions.
        or (stat.S_ISREG(metadata.st_mode) and metadata.st_nlink > 1)
    )


def is_safe(root: Path, target: Path) -> bool:
    try:
        root = root.absolute()
        target = target.absolute()
        relative = target.relative_to(root)
        if relative.parts[:2] != ("docs", "secure-development") or ".." in relative.parts:
            return False
        managed_root = root / "docs" / "secure-development"
        if is_indirect_path(root):
            return False
        parent = root
        for part in relative.parts[:-1]:
            parent /= part
            if is_indirect_path(parent):
                return False
        target.parent.resolve(strict=False).relative_to(managed_root.resolve(strict=False))
        managed_root.resolve(strict=False).relative_to(root.resolve(strict=True))
    except (OSError, ValueError):
        return False
    return not is_indirect_path(target)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--path", type=Path, required=True)
    arguments = parser.parse_args()
    if not is_safe(arguments.root, arguments.path):
        print("Managed baseline path leaves its repository or is a symlink", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
