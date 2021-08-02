def searchMatrix(matrix, target: int) -> bool:
    start = 0
    end = len(matrix) * len(matrix[0]) - 1

    while start < end - 1:
        mid = int((start + end) / 2)

        if matrix[int(mid / len(matrix))][int(mid % len(matrix))] < target:
            start = mid
        elif matrix[int(mid / len(matrix))][int(mid % len(matrix))] > target:
            end = mid
        else:
            return True

    return matrix[int(start / len(matrix))][int(start % len(matrix))] == target or matrix[int(end / len(matrix))][
        int(end % len(matrix))] == target


print(searchMatrix([[1,1]], 0))