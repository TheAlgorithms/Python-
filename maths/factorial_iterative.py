"""Factorial of a positive integer -- https://en.wikipedia.org/wiki/Factorial
"""


def factorial(input_number: int) -> int:
    """
    Calculate the factorial of specified number (n!).

    >>> import math
    >>> all(factorial(i) == math.factorial(i) for i in range(20))
    True
    >>> factorial(0.1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() only accepts integral values
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() not defined for negative values
    >>> factorial(1)
    1
    >>> factorial(6)
    720
    >>> factorial(0)
    1
    """
    if input_number != int(input_number):
        raise ValueError("factorial() only accepts integral values")
    if input_number < 0:
        raise ValueError("factorial() not defined for negative values")
    value = 1
    for i in range(1, input_number + 1):
        value *= i
    return value


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    n = int(input("Enter a positive integer: ").strip() or 0)
    print(f"factorial{n} is {factorial(n)}")
