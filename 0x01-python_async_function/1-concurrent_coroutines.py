#!/usr/bin/env python3
"""wait_n should return the list of all the delays
(float values). The list of the delays should be in
ascending order without using sort() because of concurrency."""

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of delays in ascending order"""
    delays = [wait_random(max_delay) for _ in range(n)]

    return [await delay for delay in asyncio.as_completed(delays)]
