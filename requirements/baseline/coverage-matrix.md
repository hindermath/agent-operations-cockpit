# Coverage Matrix / Coverage Matrix

`Covered` bestätigt Requirements-Abdeckung, nicht Produktimplementierung oder
Wirksamkeit. Jede Quelle und jedes Finding steht genau einmal in einer eigenen
Zeile. / *`Covered` confirms requirements coverage, not product implementation
or effectiveness. Every source and finding has exactly one individual row.*

Die kontrollierten Tabellenwerte bedeuten in jeder Zeile `Covered`
(`Abgedeckt`), `Yes` (`Ja`), `No` (`Nein`) und `N/A` (`Nicht anwendbar`).
Englische Zielbezeichnungen erhalten eine deutsche Entsprechung; weitere
Fachbegriffe stehen im [Glossar](glossary.md). / *In every row, the controlled
table values mean `Covered`, `Yes`, `No`, and `N/A`; their German equivalents
are `Abgedeckt`, `Ja`, `Nein`, and `Nicht anwendbar`. English target labels
have a German equivalent; further specialist terms are in the
[glossary](glossary.md).*

## Quellenabdeckung / Source coverage

| ID | Meta-Owner / Meta owner | Fachliche Owner-Reihe / Domain owner series | Coverage | Direkt META-LH-01 / Direct META-LH-01 |
|---|---|---|---|---|
| SRC-156 | META-01 | RAW-01 bis RAW-09 / RAW-01 through RAW-09 | Covered | N/A |
| SRC-157 | META-01, META-02 | RAW-01 bis RAW-09 / RAW-01 through RAW-09 | Covered | N/A |
| SRC-159 | META-03, META-05 | RAW-08 | Covered | N/A |
| SRC-161 | META-01, META-02 | RAW-01 | Covered | N/A |
| SRC-162 | META-02, META-05 | RAW-02, RAW-06 | Covered | N/A |
| SRC-163 | META-01 | Keine eigene Reihe; Provenienz / No separate series; provenance | Covered | N/A |
| SRC-164 | META-01 | Keine eigene Reihe; Provenienz / No separate series; provenance | Covered | N/A |
| SRC-165 | META-01 | Keine eigene Reihe; Provenienz / No separate series; provenance | Covered | N/A |
| SRC-166 | META-01 | Keine eigene Reihe; Provenienz / No separate series; provenance | Covered | N/A |
| SRC-167 | META-01 | Keine eigene Reihe; Provenienz / No separate series; provenance | Covered | N/A |
| SRC-168 | META-01, META-05 | RAW-08, RAW-09 | Covered | N/A |
| SRC-169 | META-02, META-05 | RAW-04, RAW-07 | Covered | N/A |
| SRC-170 | META-01, META-05 | RAW-09 | Covered | N/A |
| SRC-171 | META-01, META-05 | RAW-07 | Covered | N/A |
| SRC-172 | META-02, META-05 | RAW-03, RAW-04 | Covered | N/A |
| SRC-173 | META-01, META-05 | RAW-07 | Covered | N/A |
| SRC-174 | META-02, META-05 | RAW-08, RAW-09 | Covered | N/A |
| SRC-175 | META-01, META-05 | RAW-07 | Covered | N/A |
| SRC-177 | META-01, META-02 | RAW-01, RAW-02, RAW-05 | Covered | N/A |
| SRC-180 | META-01, META-04 | Alle Reihen / All series | Covered | N/A |
| SRC-181 | META-01, META-05 | Nach Finding-Owner / By finding owner | Covered | N/A |
| SRC-182 | META-01 bis META-05 / META-01 through META-05 | RAW-01 bis RAW-09 / RAW-01 through RAW-09 | Covered | N/A |
| SRC-ES-01 | META-01 | De-Duplizierung und Begriffe / Deduplication and terminology | Covered | N/A |

## Findings-Abdeckung / Finding coverage

| ID | Meta-Owner / Meta owner | Fachliche Owner-Reihe / Domain owner series | Coverage | Direkt META-LH-01 / Direct META-LH-01 |
|---|---|---|---|---|
| RF-01 | META-01 | Quellenpaket / Source pack | Covered | Yes |
| RF-02 | META-04 | Autoritätsgates / Authority gates | Covered | No |
| RF-03 | META-03 | Authoring-Vertrag / Authoring contract | Covered | No |
| RF-04 | META-01 | DEC-001 | Covered | Yes |
| RF-05 | RAW-01 | Laufzeitentscheidungen / Runtime decisions | Covered | No |
| RF-06 | RAW-01 | RAW-03 | Covered | No |
| RF-07 | RAW-05 | Ausführungsknoten / Execution nodes | Covered | No |
| RF-08 | RAW-07 | Fähigkeitsschicht / Capability layer | Covered | No |
| RF-09 | META-02 | Ownership-Matrix / Ownership matrix | Covered | No |
| RF-10 | RAW-01 | RAW-03-Evidence-Plan / RAW-03 evidence plan | Covered | No |
| RF-11 | META-01 | Öffentliche Bereitschaft / Public readiness | Covered | Yes |
| RF-12 | META-01 | Quellenpaket / Source pack | Covered | Yes |
| RF-13 | META-01 | Phase-1-Provenienz / Phase-1 provenance | Covered | Yes |
| RF-14 | META-01 | Findings Ledger und Matrix / Findings ledger and matrix | Covered | Yes |
| RF-15 | META-01 | Level-2-Leserpfad / Level-2 reader path | Covered | Yes |
| RF-16 | META-01 | META-01 bis META-05 / META-01 through META-05 | Covered | Yes |
| RF-17 | META-01 | Alle Reihen / All series | Covered | Yes |
| RF-18 | META-04 | Eignungsmatrix / Eligibility matrix | Covered | No |
| RF-19 | META-04 | ProviderFailure-Evidence / Provider-failure evidence | Covered | No |
| RF-20 | META-03 | Authoring-Hooks / Authoring hooks | Covered | No |
| RF-21 | META-01 | Source Pack und Provenienz / Source pack and provenance | Covered | Yes |

Keine blocking Zeile ist `Uncovered`. Die direkte META-LH-01-Menge umfasst
exakt RF-01, RF-04, RF-11, RF-12, RF-13, RF-14, RF-15, RF-16, RF-17 und RF-21.
/ *No blocking row is `Uncovered`. The direct META-LH-01 set contains exactly
the ten named findings.*

Weiter im Leserpfad: [Glossar](glossary.md). / *Continue with the glossary.*
