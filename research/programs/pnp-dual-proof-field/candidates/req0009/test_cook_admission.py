"""Check witness semantics and refusal to admit the refuted candidate."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

from certificate import R
from cook_admission import audit_candidate


STAR = b'{"ids":["0","1","2"],"edges":[[0,1],[0,2]],"K":2}'


class CertificateTests(unittest.TestCase):
    def test_accepts_the_two_leaves_despite_candidate_false_no(self):
        # Omitting the cardinality or conflict check breaks the tests below;
        # rejecting every certificate breaks this independently known YES.
        self.assertTrue(R(STAR, b'011'))

    def test_rejects_conflicts_and_insufficient_cardinality(self):
        self.assertFalse(R(STAR, b'110'))
        self.assertFalse(R(STAR, b'100'))
        self.assertFalse(R(STAR, b'000'))

    def test_rejects_malformed_instance_or_certificate(self):
        for x, y in [(b'not json', b''), (STAR, b'01'),
                     (STAR, b'0110'), (STAR, b'02x'),
                     (STAR, '011'), (STAR, bytes([0, 1, 1]))]:
            with self.subTest(x=x, y=y):
                self.assertFalse(R(x, y))

    def test_empty_and_impossible_targets(self):
        self.assertTrue(R(b'{"ids":[],"edges":[],"K":0}', b''))
        self.assertFalse(R(b'{"ids":[],"edges":[],"K":1}', b''))
        huge = b'{"ids":["a"],"edges":[],"K":' + b'9'*5000 + b'}'
        self.assertFalse(R(huge, b'1'))

    def test_certificate_indices_preserve_isolates_and_unicode_ids(self):
        x = b'{"ids":["\\u0000","\\u00e9","isolated"],"edges":[[0,1]],"K":2}'
        self.assertTrue(R(x, b'101'))
        self.assertTrue(R(x, b'011'))
        self.assertFalse(R(x, b'110'))


class CookAdmissionTests(unittest.TestCase):
    def test_false_no_blocks_admission_with_checked_yes_witness(self):
        report = audit_candidate()
        self.assertIsInstance(report, dict)
        self.assertFalse(report['admitted'])
        self.assertEqual(report['verdict'], 'REJECT_COUNTEREXAMPLE')
        self.assertEqual(report['claim_ceiling'], 'P ?= NP = OPEN')
        evidence = report['counterexample']
        self.assertFalse(evidence['candidate_accepts'])
        self.assertTrue(evidence['checking_relation_accepts'])
        self.assertEqual(evidence['input_sha256'],
                         '85c3f4a421656df67987092971fd87d30554049d671df289feef5e94ab03941d')
        self.assertEqual(evidence['certificate_ascii'], '011')

    def test_admission_command_exits_nonzero_and_reports_why(self):
        process = subprocess.run(
            [sys.executable, str(Path(__file__).with_name('cook_admission.py'))],
            capture_output=True, text=True, timeout=10, check=False)
        self.assertEqual(process.returncode, 1)
        self.assertEqual(process.stderr, '')
        report = json.loads(process.stdout)
        self.assertFalse(report['admitted'])
        self.assertEqual(report['verdict'], 'REJECT_COUNTEREXAMPLE')


if __name__ == '__main__':
    unittest.main()
