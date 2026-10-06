"""A_0009: deterministic one-bit descent. Refuted as an exact decider.

Only encoded x is a problem input. No witness or oracle enters this module.
Coordinates are 0.0/1.0; energy and all decisions use exact integer arithmetic.
The false-NO rule is retained so the original candidate remains reproducible.
"""
from dataclasses import dataclass

from json_codec import decode


@dataclass(frozen=True)
class Run:
    valid_input: bool
    decision: str
    witness: tuple[str, ...]
    path: tuple[tuple[float, ...], ...]
    energies: tuple[int, ...]
    counts: dict[str, int]


def run_candidate(x: bytes) -> Run:
    graph = decode(x)
    if graph is None:
        return Run(False, 'INVALID', (), (), (), {'input_bytes': len(x)})
    N, M = len(graph.ids), len(graph.edges)
    adjacency = [[False] * N for _ in range(N)]
    for u, v in graph.edges:
        adjacency[u][v] = adjacency[v][u] = True
    b = [0.0] * N
    counts = {'input_bytes': len(x), 'adjacency_cells': N*N,
              'edge_insertions': M, 'energy_evaluations': 0,
              'coordinate_terms': 0, 'edge_terms': 0,
              'trial_flips': 0, 'rollbacks': 0, 'accepted_flips': 0,
              'trace_coordinate_copies': N, 'verification_pairs': 0,
              'witness_ids': 0, 'witness_utf8_bytes': 0}

    def energy() -> int:
        counts['energy_evaluations'] += 1
        counts['coordinate_terms'] += N
        counts['edge_terms'] += M
        # int(0.0), int(1.0), and products of these bits are exact.
        return (N+1)*sum(int(b[u])*int(b[v]) for u,v in graph.edges) - sum(int(z) for z in b)

    current = energy()
    path, energies = [tuple(b)], [current]
    while True:
        best = None
        for j in range(N):
            b[j] = 1.0-b[j]
            counts['trial_flips'] += 1
            score = energy()
            b[j] = 1.0-b[j]
            counts['rollbacks'] += 1
            choice = (score, j)
            if score < current and (best is None or choice < best):
                best = choice
        if best is None:
            break
        current, j = best
        b[j] = 1.0-b[j]
        counts['accepted_flips'] += 1
        counts['trace_coordinate_copies'] += N
        path.append(tuple(b))
        energies.append(current)

    selected = [j for j in range(N) if b[j] == 1.0]
    independent = True
    for a in range(len(selected)):
        for c in range(a+1, len(selected)):
            counts['verification_pairs'] += 1
            if adjacency[selected[a]][selected[c]]:
                independent = False
    yes = independent and len(selected) >= graph.k
    # K>N maps to N+1; exact original K digits remain in the decoder result.
    witness = tuple(graph.ids[j] for j in selected[:graph.k]) if yes else ()
    counts['witness_ids'] = len(witness)
    counts['witness_utf8_bytes'] = sum(len(z.encode('utf-8')) for z in witness)
    return Run(True, 'YES' if yes else 'NO', witness, tuple(path), tuple(energies), counts)


def A(x: bytes) -> bool:
    """Total candidate Boolean output; invalid encodings are outside L_Gamma.

    This is not an admitted Independent-Set decider: false negatives exist.
    """
    return run_candidate(x).decision == 'YES'
