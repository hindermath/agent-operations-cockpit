# Implementierung: Red/Green / Implementation: Red/Green

T004-T007 bestanden lokal auf macOS. Vor dem Wertecheck bestanden die gültigen Fixtures; leere Integration ergab in beiden Shells tatsächlich Eligible (Kind-Exit 2, Test-Exit 1). Danach ergab derselbe unveränderte Test Blocked/ProductFailure (Kind- und Test-Exit 0), mit Kriteriengrund, einer DE/EN-Aktion und unveränderten Fixture-Dateien. / *T004-T007 passed locally on macOS. Valid fixtures passed first; empty integration actually returned Eligible in both shells before the fix (child exit 2, test exit 1). The identical test then returned Blocked/ProductFailure (both exits 0), with a criterion reason, one bilingual action and unchanged fixture files.*

[Ausführungen und historische Quellbytes / Execution and historical source bytes](red-green.json), SHA-256 `8399c811e75c4d19cac2de17471c28171904c1f934cebc36868218aa1d4aca8b`. Testhash `9b68771e24a7a46093c2b8288c3af808f79259286d5b957e0b776157ce6ba719`. Die historische Red-Quelle bleibt im JSON erhalten; nur der Integrationswertecheck wurde ergänzt. / *The JSON retains historical red sources; only the integration value check was added.*

Dies ist ein begrenzter erster Slice; US1-US3, native Linux-/Windows-Gates und Lieferung bleiben offen. / *This is the first bounded slice; US1-US3, native Linux/Windows gates and delivery remain pending.*
