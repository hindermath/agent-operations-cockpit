# AOC Assurance v0.1.3: Evidence-Matrix / Evidence matrix

## Prüfgrenze / Verification boundary

Dies ist ein technischer Governance-Feldtest der Installation, Baseline-Bindung,
Autoritätsgrenzen und Gate-Verarbeitung. AOC besitzt noch keinen freigegebenen
Produkt-Scaffold. Die 30 Dokumentbewertungen in baseline.json bestätigen nur
vorhandene, versionierte, hashgebundene Quellen; sie sind keine Aussage, dass
alle 157 Sicherheitsmaßnahmen in einem Produkt umgesetzt sind.

*This technical governance field test covers installation, baseline integrity,
authority separation and gate processing. AOC has no approved product scaffold.
The 30 document assessments concern source integrity, not implementation of all
157 controls in a product.*

| Gate | Anwendbarkeit / Applicability | Gegenstand / Subject | Nachweis / Evidence |
|---|---|---|---|
| Baseline | Applicable | 30 kontrollierte Quellen, 12 Checklisten / controlled sources | baseline.json and baseline-manifest.json |
| Delta | Applicable | Assurance als 13. Preset; keine Produktänderung / preset installation only | deltas/preset-v013.json; scoped Git diff |
| Closure | Applicable | Vier getrennte Entscheidungen / separate decisions | closure.json |
| Image impact | N/A | Kein Image gebaut oder verändert / no image change | image-impact.json |
| Produkt-Restore/Build/Test/TUI / Product checks | N/A | Kein genehmigter Produkt-Scaffold / no approved product scaffold | README.md; public-readiness workflow |
| CL-02-13 / C5 | N/A | Kein Cloud-Produktservice im Ausbildungs-Scope / no cloud product service | Owner-approved scope; review 2026-12-31 |

## Ausbildung und Autorität / Education and authority

AOC ist wie TinyCalc, TinyPl0, InventarWorkerService, absdd-image-sandbox,
TuiVision und home-baseline ein nichtproduktives, nichtkommerzielles
Ausbildungs- und Referenzprojekt. Zielgruppen: Fachinformatiker*innen aller vier
Fachrichtungen, IT-System-Elektroniker*innen, Kaufleute für IT-System-Management
und für Digitalisierungsmanagement. Sichere KI-gestützte Entwicklung beginnt
ab Lehrjahr 1 mit begrenzten Rechten, Geheimnisschutz, verständlichen Änderungen,
Tests und begründeten menschlichen Entscheidungen. Didaktische Tiefe wächst;
Schutz realer Dateien und Zugangsdaten wird nicht reduziert.

*All seven are non-production, non-commercial educational/reference projects
for the four IT training occupations, including all four IT specialist tracks.
Secure AI-assisted development starts in year one. Explanatory depth grows,
while real files, credentials and permission boundaries stay protected.*

Der globale 14-Intake-Review-Vertrag bleibt unverändert. Der lesende Preflight
auf Base-HEAD 17df5332f4d4b6923b1596e11ebfb56d2629a5cc bestand; daraus folgt
kein neuer Startauftrag. Kein Specify-, Autonomous-, Implementierungs-,
Produkt- oder Image-Lauf gehört zu diesem Feldtest.
Technische Wiedervorlage: 2027-09-09. Scope-Wiedervorlage: 2026-12-31,
früher bei relevantem Nutzungswechsel. Keine neue rechtliche Freistellung,
Pilot-, Produkt-, allgemeine Freigabe oder Zertifizierungsentscheidung.

*The unchanged global fourteen-intake gate passed the read-only baseline
preflight; this does not start a new lifecycle run. Technical review is due
2027-09-09; scope review 2026-12-31 or earlier on scope change. No legal
exemption, human approval or certification is inferred.*

Nächste Aktion / Next action: AOC-Feldtest abschließen, Findings prüfen und
begrenzt veröffentlichen / complete the scoped field test, review and publish.
