# CSA1751
Artificial intelligence  

## BFS  ALGORITHM
 
Start

Initialize an empty queue and a visited set

Insert the start node into the queue

Mark the start node as visited

While the queue is not empty:

Remove the front node from the queue

Check if the node is the goal state

If goal is found, terminate search

Else, expand the node and generate all adjacent nodes

For each adjacent node not visited:

Mark it as visited

Insert it into the queue

If queue becomes empty and goal not found, report failure

Stop

 ## DFS ALGORITHM
  Start

Initialize an empty stack and a visited set

Push the start node onto the stack

While the stack is not empty:

Pop the top node from the stack

If node is not visited:

Mark it as visited

Check if it is the goal state

If goal is found, terminate search

Else, push all unvisited adjacent nodes onto the stack

If stack becomes empty and goal not found, report failure

Stop
 ## UCS AGORITHM
Start

Initialize a priority queue ordered by path cost

Insert the start node with cost = 0

Initialize an empty visited set

While the priority queue is not empty:

Remove the node with the lowest path cost

If node is the goal state, terminate search

If node is not visited:

Mark it as visited

Expand the node

For each successor:

Compute cumulative path cost

Insert successor into priority queue

If queue becomes empty and goal not found, report failure

Stop


 ## A star search
 
  Start

Initialize an open list (priority queue)

Initialize a closed list (visited nodes)

Insert the start node into open list with:

g(n) = 0

f(n) = g(n) + h(n)

While open list is not empty:

Select node with minimum f(n)

If node is the goal state, reconstruct path and stop

Move node from open list to closed list

Expand node and generate successors

For each successor:

Calculate g(n), h(n), and f(n)

If successor is not in closed list, add/update in open list

If open list becomes empty and goal not found, report failure

Stop

## Greedy breadth first search

Start

Initialize an open list implemented as a priority queue ordered by heuristic value h(n)

Insert the start node into the open list

Initialize an empty closed list

While the open list is not empty:

Select and remove the node with the minimum heuristic value

If the selected node is the goal state, terminate search

Add the node to the closed list

Expand the node to generate successor states

For each successor not in closed list, insert it into the open list

If the open list becomes empty and the goal is not found, report failure

Stop
## Mini max Algorithm

 Start

Represent the game as a game tree with nodes as game states

Assign utility values to terminal states

For a MAX node:

Select the maximum value from child nodes

For a MIN node:

Select the minimum value from child nodes

Propagate values upward in the tree

Choose the move with the optimal minimax value

Stop

## Alpha–Beta Pruning Algorithm

Start

Initialize α = −∞ and β = +∞

Traverse the game tree depth-first

For MAX node:

Update α = max(α, child value)

If α ≥ β, prune remaining branches

For MIN node:

Update β = min(β, child value)

If β ≤ α, prune remaining branches

Continue until terminal or pruned

Return optimal minimax value

Stop

## Decision Tree Algorithm

Start

Collect and preprocess the training dataset

Select the best attribute using a splitting criterion (Information Gain / Gini Index)

Create a decision node using the selected attribute

Partition the dataset based on attribute values

For each partition:

If all samples belong to the same class, create a leaf node

Else, repeat steps 3–6 recursively

Stop when no attributes remain or stopping condition is satisfied

Output the decision tree

Stop
## Neural Network
Start

Initialize network architecture (input, hidden, output layers)

Initialize weights and biases randomly

For each training sample:

Perform forward propagation to compute output

Calculate error using a loss function

Perform backpropagation to compute gradients

Update weights using gradient descent

Repeat training for multiple epochs

Stop when convergence criteria is met

Output trained neural network

Stop
## Sum of Integers from 1 to N
Start

Read value of N

If N = 0, sum = 0

Else add N to sum of (N−1)

Display sum

Stop
## Database with Name and DOB
Start

Store facts with name and date of birth

Accept name as query input

Search database for matching name

Display corresponding DOB

Stop
## Student–Teacher–Subject Code Database
Start

Store student, teacher, and subject code as facts

Accept query (student/teacher/subject)

Match query with database

Display related details

Stop
## Planets Database
Start

Store planet information as facts

Accept planet name as input

Search for planet in database

Display planet details

Stop
## Towers of Hanoi
Start

Read number of disks N

If N = 1, move disk directly

Else

Move N−1 disks from source to auxiliary

Move largest disk to destination

Move N−1 disks from auxiliary to destination

Display moves

Stop
## Bird Can Fly or Not
Start

Store bird and flying ability as facts

Accept bird name as input

Check if bird can fly

Display result (can fly / cannot fly)

Stop
## Family Tree
Start

Store parent relationships

Define rules for father, mother, sibling, grandparent

Accept family query

Infer relationship using rules

Display result

Stop
## Dieting System Based on Disease
Start

Store disease and diet recommendations

Accept disease name as input

Match disease with database

Suggest appropriate diet

Stop
## Monkey Banana Problem
Start

Define initial state (monkey, box, banana positions)

Define goal state (monkey gets banana)

Define valid actions (move, push box, climb)

Apply actions to reach goal

Display solution steps

Stop
## Fruit and Color Using Backtracking
Start

Store fruit–color pairs

Accept fruit or color as input

Use backtracking to find all matches

Display possible solutions

Stop
## Best First Search
Start

Initialize open list with start node

Select node with best heuristic value

Check if goal reached

Expand node and add successors

Repeat until goal found

Display solution path

Stop
## Medical DiagnosisStart

Store symptoms and diseases

Accept symptoms as input

Match symptoms with disease rules

Diagnose disease

Display result

Stop
## Forward Chaining
Start

Store facts and rules

Apply rules on known facts

Generate new facts

Repeat until goal is derived

Display inferred facts
## Backward Chaining
Start

Set goal to be proven

Search rules that conclude the goal

Prove required sub-goals

Match with known facts

If all sub-goals satisfied, goal is true

Stop
## Web Blog Using WordPress
Start

Create WordPress account

Create a new blog

Add title, headings, and content

Insert anchor tags and links

Publish blog

Stop
## Pattern Matching in Prolog
Start

Define facts representing valid patterns

Accept an input pattern from the user

Compare the input with stored patterns

If input matches any pattern, display “Pattern Matched”

Otherwise, display “Pattern Not Matched”

Stop
## Find Number of Vowels in Prolog
Start

Define vowel facts (a, e, i, o, u)

Accept a list of characters as input

Check the first character of the list

If it is a vowel, increment the count

Move to the next character in the list

Repeat steps until list becomes empty

Display total number of vowels

Stop




