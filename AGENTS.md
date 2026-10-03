# P vs NP / Dean — agent instructions

## Mission

Pursue the P-vs-NP research program without changing the standard definitions of P, NP, polynomial time, reduction, or NP-completeness.

- `P_EQ_NP`: construct one correct deterministic polynomial-time algorithm for an NP-complete language.
- `P_NE_NP`: derive a representation-independent superpolynomial lower bound applying to every deterministic solver.

Neither direction is established. Keep the public claim ceiling `OPEN`.

## Authority order

1. Standard complexity definitions and the exact encoded problem instance.
2. Exact theorem/proof artifacts and executable evidence.
3. `research/programs/pnp-dual-proof-field/CHARTER.md`.
4. Universal obligations and current status.
5. Request bundles, battle receipts, and bounded computations.
6. Generated hypotheses.

A later layer cannot silently increase the authority of an earlier one.

## Obligation-driven generator protocol

Do not maintain permanent personas, fixed agent rosters, or fixed population sizes.

Every active process accepts a consequential slice of the current obligation and acts as a generator:

[
G_i(O_i,Gamma,C,E,B)ightarrow RequestBundle^{0..*}.
]

A generator receives only the obligation slice and context it needs. It emits requested parts, dependencies, counterprobes, acceptance criteria, cost requirements, child obligations, and an explicit remainder.

Read `research/programs/pnp-dual-proof-field/GENERATORS.md`.

Use installed Mathbox skills as execution machinery:

- `research-program` — coordinate sustained multi-route work.
- `research-attempt` — execute one requested proof/counterexample route.
- `proof-audit` — check a proof, lemma, or attack.
- `computation-audit` — DOE / exact bounded computation.
- `literature-check` — verify external theorem dependencies.
- `research-state` — append-only state and dependency tracking when initialized.
- `research-retrospective` — read-only reconciliation.
- `research-init` — only for future repository architecture migration.

Use parallel orchestration only when request bundles are independent. Never allow parallel writers to mutate the same proof/state artifact.

## Separation rules

`GENERATE != VERIFY != ADMIT`

A generator may generate referee requests, but may not admit its own claim.

A different model instance alone does not create independent evidence.

## Shared invariants

- Same definitions for both theorem directions.
- Input bit length is the complexity variable.
- Construction, discovery, selection, transformation, reconciliation, verification, storage, rollback, and reconstruction all count.
- Unknown cost becomes an obligation.
- `ERROR != NO_PROVED`.
- `UNRESOLVED` is valid research output.
- Bounded success is not a universal theorem.
- A carrier merge is lawful only if protected present and future consequences are preserved.
- Structural similarity does not transfer evidence.
- Failed branches remain recoverable history.
- Whole-history loading is forbidden by default; memory retrieval is obligation-local.

## Program entry point

Read:

`research/programs/pnp-dual-proof-field/README.md`

Do not promote `P=NP` or `P!=NP` without a complete uniform theorem under the fixed definitions.
