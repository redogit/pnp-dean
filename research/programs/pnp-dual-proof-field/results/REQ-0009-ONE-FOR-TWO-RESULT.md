# REQ-0009: one bounded continuation, repaired star, first new false NO

Parent source: `43879fe2f496f04f99a70fab0b25efb3adb20e4b`.
Date: 2026-10-06. Claim ceiling: `P ?= NP = OPEN`.
Verdict: **REJECT_COUNTEREXAMPLE** for `A_0009_ONE_FOR_TWO` as an exact decider.

Exactly one continuation was specified and implemented. Its
[pre-implementation specification](../candidates/req0009/CONTINUATION_1_FOR_2.md)
was committed at `e3312b89fb5532dedefbc0c731696749aa07b6c3` before the new
executable and tests. The initial candidate, its codec/objective, supplied-witness
checker, admission refusal, and historical evidence remain unchanged.

## Frozen continuation

After the original one-bit descent stops at S below K, enumerate triples
(u,v,w) in input-index lexicographic order, with u selected and v<w unselected.
Trial S'=(S minus {u}) union {v,w}, compute the unchanged exact energy, and
restore all trial coordinates. Commit the FIRST strictly improving triple,
then resume original one-bit descent. Repeat only this rule. If there is no
such triple, return experimental NO, never NO_PROVED.

The only problem input to [the executable](../candidates/req0009/continuation.py)
is x. Its dependencies are dataclasses and the unchanged decoder. There is
no witness, seed set, lookup advice, restart, or referee in its dependency path.
The local triple enumeration is explicit and charged, not hidden search.

## Required three-vertex repair: verified

The preserved 49-byte/392-bit input now follows

`000 -> 100 -> 011`, with exact energies `0 -> -1 -> -2`.

The exchange is (remove 0, add 1 and 2). Its internally constructed witness is
IDs 1,2. There are 11 energy evaluations: the initial score, nine one-bit
trials, and one exchange trial. Every trial is restored before any commit.
The original candidate still returns its preserved false NO on this same x.

## First new counterexample

```json
{"ids":["0","1","2","3","4"],"edges":[[0,2],[0,4],[1,2],[1,3]],"K":3}
```

This is 69 UTF-8 bytes / **552 bits**; SHA-256:
`15b404763c15827b5ad62a6bf74f64bd5aedaf519dbda90684ef4714989e14ef`.

The graph is the five-vertex path `4--0--2--1--3`. Original descent takes
`00000 -> 10000 -> 11000`, with energies `0,-1,-2`, selecting S={0,1}.
It is independent and one-bit saturated. The continuation tests all six
permitted triples and commits none:

| Removed | Added | Selected conflicts remaining | Trial energy |
| --- | --- | --- | ---: |
| 0 | 2,3 | 1--2 and 1--3 | 9 |
| 0 | 2,4 | 1--2 | 3 |
| 0 | 3,4 | 1--3 | 3 |
| 1 | 2,3 | 0--2 | 3 |
| 1 | 2,4 | 0--2 and 0--4 | 9 |
| 1 | 3,4 | 0--4 | 3 |

None improves on -2. The candidate returns NO. But I={2,3,4} has no edge,
has size 3 and energy -3. Certificate `00111` passes the retained checking
relation. This is a mathematical false negative, not an exception, numeric
rounding error, exhausted budget, or oracle failure.

The exact refuted bridge is:

`one-bit and 1-for-2 saturation below K => no independent K-set`.

Removing 0 leaves 1, which blocks 2 and 3; only 4 is available. Removing 1
leaves 0, which blocks 2 and 4; only 3 is available. The rule cannot free a
compatible pair while retaining the other selected vertex. This describes
the obstruction; it is not an implementation of a further exchange rule.

## Exhaustive stopped prefix

Order was fixed BEFORE implementation: increasing N, then K=0..N+1, then
increasing graph-mask integer in the lexicographic edge basis. Every labeled
simple graph is included; no isomorphism or family filter. IDs are canonical
index strings, not every valid Unicode/whitespace spelling.

| Population actually checked | Instances | Result |
| --- | ---: | --- |
| N=0..4, every graph, every K=0..N+1 | 437 | All agree |
| N=5, every graph, K=0,1,2 | 3,072 | All agree |
| N=5, K=3, masks 0..57 | 58 | All agree |
| N=5, K=3, mask 58 | 1 | First disagreement; stop |

Total: **3,568 instances**, consisting of 3,567 agreements and one false NO.
The separately required star regression is not included in this count.
No higher mask at K=3, later K, or N=6 was searched after the stop.
The predeclared finite ceiling was N=6 but was not reached.

### Why the failure is vertex-minimal

