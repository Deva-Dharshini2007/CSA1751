# CSA1751
Artificial intelligence  
**Breadth First Search**
step 1: Represent the graph using an adjacency list

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}


Step 2: Create an empty set Visited

Step 3: Create an empty queue Q

Step 4: Add the start node to Visited

Step 5: Enqueue the start node into Q

Step 6: While Q is not empty, do the following:

Dequeue a node from Q and store it as CurrentNode

Visit (print) CurrentNode

For each neighbor of CurrentNode in the graph:

If the neighbor is not in Visited:

Add the neighbor to Visited

Enqueue the neighbor into Q

Step 7: Repeat until the queue becomes empty

Step 8: End BFS

**BFS SECOND ALGORITHM**
Represent the graph using an adjacency list

Create an empty queue Q

Create an empty set/list Visited

Add StartNode to Visited

Enqueue StartNode into Q

While Q is not empty do

  Dequeue a node from Q → CurrentNode

  Visit CurrentNode

  For each neighbor of CurrentNode in graph do

    If neighbor is not in Visited then

      Add neighbor to Visited

      Enqueue neighbor into Q

    End If

  End For

End While

End BFS

**BFS THIRD ALGORITHM**
Represent the graph using an adjacency list

Create an empty queue Q

Create an empty set/list Visited

Add StartNode to Visited

Enqueue StartNode into Q

While Q is not empty do

  Dequeue a node from Q → CurrentNode

  If CurrentNode equals TargetNode then

    Return Reachable

  End If

  For each neighbor of CurrentNode in graph do

    If neighbor is not in Visited then

      Add neighbor to Visited

      Enqueue neighbor into Q

    End If

  End For

End While

Return Not Reachable

End BFS

**BFS FOURTH ALGORITHM**
Represent the graph using an adjacency list

Create an empty queue Q

Create a dictionary/array Distance

Create an empty set/list Visited

Add StartNode to Visited

Set Distance[StartNode] = 0

Enqueue StartNode into Q

While Q is not empty do

  Dequeue a node from Q → CurrentNode

  For each neighbor of CurrentNode in graph do

    If neighbor is not in Visited then

      Add neighbor to Visited

      Set Distance[neighbor] = Distance[CurrentNode] + 1

      Enqueue neighbor into Q

    End If

  End For

End While

Return Distance[TargetNode]

End BFS

**Depth First Search**

BEGIN

Mark the start node S as visited

Process (visit) node S

For each adjacent node M of S, do
 If M is not visited, then
    a) Call DFS recursively with node M

End For

END

**Uniform Cost Search**

BEGIN

Initialize an empty priority queue OPEN

Insert start node S into OPEN with path cost = 0

Initialize an empty visited set CLOSED

While OPEN ≠ Ø, do
Remove the node N from OPEN having the minimum path cost
If N is the goal node, return the solution path and cost
If N is not in CLOSED, then
    a) Add N to CLOSED
    b) For each successor M of N, do
        i) Compute updated cost
        ii) Insert M into OPEN

End While

END
****A* Search Algorithm****
BEGIN

Create an empty priority queue OPEN

Create an empty list CLOSED

Insert start node S into OPEN with
path cost = 0 and evaluation value = heuristic of S

While OPEN is not empty do
Remove the node N from OPEN having the lowest evaluation value
If N is the goal node then
return the solution path
Add node N to CLOSED
For each successor M of node N do
a) Calculate new path cost as cost of N plus cost from N to M
b) Calculate evaluation value as new path cost plus heuristic of M
c) If M is not in OPEN and not in CLOSED then
insert M into OPEN with calculated values

End While

END

**Greedy Best First Search**
BEGIN

Initialize an empty priority queue OPEN

Insert the start node S into OPEN with heuristic valueh(s)

Initialize an empty visited list CLOSED

While OPEN ≠ Ø, do
5.1 Remove the node N from OPEN having the minimum heuristic value
5.2 If N is the goal node, return the solution path
5.3 Add node N to CLOSED
 For each successor M of N, do
    a) If M is not in OPEN and CLOSED, insert M into OPEN

End While

END


