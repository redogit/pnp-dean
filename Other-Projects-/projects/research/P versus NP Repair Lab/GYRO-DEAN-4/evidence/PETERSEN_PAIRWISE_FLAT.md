# Petersen Pairwise-Flat Calibration

For the Petersen graph in `examples/petersen_exclusions.csv`, the following five independent 4-sets exist:

- `{0,2,8,9}`
- `{0,3,6,7}`
- `{1,3,5,9}`
- `{1,4,7,8}`
- `{2,4,5,6}`

Every vertex occurs in exactly two of these five sets, so no vertex is forced in or out across the displayed maximum witnesses.

The graph has 30 nonedges, while the five 4-sets contain `5*C(4,2)=30` pair occurrences. Direct inspection shows these pair occurrences are distinct, so every nonedge appears together in one displayed maximum set. Each nonedge also realizes 10, 01 and 00 across the remaining witnesses; each edge realizes all graph-permitted patterns 10, 01, 00 but never 11.

Thus the complete unary/pairwise no-good basis learns nothing beyond the original exclusion edges on this calibration object. This falsifies a universal "pairwise facts always progress" claim without implying that the Petersen instance is hard for stronger carriers.
