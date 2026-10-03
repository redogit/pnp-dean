# Universal obligations

The current program reconciles the older CertifiedPlanner obligations with the newer Dean/RMAL carrier language.

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

> Every purposeful transition has a Cook-compatible polynomial implementation.

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

Every valid input must terminate as:

- `YES_PROVED`, or
- `NO_PROVED`.

`ERROR` and `UNRESOLVED` are research/runtime states, not terminal answers of a final P algorithm.

Status: **OPEN**.

## U_INDUCT — universal successor

For every admissible encoded prefix/input of length N and every admissible extension:

[
I(N) \Rightarrow I(N+1)
]

under the same finite machine and same fixed polynomial exponent.

Status: **OPEN**.

## P=NP promotion condition

One construction must discharge all obligations above under the fixed definitions.

## P!=NP promotion condition

A valid lower-bound route must show that at least one required obligation cannot be satisfied by any deterministic polynomial-time algorithm, in a representation-independent way strong enough to establish the standard separation.

Counterexamples to particular carriers are evidence toward such a theorem, not the theorem itself.
