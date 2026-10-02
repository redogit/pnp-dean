CREATE MATERIALIZED VIEW conflict AS
SELECT a AS u, b AS v FROM exclusions
UNION ALL
SELECT b AS u, a AS v FROM exclusions;

CREATE UNIQUE INDEX conflict_uv ON conflict(u,v);

-- A production 400-student PostgreSQL carrier can additionally compile
-- each row to bit(400) compatible/conflict masks for branch propagation.
