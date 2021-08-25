from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # Big binary search

    start = 0
    end = len(matrix) * len(matrix[0]) - 1

    while start < end - 1:
        mid = ((start + end) // 2)

        if matrix[mid // len(matrix)][mid % len(matrix[0])] < target:
            start = mid
        else:
            end = mid
    return matrix[start // len(matrix)][start % len(matrix[0])] == target or matrix[end // len(matrix)][start % len(matrix[0])] == target

print(searchMatrix([[1,1]],3))
