import copy  
  
# Importing the heap methods from the python  
# library for the Priority Queue  
from heapq import heappush, heappop  
  
# This particular var can be changed to transform  
# the program from 8 puzzle(n=3) into 15  
# puzzle(n=4) and so on ...  
n = 3  
  
# bottom, left, top, right  
rows = [ 1, 0, -1, 0 ]  
cols = [ 0, -1, 0, 1 ]  
  
# creating a class for the Priority Queue  
class priorityQueue:  
      
    # Constructor for initializing a  
    # Priority Queue  
    def __init__(self):  
        self.heap = []  
  
    # Inserting a new key 'key'  
    def push(self, key):  
        heappush(self.heap, key)  
  
    # funct to remove the element that is minimum,  
    # from the Priority Queue  
    def pop(self):  
        return heappop(self.heap)  
  
    # funct to check if the Queue is empty or not  
    def empty(self):  
        if not self.heap:  
            return True  
        else:  
            return False  
  
# structure of the node  
class nodes:  
      
    def __init__(self, parent, mats, empty_tile_posi,  
                costs, levels):  
                      
        # This will store the parent node to the  
        # current node And helps in tracing the  
        # path when the solution is visible  
        self.parent = parent  
  
        # Useful for Storing the matrix  
        self.mats = mats  
  
        # useful for Storing the position where the  
        # empty space tile is already existing in the matrix  
        self.empty_tile_posi = empty_tile_posi  
  
        # Store no. of misplaced tiles  
        self.costs = costs  
  
        # Store no. of moves so far  
        self.levels = levels  
  
    # This func is used in order to form the  
    # priority queue based on  
    # the costs var of objects  
    def __lt__(self, nxt):  
        return self.costs < nxt.costs  
  
# method to calc. the no. of  
# misplaced tiles, that is the no. of non-blank  
# tiles not in their final posi  
def calculateCosts(mats, final) -> int:  
      
    count = 0  
    for i in range(n):  
        for j in range(n):  
            if ((mats[i][j]) and  
                (mats[i][j] != final[i][j])):  
                count += 1  
                  
    return count  
  
def newNodes(mats, empty_tile_posi, new_empty_tile_posi,  
            levels, parent, final) -> nodes:  
                  
    # Copying data from the parent matrixes to the present matrixes  
    new_mats = copy.deepcopy(mats)  
  
    # Moving the tile by 1 position  
    x1 = empty_tile_posi[0]  
    y1 = empty_tile_posi[1]  
    x2 = new_empty_tile_posi[0]  
    y2 = new_empty_tile_posi[1]  
    new_mats[x1][y1], new_mats[x2][y2] = new_mats[x2][y2], new_mats[x1][y1]  
  
    # Setting the no. of misplaced tiles  
    costs = calculateCosts(new_mats, final)  
  
    new_nodes = nodes(parent, new_mats, new_empty_tile_posi,  
                    costs, levels)  
    return new_nodes  
  
# func to print the N by N matrix  
def printMatsrix(mats):  
      
    for i in range(n):  
        for j in range(n):  
            print("%d " % (mats[i][j]), end = " ")  
              
        print()  
  
# func to know if (x, y) is a valid or invalid  
# matrix coordinates  
def isSafe(x, y):  
      
    return x >= 0 and x < n and y >= 0 and y < n  
  
# Printing the path from the root node to the final node  
def printPath(root):  
      
    if root == None:  
        return  
      
    printPath(root.parent)  
    printMatsrix(root.mats)  
    print()  
  
# method for solving N*N - 1 puzzle algo  
# by utilizing the Branch and Bound technique. empty_tile_posi is  
# the blank tile position initially.  
def solve(initial, empty_tile_posi, final):  
      
    # Creating a priority queue for storing the live  
    # nodes of the search tree  
    pq = priorityQueue()  
  
    # Creating the root node  
    costs = calculateCosts(initial, final)  
    root = nodes(None, initial,  
                empty_tile_posi, costs, 0)  
  
    # Adding root to the list of live nodes  
    pq.push(root)  
  
    # Discovering a live node with min. costs,  
    # and adding its children to the list of live  
    # nodes and finally deleting it from  
    # the list.  
    while not pq.empty():  
  
        # Finding a live node with min. estimatsed  
        # costs and deleting it form the list of the  
        # live nodes  
        minimum = pq.pop()  
  
        # If the min. is ans node  
        if minimum.costs == 0:  
              
            # Printing the path from the root to  
            # destination;  
            printPath(minimum)  
            return  
  
        # Generating all feasible children  
        for i in range(n):  
            new_tile_posi = [  
                minimum.empty_tile_posi[0] + rows[i],  
                minimum.empty_tile_posi[1] + cols[i], ]  
                  
            if isSafe(new_tile_posi[0], new_tile_posi[1]):  
                  
                # Creating a child node  
                child = newNodes(minimum.mats,  
                                minimum.empty_tile_posi,  
                                new_tile_posi,  
                                minimum.levels + 1,  
                                minimum, final,)  
  
                # Adding the child to the list of live nodes  
                pq.push(child)  
  
# Main Code  
  
# Initial configuration  
# Value 0 is taken here as an empty space  
initial = [ [ 1, 2, 3 ],  
            [ 5, 6, 0 ],  
            [ 7, 8, 4 ] ]  
  
# Final configuration that can be solved  
# Value 0 is taken as an empty space  
final = [ [ 1, 2, 3 ],  
        [ 5, 8, 6 ],  
        [ 0, 7, 4 ] ]  
  
# Blank tile coordinates in the   
# initial configuration  
empty_tile_posi = [ 1, 2 ]  
  
# Method call for solving the puzzle  
solve(initial, empty_tile_posi, final)


# LAB MANNUAL 4 | P a g e
# Assignment - 2
# TITLE :
# To study A star (A*) Algorithm
# OBJECTIVE :
# To understand the concept of A star (A*) Algorithm.
# PROBLEM STATEMENT:
# Implement A star (A*) Algorithm for any game search problem.
# ALGORITHM:
# A* Algorithm():
#  Add start node to list
#  For all the neighbouring nodes, find the least cost F node
#  Switch to the closed list
# o For 8 nodes adjacent to the current node
# o If the node is not reachable, ignore it. Else
#  If the node is not on the open list, move it to the open list and calculate f, g, h.
#  If the node is on the open list, check if the path it offers is less than the current path
# and change to it if it does so.
#  Stop working when
# o You find the destination
# o You cannot find the destination going through all possible points
# THEORY:
# A * algorithm is a searching algorithm that searches for the shortest path between the initial and the final
# state. It is used in various applications, such as maps.
# In maps the A* algorithm is used to calculate the shortest distance between the source (initial state) and the
# destination (final state).
# How it works
# Imagine a square grid which possesses many obstacles, scattered randomly. The initial and the final cell is
# provided. The aim is to reach the final cell in the shortest amount of time.
