# REQ-0009 — first bridge checkpoint

Source revision: `4d896168bd3d4a62d2f951ec6cea0cfedaa84834`.
Checked: 2026-10-05. Claim ceiling: `P ?= NP = OPEN`.

**Result: UNRESOLVED at the encoded-input binding.** The requested single
deterministic candidate `A(x)` has not been instantiated. This checkpoint
fulfills the request's explicit missing-bridge output, not its decider output.

## Exact target and first undefined operation

The charter's object-level language is finite simple conflict graphs and a
target `K`, with YES exactly when an independent set of size at least `K`
exists. The requested candidate must construct everything from one finite
encoded input `x`, measured by its bit length, without an external witness.

The first operation would be

```text
decode_Gamma(x) -> (original_ids, G, K) or invalid
```

No authoritative byte grammar, decoder, or invalid-encoding convention was
located in the operative authority chain at the pinned revision. Consequently
the encoded language `L_Gamma`, the domain of valid `x`, and the exact
construction cost are not yet bound. An invented decoder would select a new
substrate; it would not recover the asserted existing fixed encoding.

This is a specification gap, not a graph counterexample, runtime failure,
NO answer, or evidence for either theorem direction.

## Source evidence

Paths in this table are relative to the repository root. Line locators refer
only to the pinned revision above.

| Source | Finding |
| --- | --- |
| `research/programs/pnp-dual-proof-field/CHARTER.md`, lines 29–46 | Defines graph semantics and requires a shared encoding/model; does not define a byte grammar, decoder, or concrete step-count model. |
| `research/programs/pnp-dual-proof-field/COOK_CLAY_FORMALIZATION.md`, lines 7–10 | Assumes the encoding/model was already selected by the charter. This assumption is not supplied by that charter. |
| `research/programs/pnp-dual-proof-field/requests/REQ-0009-COOK-CONSTRUCTOR-BRIDGE.json`, lines 24–32 | Still lists exact encoding, coordinate arithmetic, constructor, selector, and decision rule as needed inputs. |
| `Other-Projects-/projects/research/P versus NP Repair Lab/GYRO-DEAN-4/src/main.cpp`, lines 15–47 | Takes two external CSV files, positive q, and capacity; skips rows and unknown endpoints; calls four-result enumeration. This is not the requested self-contained encoding of `(G,K)`. |
| `Other-Projects-/projects/research/P versus NP Repair Lab/GYRO-DEAN-4/include/gyro/bit_graph.hpp`, lines 9–20; `include/gyro/solver.hpp`, lines 10–16 | Provides decoded graph construction and `Solver(g).find_one(K)`. These are object-level interfaces, not a byte decoder. |
| `conscience64/research/pnp/2026-09-12/ALL_RESEARCH_TO_P_VS_NP_ROLE_MATRIX.md`, line 10 | Float64 builder is scoped to identity, integrity, and exact payload lookup; this does not define an Independent-Set route objective. |

Search coverage: operative program instructions/request/gate/status, targeted
native graph and CLI interfaces, and repository text searches for encoding,
Float64, coordinate construction, and path selection. No claim is made about
unretrieved external repositories, Library artifacts, or prior chats.

## Requested candidate parts at this stop

| Part | State |
| --- | --- |
| Construction from `x` | Blocked at `decode_Gamma`; no decoder substituted. |
| Coordinate/path construction | Not instantiated after the first missing input binding. The active request names a needed definition rather than supplying one. |
| Deterministic route selection | Not instantiated or attacked. An existing graph solver or payload lookup is not silently adopted as the requested coordinate selector. |
| Exact YES/NO rule | Object-level Independent-Set semantics are fixed; encoded-domain behavior is not yet bound. |
| Witness role | No external certificate may be supplied to the intended `A`; any claimed YES witness must be constructed/recovered with original IDs. No witness-construction claim made here. |
| Total-work recurrence | Required lifecycle terms are retained below; no numeric recurrence or polynomial constants can yet be justified for an uninstantiated `A`. |
| Successor argument | Not used; no changing exponent or machine proposed. |

Required accounting, **an obligation schema rather than an implemented
recurrence**, is

```text
W_A(n) = C_decode(n) + C_encode(n) + C_representation_build(n)
       + C_discover(n) + C_select(n) + C_transform(n)
       + C_reconcile(n) + C_verify(n) + C_rollback(n)
       + C_recover(n) + C_witness_reconstruct(n),  n = |x| bits.
```

Unknown terms remain unknown. No term is treated as zero, and no constants
`c,k` are proposed before `A` exists. A representation-local `N=|V|` does not
replace `n` without the decoded-size relation and its construction cost.

## Guarded resumption

The only next active bridge is
[REQ-0010-ENCODING-BINDING](../requests/REQ-0010-ENCODING-BINDING.json).
It must recover an authoritative codec or obtain a decision fixing one shared
codec before candidate construction resumes. There is no coordinate failure
claim and no later route/precision/cost attack at this checkpoint.

One concrete proposal, **not adopted**, is a self-contained UTF-8 JSON record
with `ids` (ordered, distinct original strings), `edges` (distinct sorted
index pairs `0 <= u < v < len(ids)`), and `K` (nonnegative integer). It would
preserve exact IDs, include isolates, permit `K=0` and `K>|V|`, and use
`n=8*len(x)` for the raw byte input. Its complete grammar, duplicate-key and
invalid-input rules, deterministic parser, model simulation, and conversion
cost would need to be pinned before it becomes the formal substrate.

Alternatively, the existing roster/conflict CSV field conventions could be
retained inside one explicit framed byte input, with `K` included. External
file paths, capacity, permissive row dropping, and four-result enumeration
would still need to be separated from the decision language. Neither proposal
is described as the existing fixed encoding.

## Verification and limits

The source finding was checked by two disjoint read-only obligation-local
audits and reconciled with direct source reads. Agent agreement is not a proof
certificate. The decisive evidence is what the pinned operative files actually
define, together with the distinct native API boundary.

Only documentation/request/state artifacts change. Historical source files,
the original request, formalization, schemas, and theorem statuses remain
preserved. Repository source-identity validation and request-shape checks are
recorded with this update; no decider correctness or runtime experiment is
claimed.

Fresh checks on 2026-10-05:

- `python validate.py --integrity-only`: PASS source identity, file modes,
  explicit repairs, and exclusions.
- `git diff --check`: PASS.
- Standard-library JSON checks: PASS syntax, request-schema required
  fields/top-level types, all local lineage/dependency links, and the explicit
  null cost envelope. This was a targeted shape check, not a full JSON Schema
  validator or a mathematical admission test.

The original implementation test suite was not rerun for this documentation
checkpoint; no executable implementation was changed.
