# Claims Index

This index separates proved claims, executable evidence, and open research claims.

## Proved theorem files

1. `proofs/01_DEAN4_NP_COMPLETENESS.md`
2. `proofs/02_PRESSURE_CLOSURE.md`
3. `proofs/03_CONTEXT_SIGNATURE.md`
4. `proofs/04_CERTIFIED_RANK_GRAVITY.md`
5. `proofs/05_FOUR_RESULT_SELF_REDUCTION.md`
6. `proofs/06_SOLVER_CORRECTNESS_AND_TERMINATION.md`
7. `proofs/07_CAPPED_RECURRENCE_AND_FACTORIZATION.md`
8. `proofs/08_VERTEX_COVER_DUALITY_AND_KERNEL.md`
9. `proofs/09_REGULAR_CORE_PLATEAU.md`
10. `proofs/10_CONTEXT_FRONTIER_AND_RANK_BARRIERS.md`
11. `proofs/11_GYRO_CLOSURE_AND_FRONTIER_MASS.md`
12. `proofs/12_MAXIMAL_LINEAR_PCA.md`
13. `proofs/13_CERTIFIED_MACAULAY_ENGINE.md`
14. `proofs/14_LIFTED_MPCA_CURVATURE.md`
15. `proofs/15_SEMANTIC_JACOBIAN_AND_BLOCK_ATTACKS.md`
16. `proofs/16_GRAPH_HILBERT_BRIDGE.md`
17. `proofs/17_DUAL_SUPPORT_FRAME_THEOREMS.md`
18. `proofs/18_MULTI_FRAME_RANK_COLLAPSE.md`
19. `proofs/19_SUBMODULAR_RANK_GRAVITY.md`
20. `proofs/20_PROOF_STATUS_AND_OPEN_CLAIMS.md`

## Executable evidence

- hand-picked exact tests in `tests/test_solver.cpp`;
- exhaustive small-graph comparison against brute force in `tests/test_exhaustive.cpp`;
- G20 cubic calibration graph in `evidence/G20_CORE.md` and `examples/g20_*.csv`.

## Open universal claims

The archive does not claim P=NP. In particular, no universal polynomial bound on gyro depth, frame entropy, certified nullity, semantic-event progress, or frontier mass has been proved.
