#!/usr/local/bin/python3
# solve_birds.py : Bird puzzle solver
#
# Code by: TANMAY GIRISH MAHINDRAKAR: TMAHIND, DHANUSH BHARATH RAJ: DBRAJ
#
# Based on skeleton code by D. Crandall & B551 course staff, Fall 2022
#
# N birds stand in a row on a wire, each wearing a t-shirt with a number.
# In a single step, two adjacent birds can swap places. How can
# they rearrange themselves to be in order from 1 to N in the fewest
# possible steps?

# !/usr/bin/env python3
import sys
from queue import PriorityQueue

N=5

#####
# THE ABSTRACTION:
#
# Initial state:

# Goal state:
# given a state, returns True or False to indicate if it is the goal state
def is_goal(state):
    return state == list(range(1, N+1))

def give_goal_state():
    return list(range(1,N+1))

# Successor function:
# given a state, return a list of successor states
def successors(state):
    return [ state[0:n] + [state[n+1],] + [state[n],] + state[n+2:] for n in range(0, N-1) ]

# Heuristic function:
# given a state, return an estimate of the number of steps to a goal from that state

def goal_state_pos(element):
    goal = give_goal_state()
    for i in range(len(goal)):
        if(element == goal[i]):
            return i
           
    return -1

def h(state):
    heuristic_value = 0
    for i in range(len(state)):
        
        #Calculating the huristic cost value by counting the total number of misplaced birds
        heuristic_value += (abs(i - goal_state_pos(state[i])))
           
    return heuristic_value


#########
#
# THE ALGORITHM:
#
# This is a generic solver using BFS. 
#
def solve(initial_state):
    fringe =  PriorityQueue()
    fringe.put((0, initial_state, []))
    while fringe:
        (heuristic, state, path) = fringe.get()
        if is_goal(state):
            return path+[state,]
        for s in successors(state):
            fringe.put((h(s), s, path+[state,]))
            #print(fringe)

    return []

# Please don't modify anything below this line
#
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a test case filename"))

    test_cases = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            test_cases.append([ int(i) for i in line.split() ])
    for initial_state in test_cases:
        print('From state ' + str(initial_state) + " found goal state by taking path: " + str(solve(initial_state)))


    


    

