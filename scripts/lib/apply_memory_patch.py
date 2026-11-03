#!/usr/bin/env python3
"""Apply reviewed memory-patch entries only to tracked Markdown within a target tree."""

from __future__ import annotations

import argparse
from collections import defaultdict
import os
from pathlib import Path
import stat
import subprocess
import sys


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", "-C", str(root), "--literal-pathspecs", *args], text=True,
                          capture_output=True, check=check)


def checked_target(root: Path, raw: str) -> tuple[Path, str, tuple[int, int]]:
    if not raw or any(char in raw for char in "\r\n\t\0"):
        raise ValueError("empty or malformed patch target")
    source = Path(raw).expanduser()
    if any(part in {".", ".."} for part in source.parts):
        raise ValueError(f"patch target has a traversal component: {raw}")
    target = source if source.is_absolute() else root / source
    target = Path(os.path.abspath(target))
    try:
        relative = target.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"patch target leaves selected root: {raw}") from exc
    if not relative.parts or ".git" in relative.parts or target.suffix.lower() != ".md":
        raise ValueError(f"patch target is not an allowed Markdown file: {raw}")
    current = root
    target_info: os.stat_result | None = None
    for part in relative.parts:
        current = current / part
        info = current.lstat()
        if (stat.S_ISLNK(info.st_mode) or
                bool(getattr(info, "st_file_attributes", 0) & 0x400)):
            raise ValueError(f"patch target contains an indirect path: {raw}")
        if current != target and not stat.S_ISDIR(info.st_mode):
            raise ValueError(f"patch target parent is not a directory: {raw}")
        if current == target and (not stat.S_ISREG(info.st_mode) or info.st_nlink > 1):
            raise ValueError(f"patch target is not a single regular file: {raw}")
        if current == target:
            target_info = info
    relative_text = relative.as_posix()
    if git(root, "ls-files", "--error-unmatch", "--", relative_text, check=False).returncode != 0:
        raise ValueError(f"patch target is not Git-tracked: {raw}")
    if git(root, "diff", "--quiet", "--", relative_text, check=False).returncode != 0:
        raise ValueError(f"patch target has uncommitted changes: {raw}")
    if git(root, "diff", "--cached", "--quiet", "--", relative_text, check=False).returncode != 0:
        raise ValueError(f"patch target has staged changes: {raw}")
    if target_info is None:
        raise ValueError(f"patch target has no file identity: {raw}")
    if os.name == "nt" and target_info.st_ino == 0:
        raise ValueError(f"patch target has no verifiable file identity: {raw}")
    return target, relative_text, (target_info.st_dev, target_info.st_ino)


def parse_patch(root: Path, patch: Path) -> tuple[dict[Path, list[str]], dict[Path, str],
                                                    dict[Path, tuple[int, int]]]:
    entries: dict[Path, list[str]] = defaultdict(list)
    relative_paths: dict[Path, str] = {}
    identities: dict[Path, tuple[int, int]] = {}
    selected: Path | None = None
    raw = patch.read_bytes()
    if len(raw) > 1_000_000:
        raise ValueError("patch exceeds the preview size limit")
    for line in raw.decode("utf-8").splitlines():
        if line.startswith("### Target: "):
            selected, relative, identity = checked_target(root, line[len("### Target: "):])
            relative_paths[selected] = relative
            identities[selected] = identity
        elif line.startswith("+++ "):
            if selected is None:
                raise ValueError("patch content appears before a target")
            payload = line[len("+++ "):]
            if payload.startswith("[Review needed:") or any(ord(char) < 32 for char in payload):
                raise ValueError("patch contains unresolved or control-character content")
            entries[selected].append(payload)
    if not entries:
        raise ValueError("patch contains no applicable entries")
    return entries, relative_paths, identities


def open_target(root: Path, relative: str, identity: tuple[int, int]) -> int:
    """Open one verified file without following a switched parent outside root."""
    parts = Path(relative).parts
    if os.name != "nt":
        directory_flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
        parent = os.open(root, directory_flags)
        try:
            for part in parts[:-1]:
                child = os.open(part, directory_flags, dir_fd=parent)
                os.close(parent)
                parent = child
            descriptor = os.open(parts[-1], os.O_WRONLY | os.O_APPEND | os.O_NOFOLLOW,
                                 dir_fd=parent)
        finally:
            os.close(parent)
    else:
        import ctypes
        import msvcrt

        descriptor = os.open(root / relative, os.O_WRONLY | os.O_APPEND | os.O_BINARY)
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        get_final_path = kernel32.GetFinalPathNameByHandleW
        get_final_path.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_uint32, ctypes.c_uint32]
        get_final_path.restype = ctypes.c_uint32
        buffer = ctypes.create_unicode_buffer(32768)
        length = get_final_path(msvcrt.get_osfhandle(descriptor), buffer, len(buffer), 0)
        if length == 0 or length >= len(buffer):
            os.close(descriptor)
            raise ValueError("cannot verify opened patch target path")
        final_path = buffer.value
        if final_path.startswith("\\\\?\\UNC\\"):
            final_path = "\\\\" + final_path[8:]
        elif final_path.startswith("\\\\?\\"):
            final_path = final_path[4:]
        expected_text = os.path.normcase(os.path.normpath(str(root / relative)))
        final_text = os.path.normcase(os.path.normpath(final_path))
        if final_text != expected_text:
            os.close(descriptor)
            raise ValueError("opened patch target differs from validated path")
    info = os.fstat(descriptor)
    if (not stat.S_ISREG(info.st_mode) or info.st_nlink > 1 or
            (info.st_dev, info.st_ino) != identity):
        os.close(descriptor)
        raise ValueError("opened patch target differs from validated file")
    return descriptor


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-dir", required=True, type=Path)
    parser.add_argument("--patch", required=True, type=Path)
    parser.add_argument("--yes", action="store_true")
    args = parser.parse_args()
    applied: list[str] = []
    try:
        root = args.target_dir.expanduser().resolve(strict=True)
        if not root.is_dir():
            raise ValueError("selected root is not a directory")
        patch = args.patch.expanduser().resolve(strict=True)
        entries, relative_paths, identities = parse_patch(root, patch)
        print(f"Patch-Datei / Patch file: {patch}")
        print("Gepruefte Aenderungen / Validated changes:")
        for path, lines in entries.items():
            print(f"### Target: {relative_paths[path]}")
            for line in lines:
                print(f"+++ {line}")
        if not args.yes and input("Patch anwenden / Apply patch? [j/N] ").strip().lower() not in {"j", "y"}:
            print("Patch abgebrochen / Patch canceled.")
            return 0
        # Recheck after confirmation before any write, including symlink parents.
        for path, relative in relative_paths.items():
            _, fresh_relative, fresh_identity = checked_target(root, str(path))
            if fresh_relative != relative or fresh_identity != identities[path]:
                raise ValueError(f"patch target changed: {relative}")
        for path, lines in entries.items():
            descriptor = open_target(root, relative_paths[path], identities[path])
            applied.append(relative_paths[path])
            with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
                for line in lines:
                    stream.write(line + "\n")
        git(root, "commit", "--only", "-m",
            f"chore: apply memory-patch -- {sum(map(len, entries.values()))} entries updated",
            "--", *relative_paths.values())
        print(f"Patch angewendet / Applied: {sum(map(len, entries.values()))} Eintraege / entries.")
        return 0
    except (EOFError, OSError, ValueError, UnicodeError, subprocess.CalledProcessError) as exc:
        if applied:
            print("WARNING: Teilweise angewendet / Partially applied: " + ", ".join(applied),
                  file=sys.stderr)
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
