"""Behavior checks for the frozen candidate, not a universal-correctness test."""
import unittest

from candidate import A, run_candidate


class CandidateTests(unittest.TestCase):
    def checked(self, raw):
        result = run_candidate(raw)
        self.assertIsNotNone(result, 'candidate must execute from encoded x')
        return result

    def test_constructs_witness_from_input_only(self):
        raw = b'{"ids":["a","b","c"],"edges":[],"K":2}'
        result = self.checked(raw)
        self.assertEqual(result.decision, 'YES')
        self.assertEqual(result.witness, ('a','b'))
        self.assertEqual(result.path, ((0.0,0.0,0.0),(1.0,0.0,0.0),(1.0,1.0,0.0),(1.0,1.0,1.0)))
        self.assertEqual(result.energies, (0,-1,-2,-3))
        self.assertTrue(A(raw))

    def test_edge_no_and_empty_boundaries(self):
        for raw, answer in [
            (b'{"ids":["a","b"],"edges":[[0,1]],"K":2}', 'NO'),
            (b'{"ids":[],"edges":[],"K":0}', 'YES'),
            (b'{"ids":[],"edges":[],"K":1}', 'NO'),
            (b'{"ids":["a"],"edges":[],"K":9999999999999999999999}', 'NO'),
        ]:
            with self.subTest(raw=raw):
                self.assertEqual(self.checked(raw).decision, answer)

    def test_invalid_is_separate_from_graph_no(self):
        result = self.checked(b'not json')
        self.assertEqual(result.decision, 'INVALID')
        self.assertFalse(result.valid_input)
        self.assertEqual(result.witness, ())
        self.assertFalse(A(b'not json'))

    def test_fixed_route_does_not_silently_repair_counterexample(self):
        raw = b'{"ids":["center","left","right"],"edges":[[0,1],[0,2]],"K":2}'
        result = self.checked(raw)
        self.assertEqual(result.path, ((0.0,0.0,0.0),(1.0,0.0,0.0)))
        self.assertEqual(result.energies, (0,-1))
        self.assertEqual(result.decision, 'NO')  # false negative; retained candidate
        self.assertFalse(A(raw))
        self.assertEqual(result.witness, ())


if __name__ == '__main__':
    unittest.main()
