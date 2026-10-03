# Dual Adversarial Proof Field

This program turns

[
P=NP
qquad	ext{and}qquad
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
G_i(O_i,Gamma,C,E,B)ightarrow RequestBundle^{0..*}.
]

The RequestBundle is the unit of work.

## Start here

1. [Charter](CHARTER.md)
2. [Generators](GENERATORS.md)
3. [Battle/request protocol](BATTLE_PROTOCOL.md)
4. [Universal obligations](OBLIGATIONS.md)
5. [Current status](STATUS.md)
6. [Generator configuration](GENERATOR_CONFIG.json)
7. [Obligation slice schema](OBLIGATION_SLICE.schema.json)
8. [Request bundle schema](REQUEST_BUNDLE.schema.json)
9. [Battle receipt schema](BATTLE_RECEIPT.schema.json)

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
