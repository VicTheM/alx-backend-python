#!/usr/bin/env python3
"""
Create a measure_time function with integers n and max_delay
as arguments that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n.
Your function should return a float.
"""

import asyncio
import random
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Returns the average execution time of wait_n"""
    s = time.perf_counter()
    await wait_n(n, max_delay)
    elapsed = time.perf_counter() - s
    return elapsed / n
