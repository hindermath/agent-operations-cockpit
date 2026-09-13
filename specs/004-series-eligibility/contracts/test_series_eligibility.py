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


# Nur Testprozesse beobachten; Sentineldateien enthalten keine echten Secrets.
# Observe test processes only; sentinel files contain no actual secrets.
PROBE = r'''
import json, os, runpy, sys
from pathlib import Path
from unittest.mock import patch
sys.dont_write_bytecode = True
request = json.loads(Path(sys.argv[1]).read_text())
repo = Path(request['repo']).resolve()
core = runpy.run_path(request['core'])
external = Path(request['external']).resolve()
reads, metadata = [], []
observing = False
def outside(path, follow=True):
    global observing
    if observing:
        return False
    observing = True
    try:
        value = os.path.realpath(os.fspath(path)) if follow else os.path.abspath(os.fspath(path))
        return Path(value).is_relative_to(external)
    except (TypeError, ValueError):
        return False
    finally:
        observing = False
def audit(event, args):
    if event == 'open' and outside(args[0]):
        reads.append('external-open')
sys.addaudithook(audit)
original_stat, original_lstat = os.stat, os.lstat
def observed_stat(path, *args, **kwargs):
    if outside(path, kwargs.get('follow_symlinks', True)):
        metadata.append('external-stat')
    return original_stat(path, *args, **kwargs)
def observed_lstat(path, *args, **kwargs):
    if outside(path, False):
        metadata.append('external-lstat')
    return original_lstat(path, *args, **kwargs)
engine = None
try:
    with patch.object(os, 'stat', observed_stat), patch.object(os, 'lstat', observed_lstat):
        if request['operation'] == 'fixture':
            result, code = core['assess'](repo, request['path'])
        else:
            if request['binding'] == 'legacy':
                import types
                engine = types.SimpleNamespace(**runpy.run_path(request['engine']))
                # Functions retain their original globals in this baseline module.
                root, path = repo, repo / request['path']
            else:
                engine, root = core['load_series_engine'](repo)
                path = root / request['path']
            op = request['operation']
            if op == 'series':
                if request['binding'] == 'feature':
                    result, code = core['assess_series'](repo, request['path'])
                    summary = result.get('summary', {})
                else:
                    _, summary = engine.validate_manifest(path, root)
            elif op == 'receipt':
                summary = engine.validate_receipt(path, root)
            elif op == 'json':
                engine.load_json(path)
                summary = {}
            elif op == 'isolation':
                other, _ = core['load_series_engine'](repo)
                assert engine is not other and engine.load_json is not other.load_json
                assert engine.normalized_bytes is not other.normalized_bytes
                summary = {}
            if op != 'series' or request['binding'] != 'feature':
                result, code = core['diagnostic'](None), 0
                result['outcome'], result['summary'] = 'Eligible', summary
except Exception as error:
    # Known engine errors keep only their stable class, never their raw message.
    result, code = core['failed_input'](), 2
    result['reasons'][0]['code'] = getattr(error, 'code', 'EL_INPUT')
print(json.dumps({'result': result, 'externalReads': reads, 'externalMetadata': metadata,
                  'binding': request['binding']}, ensure_ascii=False))
sys.exit(code)
'''

ENGINE = '.specify/presets/intake-sequencing-governance/scripts/validate-intake-series.py'
BINDING = 'feature'


def series_fixture(repo):
    targets = []
    for index, name in enumerate(['a', 'b', 'c', 'd']):
        path = 'intakes/' + name + '.md'
        (repo / path).parent.mkdir(exist_ok=True)
        content = ('# ' + name + '\n').encode()
        (repo / path).write_bytes(content)
        targets.append(dict(path=path, role='Primary' if index == 0 else 'OrderedMember',
                            normalizedSha256=hashlib.sha256(content).hexdigest(),
                            status='Completed' if index < 3 else 'Pending'))
    paths = [t['path'] for t in targets]
    return dict(schemaVersion='1.0', documentType='IntakeSeriesManifest',
                seriesId='11111111-1111-4111-8111-111111111111', title='Test / Test',
                policy='fixture', status='Ready', orderedTargets=targets, roots=[paths[0]],
                dependencies=[dict(**{'from': paths[i], 'to': paths[i+1]},
                                   kind='HardCompletionGate', binding=True) for i in range(3)],
                evidencePaths=[])


