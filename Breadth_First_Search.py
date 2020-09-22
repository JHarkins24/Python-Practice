class BFS:
    words =  ["try", "tim" , "tom" , "com", "toy" ,"cop","cuz","cob", "cup", "coy", "fry", "cry", "bay",
                  "lay", "boy", "bow","cow", "fey", "key","lop"]
    start = "boy"
    goal = "cup"
    found_goal = False
    fringe = []
    new_fringe = []
    solution_node = None
    limit = 0 

    def bfs(self):
        print("Breadth First Search")
        print(f"Start = {self.start}, goal = {self.goal}")
        print(f"words: {self.words}")
        start_node = self.Node(self.start,[])
        self.fringe.append(start_node)
        self.printFringe()
        while not self.found_goal and self.fringe:
            self.new_fringe = []
            for node_index in range(len(self.fringe)):
                curr_node = self.fringe[node_index]
                self.new_fringe.extend(self.evaluateNode(curr_node))

            self.fringe = self.new_fringe
            self.printFringe()
        
        print(f"Found goal = {self.found_goal}")
        if self.solution_node:
            self.solution_node.parents.append(self.goal)
            print(f"Solution path = {self.solution_node.parents}")

    def evaluateNode(self, curr_node):
        children = []
        if curr_node.word == self.goal:
            self.found_goal = True
            self.solution_node = curr_node
            children = []
            self.new_fringe = []
        else:
            children = self.successorFunc(curr_node)
        return children
       

    def successorFunc(self, curr_node):
        """
        Given a current node, finds all children.
        Returns a list of child nodes.
        """

        children = []
        childs_parents = curr_node.parents.copy()
        childs_parents.append(curr_node.word)
        for word in self.words:
            for charIndex in range(len(word)):
                modified_word = word
                if word != curr_node.word:
                    swapCharacter = curr_node.word[charIndex]
                    modified_word = self.changeStringChar(modified_word, charIndex, swapCharacter)
                    isUnique = word not in [child.word for child in children]
                    inParentList = word in curr_node.parents
                    inFringe = word in [node.word for node in self.fringe]
                    inNewFringe = word in [node.word for node in self.new_fringe]
                    if modified_word == curr_node.word and isUnique and not inParentList and not inFringe and not inNewFringe:
                        child_node = self.Node(word, childs_parents)
                        children.append(child_node)
                        break
        return children

    def changeStringChar(self, word, swap_index, swapCharacter):
        characters = list(word)
        characters[swap_index] = swapCharacter
        return "".join(characters)

    def printFringe(self):
        print("Fringe: ")
        for node in self.fringe:
            print(node.word)
        print("\n")

    class Node:
        word = None
        parents = []

        def __init__(self, word, new_parents):
            self.word = word
            self.parents = new_parents
        def display(self):
            print(f"word={self.word}")
            print(f"parents={self.parents}")


bfs = BFS()
bfs.bfs()
