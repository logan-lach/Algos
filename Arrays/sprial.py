from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    count = 0
    x = 0
    y = 0
    res = []

    while len(res) < len(matrix) * len(matrix[0]):

        res.append(matrix[x][y])
        matrix[x][y] = -101
        if count == 0:
            if y + 1 < len(matrix[0]) and matrix[x][y + 1] != -101:
                y += 1
            else:
                count += 1
                x -= 1

        elif count == 1:
            if x + 1 < len(matrix) and matrix[x + 1][y] != -101:
                x += 1
            else:
                count += 1
                y -= 1

        elif count == 2:
            if y - 1 > -1 and matrix[x][y - 1] != -101:
                y -= 1
            else:
                count += 1
                x -= 1

        elif count == 3:
            if x - 1 > -1 and matrix[x - 1][y] != -101:
                x -= 1
            else:
                count = 0
                y += 1
    return res

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

