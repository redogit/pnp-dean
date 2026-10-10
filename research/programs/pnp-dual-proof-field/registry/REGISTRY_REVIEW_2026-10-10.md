# Full review of the P vs NP FPCV registry

Date: 2026-10-10

Verdict: **the original 40-entry registry was not complete enough. It has been repaired.**

Claim ceiling remains:

`P ?= NP = OPEN`.

## Review scope

This review compared the registry against the current default-branch/source surfaces of:

- `redogit/pnp-dean@92040a45d9b05bdfbce0357d061cc250637d6b54`;
- `redogit/redogit@fb9c4d4b36ca218334c30c24b08db2bec1c667a7`;
- `redogit/Other-Projects-@e25aca5496436e1c67d0c0b82205575baf3e5a27`;
- `redogit/conscience64@cec20286e626c2070e95eccf084ee21146361d56`;
- the supplied `Minimum_Dorm_Repair_2026-10-07.md`, whose recorded SHA-256 was independently confirmed.

The review distinguishes source inspection, historical executed evidence, external theorem use, method/formalization, conjecture/open extension, and unresolved inference.

## What was wrong in v1

### 1. The registry treated the pnp-dean export as if it were the entire current corpus

That missed live successor work. `Other-Projects-` currently contains 223 Repair Lab files; 63 are absent from the pnp-dean imported snapshot. The substantive missing research line was FIG-5 v0.19-v0.26.

### 2. Several independent GYRO theorems had been compressed away

The following deserved their own entries and now have them:

- DEAN-4 NP-completeness;
- pressure-closure monotonicity;
- four-result self-reduction;
- exact connected/co-connected factorization;
- the regular non-bipartite repair plateau.

### 3. The Dean September-29/30 progression was over-compressed

The repaired registry now preserves separately:

- the connected C5 matching-gap family;
- cycle-certificate verification versus NP-complete discovery;
- clique/odd-cycle overlap correction and mixed-frame LP/integrality boundaries;
- fixed seven-/nine-vertex rank rows and local wheel rounding;
- exact boundary-state composition Steps 19-25;
- compact-factor construction versus optimization;
- parity switching, one-vertex bipartization and growing exceptional-set cost;
- articulation composition and the two-vertex coupling obstruction.

### 4. Session work had accidentally rediscovered an earlier source-backed result

The largest authority error was around future-state equivalence.

Dean Step 23 already proves that on an edgeless boundary of size (s), all (2^s) assignments are distinguishable by some legal one-vertex future context. That is stronger than the later session binomial-family observation.

Steps 24-25 already separate fixed-context quotienting from the cost of computing values, including the one-class identity (f_B(arnothing)=alpha(H)).

The registry now attributes these results to the September-29 source. The session term **Anti-Ouroboros** remains useful synthesis, not new theorem authority.

### 5. The external dorm note had been assigned too much authority

Its mathematical derivations were reviewed and found internally coherent under their explicit assumptions, but it is a user-supplied separate packing-model note with no newly claimed computational run.

Its entries are now `EXTERNAL_SOURCE_DERIVATION_REVIEWED`, not repository-style `PROVED_EXACT`.

### 6. The Cook/Clay gate is a formalization/admission layer, not itself a P-vs-NP theorem

Its registry status is now `FORMALIZATION_METHOD`.

## FIG-5 review

FIG-5 is now represented explicitly.

The source-backed state is:

- exact counter identity (P_{DP}=R+T_{taut});
- v0.22 bounded structural-collapse result;
- v0.23 bounded replication;
- v0.24 bounded density-4 transfer;
- v0.25 width-4/density-4 **INCONCLUSIVE_ADMISSION**, with 25/30 rows admitted and the exact-five rule failing at n=12 and n=13;
- v0.26 fresh width-4 seeds/cap preregistered, formulas not materialized, so **no v0.26 scientific result exists yet**.

Nothing in FIG-5 changes the P-vs-NP claim ceiling.

## Coverage accounting

For the pnp-dean snapshot semantic surface:

- 143 Markdown/JSON files qualified as semantic candidates after excluding generated run/evidence/transport duplicates.
- 106 are now directly referenced by registry entries.
- The remaining 37 are explicitly classified in `SOURCE_COVERAGE_AUDIT.json` as summaries, navigation, contracts, provenance, bibliography, replay receipts, or machine-readable duplicates.
- **0 semantic candidates remain unclassified.**

Evidence files and code were not discarded: they are treated as occurrences supporting their conceptual entries rather than as independent mathematical contributions.

## Structural integrity checks

Passed:

- no duplicate FPCV IDs;
- no broken local source references;
- no broken semantic-ancestry references;
- uploaded dorm SHA-256 matches the registry;
- chronology remains separate from semantic ancestry;
- failed branches remain present;
- bounded execution remains distinct from theorem authority;
- external theorem use is tagged;
- current-session derivations remain below repository authority unless an older exact source already exists.

## Current high-value state after review

The strongest common unresolved obligation is still the same:

**efficient discovery and exact value evaluation of a continuation-sufficient carrier for every residual, with the entire lifecycle and witness recovery under one fixed polynomial bound.**

The exact positive-circuit quotient survives. The normalized surviving core (U(C)) survives. Signature/core value evaluation remains open.

The Dean line supplies several exact positive composition examples, but also exact barriers showing that:

- arbitrary future context can force exponentially many distinct interface behaviors;
- short descriptions do not imply cheap value evaluation;
- constant-size individual separators do not control total coupling;
- compact local factor construction can retain the original optimization.

The current local-value-composability criterion therefore remains an **open research criterion**, not a solved universal theorem.

## Final registry verdict

After repair, the registry is suitable as a current evidence-accounting index for the reviewed default-branch corpus.

That does **not** mean every theorem was independently reproved or every historical experiment rerun. It means the registry now has the correct source authority, claim ceiling, conceptual coverage, chronology/ancestry separation, failure retention, and live-successor accounting for the reviewed corpus.
