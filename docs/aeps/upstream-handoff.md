# AEPS-Upstream-Handoff-Empfehlungen / AEPS Upstream Handoff Recommendations

## Zweck und aktueller Handoff-Status / Purpose and current handoff status

Kanonischer Anker ist
[`hindermath/home-baseline#196`](https://github.com/hindermath/home-baseline/issues/196).
Diese Bestandsaufnahme führt keine GitHub- oder Level-0-Schreibaktion aus.
Die neu erfassten Ready-Re-Reviews einschließlich RAW-03 sind noch
`PendingPublication`; deshalb bleibt der gesamte neue Handoff bis zu stabiler
Commit- oder PR-Evidence gesperrt. / *This baseline performs no GitHub or
level-0 write. The newly captured Ready re-reviews, including RAW-03, remain
unpublished, so new upstream handoff is blocked until stable commit or PR
evidence exists.*

## Direkt für #196 geeignete Ergänzungen / Suitable direct additions to #196

Nach Veröffentlichung empfiehlt sich ein einzelner strukturierter Kommentar,
der bestehende Kandidaten ergänzt, ohne sie zu duplizieren: / *After
publication, one structured comment should enrich existing candidates without
duplicating them:*

| Finding | Upstream-Bezug / upstream relation | Empfohlener Kommentarinhalt / recommended comment content |
|---|---|---|
| `AEPS-FIND-AOC-001` | `CAND-AEPS-07` | `Ready` und Series-Eligibility als getrennte Achsen; RAW-02 liefert `Ready`+`Blocked`-Evidence. |
| `AEPS-FIND-AOC-002` | `CAND-AEPS-06`, `CAND-AEPS-08` | Bounded Repair bewahrt IADs, Scope und Authority und verlangt vollständiges Re-Review. |
| `AEPS-FIND-AOC-003` und `011` | `CAND-AEPS-01`, `06`, `07` | Historische Delivery-Obergrenze, einzelnes Ready und Series-Lifecycle sind keine aktuelle Startautorität. Das AOC-weite 14er-Gate stärkt lokale Evidence, bleibt aber bis zu Runtime- und Cross-Project-Validation projektspezifisch. |
| `AEPS-FIND-AOC-005` | `CAND-AEPS-08`, RF-20 | Secret-Negativfixture als Test-Evidence, nicht als Receipt-Provenienzquelle. |
| `AEPS-FIND-AOC-006` und `010` | `CAND-AEPS-10`, `11` | Applicability plus Re-Evaluation und semantisches Review als Ergänzung zu Schema-Validation. |
| `AEPS-FIND-AOC-008` | `CAND-AEPS-05` | Neue negative Evidence: Doppelowner `PO002`, Zyklus `PO007`. |
| `AEPS-FIND-AOC-009` | `CAND-AEPS-02`, `08` | Evidence-Zahlen reichen nicht; Artefakte, Commands, Exitcodes und Traceability müssen gebunden sein. |
| `AEPS-FIND-AOC-013` | `CAND-AEPS-05`, `07` | Neun Eligibility-Achsen, Shared-Write-/Shared-Decision-Negativfixtures und lokaler vertragsgetriebener Validator; Runtime- und Cross-Project-Evidence fehlen. |
| `AEPS-FIND-AOC-014` | möglicher Ausbau `CAND-AEPS-04`, `08` | Lokale Create-/Verify-/Partial-/Collision-Fixtures bestehen; Cross-Project- und Runtime-Recovery-Evidence fehlen. |
| `AEPS-FIND-AOC-015` | `CAND-AEPS-06`, `08` | Negativ-Evidence: Ein hash- und schemagültiges Receipt kann offene Target-Decisions fälschlich als leer ausweisen. Die manuelle Reparatur mit Ready-Re-Review liefert positive lokale Paritäts-Evidence; automatische Validator- und Cross-Project-Evidence fehlen. |

Der Kommentar bindet mindestens AOC-Commit oder PR, Ledgerpfad, Ready-Review-
IDs, positive und negative Evidence, Grenzen und weiterhin offene Promotion-
Blocker. / *The comment binds the AOC commit or PR, ledger path, Ready review
IDs, positive and negative evidence, limits, and remaining promotion blockers.*

## Eigene Issues nach weiterer Evidence / Dedicated issues after further evidence

### 1. Ready-to-Eligibility-and-Authority Contract

- **Enthält / Contains:** `AEPS-FIND-AOC-001`, `003`, `011`, `013` und
  `AEPS-GAP-AOC-001`.
- **Geeignetes Repository / Suitable repository:** `hindermath/home-baseline`,
  weil drei vorhandene Preset-Familien projektübergreifend koordiniert werden.
- **Eröffnungskriterium / Opening criterion:** veröffentlichte AOC-Evidence
  plus eine zweite Anwendung oder eine reproduzierbare Ende-zu-Ende-Fixture.
- **Verlinkung / Linking:** Issue-Body verweist auf #196; #196 erhält bei
  aktueller Authority einen Rückverweis.

### 2. Intake Receipt Semantics, Evidence Roles and Safe Negative Fixtures

- **Enthält:** `AEPS-FIND-AOC-004`, `005`, `009`, `015` sowie
  `AEPS-GAP-AOC-002`, `003`, `005`, `010`.
- **Geeignetes Repository:** zunächst `hindermath/home-baseline`, falls die
  Preset-Inventur bestätigt, dass Intake Authoring und Security Governance
  gemeinsam betroffen sind; andernfalls AOC-Issue für weitere Pilot-Evidence.
- **Eröffnungskriterium:** veröffentlichte AOC-Evidence, geklärte
  Rollen-Taxonomie für Provenienz versus synthetische Testdaten sowie positive
  und negative Decision-Paritätsfixtures in einem zweiten Intake-Programm.
- **Verlinkung:** wechselseitig mit #196, keine Preset-Promotion im Issue.

### 3. Review-Lineage Impact Graph

- **Enthält:** `AEPS-FIND-AOC-007` und `AEPS-GAP-AOC-004`.
- **Geeignetes Repository:** AOC für eine erste zusätzliche Graphfixture;
  Level 0 erst bei wiederholtem Auftreten oder bestätigtem Preset-Änderungsbedarf.
- **Eröffnungskriterium:** zweite Reparaturkette mit Single- und Series-
  Supersession oder Evidence aus einem weiteren Projekt.
- **Verlinkung:** AOC-Issue verweist auf #196; Handoff nach Level 0 folgt den
  Kriterien des Anchor-Issues.

## Nicht upstream zu generalisieren / Do not generalise upstream

`AEPS-FIND-AOC-012` bleibt für TFM, JSON, Testframework, IPC, Persistenz und
Queue-Semantik AOC-spezifisch. Upstream geeignet ist nur das Prozess-Learning
aus `AEPS-FIND-AOC-002`, dass begrenzte Reparaturen bestätigte fachliche
Decisions bewahren. / *The technology choices remain AOC-specific. Only the
decision-preservation process learning is suitable for upstream use.*

## Ausführungsgrenze / Execution boundary

Vor einem Handoff werden aktuelle Authority, Authentifizierung, Zielrepository,
Duplikate und stabile Evidence erneut geprüft. Ein historischer Delivery-Modus
oder dieser Empfehlungsbericht erteilt keine GitHub-Schreibautorität. / *Before
handoff, re-check current authority, authentication, target repository,
duplicates, and stable evidence. This recommendation grants no GitHub write
authority.*
