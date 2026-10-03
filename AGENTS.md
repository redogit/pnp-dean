# P vs NP / Dean — agent instructions

## Mission

Pursue the P-vs-NP research program without changing the standard definitions of P, NP, polynomial time, reduction, or NP-completeness. The active theorem directions are:

- `P_EQ_NP`: construct one correct deterministic polynomial-time algorithm for an NP-complete language.
- `P_NE_NP`: derive a representation-independent superpolynomial lower bound applying to every deterministic solver.

Neither direction is established. Keep the public claim ceiling `OPEN`.

## Authority order

1. Standard external complexity definitions and the exact encoded problem instance.
2. Exact theorem/proof artifacts and executable evidence in this repository.
3. `research/programs/pnp-dual-proof-field/CHARTER.md`.
4. Program obligations and current status.
5. Battle receipts and bounded computations.
6. Generated hypotheses and agent suggestions.

A later layer cannot silently increase the authority of an earlier one.

## Dynamic-agent protocol

Do not maintain permanent personas. Instantiate the smallest role needed by the current unresolved obligation.

Use the installed Mathbox skills rather than copying them into this repository:

- `research-program` — coordinate the sustained multi-route program.
- `research-attempt` — one bounded offensive or defensive mathematical route.
- `proof-audit` — adversarially check a proof/lemma/counterclaim.
- `computation-audit` — design or audit bounded DOE and exact finite computation.
- `literature-check` — verify external theorem dependencies.
- `research-state` — append-only claim/evidence/run tracking when an initialized ledger is available.
- `research-retrospective` — read-only program reconciliation.
- `research-init` — only for future architecture migration.

Use parallel-agent orchestration only for independent routes. Never allow parallel writers to mutate the same proof/state artifact.

## Required role separation

Generation, verification, admission, cost accounting, and memory are distinct functions.

`GENERATE != VERIFY != ADMIT`

A combatant may not referee its own claim. A different model instance alone does not create independent evidence.

## Shared invariants

- Same definitions for both theorem directions.
- Input bit length is the complexity variable.
- Construction, discovery, selection, transformation, reconciliation, verification, storage, rollback, and reconstruction all count.
- `ERROR != NO_PROVED`.
- `UNRESOLVED` is a valid research result.
- Bounded success is not a universal theorem.
- A carrier merge is lawful only if every protected current and future consequence is preserved.
- Structural similarity does not transfer evidence.
- Failed branches remain recoverable history.

## Program entry point

Read:

`research/programs/pnp-dual-proof-field/README.md`

Do not promote `P=NP` or `P!=NP` without a complete uniform theorem under the fixed definitions.
