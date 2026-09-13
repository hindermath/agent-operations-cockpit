#!/usr/bin/env python3
"""Zusätzliche unittest-Fälle / Additional established unittest cases."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parents[3]
CONTRACTS = "specs/004-series-eligibility/contracts"
FIXTURE = "specs/intake-review-fixtures/meta-lh-04/valid-parallel.json"
CONTRACT = "requirements/baseline/series-eligibility-contract.json"
SHELL = "bash"
KEYS = ['authority', 'sideEffects', 'reversibility', 'writeScope', 'decisions',
        'integration', 'review', 'abort', 'recovery']
MODES = ['manual-assisted', 'single-autonomous', 'serial-autonomous',
         'parallel-autonomous', 'research-only', 'blocked']
FLAGS = {'currentAuthority': 'authority', 'disjointWrites': 'writeScope',
         'sharedOpenDecisions': 'decisions', 'consolidationReview': 'review',
         'abortRule': 'abort', 'recoveryRule': 'recovery'}


def valid_fixture():
    return json.loads((REPO / FIXTURE).read_text())


def snapshot(repo: Path) -> dict:
    return {str(p.relative_to(repo)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in repo.rglob("*") if p.is_file()}


class EligibilityTests(unittest.TestCase):
    def run_fixture(self, fixture, *, raw=False, legacy_error=None,
                    provider_exit=None, provider_stdout=False,
                    fixture_path='fixture.json', as_text=False):
        # Testaufbau ist getrennt von der lesenden Abfrage. / Separate setup from query.
        with tempfile.TemporaryDirectory(prefix="aoc eligibility ") as temporary:
            repo = Path(temporary)
            target = repo / CONTRACT
            target.parent.mkdir(parents=True)
            shutil.copyfile(REPO / CONTRACT, target)
            (repo / "fixture.json").write_text(fixture if raw else json.dumps(fixture), encoding="utf-8")
            surface = REPO / CONTRACTS
            if legacy_error is not None:
                surface = repo / CONTRACTS
                surface.mkdir(parents=True)
                for name in ['validate_series_eligibility.py', 'validate-series-eligibility.sh',
                             'validate-series-eligibility.ps1']:
                    shutil.copyfile(REPO / CONTRACTS / name, surface / name)
                legacy = repo / 'specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.py'
                legacy.parent.mkdir(parents=True)
                legacy.write_text('def meets_parallel_eligibility(contract, fixture):\n'
                                  '    raise ' + legacy_error + '("harmless-private-sentinel")\n')
            environment = os.environ.copy()
            if provider_exit is not None:
                tools_dir = repo / 'temporary tools'
                tools_dir.mkdir()
                interpreter = tools_dir / 'python3'
                interpreter.write_text('#!/bin/sh\nprintf harmless-private-sentinel'
                                       + ('\n' if provider_stdout else ' >&2\n') + 'exit '
                                       + str(provider_exit) + '\n')
                interpreter.chmod(0o755)
                environment['PATH'] = str(tools_dir) + os.pathsep + environment['PATH']
            before = snapshot(repo)
            if SHELL == "bash":
                args = [os.environ.get("AOC_GIT_BASH_EXE", "bash"),
                        str(surface / "validate-series-eligibility.sh"), "--repo", str(repo),
                        "--fixture", fixture_path]
                if not as_text:
                    args.append('--json')
            else:
                args = ["pwsh", "-NoProfile", "-File",
                        str(surface / "validate-series-eligibility.ps1"), "-Repo", str(repo),
                        "-Fixture", fixture_path]
                if not as_text:
                    args.append('-Json')
            child = subprocess.run(args, cwd=REPO, capture_output=True, text=True, env=environment)
            # Child-Exits bleiben sichtbar, auch wenn der Negativtest besteht.
            # Preserve actual child exits even when a negative test passes.
            print(json.dumps({"shell": SHELL, "test": self.id(),
                              "childExit": child.returncode, "stdout": child.stdout,
                              "stderr": child.stderr}, ensure_ascii=False), flush=True)
            self.assertEqual(before, snapshot(repo), "query wrote files")
            if legacy_error is not None or provider_exit is not None:
                self.assertNotIn('harmless-private-sentinel', child.stdout + child.stderr)
                self.assertNotIn('Traceback', child.stdout + child.stderr)
            if as_text:
                return child.stdout, child.returncode
            return json.loads(child.stdout), child.returncode

    def test_criteria_cardinality(self):
        result, code = self.run_fixture(valid_fixture())
        self.assertEqual(0, code)
        self.assertEqual(KEYS, list(result['criteria']))
        cases = []
        for key in KEYS:
            fixture = valid_fixture()
            del fixture['criteria'][key]
            cases.append(('missing-' + key, fixture))
        fixture = valid_fixture()
        fixture['criteria']['extra'] = 'bounded'
        cases.append(('ten', fixture))
        fixture = valid_fixture()
        del fixture['criteria']['abort'], fixture['criteria']['recovery']
        fixture['criteria']['abortAndRecovery'] = 'defined'
        cases.append(('merged-eight', fixture))
        for value in [None, {}, [], '', 9, True]:
            fixture = valid_fixture()
            fixture['criteria'] = value
            cases.append(('criteria-type-' + repr(value), fixture))
        for field in ['unexpected', 'Authority']:
            fixture = valid_fixture()
            fixture[field] = 'harmless-private-sentinel'
            cases.append(('unknown-' + field, fixture))
        for field in ['fixtureId', 'expectedOutcome']:
            for value in [None, '', [], {}, 1, True]:
                fixture = valid_fixture()
                fixture[field] = value
                cases.append(('field-type-' + field + repr(value), fixture))
        cases.extend(('root-' + repr(value), value) for value in [None, [], '', 9, True])
        for label, fixture in cases:
            with self.subTest(case=label):
                result, code = self.run_fixture(fixture)
                self.assertEqual(2, code)
                self.assertEqual('ProductFailure', result['failureClass'])
                self.assertEqual('Blocked', result['outcome'])
                self.assertNotIn('harmless-private-sentinel', json.dumps(result))
        raw = json.dumps(valid_fixture())
        for duplicate in [raw.replace('"authority":', '"authority":"current-and-explicit","authority":'),
                          raw.replace('"mode":', '"mode":"parallel-autonomous","mode":')]:
            with self.subTest(case='duplicate-key'):
                result, code = self.run_fixture(duplicate, raw=True)
                self.assertEqual(2, code)
                self.assertEqual({}, result['criteria'])
        for key in KEYS:
            for value in [None, '', [], {}, True, 1, 'harmless-private-sentinel']:
                with self.subTest(criterion=key, value=value):
                    fixture = valid_fixture()
                    fixture['criteria'][key] = value
                    fixture['expectedOutcome'] = 'Blocked'
                    result, code = self.run_fixture(fixture)
                    self.assertEqual(0, code)
                    self.assertEqual('Blocked', result['outcome'])
                    self.assertEqual('ProductFailure', result['failureClass'])
                    self.assertTrue(any(r['criterion'] == key for r in result['reasons']))
                    self.assertNotIn('harmless-private-sentinel', json.dumps(result))

    def test_modes(self):
        for mode in MODES:
            fixture = valid_fixture()
            fixture['mode'] = mode
            fixture['expectedOutcome'] = 'Blocked' if mode == 'blocked' else 'Eligible'
            for optional in [False, True]:
                if optional and mode == 'parallel-autonomous':
                    continue
                candidate = json.loads(json.dumps(fixture))
                if optional:
                    for flag in FLAGS:
                        if flag != 'currentAuthority':
                            del candidate[flag]
                with self.subTest(mode=mode, optionalAbsent=optional):
                    result, code = self.run_fixture(candidate)
                    self.assertEqual(0, code)
                    self.assertEqual(fixture['expectedOutcome'], result['outcome'])
                    self.assertIsNone(result['failureClass'])
                    self.assertEqual(mode, result['mode'])
            for flag, key in FLAGS.items():
                for value in ['false', 0, 1, None]:
                    with self.subTest(mode=mode, flag=flag, value=value):
                        candidate = json.loads(json.dumps(fixture))
                        candidate[flag] = value
                        candidate['expectedOutcome'] = 'Blocked'
                        result, code = self.run_fixture(candidate)
                        self.assertEqual(0, code)
                        self.assertEqual('ProductFailure', result['failureClass'])
                        self.assertTrue(any(r['criterion'] == key for r in result['reasons']))
                if mode == 'parallel-autonomous' or flag == 'currentAuthority':
                    with self.subTest(mode=mode, missing=flag):
                        candidate = json.loads(json.dumps(fixture))
                        del candidate[flag]
                        candidate['expectedOutcome'] = 'Blocked'
                        result, code = self.run_fixture(candidate)
                        self.assertEqual(0, code)
                        self.assertEqual('ProductFailure', result['failureClass'])
                with self.subTest(mode=mode, contradiction=flag):
                    candidate = json.loads(json.dumps(fixture))
                    candidate[flag] = not candidate[flag]
                    candidate['expectedOutcome'] = 'Blocked'
                    result, code = self.run_fixture(candidate)
                    self.assertEqual(0, code)
                    self.assertEqual('ProductFailure', result['failureClass'])
            for key, flag, shared in [('writeScope', 'disjointWrites', 'shared'),
                                      ('decisions', 'sharedOpenDecisions', 'shared-open-decision')]:
                with self.subTest(mode=mode, consistentShared=key):
                    candidate = json.loads(json.dumps(fixture))
                    candidate['criteria'][key] = shared
                    candidate[flag] = key == 'decisions'
                    candidate['expectedOutcome'] = 'Blocked' if mode in ['blocked', 'parallel-autonomous'] else 'Eligible'
                    result, code = self.run_fixture(candidate)
                    self.assertEqual(0, code)
                    self.assertEqual(candidate['expectedOutcome'], result['outcome'])
                    self.assertIsNone(result['failureClass'])
            with self.subTest(mode=mode, expectationIndependent=True):
                result, code = self.run_fixture(fixture)
                fixture['expectedOutcome'] = 'Eligible' if fixture['expectedOutcome'] == 'Blocked' else 'Blocked'
                mismatch, mismatch_code = self.run_fixture(fixture)
                self.assertEqual(0, code)
                self.assertEqual(2, mismatch_code)
                self.assertEqual(result['outcome'], mismatch['outcome'])
                self.assertEqual(result['criteria'], mismatch['criteria'])

    def test_failure_taxonomy(self):
        invalid_json = ['{', '{"expectedOutcome":"Blocked",', '\ufeff{bad}', 'NaN']
        for token in ['NaN', 'Infinity', '-Infinity']:
            fixture = valid_fixture()
            fixture['expectedOutcome'] = 'Blocked'
            invalid_json.append(json.dumps(fixture).replace('"planned"', token))
        for raw in invalid_json:
            with self.subTest(parser=raw):
                result, code = self.run_fixture(raw, raw=True)
                self.assertEqual(2, code)
                self.assertEqual('ProductFailure', result['failureClass'])
                self.assertEqual({}, result['criteria'])
                self.assertIsNone(result['mode'])
        for mode in ['harmless-private-sentinel', None, [], 3]:
            with self.subTest(mode=mode):
                fixture = valid_fixture()
                fixture.update(mode=mode, expectedOutcome='Blocked')
                result, code = self.run_fixture(fixture)
                self.assertEqual(2, code)
                self.assertIsNone(result['mode'])
                self.assertNotIn('harmless-private-sentinel', json.dumps(result))
        for path in ['absent.json', '../harmless-private-sentinel', '']:
            with self.subTest(path=path):
                result, code = self.run_fixture(valid_fixture(), fixture_path=path)
                self.assertEqual(2, code)
                self.assertEqual({}, result['criteria'])
        for error in ['ValueError', 'KeyError', 'TypeError']:
            with self.subTest(validatorException=error):
                fixture = valid_fixture()
                fixture['expectedOutcome'] = 'Blocked'
                result, code = self.run_fixture(fixture, legacy_error=error)
                self.assertEqual(2, code)
                self.assertEqual('ProductFailure', result['failureClass'])
        for error in ['RuntimeError', 'MemoryError']:
            with self.subTest(runtimeException=error):
                fixture = valid_fixture()
                fixture['expectedOutcome'] = 'Blocked'
                result, code = self.run_fixture(fixture, legacy_error=error)
                self.assertEqual(3, code)
                self.assertEqual('ProviderFailure', result['failureClass'])
        for child_exit in [0, 2, 42, 127]:
            with self.subTest(interpreterExit=child_exit):
                fixture = valid_fixture()
                fixture['expectedOutcome'] = 'Blocked'
                result, code = self.run_fixture(fixture, provider_exit=child_exit)
                self.assertEqual(3, code)
                self.assertEqual('ProviderFailure', result['failureClass'])
                self.assertFalse(result['authorityGranted'])
                self.assertEqual({'de', 'en'}, set(result['nextAction']))
        for child_exit in [0, 2]:
            with self.subTest(interpreterStdout=child_exit):
                result, code = self.run_fixture(valid_fixture(), provider_exit=child_exit, provider_stdout=True)
                self.assertEqual(3, code)
                self.assertEqual('ProviderFailure', result['failureClass'])
        for filename, outcome in [('valid-parallel', 'Eligible'), ('shared-write', 'Blocked'),
                                  ('shared-decision', 'Blocked')]:
            with self.subTest(original=filename):
                fixture = json.loads((REPO / ('specs/intake-review-fixtures/meta-lh-04/' + filename + '.json')).read_text())
                result, code = self.run_fixture(fixture)
                self.assertEqual(0, code)
                self.assertEqual(outcome, result['outcome'])
                self.assertIsNone(result['failureClass'])
                self.assertEqual('parallel-autonomous', result['mode'])
                fixture['expectedOutcome'] = 'Blocked' if outcome == 'Eligible' else 'Eligible'
                mismatch, code = self.run_fixture(fixture)
                self.assertEqual(2, code)
                self.assertEqual(outcome, mismatch['outcome'])
        fixture = valid_fixture()
        fixture['criteria'] = {k: '' for k in reversed(KEYS)}
        fixture['expectedOutcome'] = 'Blocked'
        result, code = self.run_fixture(fixture)
        self.assertEqual(0, code)
        self.assertEqual(KEYS, list(result['criteria']))
        self.assertEqual(KEYS, [r['criterion'] for r in result['reasons']])
        self.assertEqual({'de', 'en'}, set(result['nextAction']))
        self.assertTrue(all(r['code'] and r['de'] and r['en'] for r in result['reasons']))
        text, code = self.run_fixture(valid_fixture(), as_text=True)
        self.assertEqual(0, code)
        self.assertIn('parallel-autonomous', text)
        self.assertTrue(all(key in text for key in KEYS))
        self.assertIn('Keine Startfreigabe', text)
        self.assertEqual(1, text.count('Next action'))

    def test_surface(self):
        result, code = self.run_fixture(json.loads((REPO / FIXTURE).read_text()))
        self.assertEqual(0, code)
        self.assertEqual("Eligible", result["outcome"])
        self.assertFalse(result["authorityGranted"])

    def test_empty_integration(self):
        fixture = json.loads((REPO / FIXTURE).read_text())
        fixture["criteria"]["integration"] = ""
        fixture["expectedOutcome"] = "Blocked"
        result, code = self.run_fixture(fixture)
        self.assertEqual("Blocked", result["outcome"])
        self.assertEqual("ProductFailure", result["failureClass"])
        self.assertEqual(0, code)
        self.assertTrue(any(r["criterion"] == "integration" for r in result["reasons"]))
        self.assertEqual({"de", "en"}, set(result["nextAction"]))
        self.assertFalse(result["authorityGranted"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=REPO)
    parser.add_argument("--shell", choices=["bash", "pwsh"], default="bash")
    parser.add_argument("--case", choices=["surface", "empty-integration", "criteria-cardinality", "modes", "failure-taxonomy", "all"], default="all")
    args = parser.parse_args()
    REPO, SHELL = args.repo.resolve(), args.shell
    names = ["surface", "empty_integration", "criteria_cardinality", "modes", "failure_taxonomy"] if args.case == "all" else [args.case.replace("-", "_")]
    suite = unittest.TestSuite(EligibilityTests("test_" + name) for name in names)
    raise SystemExit(0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1)
