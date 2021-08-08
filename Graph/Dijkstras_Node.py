import heapq
def do_dijkstras(edges, start, end):
    edges = edges[0]
    visited = set()
    max_values = {
        start: 1
    }
    p_queue = [(1, start)]

    while len(p_queue) > 0:
        weight, vertex = heapq.heappop(p_queue)
        if vertex in visited:
            continue
        if vertex in edges.keys():
            for nodes in edges[vertex].keys():
                if nodes in max_values.keys():
                    max_values[nodes] = max(max_values[nodes], max_values[vertex] * float(edges[vertex][nodes]))
                else:
                    max_values[nodes] = float(max_values[vertex] * float(edges[vertex][nodes]))
                heapq.heappush(p_queue, (-float(edges[vertex][nodes]), nodes))
        visited.add(vertex)
    return max_values









print(do_dijkstras([{'USD': {'GBP': '0.7', 'JPY': '109'}, 'GBP': {'JPY': '155'}, 'CAD': {'CNY': '5.27', 'KRW': '921'}}
], 'USD', 'JPY'))
