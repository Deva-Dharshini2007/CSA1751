# -------- Greedy Best First Search — Problem 1 --------

import heapq

def greedy_best_first(graph, h, start, goal):
    pq = [(h[start], start, [start])]
    visited = set()

    while pq:
        _, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            print("Visited Order :", visited)
            print("GBFS Path      :", " -> ".join(path))
            return

        for neigh in graph[node]:
            heapq.heappush(pq, (h[neigh], neigh, path + [neigh]))

    print("No path found")


# ---- Edit edges as per your notebook graph ----
graph = {
    'A': ['D', 'C', 'B'],
    'D': ['F'],
    'C': ['F', 'G'],
    'B': ['E'],
    'E': ['H'],
    'H': ['G'],
    'F': ['G'],
    'G': []
}

# ---- heuristic values h(n) from your notes ----
h = {
    'A': 25,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'H': 10,
    'F': 7,
    'G': 0
}

print("Greedy Best First Search — Problem 1")
greedy_best_first(graph, h, start='A', goal='G')
# -------- Greedy Best First Search — Problem 2 --------

import heapq

def greedy_best_first(graph, h, start, goal):
    pq = [(h[start], start, [start])]
    visited = set()

    while pq:
        _, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            print("Visited Order :", visited)
            print("GBFS Path      :", " -> ".join(path))
            return

        for neigh in graph[node]:
            heapq.heappush(pq, (h[neigh], neigh, path + [neigh]))

    print("No path found")


# ---- graph edges from your notebook ----
graph = {
    'P': ['R', 'C', 'A'],
    'R': ['E', 'C'],
    'E': ['U', 'S'],
    'C': ['U', 'M'],
    'A': ['C', 'M'],
    'M': ['U', 'J'],
    'J': ['N'],
    'U': ['S', 'N'],
    'N': ['S'],
    'S': []
}

# ---- heuristic values h(n) (use values from your page) ----
h = {
    'P': 4,
    'R': 4,
    'E': 5,
    'C': 6,
    'A': 3,
    'M': 2,
    'J': 5,
    'U': 4,
    'N': 6,
    'S': 0
}

print("Greedy Best First Search — Problem 2")
greedy_best_first(graph, h, start='P', goal='S')
