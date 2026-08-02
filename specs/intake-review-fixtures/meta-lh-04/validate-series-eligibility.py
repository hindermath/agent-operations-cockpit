#!/usr/bin/env python3
"""Validate one META-LH-04 eligibility fixture against the bound contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: root must be an object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    args = parser.parse_args()

    contract = load_json(args.contract)
    fixture = load_json(args.fixture)
    criteria = contract.get("criteria")
    values = fixture.get("criteria")
    if not isinstance(criteria, list) or len(criteria) != 9 or len(set(criteria)) != 9:
        raise ValueError("contract must declare exactly nine unique criteria")
    if not isinstance(values, dict) or set(values) != set(criteria):
        raise ValueError("fixture must provide exactly the nine contract criteria")
    if fixture.get("mode") not in contract.get("modes", []):
        raise ValueError("fixture mode is not declared by the contract")

    outcome = "Eligible"
    if not fixture.get("currentAuthority", False) or fixture.get("mode") == "blocked":
        outcome = "Blocked"
    if fixture.get("mode") == "parallel-autonomous" and not all(
        (
            fixture.get("disjointWrites", False),
            not fixture.get("sharedOpenDecisions", True),
            fixture.get("consolidationReview", False),
            fixture.get("abortRule", False),
            fixture.get("recoveryRule", False),
        )
    ):
        outcome = "Blocked"

    expected = fixture.get("expectedOutcome")
    if outcome != expected:
        raise ValueError(f"expected {expected!r}, calculated {outcome!r}")
    print(f"{fixture.get('fixtureId')}: {outcome}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
