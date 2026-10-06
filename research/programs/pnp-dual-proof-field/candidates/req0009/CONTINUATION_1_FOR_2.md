# REQ-0009: one bounded 1-for-2 continuation

Pre-implementation specification. Parent: `43879fe2f496f04f99a70fab0b25efb3adb20e4b`.
User authorization: design and test exactly one x-only continuation, repair the
preserved three-vertex false NO, stop at the first unsupported bridge or
counterexample. Claim ceiling: `P ?= NP = OPEN`.

## Fixed contract

Name: `A_0009_ONE_FOR_TWO`. New executable: `continuation.py`.
Problem input: only `x: bytes`, with unchanged JSON-IS-1 semantics and decoder.
Let B=len(x), n=8B bits, N=number of explicit IDs, M=number of edges.
No seed set, certificate, advice, instance-specific budget, oracle, or route
is accepted as an additional input. Original candidate and evidence are immutable.

Use binary Float64-compatible coordinates and the unchanged exact integer
energy E(b)=(N+1)*sum_edges b_u*b_v-sum_v b_v. No float holds an unbounded integer.
Construct IDs, edge list, matrix, and zero coordinates from x and charge them.
Run the original one-bit rule: score every flip, restore every trial, choose
the least (energy,index) among strict improvements, commit, and repeat.

At its independent terminal set S:

1. If |S|>=K, verify and return YES with the first K selected original IDs.
2. Otherwise scan triples (u,v,w) lexicographically in numeric input-index
   order, with u in S, v<w, and v,w outside S. Temporarily replace u by v,w,
   evaluate exact energy, and restore all three coordinates after EVERY trial.
3. Select the FIRST triple whose trial energy is strictly smaller. Equivalently,
   S'=(S\{u}) union {v,w} is independent. Commit just that exchange, retain a
   trace, then resume the original one-bit descent. Repeat this same rule.
4. If no triple qualifies, halt with experimental candidate NO. This is NOT
   NO_PROVED. The precise hypothesis under attack is:

   `one-bit and 1-for-2 saturation below K => no independent K-set`.

This hypothesis is not an execution premise or an admitted theorem. The referee
attacks this first unsupported completeness bridge; no later bridge or different
heuristic is authorized. Runtime/resource exceptions propagate, not graph NO.
Invalid byte strings are outside the language. The formal binary wrapper rejects
incomplete octets before decoding, charging the scan, as in the existing Cook gate.

## Structural facts and preserved-example repair

An independent vector has E=-|S|<=0; a conflicted vector has E>=1. A permitted
triple changes cardinality by +1. Therefore its energy is smaller exactly when
its resulting set is independent, and then the decrease is exactly one.
Only conflict-free additions can decrease energy in the one-bit phase.
Inductively every committed state is independent and every commit raises |S|
by one. There are at most N commits total, regardless of input or target.
This is a route-length argument, not an N-to-N+1 decision-correctness proof.

On the preserved x={"ids":["0","1","2"],"edges":[[0,1],[0,2]],"K":2},
one-bit descent reaches 100 with E=-1. The first eligible triple (0,1,2)
constructs 011 with E=-2, rolls it back, then commits it. Resumed descent stops
at 011. The internally reconstructed YES witness is IDs 1,2. No referee witness
is supplied to the candidate, and the exact objective/codec are unchanged.

## Complete lifecycle charge

Let a be accepted one-bit moves, e accepted exchanges, so a+e<=N. There are
R1=a+e+1<=N+1 complete one-bit scoring rounds, including terminal rounds.
There are R2<=e+1<=N+1 exchange scans (zero when the target is already met).
Each one-bit round scores N flips; each exchange scan visits at most
N*binom(N,2) triples, plus charged loop/filter overhead. Early success only
shortens this bound. Every scored trial is restored, including the chosen one,
which is then committed separately. Exact energy work CE scans N+M terms.

For each round charge:

 W1 = N*(C_flip + CE + C_rollback + C_compare) + C_commit_trace;
 W2 = C_tuple_enumeration(N^3)
    + N*binom(N,2)*(C_three_writes + CE + C_three_restores + C_compare)
    + C_commit_trace.

Total:

 W(n) = C_read_decode + C_build_graph_matrix + C_initialize_energy
      + sum_(R1) W1 + sum_(R2) W2
      + C_final_cardinality_independence_verification
      + C_original_ID_recovery + C_diagnostics_storage + C_release.

Construction, candidate discovery/selection, continuation, comparison, exact
arithmetic, rollback, state recovery, final verification, identity recovery,
storage, and release are inside this charge. No restarts, external caches,
reconciliation service, or precomputed route exists. Unused services cost zero
calls, not unaccounted work. A failed trial is recovered by its explicit inverse;
an unexpected implementation failure is reported, not treated as a decision.

N,M<=B. At most O((N+1)*N^3*(N+M+1)) elementary route operations occur,
plus polynomial decoding, construction, verification, and output work. Thus
O((n+1)^5) is a conservative high-level bound. Stored matrix/trace/input/IDs
and O(log(n+2))-bit counters fit within O((n+1)^3) bits. In a deliberately
naive deterministic tape lowering, scan this entire bounded store for every
indexed access and allow O(n+1) extra bit work for comparisons/arithmetic:
O((n+1)^4) per high-level operation suffices. The resulting common bound is
O((n+1)^9), with ONE exponent independent of N,K,x. This is an abstract
algorithm-level simulation argument, not a measured Python machine-step
certificate or a numerical value of its constant. No correctness admission
follows from it; implementation counters are phase counts only.

## Frozen counterprobe contract

Before implementation, fix the following referee population and order:

- N=0,1,...,6, then K=0,1,...,N+1, then increasing graph-mask integer.
- At N, list all possible unordered edges (u,v), u<v, lexicographically.
  Bit i of the graph mask denotes edge i. Include EVERY labeled simple graph;
  no connectivity, isomorphism, successful-route, or family filter.
- Use IDs str(0),...,str(N-1), compact JSON with keys ids,edges,K in that order.
  This is a finite canonical encoding sweep, NOT all byte spellings/Unicode IDs.
- Compare the x-only candidate's Boolean decision with a separately implemented
  combinations oracle. The oracle lives only in `attack_continuation.py` and
  never enters the candidate dependency path. Charge its exponential work as
  external research computation, not as polynomial candidate work.
- First separately replay the required preserved example, which must return YES.
  It is a regression obligation and is not included in exhaustive-prefix counts.
- Stop immediately on the first disagreement, invariant violation, resource
  failure, or unsupported implementation premise. If the finite ceiling is
  reached without disagreement, report only bounded success, never admission.
- Enforce an external 45-second wall limit, 30-second CPU limit and 512-MiB
  address-space limit on the sweep where supported; report actual enforcement.
  A resource stop is INCONCLUSIVE, not NO or a counterexample.
- Preserve exact x, digest, full path/energies/moves, internally recovered
  witness, referee certificate, phase counters, complete-prefix counts,
  first-stop coordinates, software versions, command, and input/output hashes.

After a disagreement, only reproduce/check that stopped prefix and its witness,
verify implementation/provenance, and document the obstruction. Do not try a
second continuation, larger exchanges, neutral moves, restarts, or hidden search.
