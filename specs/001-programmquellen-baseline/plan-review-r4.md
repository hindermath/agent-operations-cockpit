# Unabhaengiges Plan-Review R4: Programmquellen-Baseline / Independent Plan Review R4: Program Sources Baseline

**Review-Datum / Review date**: 2026-08-09

**Review-Scope**: `specs/001-programmquellen-baseline`

**Review-Rolle / Review role**: neue unabhaengige R4-Plan-Review-Rolle ohne Beteiligung an R1 bis R3 oder den Remediations / new independent R4 plan reviewer without participation in R1 through R3 or their remediations

## Kurzurteil / Executive Assessment

Die R3-Leerwertluecke ist teilweise, aber nicht vollstaendig geschlossen. Der
AEPS-Validator grenzt jetzt den kanonischen Finding-Abschnitt ab, parst
zugeordnete Feldzeilen und weist fehlende, doppelte oder leere Werte
fail-closed ab. Die 16 feature-lokalen Contract-Tests bestehen, einschliesslich
des neuen Leerwert-Negativfalls. Eine zusaetzliche R4-Matrix bestaetigt, dass
alle 14 derzeit modellierten Feldzeilen bei einzeln geleertem Wert abgewiesen
werden. / *The R3 empty-value gap is partially but not completely closed. The
validator now isolates the canonical finding section, parses assigned field
rows, and rejects missing, duplicate, or empty values. All 16 feature-local
contract tests pass, including the new empty-value case. An additional R4
matrix confirmed rejection when each of the 14 currently modelled field rows
is emptied individually.*

R2-H02 bleibt dennoch als High offen. Status-, Reifegrad- und Pfadbindung
arbeiten weiterhin mit ungenauen Teilstringvergleichen. Dadurch bestehen
`NotRecordedness`, `PendingPublicationLater`, `observation-ish` sowie
Source-/Receipt-Pfade mit einem zusaetzlichen `.bak`-Suffix. Ausserdem fasst der
Validator Capture- und Upstream-Status in einem generischen gemeinsamen
`Status`-Feld zusammen und weist die zwei kanonischen Pflichtfelder
`Erfassungsstatus / Capture status` und `Upstream-Status / Upstream status` ab.
Damit beweist Gate G10 seinen deklarierten fail-closed Scope noch nicht. / *R2-H02
therefore remains open at High severity. Status, maturity, and path binding
still use imprecise substring comparisons. Invalid suffixed values and paths
pass, while the two canonical separate capture and upstream fields are
rejected. Gate G10 consequently does not yet prove its declared fail-closed
scope.*

## Pruefgrundlage und Schreibgrenze / Review Basis and Write Boundary

Vollstaendig gelesen wurden `AGENTS.md`, `.specify/memory/constitution.md`, die
einschlaegige installierte Autonomous-Run-Governance einschliesslich Preset,
Command, Handbuch, Authority, Lifecycle, Evidence, Recovery und
Kompatibilitaet, `docs/documentation-governance.md`, `docs/aeps/README.md`,
`requirements/baseline/autonomy-and-evidence-model.md`,
`requirements/baseline/authority-and-stop-gates.md`, das vollstaendige
META-LH-01-Intake und alle textuellen Artefakte unter
`specs/001-programmquellen-baseline`, besonders alle drei historischen
Plan-Reviews. Abgeleitete `__pycache__`-Binaerdateien wurden nicht als normative
Quelle behandelt. / *The review fully read the repository guidance,
constitution, applicable autonomous, Documentation Impact, AEPS and authority
governance, the complete intake, and every textual feature artefact. Derived
bytecode was not treated as a normative source.*

Alle Python-Aufrufe verwendeten zugleich `PYTHONDONTWRITEBYTECODE=1` und
`python3 -B`. Ausser dieser Datei wurde nichts erzeugt oder geaendert. Intake,
Run-State, Vertraege, Tests, Domain-Dateien, Git-Index und Remotes blieben
unveraendert. Dieses Review gehoert zum bereits geplanten einzigen
feature-weiten `UpdateRequired`-Eintrag und erzeugt keine zweite
Documentation-Impact-Entscheidung. Die AEPS-Erfassung bleibt innerhalb des
bereits geplanten G10-Implementierungs-Receipts; die R4-Schreibgrenze
autorisiert kein zusaetzliches Ledger oder Receipt. / *Every Python invocation
disabled bytecode through both controls. No artefact other than this report was
created or changed. This review remains covered by the single planned
feature-wide `UpdateRequired` decision; its write boundary authorises no
additional AEPS ledger or receipt mutation.*

