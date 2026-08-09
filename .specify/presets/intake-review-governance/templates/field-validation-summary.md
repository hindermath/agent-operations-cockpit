# Field Validation Summary

Record synthetic single/series/campaign fixtures, shell parity, an existing
project intake review, and immutable campaign evidence. Include target count,
unique intake count, worker applicability count, positive and negative cases,
hashes, command exits, and residual risks. Publication requires no unresolved
Critical or High finding.

For Series schema 1.1, record request hash binding, roots, target-order
cardinality, edge count, Bash/PowerShell error-class parity, and negative
fixtures for drift, target mismatch, invalid references, duplicate edges,
order contradiction, missing predecessors, and cycles.

For the shared requirements-governance configuration, record a terminal
`Completed` fixture with all targets `Completed` and zero eligible candidates,
plus a negative mixed-state fixture that fails with `RIG017`. Non-terminal
Series states still require exactly one eligible candidate.
