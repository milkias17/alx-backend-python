#!/usr/bin/env python3
"""Element length module"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns element length"""
    return [(i, len(i)) for i in lst]
