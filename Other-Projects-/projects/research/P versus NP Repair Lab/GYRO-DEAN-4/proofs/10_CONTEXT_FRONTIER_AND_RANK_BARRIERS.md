# Context Frontier and Rank Barriers

Across a cut `V=A dot-union B`, a partial independent set X in A has future signature

`(|X|, F_B(X))`, where `F_B(X)=N(X) intersect B`.

## Theorem 1 — Exact context equivalence

If X and Y have the same size and `F_B(X)=F_B(Y)`, every independent future Z in B is compatible with X iff it is compatible with Y. Therefore the two states are externally indistinguishable for exact-q continuation.

## Theorem 2 — Pareto dominance

If `|X|>=|Y|` and `F_B(X) subseteq F_B(Y)`, then X dominates Y for existence. Any completion Z of Y can be trimmed to `q-|X|` vertices; because X blocks no more future vertices, the trimmed set also completes X.

## Theorem 3 — A matching cut has 2^b nondominated states

Take b disjoint exclusion edges `a_i b_i`, with all a_i in A and all b_i in B. For each subset X of the a_i, the blocked future set is the corresponding subset of b_i and |X| equals its cardinality. If X is a proper subset of Y, Y has better selected cardinality but a strictly worse blocked set; otherwise the blocked sets are incomparable. Hence all `2^b` states are Pareto-nondominated.

This is a representation barrier, not a hardness proof for a matching graph.

## Theorem 4 — Disjointness matrix has full exponential rank

Index rows and columns by subsets of [b] and define `D_b[X,Y]=1` iff `X intersect Y` is empty. For b=1,

`D_1=[[1,1],[1,0]]`, whose determinant is -1 and rank is 2 over any field.

Independence across coordinates gives `D_b=D_1 tensor ... tensor D_1`, so Kronecker rank multiplication yields

`rank(D_b)=2^b`.

Thus ordinary exact linear factorization cannot compress this arbitrary cut to polynomial dimension.
