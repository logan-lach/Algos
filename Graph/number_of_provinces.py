from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    count_connected = 0
    seen = set()

    def search(column):

        queue = [column]

        while len(queue) != 0:
            node = queue.pop()

            if node in seen:
                continue

            seen.add(node)
            isConnected[node][node] = 0

            for i in range(len(isConnected)):
                if isConnected[i][node] == 1:
                    queue.append(i)

    for i in range(len(isConnected[0])):
        if i not in seen:
            count_connected += 1
            search(i)
    return count_connected
