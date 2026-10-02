# Proof Status and Open Claims

## Closed within this archive

- DEAN-4 is NP-complete for the unbounded family.
- Four distinct outputs reduce with polynomially many calls to an exact existence solver because four is fixed.
- Include/exclude recurrence and the reference branch fallback are exact.
- Compatibility q-core and exclusion-isolated inclusion are exact existence-preserving repairs.
- Independent Set / Vertex Cover complement duality, degree-pressure forcing, and the elementary O(k^2) cover kernel are exact.
- Pressure closure is monotone.
- Connected non-bipartite regular graphs provide a simultaneous plateau for several local reductions.
- Exact cut signatures, Pareto dominance, matching-frontier exponentiality, and the disjointness-rank barrier are proved.
- Certified affine/Macaulay rank gains are exact; logarithmic certified nullity is polynomially terminal.
- Lifted MPCA, curvature sandwich, stabilization, semantic Jacobian identities, and block-curvature bounds are proved as statements about the true solution set.
- Graph-Hilbert and fractional-dual frame theorems are proved.
- Multi-frame inconsistency and low-nullity rank collapse are exact certificates.
- Rank gain across candidate action subspaces is monotone submodular.

## Analysis-only versus operational

The true-solution-set PCA/Jacobian objects characterize semantic structure exactly but are generally not directly computable without solving the instance. The operational algorithm therefore uses only certified equations generated from the input and proved carrier consequences. Numerical PCA/SVD may steer candidate generation, but only exact rank/equation verification may change the logical state.

## Open claims — NOT proved

No theorem in this archive proves that every DEAN/Independent-Set instance reaches, after polynomially many gyro actions, any of:

- logarithmic certified nullity;
- a polynomial-size terminal carrier;
- constant-fraction frontier mass dissipation;
- logarithmic gyroscopic backdoor depth;
- polynomial frame entropy;
- a polynomial semantic-event basis with guaranteed progress.

Any universal theorem of sufficient strength to force polynomial exact solution of all DEAN-4 instances would imply P=NP. The archive deliberately marks these as research conjectures, not results.
