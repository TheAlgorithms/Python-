"""
== Automorphic Numbers ==
A number n is said to be a Automorphic number if
the square of n "ends" in the same digits as n itself.

Examples of Automorphic Numbers: 0, 1, 5, 6, 25, 76, 376, 625, 9376, 90625, ...
https://en.wikipedia.org/wiki/Automorphic_number
"""

# Author : Akshay Dubey (https://github.com/itsAkshayDubey)
# Time Complexity : O(log10n)


def is_automorphic_number(n: int) -> bool:
    if not isinstance(number, int):
        raise TypeError(f"Input value of [number={number}] must be an integer")
    if n < 0:
        return False
    n_square = n * n
    while (n > 0):
        if (n % 10 != n_square % 10):
            return False
        n //= 10
        n_square //= 10
    return True


if __name__ == "__main__":
    number = int(input("Enter number: ").strip())
    if is_automorphic_number(number):
        print(f"{number} is a automorphic Number.")
    else:
        print(f"{number} is not a automorphic Number.")