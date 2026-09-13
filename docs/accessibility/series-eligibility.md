# Zugänglichkeit der Series-Prüfung / Series Eligibility Accessibility

## Umgebung, Methode und Grenze / Environment, method and limits

`manual:accessibility`, T034/T037, 2026-09-13. Reviewer: Codex, lokale semantische Review-Rolle; Owner: AOC Repository Owner. Tatsächliche Umgebung: macOS 26.6.2 arm64, Bash 5.3.15, PowerShell 7.6.5, Python 3.14.7, Pandoc 3.10.2 und macOS `mandoc`. [Quality-Evidence](../../specs/004-series-eligibility/phase-results/quality-validation.json) enthält Quellhashes, Befehle, Exits und beobachtete Ausgaben. / *Actual local semantic review using the named environment; source bindings and command evidence are recorded in the linked result.*

Gelesen wurden die tatsächliche Klartextausgabe der gültigen und der Shared-write-Fixture sowie der Series-Next-Abfrage, Bash-Hilfe, PowerShell-Hilfe und dot-gesourcte Funktion. Der [Quickstart](../../specs/004-series-eligibility/quickstart.md) wurde mit `pandoc -f gfm -t plain --wrap=auto --columns=88` gerendert; die [Manpage](../man/validate-series-eligibility.1) mit `mandoc -T utf8`. Die gerenderten Textabschnitte zu Einstieg, Parametern, Modi, Kriterien, Exits und nächster Aktion wurden semantisch gelesen. / *The reviewer read actual successful/blocked/query output and help/function output, plus the rendered plain-text reader path and manual, checking meaning in the named sections.*

Zusätzlich erzeugtes Pandoc-HTML ist nur strukturelle Evidence. Ein Browserreview gelang nicht: lokale Datei-URL gesperrt, localhost-Bindung durch Sandbox abgelehnt, HTML-Inhaltsladung durch automatische Freigabeprüfung abgelehnt (`approval policy is never`). Kein Browser-, Tastatur-, VoiceOver-, NVDA-, JAWS- oder vollständiger WCAG-Konformitätspass wird behauptet. Dies begrenzt die Nachweismethode; es ersetzt keinen fehlenden Assistenztechniktest. / *HTML generation is structural evidence only. File navigation, localhost binding and content loading were blocked by the environment/approval policy. No browser, keyboard, screen-reader or full WCAG conformance pass is claimed.*

## Beobachtungen am Leserpfad / Reader-path observations

Der Einstieg nennt Zielgruppe, lokale Voraussetzungen und die Grenze „Eignung ist keine Startfreigabe“. Fixture, Manifest, Kriterium und Receipt werden vor der vertieften Nutzung erklärt. Deutsch steht jeweils vor gleichwertigem Englisch. Fachbegriffe bleiben durch Codebezeichner eindeutig, ihre Bedeutung wird erklärt. Die Sätze sind auf CEFR B2 ausgerichtet; eine menschliche Verständlichkeitsstudie fand nicht statt. / *The entry states audience, prerequisites and authority bounds, defines terms, and pairs German with equivalent English. Wording targets B2; no human comprehension study was performed.*

Die gültige Fixture zeigt alle neun Kriterien in kanonischer Reihenfolge. Die Shared-write-Fixture zeigt zusätzlich einen textuellen Grund. Beide enden mit genau einer sicheren nächsten Aktion und „Keine Startfreigabe“. Die Series-Abfrage zeigt keine Kriterienbewertung (`criteria={}`), weil sie den Manifestzustand projiziert; diese Abwesenheit wird nicht als neun bestandene Kriterien gewertet. / *The valid fixture shows nine ordered criteria; the shared-write fixture adds its textual blocker. Both have one action and a no-authority statement. A series query projects the manifest and does not claim nine assessed criteria.*

Die beobachtete Series ist deklariert `Completed`, hat null Kandidaten, Review/Delivery `NotAssessed` und historische Receipt-Herkunft `HistoricalOnly`. Der Text erklärt getrennt, dass dies den aktuellen autonomen Lauf nicht beendet. `Blocked` mit Exit 0 ist ein gültiges fachliches Ergebnis; Exit 2/3 und `ProductFailure`/`ProviderFailure` sind erklärt. Es gibt keine allein farbige oder grafische Information. / *Observed series lifecycle, zero candidates, unassessed fields and historical provenance stay separate from autonomous completion. Domain results and process exits are explained without colour-only information.*

