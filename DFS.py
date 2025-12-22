from collections import deque

# Graph definition
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS:", end=" ")
    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print()

# DFS Function (Recursive)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        print("DFS:", end=" ")

    visited.add(start)
    print(start, end=" ")

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

# Function calls
bfs(graph, 0)
dfs(graph, 0)
