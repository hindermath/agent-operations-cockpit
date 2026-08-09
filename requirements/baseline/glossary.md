# Glossargrundlage DE/EN / Bilingual Glossary Baseline

Die kurzen Erklärungen setzen keine Erfahrung mit Spec Kit, dem Werkzeug für
spezifikationsgeleitete Entwicklung, voraus. / *The short explanations assume
no prior experience with Spec Kit, the tool for specification-driven
development.*

| Deutsch | English | Erklärung / Explanation |
|---|---|---|
| Autorität | authority | Nachweisbare und begrenzte Erlaubnis, Daten zu lesen oder eine bestimmte Aktion auszuführen. / Verifiable and bounded permission to read data or perform a specific action. |
| A11Y | accessibility | Kurzform für Barrierefreiheit; die Zahl 11 steht für die ausgelassenen Buchstaben. / Short form for accessibility; 11 counts the omitted letters. |
| ADE | agentic development environment | Entwicklungsumgebung, in der Menschen und Software-Agenten nachvollziehbar zusammenarbeiten. / Development environment in which people and software agents collaborate traceably. |
| AEPS | Agentic Engineering Preset System | Verfahren, das lokale Engineering-Evidence erfasst, ohne daraus automatisch Preset- oder Level-0-Autorität abzuleiten. / Process that captures local engineering evidence without automatically granting preset or level-0 authority. |
| Analyze | analysis gate | Spec-Kit-Prüfung auf Widerspruchsfreiheit und geschlossene Findings vor der Umsetzung. / Spec Kit gate checking consistency and closed findings before implementation. |
| AOT | ahead-of-time compilation | Übersetzung eines Programms vor seiner Ausführung statt erst während des Laufs. / Translation of a program before execution rather than while it runs. |
| Allowlist | allowlist | Abschließende Liste der Pfade oder Aktionen, die ausdrücklich erlaubt sind. / Exhaustive list of paths or actions explicitly allowed. |
| Authoring Receipt | authoring receipt | Hashgebundener Nachweis, welche Eingabe welches Lastenheft erzeugt hat. / Hash-bound proof of which input produced an intake. |
| Bootstrap | bootstrap | Minimaler, noch produktneutraler Einstieg zum Anlegen eines Arbeitsbereichs. / Minimal, still product-neutral entry for creating a workspace. |
| CEFR B2 | CEFR B2 | Sprachniveau des Gemeinsamen Europäischen Referenzrahmens für selbstständiges Verstehen klarer Fachtexte. / Language level of the Common European Framework for independently understanding clear technical texts. |
| CI | continuous integration | Automatische Prüfung von Änderungen in einer gemeinsamen Integrationsumgebung. / Automated checking of changes in a shared integration environment. |
| CLI | command-line interface | Textbasierte Befehlsschnittstelle. / Text-based command interface. |
| Concern | concern | Abgegrenztes fachliches Thema, für das genau eine Owner-Reihe verantwortlich ist. / A bounded domain topic for which exactly one owner series is responsible. |
| CWE | Common Weakness Enumeration | Öffentlicher Katalog typischer Schwachstellenklassen. / Public catalogue of common weakness classes. |
| DAG | directed acyclic graph | Gerichteter Graph ohne Zyklus; Abhängigkeiten führen nicht zum Ausgangspunkt zurück. / Directed graph without a cycle; dependencies do not lead back to their starting point. |
| Discovery | discovery | Read-only Ermittlung vorhandener Arbeitsbereiche, Repositories oder Fähigkeiten. / Read-only detection of available workspaces, repositories, or capabilities. |
| Domain-Vertrag | domain contract | Maschinenprüfbarer Vertrag für Anzahl, Felder und Beziehungen der Baseline-Daten. / Machine-checkable contract for counts, fields, and relationships of the baseline data. |
| Capability | capability | Abstrakte Fähigkeit wie „Status anzeigen“, unabhängig von einem konkreten Gerät. / An abstract ability such as showing status, independent of a specific device. |
| Capability-Vertrag | capability contract | Herstellerneutraler Vertrag für eine Fähigkeit und ihre Ein- und Ausgaben. / Vendor-neutral contract for a capability and its inputs and outputs. |
| Coverage | coverage | Nachvollziehbare Zuordnung einer Quelle oder eines Findings zu Owner, Ziel und Status; sie beweist keine Umsetzung. / Traceable mapping of a source or finding to its owner, target, and status; it does not prove implementation. |
| Decision | decision | Ausdrücklich bestätigte Festlegung; nur eine neue Decision mit Revisionsgrund kann sie ablösen. / An explicitly confirmed choice; only a new decision with a revision rationale can supersede it. |
| Decision Intake | decision intake | Strukturierte Vorlage für eine noch offene, menschlich zu bestätigende Entscheidung. / A structured template for an open decision that a human must confirm. |
| Degraded Mode | degraded mode | Nutzbarer, aber eingeschränkter Zustand mit sichtbarer Ursache und Grenze. / A usable but limited state with a visible cause and boundary. |
| Evidence | evidence | Prüfbarer positiver oder negativer Nachweis zu einer Anforderung. / Verifiable positive or negative proof for a requirement. |
| Eligibility | eligibility | Nachgewiesene Eignung eines Ziels für einen bestimmten Ausführungsmodus. / Demonstrated suitability of a target for a particular execution mode. |
| Exact-SHA-Receipt | exact-SHA receipt | Nachweis, der sich auf genau einen Git-Inhaltsstand bezieht. / Evidence bound to exactly one Git content state. |
| Field Evidence | field evidence | Beobachtung aus einem realen Geräte- oder Nutzungstest, nicht automatisch ein Architekturvertrag. / Observation from a real device or usage test, not automatically an architecture contract. |
| Fixture | fixture | Kontrollierte Testeingabe für einen positiven oder negativen Fall. / Controlled test input for a positive or negative case. |
| Freshness | freshness | Nachvollziehbares Alter und Aktualitätsniveau eines Zustands. / Traceable age and currency level of a state. |
| Handoff | handoff | Explizite Übergabe von Daten, Vertrag oder Verantwortung zwischen Owner-Reihen. / Explicit transfer of data, a contract, or responsibility between owner series. |
| GUI | graphical user interface | Grafische Bedienoberfläche. / Graphical user interface. |
| Global-ready | global-ready | Gesamtprüfung, dass alle 14 gebundenen Lastenhefte gleichzeitig aktuelle Ready-Evidence besitzen. / Aggregate check that all 14 bound intakes simultaneously have current Ready evidence. |
| Happy Path | happy path | Erfolgsfall ohne absichtlich eingebrachte Störung; er genügt allein nicht als Testabdeckung. / Success case without an injected fault; by itself it is insufficient test coverage. |
| IPC | inter-process communication | Strukturierter Datenaustausch zwischen getrennten Prozessen. / Structured data exchange between separate processes. |
| JSON | JavaScript Object Notation | Textformat für strukturierte Daten. / Text format for structured data. |
| Level 0 / Level 2 | level 0 / level 2 | Level 0 ist die zentrale Basisquelle; Level 2 ist das konkrete Referenzprojekt mit lokaler Evidence. / Level 0 is the central baseline source; level 2 is the concrete reference project with local evidence. |
| MSL | memory-safe language | Programmiersprache mit Schutz vor typischen unsicheren Speicherzugriffen. / Programming language that protects against common unsafe memory access. |
| Multi-Device-Steuerung | multi-device control | Koordination mehrerer Eingabe- oder Ausgabegeräte über gemeinsame Capability-Verträge. / Coordination of multiple input or output devices through shared capability contracts. |
| NIST SSDF | NIST Secure Software Development Framework | Öffentlicher Rahmen für sichere Softwareentwicklung. / Public framework for secure software development. |
| Pre-Rename-Fixpunkt | pre-rename fixed point | Byte-stabiler geprüfter Kandidat unmittelbar vor der späteren Intake-Umbenennung. / Byte-stable checked candidate immediately before the later intake rename. |
| Lastenheft | requirements intake | Beschreibt Bedarf, Grenzen und messbare Ergebnisse, nicht die technische Umsetzung. / Describes needs, boundaries, and measurable outcomes, not technical implementation. |
| Owner-Reihe | owner series | Einzige kanonische Reihe, die ein abgegrenztes fachliches Thema, einen Concern, definiert und ändert. / The sole canonical series that defines and changes a bounded domain topic, a concern. |
| Presentation Fabric | presentation fabric | Gemeinsamer Vertrag für digitale und physische Darstellungsflächen. / Shared contract for digital and physical presentation surfaces. |
| ProductFailure / ProviderFailure | product failure / provider failure | Fehler im Produkt beziehungsweise Fehler eines externen Dienstes oder Ausführungsanbieters; beide Klassen bleiben getrennt. / Product defect versus failure of an external service or execution provider; the classes remain separate. |
| Program Charter | programme charter | Verbindliche Beschreibung von Zweck, Zielbild und Grenzen des Programms. / Binding description of the programme's purpose, target vision, and boundaries. |
| Provenienz | provenance | Nachvollziehbare Herkunft eines Inhalts oder Nachweises. / Traceable origin of content or evidence. |
| Raw MIDI | raw MIDI | Unverarbeitete gerätespezifische MIDI-Nachricht, die nur in einem dünnen Adapter bleibt. / Unprocessed device-specific MIDI message that remains only in a thin adapter. |
| Regex-Hook | regex hook | Automatische Prüfung mit einem Suchmuster für Text. / Automated check using a text-search pattern. |
| Ruleset | ruleset | Regeln des Repository-Anbieters, die zum Beispiel geschützte Branches und Prüfungen steuern. / Repository-provider rules controlling such things as protected branches and checks. |
| Runtime / Target Framework | runtime / target framework | Ausführungsumgebung beziehungsweise konkrete Bibliotheks- und Plattformversion für ein Programm. / Execution environment and the specific library and platform version for a program. |
| Laufzeitabhängigkeit | runtime dependency | Datei, Dienst oder Wissen, das während der Ausführung zwingend verfügbar sein muss. / File, service, or knowledge that must be available during execution. |
| SHA / Hash | SHA / hash | Prüfsumme, die einen konkreten Datei- oder Git-Inhaltsstand bindet. / Checksum binding a concrete file or Git content state. |
| Projektion | projection | Darstellung derselben kanonischen Zustandsdaten in einem Ausgabeformat. / Representation of the same canonical state data in an output format. |
| Receipt | receipt | Maschinen- oder menschenlesbarer Nachweis mit Scope, Eingabebindung, Ergebnis und Revision. / Machine- or human-readable evidence with scope, input binding, result, and revision. |
| Recovery | recovery | Geordnete Wiederaufnahme oder Rückkehr in einen sicheren Zustand nach Abbruch. / Controlled resumption or return to a safe state after interruption. |
| Series | series | Geordnete Menge von Lastenheften mit expliziten Abhängigkeiten und Status. / Ordered set of requirements intakes with explicit dependencies and status. |
| Side Effect | side effect | Beobachtbare Änderung außerhalb einer reinen Abfrage. / Observable change beyond a read-only query. |
| Snapshot | snapshot | Zeitlich gebundene, unveränderliche Sicht auf erkannten Zustand. / Time-bound immutable view of detected state. |
| State Truthfulness | state truthfulness | Vertrag, erkannte Zustände mit Quelle, Alter und Unsicherheit wahrheitsgemäß darzustellen. / Contract to represent detected state truthfully with source, age, and uncertainty. |
| Stop-Gate | stop gate | Sicher geschlossene Bedingung (fail-closed): Bei fehlender oder veralteter Evidence darf Arbeit nicht automatisch fortgesetzt werden. / Safely closed condition (fail-closed): work must not continue automatically when evidence is missing or stale. |
| Supersession | supersession | Nachvollziehbare Ablösung durch eine ausdrückliche Decision mit Revisionsgrund; ein neueres Datum genügt nicht. / Traceable replacement by an explicit decision with a revision rationale; a newer date is insufficient. |
| Trust Boundary | trust boundary | Grenze, an der Daten oder Autorität aus einer anderen Vertrauenszone eintreten. / Boundary where data or authority enters from another trust zone. |
| TUI | text user interface | Interaktive textbasierte Oberfläche im Terminal. / Interactive text-based terminal interface. |
| Traceability | traceability | Nachvollziehbare Kette von Quelle über Anforderung und Owner bis zu Evidence. / Traceable chain from source through requirement and owner to evidence. |
| WCAG 2.2 AA | WCAG 2.2 AA | Prüfkriterien für wahrnehmbare, bedienbare, verständliche und robuste digitale Inhalte auf Konformitätsstufe AA. / Criteria for perceivable, operable, understandable, and robust digital content at conformance level AA. |
| Working Copy | working copy | Lokal ausgecheckter Arbeitsstand eines Repositories. / Locally checked-out state of a repository. |
| Workspace Orchestrator | workspace orchestrator | Komponente, die Zustandsabfragen und ausdrücklich autorisierte Abläufe über Arbeitsbereiche koordiniert. / Component coordinating state queries and explicitly authorised workflows across workspaces. |
| WSL | Windows Subsystem for Linux | Linux-Ausführungsumgebung innerhalb von Windows. / Linux execution environment within Windows. |
| Unknown / Stale / Unavailable | unknown / stale / unavailable | Nicht bekannt / nicht ausreichend aktuell / derzeit nicht erreichbar. / Not known / not current enough / currently unreachable. |
| Vertical Slice | vertical slice | Kleiner durchgängiger Funktionsausschnitt über die notwendigen Schichten. / Small end-to-end functional slice across the required layers. |

Weiter im Leserpfad: [Authority- und Stop-Gates](authority-and-stop-gates.md). /
*Continue with the authority and stop gates.*
