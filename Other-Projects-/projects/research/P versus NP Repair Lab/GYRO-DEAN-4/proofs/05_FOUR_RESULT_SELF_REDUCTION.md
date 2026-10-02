# Four-Result Self-Reduction

Assume exact existence solver O(G,q). After solutions S1..Sj have been found, a new q-set T distinct from every Si exists iff for some tuple vi in Si, the graph G-{v1..vj} still contains a q-set. If T is distinct from Si then choose vi in Si\T; conversely any q-set surviving deletion of vi cannot equal Si.

For four total results, at most q + q^2 + q^3 existence calls are needed.
