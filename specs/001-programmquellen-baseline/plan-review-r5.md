# Unabhaengiges Plan-Review R5: Programmquellen-Baseline / Independent Plan Review R5: Program Sources Baseline

**Review-Datum / Review date**: 2026-08-09

**Review-Scope**: `specs/001-programmquellen-baseline`

**Review-Rolle / Review role**: neue unabhaengige R5-Plan-Review-Rolle ohne Beteiligung an R1 bis R4 oder den Remediations / new independent R5 plan reviewer without participation in R1 through R4 or their remediations

## Kurzurteil / Executive Assessment

Die ausdruecklich erwartete 20-Fall-Suite besteht. Ebenso bestehen beide
Input-Bindings, das globale 14er-Gate, alle JSON- und Python-Syntaxpruefungen,
die Struktur von 19 eindeutigen Gate-Anforderungen und der erwartete
Vorimplementierungs-Fail ausschliesslich fuer `SRC-163` bis `SRC-167`. Die
R4-Remediation hat ausserdem alle 15 AEPS-Pflichtfelder als getrennte,
eindeutige und nichtleere Feldzeilen modelliert, Capture- und Upstream-Status
getrennt und die benannten Suffixfaelle fuer Status, Reifegrad, Source und
Receipt geschlossen. / *The expected twenty-case suite passes, as do both
input bindings, the fourteen-target gate, JSON and Python syntax, nineteen
unique gate requirements, and the expected pre-implementation failure limited
to `SRC-163` through `SRC-167`. The remediation also models all fifteen AEPS
fields as separate, unique, non-empty rows, separates capture from upstream
status, and rejects the named suffixed status, maturity, source, and receipt
cases.*

Gate G10 bleibt dennoch fail-open. Der Validator verlangt nicht genau eine
vollstaendige kanonische Tokenmenge je gebundenem Feld. Ein korrektes
Capture-Token zusammen mit einem ungueltigen Zusatz-Token, ein doppeltes
Capture-Token, der erwartete Reifegrad zusammen mit einem zweiten Reifegrad und
die beiden erwarteten Pfade zusammen mit einem fremden dritten Pfad werden
akzeptiert. Ausserdem bestehen weiterhin ein beliebiger nichtleerer
Datum/Commit-Wert und ein unbegruendetes `N/A` beim Preset-Bezug. Diese
unzulaessigen Passes liegen innerhalb des einzigen offenen historischen
R4-Befunds und widersprechen der behaupteten vollstaendigen kanonischen
Ledger-Bindung. Der verbleibende Befund ist High und blockiert Tasks. / *Gate
G10 remains fail-open because it does not require one complete canonical token
set per bound field. Extra or duplicate status, maturity, and path tokens pass,
as do malformed date/commit content and an unjustified preset `N/A`. These
invalid passes remain within the sole historical R4 finding and block Tasks.*

## Pruefgrundlage und Schreibgrenze / Review Basis and Write Boundary

Vollstaendig gelesen wurden `AGENTS.md`, `.specify/memory/constitution.md`, die
einschlaegige Autonomous-Run-Governance zu Authority, Lifecycle, Recovery,
Evidence und Closeout, `docs/documentation-governance.md`,
`docs/aeps/README.md`, `docs/aeps/findings-ledger.md`,
`requirements/baseline/autonomy-and-evidence-model.md`,
`requirements/baseline/authority-and-stop-gates.md`, das vollstaendige
META-LH-01-Intake und alle textuellen Artefakte unter
`specs/001-programmquellen-baseline`, besonders die vier historischen
Plan-Reviews. Abgeleitete `__pycache__`-Binaerdateien wurden nicht als
normative Quelle behandelt. / *The review fully read the repository guidance,
constitution, applicable autonomous, Documentation Impact, AEPS, authority and
evidence governance, the complete intake, every textual feature artefact, and
all four historical plan reviews. Derived bytecode was not treated as a
normative source.*

