# Vertex-Cover Duality and Elementary Kernel

Let a residual graph have `m` active candidates and require `q` selected students. Put `k=m-q`.

## Theorem 1 — Independent Set / Vertex Cover duality

For every `I subseteq V`:

`I is independent` iff `V-I` is a vertex cover.

Therefore an independent set of size at least q exists iff a vertex cover of size at most `k=m-q` exists. Exact q follows by taking any q-subset of a larger independent set.

## Theorem 2 — Pressure forcing

If `deg(v)>k`, every vertex cover of size at most k contains v.

Proof. If v were omitted from a cover, every neighbor of v would have to be included, requiring more than k vertices. QED.

In cohort coordinates, v is therefore forced out.

## Theorem 3 — Elementary O(k^2) kernel after pressure closure

After Theorem 2 is applied to exhaustion, maximum degree is at most k. If more than `k^2` edges remain, no k-cover exists, because k chosen vertices can cover at most k times k incident edges.

Otherwise at most `2k^2` vertices are incident with any remaining edge. All other vertices are isolates and can be handled without combinatorial search.

Hence the nontrivial residual has at most `2k^2` vertices.

## Corollary

When `k=O(log n)`, even a `2^k poly(n)` exact cover branch is polynomial in n. This is a tractable gyro carrier, not a universal proof that k is always logarithmic.
