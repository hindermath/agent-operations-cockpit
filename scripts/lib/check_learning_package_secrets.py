#!/usr/bin/env python3
"""Require Gitleaks and accept only byte-identical, reviewed teaching examples."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


# These exact files contain reviewed instructional and fixture false positives.
# Any edit, different location, rule, or new finding must fail for review.
REVIEWED_EXAMPLES = {
    ("docs/secure-development/mitgeltende-dokumente/Leitlinie_Sichere-Programmierung.md", "generic-api-key", 38):
        "37d095a65fa498e170cf6a0e21e303a5ad1d5cdd09b3275b8c8e8fff3cb3d805",
    ("docs/secure-development/checklisten/CL_09_KI-Codeerzeugung.md", "private-key", 694):
        "071ed93b5c2bcdfa585f54e7c5386db8cc265d92c6b0bc018ed77d0adfabb766",
    ("docs/secure-development/Checklistensammelband_Sichere-Entwicklung.md", "private-key", 10081):
        "ac4ebb80a4954db060074762f99c211930a347bec965902dc08becf608aa0b69",
    ("specs/004-series-eligibility/phase-results/us1-tests.json", "generic-api-key", 185):
        "a65a9d4d3b6b820a4591e1801b05c50b7d0affe912c2ab899450b3a6539afa15",
    ("specs/004-series-eligibility/phase-results/us1-tests.json", "generic-api-key", 195):
        "a65a9d4d3b6b820a4591e1801b05c50b7d0affe912c2ab899450b3a6539afa15",
    ("specs/004-series-eligibility/phase-results/us2-tests.json", "generic-api-key", 684):
        "8931e2fd768e665e5642b210793cd9fc405a917a328a6ff26847507bf3a721a4",
}
MAX_REPORT_BYTES = 4 * 1024 * 1024
MAX_EXAMPLE_BYTES = 4 * 1024 * 1024


def check_package_secrets(root: Path) -> None:
    scanner = shutil.which("gitleaks")
    if not scanner:
        raise ValueError("gitleaks fuer den Secret-Scan erforderlich / gitleaks is required")
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Paket-Staging fehlt / package staging directory is missing")

    with tempfile.TemporaryDirectory(prefix="aoc-learning-secrets-") as temporary:
        report = Path(temporary) / "findings.json"
        config = Path(__file__).resolve().parents[1] / "templates/gitleaks-learning-package-default.toml"
        result = subprocess.run(
            [scanner, "dir", str(root), "--no-banner", "--redact", "--ignore-gitleaks-allow",
             "--report-format", "json",
             "--report-path", str(report), "--config", str(config)],
            capture_output=True, text=True, check=False, cwd=temporary,
        )
        if result.returncode == 0:
            return
        if result.returncode != 1 or not report.is_file():
            raise ValueError("gitleaks-Scan fehlgeschlagen / gitleaks scan failed")
        if report.stat().st_size > MAX_REPORT_BYTES:
            raise ValueError("gitleaks-Bericht zu gross / gitleaks report too large")
        try:
            findings = json.loads(report.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            raise ValueError("gitleaks-Bericht ungueltig / invalid gitleaks report") from error
        if not isinstance(findings, list) or not findings:
            raise ValueError("gitleaks-Bericht ungueltig / invalid gitleaks report")

        for finding in findings:
            if not isinstance(finding, dict):
                raise ValueError("gitleaks-Bericht ungueltig / invalid gitleaks report")
            reported_path = finding.get("File")
            if not isinstance(reported_path, str):
                raise ValueError("gitleaks-Bericht ungueltig / invalid gitleaks report")
            file_path = Path(reported_path)
            if not file_path.is_absolute():
                file_path = root / file_path
            try:
                file_path = file_path.resolve(strict=True)
                relative = file_path.relative_to(root).as_posix()
            except (OSError, ValueError) as error:
                raise ValueError("gitleaks-Fund ausserhalb des Pakets / finding outside package") from error
            key = (relative, finding.get("RuleID"), finding.get("StartLine"))
            expected_hash = REVIEWED_EXAMPLES.get(key)
            if not expected_hash or not file_path.is_file():
                raise ValueError("gitleaks hat einen Secret-Befund gemeldet / gitleaks reported a secret")
            if file_path.stat().st_size > MAX_EXAMPLE_BYTES:
                raise ValueError("gitleaks hat einen Secret-Befund gemeldet / gitleaks reported a secret")
            normalized = file_path.read_bytes().replace(b"\r\n", b"\n")
            if hashlib.sha256(normalized).hexdigest() != expected_hash:
                raise ValueError("gitleaks hat einen Secret-Befund gemeldet / gitleaks reported a secret")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_learning_package_secrets.py ROOT", file=sys.stderr)
        return 2
    try:
        check_package_secrets(Path(sys.argv[1]))
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
