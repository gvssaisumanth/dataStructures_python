#!/usr/bin/python3


def bellman_ford(edges, no_of_nodes, source):
    distance = [float('Inf')]*no_of_nodes
    distance[source] = 0
    predecessor = [None] * no_of_nodes

    for _ in range(no_of_nodes-1):
        for u, v, w in edges:
            if distance[u]+w < distance[v]:
                distance[v] = u
                predecessor[v] = u

    for u, v, w in edges:
        if distance[u]+w < distance[v]:
            return False, distance, predecessor

    return True, distance, predecessor


edges = [
    # (source, target, weight)
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3),
]

num_nodes = 5

source = 0  # start node

success, distances, predecessors = bellman_ford(edges, num_nodes, source)
