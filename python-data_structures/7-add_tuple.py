#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    padded_tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    padded_tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

    truncated_tuple_a = padded_tuple_a[:2]
    truncated_tuple_b = padded_tuple_b[:2]

    res = tuple(map(lambda i, j: i + j, truncated_tuple_a, truncated_tuple_b))

    return res