## Ausgefuehrte Evidence / Executed Evidence

| Pruefung / Check | Ergebnis / Result | Beurteilung / Assessment |
|---|---|---|
| `PYTHONDONTWRITEBYTECODE=1 python3 -B .../test_validate_meta_lh01.py` | Pass: 16 isolierte Faelle / 16 isolated cases | Neuer Leerwert-Negativfall enthalten; reale Repository-Dateien bleiben unberuehrt. / Includes the new empty-value case without touching real repository files. |
| `input-bindings --surface bash` | Pass | Drei reale Roh-SHA-256-Werte und Bash-Schemaoberflaechen stimmen. / Three raw hashes and Bash schema surfaces match. |
| `input-bindings --surface powershell` | Pass | Drei reale Roh-SHA-256-Werte und PowerShell-Schemaoberflaechen stimmen. / Three raw hashes and PowerShell schema surfaces match. |
| `global-ready` | Pass | Alle 14 aktuellen Ziele, Hashes, Receipts, nicht supersedierten `Ready`-Single-Leafs und beide Validatoroberflaechen bestehen; META-LH-01 bleibt zuerst. / All fourteen current targets and both surfaces pass; META-LH-01 remains first. |
| `jq empty` fuer alle Feature-JSON-Dateien / for every feature JSON file | Pass | Gate-Requirements, Run-State und Kandidaten-Allowlist sind gueltiges JSON. / Gate requirements, run state, and candidate allowlist are valid JSON. |
| Python-AST-Pruefung / Python AST check | Pass: 2 Dateien / files | Validator und Tests sind syntaktisch gueltig; kein Bytecode wurde erzeugt. / Validator and tests are syntactically valid without bytecode generation. |
| Gate-Strukturpruefung / gate shape check | Pass | 19 eindeutige Gate-IDs; Applicable- und `N/A`-Vertraege besitzen die erwartete Form. / Nineteen unique IDs with the expected Applicable and N/A shape. |
| `domain` vor Implementierung / before implementation | Erwarteter Fail / expected failure | Exit 1, stdout leer, genau eine stderr-Zeile und ausschliesslich `SRC-163` bis `SRC-167`. / Exit 1, empty stdout, one stderr line, and only the five expected source IDs. |
| R4-Leerwertmatrix / R4 empty-value matrix | Pass: 14 Einzelvarianten / individual variants | Jede derzeit modellierte Pflichtfeldzeile wird bei leerem Wert abgewiesen. / Every currently modelled required field row is rejected when empty. |
| R4-All-Checks-Grenztest / R4 all-checks boundary test | Pass | `pass` plus `skipping` wird akzeptiert; eine leere Required-Teilmenge wird abgewiesen. / Pass plus skipping is accepted; an empty required subset is rejected. |
| R4-AEPS-Adversarialpruefung / R4 AEPS adversarial check | **Unzulaessige Passes / invalid passes** | Status-Suffixe, Maturity-Suffix und Source-/Receipt-Suffixpfade werden akzeptiert; getrennte kanonische Statusfelder werden abgewiesen. / Invalid suffixed values and paths pass; canonical split status fields are rejected. |

Der reale `candidate-fixpoint` und Remote-Gates wurden vertragsgemaess nicht
gegen den Vorimplementierungs-Worktree ausgefuehrt. Ihre Reihenfolge,
Proof-Grenze und isolierten Kernfunktionen wurden statisch und mit
In-Memory-/Temporaerfixtures geprueft. / *The real candidate fixed point and
remote gates were not executed against the pre-implementation worktree. Their
ordering, proof boundary, and isolated core functions were reviewed statically
and with in-memory or temporary fixtures.*

## Offener Befund / Open Finding

### R4-H01 / R2-H02 — High — AEPS-Werte sind noch nicht exakt an ihre kanonischen Felder gebunden

**Orte / Locations**:
`contracts/validate_meta_lh01.py:451-520`,
`contracts/test_validate_meta_lh01.py:195-221`,
`autonomous-run-gate-requirements.json:105-110`,
`docs/aeps/README.md` Abschnitt `Pflichtfelder / Required fields`.