class SeriesTests(unittest.TestCase):
    def probe(self, mutation=None, *, operation='series', path='manifest.json', label='valid'):
        with tempfile.TemporaryDirectory(prefix='aoc series ') as temporary:
            base = Path(temporary)
            repo, external = base / 'repo', base / 'external'
            repo.mkdir(); external.mkdir()
            manifest = series_fixture(repo)
            (repo / CONTRACT).parent.mkdir(parents=True)
            shutil.copyfile(REPO / CONTRACT, repo / CONTRACT)
            (repo / 'fixture.json').write_text(json.dumps(valid_fixture()))
            (external / 'target.md').write_text('# a\n')
            (external / 'sentinel.json').write_text('{"harmless-private-sentinel":true}')
            shutil.copyfile(REPO / CONTRACT, external / 'contract.json')
            shutil.copyfile(repo / 'fixture.json', external / 'fixture.json')
            if mutation:
                mutation(repo, external, manifest)
            if not (repo / 'manifest.json').exists():
                (repo / 'manifest.json').write_text(json.dumps(manifest))
            probe = base / 'probe.py'
            probe.write_text(PROBE)
            request = base / 'request.json'
            request.write_text(json.dumps(dict(repo=str(repo), external=str(external),
                core=str(REPO / CONTRACTS / 'validate_series_eligibility.py'),
                engine=str(REPO / ENGINE), operation=operation, path=path, binding=BINDING)))
            if SHELL == 'bash':
                command = [os.environ.get('AOC_GIT_BASH_EXE', 'bash'), '-c',
                           'exec python3 -B "$1" "$2"', 'probe', str(probe), str(request)]
            else:
                launcher = base / 'probe.ps1'
                launcher.write_text('param([string]$Probe,[string]$Request)\n'
                                    '& python3 -B $Probe $Request\nexit $LASTEXITCODE\n')
                command = ['pwsh', '-NoProfile', '-File', str(launcher), str(probe), str(request)]
            before = snapshot(base)
            child = subprocess.run(command, cwd=REPO, capture_output=True, text=True)
            record = json.loads(child.stdout)
            print(json.dumps(dict(shell=SHELL, test=self.id(), case=label, childExit=child.returncode,
                                  **record, stderr=child.stderr), ensure_ascii=False), flush=True)
            self.assertEqual(before, snapshot(base), 'query wrote files or bytecode')
            self.assertNotIn('harmless-private-sentinel', child.stdout + child.stderr)
            self.assertNotIn('Traceback', child.stdout + child.stderr)
            return record, child.returncode

    def assert_blocked(self, record, code, expected=None):
        self.assertEqual([], record['externalReads'], 'external content was opened')
        self.assertEqual([], record['externalMetadata'], 'external metadata was queried')
        self.assertEqual(2, code)
        result = record['result']
        self.assertEqual('Blocked', result['outcome'])
        self.assertEqual('ProductFailure', result['failureClass'])
        self.assertFalse(result['authorityGranted'])
        self.assertEqual({'de', 'en'}, set(result['nextAction']))
        if expected:
            self.assertIn(expected, [r['code'] for r in result['reasons']])

    def test_transitive_paths(self):
        # Establish a runnable semantic baseline before any negative assertion.
        record, code = self.probe()
        self.assertEqual(0, code)
        forms = ['/absolute.json', 'C:/outside.json', 'C:\\outside.json',
                 '\\\\host\\share\\outside.json', '//host/share/outside.json',
                 'C:outside.json', '../external/sentinel.json', '..\\external\\sentinel.json',
                 'bad\x00.json', '.', 'intakes', 'missing.json']
        for operation in ['fixture', 'series', 'json']:
            for value in forms:
                with self.subTest(operation=operation, path=value):
                    self.assert_blocked(*self.probe(operation=operation, path=value,
                                                   label=operation + '-unsafe-path'))
        for location in ['target', 'archive']:
            for value in forms:
                def mutate(repo, external, manifest, value=value, location=location):
                    if location == 'target':
                        manifest['orderedTargets'][0]['path'] = value
                    else:
                        self.lifecycle(repo, manifest, value)
                        if value == 'missing.json':
                            (repo / 'intakes/a.md').unlink()
                with self.subTest(location=location, path=value):
                    self.assert_blocked(*self.probe(mutate, label=location + '-unsafe-path'))
        for location in ['fixture', 'contract', 'target', 'archive', 'lifecycle', 'specs-directory',
                         'receipt', 'review', 'evidence']:
            def link(repo, external, manifest, location=location):
                if location == 'fixture':
                    target, source = repo / 'fixture.json', external / 'fixture.json'
                elif location == 'contract':
                    target, source = repo / CONTRACT, external / 'contract.json'
                elif location == 'target':
                    target, source = repo / 'intakes/a.md', external / 'target.md'
                elif location == 'archive':
                    self.lifecycle(repo, manifest, 'archive.md')
                    (repo / 'intakes/a.md').unlink()
                    target, source = repo / 'archive.md', external / 'target.md'
                elif location in ['lifecycle', 'specs-directory']:
                    source = external / 'intake-lifecycle.json'
                    source.write_text('{"schemaVersion":"1.1","records":[]}')
                    if location == 'specs-directory':
                        (repo / 'specs').symlink_to(external, target_is_directory=True)
                        return
                    target = repo / 'specs/history/intake-lifecycle.json'
                    target.parent.mkdir(parents=True)
                else:
                    target, source = repo / (location + '.json'), external / 'sentinel.json'
                if target.exists():
                    target.unlink()
                target.symlink_to(source)
            operation = 'fixture' if location in ['fixture', 'contract'] else 'series'
            path = 'fixture.json' if operation == 'fixture' else 'manifest.json'
            if location in ['receipt', 'review', 'evidence']:
                operation, path = 'json', location + '.json'
            with self.subTest(symlink=location):
                # Failure to create native links is a test failure/Open, never a passing skip.
                self.assert_blocked(*self.probe(link, operation=operation, path=path,
                                               label=location + '-symlink'))
        for location in ['manifest', 'lifecycle', 'receipt', 'review', 'evidence', 'contract']:
            def duplicate(repo, external, manifest, location=location):
                if location == 'manifest':
                    raw = json.dumps(manifest).replace('"role":', '"role":"Primary","role":', 1)
                    target = repo / 'manifest.json'
                elif location == 'contract':
                    target = repo / CONTRACT
                    raw = target.read_text().replace('"criteria":', '"criteria":[],"criteria":', 1)
                else:
                    target = repo / ('specs/history/intake-lifecycle.json' if location == 'lifecycle'
                                     else location + '.json')
                    target.parent.mkdir(parents=True, exist_ok=True)
                    raw = '{"schemaVersion":"1.1","records":[],"nested":{"x":1,"x":2}}'
                target.write_text(raw)
            operation = 'fixture' if location == 'contract' else 'series'
            path = 'fixture.json' if operation == 'fixture' else 'manifest.json'
            if location in ['receipt', 'review', 'evidence']:
                operation, path = 'json', location + '.json'
            with self.subTest(duplicate=location):
                self.assert_blocked(*self.probe(duplicate, operation=operation, path=path,
                                               label=location + '-duplicate'))

    @staticmethod
    def lifecycle(repo, manifest, archived='archive.md'):
        target = manifest['orderedTargets'][0]
        path = repo / 'specs/history/intake-lifecycle.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(dict(schemaVersion='1.1', records=[dict(
            originalPath=target['path'], archivedPath=archived,
            originalNormalizedSha256=target['normalizedSha256'])])))

    def test_series_negatives(self):
        for label, mutation, expected in [
            ('cycle', lambda r, e, m: m['dependencies'].append(dict(
                **{'from': 'intakes/d.md', 'to': 'intakes/a.md'}, kind='FinalAuditInput', binding=True)), 'ISG007'),
            ('hash', lambda r, e, m: m['orderedTargets'][0].update(normalizedSha256='0'*64), 'ISG004'),
            ('missing-root-no-cycle', lambda r, e, m: m.update(roots=[]), 'ISG008'),
            ('multiple-eligible', lambda r, e, m: [t.update(status='Eligible') for t in m['orderedTargets'][:2]], 'ISG009'),
            ('order', lambda r, e, m: m['orderedTargets'].reverse(), 'ISG007'),
            ('unknown-edge', lambda r, e, m: m['dependencies'][0].update(kind='unknown'), 'ISG006'),
            ('binding', lambda r, e, m: m['dependencies'][0].update(binding=False), 'ISG006'),
            ('unknown-target', lambda r, e, m: m['dependencies'][0].update(to='missing'), 'ISG005'),
            ('self-edge', lambda r, e, m: m['dependencies'][0].update(to='intakes/a.md'), 'ISG005'),
            ('duplicate-edge', lambda r, e, m: m['dependencies'].append(m['dependencies'][0].copy()), 'ISG006'),
            ('duplicate-target', lambda r, e, m: m['orderedTargets'].append(m['orderedTargets'][0].copy()), 'ISG003'),
            ('unknown-lifecycle', lambda r, e, m: m['orderedTargets'][0].update(status='unknown'), 'ISG009'),
            ('archive-both-physical', lambda r, e, m: (self.lifecycle(r, m), (r/'archive.md').write_text('# a\n')), 'ISG004'),
            ('archive-neither-physical', lambda r, e, m: (self.lifecycle(r, m), (r/'intakes/a.md').unlink()), 'ISG004'),
            ('archive-hash-drift', lambda r, e, m: (self.lifecycle(r, m), (r/'intakes/a.md').unlink(), (r/'archive.md').write_text('drift')), 'ISG004'),
            ('invalid-lifecycle-schema', lambda r, e, m: (self.lifecycle(r, m), (r/'specs/history/intake-lifecycle.json').write_text('{}')), 'ISG004'),
            ('ambiguous-lifecycle', lambda r, e, m: (self.lifecycle(r, m), (r/'specs/other').mkdir(), shutil.copyfile(r/'specs/history/intake-lifecycle.json', r/'specs/other/intake-lifecycle.json')), 'ISG004'),
        ]:
            with self.subTest(case=label):
                self.assert_blocked(*self.probe(mutation, label=label), expected=expected)
        for label in ['valid', 'bom-crlf', 'historical-archive', 'historical-original']:
            def valid(repo, external, manifest, label=label):
                if label == 'bom-crlf':
                    for target in manifest['orderedTargets']:
                        path = repo / target['path']
                        path.write_bytes(b'\xef\xbb\xbf' + path.read_bytes().replace(b'\n', b'\r\n'))
                    (repo/'manifest.json').write_bytes(b'\xef\xbb\xbf' + json.dumps(manifest, indent=2).replace('\n','\r\n').encode())
                elif label.startswith('historical'):
                    self.lifecycle(repo, manifest)
                    if label == 'historical-archive':
                        (repo/'intakes/a.md').rename(repo/'archive.md')
            with self.subTest(case=label):
                record, code = self.probe(valid, label=label)
                self.assertEqual(0, code)
                self.assertEqual(['intakes/d.md'], record['result']['summary']['eligible'])
                self.assertEqual([], record['externalReads'])
        # The real programme's first three binding predecessors are immutable facts.
        canonical = json.loads((REPO/'specs/intake-series/aoc-phase-2/manifest.json').read_text())
        first = canonical['orderedTargets'][:4]
        for number, target in enumerate(first[:3], 1):
            self.assertIn('META-LH-0' + str(number), target['path'])
            self.assertEqual('Completed', target['status'])
            self.assertTrue(any(edge['from'] == target['path'] and edge['to'] == first[number]['path']
                                and edge['binding'] is True for edge in canonical['dependencies']))
        for predecessor in range(3):
            def incomplete(repo, external, manifest, predecessor=predecessor):
                paths = [t['path'] for t in manifest['orderedTargets']]
                manifest['dependencies'] = [dict(**{'from': p, 'to': paths[3]},
                    kind='HardCompletionGate', binding=True) for p in paths[:3]]
                manifest['roots'] = paths[:3]
                manifest['orderedTargets'][predecessor]['status'] = 'Pending'
            record, code = self.probe(incomplete, label='required-predecessor-' + str(predecessor+1))
            self.assertEqual(0, code)
            self.assertNotIn('intakes/d.md', record['result']['summary']['eligible'])
            self.assertEqual(['intakes/' + 'abc'[predecessor] + '.md'],
                             record['result']['summary']['blockers']['intakes/d.md'])

    def test_transitive_readers(self):
        def receipt(repo, external, manifest):
            raw = json.dumps(manifest).encode()
            (repo/'manifest.json').write_bytes(raw)
            (repo/'prior-receipt.json').write_text('{}')
            (repo/'prior-manifest.json').write_text('{}')
            (repo/'tombstone.json').write_text('{}')
            digest = hashlib.sha256(b'{}').hexdigest()
            value = dict(schemaVersion='1.0', documentType='IntakeSeriesReceipt',
                receiptId='22222222-2222-4222-8222-222222222222', seriesId=manifest['seriesId'],
                operation=dict(operationId='33333333-3333-4333-8333-333333333333', type='Delete',
                               authorityEvidence='Fixture only'), status='Deleted',
                manifest=dict(path='manifest.json', normalizedSha256=hashlib.sha256(raw).hexdigest()),
                supersedes=dict(receiptPath='prior-receipt.json', receiptNormalizedSha256=digest,
                                manifestArchivePath='prior-manifest.json', manifestArchiveSha256=digest),
                tombstone=dict(path='tombstone.json', normalizedSha256=digest))
            (repo/'receipt.json').write_text(json.dumps(value))
        record, code = self.probe(receipt, operation='receipt', path='receipt.json', label='valid-receipt-chain')
        self.assertEqual(0, code)
        for group, field in [('manifest', 'path'), ('supersedes', 'receiptPath'),
                             ('supersedes', 'manifestArchivePath'), ('tombstone', 'path')]:
            for form in ['../external/sentinel.json', 'C:relative.json', '\\\\host\\share\\file',
                         '/absolute.json', 'bad\x00.json', 'intakes', 'missing.json', 'symlink']:
                def mutate(repo, external, manifest, group=group, field=field, form=form):
                    receipt(repo, external, manifest)
                    value = json.loads((repo/'receipt.json').read_text())
                    if form == 'symlink':
                        target = repo / value[group][field]
                        target.unlink()
                        target.symlink_to(external/'sentinel.json')
                    else:
                        value[group][field] = form
                        (repo/'receipt.json').write_text(json.dumps(value))
                with self.subTest(group=group, field=field, form=form):
                    self.assert_blocked(*self.probe(mutate, operation='receipt', path='receipt.json',
                                                   label=group + '-' + field + '-' + form.replace('\x00','NUL')))
        if BINDING == 'feature':
            record, code = self.probe(operation='isolation', label='separate-module-instances')
            self.assertEqual(0, code)



