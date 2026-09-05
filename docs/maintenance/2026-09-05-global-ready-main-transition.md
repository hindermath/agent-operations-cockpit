# Global-Ready nach Merge / Global Ready after merge

## Auftrag und Grenze / Authority and boundary

Thorsten hat am 2026-09-05 den lokalen Model-Routing-Refresh und die begrenzte,
getestete Reparatur des Global-Ready-Uebergangs auf `main` ausdruecklich
genehmigt. Erst nach bestandenen Startgates folgt der separat beauftragte
META-LH-03-Lauf mit `MergeAndSync`. Diese Reparatur startet selbst keinen
Spec-Kit-Lauf und erteilt keinen Admin-Bypass.

*Thorsten explicitly authorised the local routing refresh and this bounded,
tested main-transition repair. The separately authorised META-LH-03 run follows
only after its entry gates pass. This repair starts no Spec Kit run and grants
no admin bypass.*

## Reproduzierbarer Ausgangspunkt / Reproducible baseline

Base-HEAD: `3c9a618243fffff187932b1ee431ffbd25d3856e`.
META-LH-01 und META-LH-02 sind `Completed`; ihre State-Validatoren bestehen.
META-LH-03 besitzt ein aktuelles Receipt und ein aktuelles Ready-Single-Review;
beide Validatoroberflaechen bestehen. Trotzdem scheitert der alte
`validate_meta_lh01.py --repo . global-ready`-Einstieg am archivierten
META-LH-02-Pfad. Die beiden `validate-meta-lh02-snapshot`-Peers scheitern auf
`main` an der fest gebundenen aktiven Feature-Branchidentitaet.

*Both predecessor run states and the target's receipt and Ready review pass.
The legacy entry point rejects the archived META-LH-02 path; both snapshot
peers reject main because they still require the former active feature branch.*

## Reparaturvertrag / Repair contract

- Aktive Laeufe behalten ihre bisherigen Branch- und Event-Grenzen.
- Vollstaendig abgeschlossene Laeufe duerfen auf nachgewiesenen Nachfahren
  ihrer ausgelieferten Historie geprueft werden; ein Branchname allein genuegt nicht.
- Die 14 logischen Ziele, Original-/Archiv-Exklusivitaet, Hashbindungen,
  eindeutige aktuelle Ready-Reviews und beide Review-Oberflaechen bleiben Pflicht.
- Bestehende Intakes, Receipts, Lifecycle- und Run-State-Artefakte werden nicht
  umgeschrieben. Unerwartete Drift wird nicht als beabsichtigtes Delta akzeptiert.
- CI prueft den exakten Event-Head und holt die Historie fuer den
  Abstammungsnachweis. Jeder native Prozess-Exitcode wird unmittelbar geprueft.
- Der abgeschlossene META-LH-02-Intake muss am Archivpfad verbleiben. Der alte
  Global-Ready-Einstieg darf auch bei fehlendem Archiv nicht auf einen frueheren
  Pruefpfad zurueckfallen. Sein Subprozess muss genau die erwartete PASS-Zeile liefern.
- Kanonische Receipt-/Review-Rohhashes bleiben bytegenau. Zusaetzlich werden
  Index und Arbeitsdateien auf Git-clean geprueft; saubere CRLF-Checkouts bleiben
  moeglich, echte Inhaltsaenderungen werden abgelehnt.

*Active runs retain their old boundaries. Completed runs require proven
delivery ancestry, not a branch-name exception. All target, hash, review,
exclusivity and platform checks remain mandatory. Historical evidence is not
rewritten, and CI checks exact event heads with full history and immediate exit
handling. Completed META-LH-02 remains archive-only; a missing archive cannot
trigger a legacy fallback. The subprocess must return the exact success line.
Canonical raw hashes remain exact, with Git-clean index and worktree proof
that permits clean CRLF checkouts but rejects content changes.*

## Pruefung und Liefergrenze / Validation and delivery boundary

