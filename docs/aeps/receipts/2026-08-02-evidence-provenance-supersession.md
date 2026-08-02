# AEPS-Evidence-Provenienz-Supersession / AEPS Evidence Provenance Supersession

## Identitaet und Ergebnis / Identity and outcome

- Receipt-ID: `AEPS-RECEIPT-AOC-2026-08-02-005`
- Datum / Date: `2026-08-02`
- Trigger: formale Korrektur historischer, nicht mehr reproduzierbarer
  Live-Pfad-Bindungen / *formal correction of historical live-path bindings
  that are no longer reproducible*
- Ergebnis / Outcome: `ReproducibleConsolidation`
- Upstream-Status: `PendingPublication`

Dieses Receipt ersetzt nicht die historischen Aussagen der drei betroffenen
Receipts. Es supersediert ausschliesslich deren Funktion als reproduzierbarer
Nachweis fuer damals erzeugte, spaeter weiterentwickelte AEPS-Arbeitsdateien.
Die historischen Receipts bleiben unveraendert erhalten. / *This receipt does
not replace the historical statements of the three affected receipts. It
supersedes only their function as reproducible evidence for AEPS working files
that were changed later. The historical receipts remain unchanged.*

## Supersedierte Nachweisfunktion / Superseded evidence function

| Historisches Receipt / Historical receipt | Receipt-SHA-256 | Betroffene Bindungen / Affected bindings | Klassifikation / Classification |
|---|---|---:|---|
| `docs/aeps/receipts/2026-08-01-initial-inventory.md` | `76a362ff2f84aba349436ffd6fe264cd17b29d74b2bb6b18139b1c737123da71` | 4 | `UnverifiableHistoricalSnapshot` |
| `docs/aeps/receipts/2026-08-01-meta-lh-04-ready.md` | `8dcedf66e71ae387cfad5787c391c6e7b335806146f3a770c58525d340251640` | 4 | `UnverifiableHistoricalSnapshot` |
| `docs/aeps/receipts/2026-08-01-meta-lh-05-needs-remediation.md` | `361a1a0a5c50aeb674e47614c6e189c432c6733b2bb548f1910077a6df7a8d73` | 4 | `UnverifiableHistoricalSnapshot` |

Betroffen sind in jedem Receipt die damaligen Hashbindungen auf
`findings-ledger.md`, `finding-to-preset-candidate-matrix.md`,
`preset-gap-analysis.md` und `upstream-handoff.md`. Die dort genannten
Zwischeninhalte wurden vor ihrer Weiterentwicklung nicht als unveraenderliche
Snapshots archiviert. Die zwoelf historischen Hashwerte lassen sich deshalb
heute nicht mehr aus dem Repository rekonstruieren. Quellen, Review-IDs,
Entscheidungen und fachliche Aussagen der Receipts sind davon nicht
automatisch entwertet. / *Each receipt is affected in its former hash bindings
to the four evolving AEPS working files. Their intermediate contents were not
archived as immutable snapshots, so the twelve historical hashes can no
longer be reconstructed from the repository. This does not automatically
invalidate the receipts' sources, review identities, decisions, or domain
statements.*

## Aktueller reproduzierbarer Konsolidierungsstand / Current reproducible consolidation

| Artefakt / Artifact | SHA-256 |
|---|---|
| `docs/aeps/findings-ledger.md` | `4bca179048c3143c8074b24e0dd9faece145e9f267f8eb3a98e5cbacac134684` |
| `docs/aeps/finding-to-preset-candidate-matrix.md` | `6ee584f7623a35269f880494531953292d536dcdd642cf79198c3b08e74b5259` |
| `docs/aeps/preset-gap-analysis.md` | `ac2cb9fcdca150bb28e8d3dd1b9fcae31ae5e334fd270b78ceaee718c7e4e981` |
| `docs/aeps/upstream-handoff.md` | `a1a81d6e6e63b385fc4740c352ec54705c9d79a649e87edd0db26f3f0adb2b52` |
| `docs/aeps/receipts/2026-08-01-meta-lh-05-ready.md` | `82b641264feaa8981f25c19432423a06fdf61870d0dc2cb0e3b35615d021b266` |

