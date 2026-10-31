#!/usr/bin/env python3
"""Extract a learning ZIP within fixed entry and byte budgets."""

from __future__ import annotations

from pathlib import Path, PurePosixPath
import re
import stat
import sys
import zipfile


MAX_ENTRIES = 20_000
MAX_UNCOMPRESSED_BYTES = 1 << 30
COPY_CHUNK = 1 << 20


class UnsafePackage(ValueError):
    """The ZIP exceeds the package boundary."""


def extract_bounded(package: Path, destination: Path) -> None:
    destination = destination.resolve(strict=True)
    with zipfile.ZipFile(package) as archive:
        entries = archive.infolist()
        if len(entries) > MAX_ENTRIES:
            raise UnsafePackage("ZIP has too many entries")
        planned_bytes = 0
        seen: set[str] = set()
        for entry in entries:
            name = entry.filename.replace("\\", "/")
            path = PurePosixPath(name)
            mode = (entry.external_attr >> 16) & 0o170000
            if (
                not name or name.startswith("/") or "\x00" in name
                or re.match(r"^[A-Za-z]:", name) is not None
                or path.is_absolute() or any(part in {".", ".."} for part in name.split("/"))
                or mode not in {0, stat.S_IFREG, stat.S_IFDIR}
                or (mode == stat.S_IFDIR and not entry.is_dir())
                or name in seen
            ):
                raise UnsafePackage(f"unsafe ZIP entry: {name!r}")
            seen.add(name)
            if not entry.is_dir():
                planned_bytes += entry.file_size
                if planned_bytes > MAX_UNCOMPRESSED_BYTES:
                    raise UnsafePackage("ZIP exceeds uncompressed byte limit")

        written_bytes = 0
        for entry in entries:
            target = destination.joinpath(*PurePosixPath(entry.filename.replace("\\", "/")).parts)
            if entry.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(entry) as source, target.open("xb") as output:
                while chunk := source.read(COPY_CHUNK):
                    written_bytes += len(chunk)
                    if written_bytes > MAX_UNCOMPRESSED_BYTES:
                        raise UnsafePackage("ZIP exceeds extracted byte limit")
                    output.write(chunk)


def main(arguments: list[str]) -> int:
    if len(arguments) != 2:
        print("Usage: check_learning_package_archive.py ZIP DESTINATION", file=sys.stderr)
        return 2
    try:
        extract_bounded(Path(arguments[0]), Path(arguments[1]))
    except (OSError, UnsafePackage, zipfile.BadZipFile, RuntimeError) as exc:
        print(f"ERROR: unsafe learning ZIP: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