QUERY_AUDIT = r"""
import json, os, runpy, sys
sys.dont_write_bytecode = True
core, repo, action = sys.argv[1:]
violations = []
def audit(event, args):
    write = event == 'open' and ((isinstance(args[1], str) and any(c in args[1] for c in 'wax+'))
        or (isinstance(args[2], int) and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_CREAT)))
    if write or event in ('subprocess.Popen', 'os.system', 'os.exec', 'os.posix_spawn',
                          'os.remove', 'os.rename', 'os.mkdir', 'os.rmdir', 'os.link', 'os.symlink'):
        violations.append(event)
        raise RuntimeError('query side effect')
sys.addaudithook(audit)
module = runpy.run_path(core)
result, code = module['assess_series'](repo, 'manifest.json', action)
print(json.dumps({'result': result, 'code': code, 'violations': violations}))
"""


class QueryTests(unittest.TestCase):
    def query(self, repo, action, *, text=False, seed=1, extra=()):
        surface = REPO / CONTRACTS
        if SHELL == 'bash':
            command = [os.environ.get('AOC_GIT_BASH_EXE', 'bash'), str(surface/'validate-series-eligibility.sh'),
                       '--repo', str(repo), '--series', 'manifest.json', '--action', action]
            if not text:
                command += ['--json']
        else:
            command = ['pwsh', '-NoProfile', '-File', str(surface/'validate-series-eligibility.ps1'),
                       '-Repo', str(repo), '-Series', 'manifest.json', '-Action', action]
            if not text:
                command += ['-Json']
        before = snapshot(repo)
        protected = [REPO/'specs/004-series-eligibility/autonomous-run-state.json',
                     REPO/'specs/intake-series/aoc-phase-2/manifest.json',
                     REPO/'specs/intake-series-receipts/aoc-phase-2.json',
                     *sorted((REPO/'specs').glob('*/intake-lifecycle.json'))]
        protected_before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
        git_before = subprocess.check_output(['git', '--no-optional-locks', 'status', '--porcelain=v1',
                                             '--untracked-files=all'], cwd=REPO)
        child = subprocess.run(command + list(extra), capture_output=True, text=True,
            env={**os.environ, 'PYTHONHASHSEED': str(seed), 'PYTHONDONTWRITEBYTECODE': '1'})
        self.assertEqual(before, snapshot(repo), 'query changed bytes or created files')
        self.assertEqual(protected_before, {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected})
        self.assertEqual(git_before, subprocess.check_output(['git', '--no-optional-locks', 'status',
                         '--porcelain=v1', '--untracked-files=all'], cwd=REPO))
        self.assertNotIn('harmless-private-sentinel', child.stdout + child.stderr)
        self.assertNotIn('Traceback', child.stdout + child.stderr)
        print(json.dumps(dict(test=self.id(), action=action, shell=SHELL, seed=seed, text=text,
                             childExit=child.returncode, noWrite=True, gitStatusUnchanged=True)), flush=True)
        return child

    def test_status_next(self):
        for state in ['Completed', 'Ready', 'Active', 'NeedsClarification']:
            for scenario in ['zero', 'one', 'multiple', 'preferred', 'two-blockers']:
                with self.subTest(state=state, scenario=scenario), tempfile.TemporaryDirectory(prefix='aoc query ') as temp:
                    repo = Path(temp)
                    manifest = series_fixture(repo)
                    paths = [t['path'] for t in manifest['orderedTargets']]
                    manifest['status'] = state
                    if scenario == 'zero':
                        for target in manifest['orderedTargets']:
                            target['status'] = 'Completed'
                        expected, preferred = [], None
                    elif scenario == 'one':
                        expected, preferred = [paths[3]], None
                    elif scenario in ['multiple', 'preferred']:
                        manifest['dependencies'], manifest['roots'] = [], paths
                        for target in manifest['orderedTargets']:
                            target['status'] = 'Pending'
                        if scenario == 'preferred':
                            manifest['orderedTargets'][2]['status'] = 'Eligible'
                        expected, preferred = paths, paths[2] if scenario == 'preferred' else None
                    else:
                        manifest['roots'] = paths[:3]
                        manifest['dependencies'] = [dict(**{'from': p, 'to': paths[3]},
                            kind='HardCompletionGate', binding=True) for p in paths[:3]]
                        for target in manifest['orderedTargets'][:2]:
                            target['status'] = 'Pending'
                        expected, preferred = paths[:2], None
                    (repo/'manifest.json').write_text(json.dumps(manifest))
                    # Unbound review and run facts must never become current authority.
                    (repo/'review.json').write_text('{"outcome":"Ready"}')
                    (repo/'autonomous-run-state.json').write_text('{"deliveryMode":"MergeAndSync"}')
                    baseline = {}
                    for action in ['status', 'next']:
                        for seed in ([1, 7, 42] if scenario == 'two-blockers' else [1]):
                            child = self.query(repo, action, seed=seed)
                            self.assertEqual(0, child.returncode, child.stderr)
                            data = json.loads(child.stdout)
                            self.assertEqual(expected, data['eligibleCandidates'])
                            self.assertEqual(preferred, data['preferredCandidate'])
                            self.assertEqual(state, data['declaredLifecycle']['series'])
                            self.assertEqual({p: t['status'] for p, t in zip(paths, manifest['orderedTargets'])},
                                             data['declaredLifecycle']['targets'])
                            self.assertEqual('NotAssessed', data['reviewState'])
                            self.assertEqual('NotAssessed', data['deliveryMode'])
                            self.assertEqual('NotGrantedByQuery', data['currentStartAuthority'])
                            self.assertFalse(data['authorityGranted'])
                            self.assertIsNone(data['failureClass'])
                            self.assertEqual({'de', 'en'}, set(data['nextAction']))
                            if scenario == 'two-blockers':
                                self.assertEqual(paths[:2], data['blockers'][paths[3]])
                                self.assertEqual(paths[:2], data['summary']['blockers'][paths[3]])
                            display = self.query(repo, action, text=True, seed=seed)
                            self.assertEqual(0, display.returncode)
                            self.assertEqual(1, display.stdout.count('Nächste Aktion / Next action:'))
                            self.assertIn('NotGrantedByQuery', display.stdout)
                            self.assertIn('NotAssessed', display.stdout)
                            self.assertIn(state, display.stdout)
                            self.assertIn('Kandidaten / Candidates: ' + json.dumps(expected, ensure_ascii=False), display.stdout)
                            self.assertIn('Blocker / Blockers: ' + json.dumps(data['blockers'], ensure_ascii=False), display.stdout)
                            if seed == 1:
                                baseline[action] = (child.stdout, display.stdout)
                            else:
                                self.assertEqual(baseline[action], (child.stdout, display.stdout))
                    self.assertEqual(baseline['status'], baseline['next'])

    def test_query_idle(self):
        with tempfile.TemporaryDirectory(prefix='aoc idle ') as temp:
            repo = Path(temp)
            manifest = series_fixture(repo)
            manifest.update(status='Idle', orderedTargets=[], roots=[], dependencies=[])
            (repo/'manifest.json').write_text(json.dumps(manifest))
            for action in ['status', 'next']:
                child = self.query(repo, action)
                self.assertEqual(0, child.returncode)
                data = json.loads(child.stdout)
                self.assertEqual([], data['eligibleCandidates'])
                self.assertEqual('Idle', data['declaredLifecycle']['series'])
                self.assertEqual({}, data['declaredLifecycle']['targets'])
                self.assertEqual('NotAssessed', data['reviewState'])
                self.assertEqual('NotGrantedByQuery', data['currentStartAuthority'])
                self.assertEqual({'de', 'en'}, set(data['nextAction']))

    def test_query_no_side_effects(self):
        with tempfile.TemporaryDirectory(prefix='aoc query proof ') as temp:
            repo = Path(temp)
            manifest = series_fixture(repo)
            SeriesTests.lifecycle(repo, manifest)
            (repo/'manifest.json').write_text(json.dumps(manifest))
            (repo/'receipt.json').write_text('{"historical":true}')
            (repo/'autonomous-run-state.json').write_text('{"status":"Active"}')
            for invalid in [False, True]:
                if invalid:
                    (repo/'intakes/a.md').write_text('hash drift')
                for action in ['status', 'next']:
                    before = snapshot(repo)
                    child = self.query(repo, action)
                    self.assertEqual(2 if invalid else 0, child.returncode)
                    proof = subprocess.run([sys.executable, '-B', '-c', QUERY_AUDIT,
                        str(REPO/CONTRACTS/'validate_series_eligibility.py'), str(repo), action],
                        capture_output=True, text=True)
                    self.assertEqual(0, proof.returncode, proof.stderr)
                    record = json.loads(proof.stdout)
                    self.assertEqual([], record['violations'])
                    self.assertEqual(2 if invalid else 0, record['code'])
                    self.assertEqual(before, snapshot(repo))
                    print(json.dumps(dict(test=self.id(), action=action, invalid=invalid,
                        auditedCoreProcesses=0, auditedWrites=0, files=before)), flush=True)

    def test_query_receipt_provenance(self):
        with tempfile.TemporaryDirectory(prefix='aoc receipt query ') as temp:
            repo = Path(temp)
            manifest = series_fixture(repo)
            manifest['evidencePaths'] = ['receipt.json']
            raw = json.dumps(manifest)
            (repo/'manifest.json').write_text(raw)
            receipt = dict(schemaVersion='1.0', documentType='IntakeSeriesReceipt',
                receiptId='22222222-2222-4222-8222-222222222222', seriesId=manifest['seriesId'],
                operation=dict(operationId='33333333-3333-4333-8333-333333333333', type='Create',
                    authorityEvidence='harmless-private-sentinel'), status='Ready',
                manifest=dict(path='manifest.json', normalizedSha256=hashlib.sha256(raw.encode()).hexdigest()),
                supersedes={})
            (repo/'receipt.json').write_text(json.dumps(receipt))
            for action in ['status', 'next']:
                child = self.query(repo, action)
                self.assertEqual(0, child.returncode)
                data = json.loads(child.stdout)
                self.assertEqual('NotAssessed', data['reviewState'])
                self.assertEqual('NotGrantedByQuery', data['currentStartAuthority'])
                self.assertEqual([dict(path='receipt.json', receiptId=receipt['receiptId'],
                    operation='Create', authorityContext='HistoricalOnly')], data['historicalReceiptProvenance'])
            receipt['manifest']['normalizedSha256'] = '0'*64
            (repo/'receipt.json').write_text(json.dumps(receipt))
            self.assertEqual(2, self.query(repo, 'status').returncode)


    def test_query_shell_surface(self):
        surface = REPO/CONTRACTS
        if SHELL == 'bash':
            for flag in ['--help', '-h']:
                child = subprocess.run([os.environ.get('AOC_GIT_BASH_EXE', 'bash'),
                    str(surface/'validate-series-eligibility.sh'), flag], capture_output=True, text=True)
                self.assertEqual(0, child.returncode)
                for token in MODES + ['--series', '--action', 'ProductFailure', 'ProviderFailure']:
                    self.assertIn(token, child.stdout)
        else:
            script = r'''
param($Surface, $FixtureRepo)
$ErrorActionPreference = 'Stop'
$global:LASTEXITCODE = 71
function python3 { throw 'Dot-sourcing/help attempted execution' }
$loaded = @(. $Surface)
if ($loaded.Count -ne 0 -or $LASTEXITCODE -ne 71) { throw 'Dot-sourcing executed or emitted output' }
$helpText = Get-Help Test-AocSeriesEligibility -Full | Out-String
foreach ($token in @('manual-assisted','single-autonomous','serial-autonomous','parallel-autonomous',
    'research-only','blocked','Series','Action','Help','ProductFailure','ProviderFailure')) {
    if (-not $helpText.Contains($token)) { throw "Help missing $token" }
}
Test-AocSeriesEligibility -Help | Out-Null
Remove-Item Function:python3
$functionResult = Test-AocSeriesEligibility -Repo $FixtureRepo -Series 'manifest.json' -Action next -Json
$code = $LASTEXITCODE
if ($code -ne 0) { throw "Advanced function failed: $code / $functionResult" }
$cliResult = & $Surface -Repo $FixtureRepo -Series 'manifest.json' -Action next -Json
$code = $LASTEXITCODE
if ($code -ne 0 -or $functionResult -ne $cliResult) { throw 'Function and CLI differ' }
'PASS: no execution on dot-source/help, complete help, function/CLI parity'
'''
            with tempfile.TemporaryDirectory(prefix='aoc function ') as temp:
                repo = Path(temp)
                (repo/'manifest.json').write_text(json.dumps(series_fixture(repo)))
                before = snapshot(repo)
                RunnerTests('test_runner_cardinality').pwsh_probe(script,
                    [str(surface/'validate-series-eligibility.ps1'), str(repo)])
                self.assertEqual(before, snapshot(repo))
                help_child = subprocess.run(['pwsh','-NoProfile','-File',str(surface/'validate-series-eligibility.ps1'),
                    '-Help'], capture_output=True, text=True)
                self.assertEqual(0, help_child.returncode)
                self.assertIn('Series', help_child.stdout)
        with tempfile.TemporaryDirectory(prefix='aoc exclusive ') as temp:
            repo = Path(temp)
            (repo/'manifest.json').write_text(json.dumps(series_fixture(repo)))
            fixture_option = '--fixture' if SHELL == 'bash' else '-Fixture'
            child = self.query(repo, 'status', extra=[fixture_option, 'unused.json'])
            self.assertEqual(2, child.returncode)
            self.assertEqual('ProductFailure', json.loads(child.stdout)['failureClass'])
            child = self.query(repo, 'unsafe-action')
            self.assertEqual(2, child.returncode)
            self.assertNotIn('unsafe-action', child.stdout + child.stderr)


