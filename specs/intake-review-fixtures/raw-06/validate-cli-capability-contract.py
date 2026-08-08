#!/usr/bin/env python3
"""Validate the RAW-06 requirements contract and its evidence fixtures."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


class ContractError(ValueError):
    """A stable, machine-readable validation error."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


def read_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ContractError("CLI000_INVALID_JSON", "JSON root must be an object")
    return data


def validate_contract(contract: dict) -> None:
    if (
        contract.get("documentType") != "AocCliCapabilityContract"
        or contract.get("schemaVersion") != "requirements-v1"
        or contract.get("owner") != "RAW-06"
    ):
        raise ContractError("CLI000_INVALID_CONTRACT", "contract identity is invalid")

    boundary = contract.get("boundary", {})
    if (
        boundary.get("logicalOrchestrationOwner") != "RAW-02"
        or boundary.get("executionNodeOwner") != "RAW-05"
        or boundary.get("processAndEnvironmentOwner") != "RAW-06"
        or boundary.get("executionEnabledByThisContract") is not False
    ):
        raise ContractError("CLI000_INVALID_CONTRACT", "ownership or execution boundary is invalid")

    decisions = contract.get("decisions", {})
    process_api = decisions.get("processApi", {})
    if (
        process_api.get("id") != "IAD601"
        or process_api.get("model") != "TypedShellFreeProcessApi"
        or process_api.get("argumentsAreArray") is not True
        or process_api.get("shellEvaluationAllowed") is not False
    ):
        raise ContractError("CLI007_SHELL_EVAL_FORBIDDEN", "IAD601 is not fail closed")

    exit_model = decisions.get("exitAndSignal", {})
    expected_outcomes = {
        "Succeeded",
        "ExitedNonZero",
        "StartFailed",
        "TimedOut",
        "Cancelled",
        "Signaled",
        "ToolMissing",
    }
    if (
        exit_model.get("id") != "IAD602"
        or set(exit_model.get("outcomes", [])) != expected_outcomes
        or exit_model.get("nativeDetailsPreserved") is not True
        or exit_model.get("partialOutputPreserved") is not True
        or exit_model.get("automaticUnknownRetryAllowed") is not False
        or exit_model.get("nonIdempotentRetryAllowed") is not False
    ):
        raise ContractError("CLI011_RETRY_FORBIDDEN", "IAD602 is incomplete")

    environment = decisions.get("environmentAllowlist", {})
    if (
        environment.get("id") != "IAD603"
        or environment.get("model") != "VersionedCapabilityAndNodeAllowlist"
        or environment.get("parentEnvironmentInheritedByDefault") is not False
        or environment.get("secretValuesAllowedInDescriptorLogOrReceipt") is not False
        or environment.get("unknownVariablesAllowed") is not False
    ):
        raise ContractError("CLI008_ENVIRONMENT_REJECTED", "IAD603 is not fail closed")

    remote = decisions.get("remoteTransport", {})
    if (
        remote.get("id") != "IAD604"
        or remote.get("contract") != "TransportNeutralRemoteExecutionContract"
        or remote.get("referenceAdapter") != "SSHv2"
        or remote.get("enabledByDefault") is not False
        or remote.get("arbitraryRemoteShellAllowed") is not False
        or remote.get("hostIdentityVerificationRequired") is not True
        or remote.get("keyOrCertificateAuthenticationRequired") is not True
        or remote.get("remoteWriteAuthorityGranted") is not False
        or remote.get("activationRequiresSeparateReviewAndAuthority") is not True
    ):
        raise ContractError("CLI009_REMOTE_DISABLED", "IAD604 is not fail closed")

    handoffs = contract.get("handoffs", [])
    handoff_keys = {
        (item.get("id"), item.get("producer"), item.get("consumer"))
        for item in handoffs
        if isinstance(item, dict)
    }
    if handoff_keys != {
        ("H-RAW05-RAW06", "RAW-05", "RAW-06"),
        ("H-RAW06-RAW02", "RAW-06", "RAW-02"),
        ("H-RAW06-RAW08", "RAW-06", "RAW-08"),
    }:
        raise ContractError("CLI000_INVALID_CONTRACT", "handoff set is invalid")

    cross_cutting = contract.get("crossCutting", {})
    if (
        cross_cutting.get("platforms") != ["macOS", "Linux", "Windows"]
        or cross_cutting.get("privacyDataMinimised") is not True
        or cross_cutting.get("documentationGermanFirstEnglishSecond") is not True
        or cross_cutting.get("cefrB2") is not True
        or cross_cutting.get("wcag22AAWhereApplicable") is not True
    ):
        raise ContractError("CLI000_INVALID_CONTRACT", "cross-cutting contract is incomplete")


def validate_fixture(fixture: dict) -> tuple[str, str]:
    fixture_id = fixture.get("fixtureId")
    kind = fixture.get("fixtureKind")
    expected = fixture.get("expectedOutcome")
    if not isinstance(fixture_id, str) or not fixture_id:
        raise ContractError("CLI000_INVALID_FIXTURE", "fixtureId is required")

    if kind == "ValidContract":
        if expected != "Valid" or not fixture.get("cases"):
            raise ContractError("CLI000_INVALID_FIXTURE", "positive cases are missing")
        for case in fixture["cases"]:
            if (
                case.get("shellEvaluation") is not False
                or not isinstance(case.get("arguments"), list)
                or case.get("sideEffectClass") != "ReadOnlyProbe"
            ):
                raise ContractError("CLI007_SHELL_EVAL_FORBIDDEN", "positive case is unsafe")
        return fixture_id, "Gültig / Valid"

    negative_rules = {
        "ShellEvaluation": (
            "CLI007_SHELL_EVAL_FORBIDDEN",
            fixture.get("shellEvaluation") is True
            and fixture.get("commandStringFromUntrustedInput") is True,
        ),
        "EnvironmentInjection": (
            "CLI008_ENVIRONMENT_REJECTED",
            fixture.get("declaredInAllowlist") is False
            and fixture.get("purposeDeclared") is False,
        ),
        "RemoteActivation": (
            "CLI009_REMOTE_DISABLED",
            fixture.get("remoteExecutionRequested") is True
            and fixture.get("separateReviewPresent") is False
            and fixture.get("separateAuthorityPresent") is False,
        ),
        "SecretMaterial": (
            "CLI010_SECRET_MATERIAL_REJECTED",
            fixture.get("secretReferencePresent") is False
            and (
                fixture.get("secretValuePresentInDescriptor") is True
                or fixture.get("secretValuePresentInLog") is True
            ),
        ),
        "NonIdempotentRetry": (
            "CLI011_RETRY_FORBIDDEN",
            fixture.get("idempotent") is False
            and fixture.get("automaticRetryRequested") is True,
        ),
    }
    if kind not in negative_rules:
        raise ContractError("CLI000_INVALID_FIXTURE", f"unknown fixtureKind {kind}")
    reason_code, condition = negative_rules[kind]
    if expected != "Rejected" or fixture.get("expectedReasonCode") != reason_code or not condition:
        raise ContractError("CLI000_INVALID_FIXTURE", "negative fixture does not prove its rejection")
    return fixture_id, f"Abgelehnt / Rejected ({reason_code})"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    args = parser.parse_args()

    try:
        contract = read_json(args.contract)
        fixture = read_json(args.fixture)
        validate_contract(contract)
        fixture_id, result = validate_fixture(fixture)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(f"ERROR: {exc}")
        return 2

    print(f"{fixture_id}: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
