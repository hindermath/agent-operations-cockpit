#!/usr/bin/env python3
"""Zusätzliche unittest-Fälle / Additional established unittest cases."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parents[3]
CONTRACTS = "specs/004-series-eligibility/contracts"
FIXTURE = "specs/intake-review-fixtures/meta-lh-04/valid-parallel.json"
CONTRACT = "requirements/baseline/series-eligibility-contract.json"
SHELL = "bash"


def snapshot(repo: Path) -> dict:
    return {str(p.relative_to(repo)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in repo.rglob("*") if p.is_file()}


class EligibilityTests(unittest.TestCase):
    def run_fixture(self, fixture: dict) -> tuple[dict, int]:
        # Testaufbau ist getrennt von der lesenden Abfrage. / Separate setup from query.
        with tempfile.TemporaryDirectory(prefix="aoc eligibility ") as temporary:
            repo = Path(temporary)
            target = repo / CONTRACT
            target.parent.mkdir(parents=True)
            shutil.copyfile(REPO / CONTRACT, target)
            (repo / "fixture.json").write_text(json.dumps(fixture), encoding="utf-8")
            before = snapshot(repo)
            if SHELL == "bash":
                args = [os.environ.get("AOC_GIT_BASH_EXE", "bash"),
                        f"{CONTRACTS}/validate-series-eligibility.sh", "--repo", str(repo),
                        "--fixture", "fixture.json", "--json"]
            else:
                args = ["pwsh", "-NoProfile", "-File",
                        f"{CONTRACTS}/validate-series-eligibility.ps1", "-Repo", str(repo),
                        "-Fixture", "fixture.json", "-Json"]
            child = subprocess.run(args, cwd=REPO, capture_output=True, text=True)
            # Child-Exits bleiben sichtbar, auch wenn der Negativtest besteht.
            # Preserve actual child exits even when a negative test passes.
            print(json.dumps({"shell": SHELL, "test": self.id(),
                              "childExit": child.returncode, "stdout": child.stdout,
                              "stderr": child.stderr}, ensure_ascii=False), flush=True)
            self.assertEqual(before, snapshot(repo), "query wrote files")
            return json.loads(child.stdout), child.returncode

    def test_surface(self):
        result, code = self.run_fixture(json.loads((REPO / FIXTURE).read_text()))
        self.assertEqual(0, code)
        self.assertEqual("Eligible", result["outcome"])
        self.assertFalse(result["authorityGranted"])

    def test_empty_integration(self):
        fixture = json.loads((REPO / FIXTURE).read_text())
        fixture["criteria"]["integration"] = ""
        fixture["expectedOutcome"] = "Blocked"
        result, code = self.run_fixture(fixture)
        self.assertEqual("Blocked", result["outcome"])
        self.assertEqual("ProductFailure", result["failureClass"])
        self.assertEqual(0, code)
        self.assertTrue(any(r["criterion"] == "integration" for r in result["reasons"]))
        self.assertEqual({"de", "en"}, set(result["nextAction"]))
        self.assertFalse(result["authorityGranted"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=REPO)
    parser.add_argument("--shell", choices=["bash", "pwsh"], default="bash")
    parser.add_argument("--case", choices=["surface", "empty-integration", "all"], default="all")
    args = parser.parse_args()
    REPO, SHELL = args.repo.resolve(), args.shell
    names = ["surface", "empty_integration"] if args.case == "all" else [args.case.replace("-", "_")]
    suite = unittest.TestSuite(EligibilityTests("test_" + name) for name in names)
    raise SystemExit(0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1)
