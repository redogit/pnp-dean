"""Tests detect input loss, invalid-graph acceptance, and integer truncation."""
import unittest

from json_codec import decode


class CodecTests(unittest.TestCase):
    def checked(self, raw):
        value = decode(raw)
        self.assertIsNotNone(value, 'valid graph encoding must be decoded')
        return value

    def test_exact_ids_isolates_and_numeric_edge_order(self):
        value = self.checked(b'{"ids":["center","left","right","isolate"],"edges":[[0,1],[0,2]],"K":2}')
        self.assertEqual(value.ids, ('center', 'left', 'right', 'isolate'))
        self.assertEqual(value.edges, ((0, 1), (0, 2)))
        self.assertEqual(value.k, 2)
        self.assertEqual(value.k_digits, '2')

    def test_empty_graph_and_zero_target(self):
        self.assertEqual(self.checked(b'{"ids":[],"edges":[],"K":0}').k, 0)

    def test_large_target_and_key_order(self):
        digits = b'9' * 5000
        raw = b'{"K":' + digits + b',"edges":[],"ids":["a"]}'
        value = self.checked(raw)
        self.assertEqual(value.k_digits, '9' * 5000)
        self.assertEqual(value.k, 2)  # capped derived field; exact digits retained
        self.assertEqual(value.n_bits, 8 * len(raw))

    def test_unicode_and_null_identity_preserved(self):
        value = self.checked(b'{"ids":["\\u0000","e\\u0301","\\u00e9","\\ud83d\\ude00"],"edges":[],"K":1}')
        self.assertEqual(value.ids, ('\x00', 'e\u0301', '\u00e9', '\U0001f600'))

    def test_numeric_pair_order(self):
        ids = b'"0","1","2","3","4","5","6","7","8","9","10"'
        self.assertEqual(self.checked(b'{"ids":['+ids+b'],"edges":[[2,3],[2,10]],"K":2}').edges, ((2,3),(2,10)))
        self.assertIsNone(decode(b'{"ids":['+ids+b'],"edges":[[2,10],[2,3]],"K":2}'))

    def test_reject_invalid_and_ambiguous_inputs(self):
        invalid = [
            b'\xff', b'[]', b'{}', b'{"ids":[],"edges":[],"K":0} {}',
            b'{"ids":[],"ids":[],"edges":[],"K":0}',
            b'{"ids":[],"\\u0069ds":[],"edges":[],"K":0}',
            b'{"ids":["a","\\u0061"],"edges":[],"K":0}',
            b'{"ids":["\\ud800"],"edges":[],"K":0}',
            b'{"ids":["a"],"edges":[[0,0]],"K":1}',
            b'{"ids":["a","b"],"edges":[[1,0]],"K":1}',
            b'{"ids":["a","b"],"edges":[[0,1],[0,1]],"K":1}',
            b'{"ids":["a"],"edges":[[0,1]],"K":1}',
            b'{"ids":["a"],"edges":[],"K":true}',
            b'{"ids":["a"],"edges":[],"K":1.0}',
            b'{"ids":["a"],"edges":[],"K":1e0}',
            b'{"ids":["a"],"edges":[],"K":-0}',
            b'{"ids":["a"],"edges":[],"K":NaN}',
            b'{"ids":["a"],"edges":[],"K":1,"advice":[]}',
            b'{"ids":[0],"edges":[],"K":0}',
            b'{"ids":[[[[]]]],"edges":[],"K":0}',
        ]
        for raw in invalid:
            with self.subTest(raw=raw):
                self.assertIsNone(decode(raw))


if __name__ == '__main__':
    unittest.main()
