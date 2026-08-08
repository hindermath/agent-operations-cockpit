#!/usr/bin/env python3
"""Validate the RAW-08 requirements contract without product execution."""

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
        raise ContractError("WFE000_INVALID_JSON", "JSON root must be an object")
    return data


def require_exact_set(actual: object, expected: set[str], code: str, label: str) -> None:
    if not isinstance(actual, list) or set(actual) != expected:
        raise ContractError(code, f"{label} is incomplete")


def validate_contract(contract: dict) -> None:
    if (
        contract.get("schemaVersion") != "requirements-v1"
        or contract.get("documentType") != "AocWorkflowEvidenceContract"
        or contract.get("contractId") != "RAW-08-Workflow-Evidence-Contract-requirements-v1"
        or contract.get("owner") != "RAW-08"
    ):
        raise ContractError("WFE000_INVALID_CONTRACT", "contract identity is invalid")

    boundary = contract.get("boundary", {})
    if (
        boundary.get("programToKnowledgeOwner") != "RAW-08"
        or boundary.get("executionNodeEvidenceOwner") != "RAW-05"
        or boundary.get("cliExecutionEvidenceOwner") != "RAW-06"
        or boundary.get("knowledgePackageConsumer") != "RAW-09"
        or boundary.get("productStateOwned") is not False
        or boundary.get("productCommandOwned") is not False
        or boundary.get("presetWriteOrPromotionOwned") is not False
        or boundary.get("executionEnabledByThisContract") is not False
    ):
        raise ContractError("WFE000_INVALID_CONTRACT", "ownership boundary is invalid")

    decisions = contract.get("decisions", {})
    persistence = decisions.get("persistence", {})
    if (
        persistence.get("id") != "IAD801"
        or persistence.get("status") != "Answered"
        or persistence.get("model") != "VersionedCanonicalJsonReceiptLast"
        or persistence.get("canonicalRoot") != "evidence/workflow/<workflow-id>/"
        or persistence.get("sameDirectoryTemporaryWrite") is not True
        or persistence.get("validateBeforeReplace") is not True
        or persistence.get("atomicReplaceRequired") is not True
        or persistence.get("receiptPublishedLast") is not True
        or persistence.get("partialTemporaryFileIsState") is not False
        or persistence.get("recoveryAnchor") != "LastFullyValidatedHashBoundReceipt"
        or persistence.get("databaseMayBeCanonical") is not False
    ):
        raise ContractError("WFE013_PARTIAL_ARTIFACT", "IAD801 is incomplete")

    attestation = decisions.get("attestation", {})
    if (
        attestation.get("id") != "IAD802"
        or attestation.get("status") != "Answered"
        or attestation.get("model") != "VersionedStandardDetachedAttestationEnvelope"
        or attestation.get("signedValue") != "CanonicalSha256ContentHash"
        or attestation.get("trustPolicySeparatelyVersioned") is not True
        or attestation.get("privateKeysOrSecretsAllowedInRepository") is not False
        or any(
            attestation.get(field) != "Blocked"
            for field in (
                "missingSignatureResult",
                "unknownKeyOrTrustRootResult",
                "invalidSignatureResult",
                "hashMismatchResult",
                "expiredPolicyResult",
            )
        )
    ):
        raise ContractError("WFE006_SIGNATURE_INVALID", "IAD802 is incomplete")

    retention = decisions.get("retention", {})
    classes = {
        item.get("evidenceClass"): item
        for item in retention.get("classes", [])
        if isinstance(item, dict)
    }
    if (
        retention.get("id") != "IAD803"
        or retention.get("status") != "Answered"
        or retention.get("model") != "EvidenceClassRetentionWithLegalHold"
        or classes.get("GovernanceDecisionCompletionReceipt", {}).get("retention")
        != "ProjectLifetime"
        or classes.get("OperationalExecution", {}).get("retentionDaysAfterCompletion") != 90
        or classes.get("SecurityAndFailure", {}).get("retentionMonthsAfterCompletion") != 12
        or retention.get("legalHoldSuspendsDeletion") is not True
        or retention.get("deletionReceiptRequired") is not True
        or retention.get("secretsAllowed") is not False
        or retention.get("unnecessaryPersonalDataAllowed") is not False
    ):
        raise ContractError("WFE007_RETENTION_VIOLATION", "IAD803 is incomplete")

    artifact = contract.get("artifactModel", {})
    require_exact_set(
        artifact.get("artifactTypes"),
        {
            "Charter",
            "Source",
            "Decision",
            "Intake",
            "Spec",
            "Plan",
            "Task",
            "Evidence",
            "Retrospective",
            "KnowledgePackage",
            "Receipt",
        },
        "WFE000_INVALID_CONTRACT",
        "artifact types",
    )
    require_exact_set(
        artifact.get("evidenceClasses"),
        {"Positive", "Negative", "ProviderFailure"},
        "WFE005_PROVIDER_FAILURE",
        "evidence classes",
    )
    if (
        artifact.get("providerFailureMayClaimCompletion") is not False
        or artifact.get("retrospectiveMayCreateNormativeDecision") is not False
    ):
        raise ContractError("WFE005_PROVIDER_FAILURE", "evidence authority is invalid")

    lifecycle = contract.get("lifecycle", {})
    require_exact_set(
        lifecycle.get("allowedTransitions"),
        {
            "Draft->Validated",
            "Validated->Approved",
            "Approved->InProgress",
            "InProgress->Blocked",
            "Blocked->InProgress",
            "InProgress->Completed",
            "Completed->Superseded",
            "Superseded->Expired",
        },
        "WFE002_INVALID_TRANSITION",
        "allowed transitions",
    )
    if (
        lifecycle.get("unknownTransitionResult") != "Blocked"
        or lifecycle.get("missingPreconditionResult") != "Blocked"
        or lifecycle.get("missingAuthorityResult") != "Blocked"
        or lifecycle.get("hashDriftResult") != "Blocked"
        or lifecycle.get("providerFailureResult") != "BlockedWithPartialEvidence"
    ):
        raise ContractError("WFE000_INVALID_CONTRACT", "lifecycle failure behavior is invalid")

    handoffs = contract.get("handoffs", [])
    handoff_keys = {
        (item.get("id"), item.get("producer"), item.get("consumer"), item.get("version"))
        for item in handoffs
        if isinstance(item, dict)
    }
    if handoff_keys != {
        ("H-RAW05-RAW08", "RAW-05", "RAW-08", "requirements-v1"),
        ("H-RAW06-RAW08", "RAW-06", "RAW-08", "requirements-v1"),
        ("H-RAW08-RAW09", "RAW-08", "RAW-09", "requirements-v1"),
    }:
        raise ContractError("WFE008_HANDOFF_INCOMPATIBLE", "handoff set is invalid")
    for handoff in handoffs:
        if not all(handoff.get(name) for name in ("requiredFields", "authority", "compatibility", "failureBehavior", "seriesRelation")):
            raise ContractError("WFE008_HANDOFF_INCOMPATIBLE", "handoff metadata is incomplete")

    children = contract.get("childContracts", [])
    require_exact_set(
        [item.get("id") for item in children if isinstance(item, dict)],
        {
            "RAW08-CHILD-ARTIFACT-LIFECYCLE",
            "RAW08-CHILD-TRACEABILITY-GRAPH",
            "RAW08-CHILD-EVIDENCE-RECEIPT",
            "RAW08-CHILD-RETROSPECTIVE-HANDOFF",
        },
        "WFE008_HANDOFF_INCOMPATIBLE",
        "child contracts",
    )

    gates = contract.get("authorityGates", {})
    require_exact_set(
        gates.get("requiredCurrentAuthoritiesForAutonomousExecution"),
        {
            "ScopeAuthority",
            "StartAuthority",
            "ImplementationAuthority",
            "GovernanceWriteAuthority",
            "RemoteWriteAuthority",
            "MergeAuthority",
            "BypassAuthority",
            "ProviderAuthority",
        },
        "WFE003_AUTHORITY_MISSING",
        "authority gates",
    )
    if (
        gates.get("historicalDeliveryAuthoritySufficient") is not False
        or gates.get("eligibleLifecycleSufficient") is not False
        or gates.get("readyReviewSufficient") is not False
        or gates.get("missingOrExpiredAuthorityResult") != "Blocked"
    ):
        raise ContractError("WFE003_AUTHORITY_MISSING", "authority semantics are invalid")

    cross = contract.get("crossCutting", {})
    if (
        cross.get("platforms") != ["macOS", "Linux", "Windows"]
        or cross.get("sameLogicalOutcomesAcrossPlatforms") is not True
        or cross.get("documentationGermanFirstEnglishSecond") is not True
        or cross.get("cefrB2") is not True
        or cross.get("wcag22AAWhereApplicable") is not True
        or not all(cross.get(name) for name in ("security", "privacy", "publicContent", "accessibility", "containerAndRemoteNodes", "supplyChain"))
    ):
        raise ContractError("WFE010_A11Y_PROJECTION_REQUIRED", "cross-cutting contract is incomplete")

    evidence = contract.get("evidence", {})
    if evidence.get("successExitCode") != 0 or evidence.get("validatorErrorExitCode") != 2:
        raise ContractError("WFE000_INVALID_CONTRACT", "evidence exit codes are invalid")


