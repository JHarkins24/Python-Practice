# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

class Node:
    def __init__(self, row, column, euclidean_distance, manhatten_distance, parent, cost):
        self.row = row
        self.column = column
        self.euclidean_distance = euclidean_distance
        self.manhatten_distance = manhatten_distance
        self.parent = parent
        self.cost = cost
    def __repre__(self):
        return "cost : " + str(self.cost) + "(" + str(self.row) + "," + str(self.column) + ")"

graph =  [[0, 2, 3, 1, 1, -1, 3],
          [1, 1, -1, -1, 3, -1, 1],
          [3, 1, -1, 1, 1, 1, 1],
          [1, 1, 3, 4, 4, 1, 2],
          [1, 4, 2, 1, -1, 1, -2]]

goal_loc = (4,6)

start_loc = (0,0)

fringe = []

visited = []


#complete       
def goal_state(current_node):
    if graph[current_node.row][current_node.column] == goal_loc:
        return True
    else:
        return False   

#complete    
def isVisited(coords):
    if coords in visited:
        return True
    else:
        return False

#Complete may need to change row to x 
def findLeastEuclid():
    least = fringe[0]
    print(least)
    for row in fringe:
        if row.euclidean_distance < least.euclidean_distance:
            least = row
    return row

#Complete may need to change row to x 
def findLeastMan():
    least = fringe[0]
    for row in fringe:
        if row.manhatten_distance < least.manhatten_distance:
            least = row
    return row

#Complete 
def successor_func(current_node):
    visited.append((current_node.row, current_node.column))
    if current_node.row < len(graph) - 1 and not isVisited((current_node.row + 1, current_node.column)) and not graph[current_node.row + 1][current_node.column] == -1: #right
        fringe.append(Node(current_node.row + 1,current_node.column,eucl(current_node.row + 1, current_node.column),man(current_node.row + 1, current_node.column), current_node, graph[current_node.row + 1][current_node.column]))
    if current_node.column < len(graph[0]) - 1 and not isVisited((current_node.row, current_node.column + 1)) and not graph[current_node.row][current_node.column + 1] == -1: #down
        fringe.append(Node(current_node.row,current_node.column + 1,eucl(current_node.row, current_node.column + 1),man(current_node.row, current_node.column + 1), current_node, graph[current_node.row][current_node.column + 1]))
        
#complete
def get_plan(current_node):
    plan = ""
    cost = 0
    while current_node is not None:
        plan = str(current_node) + "" + plan
        cost = current_node.cost + cost
        current_node = current_node.parent
    return(plan, cost)

#both are complete
def eucl( row, column):
    return math.sqrt((goal_loc[0] - row)**2 + (goal_loc[1] - column)**2)

def man(row, column):
    return goal_loc[0] - row + goal_loc[1] - column



#--------------Main Method--------------#
startNode = Node(0,0,eucl(0,0),man(0,0),None,graph[0][0])


fringe.append(startNode)


while(not goal_state(findLeastEuclid())):
    successor_func(fringe.pop(fringe.index(findLeastEuclid())))

plan = get_plan(findLeastEuclid())
print(plan[0])
print(str(plan[1]))

fringe.clear()
fringe.append(startNode)

while(not goal_state(findLeastMan())):
    successor_func(fringe.pop(fringe.index(findLeastMan())))

plan = get_plan(findLeastMan())
print(plan[0])
print(str(plan[1]))















