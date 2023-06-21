def bfs(graph, start):
    visited = [start]
    queue = [start]
    while queue:
        m = queue.pop(0)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        print(m, end=" ")


graph = {
    'a': ['b', 'e'],
    'b': ['a', 'e', 'c'],
    'c': ['b', 'd'],
    'd': ['c', 'e'],
    'e': ['a']
}

print("Following is the Breadth-First Search")
bfs(graph, 'a')
