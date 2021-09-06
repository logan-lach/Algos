from typing import List


def numSubarrayProductLessThanK(A: List[int], k: int) -> int:

    if k == 0:
        return 0

    amount = 0
    total = 1

    current_run = 0
    start = 0
    for i in range(len(A)):
        total *= A[i]
        if total < k:
            current_run += 1
            amount += current_run

        else:

            while total >= k and start <= i:
                total //= A[start]
                start += 1
                current_run -= 1
            current_run += 1
            amount += current_run

    return amount

print(numSubarrayProductLessThanK([10,5,2,6], 100))



