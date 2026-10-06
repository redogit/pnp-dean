"""Current candidate admission audit; bounded checks cannot prove universality.

This referee replays one existing refutation, not a new counterexample search.
The certificate is supplied to R only; A receives x alone. There is no admit
path: even disappearance of this mismatch leaves the universal claim unresolved.
"""
from hashlib import sha256
import json

from candidate import A
from certificate import R


def audit_candidate() -> dict:
    x = b'{"ids":["0","1","2"],"edges":[[0,1],[0,2]],"K":2}'
    y = b'011'
    digest = sha256(x).hexdigest()
    if digest != '85c3f4a421656df67987092971fd87d30554049d671df289feef5e94ab03941d':
        raise ValueError('preserved counterexample input changed')
    witness_accepts = R(x, y)
    if not witness_accepts:
        raise ValueError('preserved YES witness failed independent checking')
    candidate_accepts = A(x)
    refuted = witness_accepts and not candidate_accepts
    return {
        'candidate': 'A_0009_ONE_BIT_DESCENT',
        'admitted': False,
        'verdict': 'REJECT_COUNTEREXAMPLE' if refuted else 'UNRESOLVED',
        'claim_ceiling': 'P ?= NP = OPEN',
        'requirements': [
            {'id': 'X_ONLY_DETERMINISTIC', 'status': 'SPECIFIED',
             'evidence': 'candidate.py and CANDIDATE.md; no supplied y or oracle'},
            {'id': 'EXACT_LANGUAGE', 'status': 'REFUTED' if refuted else 'UNRESOLVED',
             'evidence': 'checked valid YES input rejected by A' if refuted
                         else 'one replay cannot establish universal correctness'},
            {'id': 'UNIFORM_POLYNOMIAL_TOTAL_TIME', 'status': 'NOT_ADMITTED',
             'evidence': 'at most N additions; scoped polynomial argument; '
                         'all-input machine lowering not admitted after correctness failure'},
            {'id': 'CHARGED_LIFECYCLE', 'status': 'SPECIFIED',
             'evidence': 'complete recurrence in CANDIDATE.md; counters are not TM steps'},
        ],
        'counterexample': {
            'encoded_utf8': x.decode('utf-8'),
            'input_sha256': digest,
            'n_bits': 8*len(x),
            'certificate_ascii': y.decode('ascii'),
            'candidate_accepts': candidate_accepts,
            'checking_relation_accepts': witness_accepts,
        },
        'remaining_obligation': 'a proved exact NO/continuation rule; no route repair attempted',
        'scope': 'existing counterexample replay only; no universal admission by finite tests',
    }


if __name__ == '__main__':
    print(json.dumps(audit_candidate(), indent=2))
    raise SystemExit(1)
