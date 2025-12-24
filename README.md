# CSA1751
Artificial intelligence  

**BFS  ALGORITHM**
1. Represent the graph using an adjacency list.

2. Create an empty queue Q.

3. Create an empty list Visited.

4. Add A to Visited.

5. Enqueue A into Q.

6. While Q is not empty do:
   a. Dequeue a node from Q → CurrentNode.
   b. Visit CurrentNode.
   c. For each neighbor of CurrentNode do:
      i. If neighbor is not in Visited then:
         - Add neighbor to Visited.
         - Enqueue neighbor into Q.
      ii. End If
   d. End For

7. End While

8. End BFS
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

4. End DFS
