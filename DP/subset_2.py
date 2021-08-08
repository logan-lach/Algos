from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    def sink(nums):

        if len(nums) <= 1:
            sets.add(frozenset(nums))
            return nums

        hold = []
        for i in range(len(nums)):
            prev = sink(nums[0:i]) + sink(nums[i + 1:])
            for x in prev:
                hold.append(prev.append(nums[i]))
                sets.add(frozenset(prev.append(nums[i])))
        return hold

    sets = set(frozenset([]))
    sink(nums)
    return sets

print(subsetsWithDup([1,2,2]))