# Battle protocol

## 0. Freeze the field

For each battle record:

- exact problem instance/family;
- current theorem direction;
- current obligation;
- fixed definitions;
- claim ceiling;
- starting carrier;
- allowed evidence.

Neither side may modify these after seeing the outcome.

## 1. Select one obligation

Choose the smallest unresolved obligation that can change the universal result.

Primary obligations are in [OBLIGATIONS.md](OBLIGATIONS.md).

Do not run a battle merely because a configuration is available.

## 2. Populate small combatant sets

Default:

- 4 active offense configurations;
- 4 active defense configurations;
- hard maximum 8 per side.

Additional candidates remain archived/cold until diversity or repair justifies promotion.

Population slots are mechanism-diverse, not score-ranked duplicates.

## 3. Matchmaking

A defense configuration should attack an offense configuration only when its failure mode is relevant.

Examples:

- quotient -> aliasing/future-divergence defense;
- decomposition -> coupling/discovery-cost defense;
- circuit -> construction/size/uniformity defense;
- induction -> successor/nonuniformity defense;
- reconciliation -> oracle-leakage defense.

Use full cross-product combat only when the population is small enough and every pairing is semantically meaningful.

## 4. Execute

Each pair produces a bounded research attempt.

Offense must state a falsifiable exact claim.

Defense must state the countercondition it is trying to produce.

DOE is targeted at that claim, not random benchmarking.

## 5. Charge work

Cost Accountant records all work that would belong to the proposed algorithm.

Research-only oracle cost is separately recorded.

An oracle may guide discovery, but any production claim must replace it with explicit circuitry/algorithmic operations and charge them.

## 6. Referee

The Referee checks the exact claim, evidence, and scope.

No combatant declares victory.

A bounded finite sweep can reject a universal claim by counterexample, but cannot establish universality by absence of counterexamples.

## 7. Repair

For `REPAIRABLE`, instantiate the Repairer against the exact failure witness.

Run the same attack again before widening the claim.

## 8. Distill

Repeated offense wins should become a reusable exact lemma or certified rule.

Repeated defense wins should become a counterfamily or obstruction lemma.

Do not merely accumulate battle counts.

## 9. Population update

Retain:

- unique surviving mechanisms;
- strongest counterexamples;
- unresolved but non-dominated routes;
- exact scoped terminals.

Retire:

- semantic duplicates;
- mechanisms strictly subsumed by a certified successor;
- disproved universals.

Retirement preserves history.

## 10. Universal promotion gates

### P=NP

Requires one shared construction satisfying:

- universal coverage;
- exact local rules;
- one fixed polynomial total-work bound;
- total deterministic decision;
- no hidden oracle;
- reconstructible witnesses where claimed.

### P!=NP

Requires a lower-bound theorem quantified over all deterministic solvers in the fixed model.

Failure of every member of the current offense population is not sufficient.
