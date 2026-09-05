# Cross-Platform-Paritätsnachweis / Cross-platform parity evidence

## Lokaler Kandidat / Local candidate

- Plattform / platform: macOS Darwin, Shell `zsh` mit Bash- und PowerShell-Unterprozessen.
- Git-HEAD: `ee530952acc8093c9afd8e01b97825a0a1c9ac72`; dies ist der Reparatur-Checkpoint, noch kein eingefrorener Feature-Commit.
- Python: `python3 -B`; PowerShell: `pwsh -NoProfile`; Bash: lokales `bash`.
- Additive Tests: `10/10`, Exit `0`.
- Gate-Evidence-Prevalidator: `6/6`, Exit `0`.
- Global Ready: 14 aktuelle Ready-Bindungen, Exit `0`.
- Receipt-Inventar über PowerShell: `14/14` eindeutige IDs, jeder unmittelbare Exit `0`.
- Receipt-, Lifecycle- und Config-Suiten: Exit `0`.
- PSScriptAnalyzer: Version `1.25.0`, 109 Dateien, Exit `0`; isolierter Negativbefund Exit ungleich `0`.
- Bash-Syntax, Python-AST, striktes JSON und drei Manpages: alle Exit `0` nach Behebung der drei reinen 80-Zeichen-Stilbefunde.

## 14 unmittelbare PowerShell-Exits / Fourteen immediate PowerShell exits

| Nr. | Logisches Ziel / Logical target | Exit |
|---:|---|---:|
| 1 | META-LH-01 | 0 |
| 2 | META-LH-02 | 0 |
| 3 | META-LH-03 | 0 |
| 4 | META-LH-04 | 0 |
| 5 | META-LH-05 | 0 |
| 6 | RAW-01 | 0 |
| 7 | RAW-02 | 0 |
| 8 | RAW-03 | 0 |
| 9 | RAW-04 | 0 |
| 10 | RAW-05 | 0 |
| 11 | RAW-06 | 0 |
| 12 | RAW-07 | 0 |
| 13 | RAW-08 | 0 |
| 14 | RAW-09 | 0 |

## Drei Runner und Auditstatus / Three runners and audit status

| Prüffeld / Checkpoint | Status | Evidence, Owner und Follow-up / Evidence, owner, and follow-up |
|---|---|---|
| `ubuntu-22.04` exakter PR-HEAD | Open | Owner: AOC-Maintainer. Der Kandidat kann nicht committed oder gepusht werden, weil `.git/index.lock` in der Sandbox nicht angelegt werden darf. Follow-up: Lauf in schreibfähiger Git-Umgebung. Trigger: `.git` write access. |
| `macos-14` exakter PR-HEAD | Open | Gleicher Blocker; lokale macOS-Evidence ersetzt keinen GitHub-Runner. / Same blocker; local macOS evidence does not replace the GitHub runner. |
| `windows-2022` exakter PR-HEAD | Open | Gleicher Blocker; Workflow fordert Git-for-Windows Bash über `AOC_GIT_BASH_EXE` und weist WSL ab. |
| Exact-head checkout | Pass | Workflow nutzt `github.event.pull_request.head.sha` und `fetch-depth: 0`. |
| Runner/HEAD/Version/Exit-Logging | Pass | Feature-003-Workflowstufe protokolliert Runner, `git rev-parse HEAD`, Python, PowerShell, Bash, jeden Befehl und unmittelbaren Exit. |
| Bash-/PowerShell-Hilfe und Manpages | Pass | Adapter-Schnittstellen, Exitklassen und drei Manpages sind statisch geprüft; `mandoc -T lint` Exit `0`. |
| Negativ-Harnesses | Pass | jq-Fehler propagiert; 14 Exits werden geloggt; erster Receipt-Fehler bleibt terminal; Analyzer-Finding bleibt terminal. |
| Drei-Runner-Gesamtaussage | Open | T056 und damit das unabhängige T060-Gesamtgate bleiben offen, bis alle drei realen Jobs denselben eingefrorenen Feature-HEAD erfolgreich geprüft haben. |

Es gibt keinen stillen Skip: Der fehlende Remote-Kandidat ist ausdrücklich
`Open` und verhindert `Completed`. / *There is no silent skip: the missing
remote candidate is explicitly Open and blocks Completed.*
