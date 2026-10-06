"""Bounded external referee: stop at the first disagreement, never repair A.

The combinations oracle is exponential research-only machinery on N<=3.
Neither this oracle nor a supplied witness is imported by candidate.py.
"""
import argparse
import hashlib
import itertools
import json
from dataclasses import asdict
from pathlib import Path

from candidate import run_candidate


def exact_witness(N, edges, K):
    for selected in itertools.combinations(range(N), K):
        if all(not (u in selected and v in selected) for u,v in edges):
            return selected
    return None


def attack():
    checked, graphs, smaller = 0, 0, []
    for N in range(4):
        pairs = list(itertools.combinations(range(N), 2))
        level_instances, level_graphs = 0, 0
        for mask in range(1 << len(pairs)):
            edges = [pair for i,pair in enumerate(pairs) if mask & (1 << i)]
            level_graphs += 1
            graphs += 1
            for K in range(N+2):
                obj = {'ids': [str(j) for j in range(N)], 'edges': edges, 'K': K}
                raw = json.dumps(obj, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
                candidate = run_candidate(raw)
                assert candidate.valid_input
                witness = exact_witness(N, edges, K)
                exact_yes = witness is not None
                candidate_yes = candidate.decision == 'YES'
                checked += 1
                level_instances += 1
                if candidate_yes != exact_yes:
                    return {
                        'status': 'COUNTEREXAMPLE_FOUND',
                        'candidate': 'A_0009_ONE_BIT_DESCENT',
                        'claim_ceiling': 'P ?= NP = OPEN',
                        'first_failed_bridge': 'a one-bit local minimum below K proves no independent K-set exists',
                        'instance': obj, 'encoded_utf8': raw.decode('utf-8'),
                        'input_sha256': hashlib.sha256(raw).hexdigest(),
                        'n_bits': 8*len(raw), 'candidate_run': asdict(candidate),
                        'exact_decision': 'YES' if exact_yes else 'NO',
                        'exact_witness_indices': witness,
                        'exact_witness_ids': [obj['ids'][j] for j in witness] if witness is not None else None,
                        'graphs_visited': graphs, 'instances_checked': checked,
                        'all_smaller_N': smaller,
                        'enumeration': 'N ascending 0..3; edge mask ascending; K ascending 0..N+1; stop at first mismatch',
                        'research_oracle': 'independent combinations enumeration, N<=3; charged research work, never inside A',
                        'non_claims': ['No P=NP or P!=NP conclusion', 'No later bridge attacked', 'No candidate repair performed']
                    }
        smaller.append({'N': N, 'graphs': level_graphs, 'instances': level_instances})
    raise AssertionError('Frozen candidate did not produce the predicted first bridge failure')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    result = attack()
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'instances_checked': result['instances_checked'],
                      'vertices': len(result['instance']['ids']), 'K': result['instance']['K']}))


if __name__ == '__main__':
    main()
