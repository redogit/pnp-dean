# Graph–Hilbert Bridge

Let X_q be the set of independent q-set incidence vectors of G. Let `W_k(X_q)` be the degree-at-most-k function space and `h_k=dim W_k`.

## Theorem — Degree-at-most-k functions are spanned by independent k-set monomials

Take a square-free monomial `x_S` with `|S|=s<=k`. On the fixed-q slice:

`sum_{T superset S, |T|=k} x_T = C(q-s,k-s) x_S`.

Proof pointwise. If x_S=0, every term on the left is zero. If x_S=1, exactly q-s additional selected coordinates exist and exactly `C(q-s,k-s)` k-subsets of the selected cohort contain S.

Hence, over characteristic zero,

`x_S = [1/C(q-s,k-s)] sum_{T superset S, |T|=k} x_T`.

If T contains an exclusion edge, x_T vanishes on every valid cohort. Therefore W_k is spanned by degree-k monomials indexed only by independent k-sets.

Let i_k(G) be the number of independent k-sets. Then

`h_k(X_q) <= i_k(G)`.

## Corollary — Quadratic bound

`h_2 <= C(n,2)-|E|`.

The defect `Delta_k=i_k(G)-h_k` measures locally legal k-patterns that are globally linearly dependent across complete q-cohorts.
