#!/usr/bin/env python3
"""to_kv module"""

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """returns tuple"""
    return (k, v ** 2)
