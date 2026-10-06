# Charter — Dual Adversarial Proof Field

## Goal

Force progress on P versus NP by making both theorem directions generate exactly the parts demanded by the current obligation while sharing one immutable definitional substrate.

### Constructive direction

Produce one deterministic algorithm `A` for an NP-complete decision language and fixed constants `c,k` such that for every encoded input `x`:

[
A(x)=L(x)
]

and

[
T_A(|x|) \le c|x|^k+c.
]

### Lower-bound direction

Establish a theorem applying to every deterministic algorithm deciding the chosen NP-complete language such that no fixed polynomial bounds its worst-case work.

Defeating finitely many algorithms is not enough.

## Current common test domain

Dean / Independent Set:

Given finite conflict graph `G=(V,E)` and target `K`, decide whether an independent set of size at least `K` exists.

Original student identities and witnesses must remain reconstructible whenever a route claims witness preservation.

## Shared base

Both theorem directions use exactly the same:

- encoding;
- input length;
- deterministic cost model;
- language semantics;
- reduction rules;
- proof/admission rules.

Generators may attack algorithms and representations. They may not redefine the game.

The shared input encoding is now explicitly bound by
[JSON-IS-1](JSON_INPUT_ENCODING.md), selected by the user on 2026-10-05:
one UTF-8 JSON record containing ordered original IDs, incompatible index
pairs, and K. Its bit length is `n=8*len(x)`. The deterministic charged model
is multi-tape Turing-machine bit work, including decoding, construction,
arithmetic, selection, storage, verification, rollback, and reconstruction.
The binary language includes only whole-octet valid YES records. Every
other bit string is rejected, and its parsing/rejection time counts in the
same worst-case bound. [JSON_IS_COMPLETENESS.md](JSON_IS_COMPLETENESS.md)
specifies the checking relation and encoded-language reduction.
This fills the earlier missing binding; it does not attribute that codec to
historical sources or alter Independent-Set semantics.

## Design hypothesis

An obligation-driven generator field can expose stronger invariants than one linear proof search when:

1. each generator accepts only a consequential obligation slice;
2. each output names the requested parts needed to advance or attack that slice;
3. generators may recursively request zero-to-many child obligations;
4. constructive requests earn authority only from exact polynomial progress;
5. lower-bound requests earn authority only from genuine counterexamples or generalized obstructions;
6. verification/admission remains independent of generation;
7. memory is retrieved obligation-locally, preventing both knowledge decay and context flooding;
8. every unknown lifecycle cost becomes an explicit obligation;
9. repeated local results are distilled into reusable lemmas/counterfamilies rather than battle counts.

## Success

### P=NP success

One admitted universal construction discharging all required obligations.

### P!=NP success

One admitted universal lower-bound theorem. A cemetery of failed constructions is not sufficient.

## Valuable fallback

Even without resolving P versus NP:

- enlarge exact polynomial terminal classes;
- prove new counterfamilies against proposed carriers;
- isolate representation-independent barriers;
- improve exact carrier/reconstruction theory;
- produce reusable, auditable negative results.

## Non-goals

- changing standard complexity definitions;
- treating neural confidence as proof;
- accepting an oracle hidden inside reconciliation;
- promoting bounded experiments to universal results;
- optimizing only wall-clock time while ignoring deterministic work;
- erasing failed approaches.
