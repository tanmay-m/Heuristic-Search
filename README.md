# tmahind-dbraj-vnayakan-a1

## Part1 
This problem deals with arranging the number of birds in order with only adjacent moves possible! This is a classic example to deal with heuristic search problems with handling multiple states in each levels. Here, we assign a cost of operation i.e the heuristic combined with the level cost which will give our total cost of operation. We push the states according to their cost and pop accordingly. Here, we divide the number of steps by 4 because each state will have 4 successors. To add a perfect digit of level cost, we divide the number of states by 4 and add to it to the total cost. Hence for level 1 with 4 nodes, we add 1, and for level 2 with 8 nodes, we add 2 and so on. While exploring, we keep appending the previous states which is the path taken to reach the goal state. We have used a heap-queue data structure to achieve this functionality. 

### Challenges faced
For the design of the heuristic function, we firstly came up with simply adding the number of misplaced birds. Later on we realized that for cases 12354 and 52341 have same number of misplaced birds but their number of steps to the goal are significantly different. Hence we used a different heuristic function which calculates the total distance of birds that needs to be changed in-order to correctly classify the above case. Next, we had an idea to perform the preferencing using a heap queue. After implementing the heap queue, I noticed the execution time being a bit large. Hence we experimented by using a priority-queue which reduced the execution time. The code for heap-queue is still commented in the solve() function for reference!


### Heuristic Function:
This function calculates the summation of all distances of misplaced positions of the bird from the original goal state positions. 
Heuristic of (12354) is 2!

### Cost Function:
The total cost function can be calculated as the cost of heuristic and the total number of states travelled i.e the traversal distance. In this way the the default cost increases at each increased level of traversal.

### Goal State:
The Goal state here is the defined as per the number of birds sitting in the ascending order. For N=5 the goal state would be 12345

