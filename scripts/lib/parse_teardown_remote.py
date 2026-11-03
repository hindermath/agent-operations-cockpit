#!/usr/bin/env python3
"""Parse an exact GitHub or GitLab clone remote for destructive teardown."""

from __future__ import annotations

import re
import sys
from urllib.parse import urlsplit


SEGMENT = re.compile(r"[A-Za-z0-9_.-]+\Z")


def parse_remote(raw: str) -> tuple[str, str] | None:
    if any(char in raw for char in "\r\n\t"):
        return None
    scp = re.fullmatch(r"git@([A-Za-z0-9.-]+):(.+)", raw)
    if scp:
        host, path = scp.groups()
    else:
        parsed = urlsplit(raw)
        if parsed.scheme not in {"https", "ssh"} or parsed.query or parsed.fragment:
            return None
        if parsed.username not in (None, "git") or parsed.password is not None:
            return None
        try:
            port = parsed.port
        except ValueError:
            return None
        if port not in (None, 443 if parsed.scheme == "https" else 22):
            return None
        host = parsed.hostname or ""
        path = parsed.path.lstrip("/")
    host = host.lower()
    if host not in {"github.com", "gitlab.com"}:
        return None
    if path.endswith(".git"):
        path = path[:-4]
    parts = path.split("/")
    if len(parts) < 2 or (host == "github.com" and len(parts) != 2):
        return None
    if not all(SEGMENT.fullmatch(part) and part not in {".", ".."} for part in parts):
        return None
    return ("github" if host == "github.com" else "gitlab"), "/".join(parts)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: parse_teardown_remote.py URL", file=sys.stderr)
        return 2
    parsed = parse_remote(sys.argv[1])
    if parsed is None:
        print("Remote is not an exact supported GitHub/GitLab URL", file=sys.stderr)
        return 2
    print("\t".join(parsed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
