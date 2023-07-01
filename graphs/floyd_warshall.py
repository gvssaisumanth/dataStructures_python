#!/usr/bin/python3

import numpy as np


def floyd_warshall(edge_list, no_of_nodes):

    # filling infinity in all cells of the matrix
    dist = np.full((no_of_nodes, no_of_nodes), np.inf)

    # keeping track of previous vertex
    next_vertex = np.zeros((no_of_nodes, no_of_nodes), dtype=int)

    for i in range(no_of_nodes):
        dist[i][i] = 0
        for j in range(no_of_nodes):
            next_vertex[i][j] = j

    # replacing already known values
    for u, v, w in edge_list:
        dist[u][v] = w

    for k in range(no_of_nodes):
        for i in range(no_of_nodes):
            for j in range(no_of_nodes):

                if dist[i][j] > dist[k][j] + dist[i][k]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]
    return dist, next_vertex


def reconstruct_path(start, end, next_vertex):
    path = [start]
    while start != end:
        start = next_vertex[start][end]
        path.append(start)
    return path


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

distances, next_vertices = floyd_warshall(num_nodes, edges)
print(f"All-pairs shortest distances:\n{distances}")

start, end = 0, 4  # change as needed
path = reconstruct_path(start, end, next_vertices)
print(f"Shortest path from node {start} to node {end}: {path}")
