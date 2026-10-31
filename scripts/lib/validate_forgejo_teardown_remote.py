#!/usr/bin/env python3
"""Bind a Forgejo teardown target to its exact Git origin and API base URL."""

from __future__ import annotations

import re
import sys
from urllib.parse import urlsplit


SEGMENT = re.compile(r"[A-Za-z0-9_.-]+\Z")
SCP_REMOTE = re.compile(r"git@([A-Za-z0-9.-]+):(.+)\Z")


def _segments(path: str) -> list[str] | None:
    parts = path.split("/")
    if not parts or not all(
        SEGMENT.fullmatch(part) and part not in {".", ".."} for part in parts
    ):
        return None
    return parts


def validate_remote(
    origin: str, base_url: str, platform: str, owner: str, repository: str
) -> str | None:
    if any(char in value for value in (origin, base_url, owner, repository)
           for char in "\r\n\t"):
        return None
    if platform not in {"forgejo", "codeberg"}:
        return None
    if not (SEGMENT.fullmatch(owner) and SEGMENT.fullmatch(repository)):
        return None
    if owner in {".", ".."} or repository in {".", ".."}:
        return None

    base = urlsplit(base_url)
    if (base.scheme != "https" or not base.hostname or base.username is not None
            or base.password is not None or base.query or base.fragment):
        return None
    try:
        base_port = base.port
    except ValueError:
        return None
    if platform == "codeberg" and (base.hostname.lower() != "codeberg.org"
                                   or base_port not in (None, 443)
                                   or base.path not in ("", "/")):
        return None
    prefix = base.path.strip("/")
    prefix_parts = _segments(prefix) if prefix else []
    if prefix_parts is None:
        return None

    scp = SCP_REMOTE.fullmatch(origin)
    if scp:
        if base_port not in (None, 443):
            return None
        remote_host, remote_path = scp.groups()
    else:
        remote = urlsplit(origin)
        if (remote.scheme not in {"https", "ssh"} or not remote.hostname
                or remote.query or remote.fragment or remote.password is not None
                or remote.username not in ((None,) if remote.scheme == "https" else ("git",))):
            return None
        try:
            remote_port = remote.port
        except ValueError:
            return None
        if remote.scheme == "https" and remote_port != base_port:
            if not (remote_port in (None, 443) and base_port in (None, 443)):
                return None
        if remote.scheme == "ssh" and base_port not in (None, 443):
            return None
        remote_host = remote.hostname
        remote_path = remote.path.lstrip("/")

    if remote_host.lower() != base.hostname.lower():
        return None
    if remote_path.endswith(".git"):
        remote_path = remote_path[:-4]
    if _segments(remote_path) != [*prefix_parts, owner, repository]:
        return None
    canonical_base = f"https://{base.netloc.lower()}"
    if prefix_parts:
        canonical_base += "/" + "/".join(prefix_parts)
    return f"{canonical_base}/{owner}/{repository}"


def main() -> int:
    if len(sys.argv) != 6:
        print("Usage: validate_forgejo_teardown_remote.py ORIGIN BASE_URL PLATFORM OWNER REPOSITORY", file=sys.stderr)
        return 2
    identity = validate_remote(*sys.argv[1:])
    if identity is None:
        print("Forgejo teardown target does not match exact origin", file=sys.stderr)
        return 2
    print(identity)
    return 0


if __name__ == "__main__":
    sys.exit(main())
