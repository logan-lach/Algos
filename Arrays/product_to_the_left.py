from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    to_the_left = []

    prev_mult = 1
    for i in range(len(nums)):
        to_the_left.append(prev_mult)
        prev_mult *= nums[i]

    prev_mult = 1
    for i in range(len(nums) - 1, -1, -1):
        to_the_left[i] *= prev_mult
        prev_mult *= nums[i]

    return to_the_left