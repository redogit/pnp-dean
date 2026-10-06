"""Behavior/contract tests, not a universal-correctness admission."""
import ast
import importlib
import importlib.util
import inspect
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from candidate import run_candidate
from certificate import R

STAR = b'{"ids":["0","1","2"],"edges":[[0,1],[0,2]],"K":2}'


class ContinuationTests(unittest.TestCase):
    def module(self):
        self.assertIsNotNone(importlib.util.find_spec('continuation'),
                             'the specified x-only continuation is not implemented')
        return importlib.import_module('continuation')

    def test_repairs_preserved_star_without_receiving_a_witness(self):
        module = self.module()
        run = module.run_continuation(STAR)
        self.assertEqual(run.decision, 'YES')
        self.assertEqual(run.witness, ('1', '2'))
        self.assertEqual(run.path, ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 1.0)))
        self.assertEqual(run.energies, (0, -1, -2))
        self.assertEqual(run.moves, (('ADD', 0), ('EXCHANGE', 0, 1, 2)))
        self.assertTrue(module.A(STAR))

    def test_lexicographic_exchange_then_resumes_original_descent(self):
        module = self.module()
        x = b'{"ids":["0","1","2","3"],"edges":[[0,1],[0,2],[0,3]],"K":3}'
        run = module.run_continuation(x)
        self.assertEqual(run.moves, (('ADD', 0), ('EXCHANGE', 0, 1, 2), ('ADD', 3)))
        self.assertEqual(run.witness, ('1', '2', '3'))
        self.assertEqual(run.energies, (0, -1, -2, -3))

    def test_determinism_restoration_and_phase_counts(self):
        module = self.module()
        run = module.run_continuation(STAR)
        self.assertEqual(run, module.run_continuation(STAR))
        c = run.counts
        self.assertEqual(c['input_bits'], 392)
        self.assertEqual(c['one_bit_trials'], c['one_bit_rollbacks'])
        self.assertEqual(c['exchange_trial_writes'], 3*c['exchange_trials'])
        self.assertEqual(c['exchange_rollback_writes'], c['exchange_trial_writes'])
        self.assertEqual(c['accepted_exchanges'], 1)
        self.assertEqual(c['one_bit_rounds'], 3)
        self.assertEqual(c['energy_evaluations'], 1+c['one_bit_trials']+c['exchange_trials'])
        self.assertEqual(c['trace_coordinate_copies'], 3*len(run.path))

    def test_original_candidate_remains_refuted(self):
        self.module()
        original = run_candidate(STAR)
        self.assertEqual(original.decision, 'NO')
        self.assertEqual(original.path, ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0)))
        self.assertTrue(R(STAR, b'011'))

    def test_x_only_interface_and_no_referee_dependency(self):
        module = self.module()
        for function in (module.A, module.run_continuation):
            self.assertEqual(tuple(inspect.signature(function).parameters), ('x',))
        tree = ast.parse(Path(module.__file__).read_text())
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                imports.append(node.module)
            elif isinstance(node, ast.Import):
                imports.extend(alias.name for alias in node.names)
        self.assertEqual(set(imports), {'dataclasses', 'json_codec'})

    def test_empty_complete_and_huge_target_boundaries(self):
        module = self.module()
        cases = [
            (b'{"ids":[],"edges":[],"K":0}', 'YES'),
            (b'{"ids":[],"edges":[],"K":1}', 'NO'),
            (b'{"ids":["0","1"],"edges":[[0,1]],"K":2}', 'NO'),
            (b'{"ids":["0"],"edges":[],"K":'+b'9'*5000+b'}', 'NO'),
        ]
        for x, decision in cases:
            with self.subTest(x=x[:80]):
                self.assertEqual(module.run_continuation(x).decision, decision)

    def test_invalid_does_not_mean_a_proved_graph_no(self):
        module = self.module()
        for x in (b'\xff', b'{}', b'not json',
                  b'{"ids":[],"edges":[],"K":0,"witness":[]}'):
            with self.subTest(x=x):
                run = module.run_continuation(x)
                self.assertEqual(run.decision, 'INVALID')
                self.assertFalse(run.valid_input)
                self.assertFalse(module.A(x))

    def test_original_unicode_and_nul_ids_recovered(self):
        module = self.module()
        x = b'{"ids":["center","\\u0000","e\\u0301"],"edges":[[0,1],[0,2]],"K":2}'
        run = module.run_continuation(x)
        self.assertEqual(run.witness, ('\x00', 'e\u0301'))
        self.assertEqual(run.counts['witness_utf8_bytes'], 4)

    def test_resource_errors_propagate_instead_of_becoming_no(self):
        module = self.module()
        with patch.object(module, 'decode', side_effect=MemoryError('test allocation failure')):
            with self.assertRaises(MemoryError):
                module.A(STAR)

    def test_binary_wrapper_rejects_incomplete_octets(self):
        module = self.module()
        for w in ('', '1', '0000000', '000000000', '0000000x'):
            self.assertFalse(module.A_bits(w))
        bits = ''.join(format(byte, '08b') for byte in STAR)
        self.assertTrue(module.A_bits(bits))
        self.assertFalse(module.A_bits('11111111'))

    def test_referee_enumerates_every_n_k_mask_prefix(self):
        self.assertIsNotNone(importlib.util.find_spec('attack_continuation'),
                             'the frozen external referee is not implemented')
        attack = importlib.import_module('attack_continuation')
        cases = list(attack.instances(2))
        self.assertEqual(len(cases), 13)
        keys = [(N, K, mask) for N, K, mask, x in cases]
        self.assertEqual(keys, sorted(keys))
        for N in range(3):
            for K in range(N+2):
                self.assertEqual([m for n, k, m in keys if (n, k) == (N, K)],
                                 list(range(1 << (N*(N-1)//2))))
        for N, K, mask, x in cases:
            data = json.loads(x)
            self.assertEqual(len(data['ids']), N)
            self.assertEqual(data['K'], K)
            self.assertEqual(attack.oracle(x)[0], K <= (N if not data['edges'] else 1))


    def test_retains_the_first_new_counterexample_without_a_second_repair(self):
        module = self.module()
        x = b'{"ids":["0","1","2","3","4"],"edges":[[0,2],[0,4],[1,2],[1,3]],"K":3}'
        run = module.run_continuation(x)
        self.assertEqual(run.decision, 'NO')  # Known false NO, NOT NO_PROVED.
        self.assertEqual(run.path[-1], (1.0, 1.0, 0.0, 0.0, 0.0))
        self.assertEqual(run.energies, (0, -1, -2))
        self.assertEqual(run.counts['exchange_trials'], 6)
        self.assertEqual(run.counts['accepted_exchanges'], 0)
        self.assertTrue(R(x, b'00111'))  # Referee receives y; candidate did not.

    def test_saved_evidence_is_exactly_the_stopped_prefix(self):
        self.module()
        from hashlib import sha256
        path = Path(__file__).resolve().parents[2]/'evidence/REQ-0009-ONE-FOR-TWO/result.json'
        report = json.loads(path.read_text())
        self.assertEqual(report['verdict'], 'REJECT_COUNTEREXAMPLE')
        self.assertFalse(report['admitted'])
        self.assertEqual(report['tested_instances'], 3568)
        self.assertEqual(report['stop'], dict(N=5, K=3, graph_mask=58, graphs_in_partial_slice=59))
        self.assertEqual(sum(row['graphs'] for row in report['completed_slices'])+59, 3568)
        self.assertEqual(sha256(report['encoded_utf8'].encode()).hexdigest(), report['input_sha256'])
        self.assertEqual(report['claim_ceiling'], 'P ?= NP = OPEN')


if __name__ == '__main__':
    unittest.main()
