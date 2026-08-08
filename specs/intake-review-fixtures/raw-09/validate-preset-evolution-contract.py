#!/usr/bin/env python3
"""Validate the RAW-09 requirements contract without preset actions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


class ContractError(ValueError):
    """Stable validation error with a machine-readable reason code."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError("PEV000_INVALID_JSON", "JSON root must be an object")
    return value


def exact_set(value: object, expected: set[str], code: str, label: str) -> None:
    if not isinstance(value, list) or set(value) != expected:
        raise ContractError(code, f"{label} is incomplete")


def validate_contract(contract: dict) -> None:
    if (
        contract.get("schemaVersion") != "requirements-v1"
        or contract.get("documentType") != "AocPresetEvolutionContract"
        or contract.get("contractId") != "RAW-09-Preset-Evolution-Contract-requirements-v1"
        or contract.get("owner") != "RAW-09"
    ):
        raise ContractError("PEV000_INVALID_CONTRACT", "identity is invalid")

    boundary = contract.get("boundary", {})
    if (
        boundary.get("knowledgePackageProducer") != "RAW-08"
        or boundary.get("proposalAnalysisOwner") != "RAW-09"
        or boundary.get("canonicalTargetRepository") != "hindermath/home-baseline"
        or boundary.get("communityTargetRepository") != "github/spec-kit"
        or boundary.get("productStateOwned") is not False
        or boundary.get("presetWriteOwned") is not False
        or boundary.get("promotionOwned") is not False
        or boundary.get("executionEnabledByThisContract") is not False
    ):
        raise ContractError("PEV000_INVALID_CONTRACT", "system boundary is invalid")

    decisions = contract.get("decisions", {})
    threshold = decisions.get("promotionThreshold", {})
    minimum = threshold.get("promotionReviewMinimum", {})
    if (
        threshold.get("id") != "IAD901"
        or threshold.get("status") != "Answered"
        or minimum.get("reviewedFindings") != 2
        or minimum.get("independentProjects") != 2
        or not all(
            minimum.get(name) is True
            for name in (
                "positiveEvidenceRequired",
                "negativeEvidenceRequired",
                "boundRetrospectiveRequired",
                "crossProjectAssessmentRequired",
                "compatibilityRequired",
                "migrationRequired",
                "rollbackRequired",
                "testsRequired",
                "securityRequired",
                "accessibilityRequired",
                "documentationRequired",
            )
        )
        or minimum.get("blockingFindingsAllowed") is not False
        or threshold.get("singleProjectMayBecomeCanonical") is not False
        or threshold.get("promotionReviewEligibilityIsPromotion") is not False
    ):
        raise ContractError("PEV002_INSUFFICIENT_PROJECTS", "IAD901 is incomplete")

    repository = decisions.get("targetRepository", {})
    if (
        repository.get("id") != "IAD902"
        or repository.get("status") != "Answered"
        or repository.get("default") != "hindermath/home-baseline"
        or repository.get("communityAlternative") != "github/spec-kit"
        or repository.get("communityGeneralApplicabilityRequired") is not True
        or repository.get("serialSingleItemQueueRequired") is not True
        or repository.get("parallelCommunitySubmissionsAllowed") is not False
    ):
        raise ContractError("PEV007_REPOSITORY_NOT_ALLOWED", "IAD902 is incomplete")

    authority = decisions.get("promotionAuthority", {})
    if (
        authority.get("id") != "AUTH-RAW09-PROMOTION"
        or authority.get("status") != "Answered"
        or authority.get("standingAuthorityAllowed") is not False
        or authority.get("automaticBypassAllowed") is not False
        or authority.get("administrativeBypassAllowed") is not False
        or authority.get("historicDeliveryAuthoritySufficient") is not False
        or authority.get("missingAuthorityResult") != "Deferred"
    ):
        raise ContractError("PEV010_AUTHORITY_MISSING", "promotion authority is invalid")

    lifecycle = contract.get("lifecycle", {})
    if (
        lifecycle.get("unknownTransitionResult") != "Blocked"
        or lifecycle.get("missingEvidenceResult") != "Deferred"
        or lifecycle.get("missingAuthorityResult") != "Deferred"
        or lifecycle.get("providerFailureResult") != "DeferredWithPartialEvidence"
        or lifecycle.get("actualPromotionStateOwned") is not False
    ):
        raise ContractError("PEV000_INVALID_CONTRACT", "lifecycle is invalid")

    handoff_keys = {
        (item.get("id"), item.get("producer"), item.get("consumer"))
        for item in contract.get("handoffs", [])
        if isinstance(item, dict)
    }
    if handoff_keys != {
        ("H-RAW08-RAW09", "RAW-08", "RAW-09"),
        ("H-RAW09-HOME-BASELINE", "RAW-09", "hindermath/home-baseline"),
        ("H-RAW09-SPEC-KIT", "hindermath/home-baseline", "github/spec-kit"),
    }:
        raise ContractError("PEV007_REPOSITORY_NOT_ALLOWED", "handoffs are invalid")
    for handoff in contract.get("handoffs", []):
        if not all(handoff.get(name) for name in ("version", "requiredFields", "authority", "compatibility", "failureBehavior", "seriesRelation")):
            raise ContractError("PEV000_INVALID_CONTRACT", "handoff metadata is incomplete")

    exact_set(
        [item.get("id") for item in contract.get("childContracts", []) if isinstance(item, dict)],
        {
            "RAW09-CHILD-GAP-DETECTION",
            "RAW09-CHILD-GENERALISATION-REVIEW",
            "RAW09-CHILD-PROPOSAL-PACKAGE",
            "RAW09-CHILD-FIELD-VALIDATION",
        },
        "PEV000_INVALID_CONTRACT",
        "child contracts",
    )

    gates = contract.get("authorityGates", {})
    exact_set(
        gates.get("requiredCurrentAuthoritiesForAnyEnabledDeliveryPrompt"),
        {
            "ScopeAuthority",
            "StartAuthority",
            "ImplementationAuthority",
            "GovernanceWriteAuthority",
            "RemoteWriteAuthority",
            "MergeAuthority",
            "BypassAuthority",
            "ProviderAuthority",
            "PresetWriteAuthority",
            "PromotionAuthority",
        },
        "PEV010_AUTHORITY_MISSING",
        "authority gates",
    )
    if (
        gates.get("historicDeliveryAuthoritySufficient") is not False
        or gates.get("eligibleLifecycleSufficient") is not False
        or gates.get("readyReviewSufficient") is not False
        or gates.get("missingOrExpiredAuthorityResult") != "Deferred"
        or gates.get("currentPromptState") != "EnabledFailClosed"
    ):
        raise ContractError("PEV010_AUTHORITY_MISSING", "authority semantics are invalid")

    cross = contract.get("crossCutting", {})
    if (
        cross.get("platforms") != ["macOS", "Linux", "Windows"]
        or cross.get("sameLogicalOutcomesAcrossPlatforms") is not True
        or not all(cross.get(name) for name in ("security", "privacy", "publicContent", "accessibility", "containerAndRemoteNodes", "supplyChain"))
    ):
        raise ContractError("PEV012_CROSS_CUTTING_EVIDENCE_MISSING", "cross-cutting contract is incomplete")

    evidence = contract.get("evidence", {})
    if evidence.get("successExitCode") != 0 or evidence.get("validatorErrorExitCode") != 2:
        raise ContractError("PEV000_INVALID_CONTRACT", "exit codes are invalid")


