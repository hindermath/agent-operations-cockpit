# test-requirements-intake-governance(1)

## Name

`test-requirements-intake-governance` — prueft die verlinkte Intake-Reihenfolge

*tests the linked intake-order projection*

## Synopsis

```bash
bash scripts/test-requirements-intake-governance.sh
bash scripts/test-requirements-intake-governance.sh --help
```

```powershell
pwsh -NoProfile -File scripts/test-requirements-intake-governance.ps1
Get-Help ./scripts/test-requirements-intake-governance.ps1 -Full
```

## Beschreibung / Description

Die Bash- und PowerShell-7-Tests erzeugen isolierte temporaere Repositories aus
`scripts/tests/linked-intake-evidence/positive/` und `negative/`. Sie rufen die
echten Bibliotheksfunktionen `sdh_build_order_section` und
`Get-SdhOrderSection` auf. Geprueft werden die fuenf Spalten, vollstaendige
Intake-Dateinamen, sichere Root- und Series-relative Links, null/eine/mehrere
direkte eingehende Kanten, literales `kind`/`binding`, eindeutige
Feature-Evidence, der exakte Fallback und Metadatenposition 39 bei
Manifestplatz 1. Zusaetzlich pruefen sie `LIE001` bis `LIE012`, alle sieben
Feature-Proof-Faelle, Check/Write, Recheck der vollstaendigen Eingabemenge,
Containment, Input-/Output-Overlap, atomaren Multi-Output-Rollback,
Null-Write-Idempotenz, Markdown-Escaping und LF-Ausgabe.

*The Bash and PowerShell 7 tests create isolated temporary repositories from
`scripts/tests/linked-intake-evidence/positive/` and `negative/`. They call the
real `sdh_build_order_section` and `Get-SdhOrderSection` library functions. The
tests cover five columns, complete intake filenames, safe root- and
series-relative links, zero/one/multiple direct incoming edges, literal
`kind`/`binding`, unique feature evidence, the exact fallback, and metadata
position 39 at manifest slot 1. They also cover `LIE001` through `LIE012`, all
seven feature-proof cases, check/write, complete-input and containment rechecks,
input/output overlap, atomic multi-output rollback, zero-write idempotence,
Markdown escaping, and LF output.*

## Sicherheit und Nebenwirkungen / Safety and Side Effects

Die Tests schreiben nur unter einem durch das Betriebssystem erzeugten
Temporaerverzeichnis und entfernen dieses beim Beenden. Das aktuelle
Repository, sein Index, seine Views und andere Repositories werden nicht
veraendert. `jq` wird fuer die bereits etablierten JSON-Fixtures im Bash-Test
verwendet; der PowerShell-Test nutzt `ConvertFrom-Json`.

*The tests write only below an operating-system-created temporary directory
and remove it on exit. They do not change the current repository, its index,
its views, or other repositories. The Bash test uses the already established
`jq` JSON dependency; the PowerShell test uses `ConvertFrom-Json`.*

## Exitcodes / Exit Codes

- `0`: Alle Vertragsassertions sind erfuellt. / All contract assertions pass.
- `1`: Mindestens eine fachliche Assertion ist fehlgeschlagen. / At least one semantic assertion failed.
- `2`: Der Bash-Aufruf enthielt eine unbekannte Option. / The Bash invocation used an unknown option.

## Naechster Schritt / Next Step

Bei einem Fehler zuerst die ausgegebene Vertragsabweichung korrigieren und
beide Shelltests erneut ausfuehren. Native Windows-Evidence wird durch einen
macOS-PowerShell-Lauf nicht ersetzt.

*On failure, first correct the reported contract mismatch and rerun both shell
tests. A macOS PowerShell run does not replace native Windows evidence.*
