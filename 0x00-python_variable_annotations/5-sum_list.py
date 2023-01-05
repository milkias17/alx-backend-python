#!/usr/bin/env python3
"""Sum List Module"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of elements in a list"""
    if len(input_list) == 0:
        return 0
    return input_list[0] + sum_list(input_list[1:])
