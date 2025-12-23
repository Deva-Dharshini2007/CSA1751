# CSA1751
Artificial intelligence  
**Breadth First Search**
BEGIN

Initialize an empty queue Q

Mark the start node S as visited

Insert S into queue Q

While Q ≠ Ø, do

Remove the front node from Q and call it N

Process (visit) node N

For each adjacent node M of N, do
    a) If M is not visited, then
        i) Mark M as visited
        ii) Insert M into Q

End While

END

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


