# Shared Independent-Set encoding — JSON-IS-1

Selected by the user on 2026-10-05 after the missing-encoding checkpoint at
`c30df58d3ed6622ed731fabc2c71d314f028ad17`. This is the first explicit binding
of the program's input codec, not a claim that older artifacts already used it.
Both theorem directions now use this encoding. Graph semantics are unchanged.

## Input and language

The external input `x` is one finite byte string. Set `B=len(x)` and `n=8B`
bits. A binary-tape input not divisible into complete octets is invalid. No
file path, capacity, selected route, certificate, or second problem input is
part of the instance. Loading the bytes and all subsequent work count.

`x` must be strict UTF-8, without a BOM, containing exactly one JSON object
with three decoded keys: `ids`, `edges`, and `K`. Keys may occur in any order;
each must occur exactly once. JSON whitespace is only space, tab, LF, and CR.
Trailing whitespace is allowed; trailing data is not.

```json
{"ids":["center","left","right"],"edges":[[0,1],[0,2]],"K":2}
```

- `ids` is an ordered array of distinct Unicode scalar strings. Empty IDs,
  escaped NUL, and Unicode noncharacters are allowed. No normalization,
  replacement, or truncation occurs. Standard JSON string escapes are allowed;
  surrogate escapes must pair to form a scalar. Two spellings decoding to the
  same string are duplicate IDs. Precomposed and decomposed strings remain
  distinct. Original identity means the decoded scalar string and its exact
  UTF-8 encoding, rather than its JSON escape spelling.
- `edges` is an array of two-element arrays of natural-number index tokens
  `u,v`, with `0 <= u < v < N`, where `N=len(ids)`. Pairs must be strictly
  increasing in **numeric pair lexicographic order**. Thus reversed edges,
  self-loops, unknown endpoints, repeated edges, and unsorted lists are invalid.
  Vertices without edges remain present in `ids`.
- `K` is a natural-number token. Both K and endpoints have grammar
  `0 | [1-9][0-9]*`. Negative forms (including `-0`), leading zeros, booleans,
  fractions, exponents, NaN, and Infinity are invalid. There is no fixed
  numeral-length limit. `K=0` and `K>N` are valid.

Write `L_Gamma(x)=YES` exactly when x is valid and its decoded simple graph has
an independent set of size at least K. Invalid strings are outside `L_Gamma`.
The decoder reports `INVALID` separately; this is not a proved NO for a valid
graph. A Boolean candidate may reject invalid strings without reporting a
runtime failure as a graph NO.

## Decoder and identity

Executable reference: `candidates/req0009/json_codec.py`, `decode(x)`.

The decoder first validates UTF-8 and bounds structural nesting at three,
ignoring delimiters inside strings. It then parses JSON, rejects decoded
duplicate/unknown keys, and retains integer tokens as decimal strings. This
avoids machine-integer overflow and Python's decimal-conversion digit limit.
Full syntax/escape validation is performed by the standard-library JSON
parser; only expected invalid-encoding exceptions are caught. Memory/runtime
failures propagate and are not graph answers.

After all fields are available, it validates IDs and edges. IDs are compared
using an explicit linear list. All edge indices are bounded by N before use.
It retains exact `k_digits` and derives `k=min(K,N+1)` for this graph's decision.
The cap is decision-sufficient because no independent set exceeds N. It is
not an injective replacement for K; changing N requires reconsidering the
retained exact digits. No graph continuation is used by this candidate.

## Size, cost, and common machine model

The charged model is deterministic multi-tape Turing-machine bit work: each
bit read/write, head move, and finite-control transition costs one step.
Integers and addresses use ordinary finite binary strings with their bit
costs; Unicode and JSON are decoded by finite scans; no oracle, infinite
precision, or free RAM lookup is allowed. Python is a reference implementation,
not a unit-cost arithmetic definition of this model.

For valid inputs, `N<=B`, `M=|edges|<=B`, total decoded ID UTF-8 bytes `<=B`, and
total raw numeral bytes `<=B`. Decimal tokens are scanned; only bounded derived
integers are accumulated. Syntax/scalar checks are linear scans; duplicate ID
checks are conservatively `O(B^2)` character work. Edge-order/range checks are
polynomial scans with `O(log(B+2))`-bit derived integers. Constructing an explicit
N-by-N adjacency matrix is charged separately. Decoder/parser allocation,
conversion, comparisons, and cleanup count; the executable's measurements do
not establish a numeric Turing-machine constant.

Every finite simple graph and nonnegative K has an encoding: order its vertices,
give them distinct scalar labels, sort canonical index pairs, and write K's
decimal token. Original IDs can be preserved whenever supplied as distinct
scalar strings. For encoded-language hardness, an explicit-vertex adjacency
matrix Independent-Set input translates polynomially by assigning index labels
and listing edges; JSON-IS-1 translates back polynomially by decoding explicit
vertices and building the matrix. If K>N, emit any fixed standard NO instance.
These translations avoid a binary vertex-count encoding hiding exponentially
many unlisted isolates. They do not construct an independent set.

No source theorem or P-vs-NP status changes by selecting this codec.
