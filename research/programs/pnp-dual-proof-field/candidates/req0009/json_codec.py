"""Decode the pinned JSON Independent-Set substrate, without deciding the graph.

The input is exactly a UTF-8 JSON object with decoded keys ``ids``, ``edges``
and ``K``. IDs are distinct Unicode scalar strings. Edges are strictly
increasing integer pairs ``0 <= u < v < len(ids)``. All number tokens must be
canonical nonnegative decimal integers. Malformed encodings and unsupported
argument types return ``None``; resource/runtime failures are not graph NOs.

``k`` is only a derived cap at ``len(ids) + 1``. ``k_digits`` retains the exact
target for reconstruction and comparisons after any change to the graph.
"""

from __future__ import annotations

from dataclasses import dataclass
import json


@dataclass(frozen=True)
class Instance:
    ids: tuple[str, ...]
    edges: tuple[tuple[int, int], ...]
    k_digits: str
    k: int
    n_bits: int


@dataclass(frozen=True)
class _IntegerToken:
    # A separate type keeps numeral tokens distinguishable from JSON strings.
    digits: str


class _InvalidEncoding(ValueError):
    pass


def _scalar_string(value: object) -> bool:
    return type(value) is str and all(
        not 0xD800 <= ord(character) <= 0xDFFF for character in value
    )


def _bounded_nesting(text: str) -> bool:
    """Bound parser depth before json.loads, ignoring brackets in strings.

    Valid records need at most object -> edges array -> edge-pair array.
    Full syntax and matching delimiter types remain json.loads' responsibility.
    """
    depth = 0
    in_string = False
    escaped = False
    for character in text:
        if in_string:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_string = False
        elif character == '"':
            in_string = True
        elif character in "[{":
            depth += 1
            if depth > 3:
                return False
        elif character in "]}":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0 and not in_string


def _integer_token(digits: str) -> _IntegerToken:
    # Retaining the token bypasses Python's decimal-to-int digit limit.
    if (
        not digits
        or (digits[0] == "0" and len(digits) != 1)
        or any(character < "0" or character > "9" for character in digits)
    ):
        raise _InvalidEncoding("noncanonical natural number")
    return _IntegerToken(digits)


def _reject_number(token: str):
    raise _InvalidEncoding("float or non-JSON constant")


def _object_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    # Only three fixed keys can survive. Duplicate checking uses a linear list,
    # including keys whose different escape spellings decode identically.
    if len(pairs) != 3:
        raise _InvalidEncoding("object does not have exactly three keys")
    seen: list[str] = []
    result: dict[str, object] = {}
    for key, value in pairs:
        if not _scalar_string(key) or key not in ("ids", "edges", "K"):
            raise _InvalidEncoding("unknown or nonscalar key")
        if key in seen:
            raise _InvalidEncoding("duplicate decoded key")
        seen.append(key)
        result[key] = value
    return result


def _capped_decimal(digits: str, cap: int) -> int:
    """Parse a previously validated token without constructing a huge int."""
    value = 0
    for character in digits:
        value = value * 10 + ord(character) - ord("0")
        if value >= cap:
            return cap
    return value


def decode(x: bytes) -> Instance | None:
    """Return a lossless semantic instance, or None for an invalid encoding.

    Only exact ``bytes`` arguments belong to this API's encoded-input domain.
    Unicode decoding and JSON syntax errors are expected invalid encodings;
    MemoryError and unexpected implementation/runtime errors propagate.
    """
    if type(x) is not bytes:
        return None
    try:
        text = x.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        return None
    if not _bounded_nesting(text):
        return None
    try:
        record = json.loads(
            text,
            parse_int=_integer_token,
            parse_float=_reject_number,
            parse_constant=_reject_number,
            object_pairs_hook=_object_pairs,
            strict=True,
        )
    except (json.JSONDecodeError, _InvalidEncoding):
        return None
    if type(record) is not dict:
        return None

    labels = record["ids"]
    raw_edges = record["edges"]
    target = record["K"]
    if (
        type(labels) is not list
        or type(raw_edges) is not list
        or type(target) is not _IntegerToken
    ):
        return None

    ids: list[str] = []
    for label in labels:
        if not _scalar_string(label) or label in ids:
            return None
        ids.append(label)

    # Keys may occur in any order, so numeral conversion waits until N is known.
    size = len(ids)
    cap = size + 1
    edges: list[tuple[int, int]] = []
    previous: tuple[int, int] | None = None
    for pair in raw_edges:
        if (
            type(pair) is not list
            or len(pair) != 2
            or type(pair[0]) is not _IntegerToken
            or type(pair[1]) is not _IntegerToken
        ):
            return None
        u = _capped_decimal(pair[0].digits, cap)
        v = _capped_decimal(pair[1].digits, cap)
        edge = (u, v)
        if not 0 <= u < v < size or (previous is not None and edge <= previous):
            return None
        edges.append(edge)
        previous = edge

    return Instance(
        ids=tuple(ids),
        edges=tuple(edges),
        k_digits=target.digits,
        k=_capped_decimal(target.digits, cap),
        n_bits=8 * len(x),
    )
