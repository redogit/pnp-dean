# Dual Adversarial Proof Field

This program turns the two theorem directions

[
P=NP
qquad	ext{and}qquad
P\ne NP
]

into adversarial research populations over one fixed formal problem.

The populations are not voting on truth. They are producing constructions and counter-constructions for an exact referee.

## Core object

[
\mathcal P =
(
\Gamma,
O,
C_{=},
C_{\ne},
S,
R,
E
)
]

where:

- `Γ` — fixed complexity definitions and input semantics;
- `O` — current proof obligation;
- `C_=` — small population of constructive configurations;
- `C_≠` — small population of adversarial configurations;
- `S` — support roles invoked dynamically;
- `R` — exact referee/admission process;
- `E` — durable evidence, failures, costs, and remainder.

## Start here

1. [Charter](CHARTER.md)
2. [Roles](ROLES.md)
3. [Battle protocol](BATTLE_PROTOCOL.md)
4. [Universal obligations](OBLIGATIONS.md)
5. [Current status](STATUS.md)
6. [Receipt schema](BATTLE_RECEIPT.schema.json)
7. [Population configuration](POPULATION_CONFIG.json)

## Execution

Use Mathbox `research-program` to coordinate the program.

Each individual offensive/defensive move is a bounded `research-attempt`.
Use `proof-audit` for formal adjudication and `computation-audit` for finite DOE/counterexample work.

No local copies of those skills belong in this repository.

## Claim ceiling

The program is a research architecture. It proves neither theorem direction by existing.
