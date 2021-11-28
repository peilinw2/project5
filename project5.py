"""
Math 560
Project 5
Fall 2021

Partner 1: Amy Wang (pw137)
Partner 2: Lu Liu (ll394)
Date: 11/28/2021
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm

inputs: 
  adjList: list of vertices
  adjMat: matrix that contains distances between vertices

outputs: none
"""
def prim(adjList, adjMat):

# initialize the cost to infinite and previous vertex to none.
    for vertex in adjList:
        vertex.prev = None
        vertex.cost = math.inf
        vertex.visited = False

# arbitrarily pick the start vertex and set the cost to 0
    start = adjList[0]
    start.cost = 0

#construct priority queue
    Q = PriorityQueue(adjList)

    while not Q.isEmpty():
        #visit the next unvisited vertex
        vertex = Q.deleteMin()
        vertex.visited = True
# for each edge in vertex.neigh
        for neighbor in vertex.neigh:
#if the edge leads out, update
            if not neighbor.visited:
                if neighbor.cost > adjMat[vertex.rank][neighbor.rank]:
                    neighbor.cost = adjMat[vertex.rank][neighbor.rank]
                    neighbor.prev = vertex
    return


################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
Inputs: 
adjList: the adjacency list for the map(a list of Vertex objects)
edgeList: the list of Edge objects for the map

Output: a list of edges that are in the MST
"""
def kruskal(adjList, edgeList):
# initialize all singleton sets for each vertex
    for v in adjList:
        makeset(v)
# initialize the empty MST
    X = []

# loop through the edges in increasing order
    for e in edgeList:
# if the min edge crosses a cut, add it to our MST
        u, v = e.vertices
        if not find(u). isEqual(find(v)):
            X.append(e)
            union(u, v)
           
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.

input: vertex
output: none
"""

def makeset(v):

    v.pi = v
    v.height = 0

    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

input: vertex
output: vertex's root vertex
"""
def find(v):

    while v != v.pi:
        v = v.pi

    return v.pi


"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
#first, find the root of the tree for u
#and the tree for v
    ru = find(u)
    rv = find(v)

#if the sets are already the same, return
    if ru == rv:
        return

#make shorter set point to taller set
    if ru.height > rv.height:
        rv.pi = ru 
    elif ru.height < rv.height:
        ru.pi = rv
#same height, break tie
    else:
        ru.pi = rv

#tree got taller, increment rv.height
        rv.height += 1
    return

################################################################################

"""
TSP
Inputs: list of vertices/the starting vertex.
Outputs: the optimal route that includes the path of vertices.
"""
def tsp(adjList, start):
  
#initialize stack and an empty list   
    tour = []
    stack = []
    
#set all vertex as unvisited 
    for vertex in adjList:
        vertex.visited = False
        
#append start to stack
    stack.append(start)

  # when stack is not empty
    while len(stack) != 0:
# Obtain the current Vertex
        current = stack.pop()

# visit the vertex that have not been visited
        if current.visited == False:
# if  it has not been visited
            current.visited = True
            tour.append(current.rank)

# push all neighbors into the stack
            for neigh in current.mstN:
                stack.append(neigh)

# Append start vertex into the tour
    tour.append(start.rank)
    
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
