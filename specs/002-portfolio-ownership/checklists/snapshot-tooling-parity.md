# Snapshot-Tooling-Paritaet / Snapshot Tooling Parity

**Stand / Status**: T053 lokal abgeschlossen; exakte Windows-CI-Evidence spaeter / T053 completed locally; exact-head Windows CI evidence is later

**Datum / Date**: 2026-08-30

**Datenklasse / Data class**: Public

## Same-commit-Pfadmenge / Same-commit path set

Die vier T052-Pfade und die neun T053-Pfade einschliesslich des minimalen
Workflow-Deltas liegen gemeinsam im ungestagten `normal-feature-candidate` und
sind dort einzeln verpflichtend. Es wurde nicht gestagt oder committet. Die
spaetere Same-commit-Lieferung bleibt T068 bis T071 vorbehalten. / *The four
T052 paths and nine T053 paths, including the minimal workflow delta, are
present together in the unstaged normal candidate and are individually required
by its allowlist. No staging or commit occurred; final same-commit proof remains
owned by T068 through T071.*

- [x] Python-Core, Bash-Peer, PowerShell-Peer und Unix-Man-Page vorhanden. / Python core, both peers, and Unix manual exist.
- [x] Sechs benannte getrackte Fixtures, isolierter Test, diese Checkliste und der minimale Matrix-Workflow-Delta vorhanden. / Six named tracked fixtures, isolated test, this checklist, and the minimal matrix workflow delta exist.
- [x] Kein weiterer getrackter Fixture-Pfad wurde erzeugt. / No additional tracked fixture path was created.
- [x] Der fremde Preset-`__pycache__` bleibt unberuehrt und ausgeschlossen. / The unrelated preset cache remains untouched and excluded.

## Automatisierte lokale Evidence / Automated local evidence

`PYTHONDONTWRITEBYTECODE=1 python3 -B specs/002-portfolio-ownership/contracts/test_validate_meta_lh02_snapshot.py`
endete auf macOS mit Exitcode `0`: zehn Tests bestanden. Abgedeckt sind beide
positiven Peers, identische Ausgabe und Exitcodes, alle sechs getrackten
Negativfaelle einschliesslich der weiterhin unzulaessigen Stage `Specify`, der
exakt gebundene positive `Plan`-Retry, temporaere Projektionen fuer
Lifecycle-Form, beide/keinen Pfad,
Zielhash-Drift und inaktiven State sowie der getrennte Ausfall jeder
installierten Review-Oberflaeche. Der Vorher-/Nachher-Status war identisch. /
*The standard-library suite passed ten tests, admitted Plan only for the exact
bound retry, kept Specify disallowed, and covered every named positive,
negative, temporary-projection, individual-review-surface, parity, and no-write
case.*

- [x] Bash `-h` und `--help` verweisen auf `docs/man/validate-meta-lh02-snapshot.1`. / Bash help points to the manual.
- [x] PowerShell `-Help` und `Get-Help Test-AocMetaLh02Snapshot -Full` liefern bilinguale Hilfe. / PowerShell help is complete and bilingual.
- [x] `Test-AocMetaLh02Snapshot` ist als Advanced Function auffindbar. / The approved cmdlet is discoverable as an Advanced Function.
- [x] Positive Bash-/PowerShell-Ausgabe ist bytegleich; beide Exitcodes sind `0`. / Positive peer output is byte-identical and both exits are zero.
- [x] Alle getrackten Negativfaelle liefern peer-gleich Exitcode `1` und denselben fail-closed Fehler. / Every tracked negative has equivalent exit 1 and diagnostics.
- [x] `bash -n` und PSScriptAnalyzer `Error,Warning` bestehen. / Bash syntax and PowerShell static analysis pass.
- [x] Bash enthaelt Shebang, `set -euo pipefail`, gequotete Variablen und `--`-Disziplin. / Bash strictness is present.
- [x] PowerShell enthaelt `#Requires -Version 7`, StrictMode, Stop-Fehlerpraeferenz und validierte Parameter; Evidence lief mit `-NoProfile`. / PowerShell strictness is present.
- [x] Der Python-AST nennt nur Standardbibliotheksimporte; `shell=True`, dynamische Ausfuehrung und unsichere Deserialisierung fehlen. / Python is standard-library-only and avoids shell, dynamic execution, and unsafe deserialization.
- [x] `gitleaks dir --redact --no-banner --no-color specs/002-portfolio-ownership` endet `0`, `no leaks found`. / Feature gitleaks scan passes.
- [x] Beide Repository-Secret-Scanner enden `0`; Bash meldet `high=0`, PowerShell keine Secrets. / Both repository secret scanners pass.
- [x] Inhalte und Pfade sind repository-relativ und fuer die Datenklasse `Public` geeignet; keine Secrets, privaten Home-Pfade oder unnoetigen Personendaten wurden gefunden. / Content and paths are public-suitable.
- [x] NIST-SSDF-/CWE-Top-25-/Secure-code-Screening findet keine blockierende Abweichung in der lokalen Implementierung. / Local SSDF, CWE, and secure-code screening has no blocker.

