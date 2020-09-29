#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:12:30 2020

@author: josephharkins
"""

graph = [['S','a','b'],['c','d','e'],['f','h','G']]
dict_cost = {'S':0, 'a':1,'b':1,'c':2,'d':2,'e':3,'f':3,'h':3,'G':1}
visited = [(0,0)]

class Node:
    def __init__(self, parent, x, y, cost):
        self.parent = parent
        self.x = x
        self.y = y
        self.cost = cost
    def __repr__(self):
        return "Char :" + graph[self.x][self.y] + "Cost :" + str(self.cost)
 
fringe = [Node(None,0,0,0)]    
 
def successor(current_node):
    visited.append((current_node.x, current_node.y))
    if(current_node.y + 1 < len(graph[0]) and (current_node.x, current_node.y + 1) not in visited):
        fringe.append(Node(current_node,current_node.x,current_node.y + 1, dict_cost[graph[current_node.x][current_node.y +  1]]))
    if(current_node.y - 1 > 0 and (current_node.x, current_node.y - 1) not in visited):
        fringe.append(Node(current_node,current_node.x,current_node.y - 1, dict_cost[graph[current_node.x][current_node.y -  1]]))
    if(current_node.x + 1 < len(graph) and (current_node.x + 1, current_node.y) not in visited):
        fringe.append(Node(current_node,current_node.x + 1,current_node.y, dict_cost[graph[current_node.x + 1][current_node.y]]))
    if(current_node.x - 1 > 0 and (current_node.x - 1, current_node.y) not in visited):
        fringe.append(Node(current_node,current_node.x - 1,current_node.y, dict_cost[graph[current_node.x - 1][current_node.y]]))
        
def getPlan(current_node):
    planString = graph[current_node.x][current_node.y]
    while current_node.parent is not None:
        planString = graph[current_node.parent.x][current_node.parent.y] + "-->" + planString
        current_node = current_node.parent
    print(planString)
    
def findLowestCost():
    lowestCost = fringe[0]
    for x in fringe:
        if x.cost < lowestCost.cost:
            lowestCost = x
    return lowestCost


current_node = fringe[0]

while(fringe and (graph[current_node.x][current_node.y] != 'G')):
    print(current_node)
    print(fringe)
    current_node = findLowestCost()
    successor(current_node)
    fringe.remove(current_node)
getPlan(current_node)
        