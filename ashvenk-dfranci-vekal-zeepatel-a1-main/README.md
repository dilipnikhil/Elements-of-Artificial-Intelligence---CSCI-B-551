# ashvenk-dfranci-vekal-zeepatel-a1

#  Part 1

h(n) = Number of misplaced tile. was the first heuristic used. Later it was changed to 

h(n) =  len(path) ( number of moves taken ) + number of misplaced tiles. 

In both the cases the program reaches the correct goal state that too by taking the shortest path. But the moves are different.

Heapq was used instead of queue.  Visited node was added to keep a track of visited states. 

#  Part 2

## Question: To find the shortest sequence of moves that restores the canonical form of 5X5 grid numbers ranging from 1 to 25 in an ascending order given any possible combination of these numbers. The acceptable moves are L,R, U, D of every row and column respectively, and moves involving  Inner ring and outer ring moving clockwise and anticlockwise [Ic,Icc, Oc, OCC].

- **State space:** Every possible combination of these 25 numbers within the grid.

- **Initial state:** the given board configuraion.

- **Goal state:** Tiles arranged in a 5X5 grid in a sequential ascending order.

- **Successor function:** Performing a valid set of given moves to reach the next set of states at every level.

## Approach breakdown:

- An **A\* Algorithm** with heuristic as the sum of manhattan distance and len of path taken to reach that state, multiplied by a penalty parameter.
- **Data Structure:**  Heap queue 
- **Manhattan distance:** To calculate the distance to define how far the tile in the current state needs to travel to the goal state.

## We have used a multiple approaches combining different types cost functions, data structures and A star algorithm.

### First Approach

- **Cost function:**  g(n) - Manhattan distance

Using only Manhattan distance as a heuristc with A star algorithm led to the program not finding the right successor state out of 24 possible succesor states at every iteration. The manhattan distance was being added at each levels leading to sub-optimal solutions.

### SecondApproach
- **Cost function:**  g(n) - Number of misplaced tiles

Using only the number of tiles that were misplaced again led to inferior solutions

### Third approach
- **Cost Function:** g(n) - Constant heuristic = 1
Instead of choosing the state that had the minimum value of cost, we defined to use states that had costs less than a constant value [ <20, < 8, etc] which led to solutions that took plenty of time to converge as every possible state at every level that met the condition was being used to find the final solution. The program rached the goal state but the path was not shortest.

### Fourth approach
- **Cost Funtion:** g(n) - Number of tiles moved for every move. {R,L,U,D} = 5, {O} =16, {I}= 8
- The program was able to find the shortest path but it took 95-120 min.

### Fifth approach
- **Cost function:** g(n) =len of the path and h(n) multipled by 0.2.
But why use a penalty parameter?
To bring down the influence of the heuristic on the A start algorithm, which is of the crucial part of obtaining an optimal solution. 

But why 0.2? 
One can use any penalty parameter ranging from 0 to 1, but the lesser the value, the faster the convergence but might lead to a sub-optimal solution. Because it is mentioned in the question that 11 moves is an optimal one, playing around with the penalty parameter finally led us to a value of 0.2. Values such as 0.25. 0.3 have also given us similar results with different combinations of path taken to goal state.

## Question: In this problem, what is the branching factor of the search tree?

- Branching factor is defined as the number of possible moves that can be made from a particular state. We have Left and right combination for every row, and up and down combination for every column. We have two ways to move the inner ring and outer ring[clockwise and anticlockwise] . 

- Hence thats a total of (2 + 2 + 2 + 2+ 2 ) for all 5 rows

- 2 + 2 + 2 + 2+ 2 for all 5 columns

- 2 for outer ring

- 2 for inner ring

- Total: 24 moves. Hence the Branching Factor of the search tree is 24.

## Question: If the solution can be reached in 7 moves, about how many states would we need to explore before we found it if we used BFS instead of A* search? A rough answer is fine.

- At every level the branching factor is 24 as calculated.

- As the question mentions that the solution was found in 7 moves, then there would be 7 levels.Because BFS explores each of 24 states at every level for every 24 state that is calculated, then total possible number of moves at most would be  + 24 [1st level] + 24 * 24 [2nd level] + 24 *24*24 at third level .......... 24^7 at third level = 4785883224 states, and at least 23 + 24^2 + 24^3 ...... 24^6 + 1[first state in 7th level being the goal state] = 199411801.

#  Part 3

- State space: Cities and road segments in the US, southern Canada and northern Mexico.

- Initial state: The origin city.

- Goal state: The destination city.

- Successor function: Travelling from the current city to the next in the most optimal way based on the specified cost function.

## Approach:
- An **A\* Algorithm** with heuristic as the Euclidean distance with an approximate conversion factor taking into account the Earth's curvature.
- **Data Structure:** Heap queue 
- **Euclidean distance:** To calculate the cost between the next and destination city for the specified cost function - _segments, time, distance_ or _delivery_ in order to decide the successor for the next move.