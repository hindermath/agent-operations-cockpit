#!/usr/bin/env python3
"""Validate META-LH-02 ownership, handoffs, order, and negative fixtures."""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path


class ContractError(Exception):
    """A stable validation code plus a learner-readable explanation."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


def fail(code: str, message: str) -> None:
    raise ContractError(code, message)


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail("PO001", f"cannot read JSON {path}: {exc}")
    if not isinstance(value, dict):
        fail("PO001", f"JSON root must be an object: {path}")
    return value


def required_text(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail("PO003", f"{label} must be non-empty text")
    return value.strip()


def required_text_list(value: object, label: str, *, allow_empty: bool = False) -> list[str]:
    if not isinstance(value, list) or (not value and not allow_empty):
        fail("PO003", f"{label} must be a {'possibly empty ' if allow_empty else ''}text array")
    result: list[str] = []
    for index, item in enumerate(value):
        result.append(required_text(item, f"{label}[{index}]"))
    return result


def validate_markdown_parity(path: Path, concern_owners: dict[str, str]) -> None:
    """Compare stable IDs and owners without treating prose formatting as data."""

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        fail("PO009", f"cannot read Markdown {path}: {exc}")
    markdown_owners: dict[str, str] = {}
    for line in lines:
        match = re.match(r"^\|\s*(C-\d{2})\s*\|.*?\|\s*(RAW-\d{2})\b", line)
        if match:
            concern_id, owner = match.groups()
            if concern_id in markdown_owners:
                fail("PO009", f"duplicate Markdown concern row: {concern_id}")
            markdown_owners[concern_id] = owner
    if markdown_owners != concern_owners:
        fail("PO009", "Markdown concern/owner rows do not match the JSON contract")


def validate_contract(data: dict, markdown: Path | None = None) -> dict[str, int]:
    if data.get("schemaVersion") != "1.0" or data.get("documentType") != "AocPortfolioOwnershipContract":
        fail("PO001", "schemaVersion or documentType is invalid")

    required_series = required_text_list(data.get("requiredSeries"), "requiredSeries")
    if required_series != [f"RAW-{number:02d}" for number in range(1, 10)]:
        fail("PO003", "requiredSeries must be RAW-01 through RAW-09 in order")
    required_set = set(required_series)

    series_rows = data.get("series")
    if not isinstance(series_rows, list) or len(series_rows) != 9:
        fail("PO003", "series must contain exactly nine rows")
    series_by_id: dict[str, dict] = {}
    list_fields = (
        "expectedChildIntakes",
        "decisionIntakes",
        "inputs",
        "outputs",
        "dependencies",
        "reviewEvidenceGates",
        "modes",
        "nonOwnership",
    )
    for index, row in enumerate(series_rows):
        if not isinstance(row, dict):
            fail("PO003", f"series[{index}] must be an object")
        series_id = required_text(row.get("id"), f"series[{index}].id")
        if series_id not in required_set or series_id in series_by_id:
            fail("PO003", f"unknown or duplicate series id: {series_id}")
        series_by_id[series_id] = row
        required_text(row.get("purpose"), f"series[{index}].purpose")
        required_text(row.get("systemBoundary"), f"series[{index}].systemBoundary")
        for field in list_fields:
            required_text_list(
                row.get(field),
                f"series[{index}].{field}",
                allow_empty=field in {"decisionIntakes", "dependencies"},
            )
    if set(series_by_id) != required_set:
        fail("PO003", "series rows do not cover RAW-01 through RAW-09 exactly")

    concerns = data.get("concerns")
    if not isinstance(concerns, list) or len(concerns) != 9:
        fail("PO002", "concerns must contain exactly nine owner assignments")
    concern_owners: dict[str, str] = {}
    for index, concern in enumerate(concerns):
        if not isinstance(concern, dict):
            fail("PO002", f"concerns[{index}] must be an object")
        concern_id = required_text(concern.get("id"), f"concerns[{index}].id")
        owner = required_text(concern.get("owner"), f"concerns[{index}].owner")
        required_text(concern.get("name"), f"concerns[{index}].name")
        if concern_id in concern_owners:
            fail("PO002", f"concern {concern_id} has more than one owner")
        if owner not in required_set:
            fail("PO002", f"concern {concern_id} has unknown owner {owner}")
        concern_owners[concern_id] = owner
    if set(concern_owners.values()) != required_set:
        fail("PO002", "each RAW series must own exactly one declared concern")

    handoffs = data.get("handoffs")
    if not isinstance(handoffs, list) or not handoffs:
        fail("PO004", "handoffs must be a non-empty array")
    handoff_ids: set[str] = set()
    pairs: set[tuple[str, str]] = set()
    adjacency = {series_id: [] for series_id in required_series}
    indegree = {series_id: 0 for series_id in required_series}
    for index, handoff in enumerate(handoffs):
        if not isinstance(handoff, dict):
            fail("PO004", f"handoffs[{index}] must be an object")
        handoff_id = required_text(handoff.get("id"), f"handoffs[{index}].id")
        producer = required_text(handoff.get("producer"), f"handoffs[{index}].producer")
        consumer = required_text(handoff.get("consumer"), f"handoffs[{index}].consumer")
        kind = required_text(handoff.get("kind"), f"handoffs[{index}].kind")
        required_text(handoff.get("contract"), f"handoffs[{index}].contract")
        required_text(handoff.get("version"), f"handoffs[{index}].version")
        required_text(handoff.get("failureBehavior"), f"handoffs[{index}].failureBehavior")
        binding = handoff.get("binding")
        if handoff_id in handoff_ids or (producer, consumer) in pairs:
            fail("PO004", f"duplicate handoff id or pair: {handoff_id}")
        if producer not in required_set or consumer not in required_set or producer == consumer:
            fail("PO004", f"handoff {handoff_id} has invalid endpoints")
        if kind not in {"BindingContract", "PreferredSerialOrder"} or not isinstance(binding, bool):
            fail("PO005", f"handoff {handoff_id} has invalid type or binding state")
        if binding != (kind == "BindingContract"):
            fail("PO005", f"handoff {handoff_id} type and binding state disagree")
        handoff_ids.add(handoff_id)
        pairs.add((producer, consumer))
        adjacency[producer].append(consumer)
        indegree[consumer] += 1

    # Kahn's algorithm removes every node only when no directed cycle exists.
    queue = [node for node in required_series if indegree[node] == 0]
    visited: list[str] = []
    while queue:
        node = queue.pop(0)
        visited.append(node)
        for successor in adjacency[node]:
            indegree[successor] -= 1
            if indegree[successor] == 0:
                queue.append(successor)
    if len(visited) != len(required_series):
        fail("PO007", "handoff graph contains a directed cycle")

    order = required_text_list(data.get("topologicalOrder"), "topologicalOrder")
    if len(order) != len(required_series) or set(order) != required_set:
        fail("PO008", "topologicalOrder must contain every series exactly once")
    position = {series_id: index for index, series_id in enumerate(order)}
    for producer, consumer in pairs:
        if position[producer] >= position[consumer]:
            fail("PO008", f"topologicalOrder violates {producer} -> {consumer}")

    decision_map = Path(required_text(data.get("decisionMapPath"), "decisionMapPath"))
    if not decision_map.is_file():
        fail("PO006", f"decision map is missing: {decision_map}")
    if markdown is not None:
        validate_markdown_parity(markdown, concern_owners)
    return {"series": len(series_by_id), "concerns": len(concern_owners), "handoffs": len(handoffs)}


def apply_fixture(fixture: dict) -> tuple[dict, str]:
    if fixture.get("schemaVersion") != "1.0" or fixture.get("documentType") != "PortfolioOwnershipNegativeFixture":
        fail("PO001", "negative fixture schema is invalid")
    base = load_json(Path(required_text(fixture.get("base"), "fixture.base")))
    candidate = copy.deepcopy(base)
    mutation = fixture.get("mutation")
    if not isinstance(mutation, dict):
        fail("PO001", "fixture.mutation must be an object")
    mutation_type = required_text(mutation.get("type"), "fixture.mutation.type")
    if mutation_type == "DuplicateConcernOwner":
        concern_id = required_text(mutation.get("concernId"), "fixture.mutation.concernId")
        second_owner = required_text(mutation.get("secondOwner"), "fixture.mutation.secondOwner")
        source = next((item for item in candidate["concerns"] if item.get("id") == concern_id), None)
        if source is None:
            fail("PO001", f"fixture concern not found: {concern_id}")
        duplicate = copy.deepcopy(source)
        duplicate["owner"] = second_owner
        candidate["concerns"].append(duplicate)
    elif mutation_type == "AddHandoff":
        handoff = mutation.get("handoff")
        if not isinstance(handoff, dict):
            fail("PO001", "fixture handoff must be an object")
        candidate["handoffs"].append(copy.deepcopy(handoff))
    else:
        fail("PO001", f"unknown fixture mutation: {mutation_type}")
    return candidate, required_text(fixture.get("expectedError"), "fixture.expectedError")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", type=Path)
    parser.add_argument("--markdown", type=Path)
    parser.add_argument("--fixture", type=Path)
    args = parser.parse_args()
    if bool(args.fixture) == bool(args.contract):
        parser.error("use exactly one of --contract or --fixture")
    if args.fixture:
        fixture = load_json(args.fixture)
        candidate, expected = apply_fixture(fixture)
        try:
            validate_contract(candidate)
        except ContractError as exc:
            if exc.code == expected:
                print(f"PASS: fixture {args.fixture.name} detected {exc.code}: {exc}")
                return 0
            print(f"ERROR: fixture expected {expected}, got {exc.code}: {exc}", file=sys.stderr)
            return 1
        print(f"ERROR: fixture expected {expected}, but validation passed", file=sys.stderr)
        return 1
    if args.markdown is None:
        parser.error("--contract requires --markdown")
    try:
        summary = validate_contract(load_json(args.contract), args.markdown)
    except ContractError as exc:
        print(f"ERROR {exc.code}: {exc}", file=sys.stderr)
        return 1
    print(
        "PASS: portfolio contract "
        f"({summary['series']} series, {summary['concerns']} concerns, {summary['handoffs']} handoffs, acyclic)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
