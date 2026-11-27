# RAW-01 · Regulatorische Anwendbarkeit / Regulatory applicability

**Stand / As of** 2026-11-27

**Anwendungsrahmen / Review scope** Deutschland und EU als Prüfreferenz / Germany and EU as the review reference

**Verantwortung / Owner** AOC-Maintainer als Nachweis-Owner. Der konkrete
Betreiber und seine qualifizierte Prüfstelle sind vor Betrieb oder
Veröffentlichung zu benennen. / AOC maintainer owns the record. Identify
the actual operator and its qualified reviewer before operation or release.

## Geltungsprüfung / Applicability screen

Die Aussagen gelten für den lokalen RAW-01-Spezifikationsumfang. Ein
Produkthersteller, KI-Anbieter, regulierter Kunde oder Finanzdienstleister
ist für diesen Umfang nicht benannt. Die drei Spalten unterscheiden das
Referenzprodukt, die Entwicklungswerkzeuge und eine spätere nutzende
Organisation. Vertragliche Pflichten sind im Specify-Auftrag nicht belegt
und müssen bei einer entsprechenden Nutzung gesondert ermittelt werden.

The findings cover the local RAW-01 specification scope. No product
manufacturer, AI provider, regulated customer or financial entity has been
identified for this scope. The columns distinguish the reference product,
development tooling and a future operating organisation. The Specify request
provides no evidence of contractual obligations. Assess any such obligations
when a concrete use case arises.

| Regel und zeitlicher Bezug / Instrument and timing | Referenzprodukt / Reference product | Entwicklungswerkzeuge / Development tools | Nutzende Organisation / Operating organisation |
|---|---|---|---|
| [DS-GVO / GDPR · VO (EU) 2016/679, 27.04.2016](https://eur-lex.europa.eu/eli/reg/2016/679) · anwendbar seit / applies from 25.05.2018 | **Applicable** als Entwurfsprüfung. Repository-Metadaten und opake Kennungen können je nach Kontext einer Person zuordenbar sein. FR-007 begrenzt Umfang und Ausgabe. / Design screen applies because metadata and opaque identifiers may be linkable to people in context. | **Applicable** als Entwicklungsgrenze. Synthetische Testdaten verwenden. Private Workspace-Daten aus Prompts, Logs und Testnachweisen heraushalten. / Use synthetic test data and exclude private workspace data from prompts, logs and evidence. | **Open.** Rollen, Rechtsgrundlage, Empfänger, Aufbewahrung und Betroffenenrechte vor Nutzung mit realen Daten klären. / Resolve roles, legal basis, recipients, retention and data-subject rights before use with real data. |
| [KI-VO / AI Act · VO (EU) 2024/1689, 13.06.2024, Art. 113](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) · gestaffelte Anwendung / phased application | **N/A** für RAW-01. Der lokale Snapshot-Vertrag hat keine KI-Systemfunktion. Neu bewerten bei Aufnahme einer KI-Funktion. / The local snapshot contract contains no AI-system functionality. Reassess if AI is added. | **Open** für konkrete Nutzung. KI-Assistenz dient der Entwicklung. Betreiberrolle, zulässige Eingaben und betriebliche Vorgaben beim Tool-Einsatz prüfen. / AI assistance is development tooling. Review deployer role, permitted input and operating rules for actual tool use. | **Open** bis Zweck, Rolle und eingesetztes KI-System für eine konkrete Organisation feststehen. / Open until purpose, role and system are known for a specific organisation. |
| [CRA · VO (EU) 2024/2847, 23.10.2024, Art. 71](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) · Meldepflichten ab / reporting from 11.09.2026, Hauptpflichten ab / main obligations from 11.12.2027 | **N/A** für Specify. Bei Bereitstellung eines Produkts auf dem EU-Markt Herstellerrolle, Anwendungsbereich und Ausnahmen prüfen. / Reassess manufacturer role, scope and exclusions before placing a product on the EU market. | **N/A** für den derzeitigen lokalen Spezifikationslauf. Auswahl und Übernahme von Abhängigkeiten löst AC-009 aus. / The local specification step adds no distributed tooling. AC-009 applies at dependency adoption. | **Open** bis Betreiber-, Hersteller- oder Vertriebsrolle und Lieferkette bekannt sind. / Open until operator, manufacturer or distribution role and supply chain are known. |
| [NIS2 · RL (EU) 2022/2555, 14.12.2022, Art. 41](https://eur-lex.europa.eu/eli/dir/2022/2555) · EU-Umsetzungsfrist / EU transposition deadline 17.10.2024 | **N/A** für den lokalen Vertrag. Kein Dienst für einen benannten regulierten Sektor. / The local contract defines no service for an identified regulated sector. | **N/A** für den Specify-Schritt. Bei Lieferantenbindung für einen regulierten Betreiber neu prüfen. / Reassess supplier dependencies for a regulated operator. | **Open.** Sektor, Größe, Mitgliedstaat, nationales Recht und Lieferkettenrolle vor dem Einsatz prüfen. / Determine sector, size, jurisdiction, national law and supply-chain role before deployment. |
| [DORA · VO (EU) 2022/2554, 14.12.2022, Art. 64](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · anwendbar seit / applies from 17.01.2025 | **N/A** für den lokalen Vertrag. Eine Rolle im Finanzsektor ist nicht Teil des spezifizierten Einsatzes. / The local contract defines no financial-sector role. | **N/A** für Specify. Neu bewerten, wenn Werkzeuge Teil einer regulierten IKT-Dienstleistung werden. / Reassess if tools become part of a regulated ICT service. | **Open.** Vor einem Finanzsektoreinsatz Unternehmen, IKT-Dienst, Vertrag und Lieferantenrolle prüfen. / Before financial-sector use, assess the entity, ICT service, contract and provider role. |

## Datenfluss und nächste Prüfung / Data flow and next review

Der Vertrag liest Git- und Werkzeugmetadaten innerhalb expliziter Wurzeln.
Er liefert eine lokale Ausgabe mit minimierten Daten. Automatische
Speicherung, externe Empfänger, Fernzugriff und Telemetrie gehören nicht zum
Vertrag. Werden Speicherung, neue Datenkategorien, Empfänger oder
Dienstanbieter eingeführt, sind Zweck, Löschung, Regionen und Rechte neu zu
bewerten. Die Prüfung fällt dem AOC-Maintainer und dem qualifizierten
Verantwortlichen des tatsächlichen Betreibers zu. Sie ist vor Einsatz realer
Daten, vor einem regulierten Einsatz oder vor Veröffentlichung fällig,
je nachdem, welcher Trigger zuerst eintritt.

The contract reads Git and tool metadata within explicit roots and returns
minimised local output. Automatic storage, external recipients, remote access
and telemetry are outside the contract. Reassess purpose, deletion, regions
and rights if adding persistence, data categories, recipients or providers.
The AOC maintainer and the actual operator's qualified reviewer own that
review. Complete it before real-data use, regulated deployment or publication,
whichever trigger comes first.

[Vertragsgrenzen / Contract boundaries](../../specs/005-reference-agentic-workspace/spec.md)
