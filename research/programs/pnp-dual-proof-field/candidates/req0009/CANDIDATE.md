# A_0009_ONE_BIT_DESCENT

Base: `c30df58d3ed6622ed731fabc2c71d314f028ad17`; JSON selection: user,
2026-10-05. The route was fixed before the bounded replay. It is a newly
specified lowering of the high/low coordinate idea, not recovered historical
code or an assertion about every possible coordinate mechanism.

**Candidate is refuted as an exact Independent-Set decider.** The first failed
bridge is terminal local optimality implying a correct NO. The supplied
procedure and its false-NO behavior are retained, without repair.

## One finite x-only algorithm

Executable: `candidate.py`, `A(x: bytes) -> bool`. Diagnostic entry point:
`run_candidate(x)`. There is no supplied y and no imported research oracle.

1. Decode x using [JSON-IS-1](../../JSON_INPUT_ENCODING.md). Invalid input is
   rejected outside `L_Gamma`; diagnostics say INVALID.
2. Construct the ordered identity array, exact edge list, and N-by-N symmetric
   Boolean adjacency matrix from x. Retain every vertex, including isolates.
3. Construct the coordinate vector `b=(0.0,...,0.0)` in `{0.0,1.0}^N`. Each
   coordinate is exactly representable in Float64. No ID, whole state, or
   unbounded objective value is packed into one float. Integer energy is

   `E(b) = (N+1)*sum_{uv in edges} int(b_u)*int(b_v) - sum_v int(b_v)`.

4. At each round, try each one-bit flip j in input order, recompute its exact
   energy, and roll the trial flip back. Among strictly smaller energies,
   select the smallest pair `(energy,j)`. If none exists, terminate. Otherwise
   perform the chosen flip and retain its full coordinate snapshot and energy.
5. Check final cardinality and independence against the constructed graph.
   Output YES if independent and at least K vertices are selected, and
   reconstruct the first K selected original IDs as a witness. Otherwise output
   candidate NO. That latter rule is part of the candidate being refuted; it is
   never labelled `NO_PROVED`.

The program always executes the same finite rule set. It does not select a new
machine, exponent, route family, or advice at larger N. No N-to-N+1 proof is
used. Arbitrarily long K digits remain exact in the decoded instance; the
derived `min(K,N+1)` comparison is sufficient for this fixed graph.

## Representation proof and route termination

For `s=sum b_v`, `q=sum_edges b_u*b_v`, a conflicted vector has
`E=(N+1)q-s >= (N+1)-N=1`. An independent vector has `E=-s<=0`.
Thus `min_b E(b)=-alpha(G)`, and the **global** threshold `min_b E(b)<=-K`
is equivalent to existence of an independent K-set. This does not give a
global-minimum constructor.

At an independent vector, deleting a selected vertex changes E by +1. Adding
an unselected vertex with d selected neighbors changes E by `(N+1)d-1`.
Therefore only conflict-free additions decrease E. Starting at zero, every
accepted move adds one vertex, decreases E by one, and preserves independence.
All admissible additions tie, so the route chooses the least eligible index.
It terminates after `t<=N` moves at an ordered greedy **maximal** independent
set. Maximal does not imply maximum.

YES outputs are sound: the final set is independently checked and first K IDs
form a valid witness. Correct NO behavior would require the unsupported arrow

`no decreasing one-bit move and |S|<K => alpha(G)<K`.

## Complete lifecycle accounting

Put `n=8B`, `N<=B`, `M<=B`, and let t be accepted flips. Define
`R_0=0` and, for each selection round including the last stop round,

```text
R_(j+1) = R_j
        + N*(C_trial_flip + C_energy(N,M,n) + C_rollback + C_compare)
        + C_route_commit_and_trace(j),      0 <= j <= t, t <= N.

W_A(n) = C_read_and_decode(n) + C_build_matrix(N,M,n)
       + C_initial_coordinates_and_energy(N,M,n) + R_(t+1)
       + C_final_cardinality_and_verify(N,n)
       + C_witness_lookup_and_reconstruct(n) + C_counts_and_storage(n)
       + C_release(n).
```

This charges discovery (all scored flips), selection, transforms, every
rollback, exact arithmetic, initial and intermediate storage, final checking,
original-ID recovery, and release. Reconciliation/advice/precomputed route
lookup are unused, with zero such calls by construction. Input generation is
outside A; reading/decoding x is inside A. No external certificate is verified
by A. Successful witness construction is inside A.

For the reference implementation:

- exactly `1+(t+1)N` energy evaluations, each scanning N coordinates and M
  edges; all scores and counters have `O(log(B+2))` bits;
- exactly `(t+1)N` trial flips and rollbacks, t committed flips;
- `N^2` matrix cells and `(t+1)N` stored path coordinates;
- at most `N(N-1)/2` final verification pairs; reconstructed ID bytes at most B.

Consequently the declared route has `O((N+1)N(N+M))` arithmetic/scanning work,
plus the charged polynomial decoder/matrix/trace/witness terms. A deliberately
naive tape lowering can scan the entire polynomial-size work store for each
indexed access, so its bit overhead also remains polynomial. This is scoped
accounting, not a numeric c,k certificate for the Python runtime. No numeric
machine-time admission is attempted after the earlier correctness failure;
the complete recurrence and raw counters are preserved for audit.

## First counterexample and stop

Ordered IDs `0,1,2`, edges `(0,1),(0,2)`, K=2. All one-student moves have E=-1;
the tie selects center 0. At state `100`, E=-1. Deleting 0 gives E=0; adding
either leaf gives E=2. The route stops and outputs NO. The vector `011` has
E=-2 and witnesses YES with IDs `1,2`.

This failure is vertex-minimal: for N=0 or 1 the route is maximum; for N=2,
the only simple graphs have either zero edges (route selects both) or one edge
(route selects one). K beyond N cannot be satisfied by any route.

The external bounded referee `attack_first_bridge.py` independently enumerates
combinations only for N<=3. It stops at the first disagreement, does not modify
A, and is never called/imported by A. Its exponential oracle is research work,
not a hidden constructor. See [the checkpoint](../../results/REQ-0009-CANDIDATE-RESULT.md)
and the associated input-hashed computation manifest.

This result refutes this selector/terminal rule only. The JSON encoding and
exact objective survive the attack. Other coordinate routes and both theorem
directions remain open. No repair or later bridge attack is included.