Alle Python-Aufrufe verwendeten `PYTHONDONTWRITEBYTECODE=1` und `python3 -B`.
Ausser dieser Datei wurde nichts erzeugt oder geaendert. Intake, Run-State,
Vertraege, Tests, Domain-Dateien, Git-Index und Remotes blieben unveraendert.
Dieses R5-Review gehoert zum bereits geplanten einzigen feature-weiten
`UpdateRequired`-Eintrag und erzeugt keine zweite Documentation-Impact-
Entscheidung. / *Every Python invocation disabled bytecode generation. No
artefact other than this report was created or changed. This review remains
within the single planned feature-wide `UpdateRequired` decision.*

## Ausgefuehrte Evidence / Executed Evidence

| Pruefung / Check | Ergebnis / Result | Beurteilung / Assessment |
|---|---|---|
| `PYTHONDONTWRITEBYTECODE=1 python3 -B .../test_validate_meta_lh01.py` | Pass: 20 isolierte Faelle / 20 isolated cases | Kanonischer Positivfall sowie vorhandene Domain-, Evidence-, Leerwert-, Suffix-, Kandidaten- und Check-Negativfaelle bestehen. / Canonical positive and existing negative cases pass. |
| `input-bindings --surface bash` | Pass | Drei reale Roh-SHA-256-Werte und Bash-Schemaoberflaechen stimmen. / Three raw hashes and Bash schema surfaces match. |
| `input-bindings --surface powershell` | Pass | Drei reale Roh-SHA-256-Werte und PowerShell-Schemaoberflaechen stimmen. / Three raw hashes and PowerShell schema surfaces match. |
| `global-ready` | Pass | Alle 14 aktiven Ziele, aktuelle Hashes, Receipts, nicht supersedierten `Ready`-Single-Leafs und beide Validatoroberflaechen bestehen; META-LH-01 bleibt zuerst. / All fourteen current targets and both surfaces pass; META-LH-01 remains first. |
| Feature-JSON mit `jq empty` | Pass | Gate-Requirements, Run-State und Kandidaten-Allowlist sind gueltiges JSON. / All feature JSON is valid. |
| Gate-Struktur mit `jq` | Pass | Genau 19 eindeutige Gate-IDs; alle `Applicable`- und `N/A`-Eintraege besitzen die erwartete Form. / Exactly nineteen unique gate IDs have the expected shape. |
| Python-AST-Pruefung / Python AST check | Pass: 2 Dateien / files | Validator und Tests sind syntaktisch gueltig; kein Bytecode wurde erzeugt. / Both files parse without bytecode generation. |
| `domain` vor Implementierung / before implementation | Erwarteter Fail / expected failure | Exit 1, stdout leer, genau eine stderr-Zeile und ausschliesslich `SRC-163` bis `SRC-167`. / Exit 1, empty stdout, one stderr line, and only the five planned IDs. |
| R5-Pflichtfeldmatrix / mandatory-field matrix | Pass: 15 Einzelvarianten / individual variants | Jede kanonische Pflichtfeldzeile wird bei einzeln geleertem Wert abgewiesen; der vollstaendige Positivfall besteht. / Every individually emptied field is rejected and the canonical case passes. |
| R5-Statusachsenpruefung / status-axis check | Pass | Getrennte kanonische Capture-/Upstream-Felder werden akzeptiert; ein gemeinsames Statusfeld sowie vertauschte oder suffigierte Werte werden abgewiesen. / Split fields pass; a combined field and swapped or suffixed values fail. |
| R5-Token-Kardinalitaetspruefung / token-cardinality check | **Unzulaessige Passes / invalid passes** | Doppeltes Capture-Token, zusaetzliches ungueltiges Capture-Token, zweiter Reifegrad und dritter Source-Pfad werden akzeptiert. / Duplicate or extra status, maturity, and path tokens are accepted. |
| R5-Datum-/Preset-Pruefung / date and preset check | **Unzulaessiger Pass / invalid pass** | `Datum und Repository-Commit: arbitrary` und unbegruendetes `Preset-Bezug: N/A` werden akzeptiert. / Malformed date/commit content and unjustified preset N/A are accepted. |

