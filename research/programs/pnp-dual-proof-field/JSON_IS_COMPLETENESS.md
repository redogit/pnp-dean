# JSON-IS-1: checking relation and NP-completeness

This supplies the language-level obligations for the codec selected by the
user. It supplies no Independent-Set constructor and does not repair or admit
`A_0009_ONE_BIT_DESCENT`. The preserved false NO remains decisive. The claim
ceiling is `P ?= NP = OPEN`.

## Fixed binary language

Let `pack` encode each byte as eight bits, most significant bit first. Define
`L_JSON_IS` over the finite alphabet `{0,1}` as follows. A bit string `w` is in
the language exactly when it is `pack(x)` for a valid
[JSON-IS-1](JSON_INPUT_ENCODING.md) byte record `x`, and the decoded graph has
an independent set of size at least its exact natural-number target K.
Strings whose lengths are not divisible by eight, malformed UTF-8/JSON, and
records violating the codec are outside the language. This is a language of
all finite binary strings, rather than a promise problem restricted to valid
graphs. Put `B=len(x)` and `n=|w|=8B` when octet decoding succeeds.

The byte API uses a fixed 256-symbol alphabet. Its size B and the binary size
n differ by a fixed factor of eight. Unicode IDs are data encoded in these
bytes; they do not enlarge the machine's input alphabet. Runtime or resource
errors in a host implementation are not evidence that a valid graph is NO.

## One explicit checking relation

The supplied-witness reference API is `R(x: bytes, y: bytes)` in
`candidates/req0009/certificate.py`. It does not call the candidate or search
for y. Define its mathematical relation on every pair of finite bit strings:

1. Reject unless both strings consist of complete octets. Decode them to x
   and y. Reject unless x is a valid JSON-IS-1 record.
2. Set `N=len(ids)`. Reject unless y has exactly N bytes, each byte being
   ASCII `0` or ASCII `1`. The byte at position j selects vertex j exactly
   when it is ASCII `1`; no IDs or graph objects are supplied by y.
3. Accept exactly when at least K positions are selected and no listed edge
   `(u,v)` has both endpoints selected.

Call this binary relation `R_bits(w,z)`. Framing its inputs as `w#z` uses the
finite alphabet `{0,1,#}` and a delimiter absent from the two input strings.
Malformed frames are rejected. ASCII certificate bytes are serialized by
`pack`, just like x. A valid certificate therefore has bit length

`|z|=8N <= 8B = |w|`.

The fixed certificate exponent is 1. K greater than N is a valid graph input
with no accepting certificate; K=0 permits the all-zero selection. For the
empty graph and K=0, the empty certificate is accepted.

**Existence proof.** If R accepts, the selected indices are distinct vertices,
contain no incompatible pair, and have cardinality at least K, so w belongs
to `L_JSON_IS`. Conversely, for every valid YES record choose any independent
set of size at least K and write its N selection bytes. This certificate
passes each check and satisfies the length bound. For every invalid w, the
first check rejects every z. Thus, for all finite binary strings w,

`w in L_JSON_IS <=> exists z (|z| <= |w| and R_bits(w,z))`.

**Checking-time proof.** Octet and UTF-8 checks scan finite strings. The
bounded-depth JSON grammar can be parsed by finite deterministic scans while
retaining O(B) token data; ID duplicate checks can compare all pairs by
scanning their scalar strings. Rejecting malformed records requires no
unbounded search. Canonical decimal tokens are retained as strings. K may be
compared with the selected count by capped conversion at N+1, without
constructing an integer of magnitude K. Validating endpoints and numeric edge
order likewise uses O(log(B+2))-bit derived indices. Certificate validation
scans y; checking an edge may obtain its two selection bytes by a sequential
scan of y. Even this deliberately naive implementation uses polynomial work
and polynomial storage in the combined input length `|w|+|z|+1`, including
rejection of malformed x and arbitrarily long y. Consequently `R_bits` is a
polynomial-time checking relation and `L_JSON_IS` is in NP. This relation is
an explicit checker for supplied y; the existential proof is not an x-only
procedure for finding y or deciding the language.

## External theorem premise

Cook's Clay description states that 3SAT, with three literals per clause, is
NP-complete. Its polynomial many-one reduction and NP-completeness rules
allow an NP language receiving such a reduction from 3SAT to be declared
NP-complete. These are the external premises; the particular coding,
construction, size bounds, and equivalence below are internal proofs.

Source: Stephen Cook, *The P versus NP Problem*, printed pp. 4-5,
[Clay Mathematics Institute](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf),
Definition 3, Definition 4, Proposition 1(b), and the 3SAT statement.

## Source language and total reduction

Pin an ordinary explicit 3-CNF coding over ASCII bytes, then pack its bytes
into bits by the same rule. The complete grammar is:

```text
W       := zero or more ASCII space, tab, LF, or CR bytes
Positive:= [1-9][0-9]*
Literal := Positive | "-" Positive
Clause  := "[" W Literal W "," W Literal W "," W Literal W "]"
Formula := W "[" W (Clause (W "," W Clause)*)? W "]" W
```

