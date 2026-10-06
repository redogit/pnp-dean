"""External finite referee. Never imported by the x-only continuation.

Order and ceiling were frozen in CONTINUATION_1_FOR_2.md before implementation.
The combinations oracle is explicitly exponential research work, NOT solver work.
"""
from dataclasses import asdict
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys

from certificate import R
from continuation import run_continuation

MAX_N = 6
STAR = b'{"ids":["0","1","2"],"edges":[[0,1],[0,2]],"K":2}'


def instances(max_n: int):
    for N in range(max_n+1):
        possible = list(combinations(range(N), 2))
        for K in range(N+2):
            for mask in range(1 << len(possible)):
                edges = [edge for i, edge in enumerate(possible) if mask & (1 << i)]
                x = json.dumps(dict(ids=list(map(str, range(N))), edges=edges, K=K),
                               separators=(',', ':')).encode('utf-8')
                yield N, K, mask, x


def oracle(x: bytes):
    # Independent parsing for this canonical finite family; no candidate state.
    data = json.loads(x)
    N, K = len(data['ids']), data['K']
    counts = dict(combinations=0, edge_checks=0)
    if K > N:
        return False, (), counts
    for choice in combinations(range(N), K):
        counts['combinations'] += 1
        selected = set(choice)
        independent = True
        for u, v in data['edges']:
            counts['edge_checks'] += 1
            if u in selected and v in selected:
                independent = False
        if independent:
            return True, choice, counts
    return False, (), counts


def check_trace(x: bytes, run) -> None:
    data = json.loads(x)
    N = len(data['ids'])
    if not run.valid_input or len(run.path) > N+1 or len(run.moves)+1 != len(run.path):
        raise AssertionError('invalid run or route-length mismatch')
    for i, (state, energy) in enumerate(zip(run.path, run.energies)):
        if len(state) != N or any(z not in (0.0, 1.0) for z in state):
            raise AssertionError('invalid coordinate')
        if sum(state) != i or energy != -i:
            raise AssertionError('cardinality/energy progress mismatch')
        if any(state[u] and state[v] for u, v in data['edges']):
            raise AssertionError('conflicted committed state')
    if len(run.path) != len(run.energies):
        raise AssertionError('energy trace length mismatch')
    c = run.counts
    if (c['one_bit_trials'] != c['one_bit_rollbacks'] or
            c['exchange_trial_writes'] != c['exchange_rollback_writes'] or
            c['exchange_trial_writes'] != 3*c['exchange_trials'] or
            c['one_bit_rounds'] > N+1 or c['exchange_scans'] > N+1 or
            c['exchange_trials'] > (N+1)*N*(N*(N-1)//2)):
        raise AssertionError('lifecycle counter invariant failed')
    if run.decision == 'YES':
        indices = [data['ids'].index(label) for label in run.witness]
        y = bytes(49 if j in indices else 48 for j in range(N))
        if len(indices) != data['K'] or not R(x, y):
            raise AssertionError('internally recovered witness rejected')


def attack() -> dict:
    repaired = run_continuation(STAR)
    check_trace(STAR, repaired)
    if repaired.decision != 'YES' or repaired.witness != ('1', '2'):
        raise AssertionError('preserved three-vertex repair failed')
    checked = 0
    oracle_totals = dict(combinations=0, edge_checks=0)
    candidate_totals = {}
    completed = []
    current_slice = None
    slice_count = 0
    for N, K, mask, x in instances(MAX_N):
        key = (N, K)
        if key != current_slice:
            if current_slice is not None:
                completed.append(dict(N=current_slice[0], K=current_slice[1], graphs=slice_count))
            current_slice, slice_count = key, 0
        run = run_continuation(x)
        check_trace(x, run)
        truth, indices, costs = oracle(x)
        for name, value in costs.items():
            oracle_totals[name] += value
        for name, value in run.counts.items():
            candidate_totals[name] = candidate_totals.get(name, 0)+value
        checked += 1
        slice_count += 1
        if (run.decision == 'YES') != truth:
            y = bytes(49 if j in indices else 48 for j in range(N))
            if truth and not R(x, y):
                raise AssertionError('oracle witness rejected by retained checker')
            return dict(
                candidate='A_0009_ONE_FOR_TWO', verdict='REJECT_COUNTEREXAMPLE',
                admitted=False, claim_ceiling='P ?= NP = OPEN',
                frozen_spec_commit='e3312b89fb5532dedefbc0c731696749aa07b6c3',
                enumeration='N, then K, then increasing lex-edge bitmask',
                maximum_N=MAX_N, tested_instances=checked,
                completed_slices=completed,
                stop=dict(N=N, K=K, graph_mask=mask, graphs_in_partial_slice=slice_count),
                encoded_utf8=x.decode(), input_sha256=sha256(x).hexdigest(), n_bits=8*len(x),
                candidate_run=asdict(run), oracle_yes=truth,
                oracle_indices=indices, certificate_ascii=y.decode(),
                checking_relation_accepts=R(x, y), oracle_totals=oracle_totals,
                candidate_totals=candidate_totals,
                preserved_repair=dict(input_sha256=sha256(STAR).hexdigest(),
                                      run=asdict(repaired), excluded_from_prefix_count=True),
                failed_bridge='one-bit and 1-for-2 saturation below K => no independent K-set',
                scope='first disagreement only; no graph or larger K/N tested after this stop')
    if current_slice is not None:
        completed.append(dict(N=current_slice[0], K=current_slice[1], graphs=slice_count))
    return dict(candidate='A_0009_ONE_FOR_TWO', verdict='BOUNDED_ONLY', admitted=False,
                claim_ceiling='P ?= NP = OPEN', tested_instances=checked,
                completed_slices=completed, maximum_N=MAX_N)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: python attack_continuation.py OUTPUT.json')
    result = attack()
    text = json.dumps(result, indent=2, sort_keys=True)+'\n'
    Path(sys.argv[1]).write_text(text, encoding='utf-8')
    print(text, end='')
