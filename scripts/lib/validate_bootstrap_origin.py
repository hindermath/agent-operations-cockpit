#!/usr/bin/env python3
"""Bind an existing bootstrap origin to the authenticated destination."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit


def remote_parts(value: str) -> tuple[str, str] | None:
    if value.startswith("git@") and ":" in value:
        host, path = value[4:].split(":", 1)
        if not host or not path:
            return None
        return host.casefold(), path
    try:
        parsed = urlsplit(value)
    except ValueError:
        return None
    if parsed.scheme not in {"https", "ssh"} or parsed.query or parsed.fragment:
        return None
    if parsed.username not in {None, "git"} or parsed.password is not None:
        return None
    if parsed.scheme == "ssh" and parsed.username != "git":
        return None
    if not parsed.netloc or not parsed.path.startswith("/"):
        return None
    return parsed.netloc.rsplit("@", 1)[-1].casefold(), parsed.path.lstrip("/")


def matches_origin(origin: str, base_url: str, owner: str, repository: str) -> bool:
    try:
        base = urlsplit(base_url)
    except ValueError:
        return False
    parts = remote_parts(origin)
    if base.scheme != "https" or not base.netloc or parts is None:
        return False
    host, path = parts
    if host != base.netloc.casefold() or "%" in path or "\\" in path:
        return False
    if path.endswith(".git"):
        path = path[:-4]
    if path.endswith("/"):
        path = path[:-1]
    expected = "/".join(filter(None, [base.path.strip("/"), owner, repository]))
    if any(segment in {"", ".", ".."} for segment in path.split("/")):
        return False
    return path.casefold() == expected.casefold()


def matches_effective_push_urls(git_repository: Path, base_url: str, owner: str, repository: str) -> bool:
    try:
        result = subprocess.run(
            ["git", "-C", str(git_repository), "remote", "get-url", "--push", "--all", "origin"],
            capture_output=True, text=True, check=False, timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    urls = result.stdout.splitlines()
    return result.returncode == 0 and bool(urls) and all(
        matches_origin(url, base_url, owner, repository) for url in urls
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--origin", required=True)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--git-repository", type=Path, required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", args.owner) or not re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9._-]*", args.repository
    ):
        return 2
    if not matches_origin(args.origin, args.base_url, args.owner, args.repository) or not matches_effective_push_urls(
        args.git_repository, args.base_url, args.owner, args.repository
    ):
        print("Existing origin does not match the authenticated bootstrap destination", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