Das META-LH-05-Ready-Receipt bindet denselben aktuellen Stand der vier
Arbeitsdateien. Dieses Konsolidierungsreceipt macht die historische
Beweisgrenze ausdruecklich und schafft einen eigenstaendigen, pruefbaren
Abschlusspunkt. Es bindet sich nicht selbst, um einen selbstreferenziellen Hash
zu vermeiden. / *The META-LH-05 Ready receipt binds the same current state of
the four working files. This consolidation receipt makes the historical
evidence limit explicit and creates an independent, verifiable closure point.
It does not hash itself.*

## Aktuelle META-LH-04-Lineage / Current META-LH-04 lineage

| Quelle / Source | SHA-256 |
|---|---|
| `specs/intake-review-results/meta-lh-04-series-eligibility-2026-08-02-r3.json` | `27a5313932aac67099851769a05fd0fa08943797b815f80e2342555ed3ec95e7` |
| `docs/reviews/meta-lh-04-series-eligibility-intake-review-2026-08-02-r3.md` | `08cb8088fd8ff0c67e50959fd3195531517c7e109a9661dfdf7fda22d85c58d6` |
| `specs/intake-authoring-receipts/META-LH-04-Series-Eligibility.json` | `215c059848c2782b33a7b6f1b068a3ad22dbaee452a4884f6f9c7c5556b4b9e4` |
| `specs/intake-series/aoc-phase-2/manifest.json` | `15ac795d2c9737896f41cd183fe9c21d39b5374f1661b9ecda0eea5ffc344f85` |
| `specs/intake-series-receipts/aoc-phase-2.json` | `5a377df09ce3ea5ebe2d3c8de687075f19ab45c446f20a8fbd552124d116ef15` |

Das aktuelle META-LH-04-Single-Review ist `Ready`. Die neue Authoring- und
Series-Lineage ist reproduzierbar gebunden. Diese Supersession aendert weder
den Series-Lifecycle noch Eligibility, Reihenfolge, Roots oder Abhaengigkeiten.
*The current META-LH-04 Single review is Ready. Its renewed authoring and
series lineage is reproducibly bound. This supersession changes no lifecycle,
eligibility, ordering, roots, or dependencies.*

## Kuenftiger Provenienzvertrag / Future provenance contract

Ein Receipt darf einen spaeter veraenderbaren Arbeitsstand nur dann als
reproduzierbare historische Evidence beanspruchen, wenn der gebundene Inhalt
unter einem unveraenderlichen Archivpfad, einem erreichbaren Git-Objekt oder
einer gleichwertig dauerhaften Referenz erhalten bleibt. Andernfalls muss die
Bindung ausdruecklich als zeitpunktbezogene, nicht archivierte Beobachtung
klassifiziert werden. / *A receipt may claim an evolving working state as
reproducible historical evidence only when the bound content remains available
through an immutable archive path, a reachable Git object, or an equivalent
durable reference. Otherwise, the binding must be classified explicitly as a
point-in-time observation without an archived snapshot.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist die genehmigte formale Supersession
der nicht reproduzierbaren historischen Live-Pfad-Bindungen. Owner ist der
AOC-AEPS-Evidence-Workstream. Aktualisiert wird ausschliesslich dieses neue
Konsolidierungsreceipt; die historischen Receipts und die fachlichen
AEPS-Arbeitsdateien bleiben unveraendert. Evidence sind der vollstaendige
Hashabgleich, die aktuelle META-LH-04-Lineage und der aktuelle reproduzierbare
AEPS-Konsolidierungsstand. / *Decision: UpdateRequired. The approved formal
supersession is the source and the AOC AEPS evidence workstream is the owner.
Only this consolidation receipt is added; historical receipts and domain
working files remain unchanged.*

## Validierung und Grenzen / Validation and boundaries

- alle in diesem Receipt gebundenen lokalen Pfade vorhanden;
- alle angegebenen SHA-256-Werte gegen den aktuellen Arbeitsbaum pruefbar;
- zwoelf nicht reproduzierbare historische Bindungen ausdruecklich
  klassifiziert;
- historische Receipts byte-identisch belassen;
- keine Presets, Produktdateien, aktiven Intakes oder Referenzprojekte
  veraendert;
- durch die Supersession selbst keine Specify-, Implementierungs-, Level-0-,
  Issue-, Remote-, Merge- oder Bypass-Aktion ausgefuehrt.

*All bound paths and hashes are verifiable, twelve historical bindings are
classified explicitly, historical receipts remain byte-identical, and no
preset, product, intake, reference-project, delivery, merge, or bypass action
was performed.*
