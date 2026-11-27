"""Read-only preflight for the nine Single reviews required before RAW-01."""

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GATE = "specs/intake-series/aoc-raw-features/review-gate.json"


def repository_file(relative):
    path = Path(relative)
    resolved = (ROOT / path).resolve()
    if path.is_absolute() or ".." in path.parts or not resolved.is_relative_to(ROOT) or not resolved.is_file():
        raise ValueError(f"Missing or unsafe evidence path: {relative}")
    return resolved


def read(relative):
    return json.loads(repository_file(relative).read_text(encoding="utf-8-sig"))


def validate_artifact(preset, kind, flag, path):
    repository_file(path)
    script = f".specify/presets/intake-{preset}-governance/scripts/validate-intake-{kind}"
    subprocess.run(["bash", f"{script}.sh", f"--{flag.lower()}", path, "--repo", "."], cwd=ROOT, check=True)
    subprocess.run(["pwsh", "-NoProfile", "-File", f"{script}.ps1", f"-{flag}", path, "-Repo", "."], cwd=ROOT, check=True)


def validate():
    gate = read(GATE)
    config = read("requirements/intake-governance.json")
    manifest_path = gate["seriesManifest"]
    if manifest_path != config["collections"]["seriesManifest"]:
        raise ValueError("The RAW gate and the active series are out of sync.")
    manifest = read(manifest_path)
    members = manifest["orderedTargets"]
    reviews = gate["requiredReviews"]
    paths = [member["path"] for member in members]
    expected_ids = {f"{i:02}" for i in range(1, 10)}
    ids = {match.group(1) for path in paths if (match := re.fullmatch(
        r"requirements/intakes/active/Lastenheft_RAW-(\d{2})-[^/]+\.md", path
    ))}
    if ids != expected_ids or len(paths) != 9 or [row["intakePath"] for row in reviews] != paths:
        raise ValueError("The gate must cover all nine RAW series targets exactly once in series order.")
    eligible = [member["path"] for member in members if member["status"] == "Eligible"]
    if eligible != [gate["initialCandidate"]] or eligible != paths[:1] or "/Lastenheft_RAW-01-" not in eligible[0]:
        raise ValueError("RAW-01 must be the sole selected initial candidate.")

    prerequisite = gate["prerequisite"]
    milestone = read(prerequisite["evidence"])["authoringMilestone"]
    text = repository_file(prerequisite["intake"]).read_text(encoding="utf-8-sig")
    if milestone["intake"] != prerequisite["intake"] or hashlib.sha256(text.encode()).hexdigest() != prerequisite["normalizedSha256"]:
        raise ValueError("META-LH-05 authoring evidence does not bind the milestone intake.")
    if {Path(path).name for path in milestone["outputs"]} != {Path(path).name for path in paths}:
        raise ValueError("META-LH-05 authoring evidence does not cover this RAW series.")

    superseded = {
        read(path.relative_to(ROOT)).get("supersedes")
        for path in (ROOT / "specs/intake-review-results").glob("*.json")
    }
    validate_artifact("sequencing", "series-manifest", "File", manifest_path)
    for member, row in zip(members, reviews):
        target = {"path": member["path"], "normalizedSha256": member["normalizedSha256"]}
        authoring = read(row["authoringReceipt"])
        review = read(row["singleReview"])
        if (authoring["status"] != "ReadyForReview" or authoring["target"] != target
                or authoring["series"]["seriesId"] != manifest["seriesId"]
                or authoring["series"]["manifestPath"] != manifest_path):
            raise ValueError(f"Authoring receipt does not bind the series target: {member['path']}")
        if (review["mode"] != "Single" or review["status"] != "Ready" or review["reviewId"] in superseded
                or len(review["targets"]) != 1
                or any(review["targets"][0].get(key) != value for key, value in target.items())
                or any(review[name] for name in ("findings", "questions", "acceptedRisks"))):
            raise ValueError(f"No current Ready Single review for: {member['path']}")
        validate_artifact("authoring", "authoring-receipt", "Receipt", row["authoringReceipt"])
        validate_artifact("review", "review-result", "Result", row["singleReview"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        validate()
    except (KeyError, OSError, TypeError, ValueError, subprocess.CalledProcessError) as error:
        sys.exit(f"RAW review gate blocked: {error}")
    print("PASS: RAW-01 selected; nine current receipts and Ready Single reviews passed in Bash and PowerShell.")