def validate_fixture(contract: dict, fixture: dict) -> tuple[str, str]:
    fixture_id = fixture.get("fixtureId")
    kind = fixture.get("fixtureKind")
    expected = fixture.get("expectedOutcome")
    if not isinstance(fixture_id, str) or not fixture_id:
        raise ContractError("WFE000_INVALID_FIXTURE", "fixtureId is required")

    if kind == "ValidEndToEnd":
        require_exact_set(
            fixture.get("artifacts"),
            set(contract["artifactModel"]["artifactTypes"]),
            "WFE013_PARTIAL_ARTIFACT",
            "end-to-end artifacts",
        )
        require_exact_set(
            fixture.get("evidenceClasses"),
            {"Positive", "Negative", "ProviderFailure"},
            "WFE005_PROVIDER_FAILURE",
            "end-to-end evidence classes",
        )
        transition_set = set(fixture.get("transitions", []))
        if not transition_set.issubset(set(contract["lifecycle"]["allowedTransitions"])):
            raise ContractError("WFE002_INVALID_TRANSITION", "positive transition is invalid")
        handoffs = fixture.get("handoffs", [])
        handoff_set = {
            (item.get("id"), item.get("version"), item.get("compatible"))
            for item in handoffs
            if isinstance(item, dict)
        }
        if handoff_set != {
            ("H-RAW05-RAW08", "requirements-v1", True),
            ("H-RAW06-RAW08", "requirements-v1", True),
            ("H-RAW08-RAW09", "requirements-v1", True),
        }:
            raise ContractError("WFE008_HANDOFF_INCOMPATIBLE", "positive handoffs are incomplete")
        attestation = fixture.get("attestation", {})
        retention = fixture.get("retention", {})
        cross = fixture.get("crossCutting", {})
        if (
            expected != "Valid"
            or fixture.get("expectedReasonCode") != "WFE001_VALID"
            or fixture.get("traceabilityComplete") is not True
            or fixture.get("allInputAndOutputHashesValid") is not True
            or not all(attestation.get(name) is True for name in ("signaturePresent", "signatureValid", "keyAllowed", "trustRootAllowed", "policyCurrent"))
            or retention.get("operationalDays") != 90
            or retention.get("securityAndFailureMonths") != 12
            or retention.get("legalHoldSuspendsDeletion") is not True
            or retention.get("deletionReceiptRequired") is not True
            or cross.get("dataMinimised") is not True
            or cross.get("publicContentDeidentified") is not True
            or cross.get("germanFirstEnglishSecond") is not True
            or cross.get("textAndKeyboardAlternatives") is not True
            or cross.get("platforms") != ["macOS", "Linux", "Windows"]
            or cross.get("sameLogicalOutcome") is not True
            or cross.get("nodeProvenanceComplete") is not True
            or cross.get("implementationDependencyIntroduced") is not False
            or fixture.get("providerFailureClaimsCompletion") is not False
            or fixture.get("retrospectiveCreatesNormativeDecision") is not False
            or fixture.get("presetPromotionClaimed") is not False
        ):
            raise ContractError("WFE000_INVALID_FIXTURE", "positive end-to-end evidence is incomplete")
        require_exact_set(
            fixture.get("currentAuthorities"),
            set(contract["authorityGates"]["requiredCurrentAuthoritiesForAutonomousExecution"]),
            "WFE003_AUTHORITY_MISSING",
            "positive authorities",
        )
        return fixture_id, "Gültig / Valid (WFE001_VALID)"

    if kind == "InvalidTransition":
        condition = (
            f"{fixture.get('from')}->{fixture.get('to')}" not in contract["lifecycle"]["allowedTransitions"]
            and fixture.get("preconditionsComplete") is False
            and fixture.get("completionClaimed") is True
        )
        code = "WFE002_INVALID_TRANSITION"
    elif kind == "MissingAuthority":
        required = set(contract["authorityGates"]["requiredCurrentAuthoritiesForAutonomousExecution"])
        condition = (
            set(fixture.get("currentAuthorities", [])) != required
            and fixture.get("historicalDeliveryAuthorityPresent") is True
            and fixture.get("eligible") is True
            and fixture.get("readyReview") is True
            and fixture.get("mergeClaimed") is True
        )
        code = "WFE003_AUTHORITY_MISSING"
    elif kind == "ProviderFailure":
        condition = (
            fixture.get("providerFailure") is True
            and fixture.get("partialEvidencePreserved") is True
            and fixture.get("completionClaimed") is False
            and fixture.get("retryClaimedSuccessful") is False
        )
        code = "WFE005_PROVIDER_FAILURE"
        if expected != "BlockedWithPartialEvidence":
            raise ContractError("WFE000_INVALID_FIXTURE", "provider failure outcome is invalid")
        if fixture.get("expectedReasonCode") != code or not condition:
            raise ContractError("WFE000_INVALID_FIXTURE", "provider failure evidence is incomplete")
        return fixture_id, f"Blockiert mit Teilevidence / Blocked with partial evidence ({code})"
    elif kind == "InvalidAttestation":
        condition = (
            fixture.get("signaturePresent") is True
            and (
                fixture.get("signatureValid") is False
                or fixture.get("keyAllowed") is False
                or fixture.get("trustRootAllowed") is False
                or fixture.get("policyCurrent") is False
            )
            and fixture.get("completionClaimed") is True
        )
        code = "WFE006_SIGNATURE_INVALID"
    elif kind == "RetentionViolation":
        condition = (
            fixture.get("evidenceClass") == "OperationalExecution"
            and fixture.get("ageDaysAfterCompletion", 0) > 90
            and fixture.get("legalHoldActive") is False
            and fixture.get("deletionReceiptPresent") is False
            and fixture.get("retainedWithoutException") is True
        )
        code = "WFE007_RETENTION_VIOLATION"
    elif kind == "IncompatibleHandoff":
        condition = (
            fixture.get("handoffId") == "H-RAW06-RAW08"
            and fixture.get("expectedVersion") == "requirements-v1"
            and fixture.get("observedVersion") != "requirements-v1"
            and fixture.get("knownOutcome") is False
            and fixture.get("completionClaimed") is True
        )
        code = "WFE008_HANDOFF_INCOMPATIBLE"
    elif kind == "CrossCuttingViolation":
        expected_codes = {
            "WFE009_PERSONAL_DATA_REJECTED",
            "WFE010_A11Y_PROJECTION_REQUIRED",
            "WFE011_PLATFORM_SEMANTICS_MISMATCH",
            "WFE012_SUPPLY_CHAIN_EVIDENCE_REQUIRED",
        }
        condition = (
            fixture.get("privateHostPathPresent") is True
            and fixture.get("unnecessaryPersonalDataPresent") is True
            and fixture.get("textAlternativePresent") is False
            and fixture.get("keyboardAlternativePresent") is False
            and fixture.get("sameLogicalOutcomeAcrossPlatforms") is False
            and fixture.get("implementationDependencyIntroduced") is True
            and fixture.get("sbomPresent") is False
            and fixture.get("vulnerabilityEvidencePresent") is False
        )
        if expected != "Rejected" or set(fixture.get("expectedReasonCodes", [])) != expected_codes or not condition:
            raise ContractError("WFE000_INVALID_FIXTURE", "cross-cutting negative evidence is incomplete")
        return fixture_id, "Abgelehnt / Rejected (WFE009,WFE010,WFE011,WFE012)"
    else:
        raise ContractError("WFE000_INVALID_FIXTURE", f"unknown fixtureKind {kind}")

    if expected not in {"Rejected", "Blocked"} or fixture.get("expectedReasonCode") != code or not condition:
        raise ContractError("WFE000_INVALID_FIXTURE", "negative fixture does not prove its expected outcome")
    result = "Blockiert / Blocked" if expected == "Blocked" else "Abgelehnt / Rejected"
    return fixture_id, f"{result} ({code})"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    args = parser.parse_args()

    try:
        contract = read_json(args.contract)
        fixture = read_json(args.fixture)
        validate_contract(contract)
        fixture_id, result = validate_fixture(contract, fixture)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(f"ERROR: {exc}")
        return 2

    print(f"{fixture_id}: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
