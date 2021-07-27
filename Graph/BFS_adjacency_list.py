from collections import deque

adj = [
    [0,0,0,1,1,1],
    [0,0,1,0,0,0],
    [0,1,0,0,1,0],
    [1,0,0,0,0,1],
    [1,0,1,0,0,0],
    [1,1,0,1,0,0]
]



def bfs(max_nodes):
    visited = set()
    queue = deque([0])

    while len(visited) != max_nodes and len(queue) > 0:

        node = queue.popleft()
        if node not in visited:
            visited.add(node)

            for i in range(len(adj)):
                if adj[node][i] == 1:
                    queue.append(i)

            print(node)

bfs(6)