from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    # This one's a DP problem

    visited = {x:set() for x in range(len(heights))}

    def bfs(x, y):

        res = {""}
        visited[x].add(y)
        if x == 0 or y == 0:
            res.add("P")
        if x == len(heights) - 1 or y == len(heights[0]) - 1:
            res.add("A")

        if x + 1 < len(heights) and y not in visited[x+1]:
            if type(heights[x + 1][y]) is not str and heights[x + 1][y] <= heights[x][y]:
                bfs(x + 1, y)
            if type(heights[x + 1][y]) is str:
                res.add(heights[x + 1][y])

        if x - 1 >= 0 and y not in visited[x-1]:
            if type(heights[x - 1][y]) is not str and heights[x - 1][y] <= heights[x][y]:
                bfs(x - 1, y)
            if type(heights[x - 1][y]) is str:
                res.add(heights[x - 1][y])

        if y + 1 < len(heights[0]) and y+1 not in visited[x]:
            if type(heights[x][y + 1]) is not str and heights[x][y + 1] <= heights[x][y]:
                bfs(x, y + 1)
            if type(heights[x][y + 1]) is str:
                res.add(heights[x][y + 1])

        if y - 1 >= 0 and y-1 not in visited[x]:
            if type(heights[x][y - 1]) is not str and heights[x][y - 1] <= heights[x][y]:
                bfs(x, y - 1)
            if type(heights[x][y - 1]) is str:
                res.add(heights[x][y - 1])

        s = "".join(sorted(list(res)))
        heights[x][y] = s


    futures = []
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            if type(heights[i][j]) == str:
                if heights[i][j] == 'AP':
                    futures.append([i, j])
            else:
                bfs(i, j)
    return futures

print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))