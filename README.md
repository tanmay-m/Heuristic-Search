# tmahind-dbraj-vnayakan-a1

## Part1 
This problem deals with arranging the number of birds in order with only adjacent moves possible! This is a classic example to deal with heuristic search problems with handling multiple states in each levels. Here, we assign a cost of operation i.e the heuristic combined with the level cost which will give our total cost of operation. We push the states according to their cost and pop accordingly. Here, we divide the number of steps by 4 because each state will have 4 successors. To add a perfect digit of level cost, we divide the number of states by 4 and add to it to the total cost. Hence for level 1 with 4 nodes, we add 1, and for level 2 with 8 nodes, we add 2 and so on. While exploring, we keep appending the previous states which is the path taken to reach the goal state. We have used a heap-queue data structure to achieve this functionality. 

### Challenges faced
For the design of the heuristic function, we firstly came up with simply adding the number of misplaced birds. Later on we realized that for cases 12354 and 52341 have same number of misplaced birds but their number of steps to the goal are significantly different. Hence we used a different heuristic function which calculates the total distance of birds that needs to be changed in-order to correctly classify the above case. Next, we had an idea to perform the preferencing using a priority queue. After implementing, I noticed the execution time being a bit large. Hence we experimented by toggling the total cost as I observed that each level increment had a cost of total length and hence the unexplored branches were popped too late which reduced the execution time. Hence the divide by 4 factor came to play which helps to add only 1 cost to each level making it fair for all branches!

### Question/Answers
A1:The branching factor for our solution is 12N.
A2: For N = 7, in our A* search algorithm, we explore 12 successors. Hence to compute, we get 7*12 which gives us 84. So for breadth first search traversal, we explore 12^7 successors!

### Heuristic Function:
This function calculates the summation of all distances of misplaced positions of the bird from the original goal state positions. 
Heuristic of (12354) is 2!

### Cost Function:
The total cost function can be calculated as the cost of heuristic and the total number of states travelled i.e the traversal distance. In this way the the default cost increases at each increased level of traversal.

### Goal State:
The Goal state here is the defined as per the number of birds sitting in the ascending order. For N=5 the goal state would be 12345


## Part 2
This problem is just an extension to the Part1 where now we have a matrix with a twist of possible moves you can make. For the heuristic function, we used the manhattan distance to calculate the distance from the goal state. Hence the total cost here is just the summation of the manhattan distance and the cost required for each move. To achieve the priority popping of states, we used heap-queue. Every pop will have the next best state according to the total cost function which eventually explores all nodes with ascending order of the costs until the goal state is reached.

### Challenges:
For Part 2, we initially struggled with the heuristic function. Firstly, we counted the number of misplaced tiles. This move was helpful to find the solution for testcase 1 within a minute but was not a good match for other test cases. Struggling with the execution time, we modified our heuristic function to manhattan distance which worked wonders! Also to tweak more execution time, we initially had an priority queue implementation which later was changed to heap-queue to save those few seconds. 

### Heuristic Function:
We have used Manhattan distance to calculate the total distance required to the goal state. 


### Cost Function:
The total cost of this function is calculated by formulating the summation of heuristic function i.e the total Manhattan distance and the cost required to take each new step.

### Goal State:
The Goal state can be expressed as a sorted matrix of N elements. To be specific, elements are sorted from the top left to the bottom right.


## Part 3

## Challenges
First We approached this problem using priority queue but the time it was executing was very large so used heapq.
The heuristic i used before was not giving the right answer but after getting to learn about haversine distance from the internet heuristic helped me to solve this better.

### Theory and Challenges:
In this problem, we have used the heap approach for storing the best possible steps. For the heuristic function, we have used Haversine distance formula which is referred from online resources. This Haversine function computes the distance between two geo locations. Each time we find neighbors from the initial location based on the latitude and longitude and calculate the best possible way to reach towards the destination location using Haversine distance.  


### Heuristic function
Here we have used Haversine distance as a heuristic function to calculate distance between two geo locations.

### Total Cost:
The cost here is calculated by considering time, distance and speed with shortest path as all the factors of cost of reaching the destination in optimal time.

### Goal State:
Our main objective is to reach the end city in the optimal amount of time.
