from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    # This is just breadth first search

    original_color = image[sr][sc]
    queue = [(sr, sc)]

    visited = dict()

    for i in range(len(image)):
        visited[i] = []

    while len(queue) != 0:
        x, y = queue[0]
        queue = queue[1:]

        if y in visited[x]:
            continue

        image[x][y] = newColor
        visited[x].append(y)

        if x + 1 < len(image) and image[x + 1][y] == original_color:
            queue.append((x + 1, y))

        if x - 1 >= 0 and image[x - 1][y] == original_color:
            queue.append((x - 1, y))

        if y + 1 < len(image[0]) and image[x][y + 1] == original_color:
            queue.append((x, y + 1))

        if y - 1 >= 0 and image[x][y - 1] == original_color:
            queue.append((x, y - 1))

    return image

print(floodFill([[0,0,0],[0,1,1]],
1,
1,
1))