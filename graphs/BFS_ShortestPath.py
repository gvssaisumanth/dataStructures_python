def bfsShortpath(graph, start, goal):
    queue = [[start]]
    distance = 0
    previous_node = [start]

    if start == goal:
        print("goal is same as start")
        return queue[0]

    while queue:
        path = queue.pop(0)  # pulling out the latest added path
        node = path[-1]  # pulling out latest added vertex or node

        neighbours = graph[node]

        # checking if node is present in the connected edges of vertex
        if goal in neighbours:
            path.append(goal)
            print("distance from ",  start,  " is", distance)
            return path

        for neighbour in neighbours:
            if neighbour not in previous_node:
                new_path = path[:]  # copy operation we are copying latest path
                new_path.append(neighbour)
                queue.append(new_path)
                previous_node.append(neighbour)
        distance += 1

    print("no path found")
    return []


graph = {
    'a': ['b'],
    'b': ['a', 'e', 'c'],
    'c': ['b', 'd'],
    'd': ['c', 'e'],
    'e': ['a']
}
path = bfsShortpath(graph, 'a', 'd')
print(path)
