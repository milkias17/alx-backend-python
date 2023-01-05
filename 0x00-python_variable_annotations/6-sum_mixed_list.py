#!/usr/bin/env python3

from typing import Union


def sum_mixed_list(mxd_list: list[Union[int, float]]) -> float:
    if len(mxd_list) == 0:
        return 0
    return mxd_list[0] + sum_mixed_list(mxd_list[1:])
