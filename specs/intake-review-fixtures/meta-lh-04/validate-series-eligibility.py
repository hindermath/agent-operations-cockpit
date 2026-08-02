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


def lower_camel(value: str) -> str:
    if not value:
        raise ValueError("parallel eligibility rule must name a fixture field")
    return value[0].lower() + value[1:]


def meets_parallel_eligibility(contract: dict, fixture: dict) -> bool:
    rules = contract.get("parallelEligibility")
    if not isinstance(rules, dict) or not rules:
        raise ValueError("contract must declare parallelEligibility rules")

    for rule, enabled in rules.items():
        if not isinstance(enabled, bool):
            raise ValueError(f"parallel eligibility rule {rule!r} must be boolean")
        if rule.startswith("requires"):
            fixture_field = lower_camel(rule.removeprefix("requires"))
            if enabled and not fixture.get(fixture_field, False):
                return False
        elif rule.startswith("allows"):
            fixture_field = lower_camel(rule.removeprefix("allows"))
            if not enabled and fixture.get(fixture_field, False):
                return False
        else:
            raise ValueError(
                f"parallel eligibility rule {rule!r} must start with 'requires' or 'allows'"
            )
    return True


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

    mode = fixture.get("mode")
    outcome = "Eligible"
    if mode == "blocked":
        outcome = "Blocked"
    elif mode == "parallel-autonomous" and not meets_parallel_eligibility(
        contract, fixture
    ):
        outcome = "Blocked"
    elif mode != "parallel-autonomous" and not fixture.get("currentAuthority", False):
        outcome = "Blocked"

    expected = fixture.get("expectedOutcome")
    if outcome != expected:
        raise ValueError(f"expected {expected!r}, calculated {outcome!r}")
    print(f"{fixture.get('fixtureId')}: {outcome}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
