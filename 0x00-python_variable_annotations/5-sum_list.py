#!/usr/bin/env python3

def sum_list(input_list: list[float]) -> float:
    if len(input_list) == 0:
        return 0
    return input_list[0] + sum_list(input_list[1:])