Der reale Kandidaten-Fixpunkt, Renderer mit Schreibwirkung, Stage und Remote-
Gates wurden wegen der R5-Schreib- und Authority-Grenze nicht gegen den
Vorimplementierungs-Worktree ausgefuehrt. Ihre Reihenfolge, Proof-Grenzen und
isolierten Kernfunktionen wurden statisch gegen die unveraenderten Artefakte
geprueft. / *The real fixed point, writing renderer, staging, and remote gates
were not executed under the R5 write and authority boundary. Their ordering,
proof limits, and isolated core functions were reviewed statically.*

## Offener Befund / Open Finding

### R5-H01 / R4-H01 / R2-H02 - High - G10 erzwingt keine exklusive kanonische AEPS-Feldbindung

**Orte / Locations**:
`contracts/validate_meta_lh01.py:502-524`,
`contracts/test_validate_meta_lh01.py:224-289`,
`autonomous-run-gate-requirements.json:105-110`,
`contracts/baseline-validation-contract.md:96-109`,
`docs/aeps/README.md:112-153`.

**Geschlossener Anteil / Closed portion**: Der Finding-Abschnitt wird exakt
abgegrenzt. Alle 15 Pflichtfelder werden einzeln zugeordnet, muessen genau eine
Feldzeile besitzen und duerfen nicht leer sein. `Erfassungsstatus / Capture
status` und `Upstream-Status / Upstream status` sind getrennte kanonische
Felder. Ein Positivfall und die geforderten Leerwert- sowie suffigierten
Status-, Reifegrad- und Pfadfaelle bestehen. / *The section boundary, fifteen
separate non-empty fields, split status axes, canonical positive case, empty
values, and suffixed-token cases are closed.*

**Verbleibende Luecke / Remaining gap**:

- `capture_matches` und `upstream_matches` pruefen nur, wie viele verschiedene
  erlaubte Werte irgendwo in der Tokenliste vorkommen. Ein erlaubtes Token
  darf deshalb doppelt vorkommen oder neben einem ungueltigen Token stehen. /
  *Status validation counts distinct allowlist matches rather than requiring
  exactly one complete token.*
- Die Reifegradpruefung verlangt den Receipt-Wert genau einmal, verbietet aber
  keinen zweiten abweichenden Reifegrad im selben Feld. / *The expected
  maturity may coexist with a second maturity token.*
- Source und Receipt muessen je einmal vorkommen, aber ein dritter fremder
  Pfadtoken wird nicht abgewiesen. / *The two required paths may coexist with
  an unrelated third path token.*
- Datum/Commit und Preset-Bezug werden weiterhin nur auf Nichtleerheit
  geprueft. Der kanonische Vertrag verlangt einen Evidence-Commit oder
  `PendingPublication` mit Base-HEAD und Artefakthash sowie eine Begruendung
  fuer `N/A`. / *Date/commit and related-presets semantics remain unchecked.*
- Die 20-Fall-Suite deckt Suffixe ab, aber keinen der reproduzierten
  Mehrtoken- oder Semantikfaelle. / *The twenty-case suite covers suffixes but
  none of the reproduced multi-token or semantic cases.*

**Auswirkung / Impact**: Ein Ledger-Eintrag kann widerspruechliche Capture-,
Reifegrad- oder Provenienzangaben enthalten und trotzdem G10 bestehen. Damit
beweist G10 nicht seinen deklarierten Scope eines vollstaendigen kanonischen
Ledger-Abschnitts. Das ist eine materielle Evidence-Integritaetsluecke vor
Tasks. / *A contradictory ledger record can pass G10, so the gate does not
prove its declared canonical-ledger scope. This is a material pre-Tasks
evidence-integrity gap.*

**Erforderliche minimale Remediation / Required minimal remediation**:

1. Fuer Capture und Upstream jeweils die gesamte Code-Tokenliste auf exakt ein
   Token begrenzen und dieses Token gegen die jeweilige Allowlist pruefen. /
   *Require exactly one total token per status field and exact allowlist
   membership.*
2. Fuer Reifegrad exakt ein Token verlangen; dieses muss erlaubt sein und
   exakt dem Receipt-Wert entsprechen. / *Require one allowed maturity token
   exactly equal to the receipt.*
