# Elements of AI - dfranci-a0


# Problem -1 :
#### The goal of the problem statement is to find the shortest path between "p" a person, and the magical portal "@", with walls "X" and open spaces "."

#### The approach that i have taken in this code is to build a BFS algorithm that keeps traversing through the state space, defined by the maze that is provided.

## 1. 

*Search Abstraction*:

- *Set of Valid states*: A Valid State is the traversal of “p”  only through node “.” and not throguh walls “X”.

- *State Space*: The state space is the representation of rows and columns that are within the maze.

- *Initial State*: The Initial State is  N rows * M columns matrix that represents the maze in map that consists of a “p”, the starting point to reach the magical portal, the ending point “@”.

- *Goal State*: The goal state is reaching the "@" from "p".

- *Successor Function*: A successor function will move the “p” in any one valid direction when a “.” exists either in “U”,”R”,”L” or “D” hence returning a tuple of row and column of the next state.

- *Cost Function*: As the goal is to find the shortest path in the map, and the fact that there is no explicit cost function mentioned, and each traverstal takes up a unit of 1, one can assume 1 to be the cost function.

*Search Strategy*:
I have used a breadth-first search (BFS) strategy to find the shortest path between "p" and "@". The idea here is to traverse throguh the maze one unit at a time, in all possible direction, abiding by the rule that one cannot pass throguh the wall X, but only through open spaces. 
 
When traversing from a node, the nodes that are linked to it is first explored. Once the parent node is explored, its removed from the que, but the direction is stored in the memory. Similarly, all the visited nodes are added into a set, that way, a node that is explored is not visited again, which aas a result is a sure way of finding the shortest distance. Finally, when the current move in the code is the final destination "@", the direction that was used from the initial state "p" and the total distance covered in units is calculated and displayed.

---

### 2) Placing Turrets

The aim of this problem is to place turrets in the maze that obey a set of predefined conditions.:

*Search Abstraction*:

- *Set of Valid States:* Valid states for the problem statements are i.e. 2 “p’s” cannot be in the same row or column, if they are present in a same row or column, there must be an “X” between them. So the set of valid states is a set which satisfies all the constraints.

The code provides ways to place turrets'p' on a map while following specific rules.
- *State Space*: All possible setups of 'p', 'X' and '@' symbols, within which we need to place turrets 

- *Initial State*: It's the beginning layout of the state space with one turret 'p' , 'X' and '@'.

- *Goal State*: Placing k number of turrets satisfying the condition that it can be placed only in the places marked with ".", and also such that two turrets cannot be placed in the same row and colum without a wall "X" or "p" in between them. Additionally, they shouldnt be placed in the matrix diagonal.

- *Successor Function*: The successor function adds a new “p” to an empty node, i.e. “.”. Thus when successor function is called, there will the same number of states generated as many as the number of “.” are present in the current map of fringe.

- *Cost Function*: The cost function will be the cost required to generate a new successor , i.e. once it checks the next state, i.e. for “p” to traverse to “.”. As it can take 1 step at a time, the cost function will be 1 here per traversal.

*Search Algorithms*:
I've used a "depth-first search" algorithm" to  a search path all the way to the last node. The code starts from initial state "p"and starts exploring all setups by successors function until goal state is reached. 
Otherwise it goes to previous map tries another way. This is how backtacking is used.

We use a function to check for conflicts. It starts from the given location (row and column) and moves in the specified direction. While it's in the bounds of the castle map, it does the following:
If it encounters another turret ('p'), it returns False because this means there's a conflict.
If it encounters an obstacle ('X'), it returns True because the player's presence allows turret placement. 
If it encounters the player's location ('@'), it breaks the loop.

 is_safe_to_place function is used to find navigation of turrets . 
Left (0, -1): finds conflicts to left . Likewise Right- (0, 1). Up- (-1, 0). 
Down- (1, 0). (-1, -1)- top-left diagonal. (1, 1)- bottom-right. (-1, 1)-top-right. (1, -1)- bottom-left.

If at any stage the goal state is encountered, it will be returned. Thus, a new map with requested number of turrets in correct and valid positions is generated. If not, then the code return False.

These checks return true is conflicts doesnt exist and go ahead with placing 'p' at the location. Returns false otherwise.


