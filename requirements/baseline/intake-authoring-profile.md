# AOC Intake Authoring Project Profile

## Identity

- Profile ID: `aoc-bilingual-requirements`
- Applies when: AOC Meta- oder fachliches Lastenheft / AOC meta or domain intake
- Target path rule: `requirements/intakes/active/Lastenheft_<slug>.md`
- Language rule: Deutsch zuerst autoritativ; vollständiges konsistentes Englisch danach oder paarweise DE/EN.
- Declared learner audience: IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte.
- Assumed prior knowledge: allgemeine IT-Grundlagen; keine Spec-Kit- oder Projektgeschichte.
- First-use terminology rule: erklären oder `requirements/baseline/glossary.md` referenzieren.
- Text-first rule: Abhängigkeiten, Status, Decisions und nächste Aktion immer als geordneter Text.
- URL-source rule: nur explizit benannte öffentliche HTTPS-Quellen; kein Crawl ohne Freigabe.
- Series rule: stabile ID, SHA-gebundenes Manifest, typisierte DAG-Kanten.
- Governance configuration: `requirements/intake-governance.json`.
- Active inventory: `DirectoryStrict`.
- Legacy names: bleiben Provenienz; kein stilles Rename.
- Archive rule: logisches Archiv mit Receipt; kein Physical Purge.

## Required Sections

Zusätzlich zum portablen Kern sind Trust-/Authority-Grenzen,
Finding-Traceability, Autonomiemodus, positive und negative Evidence,
Revisionsbedingungen und explizite Nicht-Autorität Pflicht.

*In addition to the portable core, trust and authority boundaries, finding
traceability, autonomy mode, positive and negative evidence, revision
conditions, and explicit non-authority are mandatory.*