def validate_fixture(contract: dict, fixture: dict) -> tuple[str, str]:
    fixture_id = fixture.get("fixtureId")
    case = fixture.get("case")
    expected = fixture.get("expectedReasonCode")
    if not fixture_id or not case or not expected:
        raise ContractError("PEV000_INVALID_FIXTURE", "fixture identity is incomplete")

    if case == "ValidPromotionReviewCandidate":
        required = set(contract["authorityGates"]["requiredCurrentAuthoritiesForAnyEnabledDeliveryPrompt"])
        condition = (
            fixture.get("reviewedFindings", 0) >= 2
            and fixture.get("independentProjects", 0) >= 2
            and fixture.get("positiveEvidence") is True
            and fixture.get("negativeEvidence") is True
            and fixture.get("retrospective") is True
            and fixture.get("crossProjectAssessment") is True
            and fixture.get("crossCuttingComplete") is True
            and fixture.get("blockingFindings") == 0
            and fixture.get("repository") == "hindermath/home-baseline"
            and set(fixture.get("currentAuthorities", [])) == required
            and fixture.get("actualPromotionClaimed") is False
        )
        code = "PEV001_VALID_PROPOSAL"
        label = "Gültig / Valid"
    elif case == "SingleProject":
        condition = fixture.get("independentProjects") == 1 and fixture.get("canonicalClaimed") is True
        code = "PEV002_INSUFFICIENT_PROJECTS"
        label = "Abgelehnt / Rejected"
    elif case == "NegativeEvidenceMissing":
        condition = fixture.get("negativeEvidence") is False and fixture.get("promotionReviewEligibleClaimed") is True
        code = "PEV004_NEGATIVE_EVIDENCE_MISSING"
        label = "Zurückgestellt / Deferred"
    elif case == "ProductSpecificGeneralisation":
        condition = fixture.get("productSpecific") is True and fixture.get("genericPresetRuleClaimed") is True
        code = "PEV006_PRODUCT_SPECIFIC_REJECTED"
        label = "Abgelehnt / Rejected"
    elif case == "CommunityWithoutApplicability":
        condition = fixture.get("repository") == "github/spec-kit" and fixture.get("communityGeneralApplicability") is False
        code = "PEV008_COMMUNITY_APPLICABILITY_MISSING"
        label = "Zurückgestellt / Deferred"
    elif case == "ParallelCommunityQueue":
        condition = fixture.get("repository") == "github/spec-kit" and fixture.get("activeSubmissions", 0) > 1
        code = "PEV009_SERIAL_QUEUE_VIOLATION"
        label = "Zurückgestellt / Deferred"
    elif case == "AuthorityMissing":
        required = set(contract["authorityGates"]["requiredCurrentAuthoritiesForAnyEnabledDeliveryPrompt"])
        condition = set(fixture.get("currentAuthorities", [])) != required and fixture.get("promotionClaimed") is True
        code = "PEV010_AUTHORITY_MISSING"
        label = "Zurückgestellt / Deferred"
    elif case == "PrivateOrCrossCuttingViolation":
        condition = fixture.get("privatePathPresent") is True or fixture.get("crossCuttingComplete") is False
        code = "PEV011_PRIVATE_DATA_REJECTED"
        label = "Abgelehnt / Rejected"
    else:
        raise ContractError("PEV000_INVALID_FIXTURE", "unknown fixture case")

    if not condition or expected != code:
        raise ContractError("PEV000_INVALID_FIXTURE", f"{case} does not prove {code}")
    return fixture_id, f"{label} ({code})"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    args = parser.parse_args()
    try:
        contract = read_json(args.contract)
        fixture = read_json(args.fixture)
        validate_contract(contract)
        fixture_id, outcome = validate_fixture(contract, fixture)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(f"ERROR: {exc}")
        return 2
    print(f"{fixture_id}: {outcome}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
