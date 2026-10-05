# REQ-0009 — candidate instantiated; first correctness bridge refuted

Base revision: `c30df58d3ed6622ed731fabc2c71d314f028ad17`.
Date: 2026-10-05. Claim ceiling: `P ?= NP = OPEN`.

The user selected the single JSON input, closing the earlier encoding-choice
blocker. [JSON-IS-1](../JSON_INPUT_ENCODING.md) now fixes its grammar, original
IDs, isolates, natural target K, invalid-input behavior, and bit-work model.
The previous [missing-bridge checkpoint](REQ-0009-FIRST-BRIDGE.md) remains
historical evidence; it is not the current stop condition.

One candidate is implemented:
[A_0009_ONE_BIT_DESCENT](../candidates/req0009/CANDIDATE.md).
It constructs its graph, Float64-compatible binary coordinates, exact integer
objective, deterministic route, terminal answer, and any YES witness from x
alone. Its complete lifecycle recurrence is given in that specification.

**Verdict: REJECT_COUNTEREXAMPLE for this candidate's universal decision
correctness.** This is a mathematical false negative, not an implementation
exception, numerical-precision failure, or a representation-independent
lower bound. No second candidate or repair was introduced.

## Decisive encoded input

```json
{"ids":["0","1","2"],"edges":[[0,1],[0,2]],"K":2}
```

This is 49 UTF-8 bytes / 392 bits, SHA-256
`85c3f4a421656df67987092971fd87d30554049d671df289feef5e94ab03941d`.
ID 0 conflicts with both other students; IDs 1 and 2 are compatible.

| Step | Coordinates | Energy | Consequence |
| --- | --- | ---: | --- |
| Start | `(0,0,0)` | 0 | All single additions tie at -1. |
| Select least index | `(1,0,0)` | -1 | Student 0 selected. |
| Stop | `(1,0,0)` | -1 | Removing 0 gives 0; adding either leaf gives 2. Candidate returns NO. |
| Independent witness | `(0,1,1)` | -2 | IDs 1 and 2 satisfy K=2; the correct answer is YES. |

The first failed arrow is exactly

`one-bit local minimum and fewer than K selected => no independent K-set`.

Global objective encoding is exact: conflicted vectors have positive energy;
independent vectors have energy minus their size. The route nevertheless finds
a maximal set, not necessarily a maximum set. Correctness of the NO rule is
the first unsupported step, and the displayed input refutes it.

The failure is vertex-minimal. The finite referee checked all four labeled
graphs with N=0,1,2 and all 13 targets K=0..N+1. For N=3 it stopped at the first
disagreement: eight graphs visited and 31 encoded instances checked in total.
No exhaustive success is claimed for every graph with three vertices.

## Evidence and cost

- [Raw finite result](../evidence/REQ-0009-FIRST-COUNTEREXAMPLE/result.json)
  preserves the encoded input, oracle witness, full candidate path, exact
  energies, and counts.
- [Computation manifest](../evidence/REQ-0009-FIRST-COUNTEREXAMPLE/manifest.json)
  records base revision/dirty state, actual argv, input/output hashes, software,
  runtime, and enforced resource limits. Manifest validation succeeds with
  input freshness and result-hash checks.
- The candidate made seven energy evaluations, six trial flips and six
  rollbacks, one committed flip, and copied six trace coordinates. These are
  phase counts, not unit-cost Turing-machine steps.
- The combinations oracle is external bounded referee work on N<=3. It is
  absent from the candidate's dependency path and never supplies a witness to A.

The route requires at most N additions and `(t+1)N` scored flips, so no hidden
exponential route traversal was used. Numeric c,k certification for the Python
runtime is not supplied; universal promotion has already failed at correctness.

The codec and route were checked with behavior tests: malformed/ambiguous
records, Unicode/NUL identity, huge K, numeric edge order, isolates, empty
graphs, x-only witness construction, and the retained false-NO path. Tests
first failed against missing implementations, then passed. Passing these tests
does not make the candidate correct for all instances.

Fresh verification on Python 3.12.14:

- Full `python validate.py`: source-identity check passed; the new candidate's
  10 tests passed; existing MLIR Python tests passed 19/19; decision-field
  discriminator checks passed.
- The existing `native-build-and-tests` check was blocked at launch:
  `FileNotFoundError: cmake`. The full validation command therefore exited 1.
  This host has a C++ compiler but no discovered CMake/CTest executable.
  Native implementation tests were not run; no native source was changed.
- `validate_manifest.py .../manifest.json --root .`: valid evidence record,
  with hashes/input freshness checked.
- `git diff --check`, request shape, JSON syntax, and local evidence links:
  passed.

A separate read-only mathematical derivation and implementation review agreed
with the hand counterexample and reproduced the stored finite result. They
reported no material code/evidence defect. Reviewer agreement adds review
coverage; the explicit graph and its checked witness supply the mathematical
refutation.

## Surviving result and remainder

The exact objective and input codec survive this counterexample. The candidate
is an ordered greedy maximal-independent-set constructor with sound YES
witnesses; its NO answers are not complete. The next mathematical need would
be a justified global continuation rule when one-bit descent stops short.
That repair is recorded as a remainder only; it was not attempted or silently
replaced by the exponential referee.

Both P=NP and P!=NP remain open.
