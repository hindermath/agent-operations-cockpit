# Plan remediation R4 / Plan-Reparatur R4

## Ergebnis / Result

Die beiden High-Findings O1 und O2 aus dem ersten Analyze-Pass sind begrenzt behoben. Fachlicher Scope, fünf kanonische Artefakte, die drei reservierten IDs, die 48-Pfade-Reparaturbindung, Delivery Authority und die No-Bypass-Grenze bleiben unverändert. / The two High findings O1 and O2 from the first Analyze pass are addressed within scope. Feature scope, the five canonical artefacts, the three reserved IDs, the 48-path repair binding, delivery authority, and the no-bypass boundary remain unchanged.

## O1: kausales PreMerge / causal PreMerge

Der Plan verlangt jetzt: alle Repository-Schreibvorgänge abschließen, unveränderlichen Feature-HEAD pushen, PR-/Check-/Review-/Approval-Fakten für genau diesen HEAD konvergieren und erst danach den externen PreMerge-Snapshot erzeugen und validieren. Zwischen eingefrorenem HEAD und Merge gibt es keinen Repository-Writer. / The plan now freezes and pushes the final repository head before converging PR facts, and only then creates and validates the external PreMerge snapshot. No repository writer runs between the frozen head and merge.

## O2: endlicher Closeout / finite closeout

Der einzige fünfpfadige Closeout bleibt erhalten und verwendet eine ausdrücklich transaktionale Zustandsänderung, die erst durch ihren normalen Merge kanonisch wird und ihren eigenen Merge nicht behauptet. Der Runner-PostMerge-Snapshot entsteht danach extern und bindet den realen Closeout-Merge sowie den sauberen Sync. Nach Rückkehr der gerouteten Implement-Phase ist genau ein auf `tasks.md` und `autonomous-run-state.json` begrenzter normaler Persistence-PR zulässig, um die einmalige Runner-Ergebnisbindung zu speichern; anschließend gibt es nur noch externen Fast-forward-/Clean-/0/0-Nachweis und keinen Repository-Writer. / The sole five-path closeout remains transactional and becomes canonical only through its normal merge without claiming that merge. The external runner PostMerge snapshot then binds the actual closeout merge and clean sync. After the routed Implement phase returns, one final normal persistence PR limited to `tasks.md` and `autonomous-run-state.json` may persist the one-time runner result; only external fast-forward/clean/0/0 proof follows, with no further repository writer.

## Geänderte Verträge / Changed contracts

- `specs/003-authoring-contract/plan.md`
- `specs/003-authoring-contract/contracts/authoring-contract-design.json`
- `specs/003-authoring-contract/contracts/postmerge-gate-requirements.json`

Keine Implementierung, kein Git-Write und keine Remote-Aktion wurde ausgeführt. / No implementation, Git write, or remote action was performed.
