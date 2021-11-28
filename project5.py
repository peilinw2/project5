"""
Math 560
Project 5
Fall 2021

Partner 1: Amy Wang (pw137)
Partner 2: Lu Liu (ll394)
Date:
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
"""
def kruskal(adjList, edgeList):
    ##### Your implementation goes here. #####
    X = []
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
    ##### Your implementation goes here. #####
    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):
    ##### Your implementation goes here. #####
    tour = []
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
