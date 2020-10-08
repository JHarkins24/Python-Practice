# Lab 6
# Author: @Min Ahn @Pierre Smith @Joe Harkins
# October 1, 2020

from copy import deepcopy
maxPath = []
minPath = []

class Node:
    def __init__(self, data, child, isMax):
        self.data = data
        self.child = child
        self.isMax = isMax 
    def __repr__(self):
        string = "Data:" + str(self.data) + " max?: " + str(self.isMax) 
        return string


def findSuccessors(currList,  isMax):
    successor = []
    if len(currList) > 1:
        successor.append(Node(currList[0], None, isMax))
        successor.append(Node(currList[-1], None, isMax))
    return successor


def player(currList, isMax, depth):
    if isMax:
        value = float('-inf')
    else:
        value = float('inf')
    valueNode = None
    
    successor = findSuccessors(currList, isMax)
        
    if not successor:
        if isMax:
            value = currList[0]
        else:
            value = 0
        valueNode = Node(currList[0], None, isMax)
    
    for element in successor:
        tempList = deepcopy(currList)
        if successor.index(element) == 1:
            tempList = tempList[0:-1]
        else:
            tempList = tempList[1:]
        temp = player(tempList,  not isMax, depth + 1)
        if isMax:
            if  value < temp[0] + element.data:
                value = temp[0] + element.data
                valueNode = element
                valueNode.child = temp[1]
        else:
            if  value > temp[0]:
                value = temp[0]
                valueNode = element
                valueNode.child = temp[1]
    return (value, valueNode)


def findWinner(currNode):
    maxVal = 0
    minVal = 0
    while currNode is not None:
        if currNode.isMax:
            maxVal += currNode.data
        else:
            minVal += currNode.data
        currNode = currNode.child
    print("Max Player score is:", maxVal)
    print("Min Player score is:", minVal)
    if maxVal < minVal:
        print("Min wins!")
    elif minVal < maxVal:
        print("Max wins!")
    else:
        print("Its a tie!")
    print()


#~~~~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~#        
numbers = [1, 10, 9, 10, 10, 10,  -1]
print("For the board: ")
print(numbers)
game = player(numbers, True, 0)
findWinner(game[1])

numbers = [1,2,5,2]
print("For the board: ")
print(numbers)
game = player(numbers, True, 0)
findWinner(game[1])