**Geschlossener Anteil / Closed portion**: Der Finding-Abschnitt wird exakt
zwischen kanonischen `## AEPS-FIND-AOC-NNN`-Ueberschriften abgegrenzt. Jede
modellierte Feldzeile muss genau einmal vorkommen und einen nichtleeren Wert
besitzen. Der neue Test reproduziert nicht mehr den unzulaessigen R3-Pass. / *The
canonical finding section is isolated, each modelled field row must occur once
with a non-empty value, and the former R3 empty-skeleton pass no longer
reproduces.*

**Verbleibende Luecke / Remaining gap**:

- Die kanonische AEPS-Governance definiert `Erfassungsstatus / Capture status`
  und `Upstream-Status / Upstream status` als zwei Pflichtfelder. Der Validator
  erwartet stattdessen ein gemeinsames `Status / Capture and upstream status`-
  Feld. / *The canonical contract defines two status fields, but the validator
  expects one combined field.*
- Die Statuspruefung nutzt `value in status_value`. Deshalb gelten ungueltige
  Werte mit gueltigem Teilstring als Treffer. / *Substring membership accepts
  invalid suffixed status values.*
- Die Reifegradbindung nutzt ebenfalls nur `maturity in fieldValue`; der
  Ledger-Wert muss weder exakt ein gueltiger Reifegrad sein noch exklusiv mit
  dem Receipt uebereinstimmen. / *Maturity uses substring membership rather
  than one exact allowed value equal to the receipt.*
- Source und Receipt werden nur als Teilstrings gesucht. Ein anderer Pfad mit
  angehaengtem Suffix bindet daher scheinbar dieselbe Evidence. / *Source and
  receipt paths are matched as substrings, so suffixed paths falsely bind.*
- `Datum und Commit` sowie `Preset-Bezug` werden nur auf Nichtleerheit, nicht
  auf den im AEPS-Vertrag geforderten Inhalt beziehungsweise eine begruendete
  `N/A`-Angabe geprueft. / *Date/commit and related-presets fields are checked
  only for non-emptiness, not their AEPS contract semantics or justified N/A.*

Diese Luecke ist materiell, weil G10 vollstaendige Pflichtfeld-, Binding- und
Statusvalidierung behauptet und vor Tasks fail-closed sein muss. / *This is
material because G10 claims complete field, binding, and status validation and
must fail closed before Tasks.*

**Erforderliche minimale Remediation / Required minimal remediation**:

1. Capture- und Upstream-Status als zwei kanonisch benannte Pflichtfelder
   parsen und je Feld exakt einen Wert aus der jeweiligen Allowlist verlangen.
2. Reifegrad als genau einen erlaubten Ledger-Wert parsen und exakt mit dem
   Receipt-Wert vergleichen.
3. Source- und Receipt-Pfad als vollstaendige Markdown-Pfadtoken im
   Source-Feld vergleichen, nicht als beliebige Teilstrings.
4. Datum/Commit und Preset-Bezug gegen ihre AEPS-Vertragsgrenzen pruefen.
5. Isolierte Negativfaelle fuer Status-Suffixe, Maturity-Suffix,
   Source-/Receipt-Suffixe, vertauschte oder fremde Felder und getrennte
   Statusfeld-Kardinalitaet hinzufuegen; danach die 16 bestehenden Faelle,
   beide Input-Oberflaechen und `global-ready` erneut ausfuehren.

*Parse the two status axes separately with exact allowlist membership, bind one
exact allowed maturity to the receipt, compare complete path tokens, validate
date/commit and related-preset semantics, and add isolated adversarial cases
before rerunning the existing suite and all three binding surfaces.*

## Historische Befunde / Historical Findings

