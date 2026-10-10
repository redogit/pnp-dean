# Current cross-state / Anti-Ouroboros note

Date: 2026-10-10

Status: `SESSION_DERIVATION_UNPROMOTED`

Claim ceiling: `P ?= NP = OPEN`.

This note records already-completed bounded conversation derivations so they can be compared with the source-backed registry. It does not promote them above the repository sources and performs no new proof step.

## External source anchor

User-supplied note: `Minimum_Dorm_Repair_2026-10-07.md`

SHA-256: `dc412e3f3f2fec754099fbc69baa4f41bd42a2bc9116c1554213eb84ca2f9d1d`

Its declared boundary is preserved: the dorm model is a separate packing model; it does not replace the independent-set successor analysis or prove a general P-vs-NP result.

The useful exact pattern is the two-dorm dynamic program: partial arrangements may be merged only after proving that their future possibilities are identical. For two dorms the retained state is the processed-component index plus occupancy in one dorm.

## A. Cross-state frontier candidate — refuted

On the preserved REQ-0009 five-vertex path, test

[
\sigma_{front}(S)=(|S|,A(S)),
]

where (A(S)) is the exact set of currently addable vertices.

The states (S_1=\{0,1\}) and (S_2=\{0,3\}) both have size two and empty addable frontier, yet under the frozen one-for-two continuation (S_1) has no successful exchange while (S_2\to\{2,3,4\}) succeeds.

Result:

[
\sigma_{front}\text{ is not continuation-sufficient.}
]

Interpretation: the legal frontier loses which selected vertex is responsible for each blockage.

## B. Exact blocker-incidence candidate — sufficient but not a useful quotient

Define

[
B_S(v)=N(v)\cap S
]

for every unselected vertex and retain the exact unselected-domain identities.

This distinguishes the previous collision. More generally the domain is (V\setminus S), so the carrier identifies (S) itself.

Result:

- future-sufficient under the frozen deterministic continuation;
- polynomial-size;
- injective over the selected state;
- therefore not a nontrivial state quotient.

This is identity preservation, not useful compression.

## C. Residual future-behavior equivalence

For a residual state (S), let (\Phi_S(F)) be the exact decision outcome under an allowed future continuation/attachment (F).

Define

[
S\equiv T
\iff
\forall F,\;\Phi_S(F)=\Phi_T(F).
]

This is the semantic fixed point for cross-state exclusions and obligations: any exact future-sufficient carrier must refine this equivalence, while the equivalence class itself is the coarsest exact semantic quotient.

Important boundary: semantic existence does not establish efficient discovery, representation, update, or value evaluation.

## D. Depth versus width/index

The odd path family shows that local augmentation depth can grow without a fixed constant bound. This does not imply that the information *type* must grow with depth: paths/trees can reuse a small boundary state recursively.

A separate width-(w) fixed-boundary construction yields at least

[
\binom{w}{\lfloor w/2\rfloor}
]

future-distinguishable boundary states.

This is an equivalence-class count, not a storage or runtime lower bound. One current class can still have an (O(w))-bit identifier.

## E. Anti-Ouroboros split

A polynomial-size symbolic carrier exists trivially:

[
C(x)=x.
]

Therefore finite/poly-size representation and composition closure are not enough.

Keep four obligations distinct:

1. **Representation** — write the residual/carrier.
2. **Quotient** — merge genuinely distinct states without losing protected future behavior.
3. **Value evaluation** — compute the exact decision value of the quotient.
4. **Total work** — discover/update/evaluate/reconstruct under one fixed polynomial bound in the encoded input.

If carrier evaluation reconstructs an equally hard residual solve, the problem has only been renamed.

This aligns with two prior source-backed barriers:

- `PNP_DEAN_COMPONENT_EXPRESSION_2026-09-30.md`: polynomial compact-factor construction can still leave optimization equivalent to the original Independent-Set obligation.
- `PNP_POSITIVE_CIRCUIT_SIGNATURE_COMPLETENESS_2026-09-26.md`: exact signature equality does not supply polynomial signature-value evaluation.

## F. Next open criterion — not executed here

Candidate local-value law:

[
V(C_1\otimes C_2)=F(V(C_1),V(C_2),I_{12}),
]

where (I_{12}) is an exact polynomial-size cross-state exclusion/obligation interface.

For this to be Anti-Ouroboros, (F) must not evaluate an equally hard reconstructed residual.

The articulation terminal is a scoped positive example of local value composition through a one-vertex interface. No universal composition theorem is claimed.

No further proof step is performed in this note.
