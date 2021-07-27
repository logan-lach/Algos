from typing import List


def max_clique(n, m, edges):

    adj_matrix = {
        int: List[int]
    }

    for i in edges:
        if i[0] in edges:
            adj_matrix[i[0]].append(i[1])
        else:
            adj_matrix[i[0]] = [i[1]]