Nichttriviale Codekommentare wurden ebenfalls gelesen: Duplicate Keys vor Dictionary-Verlust, Containment vor Linkfolge, isolierte Engine-Reader und Ergebnisbildung vor Erwartungsvergleich. Die DE/EN-Kommentare erklären den Grund der Grenze; sie behaupten keine zusätzliche Autorität oder Plattformabnahme. / *The reviewed bilingual code comments explain duplicate detection, containment, isolated readers and classification before assertion, without inventing authority or native acceptance.*

## WCAG-Disposition / WCAG disposition

Anwendbarkeit, Umsetzung und Prüfgrenze bleiben getrennt. Owner/Reviewer wie oben. `Fulfilled` gilt nur für den benannten Text-/Quellreview; eine Browser- oder AT-Abnahme folgt daraus nicht. / *Applicability, implementation and proof scope remain separate. Fulfilled is limited to the reviewed text/source behavior, not browser or assistive-technology acceptance.*

| Kriterium / Criterion | Anwendbarkeit / Applicability | Umsetzung und tatsächlicher Befund / Implementation and observation |
|---|---|---|
| 1.3.1 Info and Relationships | Applicable | Fulfilled im Text-/Strukturreview: Überschriftenhierarchie, Tabellenköpfe und beschreibende Links; HTML-DOM/AT nicht beobachtet. / Headings, headers and descriptive links; DOM/AT unobserved. |
| 1.3.2 Meaningful Sequence | Applicable | Fulfilled: Einstieg → Voraussetzungen → Parameter/Modi → Evidence → eine Aktion; DE vor EN, neun Kriterien und Blocker geordnet. / Meaningful reading and criterion order. |
| 1.4.1 Use of Color | Applicable | Fulfilled: Erfolg, Sperre und Gründe sind benannt; aktuelle CLI ohne ANSI-Farben. / Explicit textual status/reasons, no ANSI colours. |
| 2.4.4 Link Purpose | Applicable für Dokumentlinks / for document links | Fulfilled im Quell-/Textreview: Spec, Manpage, Schnittstellenvertrag, Datenmodell, Security und A11Y sind beschreibend. Lokale Ziele strukturell geprüft; keine Browser-Linknavigation behauptet. / Descriptive checked local targets; no claimed browser navigation. |
| 2.4.6 Headings and Labels | Applicable | Fulfilled im Textreview: Zweck, Optionen, Ergebnisse, Modi und Grenzen sind benannt; Parameter entsprechen dem echten Aufruf. / Meaningful headings and actual parameter labels. |
| 3.1.1 Language of Page | N/A für CLI/man-Klartext; Applicable bei HTML / plain text versus HTML | Not Assessed für Browser: Markdown allein garantiert kein `lang`; Preview wurde mit `lang=de` erzeugt, aber nicht im Browser abgenommen. / Metadata generation does not prove browser behavior. |
| 3.1.2 Language of Parts | N/A für CLI/man-Klartext; Applicable bei HTML / plain text versus HTML | Partly Fulfilled: DE/EN visuell/textuell bezeichnet; automatisch erzeugte englische Absätze besitzen keine verifizierte AT-Sprachumschaltung. / Bilingual labeling is not verified AT language switching. |

## Offene Nachweise und nächste Aktion / Open evidence and next action

Native Help-/Funktionsprüfungen für Linux, Windows und den konkreten `macos-14`-Provider fehlen bis T048. Der lokale macOS-Host ersetzt diese Matrix nicht. Der [Plattformreview](../../specs/004-series-eligibility/checklists/cross-platform.md) führt jede Kombination einzeln. / *Actual provider-platform help/function evidence remains open per matrix row; this local host does not substitute for CI runners.*

Restrisiken: lange JSON-Lifecycle-Zeilen und breite Klartexttabellen sind linear lesbar, auf kleinen Ansichten aber umständlich. Zeilenumbruch und maschinenlesbare JSON-Ausgabe sind Alternativen, keine getestete AT-Lösung. Owner prüft Browser-Sprachmarkierung, Tastatur-/Screenreader-Navigation und Reflow bei konkreter HTML-Veröffentlichung oder Zielumgebungsänderung; bis dahin bleibt dieser Nachweis ausdrücklich offen. / *Long JSON lines and wide text tables are readable sequentially but awkward in narrow views. Wrapping/JSON are alternatives, not proven AT solutions. The owner reassesses language tagging, navigation and reflow when HTML publication or target environment changes.*

Bilder, Audio/Video, Formulare und interaktive Produkt-UI: `N/A / Not Assessed`, nicht vorhanden. Trigger: neue Darstellungsfläche; dann Kriterien neu zuordnen. / *Media, forms and interactive product UI are absent and require reassessment when introduced.*

Nächste sichere Aktion: Die gültige lokale Fixture aus dem Quickstart lesend prüfen. / *Next safe action: assess the valid local quickstart fixture read-only.*
