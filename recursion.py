#recursive code

import sys
import itertools

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])


# Function to calculate the shortest pathway
def shortest_pathway(start_node, intermediate, end_node, distance):
    # Function will return the minimum pathway through start node, intermediate nodes, and end node. 
    # This will return shortest point of starting node, intermediate node and end node
    if 0 >= intermediate:
        # Testing all intermediate nodes 
        # -1 to represent NO_PATH 
        return min(shortest_pathway(start_node, intermediate - 1, end_node, distance),
                   shortest_pathway(start_node, intermediate - 1, intermediate, distance) +
                   shortest_pathway(end_node, intermediate, intermediate - 1, distance))
    # Base Case that removes NO_PATH
    else:
        return (distance[start_node][end_node])


# New Function for defining distance between nodes

def floyd(distance):
    # Base Case
    for start, end in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH)):
        #new call for distance in fct
        #Base case. This will call out NO_PATH
        #distance is pathway, classified as x 
        x = distance
        if distance[start][end] == 0:
            continue
          
        #Reach source through shortest destination
        distance[start][end] = shortest_pathway(start, end, MAX_LENGTH - 1, x)
        
        return distance

#Produces Matrix Graph through recursion
print(floyd(graph))