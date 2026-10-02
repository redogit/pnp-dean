# Capped Recurrence and Exact Factorization

Let `i_k(G)` denote the number of independent k-sets of G and define `c_k(G)=min(4,i_k(G))`.

## Theorem 1 — Include/exclude counting recurrence

For every vertex v:

`i_k(G) = i_k(G-v) + i_{k-1}(G-N[v])`.

Proof. Partition independent k-sets into those excluding v and those including v. Removing v from a set in the second class gives a bijection to independent `(k-1)`-sets of `G-N[v]`. QED.

With saturated addition `a ⊕ b = min(4,a+b)`:

`c_k(G) = c_k(G-v) ⊕ c_{k-1}(G-N[v])`.

Thus counts larger than four are irrelevant to the DEAN-4 decision.

## Theorem 2 — Disjoint-union factorization

If `G=G1 dot-union G2`, then

`I_G(z)=I_G1(z) I_G2(z)`

for the independence polynomial `I_G(z)=sum_k i_k(G) z^k`.

Proof. Every independent set of G is uniquely the disjoint union of one independent set from each component. QED.

Under 4-saturated arithmetic, coefficients can be convolved with all intermediate values capped at four.

## Theorem 3 — Join factorization

If `G=G1 vee G2` (all cross edges present), then for every `k>0`:

`i_k(G)=i_k(G1)+i_k(G2)`.

Proof. No nonempty independent set can contain a vertex from both sides. QED.

## Corollary

Connected-component and complement-component decomposition are exact polynomial closure operations and should be applied before exponential branching.
