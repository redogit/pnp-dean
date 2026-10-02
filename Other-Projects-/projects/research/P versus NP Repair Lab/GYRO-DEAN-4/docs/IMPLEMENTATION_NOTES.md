# Implementation Notes

- The included C++ solver is a compact exact reference core with a functional branch fallback and q-core/isolate reductions.
- Advanced LP, crown, dual-frame, SAT, factor and Macaulay carriers are deliberate extension hooks in the reference build. They must set `changed=true` only for certificate-backed exact progress.
- For production exact algebra, replace the bounded `int64_t` Bareiss helper with a big-integer or verified modular backend.
- Numerical SVD/PCA must never certify correctness. Use it only to prioritize actions, then verify gain with exact rank.
- Memoization of YES witnesses requires context-aware reconstruction. The compact reference caches only safe NO residual states.
