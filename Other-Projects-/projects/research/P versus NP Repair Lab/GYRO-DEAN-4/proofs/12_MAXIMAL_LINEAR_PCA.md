# Maximal Linear PCA: Exact Scope and Limitation

Let X be the nonempty set of valid cohort incidence vectors. Give every x in X a positive weight w_x summing to one, let `xbar=sum w_x x`, and let

`C=sum_x w_x (x-xbar)(x-xbar)^T`.

Let `L=span{x-y : x,y in X}`.

## Theorem 1 — PCA kernel equals all exact linear invariants

For any vector a,

`a^T C a = sum_x w_x (a^T(x-xbar))^2`.

All weights are positive, so this is zero iff `a^T(x-xbar)=0` for every x, i.e. iff a is orthogonal to L. Therefore

`ker(C)=L^perp`

and

`rank(C)=dim aff(X)`.

A linear equality `a^T x=beta` holds on every valid cohort iff `a in ker(C)`. Thus maximal PCA recovers every exact linear invariant of the true solution set.

## Theorem 2 — Exact rank gain in an existing affine system

Suppose certified equations are `A y=b`, with nullspace basis N and one solution y0. New certified equations `B y=c` become

`B N z = c-B y0`.

If inconsistent, no valid solution remains. Otherwise nullity drops by exactly `rank(BN)`.

## Corollary — Every new independent rank halves affine Boolean mass

If certified nullity is d, a d-dimensional affine subspace contains at most `2^d` Boolean points. Gain g gives nullity d-g and bound `2^(d-g)=2^d/2^g`.

## Limitation theorem — Linear PCA cannot be universal

For an empty exclusion graph with `1<=q<=n-1`, valid cohorts are the entire q-slice `{x in {0,1}^n : sum x_i=q}`. Differences obtained by swapping one selected and one unselected coordinate span `{z: sum z_i=0}`, which has dimension n-1. Hence the affine hull has dimension n-1 and the only independent linear equality is cardinality, even though the instance is trivial. A gyroscopic solver must therefore rotate away from PCA when another carrier is simpler.
