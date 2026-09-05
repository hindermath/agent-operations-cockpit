# META-LH-03: offene Vertragsentscheidung / Open contract decision

## Ergebnis / Outcome

`NeedsClarification` vor Plan und Implementierung. Der technisch gültige
Startnachweis nach PR #37 ist nicht gleichbedeutend mit erfülltem AC-003 von
META-LH-03. Historische Evidence bleibt unverändert. / *NeedsClarification
before planning and implementation. The valid startup gate after PR #37 is
not the same as META-LH-03 AC-003 completion. Historical evidence is preserved.*

## Reproduzierbare Befunde / Reproducible findings

Basis ist `ada16a88833aae246f2db396a565bc941109617b`. Der unabhängige lokale
Scope-Audit bestätigte die drei gebundenen Fixture-Suites und den aktuellen
META-LH-03-Receipt als bestanden. Er führte beide Receipt-Validatoren über die
14 Ziele aus. Genau drei Receipts scheitern an der Quelle
`requirements/baseline/portfolio-ownership.md`: / *The independent local scope
audit passed the three bound suites and META-LH-03 receipt, then checked all
fourteen receipts on both surfaces. Exactly three fail on the stated source:*

| Receipt unter / below `specs/intake-authoring-receipts/` | Quelle / Source |
|---|---|
| `META-LH-02-Portfolio-Ownership.json` | SRC005 |
| `META-LH-05-Erste-Welle.json` | SRC008 |
| `RAW-03-State-Truthfulness.json` | SRC007 |

Gebundener normalisierter SHA-256 / *Bound normalized SHA-256*:
`10cb40e62c4e4b44bc25942c2bdff8cd2c1cda80124f6a3bfd1dc97ac5927c9d`.
Aktueller normalisierter SHA-256 / *Current normalized SHA-256*:
`12f062ba167a43b78b899b2f7b19d310363ce8c4438b1652e71c6f94e7b25106`.

Der Koordinator bestätigte den META-LH-05-Fall zusätzlich direkt: / *The
coordinator additionally reproduced the META-LH-05 case directly:*

```text
bash .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.sh --receipt specs/intake-authoring-receipts/META-LH-05-Erste-Welle.json --repo .
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.ps1 -Receipt specs/intake-authoring-receipts/META-LH-05-Erste-Welle.json -Repo .
```

Beide melden Exitcode `2` und
`ERROR: source hash drift: requirements/baseline/portfolio-ownership.md`.
Dies ist erwartete historische Source-Drift nach META-LH-02, kein neuer
ungeklärter Fremd-Write. / *Both return exit 2 with the stated diagnostic.
This is expected historical source drift after META-LH-02, not a newly
unexplained foreign write.*

Zusätzlich nennt das gebundene META-LH-03 die Preset-Version `0.3.0` als
verbindlich, während `.specify/presets/intake-authoring-governance/preset.yml`
Version `0.3.1` deklariert. Diese Installation stammt aus Commit
`75479d284b56857bd20200ae1d66ee7d9c5b8563`; der aktuelle Lauf hat sie nicht
geändert. / *The intake binds version 0.3.0, but the installed preset declares
0.3.1 from the stated earlier commit. This run did not change the installation.*

## Unterschied zwischen Start und Akzeptanz / Startup versus acceptance

Der abgeschlossene META-LH-02-Vertrag erlaubt ausdrücklich den unveränderlichen
14-Ziele-Snapshot nach seinem dokumentarischen Delta. Der reparierte
`global-ready`-Dispatcher qualifiziert diesen Zustand über Abschluss, exakte
Historie, Ziele, Review-/Receipt-Bytes und beide Review-Oberflächen. Dieser
Start-Pass ist gültig, behauptet aber keine generische Source-Freshness. /
*The completed META-LH-02 contract explicitly accepts its immutable programme
snapshot after the documentary delta. The repaired dispatcher qualifies it
through completion, exact history, targets, receipt/review bytes and both
review surfaces. This valid startup pass does not claim generic source freshness.*

META-LH-03 AC-003 verlangt dagegen, dass alle 14 Receipts beide generischen
Receipt-Validatoren bestehen. Update bestehender Intakes und automatische
Review-Starts sind ausdrücklich außerhalb seines fachlichen Scopes. Eine
implizite Erneuerung würde diese Grenze überschreiten. / *AC-003 instead
requires all fourteen receipts to pass both generic receipt validators.
Updating existing intakes and starting their reviews are explicitly outside
this intake scope. Implicit renewal would cross that boundary.*

## Empfohlene begrenzte Freigabe / Recommended bounded approval

Separat autorisieren: Die Versionsreferenz von META-LH-03 an die bereits
installierte Version `0.3.1` angleichen; die drei betroffenen Receipts sowie den
dadurch und gegebenenfalls durch eigene Template-Änderungen betroffenen
META-LH-03-Receipt mit archivierten Vorgängern erneuern; vollständige aktuelle
Single-Re-Reviews ausführen und eine neue hashgebundene Auflösung der aktuellen
Evidence ergänzen. Den terminalen META-LH-02-Snapshot und sämtliche historischen
Evidence-Bytes dabei unverändert erhalten. / *Separately authorise aligning
META-LH-03 with the already installed version, renewing the three affected
receipts and META-LH-03 receipt with archived predecessors, full current Single
re-reviews, and a new hash-bound resolution of current evidence. Preserve the
terminal META-LH-02 snapshot and all historical evidence bytes.*

Keine Produktentscheidung, Preset-Installation/-Version, Level-0-, Promotion-
oder Bypass-Autorität wird daraus abgeleitet. Nach der begrenzten Reparatur
werden die akzeptierten Bindungen dieses einen Laufs formal erneuert; kein
zweiter Lauf beginnt. Ohne diese Freigabe bleiben Plan und Implementierung
gesperrt. / *This grants no product decision, preset installation/version,
level-0, promotion or bypass action. After approved repair, the accepted
bindings of this same run are formally renewed; no second run starts.
Without approval, planning and implementation stay blocked.*

Die einzige Dokumentationsentscheidung steht im
[Laufnachweis](autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact).
*The sole documentation decision is in the linked run evidence.*
