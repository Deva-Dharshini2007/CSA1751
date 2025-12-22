import heapq

def a_star(graph, heuristic, start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return path, g

        if node in visited:
            continue

        visited.add(node)

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(pq, (new_f, new_g, neighbour, path + [neighbour]))

    return None


# Graph (node: [(neighbour, cost)])
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}

path, cost = a_star(graph, heuristic, 'A', 'G')
print("Path:", path)
print("Cost:", cost)
