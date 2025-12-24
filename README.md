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