3. Im Source-Feld exakt die zwei gebundenen Pfadtokens ohne Zusatzpfad
   verlangen. / *Require exactly the two bound path tokens and no extra path.*
4. Datum/Commit gegen die beiden kanonischen Formen und `N/A` beim
   Preset-Bezug nur mit nichtleerer Begruendung akzeptieren. / *Validate the
   canonical date/commit forms and require rationale for preset N/A.*
5. Isolierte Negativfaelle fuer doppeltes/zusatzliches Status-Token, zweiten
   Reifegrad, dritten Pfad, fehlerhaften Datum/Commit-Wert und unbegruendetes
   Preset-`N/A` ergaenzen. Danach die komplette Suite, beide Input-Oberflaechen
   und `global-ready` erneut ausfuehren. / *Add the named adversarial cases and
   rerun the complete suite and all three binding surfaces.*

## Historische Befunde / Historical Findings

| Befund / Finding | R5-Status | Begruendung / Rationale |
|---|---|---|
| R1-C01 | Closed, keine Regression / no regression | Stabiler read-only Domain-Vertrag, sechs Pfade, exakte 23/21/10-Mengen und 20 bestehende Faelle. / Stable domain contract and existing suite. |
| R1-C02 | Closed, keine Regression / no regression | Kausale Commit-/PR-Head-Reihenfolge, All-Checks, Threads, temporaerer Evidence-Render und schema-1.1-Closeout bleiben getrennt. / Causal exact-head and closeout chain remains intact. |
| R1-C03 | Closed, keine Regression / no regression | `global-ready` besteht aktuell und bleibt vor Tasks, jedem Analyze und Implement gebunden. / Current global gate passes and remains phase-bound. |
| R1-H01 | Closed, keine Regression / no regression | Beide Input-Modi binden alle drei realen Roh-Hashes vor ihren Schemaoberflaechen. / Both input modes bind all three raw hashes. |
| R1-H02 | Open ausschliesslich ueber R5-H01 / open only through R5-H01 | Maschinen-, Secret-, Public-, Semantic- und A11Y-Proof-Grenzen bleiben getrennt; die AEPS-Exklusivbindung bleibt offen. / Proof classes remain separate; AEPS exclusive binding remains open. |
| R1-H03 | Closed, keine Regression / no regression | Schema 1.1, genau ein Documentation-Impact-Eintrag, kanonisches Intake und Kandidaten-Fixpunkt bleiben gebunden. / Schema, cardinality, source, and fixed point remain bound. |
| R1-H04 | Closed, keine Regression / no regression | Gespeicherter Liefermodus und aktuelle Authority bleiben getrennt; R5 leitet keine Remote-Berechtigung ab. / Stored mode and current authority remain separate. |
| R1-M01 | Closed, keine Regression / no regression | Staged, unstaged und untracked Inventare sowie `git diff --cached --check` bleiben fail-closed gebunden. / Candidate reconciliation remains bound. |
| R2-H01 | Closed, keine Regression / no regression | Zweipassiger Fixpunkt, vorhandene Pfadanker und bytegleiches `cmp` bleiben vor Evidence-Validierung und Stage. / Fixed-point order remains sound. |
| R2-H02 | **Open (High)** | R3-Leerwerte und R4-Suffixfaelle sind geschlossen; exklusive Tokenmenge sowie Datum/Commit- und Preset-Semantik bleiben fail-open. / Empty and suffix cases are closed; exclusive tokens and remaining field semantics are fail-open. |
| R2-H03 | Closed, keine Regression / no regression | Alle gemeldeten Checks plus nichtleere Required-Teilmenge, exakter Head und Approval-only-Bypass bleiben gebunden. / All-check and exact-head proof remains sound. |
| R2-M01 | Closed, keine Regression / no regression | Semantik und Accessibility besitzen getrennte Dateien, Kriterien, Rollen und Gate-IDs. / Semantic and accessibility evidence remain separate. |
| R3-Fortfuehrung von R2-H02 / continuation | Open ueber R5-H01 | Alle einzeln geleerten Felder werden nun abgewiesen; Mehrtoken- und Restsemantikfaelle fehlen weiterhin. / Empty fields are fixed; multi-token and remaining semantic cases are not. |
| R4-H01 | **Open (High)** | Die explizit geforderten Suffixfaelle bestehen, aber genau-ein-Wert-, Zusatzpfad-, Datum/Commit- und begruendete-`N/A`-Grenzen sind nicht vollstaendig umgesetzt. / Suffix cases pass, but the remaining exact-one and semantic boundaries do not. |

