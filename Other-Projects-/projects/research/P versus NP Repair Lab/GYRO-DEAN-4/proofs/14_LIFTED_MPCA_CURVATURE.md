# Lifted MPCA, Curvature, and Stabilization

Let X be the finite valid-solution set. Let `W_k` be the vector space of real-valued functions on X representable by multilinear polynomials of degree at most k, and let `h_k=dim W_k`.

## Theorem 1 — Lifted MPCA finds every degree-k identity

Let `Phi_k(x)` contain all square-free monomials of degree at most k and let

`M_k=sum_x w_x Phi_k(x) Phi_k(x)^T`

with all weights positive. For coefficient vector c,

`c^T M_k c = sum_x w_x (c^T Phi_k(x))^2`.

Therefore `c in ker(M_k)` iff the corresponding degree-at-most-k polynomial vanishes on every x in X. Also `rank(M_k)=h_k`.

## Theorem 2 — Curvature sandwich under conditioning

Fix variable x_i and branches `X_0={x:x_i=0}`, `X_1={x:x_i=1}`. Then

`h_k(X) <= h_k(X_0)+h_k(X_1) <= h_{k+1}(X)`.

The first inequality follows because restriction to both branches is injective. For the second, any pair of degree-k branch functions represented by p0,p1 is represented on X by `(1-x_i)p0 + x_i p1`, of degree at most k+1.

Define branch exposure

`epsilon_{i,k}=h_k(X_0)+h_k(X_1)-h_k(X)`

and residual nonlinear curvature

`kappa_{i,k}=h_{k+1}(X)-h_k(X_0)-h_k(X_1)`.

Both are nonnegative and

`h_{k+1}-h_k = epsilon_{i,k}+kappa_{i,k}`.

## Theorem 3 — Stabilization is final

If `h_{k+1}=h_k`, then `W_{k+1}=W_k`. Since multiplication by every coordinate maps W_k into W_{k+1}, W_k is closed under all coordinate multiplications. It contains 1, so it contains every Boolean monomial. Every function on finite Boolean set X is represented by a multilinear polynomial, hence `W_k=R^X` and

`h_k=|X|`.

No higher degree can reveal new semantic information after the first stabilization.
