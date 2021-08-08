from typing import List


def numIslands(grid: List[List[str]]) -> int:
    def bfs(a, b):

        queue = [(a, b)]

        while len(queue) != 0:
            x, y = queue[0]
            queue = queue[1:]

            if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0 or grid[x][y] == "0":
                continue

            grid[x][y] = "0"

            if x + 1 < len(grid) and grid[x + 1][y] == "1":
                queue.append((x + 1, y))
            if x - 1 >= 0 and grid[x - 1][y] == "1":
                queue.append((x - 1, y))
            if y + 1 < len(grid[0]) and grid[x][y + 1] == "1":
                queue.append((x, y + 1))
            if y - 1 >= 0 and grid[x][y - 1] == "1":
                queue.append((x, y - 1))

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                bfs(i, j)
    return count

print(numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))

