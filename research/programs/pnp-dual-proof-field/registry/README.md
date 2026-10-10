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

## Evidence accounting axes

Every entry is reviewed against these distinct evidence classes:

- **Source inspection** — what the authoritative source explicitly states or derives.
- **Executed verification** — finite computation/run evidence. Recorded historical runs are not silently treated as rerun by this registry audit.
- **Theorem use** — external theorem premises remain named dependencies, not project-original results.
- **Conjecture/open extension** — an unproved generalization or universal closure.
- **Unresolved inference** — a plausible consequence whose bridge has not been proved.
- **Authority** — source-local only; summaries, migrations, and registries do not upgrade predecessor claims.

## Status vocabulary

- `PROVED_EXACT` — source contains an exact mathematical derivation within its declared scope.
- `PROVED_EXACT_WITH_EXTERNAL_THEOREM_USE` / `PROVED_EXACT_WITH_EXTERNAL_COMPLETENESS_PREMISE` — internal derivation depends explicitly on a named external theorem/complexity premise.
- `PROVED_EXACT_SCOPED_OPEN_EXTENSION` — the displayed scoped theorem is exact; the proposed wider extension remains open.
- `SCOPED_TERMINAL` — exact polynomial decision/repair procedure for a declared restricted class.
- `IMPLEMENTED_VERIFIED_BOUNDED` — executable evidence exists for a bounded population/run.
- `REFUTED_UNIVERSAL` — an exact counterexample defeats the stated universal bridge.
- `FORMALIZATION_METHOD` / `METHOD_ONLY` — research/process/admission/representation contribution, not complexity evidence.
- `SOURCE_BACKED_COLLECTION` — navigation/lineage entry whose leaf claims are carried by separate registry entries.
- `SOURCE_BACKED_SYNTHESIS` — synthesis of already source-backed results; not a new theorem.
- `EXTERNAL_SOURCE_DERIVATION_REVIEWED` — user-supplied derivation reviewed for internal consistency; not repository theorem authority.
- `SESSION_DERIVATION_UNPROMOTED` / `SESSION_SYNTHESIS_SOURCE_ALIGNED` — current conversation reasoning retained below repository theorem authority.
- `EMPIRICAL_INCONCLUSIVE_WITH_PREREGISTERED_SUCCESSOR` — finite empirical route with an inconclusive current result and a frozen future protocol.
- `RESOLVED_HISTORICAL_GAP` — earlier explicit missing bridge later repaired; both states are preserved.
- `OPEN` — unresolved.

## Value classes

- `CORE` — directly defines the current surviving obligation or exact quotient.
- `TERMINAL` — closes a nontrivial restricted class exactly.
- `BARRIER` — prevents repetition of a false universal route.
- `METHOD` — reusable research/execution discipline.
- `REPRESENTATION` — exact carrier/quotient structure whose value evaluation may remain open.
- `CALIBRATION` — bounded experiment/example useful for discrimination.
- `PROVENANCE` — source/recovery/identity value.
- `PENDING` — promising or preregistered but not admitted.

## Current claim ceiling

`P ?= NP = OPEN`.

No registry score, source count, implementation test, local polynomial rule, certificate verifier, exact quotient, compact representation, empirical predictor, or migration/parity result changes that ceiling by itself.

## Reviewed corpus

The v2 review uses four live/default-branch source roots plus the supplied dorm note:

- `redogit/pnp-dean@92040a45...` — current obligation/Cook/REQ-0009 repository.
- `redogit/redogit@fb9c4d4b...` — live mathematical carrier and Dean sources.
- `redogit/Other-Projects-@e25aca549...` — live Repair Lab, Decision Field, FIG-5 and MLIR successor surface.
- `redogit/conscience64@cec20286...` — September-12 P-vs-NP method/evidence surface; those PNP bytes match the pnp-dean import.
- `Minimum_Dorm_Repair_2026-10-07.md` — external user-supplied separate packing-model derivation, SHA-256 `dc412e3f3f2fec754099fbc69baa4f41bd42a2bc9116c1554213eb84ca2f9d1d`.

The pnp-dean import is a scoped historical snapshot, not the sole current authority for every predecessor route. In particular, live `Other-Projects-` contains FIG-5 v0.19-v0.26 and later MLIR changes that are absent from the import.

Generated stdout/stderr, transport duplicates, repeated manifests and repeated evidence blobs are preserved as source occurrences, not promoted to independent conceptual contributions.

## Anti-Ouroboros rule

A carrier is not considered a solver merely because it is finite or polynomial-size. Registry entries distinguish:

`REPRESENTATION -> QUOTIENT -> VALUE EVALUATION -> TOTAL WORK`.

The September-29 Dean boundary-state work already proves the source-backed core of this warning: arbitrary future contexts can distinguish all (2^s) boundary assignments; a fixed-context quotient can be exact after full tables are known; and even a one-entry table can require evaluating `alpha(H)`, the original optimization.

If evaluating or updating a carrier reconstructs an equally hard residual decision problem, the value step remains open.

## Review artifacts

- [Machine-readable registry](FPCV_REGISTRY.json)
- [Human-readable registry](FPCV_REGISTRY.md)
- [Full review](REGISTRY_REVIEW_2026-10-10.md)
- [Source coverage audit](SOURCE_COVERAGE_AUDIT.json)
- [Current cross-state note](CURRENT_CROSS_STATE_2026-10-10.md)
