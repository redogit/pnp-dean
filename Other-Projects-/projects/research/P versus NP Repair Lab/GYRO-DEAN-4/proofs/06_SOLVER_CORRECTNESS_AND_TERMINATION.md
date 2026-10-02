# Exact Solver Correctness and Termination

## State invariant

For a state `(C,q,F_in,F_out)`, the residual decision is:

> Does the induced graph on active candidates `C` contain an independent set of size `q` that can be appended to `F_in`?

The implementation maintains that every active candidate is compatible with every member of `F_in`. `F_out` is provenance only.

## Lemma 1 — Compatibility q-core deletion is exact

If an active vertex `v` has fewer than `q-1` compatible active neighbors, then no residual independent q-set can contain `v`.

Proof. A residual independent q-set containing `v` needs exactly `q-1` other active vertices, all compatible with `v`. Fewer than `q-1` such vertices exist. Therefore deleting `v` cannot delete any feasible residual q-set. QED.

## Lemma 2 — Exclusion-isolated inclusion is existence-preserving

If `q>0` and active vertex `v` has exclusion degree zero inside the active candidate set, then forcing `v` into the cohort preserves existence.

Proof. If a residual independent q-set `I` already contains `v`, nothing is needed. Otherwise choose any `u in I`. Since `v` has no exclusion edge to any active vertex, `(I-{u}) union {v}` is another independent q-set. Hence a solution exists iff one exists containing `v`. QED.

## Lemma 3 — Include/exclude branching is exhaustive

For any active pivot `v`, every residual independent q-set either excludes `v`, giving an instance `(C-{v},q)`, or includes `v`, in which case all exclusion neighbors of `v` are forbidden and the remaining target becomes `q-1`.

Thus:

`Exists(C,q) = Exists(C-{v},q) OR Exists(C-N[v],q-1)`.

The two cases are exhaustive and disjoint. QED.

## Theorem — Reference solver is exact

Assume every carrier transformation that reports `changed=true` is itself an exact existence-preserving transformation, and every terminal carrier result is certificate-correct. Then `Solver::find_one(q)` returns YES iff the original graph has an independent set of size q; any returned witness is independent and has size q after reconstruction.

Proof by induction on the number of active candidates. Base cases are `q=0` (YES) and `|C|<q` (NO). Exact repairs preserve the answer by Lemmas 1–2 and the carrier contract. If no repair terminates the state, Lemma 3 partitions all solutions between two strictly smaller active candidate sets, and the induction hypothesis applies to both recursive calls. QED.

## Termination

Every recursive branch removes at least the pivot `v` from the active candidate set. Hence recursion depth is at most `n`. The current reference carriers are no-op or finite exact hooks, and `MAX_REPAIR` only removes candidates or decreases q, so its loop terminates. Therefore the compact reference solver always terminates.

## Memoization note

The compact reference implementation memoizes only NO states keyed by `(q,candidate_mask)`. This is sound because residual infeasibility depends only on the induced candidate graph and residual q, while all active candidates are already compatible with `forced_in`. A production implementation whose carriers introduce additional residual constraints must include those constraints (or their canonical semantic signature) in the memo key.
