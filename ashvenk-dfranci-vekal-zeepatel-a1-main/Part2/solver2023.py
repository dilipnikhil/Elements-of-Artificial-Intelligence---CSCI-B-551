#!/usr/local/bin/python3
# solver2023.py : 2023 Sliding tile puzzle solver
#
# Code by: vekal-dfranci-ashvenk-zeepatel
#
# Based on skeleton code by B551 Staff, Fall 2023
#

import sys
import heapq

ROWS=5
COLS=5

def printable_board(board):
    return [ ('%3d ')*COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]


# return a list of possible successor states
def successors(state):
    state = list(state)
    successor_states = []
    temp = [state[0:5],state[5:10],state[10:15],state[15:20],state[20:]]
    
    for shift in [(1, "R"), (-1, "L"), (1, "D"), (-1, "U")]:
        for i in range(5):
            new_state = [row[:] for row in temp]
            
            if shift[1] in ("R", "L"):
                new_state[i] = new_state[i][-shift[0]:] + new_state[i][:-shift[0]]
            else:
                column = [row[i] for row in new_state]
                column = column[-shift[0]:] + column[:-shift[0]]
                for j in range(5):
                    new_state[j][i] = column[j]
            
            m = new_state[0] + new_state[1] + new_state[2] + new_state[3] + new_state[4]
            successor_states.append((tuple(m), shift[1] + str(i + 1)))

    outer_ring = [0,1,2,3,4,9,14,19,24,23,22,21,20,15,10,5]
    temp = [state[i] for i in outer_ring]

    temp1 = temp[1:] + temp[:1]
    state1 = state.copy()
    
    for i,j in enumerate(outer_ring):
         state1[j] = temp1[i]

    successor_states+=[(tuple(state1),"Occ")]
    
    temp1 = temp[-1:]+temp[:-1]
    for i,j in enumerate(outer_ring):
         state1[j] = temp1[i]

    successor_states+= [(tuple(state1),"Oc")]

    inner_ring = [6,7,8,13,18,17,16,11]
    temp = [state[i] for i in inner_ring]

    temp1 = temp[1:] + temp[:1]
    state1 = state.copy()

    for i,j in enumerate(inner_ring):
         state1[j] = temp1[i]

    successor_states+= [(tuple(state1),"Icc")]

    temp1 = temp[-1:]+temp[:-1]
    for i,j in enumerate(inner_ring):
         state1[j] = temp1[i]

    successor_states+= [(tuple(state1),"Ic")]

    return successor_states

# check if we've reached the goal
def is_goal(state):
    if state == tuple(range(1, (ROWS*COLS)+1)):
        return True
    return False

def h(state):
    result = 0
    for i in range(len(state)):
        target = state[i] - 1
        result += abs(i // 5 - target // 5) + abs(i % 5 - target % 5)
    return result*0.2


def solve(initial_board):
    """
    1. This function should return the solution as instructed in assignment, consisting of a list of moves like ["R2","D2","U1"].
    2. Do not add any extra parameters to the solve() function, or it will break our grading and testing code.
       For testing we will call this function with single argument(initial_board) and it should return 
       the solution.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """
    fringe = []
    visited = set()
    
    path = []
    heapq.heappush(fringe, ( 0 , (initial_board,path) ) )

    while fringe:
        
        _, (state, path) = heapq.heappop(fringe)
        
        for s in successors(state):
            if is_goal(s[0]):
                return path+[s[1]]
            else:
                if s[0] not in visited: 
                    visited.add(s[0])
                    
                    hv = h(s[0])+len(path) 
                    
                    heapq.heappush(fringe, (hv ,(  s[0], path+[s[1]]) ))
    
    return []

# Please don't modify anything below this line
#
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    if len(start_state) != ROWS*COLS:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state))
    
    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))
