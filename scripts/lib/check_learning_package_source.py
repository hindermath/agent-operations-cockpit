#!/usr/bin/env python3
"""Reject indirect files before a learning tree becomes a distributable ZIP."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import stat
import sys


EXCLUDED_DIRS = {".git", "bin", "obj", "build", "node_modules", ".vs", ".idea", "__MACOSX"}
EXCLUDED_FILES = {".DS_Store", "settings.local.json", "intake-review-result.json", "intake-review-report.md"}
EXCLUDED_PATHS = {".vscode/settings.json", ".vscode/c_cpp_properties.json"}


def indirect(path: Path) -> bool:
    info = path.lstat()
    return (stat.S_ISLNK(info.st_mode) or
            bool(getattr(info, "st_file_attributes", 0) & 0x400) or
            (stat.S_ISREG(info.st_mode) and info.st_nlink > 1))


def excluded(relative: Path) -> bool:
    parts = relative.parts
    return (any(part in EXCLUDED_DIRS for part in parts) or
            relative.as_posix() == "docs/learning-units/dist" or
            relative.as_posix().startswith("docs/learning-units/dist/") or
            relative.as_posix() in EXCLUDED_PATHS or
            relative.name in EXCLUDED_FILES)


def check_tree(root: Path, *, skip_excluded: bool) -> None:
    if not root.is_dir() or indirect(root):
        raise ValueError(f"unsafe package root: {root}")
    def fail_on_walk_error(error: OSError) -> None:
        raise error

    for current, directories, files in os.walk(root, followlinks=False,
                                               onerror=fail_on_walk_error):
        parent = Path(current)
        for name in list(directories) + files:
            path = parent / name
            relative = path.relative_to(root)
            if indirect(path):
                raise ValueError(f"package source contains a link or hardlink: {relative}")
            if skip_excluded and excluded(relative):
                if name in directories:
                    directories.remove(name)
                continue
            if not skip_excluded and excluded(relative):
                raise ValueError(f"package staging contains an excluded path: {relative}")
            if not path.is_file() and not path.is_dir():
                raise ValueError(f"package source contains a special file: {relative}")


def check_guide(path: Path) -> None:
    if not path.is_file() or indirect(path):
        raise ValueError(f"package guide is not a regular file: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--staging", type=Path)
    parser.add_argument("--guide", type=Path, action="append", default=[])
    args = parser.parse_args()
    if (args.source is None) == (args.staging is None):
        parser.error("pass exactly one of --source or --staging")
    try:
        if args.source is not None:
            check_tree(args.source, skip_excluded=True)
            for guide in args.guide:
                check_guide(guide)
        else:
            check_tree(args.staging, skip_excluded=False)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