## Bewertung der 19 Gate-Anforderungen / Assessment of the 19 Gate Requirements

`Closed` bedeutet einen scope-treuen ausfuehrbaren oder klar
phasengebundenen Plan-Nachweis. Spaetere Implementierungs- und Remote-Gates
behaupten keinen vorgezogenen Ausfuehrungspass. / *Closed means a
scope-faithful executable or clearly phase-bound plan proof, not an early
implementation or remote pass.*

| Gate | R5-Status | Beurteilung / Assessment |
|---|---|---|
| `META01-G01-input-binding-bash` | Executed Pass | Drei Roh-Hashes plus Bash-Schema bestehen. / Three raw hashes and Bash schema pass. |
| `META01-G02-input-binding-powershell` | Executed Pass | Drei Roh-Hashes plus PowerShell-Schema bestehen. / Three raw hashes and PowerShell schema pass. |
| `META01-G03-global-ready-14` | Executed Pass | Alle 14 Ziele und beide Oberflaechen bestehen; erneute Ausfuehrung bleibt phasengebunden. / All targets and both surfaces pass. |
| `META01-G04-domain-contract` | Closed; erwarteter Vorimplementierungs-Fail / expected pre-implementation failure | Der Fail ist exakt auf `SRC-163` bis `SRC-167` begrenzt; die 20 isolierten Contract-Faelle bestehen. / Failure is limited to the five planned rows. |
| `META01-G05-markdown-structure` | Closed, phase-bound | Rendererfolge und Struktur-only-Proof-Grenze bleiben getrennt; kein schreibender Lauf in R5. / Renderer order and proof boundary remain sound. |
| `META01-G06-independent-semantic-review` | Closed, phase-bound | Eigene Evidence-Datei, Kriterienklasse, Rolle und Null-Blocking-Grenze. / Separate evidence, role, and outcome. |
| `META01-G06A-independent-accessibility-review` | Closed, phase-bound | Eigene A11Y-Evidence, Kriterien, Rolle und Null-Blocking-Grenze. / Separate accessibility evidence and outcome. |
| `META01-G07-secret-pattern-scans` | Closed, phase-bound | Scope behauptet nur Secret-Mustersuche. / Scope claims only pattern detection. |
| `META01-G08-independent-public-content-review` | Closed, phase-bound | Exakte Kandidatenabdeckung und Validierung folgen dem bytegleichen Fixpunkt. / Exact coverage follows the fixed point. |
| `META01-G09-documentation-impact` | Closed, phase-bound | Schema 1.1, genau ein Eintrag, einziges Intake und stabile Pfadmenge bleiben gebunden. / Schema, cardinality, source, and stable paths remain bound. |
| `META01-G10-aeps-outcome` | **Open (High)** | 20 Tests und die verlangten Suffixfaelle bestehen, aber widerspruechliche Zusatz-Tokens und unvollstaendige Datum-/Preset-Semantik passieren. / Extra contradictory tokens and incomplete field semantics pass. |
| `META01-G11-statistics` | Closed, phase-bound | Post-Implementierungs-Render und beide Check-only-Oberflaechen bleiben gebunden. / Render and both checks remain bound. |
| `META01-G12-exact-candidate` | Closed, phase-bound | Stage-, Porcelain-, Restdiff- und Whitespace-Abstimmung bleiben exakt. / Exact candidate reconciliation remains bound. |
| `META01-G12A-candidate-fixed-point` | Closed, phase-bound | Zwei Ableitungen und bytegleiches `cmp` liegen vor Evidence-Validierung und Stage. / Two derivations precede validation and staging. |
| `META01-G13-pr-head-convergence` | Closed, phase-bound | All-Checks, Required-Teilmenge, exakter Head, Threads und Approval-only-Bypass bleiben gebunden. / All checks and exact-head convergence remain sound. |
| `META01-N01-product-tests-runtime` | N/A accepted | Kein Produktcode oder Produkt-Runtime; Neubewertungs-Trigger vorhanden. / No product code or runtime. |
| `META01-N02-supply-chain` | N/A accepted | Keine Dependency-, Build-, Paket-, AI-Runtime- oder Release-Ausgabe; Trigger vorhanden. / No supply-chain output. |
| `META01-N03-script-platform-parity` | N/A accepted | Kein neues Bash-/PowerShell-Produkttool; vorhandene Paare bleiben Pruefoberflaechen. / No new product script pair. |
| `META01-N04-agent-parity-presets-level0` | N/A accepted | Shared Guidance, Presets, Level 0 und Home Sync bleiben ausserhalb des Scopes. / Shared guidance and level 0 remain out of scope. |

