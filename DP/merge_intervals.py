from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x: x[1])

    i = 0

    while len(intervals) - i - 1 > 0:
        val = len(intervals) - i - 1
        if intervals[val - 1][1] < intervals[val][0]:
            i -= 1
        else:
            intervals[val - 1][0] = min(intervals[val - 1][0], intervals[val][0])
            intervals[val - 1][1] = max(intervals[val - 1][1], intervals[val][1])
            del intervals[val]

    return intervals

print(merge([[1,4],[4,5]]))