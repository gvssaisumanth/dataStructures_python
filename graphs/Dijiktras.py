import heapq


def dijiktras(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    priorityQueue = [(0, start)]
    visited = [start]

    while priorityQueue:
        current_dist, current_node = heapq.heappop(priorityQueue)
        visited.append(current_node)
        

        for neighbour, weight in graph[current_node].items():
            if neighbour in visited:
                continue
            else:
                visited.append(neighbour)
                new_cost = current_dist+weight
                if new_cost < distances[neighbour]:
                    distances[neighbour] = new_cost
                    heapq.heappush(priorityQueue, (new_cost, neighbour))
    return distances


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

print(dijiktras(example_graph, 'W'))
