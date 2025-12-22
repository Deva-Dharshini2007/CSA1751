from collections import deque
import heapq

# Graph representation
# For BFS & DFS → normal adjacency list
# For UCS → (node, cost)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

# ---------------- BFS ----------------
def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS:", end=" ")
    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour, _ in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print()

# ---------------- DFS ----------------
def dfs(start):
    visited = set()

    def dfs_recursive(node):
        visited.add(node)
        print(node, end=" ")

        for neighbour, _ in graph[node]:
            if neighbour not in visited:
                dfs_recursive(neighbour)

    print("DFS:", end=" ")
    dfs_recursive(start)
    print()

# -------- Uniform Cost Search --------
def ucs(start, goal):
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node == goal:
            print(f"UCS: Cost to reach {goal} = {cost}")
            return

        if node not in visited:
            visited.add(node)

            for neighbour, weight in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(priority_queue, (cost + weight, neighbour))

    print("Goal not reachable")

# ------------ Function Calls ----------
bfs('A')
dfs('A')
ucs('A', 'F')
