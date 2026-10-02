# Pressure Closure

At a residual with `m` candidates and `t` required selections, let omission budget `k=m-t`. Rotate to Vertex Cover. If `deg(v)>k`, excluding v from the cover would require all its neighbors in the cover, exceeding k; hence v is forced into the cover and forced out of the cohort.

When a forced cover vertex v is removed, k falls by one. For surviving u, pressure `rho(u)=deg(u)-k` remains constant if uv is an edge and rises by one otherwise. Pressure is therefore monotone under forced repairs. Enabled pressure repairs cannot later become disabled, yielding a finite least fixed point.
