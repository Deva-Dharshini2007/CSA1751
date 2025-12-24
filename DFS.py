graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = set()

def dfs(node):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

print("DFS Traversal:")
dfs('A')
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

visited = set()

def dfs(node):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

print("DFS Traversal:")
dfs(1)

graph = {
    1: [2, 7],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [8, 10],
    8: [9],
    9: [],
    10: []
}

visited = set()

def dfs(node):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

print("DFS Traversal:")
dfs(1)
graph = {
    0: [1],
    1: [3, 2],
    2: [4],
    3: [7],
    4: [5, 6],
    5: [],
    6: [],
    7: []
}

visited = set()

def dfs(node):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

print("DFS Traversal:")
dfs(0)

