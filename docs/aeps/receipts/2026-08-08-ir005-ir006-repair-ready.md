# AEPS-Erfassungsreceipt IR005-/IR006-Repair Ready / AEPS Capture Receipt IR005/IR006 Repair Ready

## Identität und Ergebnis / Identity and outcome

- Receipt-ID: `AEPS-RECEIPT-AOC-2026-08-08-022`
- Datum / Date: `2026-08-08`
- Trigger: zwölf formal validierte Ready-Ersatzreviews und vollständiges
  Series-Ersatzreview nach begrenztem IR005-/IR006-Repair / *twelve formally
  validated Ready replacement reviews and a complete replacement Series review
  after the bounded IR005/IR006 repair*
- Series-Review-ID: `86763944-9aab-4178-81b7-40dff7c1af51`
- Series-Review-Status: `Ready`
- Repository-Base-HEAD: `a3629bd20c3596579dfa7f333e6cc8e24ca5963a`
- Ergebnis / Outcome: `StrengthenedLocalEvidenceAndResolvedGovernanceDrift`
- Upstream-Status: `PendingPublication`

Der Repair stellt Decision- und Lifecycle-Truthfulness wieder her. IAD601 bis
IAD604 stehen unverändert in der bestätigten Tabelle. Zwölf lokale
Lifecycle-Texte sind historische Authoring-Snapshots und delegieren den
aktuellen Zustand an Manifest und Order. Alle erneuerten Receipts, zwölf
Single-Reviews und das vollständige Series Review bestehen auf Bash und
PowerShell. / *The repair restores decision and lifecycle truthfulness.
IAD601-IAD604 remain semantically unchanged in the confirmed table. Twelve
local lifecycle texts are historical snapshots and delegate current state to
the canonical manifest and order document. All renewed receipts, twelve Single
reviews, and the complete Series review pass both validator surfaces.*

## Einzelne Ready-Trigger und Deduplizierung / Individual Ready triggers and deduplication

Dieser Batch-Receipt bindet die zwölf atomar zusammengehörenden Ready-Trigger
einzeln. Jede Zeile besitzt den vertraglichen Deduplizierungsschlüssel
`Review-ID + Zielpfad + Zielhash`; kein Trigger wird zusammengefasst oder
verworfen. / *This batch receipt binds every Ready trigger individually. Each
row retains the contractual review-ID, target, and target-hash deduplication
key.*

| Review-ID | Zielhash / Target hash | Receipt-Hash | Result-Hash |
|---|---|---|---|
| `722d1188-c961-47a1-b149-afef548791ed` | `9fc31a833421915b68b85c7dd499dc5b97a81152a8cf668599bb243ef3e17503` | `3c95e47592ff8eb7646d9f96b3ee173205365dfeb540da736ee5fb2c3c4d7f14` | `d32287ec6a9feec4c2bb736c6962da4d5689ccc0389f4d054be3fb6a90b67662` |
| `7667b091-eb3d-42e8-b3dd-cf52cc1175d1` | `f6d57cacc954b4899fc5bd8ddcc235570ec20470094feec506e1b8e9ea07e3e9` | `d39517bad8892012c9c2dcc00e498fd7ae84ba39c6d642a5ba80a143ee53d5a8` | `0dfbee54de985efdd5c47d2fb0c630a1a0213fb9e62c762096194348ae40d934` |
| `fc33bdf1-5857-45c1-a5d4-f89d3a4fdca9` | `eff68253a12129859ae75696cb4a8b8b009f7436d7b7c9df89238255aa5bf6ce` | `b084ca0da63ce7a286265f6dac758a3075d9dc7c0f9387993b151ab31cfc49cb` | `57983c537e106568c668ad381983995ce94b6089ce684a6f1410011de6ed5a7a` |
| `82c61d7f-9bb3-4adf-90d8-92ffeef25c76` | `cb255e60b49237f8cc655486b6529536b831b5b942f89f838678386bc31f930f` | `e699480f0c99486df3f51ea932dbef6125e5f9d69fbe586842368d8a4d43e2b7` | `ad271d30970c6dbd1ae7bbd8b780f1a1933b75ac54b6f970f5818d9958d62da9` |
| `393d5c45-2a01-4d20-8246-232060761c8e` | `6a41e6ae6447ff0192a03af7940362e05e48bff48a5fd21f39e9b6e670eade20` | `fab2ad176c3523e9ad60366cfd3676b529f652ae9de5a44bdf61a43e19bfc23c` | `19fe73b0aebff709ff16231493ef6758412bbb572d42f92d0dcdba4b3d16d865` |
| `609edc9a-96b7-4b5d-8ddf-3eb89cd1d067` | `31d31e82ab1857182d1201192438e5c91abfc3190ba47a2f68b9543034ab0cfd` | `a1f4b1905917617a405bda0d10d58711852e0f93140088b7c567843d369dd3a0` | `cf685f2e9fb88e918fe52ea389f68f3a3a48f2639d7ee13a47bd9633894a98df` |
| `101da312-394f-48e7-9ad0-ad3f718e7374` | `ce89a73e9e1d0bdeadcc166a0f4a7b3b94052037cabb8225ceb4ef2ebd345ec4` | `791a9c58879c3c3a4f67ec47141af236a94fa2303a888615aa55f19a6f33e0e4` | `8ed9eb0883ded43cf1140b1af041f6c2348adda1c6a6868304c89c8fe99dd0fa` |
| `f9f84045-d19c-486b-8813-e30c195ef205` | `3fd7c5fbf4f419ed6131c4984a948f26d0b6b8c6ab3a5b068cdadce501c3fbad` | `2b6f6f075433c446a3b9b8118347746e074bb1a2dd706df28da93c30000699f8` | `5ff27f9f3d5f81a90385948a178eeb47fad9758b6b71c3381b6dbd0d9c3e3e39` |
| `d6cea7b3-724d-4715-b2b8-7d73ac2019c8` | `dde4a283ac2c761373085beea976dcd927d813e17aa2b1ad76ceab800c1d604a` | `b061152602f0a768c957ea0ffc09dab065d90df551eddf9575b490f865109e96` | `e8689fb22097849960e259e097d298fb9e2a5800092fde02d219fc386523b6f8` |
| `14c10979-84c5-4451-957d-b34e65f111ec` | `ade666e411ed9a81b9736e628adb8613be0d9d732295c7e5470d90f0c64f513a` | `a40a457107a3e98646352f35270d39371665c109f70a56219d73ee7de93c70eb` | `3b2e76893571836fbb91a132e665c623222835e5b3f5c77e0cb6b912810c8511` |
| `97d2c9fc-2c5e-4852-8ee5-5ccbb3cee8e0` | `623451757149794556a9f4efef73c13c6894244476b7fd484f0eaaa9fdba7f1a` | `9616de1cef25bd53564cd5041a69ba34a362712445dcc398739e74b7a3ddedd3` | `37da394251c03faf451563082602358f445d4e690ae054a6dcc5c0ac92493017` |
| `2190e2cd-16cf-4afc-8d8e-12eba5bdd71f` | `c3da0eec782279678b1599e0e2365e409fbfe9e0e6f40e5f2e1b768e385f3b83` | `4a02982f3312ff40c33e98d1282645b6cdb7cd87f354faf2fc79c4bf008d595a` | `a0941c0e7813683a2e8dfcdf1a1a189f199300e783be0d00357319d7827eef98` |

