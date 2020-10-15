"""
Project Euler Problem 62: https://projecteuler.net/problem=62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3)
and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three
permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""


from collections import defaultdict
from math import ceil, floor


def solution(num_perms: int = 5) -> int:
    """
    Return the smallest cube for which exactly five permutations of its digits are cube.
    >>> solution(2)
    125
    >>> solution(3)
    41063625
    >>> solution(4)
    1006012008
    """
    cube_len = 1
    while True:
        d = defaultdict(list)
        lower_bound = ceil(10 ** ((cube_len - 1) / 3))
        upper_bound = floor(10 ** (cube_len / 3)) + 1

        for cube_base in range(lower_bound, upper_bound):
            cube = cube_base * cube_base * cube_base
            s = "".join(sorted(list(str(cube))))
            d[s].append(cube_base)

        for s in d:
            if len(d[s]) == num_perms:
                return d[s][0] ** 3

        cube_len += 1


if __name__ == "__main__":
    print(f"{solution() = }")
