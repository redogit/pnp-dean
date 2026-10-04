# Obligation / request protocol

The historical word "battle" remains for receipts, but execution is request-driven.

## 0. Freeze the field

Record:

- exact problem instance/family;
- theorem direction;
- current parent obligation;
- fixed definitions;
- claim ceiling;
- starting carrier;
- allowed evidence.

These do not mutate after seeing an outcome.

## 1. Slice the obligation

Decompose the current obligation only as far as necessary:

[
Oightarrow{O_1,ldots,O_m}.
]

Each slice must state what consequence changes if it is solved or broken.

## 2. Generator acceptance

A generator activates only by accepting one slice `O_i`.

It receives only:

- the slice;
- fixed definition references;
- relevant carrier/evidence references;
- a declared budget.

It may decline by emitting zero RequestBundles and an explicit remainder.

## 3. Generate requested parts

The generator emits zero, one, or many RequestBundles.

A RequestBundle asks for exact parts such as:

- theorem/lemma;
- carrier;
- counterexample;
- decomposition;
- circuit;
- cost bound;
- DOE panel;
- source verification;
- repair;
- reconstruction map.

It also declares dependencies, counterprobes, acceptance criteria, output contract, and any child obligation requests.

## 4. Fulfill requests

Use the smallest appropriate research skill.

Independent RequestBundles may execute in parallel.

Dependent bundles wait for their declared prerequisites.

No result inherits authority merely because another generator requested it.

## 5. Cost requests

Every algorithmic RequestBundle must pass through `COST_GENERATOR`.

Unknown construction/discovery/reconciliation/recovery cost becomes a child obligation instead of an assumption.

Research-only oracle use is allowed for discovery but must be marked; production claims must replace the oracle with explicit operations.

## 6. Adversarial generation

Constructive and lower-bound generators may request attacks against each other's parts.

Examples:

- quotient -> aliasing/future-divergence request;
- decomposition -> coupling/discovery-cost request;
- circuit -> construction/size/uniformity request;
- induction -> successor/nonuniformity request;
- reconciliation -> hidden-oracle request.

No fixed cross-product is required. Match requests by consequential relevance.

## 7. Referee generation

`REFEREE_GENERATOR` converts a claimed result into verification requests.

The generator does not decide the result.

Formal/deterministic checking and admissible evidence yield one of:

- `ADMIT_SCOPED`;
- `REJECT_COUNTEREXAMPLE`;
- `REPAIRABLE`;
- `UNRESOLVED`;
- `INVALID_ATTACK`.

Absence of a bounded counterexample never proves universality.

## 8. Repair recursion

For `REPAIRABLE`:

[
FailureWitness
ightarrow
REPAIR_GENERATOR
ightarrow
RequestedMissingParts
ightarrow
SameCounterprobe.
]

A different unrelated mechanism is a new route, not a repair.

## 9. Distill and recurse

Results update the obligation graph:

[
RequestedParts
ightarrow Evidence
ightarrow ResolvedParts + ResidualObligations.
]

Repeated constructive successes should become certified reusable rules.

Repeated failures should become counterfamilies or obstruction lemmas.

## 10. Universal promotion gates

### P=NP

Requires one construction with:

- universal coverage;
- exact local rules;
- one fixed polynomial total-work bound;
- total deterministic decision;
- no hidden oracle;
- reconstructible witnesses where claimed;
- the Cook/Clay promotion counterprobe passes: fast verification of a supplied witness, a known route/index, or a Float64/path representation is not treated as a universal constructor unless one deterministic total decider and one fixed polynomial total-work bound in encoded input length are proved.

### P!=NP

Requires a lower-bound theorem quantified over all deterministic solvers in the fixed model.

Failure of every construction generated so far is insufficient.
