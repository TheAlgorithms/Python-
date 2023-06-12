"""
The Reverse Polish Nation also known as Polish postfix notation
or simply postfix notation.
https://en.wikipedia.org/wiki/Reverse_Polish_notation
Classic examples of simple stack implementations
Valid operators are +, -, *, /.
Each operand may be an integer or another expression.
"""
from __future__ import annotations

from typing import Any


def evaluate_postfix(postfix_notation: list) -> int:
    """
    >>> evaluate_postfix(["2", "1", "+", "3", "*"])
    9
    >>> evaluate_postfix(["4", "13", "5", "/", "+"])
    6
    >>> evaluate_postfix(["2", "+"])
    2
    >>> evaluate_postfix(["5", "-"])
    -5
    >>> evaluate_postfix([])
    0
    >>> evaluate_postfix(["5"])
    5
    >>> evaluate_postfix(["5", "A"])
    Traceback (most recent call last):
     ...
    ValueError: invalid literal for int() with base 10: 'A'
    >>> evaluate_postfix(["5", "4", "A"])
    Traceback (most recent call last):
     ...
    ValueError: invalid literal for int() with base 10: 'A'
    >>> evaluate_postfix(["A"])
    Traceback (most recent call last):
     ...
    ValueError: invalid literal for int() with base 10: 'A'"""
    if not postfix_notation:
        return 0

    operations = {"+", "-", "*", "/"}
    stack: list[Any] = []

    for token in postfix_notation:
        if token in operations:
            if len(stack) == 0:
                msg = f"{token} operator with no operand(s)"
                raise ValueError(msg)
            if token == "-" and len(stack) < 2:
                operand = stack.pop()
                stack.append(-operand)
            else:
                b, a = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    if b == 0:
                        raise ValueError("Invalid expression: division by zero")
                    stack.append(a // b)
                else:
                    msg = f"Unrecognized {token = }"
                    raise ValueError(msg)
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
