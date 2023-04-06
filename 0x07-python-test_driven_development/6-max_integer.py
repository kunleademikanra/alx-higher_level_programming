#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(lst=None):
    """Finds the maximum integer in a list of integers.

    Args:
        lst (list): The list of integers to search.
    Returns:
        int: The maximum integer in the list.
    Raises:
        TypeError: If lst is not a list.
        ValueError: If lst is an empty list.
    """
    if lst is None:
        lst = []
    if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    if len(lst) == 0:
        raise ValueError("lst cannot be an empty list")

    result = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > result:
            result = lst[i]
    return result
