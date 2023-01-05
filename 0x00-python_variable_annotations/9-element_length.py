#!/usr/bin/env python3

from typing import Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> list[Sequence, int]:
    return [(i, len(i)) for i in lst]
