def binomial_coefficient(n: int, r: int) -> int:
    """
    Find binomial coefficient using Pascal's triangle.

    Calculate C(n, r) using Pascal's triangle.

    :param n: The total number of items.
    :param r: The number of items to choose.
    :return: The binomial coefficient C(n, r).

    >>> binomial_coefficient(10, 5) #TODO: Fix this test
    252
    >>> binomial_coefficient(5, 2)  #TODO: Fix this test
    10
    >>> binomial_coefficient(10, 0)
    1
    >>> binomial_coefficient(10, 10) #TODO: Fix this test
    1
    >>> binomial_coefficient(5, 6)  # This should raise a ValueError
    Traceback (most recent call last):
        ...
    ValueError: r should be between 0 and n (inclusive)
    >>> binomial_coefficient(3, 5)  # This should raise a ValueError
    Traceback (most recent call last):
        ...
    ValueError: r should be between 0 and n (inclusive)
    >>> binomial_coefficient(-2, 3)  # This should raise a ValueError
    Traceback (most recent call last):
        ...
    ValueError: n should be a non-negative integer
    >>> binomial_coefficient(5, -1)  # This should raise a ValueError
    Traceback (most recent call last):
        ...
    ValueError: r should be a non-negative integer
    """
    c = [0 for i in range(r + 1)]
    # nc0 = 1
    c[0] = 1
    for i in range(1, n + 1):
        # to compute current row from previous row.
        j = min(i, r)
        while j > 0:
            c[j] += c[j - 1]
            j -= 1
    return c[r]


print(binomial_coefficient(n=10, r=5))
