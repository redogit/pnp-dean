# Submodular Rank Gravity

Let R be the rowspace of current certified equations. Each candidate exact action a contributes a row subspace U_a after projection into the current unresolved feature space. For action set Q define

`f(Q)=dim(R + sum_{a in Q} U_a)-dim(R)`.

## Theorem 1 — f is monotone and submodular

Adding a subspace cannot reduce span dimension, so f is monotone. For `A subseteq B` and action a, the new dimensions contributed by U_a modulo the larger space `R+sum_{b in B}U_b` are a subset (in dimension) of those contributed modulo the smaller space for A. Hence marginal gain has diminishing returns, which is submodularity.

## Theorem 2 — Greedy rank-cover bound

Suppose all currently available actions together provide total new rank g, and some set of b* actions provides all g. At a greedy step with residual rank R_t, submodularity implies the sum of marginal gains of those b* optimal actions is at least R_t, so one has marginal at least `R_t/b*`. Greedy does at least as well:

`R_{t+1} <= (1-1/b*) R_t`.

Therefore `R_t <= g exp(-t/b*)`. Once the right side is below one, integer residual rank is zero. Greedy captures all currently available rank in at most

`ceil(b*(1+ln g))`

actions.

This optimizes extraction of already-available certified information; it does not prove that the available rank itself is sufficient to solve every instance.
