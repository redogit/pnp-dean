# Multi-Frame Rank Collapse

Every target-tight dual frame partitions vertices into support components P and contributes exact equations

`sum_{v in P} x_v = alpha(P)`.

Stack equations from multiple frames as `A x=b`.

## Theorem 1 — Inconsistent frame stack is a NO certificate

If

`rank(A) < rank([A|b])`,

no real vector satisfies all frame equations, hence no Boolean cohort satisfies them and the target is impossible.

A sparse Farkas-style certificate is any row multiplier lambda satisfying `lambda^T A=0` but `lambda^T b != 0`; independently checking those two identities certifies contradiction.

## Theorem 2 — Low-nullity frame stack is polynomially terminal

If the stack is consistent and `d=n-rank(A)`, choose d free coordinates in row-reduced form. At most `2^d` binary assignments to them exist, and each determines at most one full affine vector. Verify each candidate against original edges and cardinality. Therefore `d=O(log n)` gives polynomial exact solution.

## Near-tight frame family

For frame F of slack s_F, enumerate its weak-composition deficit patterns. Fixing a pattern turns every support component into one linear cardinality equation. For a family of frames, each joint deficit pattern yields an affine system. If its nullity is d(delta), exact work is bounded by

`sum_delta 2^{d(delta)} poly(n)`.

A crude bound is the number of joint deficit patterns times `2^{max_delta d(delta)}`. This is a correct carrier bound; no claim is made that it is polynomial on every graph.