Lokal bestanden / *Local passes*:

- `python3 -B specs/001-programmquellen-baseline/contracts/test_validate_meta_lh01.py`:
  71 Tests / *71 tests*.
- `python3 -B specs/002-portfolio-ownership/contracts/test_validate_meta_lh02_snapshot.py`:
  22 Tests, einschliesslich realer Bash-/PowerShell-Paritaet und sauberem
  CRLF-Git-Checkout / *22 tests including real Bash/PowerShell parity and clean
  CRLF Git checkout*.
- `python3 -B specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . global-ready`:
  Exit 0; 14 gebundene Ready-Ziele / *exit 0; 14 bound Ready targets*.
- `pwsh -NoProfile -File scripts/invoke-psscriptanalyzer.ps1`:
  108 getrackte Dateien ohne Befund / *108 tracked files without findings*.
- `bash scripts/scan-agent-secrets.sh --fail-on-high .`: Exit 0; High 0.
- `git diff --check`: Exit 0.

Negativtests decken unvollstaendigen Closeout, fehlende Abstammung, manipulierte
Hashes, falsche CI-Identitaet, Archiv-Ruecknahme, ungueltige Subprozessantworten
und unerwartete Intake-Pfade ab. Der Statistikblock wird nach dem Code-Commit
mit dem vorhandenen Renderer aktualisiert und anschliessend read-only geprueft.
Die unabhaengige Reviewkorrektur und die Remote-Ergebnisse werden im PR
nachgewiesen. Die drei CI-Plattformen bleiben vor dem Merge Pflicht, ebenso
eine aktuelle unabhaengige Approval. Es wird kein Admin-Bypass verwendet.

*Negative tests cover incomplete closeout, missing ancestry, changed hashes,
false CI identity, archive reversal, invalid subprocess output and unexpected
intake paths. The existing renderer updates statistics after the code commit;
the result is then checked read-only. The PR records the independent review and
actual remote results. All three CI platforms and a current independent approval
remain mandatory before merge; no admin bypass is used.*

Die exakten zusaetzlichen Liefergates stehen in
[gate-requirements.json](global-ready-main-transition-20260905/gate-requirements.json).
Die vorhandenen Repository-Pflichtchecks bleiben zusaetzlich verbindlich.

*The linked file declares the exact additional delivery gates. Existing required
repository checks remain mandatory.*

Unabhaengiges Code-Review: `review_main_gate`, 2026-09-05. Die drei Befunde zu
sauberen CRLF-Checkouts, Archiv-Ruecknahme und exakter Subprozessantwort wurden
begrenzt behoben und erneut geprueft. Ergebnis: keine verbleibenden Befunde im
Reparaturumfang. Das Review stuetzt die Tests auf den separat berichteten Lauf;
die Remote-Matrix ist vor Merge weiterhin nachzuweisen.

*Independent code review: review_main_gate, 2026-09-05. All three findings were
fixed and re-reviewed; none remain in scope. The reviewer used the separately
reported test run, so the remote platform matrix remains mandatory before merge.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle sind die beiden Python-Vertraege und
die CI-Definition; Owner ist der AOC-Maintainer. Dieses Dokument und die
Snapshot-Manpage erklaeren den geaenderten Uebergang fuer Maintainer und
Lernende auf CEFR-B2-Niveau, Deutsch zuerst und Englisch danach. Leserpfad:
Ausgangsfehler, Sicherheitsgrenze, Pruefung, danach ausdruecklich autorisierter
Start. Nur Level-2-Quellen werden geliefert; kein Home-Sync oder Preset-Rollout.
Neue Lifecycle- oder Review-Formen loesen eine erneute Bewertung aus.

*Decision: UpdateRequired. The two Python contracts and CI definition are the
source; the AOC maintainer owns this note and the snapshot manual. The text-first
reader path explains the failure, safety boundary, tests and authorised start.
No home sync or preset rollout is involved; new lifecycle or review forms trigger
re-evaluation.*
