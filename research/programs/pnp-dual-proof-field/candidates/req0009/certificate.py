"""Supplied-witness relation, not a constructor or decider.

y has exactly one ASCII 0/1 byte per ordered vertex. Its bit encoding has
length 8N <= len(x)*8. This module never discovers a witness or calls A.
"""
from json_codec import decode


def R(x: bytes, y: bytes) -> bool:
    """Check R(x,y); malformed strings reject, runtime errors propagate."""
    graph = decode(x)
    if graph is None or type(y) is not bytes or len(y) != len(graph.ids):
        return False
    if any(bit not in (48, 49) for bit in y):
        return False
    if y.count(b'1') < graph.k:
        return False
    return all(not (y[u] == 49 and y[v] == 49) for u, v in graph.edges)
