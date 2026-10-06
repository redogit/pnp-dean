# Cook / Clay formalization gate

## Scope

This is a bounded source-anchored admission layer for the existing P-vs-NP obligation field.

It does **not** change:

- Dean / Independent-Set language semantics;
- the shared encoding and deterministic cost model required by the charter,
  now explicitly pinned in [JSON_INPUT_ENCODING.md](JSON_INPUT_ENCODING.md);
- any existing scoped result;
- the theorem status.

The claim ceiling remains:

`P ?= NP = OPEN`.

## Primary sources

Operative formal source:

- Stephen Cook, *The P versus NP Problem*, Clay Mathematics Institute, pp. 1-2:
  https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf

Historical primary anchor, retained as lineage rather than as a replacement definition:

- Stephen A. Cook, *The Complexity of Theorem-Proving Procedures* (STOC 1971):
  https://www.cs.utoronto.ca/~sacook/homepage/1971.pdf

The formal mapping below is taken from Cook's Clay problem description. The 1971 paper is not used to redefine the modern P/NP substrate in this repository.

## Cook / Clay anchors

### Encoded input length

Cook measures worst-case machine time over strings of length `n`, with `n = |w|`. Polynomial time uses one exponent fixed for the machine; in the Clay statement the bound is written:

`T_M(n) <= n^k + k`

for all `n` and some fixed `k`.

Repository consequence: coordinate count, graph family, recursion depth, path length, Float64 dimension, or any other representation-local size does not replace the fixed encoded input length unless the conversion from the fixed encoding is itself explicit and charged.

### Deterministic algorithm

Cook defines `P` using a Turing machine `M` that runs in polynomial time and accepts exactly the language.

Repository consequence: the constructive direction still requires the charter's one deterministic algorithm `A` that returns the exact language decision for every encoded input. A bounded representation or route lookup is not that algorithm unless the whole computation is supplied.

### Verifier / certificate existence

Cook gives the equivalent checking-relation definition of `NP`: there are a fixed `k` and a polynomial-time checking relation `R` such that

`w in L <=> exists y (|y| <= |w|^k and R(w,y))`.

This is an existential certificate statement. It permits efficient checking of a supplied `y`; it does not itself provide a deterministic polynomial-time procedure that finds such a `y` or decides `L` from `w` alone.

### Fixed polynomial bound

The exponent belongs to the machine/algorithm, not to the individual input, graph family, route, certificate, or recursion depth.
A rigorous uniform polynomial proof and justified machine simulation suffice;
benchmark-derived numeric constants and a printed transition table are not
additional Cook requirements. Repository requests for candidate constants
remain evidence obligations, rather than a redefinition of P.

Repository consequence: a collection of locally polynomial transitions does not discharge the constructive theorem unless their complete worst-case lifecycle is bounded by one fixed polynomial in encoded input length.

## Exact mapping into existing obligations

### `U_LOCAL`

For every purposeful transition used by a candidate deterministic decider, recognition, construction, carrier update, verification, reconciliation, rollback, and witness recovery must each have explicit deterministic cost measured against the fixed encoded input length.

`U_LOCAL` is necessary but not sufficient: polynomial cost per transition does not bound the number or composition of transitions.

### `U_MASS`

All lifecycle work is summed into the candidate decider's worst-case total work. Universal constructive promotion requires one fixed bound of the form

`T_A(|x|) <= c*|x|^k + c`

with fixed `c,k`, including representation construction, route discovery, certificate construction/recovery when required, reconciliation, verification, rollback, and recovery.

### `U_TOTAL`

The candidate `A` must halt on every finite binary input. It accepts exactly
valid YES encodings and rejects valid NO encodings and malformed strings.
The same worst-case time bound covers all strings of each length, including
invalid UTF-8/JSON and inputs without complete octets. INVALID diagnostics
do not assert NO for a valid graph.

A verifier that is fast only after a witness/certificate has already been supplied does not discharge `U_TOTAL` as a P-algorithm.

### `U_INDUCT`

`U_INDUCT` is a repository proof discipline, not an additional Cook definition.

If an `N -> N+1` argument is used, it may support the Cook/Clay requirement only when the successor preserves the same finite deterministic algorithm and the same fixed exponent over all encoded input lengths. Choosing a new exponent, machine, route-specific advice, or uncharged preprocessing as `N` grows does not discharge the global bound.

## RequestBundle mapping

Algorithmic RequestBundles keep the existing fields and must use them as follows:

- `needed_inputs`: name the fixed encoded input length and whether any witness/certificate is supplied or must be constructed;
- `requested_parts`: distinguish verifier/checker work from constructor/decider work;
- `counterprobes`: include the promotion barrier below whenever universality is claimed;
- `cost_envelope`: charge all lifecycle and representation/certificate work against encoded input length;
- `acceptance_criteria`: require the exact deterministic-total and fixed-polynomial obligations appropriate to the claim.

Concrete cost and referee mappings are pinned in `requests/REQ-0007-COST-MASS.json` and `requests/REQ-0008-REFEREE.json`.

## Promotion counterprobe

Before any verifier, route, or coordinate/path mechanism is promoted to a universal constructive result, require all of the following:

1. one deterministic algorithm `A` operating from the encoded input `x` alone;
2. exact agreement `A(x) = L(x)` for every finite encoded string, with
   malformed strings outside the language;
3. termination on every such string with total worst-case work bounded by
   one fixed polynomial in `|x|`;
4. all representation construction, route discovery, certificate construction/recovery, reconciliation, verification, rollback, and recovery included in that bound.

Therefore the following non-implications are admission invariants:

`FAST_VERIFY(x,y) != FAST_FIND_OR_DECIDE(x)`

`CERTIFICATE_EXISTS != CERTIFICATE_CONSTRUCTOR`

`KNOWN_ROUTE != KNOWN_ANSWER`

`FLOAT64_OR_PATH_REPRESENTATION != POLYNOMIAL_DECIDER`

`POLYNOMIAL_LOCAL_STEP != POLYNOMIAL_TOTAL_WORK`

A Float64/path representation is not rejected merely for being a Float64/path representation. It remains admissible as a representation if exact Independent-Set semantics are preserved and the missing construction/decision and total-work proofs are supplied under the fixed encoding.

If any required bridge is absent, the referee may admit only the exact scoped result supported by evidence; universal constructive promotion remains `UNRESOLVED`.

## Current candidate enforcement

[REQ-0009 compliance audit](results/REQ-0009-COOK-COMPLIANCE.md) records each
of the four requirements separately. The unchanged candidate is refuted at
exact NO correctness. The standalone `candidates/req0009/cook_admission.py`
command checks that existing witness and exits nonzero; passing ordinary
implementation tests cannot admit the candidate. The supplied-witness
checker and [encoded-language proof](JSON_IS_COMPLETENESS.md) support the
substrate, without supplying the missing continuation rule.

Older request wording about valid instances is read under the all-string
requirement above. No new graph semantics or route has been introduced.

## Boundary

This layer formalizes the source gate and links its substrate support. It
does not repair the candidate, attempt a new decision route or lower bound,
or prove `P = NP` or `P != NP`.
