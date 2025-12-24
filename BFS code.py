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

def bfs(start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Start BFS from node 0
bfs(0)

from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

def bfs_shortest_path(start):
    visited = set()
    distance = {}
    queue = deque()

    visited.add(start)
    distance[start] = 0
    queue.append(start)

    while queue:
        node = queue.popleft()

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                distance[neighbour] = distance[node] + 1
                queue.append(neighbour)

    return distance

print(bfs_shortest_path(0))

from collections import deque

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}

def bfs_levels(start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            print(node, end=" ")

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        print()  # new line for each level

bfs_levels(0)


from collections import deque

graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: []
}

def bfs_disconnected():
    visited = set()

    for start in graph:
        if start not in visited:
            queue = deque()
            queue.append(start)
            visited.add(start)

            while queue:
                node = queue.popleft()
                print(node, end=" ")

                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)

bfs_disconnected()


