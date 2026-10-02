# SQL Carrier

SQL is used as a polynomial closure/compiler layer, not as a 100-way combinatorial join generator.

Recommended flow:

1. canonicalize exclusion rows (`a < b`);
2. materialize both orientations for lookup;
3. compile candidate/conflict masks when the DB supports fixed-size bit strings;
4. detect components/signature duplicates;
5. feed only the residual kernel to the exact solver;
6. store proof/certificate events and reconstructed results;
7. independently verify cardinality and exclusion constraints using the original tables.

Avoid enumerating `C(400,100)` candidate rows or using 100 aliases of `students`.