class RunnerTests(unittest.TestCase):
    @staticmethod
    def workflow_block(start, end):
        source = (REPO/'.github/workflows/powershell-analysis.yml').read_text()
        body = source.split(start, 1)[1].split(end, 1)[0]
        return '\n'.join(line[10:] if line.startswith(' '*10) else line for line in body.splitlines())

    def pwsh_probe(self, script, arguments=(), expected=0):
        with tempfile.TemporaryDirectory(prefix='aoc runner spaces ') as temp:
            probe = Path(temp)/'runner probe.ps1'
            probe.write_text(script)
            # Both launch surfaces must preserve script paths containing spaces.
            if SHELL == 'bash':
                command = [os.environ.get('AOC_GIT_BASH_EXE', 'bash'), '-c',
                           'exec pwsh -NoProfile -File "$@"', 'runner', str(probe), *arguments]
            else:
                command = ['pwsh', '-NoProfile', '-File', str(probe), *arguments]
            child = subprocess.run(command, capture_output=True, text=True)
            print(json.dumps(dict(test=self.id(), shell=SHELL, childExit=child.returncode,
                                  stdout=child.stdout, stderr=child.stderr)), flush=True)
            self.assertEqual(expected, child.returncode, child.stdout + child.stderr)
            return child

    def test_runner_cardinality(self):
        legacy = self.workflow_block('        run: |\n          if ($IsWindows)',
            '      - name: Test Feature 003 authoring contract matrix')
        legacy = 'if ($IsWindows)' + legacy
        legacy = legacy.replace('$IsWindows', '$FixtureWindows')
        legacy = legacy.split('"AOC_GIT_BASH_EXE=')[0]
        prelude = '''
$ErrorActionPreference = 'Stop'
$FixtureWindows = $false
$actual = @(Microsoft.PowerShell.Core\\Get-Command bash -CommandType Application)[0]
function Get-Command { param($Name, $CommandType, $ErrorAction)
    for ($i = 0; $i -lt $script:Count; $i++) { $script:actual }
}
'''
        for count in [0, 1, 3]:
            self.pwsh_probe(prelude + '\n$Count = ' + str(count) + '\n' + legacy,
                            expected=1 if count == 0 else 0)
        source = (REPO/'.github/workflows/powershell-analysis.yml').read_text()
        self.assertIn('# FEATURE004-CAPABILITY-BEGIN', source, 'Feature-004 capability boundary absent')
        capability = self.workflow_block('# FEATURE004-CAPABILITY-BEGIN', '# FEATURE004-CAPABILITY-END')
        # Isolate version/cardinality decisions using real contained files, never label mocks native evidence.
        with tempfile.TemporaryDirectory(prefix='aoc candidates ') as temp:
            root = Path(temp)
            for relative in ['old/bash', 'new/bash', 'Git/bin/bash.exe', 'Windows/System32/bash.exe']:
                path = root/relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('fixture')
            config = root/'paths.json'
            config.write_text(json.dumps(dict(old=str(root/'old/bash'), new=str(root/'new/bash'),
                git=str(root/'Git/bin/bash.exe'), wsl=str(root/'Windows/System32/bash.exe'))))
            script = '''param($Config)
$ErrorActionPreference = 'Stop'
''' + capability + '''
$p = Get-Content -Raw -LiteralPath $Config | ConvertFrom-Json
function Get-AocFeature004BashMajor { param($Executable)
    if ($Executable -eq $p.old) { return 3 }; return 5
}
function Assert-Rejected { param([scriptblock]$Probe)
    $rejected = $false
    try { & $Probe | Out-Null } catch { $rejected = $true }
    if (-not $rejected) { throw 'Required rejection absent' }
}
Assert-Rejected { Resolve-AocFeature004Bash -Candidates @() }
Assert-Rejected { Resolve-AocFeature004Bash -Candidates @($p.old) }
Assert-Rejected { Resolve-AocFeature004Bash -Candidates @('missing') }
foreach ($candidates in @(@($p.new), @($p.old, $p.new), @($p.new, $p.new))) {
    $chosen = Resolve-AocFeature004Bash -Candidates $candidates
    if ($chosen -ne $p.new) { throw 'Bash 5 selection differs' }
}
Assert-Rejected { Resolve-AocFeature004Bash -Candidates @($p.wsl) -WindowsHost -GitBashPath $p.wsl }
Assert-Rejected { Resolve-AocFeature004Bash -Candidates @($p.new) -WindowsHost -GitBashPath $p.git }
$chosen = Resolve-AocFeature004Bash -Candidates @($p.git) -WindowsHost -GitBashPath $p.git
if ($chosen -ne $p.git) { throw 'Git Bash identity differs' }
'PASS: zero/one/multiple references, Bash 3/5, Git Bash/WSL policy and spaced paths (isolated fixtures)'
'''
            self.pwsh_probe(script, [str(config)])
        # Real native children verify executable identity beyond PowerShell aliases.
        runtime = self.workflow_block('# FEATURE004-RUNTIME-BEGIN', '# FEATURE004-RUNTIME-END')
        self.pwsh_probe("$ErrorActionPreference = 'Stop'\n" + capability + runtime)
        alias_only = r'''
$ErrorActionPreference = 'Stop'
$python = (Get-Command python3 -CommandType Application | Select-Object -First 1).Source
Set-Alias python3 $python
$env:PATH = [IO.Path]::GetTempPath()
if (@(Get-Command python3 -CommandType Application -ErrorAction SilentlyContinue).Count -ne 0) {
    throw 'Fixture unexpectedly has a child executable'
}
& $python -B -c "import shutil,sys;sys.exit(0 if shutil.which('python3') is None else 1)"
if ($LASTEXITCODE -ne 0) { throw 'Alias leaked into fresh process' }
'PASS: a PowerShell alias alone cannot satisfy child PATH'
'''
        self.pwsh_probe(alias_only)
        self.assertIn("$_.executionClass -eq 'native-automated-gate'", source)
        self.assertIn("$_.executionTasks -contains 'T048'", source)
        self.assertIn('$_.platforms -contains $env:AOC_FEATURE004_PLATFORM', source)
        catalog = json.loads((REPO/CONTRACTS/'validation-commands.json').read_text())['commands']
        selected = [c for c in catalog if c['executionClass'] == 'native-automated-gate'
                    and 'T048' in c['executionTasks']]
        self.assertTrue(selected)
        self.assertTrue(all(c['command'].split()[0] in ['bash', 'pwsh', 'python3', 'git'] for c in selected))
        self.assertFalse(any(c['id'] in ['stats-render', 'stats-preview', 'public-readiness'] for c in selected))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=REPO)
    parser.add_argument("--shell", choices=["bash", "pwsh"], default="bash")
    parser.add_argument("--case", choices=["surface", "empty-integration", "criteria-cardinality", "modes", "failure-taxonomy", "transitive-paths", "transitive-readers", "series-negatives", "status-next", "query-no-side-effects", "query-receipt-provenance", "runner-cardinality", "all"], default="all")
    parser.add_argument("--binding", choices=["feature", "legacy"], default="feature")
    args = parser.parse_args()
    BINDING = args.binding
    REPO, SHELL = args.repo.resolve(), args.shell
    names = ["surface", "empty_integration", "criteria_cardinality", "modes", "failure_taxonomy", "transitive_paths", "transitive_readers", "series_negatives", "status_next", "query_no_side_effects", "query_receipt_provenance", "query_idle", "query_shell_surface", "runner_cardinality"] if args.case == "all" else [args.case.replace("-", "_")]
    if args.case == "status-next":
        names += ["query_no_side_effects", "query_receipt_provenance", "query_idle", "query_shell_surface"]
    suite = unittest.TestSuite((SeriesTests if name in ["transitive_paths", "transitive_readers", "series_negatives"] else RunnerTests if name == "runner_cardinality" else QueryTests if name in ["status_next", "query_no_side_effects", "query_receipt_provenance", "query_idle", "query_shell_surface"] else EligibilityTests)("test_" + name) for name in names)
    raise SystemExit(0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1)