Only complete input matching this grammar is valid. Leading zeros, zero,
plus signs, other whitespace, non-ASCII bytes, fractional/exponent tokens,
extra delimiters, and trailing data are invalid. A positive token identifies
a variable by its exact canonical digit string. Its negative form is the
negation of that variable. Repeated literals and repeated clauses are
allowed. The outer empty array is the true conjunction of zero clauses.
Variables need not have small numeric values: comparing their canonical
digit strings establishes identity without converting them to unbounded
machine integers. The source YES language contains precisely the valid
satisfiable formulas.

This coding has the same ordinary explicit 3SAT problem as the external
premise. Translating an explicitly written 3-CNF formula into this syntax
renames distinct variable identifiers to consecutive positive indices by
finite scans and writes its literal occurrences. Translating back writes
the explicitly present literals and clauses. Both translations have
polynomial time and output size; neither lists every numeric variable up to
the largest label. Invalid inputs in either source coding can be mapped to
the fixed unsatisfiable formula `[[1,1,1],[-1,-1,-1]]`. The recoding therefore
does not assume an implicit exponential variable list.

Define f on **every** source bit string. If the input is not octet-aligned
or does not match the source grammar, output

```json
{"ids":[],"edges":[],"K":1}
```

packed as bits. This is a fixed valid JSON-IS-1 NO instance.

For a valid formula containing m clauses:

1. Create one vertex for each literal occurrence `(i,j)`, where clause index
   `0 <= i < m` and slot `0 <= j < 3`. Order vertices by i and then j. Its
   vertex index is `3*i+j`, and its distinct original occurrence ID is the
   ASCII string `c<i>:l<j>` with canonical decimal indices.
2. For each pair of indices `u<v`, emit one edge if their occurrences are in
   the same clause or are opposite signs of the same variable. Enumerate u
   increasingly and then v increasingly. This directly produces strictly
   increasing numeric pair order, with no loops or duplicate edges, including
   when both edge conditions hold.
3. Write the ordered ID list, emitted index pairs, and canonical decimal
   target `K=m` as the three fields of a JSON-IS-1 record. Pack its UTF-8
   bytes into bits. The occurrence labels are ASCII scalar strings and need
   no exceptional escaping. They identify the original formula positions;
   they do not assert identities of students absent from the source formula.

For m=0 the output is the empty graph with K=0 and is YES. All graph state,
edge tests, ordering, labels, and output are constructed from the source
string alone. No assignment, witness, route, or decider is called.

## Equivalence proof

If the formula is satisfiable, choose a true literal occurrence from each
clause. There are m selected vertices and no same-clause selected pair.
Opposite signs of one variable cannot both be true, so there is no selected
complementary pair either. The selected set is independent, and the output
is YES.

Conversely, each clause's three vertices are mutually adjacent, so an
independent set contains at most one vertex per clause. A set of size at
least m must have exactly one from every clause. The complementary edges
ensure that its selected literals impose no contradictory variable values.
Assign each variable mentioned by a selected positive literal true and each
mentioned by a selected negative literal false; assign the remaining
variables arbitrarily. Every clause has its selected literal true, so the
formula is satisfiable. This also covers repeated occurrences. For m=0,
both the empty conjunction and the zero-target empty graph are YES.

Malformed source inputs are outside the source language and f maps them to
the fixed NO record. Thus for all source bit strings s,

`s in L_3SAT <=> f(s) in L_JSON_IS`.

## Uniform size and bit-work bound

Let `ell=|s|` and let b be its byte length when octet-aligned. Parsing and
validation are finite scans of at most b bytes. For a valid source formula,
`m<=b` and the number of vertices is `N=3m<=3b`. There are at most
`N(N-1)/2` edges. Each emitted endpoint, ID index, and K uses
`O(log(b+2))` decimal bytes. Hence the entire output, including punctuation,
IDs, isolated vertices, and K, has

`O((b+1)^2 log(b+2)) = O((ell+1)^2 log(ell+2))` bits.

A deterministic multitape construction stores the explicit source tokens,
maintains binary loop indices, compares signs and digit strings by scans,
and appends output to an output tape. There are O((b+1)^2) pair tests; even
repeatedly scanning the source for each occurrence comparison costs only
polynomial bit work. Parsing, index arithmetic, label conversion, ordering,
output writing, allocation, and cleanup are included. Sequential simulation
of any indexed store adds at most a polynomial factor because the store and
output sizes are polynomial. One fixed algorithm and fixed polynomial bound
therefore cover every source string, including malformed inputs; the
construction does not change with m, variable-label magnitude, or instance.

Together with NP membership and the external 3SAT premise, this establishes
the NP-completeness of the fixed binary language `L_JSON_IS`. It establishes
no polynomial x-only algorithm for that language. In particular, it does
not repair the candidate's failed local-optimum-to-correct-NO implication.
