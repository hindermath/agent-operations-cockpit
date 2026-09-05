# Plan-Remediation R8: Aktuelle Bindung ohne Vorabbehauptung / Current binding without preclaim

## Ergebnis / Result

**Completed.** Die beiden High-Befunde `H1` und `H2` aus Plan Review R7 sind
mit den kleinsten moeglichen Aenderungen behoben. / *The two R7 High findings
`H1` and `H2` are resolved with the smallest possible changes.*

- `spec.md` bindet jetzt den aktuellen META-LH-03-Receipt-Hash
  `85ffcea67b0723241606040c5d2b9eb586a51d8d13005b676ceb6eeab2caa745`.
- `tasks.md` behauptet kein noch nicht bestandenes Review mehr. Die Tasks-Phase
  muss nach einem tatsaechlich bestandenen Review dessen Ergebnis binden.
- Der historische Hash `392d8934...` bleibt nur dort erhalten, wo
  `data-model.md` den frueheren R1-Archivstand ausdruecklich beschreibt.
- Scope, Anforderungen, IDs, Autoritaet, Reparatur-Checkpoint und
  Domain-Artefakte bleiben unveraendert. / *Scope, requirements, IDs,
  authority, repair checkpoint, and domain artefacts remain unchanged.*

## Aktuelle Bindungen / Current bindings

- `spec.md`: `607653676c04f1d232c3bad600a524ae37bf14bc075b9c52654e33739f411c59`
- `plan.md`: `a74baaaa1972cce76bd23303a6b91df507711fc643af2d19acaa360c9a65225c`
- `tasks.md`: `046b550b241810469b2bb9858629d5a55b1c4b5d8f4b124ee10f911b9af89497`
- `contracts/authoring-contract-design.json`: `e44d9c72762aec444abff72ad87497455a917dfbaded8a7cc85b26a4eaad4b02`
- `current-evidence-binding.json`: `41d271b770622305338f316e059e70ccf0a5f16f086a18295bb2c2a0af7a0b5c`
- Blockiertes Review R7: `phase-results/plan-review-r7.json`,
  `2c2b448612dbbe2edbb42ba0a7a27ffcfc5bb3bf21c120a5e1ba064034f19b3d`

Der naechste Gate-Schritt ist genau ein Plan Review R8. / *The next gate is
exactly one Plan Review R8.*
