# Regular Non-Bipartite Repair Plateau

Let G be connected, non-bipartite, d-regular, and `n>2d`.

## Theorem 1 — Degree-pressure forcing stalls

Every vertex cover has size at least n/2: G has `dn/2` edges and one cover vertex can cover at most d edges. Thus any feasible cover budget k satisfies `k>=n/2>d=deg(v)` for every v. The forcing rule `deg(v)>k` fires nowhere.

## Theorem 2 — Fractional Vertex Cover optimum is n/2

The primal assignment `x_v=1/2` is feasible with value n/2. In the dual fractional matching, assign `y_e=1/d` to every edge. Each vertex constraint is tight and the dual value is `(dn/2)/d=n/2`. Strong LP duality gives `tau_f(G)=n/2`.

The Vertex Cover LP has half-integral extreme optima. For any half-integral optimum partition vertices into `V0,V1/2,V1`. Objective n/2 implies `|V0|=|V1|`. Every neighbor of a V0 vertex lies in V1; counting d|V0| incident edges and using d|V1|=d|V0| shows every edge incident with V1 enters V0. Hence `V0 union V1` is a connected component. Connectedness gives either empty or all vertices; the latter would make G bipartite. Therefore every half-integral optimal extreme point has all coordinates 1/2. Nemhauser-Trotter persistency exposes no 0/1 vertex at the root.

## Theorem 3 — No proper crown

Suppose `(C,H)` is a crown: C is independent, H=N(C), and a matching saturates H into C. Then `|H|<=|C|`. Since G is d-regular all d|C| edges leaving C enter H, whose total degree capacity is d|H|, so `|C|<=|H|`. Equality follows, and all edges incident with H must enter C. Thus `C union H` is a connected component; connectedness makes it all of V, yielding a bipartition, contradiction.

## Theorem 4 — G and its complement are connected

G is connected by hypothesis. If the complement were disconnected, G would be a nontrivial join `A vee B`. Every vertex of A has at least |B| cross-neighbors, so `|B|<=d`; similarly `|A|<=d`, giving `n<=2d`, contradiction.

## Corollary

Pressure, component/co-component splitting, half-integral LP persistency, and crown reduction can all stall simultaneously on an infinite structural family. Local repair alone is therefore not a universal collapse mechanism.
