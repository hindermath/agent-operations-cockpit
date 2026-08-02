#!/usr/bin/env python3
"""Validate META-LH-05 re-entry fixtures and the current nine-target inventory."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: root must be an object")
    return value


def validate_contract(contract: dict) -> list[str]:
    required = [f"RAW-{number:02d}" for number in range(1, 10)]
    if contract.get("schemaVersion") != "1.0" or contract.get("documentType") != "FirstWaveAuthoringContract":
        raise ValueError("contract identity is invalid")
    if contract.get("requiredSeries") != required:
        raise ValueError("requiredSeries must be RAW-01 through RAW-09 in order")
    criteria = contract.get("eligibilityCriteria")
    if not isinstance(criteria, list) or len(criteria) != 9 or len(set(criteria)) != 9:
        raise ValueError("contract must bind exactly nine unique eligibility criteria")
    ownership = contract.get("concernOwnership", {})
    if ownership.get("requiredConcernOwnersPerConcern") != 1 or not ownership.get("forbidsDuplicateConcernOwners"):
        raise ValueError("contract must require exactly one concern owner")
    return criteria


def fixture_outcome(contract: dict, fixture: dict, criteria: list[str]) -> str:
    values = fixture.get("criteria")
    if not isinstance(values, dict) or set(values) != set(criteria):
        raise ValueError("fixture must provide exactly the nine contract criteria")
    state = fixture.get("presenceState")
    if state == "AllMatching":
        return "VerifyOnly"
    if state in {"Partial", "Collision"}:
        return "Blocked"
    if state == "AllAbsent":
        return "CreateAtomic" if fixture.get("currentAuthority") is True else "Blocked"
    raise ValueError(f"unknown presenceState: {state!r}")


def verify_current(repo: Path, contract: dict) -> None:
    active = repo / "requirements/intakes/active"
    receipts = repo / contract["evidence"]["receiptDirectory"]
    for series_id in contract["requiredSeries"]:
        if len(list(active.glob(f"Lastenheft_{series_id}-*.md"))) != 1:
            raise ValueError(f"{series_id}: expected exactly one active target")
        if len(list(receipts.glob(f"{series_id}-*.json"))) != 1:
            raise ValueError(f"{series_id}: expected exactly one active receipt")
    for key in ("ownershipContract", "ownershipView", "coverageMatrix", "seriesManifest"):
        if not (repo / contract["evidence"][key]).is_file():
            raise ValueError(f"missing evidence path: {contract['evidence'][key]}")
    print("META05-CURRENT-WAVE: VerifyOnly (9 targets, 9 receipts)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--fixture", type=Path)
    parser.add_argument("--repo", type=Path)
    args = parser.parse_args()
    contract = load(args.contract)
    criteria = validate_contract(contract)
    if bool(args.fixture) == bool(args.repo):
        parser.error("use exactly one of --fixture or --repo")
    if args.repo:
        verify_current(args.repo.resolve(), contract)
        return 0
    fixture = load(args.fixture)
    outcome = fixture_outcome(contract, fixture, criteria)
    expected = fixture.get("expectedOutcome")
    if outcome != expected:
        raise ValueError(f"expected {expected!r}, calculated {outcome!r}")
    print(f"{fixture.get('fixtureId')}: {outcome}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
