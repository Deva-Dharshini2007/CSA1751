# CSA1751
Artificial intelligence  

**BFS  ALGORITHM**
 
 1.Represent the graph using an adjacency list.

2. Create an empty queue Q.

3. Create an empty list Visited.

 4.Add A to Visited.

 5.Enqueue A into Q.

6. While Q is not empty do:
  a. Dequeue a node from Q → CurrentNode.
 
  b.Visit CurrentNode.
 
  c. For each neighbor of CurrentNode do:
  
  i. If neighbor is not in Visited then:
  
 7. Add neighbor to Visited.
  
 8. Enqueue neighbor into Q.
  ii. End If
  d. End For

 9.End While

 10.End BFS

   **DFS ALGORITHM**
  
1. Represent the graph using an adjacency list.

2. Create an empty set/list Visited.

3. Define a recursive function DFS(Node):
   a. Add Node to Visited.
   
   b. Visit Node.
   
   c. For each neighbor of Node in Graph do:

    i. If neighbor is not in Visited then:
    
    - Call DFS(neighbor)
     
      ii. End If

    d. End For

5. End DFS

  **UCS AGORITHM**

 1. Represent the graph using an adjacency list with edge costs.

2. Create an empty priority queue PQ (ordered by path cost).

3. Create an empty set/list Visited.

4. Insert StartNode into PQ with cost = 0.

5. While PQ is not empty do:
   a. Remove the node with the lowest path cost from PQ → CurrentNode.

    b. If CurrentNode is the goal node then:
     
      - Return the path and its cost.

    c. If CurrentNode is not in Visited then:
      i. Add CurrentNode to Visited.

    ii. Visit CurrentNode.

    iii. For each neighbor of CurrentNode in Graph do:
          - Calculate the total cost to reach neighbor.
          - Insert neighbor into PQ with its total cost.

    iv. End For

    d. End If

7. End While

8. End UCS

 **A star search**
 
 1. Represent the graph using an adjacency list with edge costs.

2. Define a heuristic function h(n) that estimates the cost from node n to the goal.

3. Create an empty priority queue PQ (ordered by f(n) = g(n) + h(n)),
   where g(n) is the actual path cost from the start node.

4. Create an empty set/list Visited.

5. Insert StartNode into PQ with:
        g(StartNode) = 0
        f(StartNode) = g(StartNode) + h(StartNode)

6. While PQ is not empty do:

   a. Remove the node with the lowest f(n) value from PQ → CurrentNode.

    b. If CurrentNode is the Goal node then:
            Return the optimal path and its total cost.

   c. If CurrentNode is not in Visited then:

   i. Add CurrentNode to Visited
   ii. Visit CurrentNode

   iii. For each neighbor of CurrentNode in Graph do:

     Calculate new_g = g(CurrentNode) + cost(CurrentNode → neighbor)
     Calculate new_f = new_g + h(neighbor)
     Insert neighbor into PQ with values (new_g, new_f)

   iv. End For

    d. End If

    End While

7. If goal is not found, return "No path exists".

End A* Search

**Greedy breadth first search**

1. Represent the graph using an adjacency list with edge costs or structure.

2. Define a heuristic function h(n) that estimates the distance from node n to the goal.

3. Create an empty priority queue PQ (ordered by heuristic value h(n)).

4. Create an empty set/list Visited.

5. Insert StartNode into PQ with priority = h(StartNode).

6. While PQ is not empty do:

   a. Remove the node with the lowest heuristic value → CurrentNode.

    b. If CurrentNode is the Goal node then:
            Return the path found to the goal.

   c. If CurrentNode is not in Visited then:

   i. Add CurrentNode to Visited
   ii. Visit CurrentNode

   iii. For each neighbor of CurrentNode in Graph do:

   - Calculate heuristic value h(neighbor)
   - Insert neighbor into PQ with priority = h(neighbor)

    iv. End For

   d. End If

   End While

7. If goal is not reached, return "Path not found".

End Greedy Best-First Search

