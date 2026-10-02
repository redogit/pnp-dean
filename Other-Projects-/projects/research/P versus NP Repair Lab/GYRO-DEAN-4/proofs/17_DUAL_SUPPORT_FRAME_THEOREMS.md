# Fractional-Dual Support Frames

Consider an all-1/2 Vertex-Cover core. Its dual is a fractional perfect matching: nonnegative edge weights y with `sum_{e incident v} y_e=1` for every vertex.

## Lemma — Extreme support components are edges or odd cycles

At an extreme point, positive support columns of the vertex-edge incidence matrix are linearly independent. If a connected support component has a degree-1 vertex, its sole edge has weight 1; the opposite endpoint can have no other positive edge, so the component is a single edge. Otherwise minimum support degree is at least two. Linear independence gives `|E_support|<=|V_support|`; connected minimum degree two gives `|E_support|>=|V_support|`, hence equality and every degree is two: the component is a cycle. An even cycle admits a nonzero alternating +/- perturbation preserving all vertex sums, contradicting extremality. Thus the cycle is odd. Solving equal vertex sums on an odd cycle gives weight 1/2 on every cycle edge.

Therefore an extreme fractional perfect matching decomposes the vertex set into disjoint weight-1 edges and weight-1/2 odd cycles.

## Theorem 1 — Odd-cycle defect bound

Suppose the frame has e edge components and c odd cycles `C_{2r_j+1}`. Any independent set takes at most one vertex from each edge and at most r_j from each odd cycle. Hence

`alpha(G) <= e + sum_j r_j = (n-c)/2`.

Equivalently every vertex cover has size at least `(n+c)/2`.

## Theorem 2 — Tight-frame factorization

If target q equals `(n-c)/2`, any valid q-independent set must attain the local upper bound in every support component, because the sum of component upper bounds already equals q. Hence each support edge contributes exactly one selected endpoint and each odd cycle C_{2r+1} contributes exactly r selected vertices.

This turns the residual problem into a finite-domain CSP over support components, with original cross-component exclusion edges as compatibility constraints.

## Near-tight frame corollary

Define frame slack `s_F=(n-c(F))/2-q`. For a q-cohort let `d_P=alpha(P)-|I intersect P|` on every support component. Then each d_P is a nonnegative integer and

`sum_P d_P=s_F`.

Thus at most s_F components can have positive deficit. There are at most `C(h+s_F-1,s_F)` weak-composition deficit patterns for h components. Small slack yields an almost-tight factor carrier rather than a return to raw search.
