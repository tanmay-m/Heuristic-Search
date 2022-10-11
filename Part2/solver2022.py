#!/usr/local/bin/python3
# solver2022.py : 2022 Sliding tile puzzle solver
#
# Code by: VNAYAKAN, TMAHIND, DBRAJ
#
# Based on skeleton code by D. Crandall & B551 Staff, Fall 2022
#
import numpy as np
import sys
import copy
import math
import heapq as hp

ROWS=5
COLS=5

def printable_board(board):
    return [ ('%3d ')*COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]


def move_right(state, row):
  """Move the given row to one position right"""
  state[row] = state[row][-1:] + state[row][:-1]
  return state

def move_left(board, row):
  """Move the given row to one position left"""
  board[row] = board[row][1:] + board[row][:1]
  return board

def rotate_right(board,row,residual):
    board[row] = [board[row][0]] +[residual] + board[row][1:]
    residual=board[row].pop()
    return residual

def rotate_left(board,row,residual):
    board[row] = board[row][:-1] + [residual] + [board[row][-1]]
    residual=board[row].pop(0)
    return residual

def move_clockwise(board):
    """Move the outer ring clockwise"""
    board[0]=[board[1][0]]+board[0]
    residual=board[0].pop()
    board=transpose_board(board)
    residual=rotate_right(board,-1,residual)
    board=transpose_board(board)
    residual=rotate_left(board,-1,residual)
    board=transpose_board(board)
    residual=rotate_left(board,0,residual)
    board=transpose_board(board)
    return board

def move_cclockwise(board):
    """Move the outer ring counter-clockwise"""
    board[0]=board[0]+[board[1][-1]]
    residual=board[0].pop(0)
    board=transpose_board(board)
    residual=rotate_right(board,0,residual)
    board=transpose_board(board)
    residual=rotate_right(board,-1,residual)
    board=transpose_board(board)
    residual=rotate_left(board,-1,residual)
    board=transpose_board(board)
    return board

# return a list of possible successor states
def successors(state):
    moves=[]
    for i in range(ROWS):
        moves.append(['R'+str(i+1),move_right(copy.deepcopy(state), i)])
        
    for i in range(ROWS):
        moves.append(['L'+str(i+1),move_left(copy.deepcopy(state), i)])
        
    for i in range(COLS):
        moves.append(['U'+str(i+1),transpose_board(move_left(transpose_board(copy.deepcopy(state)), i))])
        moves.append(['D'+str(i+1),transpose_board(move_right(transpose_board(copy.deepcopy(state)), i))])
    
    moves.append(['Oc',move_clockwise(copy.deepcopy(state))])
    
    moves.append(['Occ',move_cclockwise(copy.deepcopy(state))])
    
    
    state_Ic=np.array(copy.deepcopy(state))
    
    inner_state=state_Ic[1:-1,1:-1].tolist()
    inner_state = move_clockwise(inner_state)
    state_Ic[1:-1,1:-1]=np.array(inner_state)
    state_Ic=state_Ic.tolist()
    moves.append(['Ic',state_Ic])

    state_Icc=np.array(copy.deepcopy(state))
    inner_state=state_Icc[1:-1,1:-1].tolist()
    inner_state = move_cclockwise(inner_state)
    state_Icc[1:-1,1:-1]=np.array(inner_state)
    state_Icc=state_Icc.tolist()
    moves.append(['Icc',state_Icc])
    
    return moves

#tcalculate manhattan distance of each location in given board to its location in goal state and get the sum of those distances
def manhattan_dist(state):
    m_dist = []
    goal_state_dictionary={1:[0,0],2:[0,1],3:[0,2],4:[0,3],5:[0,4],
     6:[1,0],7:[1,1],8:[1,2],9:[1,3],10:[1,4],
     11:[2,0],12:[2,1],13:[2,2],14:[2,3],15:[2,4],
     16:[3,0],17:[3,1],18:[3,2],19:[3,3],20:[3,4],
     21:[4,0],22:[4,1],23:[4,2],24:[4,3],25:[4,4]}
    for i in range(5):
        a = []
        for j in range(5):
            k,l = goal_state_dictionary[state[i][j]]
            dist = math.fabs(i-k) + math.fabs(j-l)
            a.append(int(dist))
        m_dist.append(a)
    sum_manhattan = sum(sum(m_dist,[]))//ROWS
    return(sum_manhattan)

#First approach was using simple heuristict value that takes number of tiles misplaced to decide priroity of state in list of fringes
# This takes a lot of time as a lot of states are needed to explored to     
# def heuristic(state):
#     count=1
#     gstate=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
#     h=0
#     for i in range(ROWS):
#         for j in range(COLS):
#             if state[i][j]!=gstate[i][j]:
#                 h+=1
#     return h

# check if we've reached the goal
def is_goal(state):
    count=1
    gstate=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    for i in range(ROWS):
        for j in range(COLS):
            if gstate[i][j]!=state[i][j]:
                return False
    return True

def transpose_board(board):
  """Transpose the board --> change row to column"""
  return [list(col) for col in zip(*board)]

def solve(initial_board):
    
    state=[]
    k=0
    for i in range(ROWS):
        temp=[]
        for j in range(COLS):
            temp.append(initial_board[k])
            k+=1
        state.append(temp)
    initial_board=state
    
    fringe=[]
    fringe.append((0,0,initial_board,[]))
    hp.heapify(fringe)
    while fringe:
        cost,count,next_tstate,route=hp.heappop(fringe)
        if is_goal(next_tstate): 
            return route
        for transition_state in successors(next_tstate):
            u_board = transition_state[1] 
            n_step = transition_state[0]  
            h_ofN=manhattan_dist(u_board)
            cost = count + h_ofN
            u_route = route + [n_step]
            hp.heappush(fringe,(cost,count+1,u_board,u_route))
    return []

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
