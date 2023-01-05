#!/usr/bin/env python3
"""make_multiplier module"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Make multiplier"""
    return lambda x: x * multiplier
