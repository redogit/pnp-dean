# Universal obligations

The current program reconciles the older CertifiedPlanner obligations with the newer Dean/RMAL carrier language.

The complexity-specific admission gate is [COOK_CLAY_FORMALIZATION.md](COOK_CLAY_FORMALIZATION.md). It anchors only encoded-input length, deterministic decision, verifier/certificate existence, and fixed polynomial bounds. It does not alter Dean/Independent-Set semantics or the existing cost model.

## U_COVER — universal exact coverage

For every reachable nonterminal residual:

- an exact next rule exists;
- its applicability can be recognized without solving the original hard problem as a hidden oracle;
- the rule preserves the protected decision consequence.

Current-language equivalent:

> The contextual path selector plus Reconcile can always find a lawful continuation or terminal decision.

Status: **OPEN**.

## U_LOCAL — polynomial lifecycle per move

Every selected rule has uniformly polynomial:

- recognition;
- construction;
- carrier update;
- verification;
- reconciliation;
- rollback;
- witness reconstruction.

Current-language equivalent:

> Every purposeful transition used by a candidate decider has deterministic work polynomial in the fixed encoded input length; local polynomiality alone does not discharge `U_MASS`.

Status: **PARTIAL**. Many scoped terminals exist.

## U_MASS — one fixed polynomial total-work bound

Across the complete computation:

- branching;
- composition;
- repeated reconciliation;
- reverse lookup;
- carrier growth;
- recovery

must fit one fixed polynomial in encoded input length.

Current-language equivalent:

> The complete odd/even/shared-carrier machine has a single exponent independent of graph family, K, deficit, depth, or chosen route.

Status: **OPEN/PARTIAL**.

## U_CONT — continuation sufficiency

If two configurations are merged, no permitted future transform may separate their protected consequence.

[
C(x)=C(y)
\Rightarrow
Q(F(x))=Q(F(y))
]

for every admitted future continuation relevant to the obligation.

Status: **OPEN as a universal cheaply discoverable carrier condition**.

## U_TOTAL — total decision

Every finite binary input must halt within the same uniform time bound.
Malformed encodings are rejected outside the language; INVALID is not a
NO assertion about a valid graph. Every valid instance must terminate as:

- `YES_PROVED`, or
- `NO_PROVED`.

`ERROR` and `UNRESOLVED` are research/runtime states, not terminal answers of a final P algorithm.

Cook/Clay gate: fast checking of a supplied certificate does not itself provide the deterministic algorithm on input `x` alone required by the constructive direction.

Status: **OPEN**.

## U_INDUCT — universal successor

For every admissible encoded prefix/input of length N and every admissible extension:

[
I(N) \Rightarrow I(N+1)
]

under the same finite machine and same fixed polynomial exponent.

`U_INDUCT` is this program's proof discipline, not an additional Cook definition. An `N -> N+1` step is admissible only if it preserves the same finite deterministic algorithm and one fixed exponent across all encoded input lengths.

Status: **OPEN**.

## P=NP promotion condition

One construction must discharge all obligations above under the fixed definitions.

## P!=NP promotion condition

A valid lower-bound route must show that at least one required obligation cannot be satisfied by any deterministic polynomial-time algorithm, in a representation-independent way strong enough to establish the standard separation.

Counterexamples to particular carriers are evidence toward such a theorem, not the theorem itself.
