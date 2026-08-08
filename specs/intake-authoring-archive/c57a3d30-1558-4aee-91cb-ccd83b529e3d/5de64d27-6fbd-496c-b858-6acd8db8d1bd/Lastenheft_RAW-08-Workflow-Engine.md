<!-- intake-authoring:begin -->
# RAW-08 – Workflow Engine und Program-to-Knowledge / Workflow Engine and Program-to-Knowledge

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Git- und Review-Grundlagen; keine Governance-Engine-Erfahrung / Git and review basics; no governance-engine experience
**Profile:** `aoc-bilingual-requirements`

## Zweck und Grenze / Purpose and boundary

Die Reihe verbindet Charter, Sources, Decisions, Intakes, Specs, Plans, Tasks,
Evidence und Retrospektiven als nachvollziehbaren Workflow. Sie besitzt deren
Lifecycle und Traceability, aber keine AOC-Produktzustandslogik. / *The series
connects programme artifacts into a traceable workflow and owns lifecycle, not
product-state semantics.*

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

SRC-159, 168, 174; RF-03, RF-12, RF-14. Inputs: RAW-05/06 Execution Evidence
und alle Governance Receipts. Output: prüfbare Knowledge Package an RAW-09.

## Anforderungen / Requirements

- **FR-001:** Jedes Artefakt MUSS stabile ID, Quelle, Status, Owner und Revision besitzen.
- **FR-002:** Übergänge MÜSSEN Preconditions, Authority, Output Hash und Stop-Gate binden.
- **FR-003:** Evidence MUSS positive, negative und Provider-Failure-Klassen trennen.
- **FR-004:** Retrospektive darf Beobachtung nicht still in normative Decision verwandeln.
- **NFR-001:** JSON-/Textnachweis ist reproduzierbar, secret-free und B2-erklärbar.

## Bestätigte Decisions, Mode und Recovery / Confirmed decisions, mode, and recovery

Die drei materiellen Entscheidungen sind bestätigt: / *The three material
decisions are confirmed:*

1. **IAD801 – Persistenz:** Workflow-, Evidence- und Knowledge-Package-
   Artefakte verwenden versionierte, kanonische und menschenlesbare JSON-
   Dokumente unter `evidence/workflow/<workflow-id>/`. Jedes veröffentlichte
   Dokument bindet Schema-Version, stabile ID, Revision und SHA-256. Ein Writer
   schreibt zuerst eine temporäre Datei im selben Verzeichnis, validiert sie
   und ersetzt das Ziel atomar; das Receipt wird zuletzt veröffentlicht.
   Unvollständige temporäre Dateien gelten nie als Zustand. Recovery beginnt
   ausschließlich am letzten vollständig validierten und hashgebundenen
   Receipt. Eine Datenbank darf ein ableitbarer Index, aber nie die kanonische
   Quelle sein. / *Workflow, evidence, and knowledge-package artifacts use
   versioned, canonical, human-readable JSON documents below
   `evidence/workflow/<workflow-id>/`. Every published document binds its
   schema version, stable ID, revision, and SHA-256. A writer first writes and
   validates a temporary file in the same directory, atomically replaces the
   target, and publishes the receipt last. Partial temporary files are never
   state. Recovery starts only from the last fully validated, hash-bound
   receipt. A database may be a derived index, but never the canonical source.*
2. **IAD802 – Signatur und Attestation:** Receipts und Knowledge Packages
   verwenden ein versioniertes standardisiertes Attestation-Envelope mit
   abgetrennter Signatur über den kanonischen SHA-256-Inhaltshash. Zulässiges
   Signaturprofil, Key-ID und Trust Roots stehen in einer separat versionierten
   Trust Policy; private Schlüssel und Secrets liegen nie im Repository.
   Fehlende Signatur, unbekannter Schlüssel oder Trust Root, ungültige
   Signatur, Hashabweichung oder abgelaufene Policy werden fail-closed
   abgelehnt und dürfen weder Completion noch Recovery begründen. / *Receipts
   and knowledge packages use a versioned standard attestation envelope with
   a detached signature over the canonical SHA-256 content hash. The allowed
   signature profile, key ID, and trust roots are held in a separately
   versioned trust policy; private keys and secrets never enter the repository.
   A missing signature, unknown key or trust root, invalid signature, hash
   mismatch, or expired policy fails closed and cannot support completion or
   recovery.*
3. **IAD803 – Retention:** Governance-, Decision- und Completion-Receipts
   bleiben für die Projektlebensdauer erhalten und werden bei Supersession
   archiviert. Operative Ausführungsevidence läuft standardmäßig 90 Tage nach
   Abschluss ab; Sicherheits- und Fehlschlagevidence läuft nach zwölf Monaten
   ab. Ein dokumentierter Legal Hold setzt die Löschung bis zur Freigabe aus
   und bindet Grund, Owner, Prüfdatum und Ablauf. Jede Löschung erzeugt ein
   Lösch-Receipt mit Artefakt-ID, Evidence-Klasse, Fälligkeit, Authority,
   Ausführungszeit und Ergebnis; Secrets und unnötige personenbezogene Daten
   dürfen nicht gespeichert werden. / *Governance, decision, and completion
   receipts remain for the project lifetime and are archived when superseded.
   Operational execution evidence expires 90 days after completion by
   default; security and failure evidence expires after twelve months. A
   documented legal hold suspends deletion until release and binds its reason,
   owner, review date, and expiry. Every deletion creates a deletion receipt
   with artifact ID, evidence class, due date, authority, execution time, and
   result; secrets and unnecessary personal data must not be stored.*

RAW-05 und RAW-06 liefern die abhängigen Evidence Contracts. Der zulässige
Mode bleibt bis zu einem aktuellen vollständigen Review und separater
Ausführungsautorität `research-only`; `serial-autonomous` ist nur eine spätere
Möglichkeit. Keine Decision, Eligibility oder Receipt erteilt selbst Start-,
Implementierungs-, Governance-Write-, Remote-, Merge- oder Bypass-Autorität. /
*RAW-05 and RAW-06 provide the dependent evidence contracts. The allowed mode
remains `research-only` until a current complete review and separate execution
authority exist; `serial-autonomous` is only a later possibility. No decision,
eligibility state, or receipt itself grants start, implementation,
governance-write, remote, merge, or bypass authority.*

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Artifact Lifecycle; Traceability Graph; Evidence/Receipt Contract;
Retrospective Handoff. **AC-001:** ein End-to-End-Beispiel ist von Source bis
Retrospektive lückenlos. **AC-002:** fehlende Authority, Hash-Drift und
ProviderFailure blockieren falsche Completion.

Revision bei Lifecycle-/Receipt-Schema. Keine Produkt-, Delivery- oder Preset-Promotion-Autorität.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md --delivery-mode MergeAndSync --require-current-review
```
<!-- intake-authoring:end -->
