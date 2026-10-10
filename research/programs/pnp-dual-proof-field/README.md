# Dual Adversarial Proof Field

This program turns

[
P=NP
qquad\text{and}\qquad
P\ne NP
]

into opposing theorem directions over one immutable formal substrate.

The field is not a fixed population of agents. It is an obligation-driven generator system.

## Core object

[
\mathcal P=
(
\Gamma,
O,
G,
R,
E
)
]

where:

- `Γ` — fixed definitions and input semantics;
- `O` — the current obligation graph;
- `G` — generators accepting obligation slices;
- `R` — deterministic/formal referee and admission machinery;
- `E` — durable evidence, costs, failures, provenance, and remainder.

Each generator obeys:

[
G_i(O_i,Gamma,C,E,B)\rightarrow RequestBundle^{0..*}.
]

The RequestBundle is the unit of work.

## Executable lineage

The generator field is an explicit successor of:

[
FunctionalObject
\rightarrow
AnyFunctor/FunctionObject
\rightarrow
LocalPlane
\rightarrow
ObligationGenerator.
]

See:

- [FunctionalObject → AnyFunctor → generator lineage](FUNCTIONALOBJECT_ANYFUNCTOR_GENERATOR_LINEAGE.md)
- [Machine-readable lineage](LINEAGE.json)

The relation is provenance and lowering, not retroactive equivalence.

## Start here

1. [Charter](CHARTER.md)
2. [Cook / Clay formalization gate](COOK_CLAY_FORMALIZATION.md)
3. [Generators](GENERATORS.md)
4. [FunctionalObject / AnyFunctor lineage](FUNCTIONALOBJECT_ANYFUNCTOR_GENERATOR_LINEAGE.md)
5. [Battle/request protocol](BATTLE_PROTOCOL.md)
6. [Universal obligations](OBLIGATIONS.md)
7. [Current status](STATUS.md)
8. [Generator configuration](GENERATOR_CONFIG.json)
9. [Machine-readable lineage](LINEAGE.json)
10. [Obligation slice schema](OBLIGATION_SLICE.schema.json)
11. [Request bundle schema](REQUEST_BUNDLE.schema.json)
12. [Battle receipt schema](BATTLE_RECEIPT.schema.json)
13. [Feature / Property / Contribution / Value registry](registry/FPCV_REGISTRY.md)
14. [Machine-readable FPCV registry](registry/FPCV_REGISTRY.json)
15. [Current cross-state / Anti-Ouroboros note](registry/CURRENT_CROSS_STATE_2026-10-10.md)

## Execution

Use Mathbox `research-program` to coordinate the program.

A RequestBundle may be fulfilled with:

- `research-attempt`;
- `proof-audit`;
- `computation-audit`;
- `literature-check`;
- `research-state`.

No local copies of those skills belong in this repository.

## Claim ceiling

The generator architecture proves neither theorem direction by existing.
