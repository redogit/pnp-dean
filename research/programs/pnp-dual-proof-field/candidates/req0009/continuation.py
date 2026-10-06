"""One specified 1-for-2 continuation; candidate NO is NOT NO_PROVED.

The only problem input is x. See CONTINUATION_1_FOR_2.md, fixed before code.
Exact integer energy, complete rollback, no supplied witness or referee import.
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
    moves: tuple[tuple, ...]
    counts: dict[str, int]


def run_continuation(x: bytes) -> Run:
    if type(x) is not bytes:
        raise TypeError('the encoded-input API requires bytes')
    graph = decode(x)
    if graph is None:
        return Run(False, 'INVALID', (), (), (), (),
                   {'input_bytes': len(x), 'input_bits': 8*len(x)})
    N, M = len(graph.ids), len(graph.edges)
    adjacency = [[False]*N for _ in range(N)]
    for u, v in graph.edges:
        adjacency[u][v] = adjacency[v][u] = True
    b = [0.0]*N
    counts = dict(input_bytes=len(x), input_bits=8*len(x),
                  adjacency_cells=N*N, edge_insertions=M,
                  energy_evaluations=0, coordinate_terms=0, edge_terms=0,
                  one_bit_rounds=0, one_bit_trials=0, one_bit_rollbacks=0,
                  one_bit_comparisons=0, accepted_additions=0,
                  exchange_scans=0, exchange_u_visits=0, exchange_v_visits=0,
                  exchange_w_visits=0, exchange_trials=0,
                  exchange_trial_writes=0, exchange_rollback_writes=0,
                  exchange_comparisons=0, accepted_exchanges=0,
                  commit_coordinate_writes=0, cardinality_terms=0,
                  trace_coordinate_copies=N, verification_pairs=0,
                  witness_ids=0, witness_utf8_bytes=0)

    def energy() -> int:
        counts['energy_evaluations'] += 1
        counts['coordinate_terms'] += N
        counts['edge_terms'] += M
        return (N+1)*sum(int(b[u])*int(b[v]) for u, v in graph.edges) - sum(int(z) for z in b)

    current = energy()
    path, energies, moves = [tuple(b)], [current], []
    while True:
        # The original least-(energy,index) one-bit rule, including stop rounds.
        counts['one_bit_rounds'] += 1
        best = None
        for j in range(N):
            b[j] = 1.0-b[j]
            counts['one_bit_trials'] += 1
            score = energy()
            b[j] = 1.0-b[j]
            counts['one_bit_rollbacks'] += 1
            counts['one_bit_comparisons'] += 1
            choice = (score, j)
            if score < current and (best is None or choice < best):
                best = choice
        if best is not None:
            score, j = best
            if b[j] != 0.0 or score != current-1:
                raise AssertionError('one-bit independent-addition invariant failed')
            b[j] = 1.0
            current = score
            counts['accepted_additions'] += 1
            counts['commit_coordinate_writes'] += 1
            moves.append(('ADD', j))
        else:
            counts['cardinality_terms'] += N
            if sum(int(z) for z in b) >= graph.k:
                break
            counts['exchange_scans'] += 1
            chosen = None
            # Explicit bounded local enumeration: no subset oracle or advice.
            for u in range(N):
                counts['exchange_u_visits'] += 1
                if b[u] != 1.0:
                    continue
                for v in range(N):
                    counts['exchange_v_visits'] += 1
                    if b[v] != 0.0:
                        continue
                    for w in range(v+1, N):
                        counts['exchange_w_visits'] += 1
                        if b[w] != 0.0:
                            continue
                        b[u], b[v], b[w] = 0.0, 1.0, 1.0
                        counts['exchange_trials'] += 1
                        counts['exchange_trial_writes'] += 3
                        score = energy()
                        b[u], b[v], b[w] = 1.0, 0.0, 0.0
                        counts['exchange_rollback_writes'] += 3
                        counts['exchange_comparisons'] += 1
                        if score < current:
                            chosen = (score, u, v, w)
                            break
                    if chosen is not None:
                        break
                if chosen is not None:
                    break
            if chosen is None:
                break  # experimental NO; completeness is the attacked bridge
            score, u, v, w = chosen
            if score != current-1:
                raise AssertionError('exchange progress invariant failed')
            b[u], b[v], b[w] = 0.0, 1.0, 1.0
            current = score
            counts['accepted_exchanges'] += 1
            counts['commit_coordinate_writes'] += 3
            moves.append(('EXCHANGE', u, v, w))
        if len(moves) > N:
            raise AssertionError('uniform route-length invariant failed')
        path.append(tuple(b))
        energies.append(current)
        counts['trace_coordinate_copies'] += N

    counts['cardinality_terms'] += N
    selected = [j for j in range(N) if b[j] == 1.0]
    independent = True
    for a in range(len(selected)):
        for c in range(a+1, len(selected)):
            counts['verification_pairs'] += 1
            if adjacency[selected[a]][selected[c]]:
                independent = False
    if not independent:
        raise AssertionError('final independent-set verification failed')
    yes = len(selected) >= graph.k
    witness = tuple(graph.ids[j] for j in selected[:graph.k]) if yes else ()
    counts['witness_ids'] = len(witness)
    counts['witness_utf8_bytes'] = sum(len(label.encode('utf-8')) for label in witness)
    return Run(True, 'YES' if yes else 'NO', witness, tuple(path),
               tuple(energies), tuple(moves), counts)


def A(x: bytes) -> bool:
    """Experimental Boolean output; NOT an admitted Independent-Set decider."""
    return run_continuation(x).decision == 'YES'


def A_bits(w: str) -> bool:
    """MSB-first binary wrapper; incomplete octets are outside the language."""
    if type(w) is not str or any(bit not in '01' for bit in w) or len(w) % 8:
        return False
    return A(bytes(int(w[j:j+8], 2) for j in range(0, len(w), 8)))
