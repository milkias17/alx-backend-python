#!/usr/bin/env python3
"""Element length module"""

from typing import Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> list[Sequence, int]:
    """returns element length"""
    return [(i, len(i)) for i in lst]
