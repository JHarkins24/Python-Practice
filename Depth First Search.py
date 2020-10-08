# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:03:36 2020

@authors: luis Figueroa 
        Joe Harkins
"""


class DepthSearch:
    dictionary = ["try", "tim" , "tom" , "com", "toy" ,"cop","cuz","cob", "cup", "coy", "fry", "cry", "bay",
                  "lay", "boy", "bow","cow", "fey", "key","lop"]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    
    
    '''List of Nodes'''
    fringe = []

    "List of Nodes "
    vertices_links = []
    
    "List of str"
    visited_nodes = []
    
    
    def transform_word(self,start_word,goal_word):
    
    
        solution_found = False
    
        root_node = self.Node(start_word)
        self.vertices_links.append(root_node)
    
        self.fringe.append(root_node)
        self.dictionary.remove(start_word)
    
        while(len(self.fringe) != 0):
            self.displayList(self.fringe)

            current_node = self.fringe.pop()

       
            self.visited_nodes.append(current_node.data)
            
            if(self.check_goal(current_node)):
            
                solution_found = True
                print("\n\nPath :",self.findNode(current_node.data, self.vertices_links).ancestry)
                break;
            else:
                    self.successor(current_node)  
        print("Visited Nodes: ",self.visited_nodes)
        return solution_found
  
    
    '''ArgType:Node   Return:Boolean '''
    def check_goal(self,current_node):
        response = False
        if(current_node.data == goal_word):
            response = True
            return response
        
    '''ArgType: Node List  Return: Str list '''
    def displayList(self, nodeList):
        display = []
        for node in nodeList:
            display.append(node.data)
        print(display)
        
    '''ArgType: str, Node list  Return: Node '''    
    def findNode(self, node, nodeList):
        for item in nodeList:
            if(node == item.data):
                return item
            
            
    '''Arg:Node  Return: None '''        
    def successor(self,current_word):
    
        generated_nodes_count=0
        for i in range(len(current_word.data)):
            for char in self.alphabet:
                next_word = current_word.data[:i] + char + current_word.data[i+1:]
                if next_word in self.dictionary:
                    
                    new_node = self.Node(next_word)
                    new_node.parent = current_word
                    self.vertices_links.append(new_node)
                    
                    self.fringe.append(new_node)
                    generated_nodes_count+=1
                    self.dictionary.remove(next_word)
                    
                    new_node.ancestry = new_node.ancestry + "->" + current_word.ancestry
                    
        print("Generated nodes: ",generated_nodes_count)
        
          

    class Node:
            def __init__(self, data = None):
                self.data = data
                self.parent = None
                self.ancestry = data



start_word = "boy"
goal_word = "cup"
myBFS = DepthSearch()
print("Solution found " if myBFS.transform_word(start_word, goal_word) == True else "No Solution")


