# FunctionalObject → AnyFunctor → local-plane → obligation-generator lineage

Date: 2026-10-03

This is a provenance and successor map. It does **not** claim that an earlier implementation already contained later semantics.

## L0 — Historical FunctionalObject anchor

Original repository: `BanalityOfSeeking/ServeExcel`

Original path: `FunctionalObject.cs`

Recovered source anchor from the Decision Field provenance record:

- earliest visible path commit: `cd5bfe729d7461e9773ac4873767096c8e6146a0`
- date: 2019-06-10
- blob: `fc2716e1a3c4c2c7ea18541f25d94a26d24dca54`

Source-derived shape:

- ordered `IOBuffer` and `DataBuffer`;
- zero-to-many `Operations[]`;
- zero-to-many `Checks[]`;
- reusable alternating dataflow links;
- terminal `NullTarget<T>()` for otherwise unconsumed flow.

Historical claim ceiling:

[
HISTORICAL\_SHAPE \neq CURRENT\_SEMANTICS.
]

The 2019 object supplies lineage for plural operations/checks and reusable flow. It did not yet carry modern obligation identity, occurrence identity, provenance authority, Homeward recovery, or retained failure semantics.

## L1 — AnyFunctor / FunctionObject execution carrier

The preserved Decision Field v0.7 path separates represented function identity, invocation occurrence, execution, verification, admission, and recovery.

Current source anchors in `redogit/DnD`:

- `projects/decision-field/include/decision_field/anyfunctor_mirror.hpp`
- `projects/decision-field/docs/ANYFUNCTOR_STRUCTURAL_RECONCILIATION_2026-09-29.md`
- `projects/decision-field/docs/MIRROR_RMAL_HOMEWARD.md`

The executable relation is:

[
RMAL
\to
FunctionObject<T>
\to
AnyInvocation<T>
\to
AnyFunctor
\to
receipt
\to
verification/admission
\to
Homeward.
]

Important inherited distinctions:

[
DISCOVER \neq EXECUTE
]

[
EXECUTE \neq VERIFY
]

[
VERIFY \neq ADMIT
]

[
OCCURRENCE \neq SEMANTIC\ OBJECT.
]

This is the point where the old generic flow becomes an obligation-bearing, occurrence-aware execution carrier.

## L2 — Lowered/local-plane AnyFunctor

The local-plane successor reduces the broad AnyFunctor machinery to a finite reusable plane:

[
Receive(0)
\to
Contextualize(1)
\to
Represent(2)
\to
Integrate(3)
\to
Receive(0').
]

Source anchors:

- `redogit/DnD:projects/decision-field/docs/FUNCTIONALOBJECT_ANYFUNCTOR_LINEAGE_2026-10-03.md`
- `redogit/DnD:projects/decision-field/include/decision_field/local_plane.hpp`
- `redogit/DnD:projects/decision-field/include/decision_field/anyfunctor_local_plane.hpp`
- `redogit/DnD:projects/decision-field/evidence/local_plane_2026-10-03/VERIFICATION.md`

The local plane:

1. requires multiple obligations;
2. binds observations to contextual and representation signatures;
3. integrates a route only after the underlying AnyFunctor invocation is admitted;
4. retains rejected/incomplete/conflicting observations as residuals;
5. forbids conflicting overwrite of an admitted route;
6. provides a local route index.

The intended lowering is:

[
first:
discover \to execute/verify \to satisfy\ obligations \to integrate\ route
]

[
later:
route\ lookup \to execute/verify \to satisfy\ obligations.
]

The verified boundary is:

[
KNOWN\_ROUTE \neq KNOWN\_ANSWER
]

and

[
AVERAGE\ O(1)\ ROUTE\ LOOKUP \neq O(1)\ UNDERLYING\ COMPUTATION.
]

This is the closest executable ancestor of the obligation-generator field.

## L3 — Obligation-driven generator lowering

The P-vs-NP field lowers the same pattern one step further.

A generator no longer receives an unconstrained world or permanent role. It accepts one consequential obligation slice:

[
G_i(O_i,\Gamma,C,E,B)\rightarrow RequestBundle^{0..*}.
]

Mapping:

| FunctionalObject / AnyFunctor lineage | Obligation-generator successor |
|---|---|
| `Operations[]` | `requested_parts[]` + `candidate_operations[]` |
| `Checks[]` | `acceptance_criteria[]` + `counterprobes[]` |
| `IOBuffer/DataBuffer` | obligation-local carrier/context/evidence refs |
| reusable link | admitted route / dependency edge |
| `NullTarget<T>()` | explicit residual obligation / zero-output remainder |
| `FunctionObject<T>` contract | generator contract |
| `AnyInvocation<T>` | obligation-slice acceptance |
| computation receipt | RequestBundle/result receipt |
| admission | referee-controlled scoped admission |
| Homeward | reconstruction/recovery reference |
| local route index | obligation-local MemoryGenerator retrieval |
| distinct occurrence | distinct request/receipt identity even when semantic mechanism is shared |

## What is inherited versus new

Inherited shape:

- zero-to-many transforms;
- plural checks/obligations;
- reusable routing;
- occurrence-sensitive execution;
- explicit residuals;
- separated execution/verification/admission;
- recovery;
- finite local plane.

New in the P-vs-NP generator field:

- theorem-direction tags;
- explicit obligation slicing;
- zero-to-many child obligations;
- independent cost generator;
- independent referee generator;
- claim-ceiling propagation;
- recursive request graph.

## Non-collapse rules

[
FunctionalObject \neq AnyFunctor
]

[
AnyFunctor \neq LocalPlane
]

[
LocalPlane \neq ObligationGenerator
]

[
SUCCESSOR\ RELATION \neq SOURCE\ REWRITE.
]

The lineage is useful because each successor preserves a smaller executable core while adding the distinctions required by the newer obligation.
