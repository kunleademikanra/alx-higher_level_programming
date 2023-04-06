#!/usr/bin/python3
"""Defines an integer addition function."""


def integer_addition(x, y=98):
    """Return the sum of two integers.

    Float arguments are converted to integers before the addition is performed.

    Raises:
        TypeError: If either x or y is not an integer or a float.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be an integer or a float")
    if not isinstance(y, (int, float)):
        raise TypeError("y must be an integer or a float")
    return int(x) + int(y)

