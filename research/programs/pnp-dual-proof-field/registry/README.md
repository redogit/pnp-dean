# Feature / Property / Contribution / Value Registry

Date: 2026-10-10

This registry is an evidence-accounting surface for the P vs NP / Dean program. It does not create new theorem authority.

## Purpose

For each distinct research object, retain four views:

- **Feature** — the mechanism or mathematical object.
- **Properties** — exactness, scope, computability, complexity, continuation behavior, reconstruction, and known failure conditions.
- **Contribution** — what the object actually added: theorem, implementation, counterexample, scoped terminal, method, empirical evidence, or unresolved hypothesis.
- **Value** — how the object is useful to the current program without confusing usefulness with proof authority.

Chronology and semantic ancestry are separate. A later file may restate an older result without becoming its mathematical authority. Duplicate source occurrences remain listed as occurrences rather than being counted as independent evidence.

## Status vocabulary

- `PROVED_EXACT` — source contains an exact mathematical derivation within its declared scope.
- `SCOPED_TERMINAL` — exact polynomial decision/repair procedure for a declared restricted class.
- `IMPLEMENTED_VERIFIED_BOUNDED` — executable evidence exists only for a bounded population/run.
- `REFUTED_UNIVERSAL` — an exact counterexample defeats the stated universal bridge.
- `METHOD_ONLY` — research/process/representation contribution, not complexity evidence.
- `OPEN` — unresolved.
- `SESSION_DERIVATION_UNPROMOTED` — derived in the 2026-10-10 authorized conversation step but not yet source-reviewed or repository-verified as theorem authority.

## Value classes

- `CORE` — directly defines the current surviving obligation or exact quotient.
- `TERMINAL` — closes a nontrivial restricted class exactly.
- `BARRIER` — prevents repetition of a false universal route.
- `METHOD` — reusable research/execution discipline.
- `REPRESENTATION` — exact carrier/quotient structure whose value evaluation may remain open.
- `CALIBRATION` — bounded experiment/example useful for discrimination.
- `PROVENANCE` — source/recovery/identity value.
- `PENDING` — promising but not yet admitted.

## Current claim ceiling

`P ?= NP = OPEN`.

No registry score, source count, implementation test, local polynomial rule, certificate verifier, exact quotient, or compact representation changes that ceiling by itself.

## Corpus scope

The canonical `redogit/pnp-dean` tree was traversed back-to-front at the current default branch. The pass includes:

- current dual-proof-field obligation/Cook/JSON-IS/REQ-0009 sources;
- imported `redogit/research/pnp` carrier, Dean, handoff, probe, and run surfaces;
- imported `Other-Projects-/projects/research/P versus NP Repair Lab` sources, including GYRO-DEAN-4, Decision Field, mutation/full-cost/MLIR evidence surfaces;
- imported `conscience64/research/pnp/2026-09-12` HSP/Fourier/Partial-Hard role-matrix sources;
- top-level recovery/provenance/validation surfaces.

Generated stdout/stderr, transport duplicates, and repeated evidence blobs are preserved as source occurrences, not promoted to separate semantic contributions.

The user-supplied `Minimum_Dorm_Repair_2026-10-07.md` is represented as an external conversation source with SHA-256 `dc412e3f3f2fec754099fbc69baa4f41bd42a2bc9116c1554213eb84ca2f9d1d`. It is not silently treated as repository theorem authority.

## Anti-Ouroboros rule

A carrier is not considered a solver merely because it is finite or polynomial-size. Registry entries distinguish:

`REPRESENTATION -> QUOTIENT -> VALUE EVALUATION -> TOTAL WORK`.

If evaluating or updating a carrier reconstructs an equally hard residual decision problem, the value step remains open.
