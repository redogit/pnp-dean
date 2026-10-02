# Certified Macaulay / MPCA Engine

Let the exact Boolean polynomial system contain:

- `x_i^2-x_i=0` for every variable;
- `x_u x_v=0` for every exclusion edge uv;
- `sum_i x_i-q=0`.

Choose a finite feature dictionary M of square-free monomials, always including 1 and all x_i. Let `y=Phi_M(x)`.

## Theorem 1 — Certified linearization is sound

Multiply any already-proved polynomial identity by selected monomials, reduce Boolean powers `x_i^2 -> x_i`, and express the result in M. Every resulting row `a^T y=b` holds on every valid cohort because polynomial multiplication and Boolean reduction preserve equality on Boolean solutions.

Therefore the accumulated system `A y=b` is an affine relaxation containing every valid feature vector.

## Theorem 2 — Affine hypercube bound

If `A y=b` has m feature coordinates and rank r, its affine dimension is `d=m-r`. A d-dimensional affine subspace of R^m contains at most `2^d` Boolean vectors: choose d free pivot-complement coordinates; each binary assignment to them determines at most one full affine vector.

Because the feature dictionary contains all singleton x_i, distinct cohorts have distinct feature vectors. Hence the number of valid cohorts is at most `2^d`.

## Corollary — Logarithmic certified nullity is polynomially terminal

If M has polynomial size and `d=O(log n)`, enumerate the at most `2^d` affine Boolean candidates, check monomial consistency and verify the original graph/cardinality constraints. This is polynomial time.

## Theorem 3 — Cardinality ladder

For an independent index set S of size s, multiply `sum_i x_i=q` by `x_S`. Boolean reduction and edge-zero identities give

`sum_{i notin S, S union {i} independent} x_{S union {i}} = (q-s) x_S`.

This is an exact family of higher-order extension equations generated without knowledge of the unknown solution set.

## Branch mass law

If x_i is not already fixed by the current affine system, adding `x_i=0` or `x_i=1` reduces affine nullity by one in each consistent branch before additional repair. If the two branches gain extra certified ranks g0 and g1 after closure, their total affine mass is bounded by

`2^(d-1-g0) + 2^(d-1-g1)`.

Thus ordinary branching can conserve mass, while post-branch learned rank creates genuine dissipation.
