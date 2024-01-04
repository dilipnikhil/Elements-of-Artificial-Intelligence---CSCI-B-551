#!/usr/local/bin/python3
#
# mystical_castle.py : a maze solver
#
# Submitted by : Dilip Nikhil Francies, dfranci
#
# Based on skeleton code provided in CSCI B551, Fall 2023.

import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(castle_map, row, col):
    moves = [(row+1, col), (row-1, col), (row, col-1), (row, col+1)]
    return [move for move in moves if valid_index(move, len(castle_map), len(castle_map[0])) and (castle_map[move[0]][move[1]] in ".@")]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the castle map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

""" 
Approach - To find the shortest path in a maze from "p" to "@" while navigating through empty spaces "." I have used a Breadth first Seearch Algorithm.
 """
def search(castle_map):
    # Find current start position
    current_loc = [(row_i, col_i) for col_i in range(len(castle_map[0])) for row_i in range(len(castle_map)) if castle_map[row_i][col_i] == "p"][0]
    fringe = [(current_loc, '', 0)]
    visited_node = set()
    while fringe:
        (current_loc, current_path, current_dist) = fringe.pop()
        visited_node.add(current_loc)
        for move in moves(castle_map, *current_loc):
            if move not in visited_node:
                fringe.append((move, current_path + getPath(move, current_loc), current_dist + 1))
        if castle_map[current_loc[0]][current_loc[1]] == "@":
            return (current_dist, current_path)     
    return (-1,'')


# function to obtain the direction of the move based on increment or decrement in the row and column value while navigating.
def getPath(move, current_loc):
    r = move[0] - current_loc[0]
    c = move[1] - current_loc[1]
    if r == 1:
        return 'D'
    elif r == -1:
        return 'U'
    elif c == 1:
        return 'R'
    elif c == -1:
        return 'L'


# Main Function
if __name__ == "__main__":
        castle_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(castle_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])