| Befund / Finding | R4-Status | Begruendung / Rationale |
|---|---|---|
| R2-H01 | Closed, keine Regression / no regression | Zweipassiger Kandidaten-Fixpunkt, vorhandene Evidence-Pfadanker, bytegleiches `cmp`, anschliessende Evidence-Validierung und Stage-Reihenfolge bleiben erhalten; die isolierte Spaetpfad-Erkennung besteht. / Two-pass fixed point and ordering remain intact. |
| R2-H02 | **Open (High)** | Leerwerte sind geschlossen; exakte Status-, Maturity- und Pfadbindung bleibt fail-open. / Empty values are fixed, but exact status, maturity, and path binding remains fail-open. |
| R2-H03 | Closed, keine Regression / no regression | Alle gemeldeten Checks plus nichtleere Required-Teilmenge, `pass`/`skipping`, atomare Tokens, exakter Head, Review-Decision und Threads bleiben gebunden. / All checks, required subset, exact head, review decision, and threads remain bound. |
| R2-M01 | Closed, keine Regression / no regression | Semantik und Accessibility besitzen weiterhin getrennte Dateien, Kriterienmengen, unabhaengige Rollen und Gate-IDs. / Semantic and accessibility evidence remain separate. |
| R1-C01 | Closed | Stabiler read-only Domain-Vertrag, sechs Pfade, exakte 23/21/10-Mengen und 16 bestehende Contract-Faelle. / Stable executable domain contract and 16 passing cases. |
| R1-C02 | Closed | Kausale Commit-/PR-Head-Reihenfolge, All-Checks, Threads, temporaerer Evidence-Render und getrennter schema-1.1-Closeout bleiben erhalten. / Causal exact-head and closeout chain remains intact. |
| R1-C03 | Closed | `global-ready` besteht aktuell und bleibt vor Tasks, jedem Analyze und Implement gebunden. / Current global gate passes and remains phase-bound. |
| R1-H01 | Closed | Beide Input-Modi binden alle drei realen Roh-Hashes vor ihren Schemaoberflaechen. / Both input modes bind all three raw hashes. |
| R1-H02 | Offen ausschliesslich ueber R2-H02 / open only through R2-H02 | Maschinen-, Secret-, Public-, Semantic- und A11Y-Proof-Grenzen bleiben getrennt; nur die AEPS-Exaktbindungs-Luecke verbleibt. / Proof classes remain separate; only exact AEPS binding remains open. |
| R1-H03 | Closed | Schema 1.1, genau ein Documentation-Impact-Eintrag, kanonisches Intake und Kandidaten-Fixpunkt bleiben gebunden. / Schema, cardinality, source, and fixed point remain bound. |
| R1-H04 | Closed | Gespeicherter Liefermodus und aktuelle Autoritaet bleiben getrennt; Revalidierung vor irreversiblen Aktionen bleibt gefordert. / Stored mode and current authority remain separate. |
| R1-M01 | Closed | Staged, unstaged und untracked Inventare sowie `git diff --cached --check` bleiben fail-closed gebunden. / Candidate inventories and staged whitespace remain fail closed. |

## Bewertung der 19 Gate-Anforderungen / Assessment of the 19 Gate Requirements

`Closed` bedeutet hier einen scope-treuen, ausfuehrbaren oder klar
phasengebundenen Nachweis; es behauptet keinen vorgezogenen Implementierungs-
oder Remote-Pass. / *Closed means scope-faithful executable or clearly
phase-bound evidence, not an early implementation or remote pass.*

