from collections import deque

def water_jug_bfs(capacity, target):
    """
    capacity : tuple -> (jug1_capacity, jug2_capacity)
    target   : int -> desired water amount in any jug
    """
    visited = set()
    queue = deque()
    
    # Each state: (jug1, jug2, path)
    queue.append((0, 0, []))
    
    while queue:
        jug1, jug2, path = queue.popleft()
        
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        
        # Check if we reached the target
        if jug1 == target or jug2 == target:
            print("Steps to reach target:")
            for step in path:
                print(step)
            print(f"Final state: Jug1={jug1}, Jug2={jug2}")
            return
        
        # Possible next moves
        next_states = [
            (capacity[0], jug2, path + ["Fill Jug1"]),
            (jug1, capacity[1], path + ["Fill Jug2"]),
            (0, jug2, path + ["Empty Jug1"]),
            (jug1, 0, path + ["Empty Jug2"]),
            (min(jug1 + jug2, capacity[0]), jug2 - min(jug1 + jug2, capacity[0] - jug1), path + ["Pour Jug2 -> Jug1"]),
            (jug1 - min(jug1 + jug2, capacity[1]), min(jug1 + jug2, capacity[1]), path + ["Pour Jug1 -> Jug2"])
        ]
        
        for state in next_states:
            if state[:2] not in visited:
                queue.append(state)

    print("No solution found.")

# Example usage
capacity = (4, 3)   # Jug1=4L, Jug2=3L
target = 2          # Desired amount
water_jug_bfs(capacity, target)