## Series- und Vorgänger-Evidence / Series and predecessor evidence

| Quelle / Source | Normalisierter SHA-256 / Normalised SHA-256 |
|---|---|
| `specs/intake-review-results/aoc-phase-2-series-2026-08-08-r3.json` | `11a42bd28136bf82c4dc0f36ac6e4d69b5ad8bfed6422d98d9cdb9be7c603345` |
| `specs/intake-review-requests/aoc-phase-2-series-2026-08-08-r4.json` | `e43acab4931d09a3a4917327f468e1ae2b6c6ec7546600c8d6b66b5c3dfc96fe` |
| `specs/intake-review-results/aoc-phase-2-series-2026-08-08-r4.json` | `c511ea75ac1fe67ee4701cd45c9d9e9876bb3c39c0a84dcd7debdac647c1238b` |
| `docs/reviews/aoc-phase-2-intake-review-2026-08-08-r4.md` | `0637663d69681f86a42efc0994b53f0849aeeab90e5406c8b497d94f45fa68af` |
| `docs/decisions/open-decisions.md` | `cf85b9053368903d0126cb080237dea04c3abed3620f5d29709d20466f461d15` |
| `specs/intake-series/aoc-phase-2/manifest.json` | `d05c8c5c6e860b20c1c9419360dba188f713be39a6f34c21a785d28d8da65c00` |
| `specs/intake-series-receipts/aoc-phase-2.json` | `cbe6e196784b397404d819beb381e2e4c93823994f1d36f1dbda6fc42a881397` |
| `docs/aeps/findings-ledger.md` | `ad4b1efbfaf5061ee7405e89c3323af83cd4bf9c42777a7c61678712d4607b12` |

Der Series-Deduplizierungsschlüssel ist Ergebnisartefakt,
`c511ea75ac1fe67ee4701cd45c9d9e9876bb3c39c0a84dcd7debdac647c1238b` und Datum `2026-08-08`. Das R3-Ergebnis bleibt als
negative Vorgänger-Evidence unverändert erhalten. / *The result artifact, its
hash, and date form the Series deduplication key. R3 remains immutable negative
predecessor evidence.*

## Einordnung / Assessment

Es entsteht keine neue AEPS-Finding-ID. Die Evidence stärkt
`AEPS-FIND-AOC-001`, `007`, `010` und `015`. Candidate-Matrix,
Gap-Analyse und Handoff-Empfehlung bleiben unverändert, weil die Reparatur
ausschließlich AOC-lokale Requirements-Governance-Evidence liefert. Ein
einzelnes Referenzprojekt genügt nicht für Cross-Project-Validierung oder
Preset-Promotion. / *No new finding is created. Existing findings are
strengthened, while derived candidate artifacts remain unchanged because this
is AOC-local requirements-governance evidence.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `GeneratedUpdate`. Quelle ist die verpflichtende AEPS-Prüfung
nach jedem formal validierten Ready-Review und nach dem materiellen
Series-Repair; Owner ist der AOC-AEPS-Evidence-Workstream. Ledger und dieses
Receipt werden aktualisiert; Matrix, Gap-Analyse, Handoff und Presets bleiben
unverändert. / *Decision: GeneratedUpdate. The mandatory post-Ready and
post-repair assessment is the source; the AOC AEPS evidence workstream is the
owner.*

## Grenzen und Nicht-Autorität / Boundaries and non-authority

- Der Manifeststatus bleibt `NeedsClarification`, bis ein neuer
  ausdrücklicher Series-Update-Auftrag ihn formal abschließt. / *The manifest
  remains NeedsClarification until a new explicit Series update completes it.*
- Keine Produktimplementierung oder Cross-Project-Validierung.
- Keine Änderung oder Promotion eines Presets.
- Keine Specify-, Remote-, Merge-, Bypass-, GitHub- oder Level-0-Aktion.

`Ready` und dieses Receipt erteilen keine nachgelagerte Ausführungsautorität.
/ *Ready and this receipt grant no downstream execution authority.*
