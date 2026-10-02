# DEAN-4 NP-Completeness

Membership in NP: four proposed cohorts can be checked for size, capacity, distinctness and exclusion-edge violations in polynomial time.

Hardness: map an Independent Set instance `(G,k)` to `G' = G disjoint-union K4`, set `q=k+1`. If `I` is an independent k-set of G, then `I` plus each of the four K4 vertices gives four distinct `(k+1)`-sets. Conversely any `(k+1)`-independent set in `G'` contains at most one K4 vertex and therefore at least k original vertices forming an independent set.

Therefore DEAN-4 is NP-complete for the unbounded family.
