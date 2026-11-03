#!/usr/bin/env python3
"""Extract a learning ZIP within fixed entry and byte budgets."""

from __future__ import annotations

import codecs
from pathlib import Path, PurePosixPath
import re
import stat
import struct
import sys
import zipfile


MAX_ENTRIES = 20_000
MAX_CENTRAL_DIRECTORY_BYTES = 32 << 20
MAX_ARCHIVE_BYTES = 2 << 30
MAX_CHECKSUM_BYTES = 4096
MAX_UNCOMPRESSED_BYTES = 1 << 30
COPY_CHUNK = 1 << 20
END_RECORD = struct.Struct("<4s4H2IH")
CENTRAL_HEADER_BYTES = 46


class UnsafePackage(ValueError):
    """The ZIP exceeds the package boundary."""


def has_control_character(name: str) -> bool:
    return any(ord(character) < 32 or ord(character) == 127 for character in name)


def invalid_windows_component(part: str) -> bool:
    device_name = part.split(".", 1)[0].upper()
    return (":" in part or part.endswith((" ", "."))
            or device_name in {"CON", "PRN", "AUX", "NUL"}
            or re.fullmatch(r"(?:COM|LPT)[1-9¹²³]", device_name) is not None)


def read_checksum_bounded(sidecar: Path) -> str:
    with sidecar.open("rb") as source:
        contents = source.read(MAX_CHECKSUM_BYTES + 1)
    if len(contents) > MAX_CHECKSUM_BYTES:
        raise UnsafePackage("SHA-256 sidecar exceeds byte limit")
    for marker, encoding in (
        (codecs.BOM_UTF32_LE, "utf-32"),
        (codecs.BOM_UTF32_BE, "utf-32"),
        (codecs.BOM_UTF16_LE, "utf-16"),
        (codecs.BOM_UTF16_BE, "utf-16"),
    ):
        if contents.startswith(marker):
            try:
                lines = contents.decode(encoding).splitlines()
            except UnicodeDecodeError as exc:
                raise UnsafePackage("SHA-256 sidecar encoding is invalid") from exc
            fields = lines[0].split() if lines else []
            digest = fields[0] if fields else ""
            if re.fullmatch(r"[0-9a-fA-F]{64}", digest) is None:
                raise UnsafePackage("SHA-256 sidecar has no valid digest on its first line")
            return digest.lower()
    first_line = contents.removeprefix(codecs.BOM_UTF8).split(b"\n", 1)[0]
    fields = first_line.split()
    if not fields or re.fullmatch(rb"[0-9a-fA-F]{64}", fields[0]) is None:
        raise UnsafePackage("SHA-256 sidecar has no valid digest on its first line")
    return fields[0].decode("ascii").lower()


def check_archive_size(source) -> int:
    source.seek(0, 2)
    size = source.tell()
    if size > MAX_ARCHIVE_BYTES:
        raise UnsafePackage("ZIP archive exceeds byte limit")
    return size


def check_metadata_budget(source) -> None:
    """Count central-directory records before ZipFile builds its object list."""
    size = check_archive_size(source)
    tail_size = min(size, END_RECORD.size + 65_535)
    source.seek(size - tail_size)
    tail = source.read(tail_size)
    marker = tail.rfind(b"PK\x05\x06")
    if marker < 0 or len(tail) - marker < END_RECORD.size:
        raise UnsafePackage("ZIP end record is missing")
    (signature, disk, directory_disk, disk_entries, total_entries,
     directory_size, directory_offset, comment_size) = END_RECORD.unpack_from(tail, marker)
    if signature != b"PK\x05\x06" or marker + END_RECORD.size + comment_size != len(tail):
        raise UnsafePackage("ZIP end record is inconsistent")
    if disk or directory_disk or disk_entries != total_entries:
        raise UnsafePackage("multi-disk ZIP is not supported")
    if total_entries == 0xFFFF or directory_size == 0xFFFFFFFF or directory_offset == 0xFFFFFFFF:
        raise UnsafePackage("ZIP64 metadata exceeds the package contract")
    if total_entries > MAX_ENTRIES:
        raise UnsafePackage("ZIP has too many entries")
    if directory_size > MAX_CENTRAL_DIRECTORY_BYTES:
        raise UnsafePackage("ZIP central directory exceeds byte limit")

    end_offset = size - tail_size + marker
    if end_offset >= 20:
        source.seek(end_offset - 20)
        if source.read(4) == b"PK\x06\x07":
            raise UnsafePackage("ZIP64 metadata exceeds the package contract")
    start_offset = end_offset - directory_size
    if start_offset < 0 or directory_offset > start_offset:
        raise UnsafePackage("ZIP central directory offset is invalid")
    source.seek(start_offset)
    counted = 0
    while source.tell() < end_offset:
        header = source.read(CENTRAL_HEADER_BYTES)
        if len(header) != CENTRAL_HEADER_BYTES or header[:4] != b"PK\x01\x02":
            raise UnsafePackage("ZIP central directory is malformed")
        name_size, extra_size, entry_comment_size = struct.unpack_from("<HHH", header, 28)
        next_offset = source.tell() + name_size + extra_size + entry_comment_size
        if next_offset > end_offset:
            raise UnsafePackage("ZIP central directory is malformed")
        source.seek(next_offset)
        counted += 1
        if counted > MAX_ENTRIES:
            raise UnsafePackage("ZIP has too many entries")
    if counted != total_entries:
        raise UnsafePackage("ZIP entry count is inconsistent")


def list_bounded(package: Path) -> None:
    with package.open("rb") as source:
        check_metadata_budget(source)
        source.seek(0)
        with zipfile.ZipFile(source) as archive:
            for entry in archive.infolist():
                if has_control_character(entry.filename):
                    raise UnsafePackage("ZIP entry has a control character")
                print(entry.filename)


def extract_bounded(package: Path, destination: Path) -> None:
    destination = destination.resolve(strict=True)
    with package.open("rb") as source:
        check_metadata_budget(source)
        source.seek(0)
        with zipfile.ZipFile(source) as archive:
            _extract_checked_archive(archive, destination)


def _extract_checked_archive(archive: zipfile.ZipFile, destination: Path) -> None:
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
            not name or name.startswith("/") or has_control_character(name)
            or any(invalid_windows_component(part) for part in name.split("/") if part)
            or any(part.casefold() == ".git" for part in name.split("/"))
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
        if not target.resolve(strict=False).is_relative_to(destination):
            raise UnsafePackage(f"unsafe ZIP entry: {entry.filename!r}")
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
        print("Usage: check_learning_package_archive.py ZIP DESTINATION | --list ZIP | --size ZIP | --checksum SIDECAR", file=sys.stderr)
        return 2
    try:
        if arguments[0] == "--checksum":
            print(read_checksum_bounded(Path(arguments[1])))
        elif arguments[0] == "--size":
            with Path(arguments[1]).open("rb") as source:
                check_archive_size(source)
        elif arguments[0] == "--list":
            list_bounded(Path(arguments[1]))
        else:
            extract_bounded(Path(arguments[0]), Path(arguments[1]))
    except (OSError, UnsafePackage, zipfile.BadZipFile, RuntimeError) as exc:
        subject = "invalid SHA-256 sidecar" if arguments[0] == "--checksum" else "unsafe learning ZIP"
        print(f"ERROR: {subject}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