## Scope, Proof-Grenzen und Authority / Scope, Proof Boundaries, and Authority

Der fachliche Scope bleibt auf sechs Level-2-Domain-Dokumente und begrenzte
Workflow-, Documentation-Impact-, AEPS- und Statistik-Evidence beschraenkt.
Produktarchitektur, Produktcode, Scaffold, Produkt-Runtime, Preset-Promotion,
Level-0-Mutation und andere Intakes bleiben ausgeschlossen. Deterministische
Pruefungen beweisen nur Struktur, Mengen, Pfade, Hashes, Tokens und
Evidence-Vollstaendigkeit; fachliche, sprachliche, Accessibility- und
Publikationseignung bleiben getrennten unabhaengigen Reviews vorbehalten. /
*The scope remains limited to six level-2 domain documents and bounded
workflow evidence. Deterministic validation proves only its documented
structural boundary; semantic, accessibility, and publication truth remain
independent review responsibilities.*

Die aktuelle R5-Anweisung autorisiert nur dieses Review und genau diese neue
Berichtsdatei. Sie autorisiert weder Vertrags- oder Testreparatur noch Tasks,
Implementierung, Index, Commit, Remote, Merge, Bypass, Preset-Promotion oder
Level-0-Handoff. Der gespeicherte `MergeAndSync`-Modus ist Run-Evidence und
keine aktuelle R5-Berechtigung. / *The R5 instruction authorises only this
review report. Stored delivery mode is evidence, not current R5 authority.*

Der AEPS-Trigger wurde bewertet: R5-H01 ist ein neues reproduzierbares
Evidence-Integritaetsdetail innerhalb des bereits offenen R4-/R2-Findings.
Die aktuelle Schreibgrenze verbietet ein Ledger- oder Receipt-Update. Owner ist
der AOC Requirements Maintainer; Risiko ist ein fail-open G10 vor Tasks; die
Wiedervorlage erfolgt nach minimaler Contract-/Testreparatur und vor dem
naechsten Plan-Review. Evidence ist dieser Bericht; Scope-Grund ist die
ausdrueckliche Ein-Datei-Grenze. / *The AEPS trigger was assessed. This is new
reproducible detail within the existing finding, but the one-file boundary
forbids ledger or receipt mutation. Re-evaluate after a minimal contract/test
repair and before the next plan review.*

## Naechste sichere Aktion / Next Safe Action

Die naechste sichere Aktion ist die eng begrenzte Reparatur von R5-H01 in der
bereits vorhandenen Contract-/Testflaeche. Danach muessen die erweiterte
isolierte Suite, beide Input-Bindings, `global-ready`, JSON/Python-Syntax, die
19 Gate-Anforderungen und der erwartete Domain-Fail erneut unabhaengig
ausgefuehrt werden. Tasks, Analyze, Implementierung, Commit und Remote bleiben
bis zu einem Review ohne offenen Critical- oder High-Befund gesperrt. / *The
next safe action is a minimal contract/test repair followed by a new
independent review of all named evidence. Downstream work remains blocked.*

## Terminales Urteil / Terminal Verdict

NeedsRemediation
