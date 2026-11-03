#!/usr/bin/env python3
"""Reject linked paths in an existing bootstrap target before managed writes."""

from __future__ import annotations

import os
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


def is_safe_target(target: Path) -> bool:
    if is_indirect_path(target) or (target.exists() and not target.is_dir()):
        return False
    if not target.exists():
        return True
    def fail_on_walk_error(error: OSError) -> None:
        raise error

    try:
        for current, directories, files in os.walk(target, followlinks=False, onerror=fail_on_walk_error):
            for name in directories + files:
                if is_indirect_path(Path(current) / name):
                    return False
    except OSError:
        return False
    return True


def main(arguments: list[str]) -> int:
    if len(arguments) != 1:
        print("Usage: check_bootstrap_target_symlinks.py TARGET", file=sys.stderr)
        return 2
    if not is_safe_target(Path(arguments[0])):
        print("Bootstrap target contains a symlink or is not a directory", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
