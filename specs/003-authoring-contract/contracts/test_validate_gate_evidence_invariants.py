#!/usr/bin/env python3
"""Tests for feature-local autonomous Gate Evidence invariants."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

CONTRACT_DIR = Path(__file__).resolve().parent
FIXTURES = CONTRACT_DIR / "fixtures/gate-evidence"
sys.path.insert(0, str(CONTRACT_DIR))

from validate_gate_evidence_invariants import (  # noqa: E402
    EvidenceViolation,
    validate_premerge_binding,
    validate_supplemental_references,
)


def fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class GateEvidenceInvariantTests(unittest.TestCase):
    def test_valid_supplemental_primary_reference(self) -> None:
        validate_supplemental_references(
            fixture("valid-supplemental-primary-reference.json")
        )

    def test_missing_primary_reference_is_rejected(self) -> None:
        with self.assertRaises(EvidenceViolation):
            validate_supplemental_references(
                fixture("missing-primary-reference.json")
            )

    def test_wrong_primary_reference_is_rejected(self) -> None:
        with self.assertRaises(EvidenceViolation):
            validate_supplemental_references(fixture("wrong-primary-reference.json"))

    def test_valid_postmerge_premerge_binding(self) -> None:
        validate_premerge_binding(
            fixture("valid-postmerge-premerge-binding.json"),
            "runner/premerge.json",
            "a" * 64,
        )

    def test_wrong_premerge_path_is_rejected(self) -> None:
        with self.assertRaises(EvidenceViolation):
            validate_premerge_binding(
                fixture("wrong-premerge-path.json"),
                "runner/premerge.json",
                "a" * 64,
            )

    def test_wrong_premerge_hash_is_rejected(self) -> None:
        with self.assertRaises(EvidenceViolation):
            validate_premerge_binding(
                fixture("wrong-premerge-hash.json"),
                "runner/premerge.json",
                "a" * 64,
            )


if __name__ == "__main__":
    unittest.main()