## Manuelle Plattform-Evidence / Manual platform evidence

### macOS

- [x] Host: macOS 26.6.2, Darwin 25.6.0 arm64. / Host identity recorded.
- [x] Bash-Peer gegen das reale Repository: Exit `0`, exakte PASS-Zeile. / Bash peer passed against the real repository.
- [x] PowerShell-Core-7-Peer mit `-NoProfile`: Exit `0`, gleiche PASS-Zeile. / PowerShell peer passed with equivalent output.
- [x] Hilfe, Cmdlet, Man-Page, Negativfaelle und null Repository-Write manuell beziehungsweise durch den lokalen isolierten Lauf bestaetigt. / Help, cmdlet, manual, negatives, and no-write behaviour were verified locally.

### Windows-CI am exakten Head / Windows CI on the exact head

- [ ] `PowerShell Static Analysis / PSScriptAnalyzer` fuehrt fuer den exakt reviewten normalen Head die Feature-002-Snapshot-Suite und den PowerShell-Peer auf `windows-2022` aus. / The exact normal head runs the Feature-002 suite and PowerShell peer on Windows.
- [ ] Workflow, Job, Runner, Head-SHA, Log-URL, ausgefuehrter Command und Exitcode sind fuer Windows sowie die weiterhin erforderlichen Linux-/macOS-Jobs gebunden. / Workflow, job, runner, head, log, command, and exit are bound for Windows and the required Linux/macOS jobs.
- [ ] T090 wiederholt dieselbe fail-closed Evidence fuer den exakten terminalen Rename-Head. / T090 repeats the same fail-closed evidence for the exact terminal rename head.

**Evidence-Zeitplan / Evidence schedule**: Die Constitution verlangt die
manuelle Verifikation beider Varianten. Diese ist oben auf dem verfuegbaren
macOS-Host belegt. Sie ist keine Windows-Evidence. Reale Windows-Ausfuehrung
bleibt vor jedem Merge fuer den exakten reviewten Head zwingend und darf weder
erfunden noch durch Admin-Bypass ersetzt werden. Der historische
`implement-resume` bleibt bei T053 blockiert, weil der damalige Text einen
lokalen Windows-Host verlangte. Der aktuelle `implement-resume-3` schliesst
T053 mit der akzeptierten macOS- und Workflow-Evidence ab, ohne den historischen
Ausgang umzuschreiben. / *Both variants are manually verified on macOS. Real
Windows execution remains mandatory in exact-head CI before each merge and
cannot be invented or bypassed. The current resume completes T053 without
rewriting the historical blocked result.*

## Review-Disposition / Review disposition

Die lokale Security-/Plattform-Review meldet fuer beide auf macOS ausgefuehrten
Varianten und den minimalen Workflow-Delta `blocking findings: 0`.
Windows-Ausfuehrung, nachtraeglicher Analyze-6-Erfolg, Delivery, Level-0-Handoff oder
Preset-Promotion werden nicht behauptet. Die offene Windows-Evidence ist ein
spaeterer exakter CI-Head-Mergeblocker. / *Local review reports zero blockers
for both variants on macOS and the minimal workflow delta. Windows execution,
retroactive Analyze-6 success,
and downstream completion are not claimed; Windows remains a later exact-head
CI merge gate.*

## T079-Reparaturevidence / T079 repair evidence

Der erneute lokale Standardbibliothekslauf umfasst jetzt 14 Tests und endet
mit Exitcode `0`. Die vier fokussierten Faelle beweisen zusaetzlich: einen
exakten `pull_request`-Head mit passendem Repository und `GITHUB_HEAD_REF`, die
Ablehnung eines synthetischen SHA-Mismatch und einer lokal mehrdeutigen
detached Identitaet, identische normalisierte SHA-256 fuer LF und CRLF bei
weiterhin abgelehnter fachlicher Inhaltsdrift sowie die Auswahl eines absoluten
Git-for-Windows-`bash.exe` bei Ablehnung eines `System32`-/WSL-Launchers. /
*The renewed fourteen-test suite passes and adds exact PR-head proof,
synthetic/detached rejection, LF/CRLF equivalence with substantive-drift
failure, and Git-for-Windows Bash selection with WSL-launcher rejection.*

Beide reale Snapshot-Peers, beide Intake-Review-Peers, beide Series-Peers,
beide Run-State-Peers, alle sechs Portfolio-Laeufe, Bash-Syntax und
PSScriptAnalyzer `1.25.0` bestanden lokal. Das Workflow-Delta checkt
`github.event.pull_request.head.sha` beziehungsweise `github.sha` explizit aus
und startet den Bash-Peer nur ueber ein validiertes ausfuehrbares Argumentarray.
Die drei Windows-/Provider-Checkboxen oben bleiben bis zur erneuten Evidence am
exakten publizierten Head bewusst offen. / *All proportional local peers pass;
the provider-bound checkboxes remain open until renewed exact-head CI evidence.*
