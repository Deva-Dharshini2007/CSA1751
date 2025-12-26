# ---------- A* Search : Problem 1 ----------

import heapq

def astar(graph, h, start, goal):
    pq = [(h[start], start, [start], 0)]
    visited = set()

    while pq:
        f, node, path, g = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            print("Optimal Path :", " -> ".join(path))
            print("Actual Cost g(n) :", g)
            print("Final f(n)=g+h  :", f)
            return

        for neigh, cost in graph[node]:
            g2 = g + cost
            f2 = g2 + h[neigh]
            heapq.heappush(pq, (f2, neigh, path + [neigh], g2))

    print("No path found")


graph = {
    'S': [('A', 10), ('B', 5)],
    'A': [('C', 5)],
    'B': [('A', 4), ('D', 7), ('E', 3)],
    'C': [('F', 4)],
    'D': [('C', 3)],
    'E': [('D', 2), ('F', 6)],
    'F': []
}

h = {
    'S': 11,
    'A': 6,
    'B': 9,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 0
}

print("A* Search — Problem 1")
astar(graph, h, start='S', goal='F')

# ---------- A* Search : Problem 2 ----------

import heapq

def astar(graph, h, start, goal):
    pq = [(h[start], start, [start], 0)]
    visited = set()

    while pq:
        f, node, path, g = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            print("Optimal Path :", " -> ".join(path))
            print("Actual Cost g(n) :", g)
            print("Final f(n)=g+h  :", f)
            return

        for neigh, cost in graph[node]:
            g2 = g + cost
            f2 = g2 + h[neigh]
            heapq.heappush(pq, (f2, neigh, path + [neigh], g2))

    print("No path found")


graph = {
    'A': [('B', 6), ('D', 4)],
    'B': [('C', 3), ('E', 2)],
    'C': [('F', 2)],
    'D': [('E', 3)],
    'E': [('F', 5), ('G', 3)],
    'F': [],
    'G': [('F', 2)]
}

h = {
    'A': 8,
    'B': 6,
    'C': 2,
    'D': 4,
    'E': 3,
    'F': 0,
    'G': 1
}

print("A* Search — Problem 2")
astar(graph, h, start='A', goal='F')





