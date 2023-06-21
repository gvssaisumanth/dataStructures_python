import heapq


def dijiktras(graph, start, end):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    parentsMap = {}  # keep track of parents
    priorityQueue = [(0, start)]
    visited = [start]

    while priorityQueue:
        current_dist, current_node = heapq.heappop(priorityQueue)
        visited.append(current_node)
        # print("distances", distances)
        # print("parents", parentsMap)
        # print("priority queue", priorityQueue, "\n")
        if current_node == end:
            path = []

            while current_node != start:
                path.append(current_node)
                current_node = parentsMap[current_node]
            path.append(current_node)
            path.reverse()
            return path, distances[end]

        for neighbour, weight in graph[current_node].items():
            if neighbour in visited:
                continue
            else:
                visited.append(neighbour)
                new_cost = current_dist+weight
                if new_cost < distances[neighbour]:
                    distances[neighbour] = new_cost
                    # assigning parent to the shorest weighted node
                    parentsMap[neighbour] = current_node
                    heapq.heappush(priorityQueue, (new_cost, neighbour))
    return distances


# example_graph = {
#     'U': {'V': 2, 'W': 5, 'X': 1},
#     'V': {'U': 2, 'X': 2, 'W': 3},
#     'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
#     'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
#     'Y': {'X': 1, 'W': 1, 'Z': 1},
#     'Z': {'W': 5, 'Y': 1},
# }

# print(dijiktras(example_graph, 'U', 'Z'))

example_graph = {
    'A': {'B': 4, 'C': 5, 'D': 2},
    'B': {'A': 4, 'F': 1},
    'C': {'A': 5, 'E': 4},
    'D': {'A': 2, 'E': 4},
    'E': {'D': 4, 'F': 2, 'G': 3},
    'F': {'G': 1},
    'G': {'F': 1}
}

print(dijiktras(example_graph, 'A', 'I'))
