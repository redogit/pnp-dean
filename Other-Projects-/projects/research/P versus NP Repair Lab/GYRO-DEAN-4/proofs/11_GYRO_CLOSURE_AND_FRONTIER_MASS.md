# Gyroscopic Closure and Frontier Mass

## Theorem 1 — Closure soundness

Assume every carrier rotation preserves the decision predicate, every learned consequence is logically valid, and every destructive repair has an exact reconstruction map. Then any finite composition of such operations preserves the decision predicate. Therefore the least fixed point `Gamma_infinity(S)` reached by fair finite exact closure has the same YES/NO answer as S.

## Theorem 2 — Frontier Mass Contraction

Let M(S) be a positive integer mass for unresolved canonical states. Suppose initial mass is at most polynomial p(n), and every unresolved state has a polynomially discoverable exact action whose distinct nonterminal closed children C satisfy

`1 + sum_{T in C} M(T) <= M(S)`.

Let Q be the live frontier and `Psi(Q)=sum_{S in Q} M(S)`. Replacing S by C decreases Psi by at least one. Since Psi starts at most p(n) and is nonnegative, at most p(n) expansions occur. If each expansion is polynomial, total runtime is polynomial.

## Corollary

A proof of such a polynomially bounded mass for every DEAN state would imply DEAN-4 is in P; since DEAN-4 is NP-complete, it would imply P=NP.

## Theorem 3 — Polynomial semantic-event progress

Alternatively, suppose all irreversible learned events come from a universe E_n of polynomial size and every nonsolved round derives at least one previously unknown sound event. The potential `|E_n-K|` falls by at least one per round, so only polynomially many rounds are possible.

This is a sufficient proof template, not a claim that such a universal event basis has been found.
