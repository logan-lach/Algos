import math
from typing import List


def minSubArrayLen(target: int, A: List[int]) -> int:
    start = 0
    total = 0
    shortest = math.inf

    for i in range(len(A)):

        total += A[i]

        while total >= target and start <= i:
            shortest = min(shortest, i - start + 1)
            total -= A[start]
            start += 1

    return shortest if shortest != math.inf else 0