# Obligation-driven generators

The field does not maintain fixed agents or populations.

Every active process is a generator:

[
G_i(O_i,Gamma,C,E,B)ightarrow R_i^{0..*}
]

where:

- `O_i` — the accepted slice of the current obligation;
- `Γ` — fixed definitions and theorem-direction boundary;
- `C` — current carrier/context references;
- `E` — relevant evidence/history references;
- `B` — resource/cost budget;
- `R_i^{0..*}` — zero, one, or many RequestBundles.

A generator wakes only when it can accept an obligation slice. It does not receive the whole project by default.

## Inherited executable shape

This contract is not provenance-free. It lowers the preserved line:

[
FunctionalObject
ightarrow
AnyFunctor/FunctionObject
ightarrow
LocalPlane
ightarrow
ObligationGenerator.
]

The inheritance is structural:

- plural `Operations[]` → zero-to-many requested parts/operations;
- plural `Checks[]` → acceptance criteria/counterprobes;
- ordered buffers → obligation-local carrier/context;
- reusable links → admitted route/dependency edges;
- `NullTarget<T>()` → retained residual obligation;
- `AnyInvocation<T>` → explicit obligation-slice acceptance;
- receipt → request/result receipt;
- Homeward → recovery reference;
- local route index → obligation-local memory retrieval.

Do not collapse the stages:

[
FunctionalObject \neq AnyFunctor \neq LocalPlane \neq ObligationGenerator.
]

See `FUNCTIONALOBJECT_ANYFUNCTOR_GENERATOR_LINEAGE.md` and `LINEAGE.json`.

## Common output: RequestBundle

Every generator emits requested parts, not a rhetorical answer.

A RequestBundle contains:

- accepted obligation slice;
- source-lineage references when inherited machinery matters;
- exact inputs still needed;
- requested parts to construct/recover/test;
- candidate operations allowed;
- counterprobes required;
- dependencies;
- acceptance criteria;
- cost envelope;
- output contract;
- zero-to-many child obligation requests;
- explicit remainder.

This is the lowered AnyFunctor shape: one accepted obligation object may yield zero, one, or many requested parts and may recursively request further obligation slices.

## Generator family

### P_EQ_NP_GENERATOR

Accepts a constructive obligation slice.

Requests only parts needed to produce exact polynomial progress, such as:

- carrier;
- decomposition;
- circuit;
- recognizer;
- reconciliation rule;
- induction step;
- progress potential;
- terminal algorithm;
- reconstruction map.

It must request its own falsification probes.

### P_NE_NP_GENERATOR

Accepts a failure/lower-bound obligation slice.

Requests parts capable of defeating or generalizing a constructive claim:

- aliasing pair;
- future-divergence witness;
- hidden-oracle reduction;
- coupling family;
- construction-cost family;
- nonuniform-exponent witness;
- recovery failure;
- uncovered residual.

Repeated defeats should generate a request to distill a counterfamily or representation-independent obstruction.

### EXPLORER_GENERATOR

Accepts an obligation whose current representation is stalled.

Requests alternate mathematical shapes or carriers without changing the obligation:

- quotient coordinates;
- decomposition;
- dual formulation;
- circuit replacement;
- cross-domain primitive;
- alternate serialization.

It transfers methods, not evidence authority.

### REPAIR_GENERATOR

Accepts an exact failure witness.

Requests the minimum missing distinction or transform needed to repair that failure, followed by the same counterprobe.

[
Failureightarrow MissingPartightarrow MinimalRepairightarrow SameAttack
]

### DIVERSITY_GENERATOR

Accepts the current active request set.

Requests only missing mechanism classes or deduplication decisions.

It may collapse duplicate occurrences into one semantic mechanism while preserving every occurrence/provenance edge.

No scalar fitness score may erase a unique mechanism.

### MEMORY_GENERATOR

Accepts the current obligation slice and asks historical storage only for consequential predecessors:

- prior exact rules;
- counterexamples;
- failed universals;
- source identities;
- costs;
- reconstruction paths;
- unresolved remainder;
- lineage nodes/edges needed to reconstruct the mechanism.

It is retrieval-on-demand, not whole-history loading.

### COST_GENERATOR

Accepts an algorithmic obligation slice and requests all lifecycle counters necessary to translate the proposal into the standard deterministic model:

[
C_{total}=C_{encode}+C_{discover}+C_{build}+C_{select}+C_{transform}+C_{reconcile}+C_{verify}+C_{rollback}+C_{recover}.
]

Unknown cost components become child obligations.

Cook/Clay mapping for every constructive algorithmic claim:

- bind `n` to the fixed encoded input length `|x|`;
- distinguish checking a supplied certificate from constructing or deciding from `x` alone;
- charge representation construction, route discovery, certificate construction/recovery, and every lifecycle term above;
- require one fixed exponent for total work before universal constructive promotion, not one polynomial per route, family, or input size.

See `COOK_CLAY_FORMALIZATION.md`.

### REFEREE_GENERATOR

Accepts a claimed result and generates the exact verification requests required for admission.

It may request:

- proof audit;
- computation audit;
- external theorem verification;
- reconstruction check;
- lineage/authority check;
- cost audit;
- counterexample replay.

The generator does not decide truth. Deterministic/formal checks and admissible evidence determine the verdict.

For any universal constructive promotion, the referee must demand the missing bridge explicitly: one deterministic decider on `x` alone plus one fixed polynomial total-work bound in encoded input length. Fast verification of a supplied witness, a known route/index, or a Float64/path representation does not supply that bridge by itself. Such mechanisms may remain scoped evidence; without the bridge, universal promotion remains `UNRESOLVED`.

## Recursion

The field advances by obligation decomposition:

[
O
ightarrow
\{O_1,ldots,O_m\}
ightarrow
\{G_i(O_i)\}
ightarrow
\{R_{ij}\}
ightarrow
Evidence
ightarrow
ResidualObligations.
]

A request that cannot name a consequential obligation slice is not admitted to the active field.
