#!/usr/bin/env python3
"""Validate the RAW-03 requirements contract and its review fixtures."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


class ContractError(ValueError):
    """A stable, machine-readable validation error."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


def load_json(file_path: Path) -> dict:
    value = json.loads(file_path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError("ST001", f"{file_path}: root must be an object")
    return value


def validate_contract(contract: dict) -> None:
    if contract.get("schemaVersion") != "1.0" or contract.get("documentType") != "AocStateTruthfulnessContract":
        raise ContractError("ST001", "contract identity is invalid")
    decision = contract.get("decision", {})
    if (
        contract.get("owner") != "RAW-03"
        or decision.get("status") != "Superseded"
        or decision.get("supersededBy") != ["IAD301", "IAD302", "IAD303"]
    ):
        raise ContractError("ST002", "RAW-03 ownership and IAD301-IAD303 supersession of DEC-T03 are required")
    expected_statuses = ["Known", "Unknown", "Stale", "Unavailable", "Degraded"]
    if contract.get("stateStatuses") != expected_statuses:
        raise ContractError("ST003", "state status vocabulary is invalid")
    freshness = contract.get("freshnessPolicy", {})
    band_names = [band.get("name") for band in freshness.get("bands", [])]
    if band_names != ["Fresh", "Aging", "Stale", "Expired", "Unknown"]:
        raise ContractError("ST003", "freshness vocabulary or order is invalid")
    confidence = contract.get("confidencePolicy", {})
    if confidence.get("values") != ["High", "Medium", "Low", "Unknown"]:
        raise ContractError("ST004", "confidence vocabulary is invalid")
    if confidence.get("numericOrPercentageValuesAllowed") is not False or confidence.get("machineReadableReasonRequired") is not True:
        raise ContractError("ST004", "confidence must be deterministic, reasoned, and non-numeric")
    envelope = contract.get("envelope", {})
    required = set(envelope.get("requiredFields", []))
    expected = {
        "schemaVersion", "stateId", "valueOrAbsence", "sources", "observedAt",
        "freshnessAsOf", "freshness", "status", "authority", "confidence", "reasonCodes"
    }
    if required != expected:
        raise ContractError("ST005", "StateEnvelope required fields are incomplete")


def parse_utc(value: object, missing_code: str, invalid_code: str) -> datetime:
    if not isinstance(value, str) or not value:
        raise ContractError(missing_code, "timestamp is missing")
    if not value.endswith("Z"):
        raise ContractError(invalid_code, "timestamp must be UTC RFC3339 with Z")
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise ContractError(invalid_code, "timestamp is not valid RFC3339") from exc


def classify(case: dict) -> dict[str, str]:
    source_state = case.get("sourceState")
    source_id = case.get("sourceId")
    if source_state == "Missing" or not isinstance(source_id, str) or not source_id:
        return result("Unknown", "Unknown", "Unknown", "SOURCE_MISSING")
    if case.get("valueState") not in {"Value", "AbsenceDeclared"}:
        return result("Unknown", "Unknown", "Unknown", "VALUE_OR_ABSENCE_MISSING")
    try:
        observed = parse_utc(case.get("observedAt"), "OBSERVED_AT_MISSING", "OBSERVED_AT_INVALID")
        as_of = parse_utc(case.get("freshnessAsOf"), "FRESHNESS_AS_OF_MISSING", "FRESHNESS_AS_OF_INVALID")
    except ContractError as exc:
        return result("Unknown", "Unknown", "Unknown", exc.code)
    threshold = case.get("baseThresholdSeconds")
    skew = case.get("maxClockSkewSeconds")
    if not isinstance(threshold, (int, float)) or threshold <= 0:
        return result("Unknown", "Unknown", "Unknown", "FRESHNESS_UNKNOWN")
    if not isinstance(skew, (int, float)) or skew < 0:
        return result("Unknown", "Unknown", "Unknown", "FRESHNESS_UNKNOWN")
    age = (as_of - observed).total_seconds()
    tolerated_skew = age < 0 and abs(age) <= skew
    if age < 0 and not tolerated_skew:
        return result("Unknown", "Unknown", "Unknown", "OBSERVED_AT_IN_FUTURE")
    effective_age = max(age, 0)
    if effective_age <= 0.5 * threshold:
        freshness = "Fresh"
    elif effective_age <= threshold:
        freshness = "Aging"
    elif effective_age <= 2 * threshold:
        freshness = "Stale"
    else:
        freshness = "Expired"
    if source_state == "Unavailable":
        return result(freshness, "Unavailable", "Unknown", "SOURCE_UNAVAILABLE")
    authority_state = case.get("authorityState")
    if authority_state == "Missing":
        return result(freshness, "Unknown", "Unknown", "AUTHORITY_MISSING")
    conflict_state = case.get("conflictState")
    if authority_state == "Conflict" or conflict_state == "AuthorityConflict":
        return result(freshness, "Degraded", "Low", "AUTHORITY_CONFLICT")
    if conflict_state in {"SourceConflict", "Partial"}:
        return result(freshness, "Degraded", "Low", "SOURCE_CONFLICT")
    if freshness == "Expired":
        return result(freshness, "Unavailable", "Unknown", "EXPIRED_THRESHOLD_EXCEEDED")
    if freshness == "Stale":
        return result(freshness, "Stale", "Low", "STALE_THRESHOLD_EXCEEDED")
    if tolerated_skew:
        return result(freshness, "Known", "Medium", "CLOCK_SKEW_TOLERATED")
    if freshness == "Aging":
        return result(freshness, "Known", "Medium", "STATE_AGING")
    return result(freshness, "Known", "High", "STATE_FRESH")


def result(freshness: str, status: str, confidence: str, reason_code: str) -> dict[str, str]:
    return {
        "freshness": freshness,
        "status": status,
        "confidence": confidence,
        "reasonCode": reason_code,
    }


def validate_fixture(fixture: dict) -> None:
    kind = fixture.get("fixtureKind")
    if kind == "StateCases":
        cases = fixture.get("cases")
        if not isinstance(cases, list) or not cases:
            raise ContractError("ST006", "StateCases fixture needs at least one case")
        for case in cases:
            actual = classify(case)
            if actual != case.get("expected"):
                raise ContractError("ST006", f"{case.get('id')}: expected {case.get('expected')!r}, calculated {actual!r}")
        return
    if kind == "ProjectionParity":
        if fixture.get("jsonProjection") != fixture.get("textProjection"):
            raise ContractError("ST007", "JSON and text projection semantics differ")
        return
    raise ContractError("ST006", f"unknown fixtureKind: {kind!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    args = parser.parse_args()
    contract = load_json(args.contract)
    fixture = load_json(args.fixture)
    expected_outcome = fixture.get("expectedOutcome")
    try:
        validate_contract(contract)
        validate_fixture(fixture)
    except ContractError as exc:
        if expected_outcome == "Rejected" and fixture.get("expectedError") == exc.code:
            print(f"{fixture.get('fixtureId')}: Rejected ({exc})")
            return 0
        raise
    if expected_outcome == "Rejected":
        raise ContractError("ST008", "fixture expected rejection but validation passed")
    if expected_outcome != "Valid":
        raise ContractError("ST008", "expectedOutcome must be Valid or Rejected")
    print(f"{fixture.get('fixtureId')}: Valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
