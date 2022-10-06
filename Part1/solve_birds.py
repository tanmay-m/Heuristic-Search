#!/usr/local/bin/python3
# solve_birds.py : Bird puzzle solver
#
# Code by: Dhanush Bharath Raj dbraj
#
# Based on skeleton code by D. Crandall & B551 course staff, Fall 2022
#
# N birds stand in a row on a wire, each wearing a t-shirt with a number.
# In a single step, two adjacent birds can swap places. How can
# they rearrange themselves to be in order from 1 to N in the fewest
# possible steps?

# !/usr/bin/env python3
import sys

N=5

#####
# THE ABSTRACTION:
#
# Initial state:

# Goal state:
# given a state, returns True or False to indicate if it is the goal state
def is_goal(state):
    return state == list(range(1, N+1))

# Successor function:
# given a state, return a list of successor states
def successors(state):
    return [ state[0:n] + [state[n+1],] + [state[n],] + state[n+2:] for n in range(0, N-1) ]

#To Compare the Distances between the current and the goal state
def goal_state_pos(element):
    
    goal = [1,2,3,4,5]
    for i in range(len(goal)):
        if(element == goal[i]):
            return i
           
    return -1


# Heuristic function:
# given a state, return an estimate of the number of steps to a goal from that state
def h(state):
    
    huristic_value = 0
    for i in range(len(state)):
        
        #Calculating the huristic cost value by counting the total number of misplaced birds
        huristic_value += (abs(i - goal_state_pos(state[i])))
           
    return huristic_value

#########
#
# THE ALGORITHM:
#
# This is a generic solver using BFS. 
#
def solve(initial_state):
    fringe = []
    
    #Initializing some Constant variables 
    least = 99999
    prior_state = 0
    
    #Initializing the fringe with the state, path and Cost till that state
    fringe += [(initial_state, [], 0),]
    
    
    while len(fringe) > 0:
        
        #Popping the fringe with the maximum priority that is minimum cost value 
        (state, path, cost) = fringe.pop(prior_state)
        
        for i in range(len(fringe)):
            
            #Identifying the state in the fringe with least cost value and initializing it as the most prioritized one 
            (state_i,path_i,cost_i) = fringe[i]
            
            if(cost_i < least):
                least = cost_i
                prior_state = i
            
        
        if is_goal(state):
            return path+[state,]

        for s in successors(state):
            
            #Calculating the cost function that is f(x) = h(x) + g(x)
            cost = len(state) + h(state)
            
            #Appending all the possible successor states to the fringe
            fringe.append((s, path+[state,], cost))
            

    return []

# Please don't modify anything below this line
#
if __name__ == '__main__':
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a test case filename"))

    test_cases = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            test_cases.append([ int(i) for i in line.split() ])
    for initial_state in test_cases:
        	print('From state ' + str(initial_state) + " found goal state by taking path: " + str(solve(initial_state)))