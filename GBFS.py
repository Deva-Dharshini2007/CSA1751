import heapq

def gbfs(graph, start, goal, h):
    """
    graph : dict -> adjacency list, e.g., { 'A': ['B','C'], ... }
    start : starting node
    goal  : goal node
    h     : heuristic function as a dict, e.g., { 'A': 3, 'B': 2, ... }
    """
    visited = set()
    queue = []
    heapq.heappush(queue, (h[start], start))  # priority queue based on heuristic

    while queue:
        _, node = heapq.heappop(queue)

        if node == goal:
            print(f"Goal {goal} reached!")
            return

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (h[neighbor], neighbor))

# Example usage
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}

gbfs(graph, 'A', 'F', heuristic)
