#!/usr/bin/env python3
"""Concurrent python"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Import wait_random from the previous python file that you’ve
    written and write an async routine called wait_n that takes in
    2 int arguments (in this order): n and max_delay. You will spawn
    wait_random n times with the specified max_delay.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
