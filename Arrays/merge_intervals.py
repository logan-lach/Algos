from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 0:
        return []

    intervals = sorted(intervals, key=lambda x: x[0])

    prev_index = 0
    prev_start, prev_end = intervals[0]

    for i in range(1, len(intervals)):

        if intervals[i][0] > prev_end:
            prev_index = i
            prev_start, prev_end = intervals[i]

        else:
            intervals[prev_index][0] = min(prev_start, intervals[i][0])
            intervals[prev_index][1] = max(prev_end, intervals[i][1])

            prev_start = intervals[prev_index][0]
            prev_end = intervals[prev_index][1]

            intervals[i] = None

    return [x for x in intervals if x is not None]


