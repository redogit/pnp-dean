# REQ-0009 — Cook admission audit

Audit base: `52c725cb002fecdd3974e341291e4fff5aaf3206`, 2026-10-05.
Primary verdict: **refuted, with the preserved vertex-minimal counterexample**.
Claim ceiling: `P ?= NP = OPEN`.

The claim under review is that the fixed candidate
`A_0009_ONE_BIT_DESCENT` decides the fixed binary JSON-IS-1 language on all
inputs with one uniform polynomial bound. Both acceptance and rejection must
agree with the language; malformed strings are outside it. The diagnostic
INVALID state is distinct from a NO assertion about a valid graph.

## Four promotion requirements

Cook's operative definitions are in the [Clay description](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf),
pp. 1–2; its machine appendix is pp. 9–10. The four rows below instantiate
the repository's [promotion counterprobe](../COOK_CLAY_FORMALIZATION.md).

| Requirement | Exact current evidence | Status |
| --- | --- | --- |
| One finite deterministic A using x alone | Decoder, graph/matrix, exact binary coordinates, scored one-bit selection and terminal rule are in `candidate.py`; no supplied y or research oracle enters A. | Specified; no machine/advice changes with input size. |
| Exact language agreement for every input | On the valid 392-bit star input, A rejects while supplied certificate `011` passes R. | **Refuted. This alone blocks admission.** |
| Halting within one fixed polynomial in input bit length | Valid-state route accepts at most N additions. Decoder, matrix, trial scans and trace have a scoped polynomial argument. | Algorithm-level support; all-input machine lowering remains unadmitted after the correctness failure. |
| Every lifecycle cost included | The existing complete recurrence charges decoding, construction, discovery, selection, transforms, checking, rollback, storage, recovery and release. | Specified; phase counts are not machine-step measurements. |

No row labelled specified or supported is a universal admission. Cook does
not require benchmark-derived numeric constants or a printed transition table:
a rigorous uniform polynomial proof with justified model simulation suffices.
The repository's request for explicit candidate constants is an additional
evidence obligation. Even a complete time proof would leave this A refuted.

The all-input requirement includes malformed UTF-8/JSON and binary strings
whose length is not a multiple of eight. A binary lowering rejects incomplete
octets before invoking the byte API, and charges that scan. Unexpected runtime
or resource failures are not language decisions. Resource-bounded executions
are not a replacement for the ideal machine's quantified total-time proof.

The formal binary wrapper is `A_bits(w)=False` for incomplete octets and
`A(unpack(w))` otherwise, using the fixed most-significant-bit-first byte
packing in the language proof. This wrapper preserves the displayed false
negative; it adds no alternative graph solver.

## Separate certificate and language support

The independent supplied-witness relation is implemented in
[`certificate.py`](../candidates/req0009/certificate.py). It checks one ASCII
0/1 byte per ordered vertex, sufficient cardinality and no selected edge.
Its binary certificate length is `8N <= 8B = n`, with fixed exponent 1.
The [membership and reduction proof](../JSON_IS_COMPLETENESS.md) gives both
directions of the certificate equivalence and an explicit 3SAT-to-JSON map.
This support establishes the target and the checker role, not construction
of a witness from x by the failed route.

The dependency structure is:

- JSON-IS-1 and the checking relation give the target language and supplied
  certificate semantics.
- The internal occurrence-graph reduction and Cook's external 3SAT theorem
  support encoded-language NP-completeness.
- The candidate's route invariant gives termination and sound YES witnesses.
- Exact NO needs local optimality to imply absence of a K-set. That implication
  is refuted by the retained star. The constructive chain stops here.

## Executable refusal to admit

From the repository root:

```bash
python research/programs/pnp-dual-proof-field/candidates/req0009/cook_admission.py
```

The command independently checks the supplied leaf certificate, checks the
preserved input hash, runs the unchanged A on x alone, prints a JSON report
and exits **1** with `REJECT_COUNTEREXAMPLE`. It performs no new graph search.
It has no successful admission path: disappearance of this one mismatch would
yield `UNRESOLVED`, because finite successes cannot prove language equality.
Unexpected exceptions propagate rather than becoming graph NOs.

Unit-test success means the checker and refusal behave as specified. It does
not mean the candidate meets Cook's constructive requirements. The existing
validation entry discovers the seven new tests alongside the original ten.

Fresh verification on Python 3.12.14:

- The seven new tests first failed against unimplemented checker/admission
  behavior. All 17 candidate, codec and admission tests now pass.
- `python validate.py` passes source identity, the 17 tests, the existing 19
  MLIR Python tests, and decision-field discriminators. Its native check is
  blocked by missing `cmake`, so full validation exits 1. Native code was
  not changed, and native tests were not run.
- Direct `cook_admission.py` execution prints the checked refutation and
  exits 1 as intended. The original computation manifest validates with
  input freshness and output hashes intact.
- `git diff --check` passes. The preserved evidence has not been regenerated
  or substituted with a new search.

The original five manifest-pinned inputs and the original evidence files are
unchanged. This audit adds no route repair, no second candidate, no later
bridge attack, and no P=NP or P!=NP conclusion. The exact remaining need is a
proved continuation/NO rule when local descent stops short of K.