Suppose N<=4 and an independent S is saturated for both permitted moves, but
there is a larger independent I. One-bit saturation means S is maximal.
For |S|=1, maximality prevents a larger I containing S; two vertices of I
therefore replace S's vertex by a valid pair, contradicting saturation.
For |S|=2 and |I|>=3, at least one vertex is shared because N<=4. I cannot
contain both vertices of S, by maximality. Keeping the shared vertex and
replacing the other by two vertices of I gives a permitted exchange.
For |S|>=3, the only larger case under N<=4 is a four-vertex independent
set containing S, again contradicting maximality. The empty case is immediate.
Thus the displayed N=5 failure is vertex-minimal, not just a small example.
This argument uses no claim about arbitrary-N correctness.

## Cook gate and complete work charge

| Gate | Outcome for this one continuation |
| --- | --- |
| One finite deterministic x-only rule | Specified and implemented; binary wrapper included |
| Exact language agreement on every string | **Refuted** by the 552-bit valid YES instance |
| One fixed polynomial total-time bound | Abstract route/tape-lowering argument; no numeric Python/TM constant certificate or universal admission |
| Entire lifecycle charged | Construction, explicit trial enumeration, continuation, exact scoring, comparison, every rollback, trace/storage, verification, original-ID recovery and release included |

Every accepted addition or exchange increases independent-set cardinality by
one, so at most N commits occur. There are at most N+1 one-bit scoring rounds
and at most N+1 triple scans. Each triple scan examines at most N*binom(N,2)
trials; each score scans N+M terms. With N,M<=B and n=8B this gives the
specification's conservative O((n+1)^5) high-level bound. Charging naive
finite-tape access/arithmetic over the polynomial work store gives the stated
O((n+1)^9) abstract bound with one fixed exponent. These are algorithm-level
bounds, not unit-cost claims about Python or measured TM steps.

On the first new counterexample, the candidate performs 22 energy evaluations,
15 one-bit trials and rollbacks, six exchange trials and 18 coordinate restores,
two committed additions, no accepted exchanges, 15 trace-coordinate copies,
and one final verification pair. The 25 matrix cells, decoded IDs/edges,
cardinality scans and recovery/cleanup remain in the lifecycle accounting.

The external combinations referee examined 4,958 candidate certificates and
24,198 edge checks across the stopped prefix. That exponential oracle is
research computation, not part of A and not hidden inside its polynomial bound.
A polynomial runtime does not make this candidate's false NO correct.

## Reproduction, review, and scope

[Raw result](../evidence/REQ-0009-ONE-FOR-TWO/result.json) retains the exact x,
complete traces, moves, witnesses, phase counters, prefix counts and stop.
[Execution manifest](../evidence/REQ-0009-ONE-FOR-TWO/manifest.json) retains
source hashes before/after, actual argv, software and resource caps.
[Verification record](../evidence/REQ-0009-ONE-FOR-TWO/verification.json)
retains all six rejected triples and the independent checking results.

From the repository root:

```bash
python -m unittest discover -s research/programs/pnp-dual-proof-field/candidates/req0009 -p 'test_*.py' -v
python research/programs/pnp-dual-proof-field/candidates/req0009/attack_continuation.py /tmp/req0009-continuation-result.json
```

The first sweep ran on Python 3.13.5 in 1.296 seconds; an identical-prefix
replay ran in 1.360 seconds and produced byte-identical result JSON. The host
actually enforced a 45-second parent timeout, 30-second POSIX CPU cap and
512-MiB POSIX address-space cap. The command's exit zero means the research
run completed; the JSON verdict explicitly refuses constructive admission.
An additional vertex-bitmask oracle, separate from the combinations oracle,
checked exactly the same stopped prefix and confirmed the first disagreement.
The hand derivation above independently exhibits the checked witness and
exhausts every permitted exchange at the stopped state.

The 17 unchanged tests passed before implementation. Eleven new tests first
failed because the continuation/referee were absent, then passed. Two further
regression/evidence checks preserve the discovered false NO. The final scoped
suite has 30 passing tests. Implementation success is not theorem admission.
The seven recovered baseline files were checked against their exact Git blob
hashes. Git transport was unavailable in this host; tests used a hash-verified
source subset retrieved through the connected GitHub API, not a full clone.
Whole-repository/native validation was not rerun; no native source was changed.
Review was an inline code/contract audit plus the explicit independent oracle
and mathematical checks, not a claimed separate model review.

## Surviving result and stop

The codec and exact objective survive. This x-only rule repairs the original
star and has sound verified YES witnesses and a bounded monotone route. It is
**not** a correct universal NO decider. No neutral move, restart, larger
exchange, second heuristic, or later bridge was attempted after this failure.
The remaining obligation is completeness of a continuation/NO rule; it is
unresolved, not discharged by these finite tests or by the work bound.

`P ?= NP = OPEN`.