| Gate | R4-Status | Beurteilung / Assessment |
|---|---|---|
| `META01-G01-input-binding-bash` | Closed | Aktuell ausgefuehrt und bestanden: drei Roh-Hashes plus Bash-Schema. / Executed and passed. |
| `META01-G02-input-binding-powershell` | Closed | Aktuell ausgefuehrt und bestanden: drei Roh-Hashes plus PowerShell-Schema. / Executed and passed. |
| `META01-G03-global-ready-14` | Closed | Aktuell fuer alle 14 Ziele und beide Oberflaechen bestanden; erneute Ausfuehrung bleibt phasengebunden. / Passed and phase-bound. |
| `META01-G04-domain-contract` | Closed | Vertrag und 16 Tests bestehen; der reale Vorimplementierungs-Fail nennt nur `SRC-163` bis `SRC-167`. / Contract passes and real failure is limited to the planned rows. |
| `META01-G05-markdown-structure` | Closed | Rendererfolge und Struktur-only-Proof-Grenze bleiben ehrlich getrennt. / Renderer order and structure-only boundary remain sound. |
| `META01-G06-independent-semantic-review` | Closed | Eigene Datei, Kriterienklasse, Rolle und Null-Blocking-Grenze. / Separate evidence, role, and outcome. |
| `META01-G06A-independent-accessibility-review` | Closed | Eigene Datei, A11Y-Kriterien, Rolle und Null-Blocking-Grenze. / Separate accessibility evidence, role, and outcome. |
| `META01-G07-secret-pattern-scans` | Closed | Scope behauptet nur Secret-Mustersuche. / Scope claims only pattern detection. |
| `META01-G08-independent-public-content-review` | Closed | Exakte Kandidatenabdeckung und Validierung folgen dem bytegleichen Fixpunkt. / Exact coverage follows the fixed point. |
| `META01-G09-documentation-impact` | Closed | Schema 1.1, genau ein Eintrag, einziges Intake und stabile exakte Pfadmenge bleiben gebunden. / Correct schema, cardinality, source, and path set. |
| `META01-G10-aeps-outcome` | **Open (High)** | Required Scope ueberbehauptet exakte Status-, Maturity- und Pfadbindung; R4 reproduziert unzulaessige Passes. / Required scope overclaims exact binding; R4 reproduced invalid passes. |
| `META01-G11-statistics` | Closed | Post-Implementierungs-Render und beide check-only-Oberflaechen bleiben gebunden. / Render and both check-only surfaces remain bound. |
| `META01-G12-exact-candidate` | Closed | Stage-, Porcelain-, Restdiff- und Whitespace-Abstimmung bleiben exakt. / Exact candidate reconciliation remains bound. |
| `META01-G12A-candidate-fixed-point` | Closed | Zwei Ableitungen, bytegleiches `cmp` und Fixpunkt liegen vor Evidence-Validierung und Stage. / Two derivations precede validation and staging. |
| `META01-G13-pr-head-convergence` | Closed | All-Checks, Required-Teilmenge, atomare Tokens, exakter Head, Threads und Approval-only-Bypass bleiben gebunden. / All-check and exact-head convergence remains sound. |
| `META01-N01-product-tests-runtime` | N/A accepted | Kein Produktcode oder Produkt-Runtime; Trigger vorhanden. / No product code or runtime; trigger exists. |
| `META01-N02-supply-chain` | N/A accepted | Keine Dependency-, Build-, Paket-, AI-Runtime- oder Release-Ausgabe; Trigger vorhanden. / No supply-chain output; trigger exists. |
| `META01-N03-script-platform-parity` | N/A accepted | Kein neues Bash-/PowerShell-Produkttool; vorhandene Paare bleiben Pruefoberflaechen. / No new product script pair. |
| `META01-N04-agent-parity-presets-level0` | N/A accepted | Shared Guidance, Presets, Level 0 und Home Sync bleiben ausserhalb des Scopes. / Shared guidance, presets, level 0, and Home Sync remain out of scope. |

## Scope, Authority und naechste sichere Aktion / Scope, Authority, and Next Safe Action

Der fachliche Scope bleibt unveraendert auf sechs Level-2-Domain-Dokumente und
begrenzte Workflow-, Documentation-Impact-, AEPS- und Statistik-Evidence. Es
gibt keine Produktarchitektur, keinen Produktcode, kein Scaffold, keine
Produkt-Runtime, keine Preset-Promotion und keine Level-0-Mutation. Die aktuelle
R4-Anweisung autorisiert nur dieses Review und genau diese Berichtsdatei; sie
autorisiert weder Tasks noch Implementierung, Index-, Commit- oder
Remote-Aktionen. Der gespeicherte `MergeAndSync`-Modus bleibt historische
Run-Evidence und erzeugt fuer R4 keine zusaetzliche Berechtigung. / *The domain
scope remains unchanged. The current R4 instruction authorises only this
review and this report, not Tasks, implementation, index, commit, or remote
actions. Stored delivery mode remains historical evidence rather than current
R4 authority.*

Die naechste sichere Aktion ist eine minimale Reparatur von R4-H01 innerhalb
der bereits definierten Contract-/Testflaeche und danach ein erneutes
unabhaengiges Plan-Review mit 16 bestehenden sowie den neuen adversarialen
Negativfaellen. Tasks bleiben bis zu einem Review ohne offenen Critical- oder
High-Befund gesperrt. / *The next safe action is a minimal contract/test repair
for R4-H01 followed by another independent plan review. Tasks remain blocked
until no Critical or High finding remains.*

## Terminales Urteil / Terminal Verdict

NeedsRemediation
